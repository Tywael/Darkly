# Breach: SQL Injection on Image Listing

## Discovery & Exploit

On a page that displays images, we noticed the same SQL injection vector as seen in the member listing page.

Submitting the input:

``0=0``

revealed several image entries, including:

- **Title**: Hack me ?  
- **URL**: borntosec.ddns.net/images.png

This hinted that a SQL injection might again be possible via UNION SELECT.

We confirmed this using:

``0=0 UNION SELECT table_name, column_name FROM information_schema.columns``

Among the large volume of results, we identified the following structure:

- **Table**: list_images
- **Columns**: id, url, title, comment

We then queried:

``0=0 UNION SELECT url, comment FROM list_images``

This revealed the following:

- **URL**: borntosec.ddns.net/images.png  
- **Comment**: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : `1928e8083cf461a51303633093573c46`

We [decoded the MD5](https://md5hashing.net/hash/md5/1928e8083cf461a51303633093573c46) hash to:

``albatroz``

Then hashed it using [SHA256](https://10015.io/tools/sha256-encrypt-decrypt) to obtain the final [flag](../flag)

## Vulnerability Details

This is a classic **UNION-based SQL Injection**. The application fails to sanitize user input and allows SQL code to be appended to queries.

This gives attackers read access to:

- The database schema via `information_schema`
- The contents of internal application tables

References:

- https://owasp.org/www-community/attacks/SQL_Injection
- https://portswigger.net/web-security/sql-injection/union-attacks

## Remediation

1. Use parameterized queries or ORM libraries to prevent direct SQL injection.
2. Sanitize all user input before including it in SQL queries.
3. Limit database access rights to prevent information leakage.
4. Avoid displaying database errors or debug content in production environments.

---

<table width="100%">
  <tr>
    <td align="left"><a href="../../Breach08_SQLi_DeepEnumerationFlagRebuild/Ressources/writeup.md">← Previous: Breach07</a></td>
    <td align="center"><a href="../../README.md">↑ Back to README</a></td>
    <td align="right"><a href="../../Breach10_SurveyValueBypass/Ressources/writeup.md">Next: Breach09 →</a></td>
  </tr>
</table>
