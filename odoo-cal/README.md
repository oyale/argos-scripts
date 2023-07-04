# Argos Odoo Events Script

This Python script is designed to work with the [Argos](https://github.com/p-e-w/argos/) plugin for GNOME Shell. It connects to an Odoo instance and retrieves the user's events for the day. The events are then displayed in the Argos plugin dropdown.

## Requirements

1. Python: This script is written in Python, so you need to have Python installed on your system to run it. It's recommended to use Python 3.7 or above.

2. OdooRPC: The script uses the OdooRPC library to interact with the Odoo API. You can install it using pip:

    ```bash
    pip install odoorpc
    ```

3. Argos: This script is designed to work with the Argos GNOME extension, which needs to be installed on your system. Visit [Argos's Github page](https://github.com/p-e-w/argos) for installation instructions.


## Configuration

To set up this script, you will need to provide your Odoo connection credentials. You can do this by either defining them in the script itself or by setting them as environment variables.

The variables to configure are:

- `ODOO_DOMAIN`: The domain of your Odoo instance.
- `ODOO_DB`: The name of your Odoo database.
- `ODOO_USER`: Your Odoo login user.
- `ODOO_PASSWORD`: Your Odoo login password.

If both environment variables and script variables are defined, the script variables will take precedence.

## Usage

Place the script in the Argos plugin directory and ensure it has execute permissions. The Argos plugin will automatically load and execute the script, displaying your events in its dropdown menu.
