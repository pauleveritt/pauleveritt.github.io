import $ from 'jquery';
import ToDo from './todo';

$(document).ready(() => {

    // All REST requests should send content type, and log failures
    $.ajaxSetup({contentType: 'application/json'});
    $(document).ajaxError((event, jqxhr, settings, thrownError) => {
        console.error('Ajax call failed:',
            settings.type, settings.url, thrownError);
    });

    new ToDo();

});
