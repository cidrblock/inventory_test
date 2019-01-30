```
(venv) t25 ➜  inventory_test git:(master) ansible-playbook -i inventory/inventory.yml site.yml 

PLAY [all] **********************************************************************************************************

TASK [debug] ********************************************************************************************************
ok: [searouter1] => {
    "msg": [
        {
            "ip": {
                "address": "10.1.1.1/32"
            },
            "name": "loopback0",
            "ospf_enabled": false
        },
        {
            "description": "connection to searouter2",
            "ip": {
                "address": "10.1.2.1/30"
            },
            "name": "Ethernet0",
            "ospf_enabled": true
        },
        {
            "description": "connection to server",
            "name": "Ethernet2",
            "ospf_enabled": false,
            "vlan": "100"
        },
        {
            "description": "dg v100",
            "hsrp": {
                "address": "10.1.3.1/24",
                "group": 100
            },
            "ip": {
                "address": "10.1.3.2/24"
            },
            "name": "Vlan100",
            "ospf_enabled": false
        }
    ]
}
ok: [searouter2] => {
    "msg": [
        {
            "ip": {
                "address": "10.1.1.2/32"
            },
            "name": "loopback0",
            "ospf_enabled": false
        },
        {
            "description": "connection to searouter2",
            "ip": {
                "address": "10.1.2.2/30"
            },
            "name": "Ethernet0",
            "ospf_enabled": true
        },
        {
            "description": "connection to server",
            "name": "Ethernet2",
            "ospf_enabled": false,
            "vlan": "100"
        },
        {
            "description": "dg v100",
            "hsrp": {
                "address": "10.1.3.1/24",
                "group": 100
            },
            "ip": {
                "address": "10.1.3.3/24"
            },
            "name": "Vlan100",
            "ospf_enabled": false
        }
    ]
}

TASK [debug] ********************************************************************************************************
ok: [searouter2] => {
    "ospf": [
        {
            "areas": {
                "0": {
                    "networks": [
                        "10.1.2.0"
                    ],
                    "type": null
                }
            },
            "auto-cost": {
                "reference-bandwidth": 40000
            },
            "default-information": {
                "metric": 1000,
                "metric-type": 1,
                "originate": true
            },
            "distribute-list": {
                "direction": "in",
                "name": "dlist1",
                "type": "route-map"
            },
            "enabled_interfaces": [
                "Ethernet0"
            ],
            "log_adjacency_changes": true,
            "process_id": 100,
            "redistribute": {
                "bgp_65003": {
                    "AS": 65003,
                    "metric": 10,
                    "metric-type": 1,
                    "route-map": "rmap1",
                    "subnets": true,
                    "tag": 65003,
                    "type": "bgp"
                },
                "static": {
                    "subnets": true,
                    "type": "static"
                }
            },
            "router_id": "10.1.1.2",
            "vrf": "rh_lan"
        }
    ]
}
ok: [searouter1] => {
    "ospf": [
        {
            "areas": {
                "0": {
                    "networks": [
                        "10.1.2.0"
                    ],
                    "type": null
                }
            },
            "auto-cost": {
                "reference-bandwidth": 40000
            },
            "default-information": {
                "metric": 1000,
                "metric-type": 1,
                "originate": true
            },
            "distribute-list": {
                "direction": "in",
                "name": "dlist1",
                "type": "route-map"
            },
            "enabled_interfaces": [
                "Ethernet0"
            ],
            "log_adjacency_changes": true,
            "process_id": 100,
            "redistribute": {
                "bgp_65003": {
                    "AS": 65003,
                    "metric": 10,
                    "metric-type": 1,
                    "route-map": "rmap1",
                    "subnets": true,
                    "tag": 65003,
                    "type": "bgp"
                },
                "static": {
                    "subnets": true,
                    "type": "static"
                }
            },
            "router_id": "10.1.1.1",
            "vrf": "rh_lan"
        }
    ]
}

PLAY RECAP **********************************************************************************************************
searouter1                 : ok=2    changed=0    unreachable=0    failed=0   
searouter2                 : ok=2    changed=0    unreachable=0    failed=0   

(venv) t25 ➜  inventory_test git:(master) 
```