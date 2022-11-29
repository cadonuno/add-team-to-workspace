import sys
import requests
import getopt
import json
import urllib.parse
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC

from veracode_api_signing.credentials import get_credentials

headers = {
    "User-Agent": "Dynamic Analysis API Example Client",
    "Content-Type": "application/json"
}


def print_help():
    """Prints command line options and exits"""
    print("""add-team-to-workspace.py -w <workspace_name> -t <team> [-d]"]
        Gives access to <workspace_name> to the <team> team
""")
    sys.exit()

def get_workspace_by_name(api_base, workspace_name, verbose):
    path = f"{api_base}srcclr/v3/workspaces?filter%5Bworkspace%5D={urllib.parse.quote(workspace_name, safe='')}"
    response = requests.get(path, auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    data = response.json()

    if verbose:
        print(data)

    if len(data["_embedded"]["workspaces"]) > 0:
        return find_exact_match(data["_embedded"]["workspaces"], workspace_name, "name")
    else:
        print(f"ERROR: No workspace named '{workspace_name}' found")
        sys.exit(1)

def get_team_by_name(api_base, team_name, verbose):
    path = f"{api_base}api/authn/v2/teams?all_for_org=true&team_name={urllib.parse.quote(team_name, safe='')}"
    response = requests.get(path, auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    data = response.json()

    if verbose:
        print(path)
        print(data)

    if len(data["_embedded"]["teams"]) > 0:
        return find_exact_match(data["_embedded"]["teams"], team_name, "team_name")
    else:
        print(f"ERROR: No team named '{team_name}' found")
        sys.exit(1)

def add_team_to_workspace(api_base, workspace_name, team_name, verbose):
    print(f"Looking for workspace: {workspace_name}")
    workspace = get_workspace_by_name(api_base, workspace_name, verbose)
    if workspace:
        workspace_guid = workspace["id"]
    else:
        print(f"ERROR: No workspace named '{workspace_name}' found")
        sys.exit(1)

    print(f"Looking for team: {team_name}")
    team = get_team_by_name(api_base, team_name, verbose);
    if team:
        team_id = team["team_legacy_id"]
    else:
        print(f"ERROR: No team named '{team_name}' found")
        sys.exit(1)
    
    path = f"{api_base}srcclr/v3/workspaces/{workspace_guid}/teams/{team_id}"

    if verbose:
        print(f"Calling {path}")

    response = requests.put(path, auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)

    if verbose:
        print(f"status code {response.status_code}")
        
    if response.status_code == 204:
        print("Successfully added team to workspace.")
        return True
    else:
        print(f"Unable to provide access to team: {response.status_code}")
        if verbose and response:
            body = response.json()
            if body:
                print(body)
        return False


def find_exact_match(list, to_find, field_name):
    for index in range(len(list)):
        if list[index][field_name] == to_find:
            return list[index]
    return -1
        
def get_api_base():
    api_key_id, api_key_secret = get_credentials()
    api_base = "https://api.veracode.{instance}/"
    if api_key_id.startswith("vera01"):
        return api_base.replace("{instance}", "eu", 1)
    else:
        return api_base.replace("{instance}", "com", 1)

def main(argv):
    """Simple command line support for creating, deleting, and listing DA scanner variables"""
    try:
        verbose = False
        workspace_name = ''
        team_name=''

        opts, args = getopt.getopt(argv, "hdw:t:",
                                   ["workspace=", "team="])
        for opt, arg in opts:
            if opt == '-h':
                print_help()
            if opt == '-d':
                verbose = True
            if opt in ('-w', '--workspace_name'):
                workspace_name=arg
            if opt in ('-t', '--team_name'):
                team_name = arg


        api_base = get_api_base()
        if workspace_name and team_name:
            add_team_to_workspace(api_base, workspace_name, team_name, verbose)
        else:
            print_help()

    except requests.RequestException as e:
        print("An error occurred!")
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
