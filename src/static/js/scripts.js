document.addEventListener('DOMContentLoaded', function () {
    // Define the categories array from the Django context (passed through the template)
    const categories = JSON.parse('{{ categories|safe|escapejs }}');

    let currentIndex = 0;

    function updateCategory() {
        const titleElement = document.getElementById('category-title');
        const textElement = document.getElementById('category-text');
        const iconElement = document.getElementById('category-icon');

        const category = categories[currentIndex];

        // Update the content dynamically from the category data
        titleElement.textContent = category.title;
        textElement.textContent = category.text;
        iconElement.src = category.icon;

        // Increment the index (and reset if it exceeds the array length)
        currentIndex = (currentIndex + 1) % categories.length;
    }

    // Start the rotation every 5 seconds
    updateCategory();  // Set initial category
    setInterval(updateCategory, 5000);
});