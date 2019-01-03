function sendform() {
    var formElement = document.querySelector("form");
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/v2/sequenceSeekerV3_view.py");
    xhr.timeout = 4294967295;

    function set_loader() {
        start = new Date().valueOf();
        init = new Date();
        document.getElementById("init_field").innerHTML = init;
        document.getElementById("init_field_full").style.visibility='visible';
        document.getElementById("elapsed_field_full").style.visibility='hidden';
        document.getElementById("end_field_full").style.visibility='hidden';
        document.getElementById("loader").style.visibility='visible';
        document.getElementById("content").style.visibility='hidden';
}
    function show_time() {
        stop = new Date().valueOf();
        end = new Date();
        total = stop - start
        document.getElementById("end_field").innerHTML = end;
        document.getElementById("elapsed_field").innerHTML = total.toString().concat('ms');
        document.getElementById("elapsed_field_full").style.visibility='visible';
        document.getElementById("end_field_full").style.visibility='visible';
    };

    xhr.onload = function () {
        show_time()
        document.getElementById("loader").style.visibility='hidden';
        document.getElementById("content").style.visibility='visible';
        document.getElementById("content").innerHTML = xhr.responseText;
    };

    xhr.send(new FormData(formElement));
    document.onload = set_loader();

}