# Add team to workspace

## Overview

This script allows for adding teams to workspaces

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

### Running the script

    add-team-to-workspace.py -w <workspace_name> -t <team_name> [-d]
        Gives access to <workspace_name> to a team called <team_name>
        -workspace/-w: workspace_name
        -team/-t: team_name

If a credentials file is not created, you can export the following environment variables:

    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
    python add-team-to-workspace.py -w <workspace_name> -t <team_name> [-d]

## License

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

See the [LICENSE](LICENSE) file for details
