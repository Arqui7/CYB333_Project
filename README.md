# CYB333_Project
First Port scanner for project in class CYB333

Installation

To use the Port Scanner tool, follow these simple steps:

Clone the Repository: Start by cloning this repository to your local machine using Git:
"git clone https://github.com/your_username/CYB333_Project.git"

Navigate to the Directory: Move into the directory containing the Port Scanner script: cd CYB333_Project

Install Dependencies (Optional): There are no external dependencies required for this script, as it utilizes only Python's built-in socket module.

Run the Script: Execute the Python script by running the following command: python port_scanner.py
"Note: depending on what version of python you are using"


Usage

Once you have installed the Port Scanner tool, you can use it to scan ports on a target host. Follow these steps to perform a port scan:

Enter Target Host: When prompted, enter the IP address or hostname of the target host you want to scan.

Enter Port Range: Provide the starting and ending port numbers for the scan when prompted.

View Scan Results: The script will initiate the port scan and display the results, indicating which ports are open and which are closed.

Repeat as Needed: You can perform multiple scans by running the script again and providing new target hosts or port ranges.

Example

Here's an example of how to use the Port Scanner tool:

$ python port_scanner.py

Enter IP address or hostname: example.com

Enter the starting port number: 1

Enter the ending port number: 9000

Starting port scan on example.com...

Port 80 is open
Port 443 is open
Port 8080 is closed

In this example, the tool scans ports 1 to 100 on the host example.com and identifies that ports 80 and 443 are open, while port 8080 is closed.

Troubleshooting

If you encounter any issues while using the Port Scanner tool, consider the following troubleshooting tips:

Hostname Resolution Error: If the hostname provided cannot be resolved to an IP address, ensure that the hostname is spelled correctly and that the target host is reachable from your network.

Connection Timeout: If the script takes too long to complete or hangs during scanning, check your network connection and ensure that the target host is responsive.

Socket Errors: If you encounter socket errors during the scan, verify that your system's firewall settings allow outgoing connections to the target host's ports.
