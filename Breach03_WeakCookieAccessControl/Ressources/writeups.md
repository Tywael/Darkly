# Breach: Weak Cookie-Based Access Control (Client-Side Trust)

## Discovery & Exploit

While navigating the site, we opened the browser inspector (`Right click > Inspect Element`) and examined the `Storage > Cookies` section.

There, we found a cookie named:

``I_am_admin=68934a3e9455fa72420237eb05902327``

A quick Google search revealed that this MD5 hash corresponds to the value:

``false``

We suspected that the application might rely on this cookie value to determine user privileges. To test this hypothesis, we replaced the value with the MD5 hash of `true`, which is:

``b326b5062b2f0e69046810717534cb09``

After refreshing the page with this modified cookie, the application revealed a success message and a flag:

``Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3``


## Vulnerability Details

The vulnerability lies in the use of **client-side cookies for access control**, without any form of server-side validation or cryptographic integrity checking.

In this case, the application assumes that the value of the `I_am_admin` cookie is trustworthy. Since the value is a predictable MD5 hash (`false` → `6893...`), it is trivial for an attacker to guess and alter the hash to obtain elevated privileges (`true` → `b326...`).

This form of **client-side trust** is a critical security misconfiguration.

Related references:

- https://owasp.org/Top10/A05_2021-Security_Misconfiguration/
- https://owasp.org/www-community/Attacks/Manipulating_HTTP_Cookies
- https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html

## Remediation

To prevent this issue:

1. Never rely on client-side data (cookies, hidden fields, etc.) to control authorization logic.
2. Always verify privileges on the server side based on session state or secure tokens.
3. Avoid storing sensitive values or access indicators in cookies unless they are cryptographically signed (e.g., JWTs with validation).
4. Use HTTP-only and secure flags on cookies to reduce exposure.
5. Implement proper session management with backend validation mechanisms.
