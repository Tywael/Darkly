# Breach: Authentication Bypass via Password-Only Logic

## Discovery & Exploit

The login page prompted for a username and password, but provided no error messages to help distinguish incorrect usernames or passwords.

Initially, brute-forcing both the username and password would have been very time-consuming. We decided to narrow down our test set:

- **Usernames tested**:
  - `wil` (seen in feedback section)
  - `admin` (classic default)
  - `root` (seen in admin panel)

- **Passwords**:
  - We used a list of the 10,000 most common passwords

Using a small Python script to test every combination (see `login.py`), we found:

``wil:shadow`` → success → flag displayed

Out of curiosity, we also tested:

- `admin:shadow` → success  
- `root:shadow` → success  
- Even random usernames like `skjfgsdiugjfseidufgsdjkfgsdkjfghsd:shadow` → also worked

This confirmed that **only the password "shadow" was being checked**, and the username was completely ignored by the authentication logic.

## Vulnerability Details

This is a serious authentication flaw where the application verifies only the password field, ignoring the username entirely. This allows any user to authenticate using the correct password, regardless of the username used.

Such flaws are typically caused by:

- Bad comparison logic (e.g., checking password before matching username)
- Misconfigured authentication middleware
- Incomplete conditional checks (e.g., `if password == correct_password` instead of matching both)

References:

- https://owasp.org/Top10/A01_2021-Broken_Access_Control/
- https://owasp.org/www-community/Broken_Authentication

## Remediation

1. Always validate both the username and password together.
2. Use strong, proven authentication mechanisms (e.g., OAuth, bcrypt-based login).
3. Display generic error messages to avoid leaking authentication logic.
4. Log all failed login attempts and implement rate limiting.
5. Perform thorough code reviews on custom authentication systems.

> The Python script used for bruteforce testing is available at:  
> [`Ressources/login.py`](../login.py)

---

<table width="100%">
  <tr>
    <td align="left"><a href="../Breach12_*/Ressources/writeup.md">← Previous: Breach12</a></td>
    <td align="center"><a href="../../README.md">↑ Back to README</a></td>
    <td align="right"><a href="../Breach14_*/Ressources/writeup.md">Next: Breach14 →</a></td>
  </tr>
</table>