document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('orderForm');
    if(form) {
        form.onsubmit = function() {
            var checkboxes = document.querySelectorAll('input[type="checkbox"]');
            var checkedOne = Array.prototype.slice.call(checkboxes).some(x => x.checked);

            if (!checkedOne) {
                alert('Please select at least one item to order.');
                return false; // Prevent form from submitting
            }
            return true; // Allow form submission
        };
    }
});
