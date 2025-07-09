document.addEventListener("DOMContentLoaded", function () {

    console.log("Life, The Universe and Everything!");


    document.querySelectorAll('back-btn').forEach(button => {
        button.addEventListener('click', function () {
            window.history.back();
        });
    });
    




    // JavaScript to open and close add excercise modal
    document.getElementById("add-ex-btn").addEventListener("click", function () {
        console.log("Add Exercise button clicked");
        document.getElementById("exercise-modal").style.display = "block";
    });

    document.getElementById("close-modal-btn").addEventListener("click", function () {
        document.getElementById("exercise-modal").style.display = "none";
    });

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




    document.getElementById("add-exercises-btn").addEventListener("click", function () {
        // Get all selected exercises from the modal
        const selectedExercises = document.querySelectorAll('input[name="selected_exercises"]:checked');

        selectedExercises.forEach(exerciseCheckbox => {
            // Create the exercise HTML structure dynamically
            const exerciseName = exerciseCheckbox.value;
            const exerciseId = exerciseCheckbox.id.replace('exercise', ''); // Extract the exercise ID
            // const exerciseImage = document.querySelector(`#exercise${exerciseId} img`).src;

            // Create a new exercise div
            const exerciseDiv = document.createElement("div");
            exerciseDiv.classList.add("exercise");
            exerciseDiv.setAttribute("data-id", exerciseName);

            exerciseDiv.innerHTML = `
<h2>${exerciseName}</h2>

<button type="button" class="delete-exercise-button btn btn-danger">Delete Exercise</button>
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
        <td><input type="number" name="reps_${exerciseId}_1" value="10" /></td>
        <td></td>
    </tr>
</tbody>
</table>
<button type="button" class="add-set-button btn btn-primary">Add Set</button>
`;

            // Append the new exercise to the workout exercises section
            document.querySelector(".workout-exercises").appendChild(exerciseDiv);
        });


        assignAddSetButtonEvent();
        // Close the modal after saving
        document.getElementById("exercise-modal").style.display = "none";

    });


    const input = document.getElementById("workout-title");
    const saveBtn = document.getElementById("update-workout-btn");



    // Function to update button disabled state
    function updateButtonState() {
        // Trim whitespace and check if input is empty
        if (input.value.trim() === "") {
            saveBtn.disabled = true;
        } else {
            saveBtn.disabled = false;
        }
    }

    // Initialize button state on page load
    updateButtonState();

    // Listen for input changes and update button state
    input.addEventListener("input", updateButtonState);



    const addSetButtons = document.querySelectorAll('.add-set-button');
    const deleteExerciseButtons = document.querySelectorAll('.delete-exercise-button');
    let exerciseToDelete = null;
    const saveWorkoutButton = document.getElementById('save-workout-btn');
    const updateWorkoutButton = document.getElementById('update-workout-btn');
    const workoutTitle = document.getElementById('workout-title').value;

    let workoutId = null;
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


    deleteExerciseButtons.forEach(button => {
        button.addEventListener('click', function () {
            exerciseToDelete = button.closest('.exercise');
            $('#deleteModal').modal('show');
        });
    });

    document.getElementById('confirmDeleteButton').addEventListener('click', function () {
        if (exerciseToDelete) {
            exerciseToDelete.remove();
            $('#deleteModal').modal('hide');
            checkRemainingExercises();
        }
    });

    function checkRemainingExercises() {
        const remainingExercises = document.querySelectorAll('.exercise');
        if (remainingExercises.length === 0) {
            const workoutTitle = "workout-title";
            // window.location.href = `'create_workout'?workout_title=${encodeURIComponent(workoutTitle)}`;
            // const createUrl = `create_workout/${workoutIdToDelete}/`;
            // window.location.href = createUrl;
        }
    }


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
    // if (saveWorkoutButton) {
    //     saveWorkoutButton.addEventListener('click', function () {
    //         sendWorkoutData('save_workout');
    //     });
    // }


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