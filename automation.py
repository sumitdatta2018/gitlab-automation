import requests


def get_projects():
    headers = {"Host": "localhost", "Authorization": "Bearer ASTfbsaLTYEZpM7VX8vz"}
    req = requests.get('http://localhost:9000/api/v4/projects', headers=headers)
    print(req.json())


def search_projects(project_name):
    headers = {"Host": "localhost", "Authorization": "Bearer ASTfbsaLTYEZpM7VX8vz"}
    req = requests.get('http://localhost:9000/api/v4/projects?scope=projects&search=' + project_name, headers=headers)
    return req.json()[0]


def update_project(project_name):
    headers = {"Host": "localhost", "Authorization": "Bearer ASTfbsaLTYEZpM7VX8vz"}
    found_project = search_projects(project_name)
    print(found_project['id'])
    project_id = found_project['id']
    data = {
        'merge_method': "rebase_merge",
        "resolve_outdated_diff_discussions": True,
        "remove_source_branch_after_merge": True,
        "only_allow_merge_if_all_discussions_are_resolved": True,
        "only_allow_merge_if_pipeline_succeeds": True,
        "squash_option": "always"
    }
    requests.put(url="http://localhost:9000/api/v4/projects/" + str(project_id), data=data, headers=headers)
    update_project_push_rule(project_id)


def update_project_push_rule(project_id):
    headers = {"Host": "localhost", "Authorization": "Bearer ASTfbsaLTYEZpM7VX8vz"}
    data = {
        'commit_committer_check': True,
        "deny_delete_tag": True,
        "prevent_secrets": True,
        "file_name_regex": True,
        "max_file_size": True
    }
    requests.put(url="http://localhost:9000/api/v4/projects/" + str(project_id) + "/push_rule", data=data,
                 headers=headers)


def get_groups():
    headers = {"Host": "localhost", "Authorization": "Bearer ASTfbsaLTYEZpM7VX8vz"}
    req = requests.get('http://localhost:9000/api/v4/groups', headers=headers)
    print(req.json())


if __name__ == '__main__':
    update_project('charter')
