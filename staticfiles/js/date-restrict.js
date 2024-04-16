document.addEventListener('DOMContentLoaded', function () {
    var date = new Date(); // Gets today's date
    date.setDate(date.getDate() + 3); // Adds three days to today's date

    // Formats the date as YYYY-MM-DD for the input
    var dateString = date.toISOString().split('T')[0];

    // Sets the minimum date that can be chosen to three days from today
    document.getElementById('delivery_date').setAttribute('min', dateString);
});
