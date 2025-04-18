# Project WEB SECURITY: Darkly

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Breaches](#breaches)

## Introduction

This repository documents the analysis and exploitation of 14 web vulnerabilities discovered during a controlled security lab named "Darkly", conducted as part of the curriculum at 42.

Each breach has been isolated and exploited to retrieve a flag, and is documented in a dedicated write-up.

The goal of this project is to demonstrate practical offensive techniques, provide clear documentation of each vulnerability, and suggest potential mitigations.

## Requirements

- VirtualBox or VMware
- Web browser
- [Lab ISO image](http://example.com/path/to/iso)

## Installation

1. Download the ISO and create a VMs from it on your virtualization platform.
2. Set the VM's network mode to **bridged adapter**. This will ensure that the VM is accessible on the same local network as your host machine.
3. Start the virtual machine.
4. Once booted, on the login page there will be the ip and port to the webserver. (you do not need to login to do this exercise)
5. Open your browser and navigate to the lab interface using that IP (e.g., `http://192.168.X.X`).

## Breaches

The repository is organized as follows:
```
├── README.md
├── Breach01/
│   ├── flag
│   └── Ressources/
│       ├── writeup.md
│       └── [scripts, payloads, etc.]
├── Breach02/
│   └── ...
├── ...
└── Breach14/
    ├── flag
    └── Ressources/
        ├── writeup.md
        └── ...
```


| Breach ID | Title             | Write-up                                      |
|-----------|------------------|-----------------------------------------------|
| 01        | ExposedHtpasswdCredentials     | [Breach01_ExposedHtpasswdCredentials/Ressources/writeups.md](Breach01_ExposedHtpasswdCredentials/Ressources/writeups.md) |

Each write-up includes:
- **Discovery & Exploit**: How the flag was obtained
- **Vulnerability Details**: Nature and classification of the vulnerability
- **Remediation**: Suggestions to fix or prevent the issue

## Notes

All tests were performed in an isolated environment.  
This repository is intended for educational and ethical purposes only.
