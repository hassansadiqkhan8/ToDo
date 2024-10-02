const checkboxes = document.getElementsByName('checkbox');

// Add event listener to each checkbox
checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        const todoText = this.nextElementSibling;
        if (this.checked) {
            todoText.classList.add('completed');
        } else {
            todoText.classList.remove('completed');
        }
    });
});