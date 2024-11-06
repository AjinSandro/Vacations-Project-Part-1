document.addEventListener("DOMContentLoaded", function() {
    const likeButtons = document.querySelectorAll(".like-button"); // Gets all card buttons

    likeButtons.forEach(button => {
        button.addEventListener("click", async function() {  
            const vacation_id = this.dataset.vacation_id; // Gets VacationId of the card
            const isLiked = this.classList.contains("liked"); // Check if the vacation is liked (boolean)
            console.log(vacation_id)
            const url = isLiked ? `/vacations/unlike_vacation/${vacation_id}` : `/vacations/like_vacation/${vacation_id}`;
            const icon = this.querySelector("i"); // Get the like icon
            const likesCounter = this.querySelector(".countLikes");

            try {
                const response = await fetch(url, {  // receives data from view in jason format
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": "{{ csrf_token() }}" // CSRF protection
                    }
                });

                const data = await response.json(); // turns data to dictionary

                if (data.success) {
                    this.classList.toggle("liked");

                    // Update the icon and like count using the server-returned data
                    if (isLiked) {
                        icon.classList.remove("fas"); // Remove like icon
                        icon.classList.add("far"); // Add unlike icon
                    } else {
                        icon.classList.remove("far");
                        icon.classList.add("fas");
                    }
                    // Use the likeCount from the server response
                    likesCounter.textContent = data.LikeCount;
                    this.dataset.LikeCount = data.LikeCount; // Update the data attribute
                } else {
                    alert(data.message);
                }
            } catch (error) {
                console.error('Error:', error);
                alert("An error occurred. Please try again later.");
            }
        });
    });
});


function confirmDelete(){
    const ok = confirm("Are you sure ?")
    if(!ok){
        event.preventDefault()
    }
}

function AlertRegistration(){
    alert("Your registration has been completed !")
}

function TicketSubmissionAlert(){
    alert("Your ticket has been submitted !")
}