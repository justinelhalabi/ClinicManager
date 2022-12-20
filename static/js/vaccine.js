$(document).ready(function () {

    var table


    function addVaccine(data) {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "vaccine",
            "method": "POST",
            "headers": {
                "content-type": "application/json",
                "cache-control": "no-cache",
                "postman-token": "2612534b-9ccd-ab7e-1f73-659029967199"
            },
            "processData": false,
            "data": JSON.stringify(data)
        }

        $.ajax(settings).done(function (response) {
         $.notify("Vaccine Added Successfully", {"status":"success"});

            $('.modal.in').modal('hide')
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getVaccine()
        });

    }

    function deleteVaccine(id) {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "vaccine/" + id,
            "method": "DELETE",
            "headers": {
                "cache-control": "no-cache",
                "postman-token": "28ea8360-5af0-1d11-e595-485a109760f2"
            }
        }

swal({
    title: "Are you sure?",
    text: "You will not be able to recover this data",
    type: "warning",
    showCancelButton: true,
    confirmButtonColor: "#DD6B55",
    confirmButtonText: "Yes, delete it!",
    closeOnConfirm: false
}, function() {
 $.ajax(settings).done(function (response) {
   swal("Deleted!", "Vaccine has been deleted.", "success");
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getVaccine()
        });


});

    }

    function updateVaccine(data, id) {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "vaccine/" + id,
            "method": "PUT",
            "headers": {
                "content-type": "application/json",
                "cache-control": "no-cache"
            },
            "processData": false,
            "data": JSON.stringify(data)
        }

        $.ajax(settings).done(function (response) {
            $('.modal.in').modal('hide')
            $.notify("Vaccine Updated Successfully", {"status":"success"});
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getVaccine()
        });


    }

    function getVaccine() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "vaccine",
            "method": "GET",
            "headers": {
                "cache-control": "no-cache"
            }
        }

        $.ajax(settings).done(function (response) {

            table = $('#datatable4').DataTable({
                "bDestroy": true,
                'paging': true, // Table pagination
                'ordering': true, // Column ordering
                'info': true, // Bottom left status text
                aaData: response,
                   "aaSorting": [],
                aoColumns: [
                    {
                        mData: 'ID'
                    },
                    {
                        mData: 'DateTaken'
                    },
                    {
                        mData: 'hospitalName'
                    },
                    {
                        mData: 'patientName'
                    },
                    {
                        mRender: function (o) {
                            return '<button class="btn-xs btn btn-info btn-edit" type="button">Edit</button>';
                        }
                    },
                    {
                        mRender: function (o) {
                            return '<button class="btn-xs btn btn-danger delete-btn" type="button">Delete</button>';
                        }
                    }
        ]
            });

            $('#datatable4 tbody').on('click', '.delete-btn', function () {
                var data = table.row($(this).parents('tr')).data();
                console.log(data)
                deleteVaccine(data.ID)

            });

            $('.btn-edit').one("click", function(e) {
                var data = table.row($(this).parents('tr')).data();
                $('#myModal').modal().one('shown.bs.modal', function (e) {
                    for (var key in data) {
                        $("[name=" + key + "]").val(data[key])
                    }
                    $("#savethevaccine").off("click").on("click", function(e) {
                    var instance = $('#detailform').parsley();
                    instance.validate()
                    console.log(instance.isValid())
                    if(instance.isValid()){
                        jsondata = $('#detailform').serializeJSON();
                        updateVaccine(jsondata, data.ID)
                        }

                    })
                })



            });


        });


    }




    $("#addvaccine").click(function () {

        $('#myModal').modal().one('shown.bs.modal', function (e) {

    $("#hospital_select").html(hospitalSelect)
    $("#patient_select").html(patientSelect)

    });
            $("#savethevaccine").off("click").on("click", function(e) {


            var instance = $('#detailform').parsley();
            instance.validate()
                    if(instance.isValid()){
                jsondata = $('#detailform').serializeJSON();
                addVaccine(jsondata)
                }

            })

        })


var hospitalSelect=""
 function getHospital() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "hospital",
            "method": "GET",
            "headers": {
                "cache-control": "no-cache"
            }
        }

        $.ajax(settings).done(function (response) {

        for(i=0;i<response.length;i++){

        hospitalSelect +="<option value="+response[i].ID+">"+response[i].Name+"</option>"
        }


        })
        }

var patientSelect=""
  function getPatient() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "patient",
            "method": "GET",
            "headers": {
                "cache-control": "no-cache"
            }
        }

        $.ajax(settings).done(function (response) {
         for(i=0;i<response.length;i++){
        patientSelect +="<option value="+response[i].ID+">"+response[i].patientFullName+"</option>"
        }

                })
        }

getPatient()
getHospital()
getVaccine()
})