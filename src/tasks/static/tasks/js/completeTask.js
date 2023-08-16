document.addEventListener("DOMContentLoaded", function () {
    const completeButtons = document.querySelectorAll(".complete-task");
    completeButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();
            
            const taskId = this.getAttribute("data-task-id");
            if (taskId) {
                const csrfToken = this.closest(".complete-form").querySelector("[name=csrfmiddlewaretoken]").value;
                
                fetch(`/dashboard/complete/${taskId}/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        window.location.reload();
                    } else {
                        console.error('Erro ao completar a tarefa.');
                    }
                })
                .catch(error => {
                    console.error('Erro ao completar a tarefa:', error);
                });
            }
        });
    });
});