# Breach: Hidden Field Manipulation on Password Recovery

## Discovery & Exploit

While inspecting the password recovery form on the site, we noticed a hidden input field in the HTML code:

``<input type="hidden" name="mail" value="default@example.com">``

Using browser developer tools (`Right click > Inspect`), we manually changed the `value` attribute of this hidden field to an arbitrary email address under our control:

``<input type="hidden" name="mail" value="admin@target.com">``

We then submitted the password reset request with the modified value.

The application accepted the input without any client-side or server-side validation and responded with a success message, revealing a flag:

``The flag is : 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0``

## Vulnerability Details

This breach highlights a **common misuse of hidden form fields** to transmit security-sensitive data from the client to the server.

In this case, the server blindly trusted the hidden `mail` field submitted by the client, and allowed unauthorized manipulation of account-related functionality. This allowed us to impersonate another user during the password recovery process and extract the flag.

Related references:

- https://owasp.org/Top10/A04_2021-Insecure_Design/
- https://owasp.org/www-community/attacks/Hidden_Field_Manipulation
- https://portswigger.net/web-security/information-disclosure/exploiting-hidden-fields

## Remediation

To prevent this issue:

1. Never trust client-side input, including hidden fields.
2. Always validate critical user input on the server-side using known session or account data.
3. Avoid exposing any sensitive identifiers (email, user ID) in hidden fields.
4. Implement CSRF protection on form submissions.
5. Log and monitor anomalies in password recovery flows.

---
<table width="100%">
  <tr>
    <td align="left"><a href="../Breach03_*/Ressources/writeup.md">← Previous: Breach03</a></td>
    <td align="center"><a href="../../README.md">↑ Back to README</a></td>
    <td align="right"><a href="../Breach05_*/Ressources/writeup.md">Next: Breach05 →</a></td>
  </tr>
</table>
