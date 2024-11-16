document.addEventListener('DOMContentLoaded', function () {
    const totalViews = JSON.parse(document.getElementById('totalViews').textContent);
    const totalDownloads = JSON.parse(document.getElementById('totalDownloads').textContent);

    // Calcular el porcentaje de descargas frente a las vistas
    const downloadPercentage = ((totalDownloads / totalViews) * 100).toFixed(2);

    const data = {
        labels: ['Total Views', 'Total Downloads'],
        datasets: [{
            label: 'Métricas',
            data: [totalViews, totalDownloads],
            backgroundColor: ['#17a2b8', '#dc3545']
        }]
    };

    const config = {
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            // Mostrar el porcentaje en el tooltip de "Total Downloads"
                            if (context.label === 'Total Downloads') {
                                return `${context.label}: ${context.raw} (${downloadPercentage}%)`;
                            }
                            return `${context.label}: ${context.raw}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    ticks: {
                        font: {
                            size: 16,
                            weight: 'bold'
                        },
                        color: '#333'
                    }
                },
                y: {
                    beginAtZero: true,
                    ticks: {
                        font: {
                            size: 14,
                            weight: 'normal'
                        }
                    }
                }
            }
        }
    };

    const ctx = document.getElementById('viewsDownloadsChart').getContext('2d');
    new Chart(ctx, config);

    const percentageElement = document.createElement('p');
    percentageElement.textContent = `Percentage of Downloads vs Views: ${downloadPercentage}%`;
    percentageElement.style.textAlign = 'center';
    percentageElement.style.fontWeight = 'bold';
    document.getElementById('viewsDownloadsChart').parentElement.appendChild(percentageElement);
});
