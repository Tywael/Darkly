# Breach: Access Control Bypass via Spoofed HTTP Headers

## Discovery & Exploit

While exploring the website, we clicked on the footer link labeled:

``© BornToSec``

This led us to a special page, seemingly static. Upon inspecting the HTML code of this page, we found a commented block within the source:

This suggested that the server checks for specific HTTP headers before revealing content — namely:

- `User-Agent: ft_bornToSec`
- `Referer: https://www.nsa.gov`

We used the browser's developer tools to modify the request headers and added the required `User-Agent` and `Referer` headers.

Into the response, we found the [flag](../flag).:


## Vulnerability Details

This is a classic case of **Access Control through Obscurity**, relying on easily spoofable client-side headers.

Using `Referer` and `User-Agent` as mechanisms to authorize access to sensitive information is inherently insecure. These headers are entirely under the control of the client and can be modified using browser tools, proxies (e.g., Burp), or even `curl`.

References:

- https://owasp.org/www-community/controls/Access_Control
- https://owasp.org/Top10/A01_2021-Broken_Access_Control/

## Remediation

To prevent this vulnerability:

1. Never rely on `Referer`, `User-Agent`, or any client-controlled header to enforce access restrictions.
2. Implement proper server-side authentication and role-based access control (RBAC).
3. Ensure that hidden resources are protected by session checks or tokens, not obscurity.
4. Log access attempts with unusual or spoofed headers for auditing.

---

<table width="100%">
  <tr>
    <td align="left"><a href="../../Breach06_OpenRedirectSiteParameter/Ressources/writeup.md">← Previous: Breach06</a></td>
    <td align="center"><a href="../../README.md">↑ Back to README</a></td>
    <td align="right"><a href="../../Breach08_SQLi_DeepEnumerationFlagRebuild/Ressources/writeup.md">Next: Breach08 →</a></td>
  </tr>
</table>
