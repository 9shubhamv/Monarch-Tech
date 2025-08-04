const fileSelect = document.getElementById('fileSelect');
    const viewButton = document.getElementById('viewBtn');
    const modal = document.getElementById('modal');
    const downloadBtn = document.getElementById('downloadBtn');

    let selectFile = "";

    fileSelect.addEventListener("change", () => {
        selectFile = fileSelect.value;
        viewButton.disabled = !selectFile;
    });

    viewButton.addEventListener('click', () => {
    fetch(`/open/?filename=${encodeURIComponent(selectFile)}`)
        .then(response => response.json())
        .then(data => {
            if (data.status === "not found") {
                modal.style.display = "flex";
                downloadBtn.onclick = () => {
                    if (data.gdrive_link) {
                        window.open(data.gdrive_link, "_blank");
                        modal.style.display = "none";
                    } else {
                        alert("No Google Drive link available.");
                    }
                };
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

    // Close modal when clicking outside
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = "none";
        }
    });