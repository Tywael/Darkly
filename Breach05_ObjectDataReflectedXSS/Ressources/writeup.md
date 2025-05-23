# Breach: Reflected XSS via Object Tag and Data URI

## Discovery & Exploit

While analyzing the homepage, we noticed that the "NSA" image was the only one that acted as a clickable link. Clicking it redirected us to the following URL:

``/?page=media&src=nsa``

This revealed two things:

- A `media` page exists
- It takes a `src` parameter, likely corresponding to an embedded resource

We experimented by changing the `src` value to something arbitrary:

``/?page=media&src=toto``

The page displayed a 404 message. Inspecting the HTML showed that the `src` value was inserted inside an `<object>` tag like so:

``<object data="toto"></object>``

This led us to investigate potential vulnerabilities related to the `<object data="">` attribute. Searching for known web exploits involving this pattern, we found that it's commonly vulnerable to **Reflected XSS**, especially when combined with `data:` URIs.

We tested this hypothesis by injecting a JavaScript payload directly into the URL:

``/?page=media&src=data:text/html,<script>alert(1)</script>``

And it worked — a browser alert was triggered.

While this already confirmed the vulnerability, further research led us to a more standardized attack vector documented by CAPEC:

https://capec.mitre.org/data/definitions/244.html

This reference suggested using Base64 encoding in the `data:` URI.

We then crafted the following payload:

``/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==``

Decoded, this represents:

``<script>alert(1)</script>``

When loaded, this version triggered the payload and displayed the flag:

``The flag is : 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d``

## Vulnerability Details

This is a classic example of **Reflected Cross-Site Scripting (XSS)** made possible through improper sanitization of user-controlled input passed into an HTML attribute.

Specifically, inserting attacker-controlled content inside the `data` attribute of an `<object>` tag — combined with a `data:` URI using a valid MIME type like `text/html` — allows full script injection and execution.

The vulnerability is especially severe because:

- No authentication is required
- No server response is needed to trigger the payload
- The payload is fully reflected into the DOM and executed client-side

References:

- https://owasp.org/www-community/attacks/xss/
- https://capec.mitre.org/data/definitions/244.html
- https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object#data

## Remediation

To mitigate this vulnerability:

1. Sanitize and validate all user input before inserting it into HTML attributes.
2. Reject or sanitize dangerous URI schemes like `data:`, `javascript:`, and `vbscript:` from user input.
3. Set appropriate Content Security Policy (CSP) headers to block inline scripts and dangerous sources.
4. Escape user input in HTML contexts using safe encoding techniques (e.g., OWASP’s ESAPI).
5. Use frameworks and libraries that auto-escape content and protect against injection attacks.

---

<table width="100%">
  <tr>
    <td align="left"><a href="../../Breach04_HiddenFieldEmailManipulation/Ressources/writeup.md">← Previous: Breach04</a></td>
    <td align="center"><a href="../../README.md">↑ Back to README</a></td>
    <td align="right"><a href="../../Breach06_OpenRedirectSiteParameter/Ressources/writeup.md">Next: Breach06 →</a></td>
  </tr>
</table>
