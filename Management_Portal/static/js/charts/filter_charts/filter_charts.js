$('#submit-filters').submit(function () {
        event.preventDefault();

        let filters = {
            month: $( "#month" ).val(),
            year: $( "#year" ).val(),
            facility: $( "#facility" ).val(),
            county: $('#county').val()
        };

        // call function to post data to get filtered gender stats
        postData_to_gender_filter(filters)

        // call function to post data to get filtered age stats
        postData_to_age_filter(filters)

        // call function to post data to get filtered monthly registrations
        postData_to_registrations_filter(filters)
});


function postData_to_gender_filter(filters){
        var gender = [];
        var count = [];

       $.ajax({
        url: "/gender_filter",
        type: "POST",
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(filters),
        success: function (data) {

            //$("#gender_title").remove();
            //document.getElementById("genderPieChartContainer").remove();
            $( "#gender_stats" ).empty();
            title = $('<h5 class="heading mb-sm-5 mb-4" id="gender_title">Gender <strong>Stats </strong></h5>' );
            $('#gender_stats').append(title);



            //alert(JSON.stringify(data));
            if (Object.keys(data).length == 0) {
                // if length of result is 0, tell user no results were found
                msg = $('<div class="alert" style="padding: 15px; background-color: #FFEBEE; color: #B71C1C;">No Data</div>' );
                $('#gender_stats').append(msg);
            } else {
                // add back the container for the chart
                filteredgenderPieChartContainer = $('<canvas id="genderPieChartContainer" style="height: 300px; width: 300px;"></canvas>' );
                $('#gender_stats').append(filteredgenderPieChartContainer);

                for (var i = 0; i < data.length; i++) {
                    gender.push(data[i][0]);
                    count.push(data[i][1]);
                }

                var ctx = document.getElementById('genderPieChartContainer');
                var myDoughnutChart = new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        datasets: [{
                            data: count,
                            backgroundColor: ['#665ED5','#938ee1']
                        }],
                        // These labels appear in the legend and in the tooltips when hovering different arcs
                        labels: gender
                    }
                    //options: options
                });
            }


        },
        error: function () {
            console.log("...error");
            $('#fetching-filters-spinner').hide();
            $('#submit-filters-btn').show();
        }
    })
}


function postData_to_age_filter(filters){
        var age_range = [];
        var totals = [];

       $.ajax({
        url: "/age_filter",
        type: "POST",
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(filters),
        success: function (data) {

            //document.getElementById("age_title").remove();
            //document.getElementById("ageChartContainer").remove();
            $( "#age_stats" ).empty();
            title = $('<h5 class="heading mb-sm-5 mb-4" id="age_title">Age dsdffsd <strong>Stats </strong></h5>' );
            filteredagePieChartContainer = $('<canvas id="ageChartContainer" style="height: 300px; width: 300px;"></canvas>' );
            $('#age_stats').append(title);
            $('#age_stats').append(filteredagePieChartContainer);


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
                    text: 'Filtered ages'
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

        },
        error: function () {
            console.log("...error");
            $('#fetching-filters-spinner').hide();
            $('#submit-filters-btn').show();
        }
    })
}




function postData_to_registrations_filter(filters){
        var month = [];
        var totals = [];

       $.ajax({
        url: "/monthly_reg_filter",
        type: "POST",
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(filters),
        success: function (data) {

            //document.getElementById("monthly_reg_title").remove();
            //document.getElementById("monthly_reg_ChartContainer").remove();
            $( "#monthly_reg_stats" ).empty();
            title = $('<h5 class="heading mb-sm-5 mb-4" id="monthly_reg_title">Monthly Registrations <strong>Stats </strong></h5>' );
            filteredregPieChartContainer = $('<canvas id="monthly_reg_ChartContainer" style="height: 300px; width: 300px;"></canvas>' );
            $('#monthly_reg_stats').append(title);
            $('#monthly_reg_stats').append(filteredregPieChartContainer);

            //alert(JSON.stringify(data));
            if (Object.keys(data).length == 0) {
                // if length of result is 0, tell user no results were found
                msg = $('<div class="alert" style="padding: 15px; background-color: #FFEBEE; color: #B71C1C;">No Data</div>' );
                $('#monthly_reg_stats').append(msg);
            } else {
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
                        text: 'Filtered Monthly registrations'
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


        },
        error: function () {
            console.log("...error");
            $('#fetching-filters-spinner').hide();
            $('#submit-filters-btn').show();
        }
    })
}