document.addEventListener("DOMContentLoaded", async function() {

    // Проверяем, находимся ли мы на главной странице или на странице home
    if (window.location.pathname === "/" || window.location.pathname === "/home") {
        // Выполняем запрос для загрузки контента
        fetchHomeContent();
    }
    else if(window.location.pathname === "/article") {
        fetchArticleContent();
    }
    else if(window.location.pathname === "/publisher") {
        fetchPublisherContent();
    }
});

function fetchHomeContent() {
    // Выполняем запрос к серверу для получения контента для главной страницы
    fetch('/home-content')
        .then(response => response.json())
        .then(data => {
            var mainContent = document.getElementById("main-content");
            mainContent.innerHTML = data.content; // Используем свойство content для замены содержимого div'а
        })
        .catch(error => console.error('Ошибка при загрузке контента для главной страницы:', error));
};

function fetchArticleContent() {
    fetch('/article-content')
        .then(response => response.json())
        .then(data => {
            var mainContent = document.getElementById("main-content");
            mainContent.innerHTML = data.content; // Используем свойство content для замены содержимого div'а
        })
        .catch(error => console.error('Ошибка при загрузке контента для страницы article:', error));
};

function fetchPublisherContent() {
    fetch('/publisher-content')
        .then(response => response.json())
        .then(data => {
            var mainContent = document.getElementById("main-content");
            mainContent.innerHTML = data.content; // Используем свойство content для замены содержимого div'а
        })
        .catch(error => console.error('Ошибка при загрузке контента для страницы publisher:', error));
};