document.addEventListener('DOMContentLoaded', function () {
    const addSetButtons = document.querySelectorAll('.add-set-button');
    const deleteExerciseButtons = document.querySelectorAll('.delete-exercise-button');
    let exerciseToDelete = null;
    const saveWorkoutButton = document.getElementById('save-workout-btn');
    const updateWorkoutButton = document.getElementById('update-workout-btn');

    let workoutId = null;
    const workoutIdElement = document.getElementById('workout-id');
    if (workoutIdElement) {
        workoutId = workoutIdElement.value;
    }


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
    function sendWorkoutData(url, workoutId = null) {
        console.log("send workout data function triggered")
        const workoutData = gatherWorkoutData();

        // If a workout id is sent to the function then print it
        if(workoutId){
            console.log("The workout id is:",  workoutId)
            console.log("The url is:", url);
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
                } else {
                    alert(`Failed to ${workoutId ? 'update' : 'save'} workout.`);
                }
            },
            error: function () {
                alert('An error occurred.');
            }
        });
    }

    // Button click handlers
    if(saveWorkoutButton){
        saveWorkoutButton.addEventListener('click', function () {
            sendWorkoutData('save_workout');
        });
    }


    if(updateWorkoutButton){
        if(workoutId){
            updateWorkoutButton.addEventListener('click', function () {
                console.log("update workout button pressed");
                console.log("Workout id:" , workoutId);

                const updateWorkoutUrl = `/workouts/update_workout/`;  // Match the URL pattern
                sendWorkoutData(updateWorkoutUrl, workoutId);
            });
        }else{
            console.log("There is no workout Id");
        }
    }
   
    







});