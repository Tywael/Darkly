# Breach: Open Redirect via Unvalidated URL Parameter

## Discovery & Exploit

While exploring the footer of the website, we observed that the social media links pointed to an internal redirector:

``/redirect?site=https://facebook.com``  
``/redirect?site=https://twitter.com``  
...

This suggested that the application uses a local `redirect` page with a `site` parameter to forward users to external URLs.

We tested the behavior by changing the `site` parameter to an arbitrary value:

``/redirect?site=test``

Unexpectedly, instead of receiving an error or fallback behavior, the application responded with a message:

``Good Job Here is the flag : b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3``

This means that the application performs redirection based on user input without validating the destination, and that it even reveals sensitive information under specific conditions.

## Vulnerability Details

This vulnerability is known as an **Open Redirect** (or Unvalidated Redirect).

When an application allows users to specify external URLs for redirection without properly validating them, it opens the door to multiple risks:

- **Phishing**: attackers can craft links pointing to the legitimate domain, but which ultimately redirect to a malicious site.
- **Access Control Bypass**: as in this case, internal logic may inadvertently expose protected data when unexpected input is used.
- **SEO Manipulation**: abuse of the site's reputation to manipulate search engine ranking or indexing.

References:

- https://owasp.org/www-community/attacks/Unvalidated_Redirects_and_Forwards
- https://capec.mitre.org/data/definitions/160.html

## Remediation

To prevent this issue:

1. Avoid redirecting users based on URL parameters.
2. If redirection is required, only allow a predefined list of safe destinations (whitelist).
3. Use short, indirect redirect codes (e.g., `/redirect?id=2`) rather than exposing full URLs.
4. Always validate and sanitize user input.
5. Implement logging and monitoring to detect unexpected redirect patterns.
