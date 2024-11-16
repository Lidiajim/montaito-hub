document.addEventListener('DOMContentLoaded', function () {
    // Obtener datos dinámicos desde los elementos ocultos
    const totalViews = JSON.parse(document.getElementById('totalViews').textContent);
    const totalDownloads = JSON.parse(document.getElementById('totalDownloads').textContent);

    // Datos para la gráfica
    const data = {
        labels: ['Total Views', 'Total Downloads'],
        datasets: [{
            label: 'Métricas',
            data: [totalViews, totalDownloads],
            backgroundColor: ['#17a2b8', '#dc3545'] /* Colores */
        }]
    };

    // Configuración de la gráfica
    const config = {
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false // Ocultar la leyenda
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            return `${context.label}: ${context.raw}`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    };

    // Renderizar la gráfica en el canvas
    const ctx = document.getElementById('viewsDownloadsChart').getContext('2d');
    new Chart(ctx, config); // Inicializamos la gráfica
});
