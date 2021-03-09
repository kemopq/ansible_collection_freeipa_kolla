README.freeipa_kolla  
# kemopq.freeipa_kolla collection
Collection for integrating FreeIPA directory to kolla Openstack.  

### Installing collection  
Install this collection locally:
```
ansible-galaxy collection install kemopq.freeipa_kolla -p ./collections
```
_./collections_ folder should be included to _collections_path_ parameter in ansible configuration file. See:
https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings-locations

### Dependencies
The collection depends on freeipa.ansible_freeipa collection. That collection can also be used for IPA servers deployment 
(see the playbook on playbook folder)

### Using collection  
Roles and module can be used on your ansible playbook. It can be referenced by its fully qualified collection name (FQCN):
```
- name: Configure freeipa server
  hosts: ipaserver
  gather_facts: 'no'

  collections:
    - kemopq.freeipa_kolla

  tasks:
    - name: Import ipa_config role
      import_role:
        name: "ipa_config"

- name: Prepare Keystone and Horizon configuration files
  hosts: openstack_deployment_srv
  gather_facts: 'no'

  collections:
    - kemopq.freeipa_kolla

  tasks:
    - name: Import openstack_config role
      import_role:
        name: "openstack_config"

- name: Prepare openstack domains and projects
  hosts: openstack_client
  gather_facts: 'no'

  collections:
    - kemopq.freeipa_kolla

  tasks:
    - name: Import openstack_admin role
      import_role:
        name: "openstack_admin"
```

### Configuration parameters
Template of configuration file is in config folder. It's well commented. The configuration file has three parts:
- IPA configuration (default users and groups)
- kolla openstack configuration

### Inventory
Template of inventory file is in config folder. There are three types of server:
- openstack_deployment_srv => the server where kolla ansible playbooks run
- ipa_server => IPA server node
- openstack_client => A node, which has access to Openstack API URL and have openstack client package installed

### Running your playbook
When running your playbook a path to configuration file should be provided. Additionaly a parameter _freeipa_kolla_action_ parameter should be set. Possible values are:
- 'deploy': freeipa directory is integrated to kolla Openstack
- 'destroy': integration is removed
```
ansible-playbook  -i <inventory> -e freeipa_kolla_action=[deploy/destroy] -e "@<your_config_file>.json" <your_playbook>.yml
```

### Integration with kolla Openstack
- prepare IPA server
- deploy Openstack cloud with kolla-ansible playbooks
- make configuration of IPA server and Openstack using roles of this collection
- run kolla-ansible playbook with reconfigure option

### Basic test
On openstack client host:  
```
source admin-openrc.sh
openstack domain list
openstack group list --domain <ipa_domain>
openstack user list --domain <ipa_domain>
```

### Testing with molecule
Not prepaired yet
