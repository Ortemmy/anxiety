// Обработчик формы
document.getElementById('analyzeForm').addEventListener('submit', async function (event) {
    event.preventDefault(); // Отключаем перезагрузку страницы

    // Получаем текст из текстового поля
    const text = document.getElementById('textInput').value;

    // Проверяем, что текст не пустой
    if (!text) {
        document.getElementById('result').textContent = 'Введите сообщение для анализа.';
        return;
    }

    try {
        // Отправляем запрос к API
        const response = await fetch('http://127.0.0.1:8000/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text }),
        });

        // Обрабатываем ответ
        const data = await response.json();
        if (response.ok) {
            // Отображаем результат в <div id="result">
            document.getElementById('result').textContent = `Оценка тревожности: ${data.anxiety_score}`;
        } else {
            document.getElementById('result').textContent = `Ошибка: ${data.detail || 'Невозможно проанализировать сообщение'}`;
        }
    } catch (error) {
        // Выводим сообщение об ошибке
        document.getElementById('result').textContent = 'Ошибка соединения с сервером.';
        console.error('Ошибка:', error);
    }
});
