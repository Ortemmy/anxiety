// Обработчик формы
document.getElementById('analyzeForm').addEventListener('submit', async function (event) {
    event.preventDefault(); // Отключаем стандартное поведение формы

    // Получаем текст из поля
    const text = document.getElementById('textInput').value;

    // Проверяем, что текст не пустой
    if (!text) {
        document.getElementById('result').textContent = 'Введите сообщение для анализа.';
        return;
    }

    try {
        // Отправляем POST-запрос к API
        const response = await fetch('http://127.0.0.1:8000/analyze', { // Укажите адрес вашего API
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text })
        });

        // Читаем ответ
        const data = await response.json();
        if (response.ok) {
            document.getElementById('result').textContent = `Оценка тревожности: ${data.anxiety_score}`;
        } else {
            document.getElementById('result').textContent = `Ошибка: ${data.detail || 'Невозможно проанализировать сообщение'}`;
        }
    } catch (error) {
        document.getElementById('result').textContent = 'Ошибка соединения с сервером.';
        console.error('Ошибка:', error);
    }
});
