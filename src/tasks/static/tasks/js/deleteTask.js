document.addEventListener("DOMContentLoaded", function () {
    const deleteButtons = document.querySelectorAll(".delete-task");
    deleteButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();
            
            const taskId = this.getAttribute("data-task-id");
            if (taskId) {
                const csrfToken = this.closest(".delete-form").querySelector("[name=csrfmiddlewaretoken]").value;
                
                fetch(`/dashboard/delete/${taskId}/`, {
                    method: 'DELETE',
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
                        console.error('Erro ao excluir a tarefa.');
                    }
                })
                .catch(error => {
                    console.error('Erro ao excluir a tarefa:', error);
                });
            }
        });
    });
    
    const completeButtons = document.querySelectorAll(".complete-task");
    completeButtons.forEach(button => {
        button.addEventListener("click", function () {
            const taskId = this.getAttribute("data-task-id");
            if (taskId) {
                // ...
            }
        });
    });
});