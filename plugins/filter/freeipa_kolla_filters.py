#########################################
# freeipa_kolla collection's filters
#########################################

# Converts domain string in the following format:
# "first.second.third" --> "dc=first,dc=second,dc=third"
def gen_dc_suffix(domain):
    return ",".join(map(lambda x: "dc=" + x, domain.split(".")))


# filter: os_domain_list
# Prepare list of openstack domains from "openstack domain list" JSON output
def filter_domain_list(in_list):
    domain_list = []
    if type(in_list) is list:
        for domain in in_list:
            domain_list.append(domain['Name'])
    return domain_list


# filter: os_project_list
# Prepare list of openstack projects from "openstack project list" JSON output
def filter_project_list(in_list):
    project_list = []
    if type(in_list) is list:
        for project in in_list:
            project_list.append(project['Name'])
    return project_list


# filter: os_group_list
# Prepare dict of openstack groups with ids from "openstack group list" JSON output
def filter_group_list(in_list):
    group_list = {}
    if type(in_list) is list:
        for group in in_list:
            group_list[group['Name']] = group['ID']
    return group_list


# filter module
class FilterModule(object):
    def filters(self):
        return {
                'gen_dc_suffix': gen_dc_suffix,
                'os_domain_list': filter_domain_list,
                'os_project_list': filter_project_list,
                'os_group_list': filter_group_list
        }
