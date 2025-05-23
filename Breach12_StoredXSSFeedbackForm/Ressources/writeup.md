# Breach: Stored XSS in Feedback Form

## Discovery & Exploit

The feedback page includes a comment field, but no input validation or sanitization is applied.

Submitting any basic XSS payload in the `comment` field causes it to be stored server-side. When the page is reloaded, the comment is rendered without escaping, and the script is executed in the browser.

### Example payloads:

1. `<img src=x onerror=alert('XSS réussie')>`
2. `<svg/onload=alert('XSS')>`
3. `script` (WTF?)

These payloads are not only executed immediately after submission but also persist across page reloads.

Upon execution, the following message appears:

The [flag](../flag) is

## Vulnerability Details

This is a classic case of **Stored Cross-Site Scripting (XSS)**.

The application stores user input (comments) without sanitization, and then directly injects this content into the HTML DOM when rendering the feedback page. Any script included in the comment field is executed in the context of the user's browser when the page loads.

Stored XSS is particularly dangerous because it affects **all users** who view the infected page — not just the one who submitted the input.

References:

- https://owasp.org/www-community/attacks/xss/
- https://portswigger.net/web-security/cross-site-scripting/stored

## Remediation

1. Sanitize and encode all user input before rendering it in the browser.
2. Store only escaped/cleaned versions of user-submitted data.
3. Use frameworks or templating engines that auto-escape output.
4. Apply a strict Content Security Policy (CSP) to reduce XSS impact.
5. Review stored content periodically for unexpected or malicious input.

---

<table width="100%">
  <tr>
    <td align="left"><a href="../../Breach11_DirectoryTraversalEtcPasswd/Ressources/writeup.md">← Previous: Breach11</a></td>
    <td align="center"><a href="../../README.md">↑ Back to README</a></td>
    <td align="right"><a href="../../Breach13_PasswordOnlyAuthBypass/Ressources/writeup.md">Next: Breach13 →</a></td>
  </tr>
</table>
