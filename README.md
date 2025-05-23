# Project WEB SECURITY: Darkly

## Table of Contents

- [Project WEB SECURITY: Darkly](#project-web-security-darkly)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Breaches](#breaches)
  - [Notes](#notes)

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
| 01        | ExposedHtpasswdCredentials     | [Breach01_ExposedHtpasswdCredentials](Breach01_ExposedHtpasswdCredentials/Ressources/writeups.md) |
| 02        | RecursiveReadmeEnumeration     | [Breach02_RecursiveReadmeEnumeration](Breach02_RecursiveReadmeEnumeration/Ressources/writeups.md) |
| 03        | WeakCookieAccessControl          | [Breach03_WeakCookieAccessControl](Breach03_WeakCookieAccessControl/Ressources/writeup.md) |
| 04        | HiddenFieldEmailManipulation     | [Breach04_HiddenFieldEmailManipulation](Breach04_HiddenFieldEmailManipulation/Ressources/writeup.md) |
| 05        | ObjectDataReflectedXSS           | [Breach05_ObjectDataReflectedXSS](Breach05_ObjectDataReflectedXSS/Ressources/writeup.md) |
| 06        | OpenRedirectSiteParameter        | [Breach06_OpenRedirectSiteParameter](Breach06_OpenRedirectSiteParameter/Ressources/writeup.md) |
| 07        | SpoofedHeaderAccessBypass        | [Breach07_SpoofedHeaderAccessBypass](Breach07_SpoofedHeaderAccessBypass/Ressources/writeup.md) |
| 08        | SQLi_Union_ExtractFlag           | [Breach08_SQLi_Union_ExtractFlag](Breach08_SQLi_Union_ExtractFlag/Ressources/writeup.md) |
| 09        | SQLi_DeepEnumerationFlagRebuild  | [Breach09_SQLi_DeepEnumerationFlagRebuild](Breach09_SQLi_DeepEnumerationFlagRebuild/Ressources/writeup.md) |
| 10        | SurveyValueBypass                | [Breach10_SurveyValueBypass](Breach10_SurveyValueBypass/Ressources/writeup.md) |
| 11        | DirectoryTraversalEtcPasswd      | [Breach11_DirectoryTraversalEtcPasswd](Breach11_DirectoryTraversalEtcPasswd/Ressources/writeup.md) |
| 12        | StoredXSSFeedbackForm            | [Breach12_StoredXSSFeedbackForm](Breach12_StoredXSSFeedbackForm/Ressources/writeup.md) |
| 13        | PasswordOnlyAuthBypass           | [Breach13_PasswordOnlyAuthBypass](Breach13_PasswordOnlyAuthBypass/Ressources/writeup.md) |
| 14        | FileUploadMIMESpoofing           | [Breach14_FileUploadMIMESpoofing](Breach14_FileUploadMIMESpoofing/Ressources/writeup.md) |


Each write-up includes:
- **Discovery & Exploit**: How the flag was obtained
- **Vulnerability Details**: Nature and classification of the vulnerability
- **Remediation**: Suggestions to fix or prevent the issue

## Notes

All tests were performed in an isolated environment.  
This repository is intended for educational and ethical purposes only.
