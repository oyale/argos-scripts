# Argos Scripts Repository

This repository contains a collection of scripts designed for use with the [Argos GNOME extension](https://github.com/p-e-w/argos). These scripts provide quick and convenient access to various pieces of information directly from the GNOME top bar.

Each script is designed for a specific purpose and interacts with different systems or APIs. For example, we have a script that connects to an Odoo instance and retrieves the user's events for the day. Other scripts may interact with different APIs or services to provide various types of information.

## Scripts

| Script | Description |
| ------ | ----------- |
| [Odoo Events](./odoo-cal/README.md) | Connects to an Odoo instance and retrieves the user's events for the day, displaying them in the Argos dropdown. |

## Usage

To use a script, place it in the Argos plugin directory and ensure it has execute permissions. The Argos plugin will automatically load and execute the script, displaying the information in its dropdown menu.

## Contributing

If you have created a script for Argos that you think would be useful to others, please address to [argo's wiki](https://github.com/p-e-w/argos/wiki). The wiki is the official place to share useful scripts. 

Having said that, feel free to open a pull request to this repository. Your contributions are welcome!