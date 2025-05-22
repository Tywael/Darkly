# Breach: Access Control Bypass via Spoofed HTTP Headers

## Discovery & Exploit

While exploring the website, we clicked on the footer link labeled:

``© BornToSec``

This led us to a special page, seemingly static. Upon inspecting the HTML code of this page, we found a commented block within the source:

```html
<!-- 
  To access the hidden content, please make sure:
  - You are using the User-Agent: BornToSec
  - Your Referer is: https://www.borntosec.net
-->
```

This suggested that the server checks for specific HTTP headers before revealing content — namely:

- `User-Agent: BornToSec`
- `Referer: https://www.borntosec.net`

We used a tool (such as curl or a browser extension) to send a request to the page with these headers:

``curl -H "User-Agent: BornToSec" -H "Referer: https://www.borntosec.net" http://target/page``

Upon reloading the page with these custom headers, the hidden content became visible and revealed a flag:

``The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188``

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
