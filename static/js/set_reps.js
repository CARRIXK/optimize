document.addEventListener('DOMContentLoaded', function () {
    const addSetButtons = document.querySelectorAll('.add-set-button');
    const deleteExerciseButtons = document.querySelectorAll('.delete-exercise-button');
    let exerciseToDelete = null;
    const saveWorkoutButton = document.getElementById('save-workout-btn');


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


    // Save workout button click handler
    // saveWorkoutButton.addEventListener('click', function () {
    //     const workoutTitle = document.getElementById('workout-title').innerText;  // Assuming you have the title in the <h1> tag
    //     const exercises = [];
    //     const reps = {};

    //     console.clear();

    //     // Collect exercise IDs and reps for each exercise
    //     document.querySelectorAll('.exercise').forEach(function (exerciseDiv) {
    //         const exercise_name = exerciseDiv.getAttribute('data-id');
    //         const exerciseReps = [];

    //         // Collect the data for the workout and exercise_type (exercise name in this case)
    //         // Collect reps for each set
    //         exerciseDiv.querySelectorAll('input[type="number"]').forEach(function (input, index) {
    //             const setNumber = index + 1;  // Set number starts from 1
    //             const reps = input.value;  // Get the number of reps
    //             exerciseReps.push({ set: setNumber, reps: reps });  // Add set and reps to the array
    //         });

    //         // Add the exercise data to the exercises array
    //         exercises.push({
    //             exercise_type: exercise_name,  // exercise_name should be the exercise type ID here
    //             set_reps: exerciseReps  // This should be the array of sets and reps for each exercise
    //         });
    //     });



    //     // Prepare data to send to the backend
    //     const formData = new FormData();
    //     formData.append('workout_title', workoutTitle);

    //     // Append each exercise to the FormData object
    //     exercises.forEach((exercise, index) => {
    //         formData.append(`exercise_${index}_exercise_type`, exercise.exercise_type);
    //         formData.append(`exercise_${index}_sets_reps`, JSON.stringify(exercise.set_reps));  // Ensure sets_reps is sent as JSON
    //     });

    //     // Output the data to the console
    //     console.log('Workout Title:', workoutTitle);
    //     console.log('Exercises data:', exercises);

    

    //     createWorkoutUrl = 'save_workout';
    //     editWorkoutUrl = 'edit_workout';


    //     // Add CSRF token to all jQuery AJAX requests
    //     $.ajaxSetup({
    //         headers: {
    //             'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
    //         }
    //     });

    //     $.ajax({
    //         type: 'POST',
    //         url: createWorkoutUrl,
    //         data: {
    //         'title': workoutTitle,
    //         'exercise_type': JSON.stringify(exercises),
            
    //         },
    //         success: function (response) {
    //         if (response.status === 'success') {
    //             alert('Workout saved successfully!');
    //         } else {
    //             alert('Failed to save workout.');
    //         }
    //         },
    //         error: function () {
    //         alert('An error occurred.');
    //         }
    //     });

    // });



    // Function to gather workout data
    function gatherWorkoutData() {
        const workoutTitle = document.getElementById('workout-title').innerText;
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

    // Function to send workout data to the backend
    function sendWorkoutData(url) {
        const workoutData = gatherWorkoutData();

        $.ajaxSetup({
            headers: {
                'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
            }
        });

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'title': workoutData.title,
                'exercise_type': JSON.stringify(workoutData.exercises),
            },
            success: function (response) {
                if (response.status === 'success') {
                    alert('Workout saved successfully!');
                } else {
                    alert('Failed to save workout.');
                }
            },
            error: function () {
                alert('An error occurred.');
            }
        });
    }

    // Button click handlers
    saveWorkoutButton.addEventListener('click', function () {
        sendWorkoutData('save_workout');
    });





});