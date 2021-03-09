# kemopq.freeipa_kolla collection plugins
Filters:
- gen_dc_suffix (Converts domain string in the following format: "first.second.third" --> "dc=first,dc=second,dc=third"
- filter_domain_list (Prepare list of openstack domains from "openstack domain list" JSON output)
- filter_project_list (Prepare list of openstack projects from "openstack project list" JSON output)
- filter_group_list (Prepare dict of openstack groups with ids from "openstack group list" JSON output)
