# Bulk add teams to workspace

## Overview

This script allows for adding teams to workspaces in bulk

## Installation

Clone this repository:

    git clone https://github.com/cadonuno/add-team-to-workspace.git

Install dependencies:

    cd add-team-to-workspace
    pip install -r requirements.txt

### Getting Started

It is highly recommended that you store veracode API credentials on disk, in a secure file that has 
appropriate file protections in place.

(Optional) Save Veracode API credentials in `~/.veracode/credentials`

    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>


### Preparing the Excel Template
    The Excel template present in the repository can be used to prepare the metadata, after the script finishes execution.
    the Status (third) column will contain the status of each line
    
### Running the script
    add-team-to-workspace.py -f <excel_file_with_workspaces_and_teams> [-d] [--use_team_id]"
        Reads all lines in <excel_file_with_workspaces_and_teams>, for each line, it will search for the column
        * Can optionally use team id's instead of names by passing the --use_team_id parameter

If a credentials file is not created, you can export the following environment variables:
    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
    python add-team-to-workspace.py -w <workspace_name> -t <team_name> [-d]

## License

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

See the [LICENSE](LICENSE) file for details
