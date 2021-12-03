$(document).ready(function(){
  var month = [];
  var totals = [];


  $.ajax({
    type: "GET",
    url: "/monthly_reg_stats",
    dataType:"json",
    success: function (data){
      for (var i = 0; i < data.length; i++) {
        month.push(data[i][0]);
        totals.push(data[i][1]);
      }

      var ctx = document.getElementById('monthly_reg_ChartContainer').getContext('2d');
      var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: month,
          datasets: [{
            label:"Total",
            barPercentage: 0.7,
            barThickness: 'flex',
            minBarLength: 2,
            data: totals,

            backgroundColor: [
              '#847edd',
              '#b2aeea',
              '#847edd',
              '#b2aeea',
              '#847edd',
              '#b2aeea',
              '#847edd',
              '#b2aeea',
              '#847edd',
              '#b2aeea',
              '#847edd',
              '#b2aeea',
            ],
          }]
        },
        options: {
          legend: {display: false},
          title: {
            display: true,
            text: 'Monthly registrations per month in 2020'
          },
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              }
            }],
            xAxes: [{
              gridLines: {
                offsetGridLines: true
              }
            }]
          }
        }
      }); // end of bar chart

    }
  });

});