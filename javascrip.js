function startDownload() {
    const videoUrl = document.getElementById("videoUrl").value;
    const quality = document.getElementById("quality").value;
  
    if (!videoUrl) {
      alert("Por favor ingresa una URL.");
      return;
    }
  
    // Muestra el estado de la descarga
    document.getElementById("status").innerText = "Descargando...";
  
    // Realiza la petición al backend para procesar la descarga
    fetch('http://localhost:5000/download', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ videoUrl: videoUrl, quality: quality })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById("status").innerHTML = `<a href="${data.downloadLink}" target="_blank">Haz clic aquí para descargar</a>`;
    })
    .catch(error => {
      console.error("Error en la descarga:", error);
      document.getElementById("status").innerText = "Hubo un error al procesar la descarga.";
    });
  }
  