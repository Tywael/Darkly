# Breach: Insecure Directory Disclosure and Unprotected File Enumeration

## Discovery & Exploit

As in a previous case, the initial step was checking for a `robots.txt` file:

```
http://{IP}/robots.txt
```

Which revealed:

```
Disallow: /.hidden/
```

Visiting `/.hidden/` revealed a directory listing containing hundreds of folders and subfolders, sometimes deeply nested.

Manual exploration was quickly deemed impractical due to the sheer number of directories. We assumed the presence of a hidden `README` file somewhere within the tree, possibly containing a flag.

To solve this efficiently, we wrote a custom Python script using `requests`, `BeautifulSoup`, and `ThreadPoolExecutor` to crawl the entire `.hidden/` directory structure. The script does the following:

- Starts at `/.hidden/`
- Recursively follows all subdirectories
- Looks for any file containing "README" in its name
- Downloads and scans each README's content
- Stops automatically once a flag is found

The flag was successfully retrieved from one of the deepest folders in the hierarchy.

> The script used to automate this process is available here:  
> [`Ressources/find_readme.py`](./find_readme.py)


## Vulnerability Details

This vulnerability stems from multiple weaknesses:

- **Directory listing enabled**  
  Allowing attackers to view and enumerate the contents of server-side folders opens up unnecessary exposure.

- **Sensitive content in accessible locations**  
  Even with no direct link to these folders, the presence of `README` files containing secrets in browsable paths is a critical misconfiguration.

- **robots.txt leaking hidden paths**  
  As previously noted, `robots.txt` is not a security measure. By disclosing the `.hidden/` path, it effectively pointed us directly to the target.

References:

- https://owasp.org/www-community/Directory_Listing
- https://owasp.org/Top10/A05_2021-Security_Misconfiguration/
- https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

## Remediation

To prevent such issues:

1. Disable **directory listing** on the web server.
2. Avoid storing sensitive content like flags or credentials in web-accessible folders.
3. Do not expose internal or restricted paths in `robots.txt`.
4. Implement proper access control and authentication mechanisms for any confidential resource.
5. Use automated scanners to audit public paths for information leaks or misconfigurations.
