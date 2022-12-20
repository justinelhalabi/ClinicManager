$(document).ready(function () {

    var table


    function addDistrict(data) {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "district",
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
         $.notify("District Added Successfully", {"status":"success"});

            $('.modal.in').modal('hide')
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getDistrict()
        });

    }

    function deleteDistrict(id) {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "district/" + id,
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
   swal("Deleted!", "District has been deleted.", "success");
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getDistrict()
        });


});

    }

    function updateDistrict(data, id) {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "district/" + id,
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
            $.notify("District Updated Successfully", {"status":"success"});
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getDistrict()
        });


    }

    function getDistrict() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "district",
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
                        mData: 'Name'
                    },
                    {
                        mData: 'GovernateName'
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
                deleteDistrict(data.ID)

            });

            $('.btn-edit').one("click", function(e) {
                var data = table.row($(this).parents('tr')).data();
                $('#myModal').modal().one('shown.bs.modal', function (e) {
                    for (var key in data) {
                        $("[name=" + key + "]").val(data[key])
                    }
                    $("#savethedistrict").off("click").on("click", function(e) {
                    var instance = $('#detailform').parsley();
                    instance.validate()
                    console.log(instance.isValid())
                    if(instance.isValid()){
                        jsondata = $('#detailform').serializeJSON();
                        updateDistrict(jsondata, data.ID)
                        }

                    })
                })



            });


        });


    }




    $("#adddistricts").click(function () {

        $('#myModal').modal().one('shown.bs.modal', function (e) {

    $("#governate_select").html(governateSelect)

    });
            $("#savethedistrict").off("click").on("click", function(e) {


            var instance = $('#detailform').parsley();
            instance.validate()
                    if(instance.isValid()){
                jsondata = $('#detailform').serializeJSON();
                addDistrict(jsondata)
                }

            })

        })


var governateSelect=""
 function getGovernate() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "governate",
            "method": "GET",
            "headers": {
                "cache-control": "no-cache"
            }
        }

        $.ajax(settings).done(function (response) {

        for(i=0;i<response.length;i++){

        governateSelect +="<option value="+response[i].ID+">"+response[i].Name+"</option>"
        }


        })
        }
getGovernate()
getDistrict()
})