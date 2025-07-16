document.addEventListener("DOMContentLoaded", function () {

    // 🔹 Declare all DOM element references at the top
    const checkboxes = document.querySelectorAll('.form-check-input');
    const addExBtn = document.getElementById('add-ex-btn');
    const selectedExercisesInput = document.getElementById('selected-exercises');
    const closeModalBtn = document.getElementById("close-modal-btn");
    const input = document.getElementById("workout-title");
    const saveBtn = document.getElementById("update-workout-btn");
    const addSetButtons = document.querySelectorAll('.add-set-button');
    const deleteExerciseButtons = document.querySelectorAll('.delete-exercise-button');
    let exerciseToDelete = null;
    const saveWorkoutButton = document.getElementById('save-workout-btn');
    const updateWorkoutButton = document.getElementById('update-workout-btn');
    const workoutTitle = document.getElementById('workout-title').value;
    let workoutId = null;
    const openExercisesModelBtn = document.getElementById("open-exercises-model-btn");
    const workoutExercises = document.querySelector('.workout-exercises');


    document.querySelectorAll('back-btn').forEach(button => {
        button.addEventListener('click', function () {
            window.history.back();
        });
    });


    // JavaScript to open and close add excercise modal
    if (openExercisesModelBtn) {
        openExercisesModelBtn.addEventListener("click", function () {
            console.log("Add Exercise button clicked");
            const modal = document.getElementById("exercise-modal");
            if (modal) {
                // Unselect all checked inputs inside the modal
                const selectedInputs = modal.querySelectorAll('input[type="checkbox"]:checked, input[type="radio"]:checked');
                selectedInputs.forEach(input => {
                    input.checked = false;
                });
                modal.style.display = "block";
            }
        });
    }



    function updateButtonText() {
        const checkedCheckboxes = document.querySelectorAll('.form-check-input:checked');
        const selectedCount = checkedCheckboxes.length;

        // Update all buttons with class "add-excersies-btn"
        document.querySelectorAll('.add-excersies-btn').forEach(addExBtn => {
            addExBtn.textContent = `Add Exercises (${selectedCount})`;
        });

        const selectedExercises = Array.from(checkedCheckboxes)
            .map(checkbox => checkbox.value);

        // Assuming selectedExercisesInput is a single input element:
        if (selectedExercisesInput) {
            selectedExercisesInput.value = JSON.stringify(selectedExercises);
        }

        console.log(selectedExercises);
    }

    // Listen for changes on all checkboxes
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateButtonText);
    });

    // Run once after a short delay to initialize
    setTimeout(updateButtonText, 100);


    if (closeModalBtn) {
        closeModalBtn.addEventListener("click", function () {
            const modal = document.getElementById("exercise-modal");
            if (modal) {
                modal.style.display = "none";
            }
        });
    }



    function assignAddSetButtonEvent() {
        const addSetButtons = document.querySelectorAll('.add-set-button');

        addSetButtons.forEach(button => {
            button.addEventListener('click', function () {
                const exerciseDiv = button.closest('.exercise');
                const tableBody = exerciseDiv.querySelector('tbody');
                const setCount = tableBody.querySelectorAll('tr').length + 1;
                const exerciseId = exerciseDiv.getAttribute('data-id');

                const newRow = document.createElement('tr');
                newRow.innerHTML = `
        <td>${setCount}</td>
        <td><input class="reps-input" type="number" name="reps_${exerciseId}_${setCount}" value="10" min="1" step="1"/></td>
        <td><button type="button" class="delete-set-button btn btn-danger">Delete</button></td>
    `;

                const deleteButton = newRow.querySelector('.delete-set-button');
                deleteButton.addEventListener('click', function () {
                    newRow.remove();
                });

                tableBody.appendChild(newRow);
            });
        });
    }

    // Your existing function to update button text
    function updateButtonText() {
        const checkedCheckboxes = document.querySelectorAll('.form-check-input:checked');
        const selectedCount = checkedCheckboxes.length;

        document.querySelectorAll('.add-excersies-btn').forEach(addExBtn => {
            addExBtn.textContent = `Add Exercises (${selectedCount})`;
        });

        const selectedExercises = Array.from(checkedCheckboxes)
            .map(checkbox => checkbox.value);

        if (selectedExercisesInput) {
            selectedExercisesInput.value = JSON.stringify(selectedExercises);
        }

        console.log(selectedExercises);
    }




    function attachDeleteListeners() {
        const deleteButtons = document.querySelectorAll(".delete-exercise-button");
        deleteButtons.forEach(button => {
            button.addEventListener("click", function () {
                const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
                deleteModal.show();

                // Optional: Store reference to the clicked element
                const exerciseDiv = button.closest(".exercise-block"); // wrap each in a div with this class
                const confirmBtn = document.getElementById("confirmDeleteButton");

                confirmBtn.onclick = function () {
                    if (exerciseDiv) exerciseDiv.remove();
                    deleteModal.hide();
                };
            });
        });
    }


    // Function to add exercises from modal selections
    function addSelectedExercises() {
        // Get all selected exercises from the modal
        const selectedExercises = document.querySelectorAll('input[name="selected_exercises"]:checked');

        selectedExercises.forEach(exerciseCheckbox => {
            const exerciseName = exerciseCheckbox.value;
            const exerciseId = exerciseCheckbox.id.replace('exercise', '');

            const exerciseDiv = document.createElement("div");
            exerciseDiv.classList.add("exercise");
            exerciseDiv.setAttribute("data-id", exerciseName);

            const saveHTML = ` 
                 <div class="excersise">
                    <h2>${exerciseName}</h2>
                    <button type="button" class="delete-exercise-button btn btn-danger">Delete Exercise</button>
                    <table class="custom-table">
                        <thead>
                            <tr>
                                <th>Set Number</th>
                                <th>Reps</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1</td>
                                <td><input type="number" name="reps_${exerciseId}_1" value="10" min="1" step="1"/></td>
                                <td></td>
                            </tr>
                        </tbody>
                    </table>
                    <button type="button" class="add-set-button btn btn-primary">Add Set</button>
                </div>`


            exerciseDiv.innerHTML = `
        

                <div class="excersise-header">
                     <img class="" src="/static/images/image-coming-soon.png" alt="Exercise Image" />
                    <h2>${exerciseName}</h2>
                    <button type="button" class="delete-exercise-button btn btn-danger">Delete Exercise</button>
                </div>
             
                <table class=".custom-table">
                    <thead>
                        <tr>
                            <th>Set Number</th>
                            <th>Reps</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td><input type="number" name="reps_${exerciseId}_1"
                                    value="10" min="1" step="1"/></td>
                            <td><button type="button" class="delete-set-button btn btn-danger">Delete</button></td>
                        </tr>
                    </tbody>
                </table>
                <button type="button" class="add-set-button btn btn-primary">Add Set</button>
                
            `;


            document.querySelector(".workout-exercises").appendChild(exerciseDiv);
            attachDeleteListeners();
        });

        assignAddSetButtonEvent();

        // Close the modal after saving
        document.getElementById("exercise-modal").style.display = "none";
    }

    // When add exercises button is clicked, add selected exercises to excersises in workout
    document.querySelectorAll('.add-excersies-btn').forEach(button => {
        // On button click: add selected exercises
        button.addEventListener('click', addSelectedExercises);
    });









    // Listen for checkbox changes to update button text count
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateButtonText);
    });

    // Initialize button text on load
    setTimeout(updateButtonText, 100);


    // Define the function in outer scope
    function updateButtonState() {
        if (input && saveBtn) {
            if (input.value.trim() === "") {
                saveBtn.disabled = true;
            } else {
                saveBtn.disabled = false;
            }
        }
    }

    // Initialize button state on page load
    updateButtonState();

    // Listen for input changes and update button state
    if (input) {
        input.addEventListener("input", updateButtonState);
    }


    const workoutIdElement = document.getElementById('workout-id');
    if (workoutIdElement) {
        workoutId = workoutIdElement.value;
    }


    // addSetButtons.forEach(button => {
    //     button.addEventListener('click', function () {
    //         const exerciseDiv = button.closest('.exercise');
    //         const tableBody = exerciseDiv.querySelector('tbody');
    //         const setCount = tableBody.querySelectorAll('tr').length + 1;
    //         const exerciseId = exerciseDiv.getAttribute('data-id');

    //         const newRow = document.createElement('tr');
    //         newRow.innerHTML = `
    //             <td>${setCount}</td>
    //             <td><input type="number" name="reps_${exerciseId}_${setCount}" value="10" /></td>
    //             <td><button type="button" class="delete-set-button btn btn-danger">Delete</button></td>
    //         `;
    //         const deleteButton = newRow.querySelector('.delete-set-button');
    //         deleteButton.addEventListener('click', function () {
    //             newRow.remove();
    //         });
    //         tableBody.appendChild(newRow);
    //     });
    // });

    function assignAddSetButtonEvent() {
        const addSetButtons = document.querySelectorAll('.add-set-button');

        addSetButtons.forEach(button => {
            button.addEventListener('click', function () {
                const exerciseDiv = button.closest('.exercise');
                const tableBody = exerciseDiv.querySelector('tbody');
                const setCount = tableBody.querySelectorAll('tr').length + 1;
                const exerciseId = exerciseDiv.getAttribute('data-id');

                const newRow = document.createElement('tr');
                newRow.innerHTML = `
                    <td>${setCount}</td>
                    <td><input type="number" name="reps_${exerciseId}_${setCount}" value="10" /></td>
                    <td><button type="button" class="delete-set-button btn btn-danger">Delete</button></td>
                `;

                const deleteButton = newRow.querySelector('.delete-set-button');
                deleteButton.addEventListener('click', function () {
                    newRow.remove();
                });

                tableBody.appendChild(newRow);
            });
        });
    }
    assignAddSetButtonEvent();



    // Delete exercise button functionality
    // deleteExerciseButtons.forEach(button => {
    //     button.addEventListener('click', function () {
    //         exerciseToDelete = button.closest('.exercise');
    //         console.log("Exercise to delete:", exerciseToDelete);
    //         $('#deleteModal').modal('show');
    //     });
    // });

    if (workoutExercises) {
        workoutExercises.addEventListener("click", function (event) {
            if (event.target.classList.contains("delete-exercise-button")) {
                // Always set a fresh reference
                exerciseToDelete = event.target.closest(".exercise");
                console.log("Exercise to delete:", exerciseToDelete);
                if (exerciseToDelete) {
                    $('#deleteModal').modal('show');
                }
            }
        });
    }

    // Confirm deletion – use one single event listener
    if (confirmDeleteButton) {
        confirmDeleteButton.addEventListener("click", function () {
            if (exerciseToDelete) {
                exerciseToDelete.remove();
                exerciseToDelete = null; // Reset reference
                $('#deleteModal').modal('hide');
            }
        });
    }




    // Delete set button functionality
    document.addEventListener('click', function (e) {
        if (e.target && e.target.classList.contains('delete-set-button')) {
            const row = e.target.closest('tr'); // Adjust to match your row class
            if (row) row.remove();
        }
    });

    // Input validation for reps
    document.querySelectorAll('.reps-input').forEach(input => {
        input.addEventListener('input', function () {
            let value = input.value;

            // Remove non-digits and leading zeros
            value = value.replace(/[^0-9]/g, '');

            // Convert to number and prevent zero or empty
            if (value !== '') {
                const intValue = parseInt(value);
                input.value = intValue < 1 ? 1 : intValue;
            } else {
                input.value = ''; // Allow empty temporarily
            }
        });
    });



    document.getElementById('confirmDeleteButton').addEventListener('click', function () {
        if (exerciseToDelete) {
            exerciseToDelete.remove();
            $('#deleteModal').modal('hide');
        }
    });



    // Function to gather workout data
    function gatherWorkoutData() {
        const workoutTitle = document.getElementById('workout-title').value;

        const exercises = [];

        console.clear();

        document.querySelectorAll('.exercise').forEach(function (exerciseDiv) {
            const exercise_name = exerciseDiv.getAttribute('data-id');
            const exerciseReps = [];

            exerciseDiv.querySelectorAll('input[type="number"]').forEach(function (input, index) {
                const setNumber = index + 1;
                const reps = input.value;
                exerciseReps.push({ set: setNumber, reps: reps });
            });

            exercises.push({
                exercise_type: exercise_name,
                set_reps: exerciseReps
            });
        });

        console.log('Workout Title:', workoutTitle);
        console.log('Exercises data:', exercises);

        return {
            title: workoutTitle,
            exercises: exercises
        };
    }


    function sendWorkoutData(url, workoutId = null) {
        console.log("send workout data function triggered")
        const workoutData = gatherWorkoutData();


        // If a workout id is sent to the function then print it
        if (workoutId) {
            console.log("The workout id is:", workoutId)
            console.log("The url is:", url);
        }

        // Validate workout title
        console.log("Validating workout title:", workoutData.title);
        const titleValidation = validateWorkoutTitle(workoutData.title);
        if (!titleValidation.isValid) {
            console.log("Invalid title:", result.errors);
        } else {
            console.log("Title is valid!");
        }


        $.ajaxSetup({
            headers: {
                'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
            }
        });

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'id': workoutId,  // Only included if editing
                'title': workoutData.title,
                'exercise_type': JSON.stringify(workoutData.exercises),
            },
            success: function (response) {
                if (response.status === 'success') {
                    alert(`Workout ${workoutId ? 'updated' : 'saved'} successfully!`);
                    window.location.href = '/workouts/';  // Redirect to the workouts page
                } else {
                    alert(`Failed to ${workoutId ? 'update' : 'save'} workout.`);
                }
            },
            error: function (xhr, status, error) {
                console.error('Error updating workout:', error);
                alert('Something went wrong. Please try again.');
            }
        });
    }


    // Validate workout title
    function validateWorkoutTitle(title) {
        const errors = [];

        // Trim whitespace
        const trimmedTitle = title.trim();

        // Required check
        if (trimmedTitle.length === 0) {
            errors.push("Workout title is required.");
        }

        if (trimmedTitle.length > 50) {
            errors.push("Workout title must be 50 characters or fewer.");
        }

        // Allowed characters (letters, numbers, spaces, dashes, and apostrophes)
        const pattern = /^[a-zA-Z0-9\s\-']+$/;
        if (!pattern.test(trimmedTitle)) {
            errors.push("Workout title can only contain letters, numbers, spaces, dashes, and apostrophes.");
        }

        return {
            isValid: errors.length === 0,
            errors: errors
        };
    }

    // Button click handlers
    if (saveWorkoutButton) {
        saveWorkoutButton.addEventListener('click', function () {
            console.log("Save workout button pressed");
            sendWorkoutData('save_workout');
        });
    }


    if (updateWorkoutButton) {
        if (workoutId) {
            updateWorkoutButton.addEventListener('click', function () {
                console.log("update workout button pressed my g");
                console.log("Workout id:", workoutId);

                // Validate workout data on frontend before sending to backend
                console.log("Validating workout data before sending to backend...");
                const titleValidation = validateWorkoutTitle("Chest Day 1");

                if (!titleValidation.isValid) {
                    console.log("Invalid title:", result.errors);
                } else {
                    console.log("Title is valid!");
                }

                const updateWorkoutUrl = `/workouts/update_workout/`;  // Match the URL pattern
                sendWorkoutData(updateWorkoutUrl, workoutId);
            });
        } else {
            console.log("There is no workout Id");
        }
    }




});