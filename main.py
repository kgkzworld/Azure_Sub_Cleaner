"""
    .DESCRIPTION
        Azure Subscription Cleanup Script

        The script is designed for Subscription cleanup and maintenance based on the configuration file.

        Configuration File:
            The configuration file is a YAML file that will manage the settings for the script.
            The configuration file will manage the following settings:
                - Subscription Information
                - Permissions
                - Maintenance Window

    .NOTES
        [Original Author]
            o Michael Arroyo
        [Original Build Version]
            o 1.0.0.20241216 (Major.Minor.Patch.Date<YYYYMMDD>)
        [Latest Author]
            o Michael Arroyo
        [Latest Build Version]
            o 1.0.1.20241216 (Major.Minor.Patch.Date<YYYYMMDD>)
        [Comments]
            o
        [Python Compatibility / Tested On]
            o Python 3.10.15
        [Forked Project]
            o
        [Dependencies]
            o os # The os module provides a way to use operating system dependent functionality
            o argparse # The argparse module makes it easy to write user-friendly command-line interfaces
            o rich # Rich is a Python library for rich text and beautiful formatting in the terminal

	.Build Notes
		o 1.0.0.20241216 -
			[Michael Arroyo] Initial Build
		o 1.0.1.20241216 -
			[Michael Arroyo] Update the Examples

	.Examples
	    o Example:
	        Command: python main.py --config ./config/Ares-Sec-Blue.yaml
	        Description: Run the Azure Subscription Cleanup process using te given configuration file (List Resource Groups Only)
	        Notes: This process will only run if the script is executed in the correct Maintenance windows defined in the configuration file
	        Output: N/A

	    o Example:
	        Command: python main.py --config ./config/Ares-Sec-Blue.yaml --bypass
	        Description: Run the Azure Subscription Cleanup process using te given configuration file
	        Notes: This process runs even outside the Maintenance Window (Note: Username and process is logged)
	        Output: N/A
"""
# region Import the required modules
## region Core Modules
import argparse
## endregion Core Modules

## region Import Third-Party Modules
from rich import print
## endregion Import Third-Party Modules
# endregion Import the required modules

def main(s_config, s_bypass):
    import os

    os.environ['s_config'] =  s_config
    os.environ['s_bypass'] = str(s_bypass)
    os.system("ipython main.ipynb")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Azure Subscription Cleanup Script")
    parser.add_argument('--config', type=str, required=False, help='Path to the YAML config file')
    parser.add_argument('--bypass', action='store_true', help='Bypass the maintenance window')
    parser.add_argument('--examples', action='store_true', help='Show Examples')

    args = parser.parse_args()
    if args.examples:
        print("""
o Example:
    Command: python main.py --config ./config/Ares-Sec-Blue.yaml
    Description: Run the Azure Subscription Cleanup process using te given configuration file (List Resource Groups Only)
    Notes: This process will only run if the script is executed in the correct Maintenance windows defined in the configuration file
    Output: N/A

o Example: 
    Command: python main.py --config ./config/Ares-Sec-Blue.yaml --bypass
    Description: Run the Azure Subscription Cleanup process using te given configuration file
    Notes: This process runs even outside the Maintenance Window (Note: Username and process is logged)
    Output: N/A
""")
        exit()
    elif args.config is None:
        print("""
usage: main.py [-h] --config CONFIG [--bypass BYPASS] [--examples EXAMPLES]

Azure Subscription Cleanup Script

options:
  -h, --help           show this help message and exit
  --config CONFIG      Path to the YAML config file
  --bypass BYPASS      Bypass the maintenance window
  --examples EXAMPLES  Show Examples
        """)
        exit()

    main(args.config, args.bypass)