$(document).ready(function () {

var settings = {
  "async": true,
  "crossDomain": true,
  "url": "common",
  "method": "GET",
  "headers": {
    "cache-control": "no-cache"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
  $('#patientcount').text(response.patient)
  $('#hospitalCount').text(response.hospital)
  $('#governateCount').text(response.governate)
  $('#districtCount').text(response.district)
  $('#medicalRecCount').text(response.medicalrecord)
  $('#vaccineCount').text(response.vaccine)

});


})
