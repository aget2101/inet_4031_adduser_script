#!/usr/bin/env python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        # Skip lines starting with a hashtag
        if re.match(r'^#', line):
            continue
        
        # Split line into fields
        fields = line.strip().split(':')
        if len(fields) != 5:
            continue  # Skip lines that do not have exactly 5 fields
        
        username, password, lastname, firstname, groups = fields
        gecos = f"{lastname} {firstname},,,"
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        
        # Create user account
        print(f"==> Creating account for {username}...")
        os.system(cmd)
        
        # Set password for the user
        print(f"==> Setting the password for {username}...")
        cmd = f"echo '{password}:{password}' | sudo chpasswd {username}"
        os.system(cmd)
        
        # Assign groups, if any
        for group in groups.split(','):
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"
                os.system(cmd)

if __name__ == '__main__':
    main()

