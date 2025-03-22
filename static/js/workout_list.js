document.addEventListener('DOMContentLoaded', function () {
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    const deleteButtons = document.querySelectorAll('.delete-workout');
    const confirmDeleteButton = document.getElementById('confirmDeleteButton');
    let workoutIdToDelete = null;

    // Function to show the modal and set the workout ID to delete
    function showDeleteModal(workoutId, workoutTitle) {
        workoutIdToDelete = workoutId;
        document.getElementById('workoutTitle').innerText = workoutTitle
        deleteModal.show();

    }

    // Add event listeners to delete buttons
    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const workoutId = this.getAttribute('workout_id');
            const workoutTitle = this.getAttribute('workout_title');
            showDeleteModal(workoutId, workoutTitle);
        });
    });

    // Handle the actual deletion when confirmed
    confirmDeleteButton.addEventListener('click', function () {
        if (workoutIdToDelete) {
            const deleteUrl = `delete_workout/${workoutIdToDelete}/`;
            window.location.href = deleteUrl;
        }
    });
});