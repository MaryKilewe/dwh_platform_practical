$(document).ready(function(){
  var age_range = [];
  var totals = [];


  $.ajax({
    type: "GET",
    url: "/get_age_statistics",
    dataType:"json",
    success: function (data){

      for (var i = 0; i < data.length; i++) {
        age_range.push(data[i][0]);
        totals.push(data[i][1]);
      }

      var ctx = document.getElementById('ageChartContainer').getContext('2d');
      var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: age_range,
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
            text: 'Number of candidates in each age group'
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