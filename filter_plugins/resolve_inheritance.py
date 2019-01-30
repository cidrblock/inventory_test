try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display #pylint: disable=C0412
    display = Display()

import json

def dump(obj):
    display.vvv(json.dumps(obj))

def deep_merge_lists(original, incoming):
    """
    Deep merge two lists. Modifies original.
    Reursively call deep merge on each correlated element of list.
    If item type in both elements are
     a. dict: call deep_merge_dicts on both values.
     b. list: Calls deep_merge_lists on both values.
     c. any other type: Value is overridden.
     d. conflicting types: Value is overridden.

    If length of incoming list is more that of original then extra values are appended.
    """
    common_length = min(len(original), len(incoming))
    for idx in range(common_length):
        if isinstance(original[idx], dict) and isinstance(incoming[idx], dict):
            deep_merge_dicts(original[idx], incoming[idx])

        elif isinstance(original[idx], list) and isinstance(incoming[idx], list):
            deep_merge_lists(original[idx], incoming[idx])

        else:
            original[idx] = incoming[idx]

    for idx in range(common_length, len(incoming)):
        original.append(incoming[idx])
    return original

def deep_merge_dicts(original, incoming):
    """
    Deep merge two dictionaries. Modifies original.
    For key conflicts if both values are:
     a. dict: Recursivley call deep_merge_dicts on both values.
     b. list: Calls deep_merge_lists on both values.
     c. any other type: Value is overridden.
     d. conflicting types: Value is overridden.

    """
    display.vvv(f"Original: {str(original)}")
    display.vvv(f"Original type: {type(original).__name__}")

    display.vvv(f"Incoming: {str(incoming)}")
    display.vvv(f"Incoming type: {type(original).__name__}")

    for key in incoming:
        if key in original:
            if isinstance(original[key], dict) and isinstance(incoming[key], dict):
                deep_merge_dicts(original[key], incoming[key])

            elif isinstance(original[key], list) and isinstance(incoming[key], list):
                deep_merge_lists(original[key], incoming[key])

            else:
                original[key] = incoming[key]
        else:
            original[key] = incoming[key]
    return original


def resolve_inheritance(original):
    dump(original)
    if isinstance(original, list):
        for entry in original:
            if 'inherit_from' in entry:
                entry = resolve_inheritance(entry)      
    elif isinstance(original, dict):
        if 'inherit_from' in original:
            if 'inherit_from' in original['inherit_from']:
                original['inherit_from'] = resolve_inheritance(original['inherit_from'])
            original = deep_merge_dicts(original, original['inherit_from'])
            original.pop('inherit_from')
    return original

class FilterModule(object):
    def filters(self):
        return {
            'resolve_inheritance': resolve_inheritance,
        }
