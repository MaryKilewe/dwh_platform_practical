
$(document).ready(function(){
    var gender = [];
    var count = [];

    $.ajax({
        type: "GET",
        url: "/get_gender_statistics",
        dataType:"json",
        success: function(data){

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
    });
});