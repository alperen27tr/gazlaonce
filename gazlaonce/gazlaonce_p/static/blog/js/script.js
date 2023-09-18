// document.addEventListener("DOMContentLoaded", function() {
//     var clearButton = document.getElementById("yenibaslayan");
//     var incelemeButton = document.getElementById("inceleme");


//     var myDiv = document.getElementById("divmetin");
//     var headername = document.getElementById("headername");

//     clearButton.addEventListener("click", function() {
//         headername.textContent="yeni başlayan";
//          myDiv.innerHTML = ""; // Div içeriğini silme
//          myDiv.innerHTML = "<label class='form-control label-warning text-center'>yenibaslayan viedosu 1</label>";
//     });

//     incelemeButton.addEventListener("click", function() {
//         headername.textContent="inceleme";
//         myDiv.innerHTML = ""; // Div içeriğini silme
//         myDiv.innerHTML = "<label class='form-control label-warning text-center'>inceleme videosu1</label>";
//     });

// });

// $(document).ready(function() {
//     $('#yenibaslayan').click(function() {
//         $.ajax({
//             url: '{% url "get_data" %}',
//             type: 'GET',
//             dataType: 'json',
//             success: function(data) {
//                 $('#inceleme').text(data.message);
//             },
//             error: function() {
//                 $('#messageincelemeDiv').text('Veri alınamadı.');
//             }
//         });
//     });
// });
