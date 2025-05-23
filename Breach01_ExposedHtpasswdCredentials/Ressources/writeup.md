# Breach: ExposedHtpasswdCredentials

## Discovery & Exploit

While browsing the application, we checked for a `robots.txt` file at the root of the server:

```
http://{IP}/robots.txt
```

This file revealed the presence of a hidden path:

```
Disallow: /whatever
```

Navigating to `/whatever` exposed a file named `.htpasswd`. This file contained the following credentials:

```
http://{IP}/whatever/
root:437394baff5aa33daa618be47b75cb49
```


This format clearly resembles a typical `username:hashed_password` combo. Based on its structure and length, we suspected an MD5 hash.

After verifying, the hash was found in publicly known hash databases. Using a free MD5 reverse lookup tool.
```
https://md5.gromweb.com/?md5=437394baff5aa33daa618be47b75cb49
```
We were able to recover the original password:


```
qwerty123@ 
```

This gives us the credentials:

```
Username: root
Password: qwerty123@
```

Using these credentials on the `/admin` page allowed us to log in successfully and retrieve the [flag](../flag).

## Vulnerability Details

This breach is a combination of two poor security practices:

- **Sensitive path disclosure via robots.txt**  
  The `robots.txt` file is intended for search engine crawlers, not as a security mechanism. Including sensitive paths like `/whatever` essentially advertises them to attackers.

- **Insecure password storage**  
  The use of an unsalted MD5 hash for password storage is deprecated and insecure. MD5 is fast to compute and vulnerable to rainbow table attacks.

Related references:

- https://owasp.org/Top10/A01_2021-Broken_Access_Control/
- https://owasp.org/Top10/A04_2021-Insecure_Design/
- https://www.w3.org/TR/2019/WD-usecure-robots-20191119/

## Remediation

To prevent this issue:

1. Do **not include sensitive or hidden paths** in the `robots.txt` file.
2. Protect sensitive directories and configuration files through server configuration.
3. Avoid using `.htpasswd` files with weak or outdated hashing algorithms like MD5.
4. Use modern, salted password hashing algorithms (e.g., bcrypt, scrypt, Argon2).
5. Restrict access to administrative paths through authentication and proper access control.

---

<table width="100%">
  <tr>
    <td align="left">No Previous</td>
    <td align="center"><a href="../../README.md">↑ Back to README</a></td>
    <td align="right"><a href="../../Breach02_RecursiveReadmeEnumeration/Ressources/writeup.md">Next: Breach02 →</a></td>
  </tr>
</table>
