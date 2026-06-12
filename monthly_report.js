const monthlyChart = new Chart(document.getElementById('monthlyChart'), {
  type: 'doughnut',
  data: {
    labels: ['Food', 'Shopping', 'Transport', 'Bills', 'Savings'],
    datasets: [{
      data: [430, 270, 160, 310, 70],
      backgroundColor: ['#4e90bf', '#536eda', '#76549b', '#3ea8cd', '#1a3a52'],
      borderWidth: 0,
      hoverOffset: 8
    }]
  },
  options: {
    responsive: true,
    cutout: '68%',
    plugins: {
      legend: {
        labels: {
          color: '#b8d5d9'
        }
      }
    }
  }
});