# Breach: Insufficient Input Validation on Survey Submission

## Discovery & Exploit

On the survey page, users are allowed to rate subjects from **1 to 10**. The form sends a POST request with parameters like:

``sujet=2&valeur=1``

Using Firefox’s developer tools:

1. Right-click on the request in the network tab
2. Choose "Edit and Resend"
3. Change the request body to include a value higher than 10 (e.g., `valeur=99`)
4. Send the modified request
5. Double-click the new request in the network list

The server responded with a new page containing the flag:

``The flag is: [FLAG_VALUE]``  
(In the real case: `b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3`)

## Vulnerability Details

This is a case of **missing server-side validation**.

Although the frontend restricts values to a specific range (1–10), the backend blindly trusts the submitted `valeur` parameter. By manually modifying the HTTP request, a user can bypass any client-side restriction and send arbitrary data.

References:

- https://owasp.org/Top10/A04_2021-Insecure_Design/
- https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html

## Remediation

1. Always enforce validation rules on the server, regardless of client-side constraints.
2. Reject or sanitize any value outside the accepted range (1–10).
3. Avoid relying on frontend controls (e.g., sliders or dropdowns) for data integrity.
4. Log invalid submissions for review or rate-limiting.

---

<table width="100%">
  <tr>
    <td align="left"><a href="../../Breach09_SQLi_DeepEnumerationFlagRebuild/Ressources/writeup.md">← Previous: Breach09</a></td>
    <td align="center"><a href="../../README.md">↑ Back to README</a></td>
    <td align="right"><a href="../../Breach11_DirectoryTraversalEtcPasswd/Ressources/writeup.md">Next: Breach11 →</a></td>
  </tr>
</table>
