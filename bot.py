from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
import telegram.error

# Константы
TOKEN = '7806006262:AAF-FTDOU8WBzJCmT9Rjug8U7cm8cELVAW8'  # Токен бота
PHOTO_PATH = 'photo.jpg'  # Путь к фото
WELCOME_TEXT = "Привет! Моя специализация 'QA Automation Engineer'. Нажми кнопку, чтобы начать:"
MENU_TEXT = "Привет! Моя специализация 'QA Automation Engineer'. Выбери, что хочешь узнать обо мне:"

# Главное меню как константа
MAIN_MENU = [
    [InlineKeyboardButton("Обо мне", callback_data='about'), InlineKeyboardButton("Резюме (ссылка)", callback_data='resume')],
    [InlineKeyboardButton("Образование", callback_data='education'), InlineKeyboardButton("Опыт работы", callback_data='experience')],
    [InlineKeyboardButton("Навыки", callback_data='skills'), InlineKeyboardButton("Связаться", callback_data='contacts')],
]

# Данные резюме в словаре
RESUME_DATA = {
    'about': (
        "Привет! Меня зовут Чистяков Сергей. Я 'QA Automation Engineer' с опытом создания автоматизированных тестов для обеспечения качества ПО.\n\n"
        "Веду научную деятельность на языке программирования Python в университете, в рамках обучения в аспирантуре. "
        "И, исходя из этого, в последнее время для себя активно изучаю фреймворки для тестирования Pytest и Selenium.\n\n"
        "В настоящий момент активно ищу работу.\n\n"
        "💰 **Ожидаемая зарплата**: от 220 000 рублей в месяц."
    ),
    'resume': "https://ekaterinburg.hh.ru/resume/8f53e19bff0e7060040039ed1f6d6f34497977",
    'education': (
        "🎓 **Образование**\n"
        "- **Уральский федеральный университет имени первого Президента России Б.Н. Ельцина**\n"
        "  Институт радиоэлектроники и информационных технологий\n"
        "  Системный анализ, управление и обработка информации\n"
        "  Аспирантура, 2022–2025\n\n"
        "- **Уральский федеральный университет имени первого Президента России Б.Н. Ельцина**\n"
        "  Институт радиоэлектроники и информационных технологий\n"
        "  Информационные системы и технологии\n"
        "  Магистратура, 2019–2022\n\n"
        "- **Югорский государственный университет, Ханты-Мансийск**\n"
        "  Программная инженерия\n"
        "  Бакалавриат, 2022–2025\n"
    ),
    'experience': (
        "💼 **Опыт работы**\n"
        "- **Ведущий тестировщик, ООО 'ПочтаТех'**\n"
        "  Июнь 2024 – настоящее время\n"
        "  Разработка и запуск автотестов для нетиповой конфигурации 1С с помощью фреймворка Vanessa automation с нуля (язык программирования Gherkin и 1С).\n"
        "  - Проведение интеграционного, регрессионного, смоук тестирования на базе реализованных автотестов.\n"
        "  - Обработка файлов формата json.\n"
        "  - Участие в создании Mock-сервера с помощью Postman для имитации взаимодействия сервисов и стабилизации тестов и тестировании API.\n"
        "  - Анализ прохождения тестов с помощью фреймворка Allure.\n"
        "  - Заведение тест-кейсов на платформе Confluence.\n"
        "  - Участие в внедрении и настройке GitLab CI/CD.\n"
        "  - Использование gitlab как системы контроля версий и запуск автотестов.\n"
        "  - Использование среды разработки прикладных решений 1С:EDT для тестирования.\n"
        "  - Активное использование Jira для командной работы над проектом и в части заведения и обработки дефектов.\n"
        "  - Проведение обучения коллег работы с фреймворком Vanessa automation.\n\n"
        "- **Тестировщик 1С, ООО 'Верные цифровые решения'**\n"
        "  Апрель 2024 – Июнь 2024\n"
        "  Разработка и запуск автотестов для конфигурации 1С:Розница и 1С:УправлениеТорговлей с помощью фреймворка Vanessa automation с нуля (язык программирования Gherkin и 1С).\n"
        "  - Проведение регрессионного тестирования на базе реализованных автотестов.\n"
        "  - Анализ прохождения тестов с помощью фреймворка Allure.\n"
        "  - Заведение тест-кейсов на платформе Confluence.\n"
        "  - Использование gitlab как системы контроля версий и запуск автотестов.\n"
        "  - Активное использование Jira для командной работы над проектом и в части заведения и обработки дефектов.\n\n"
        "- **Тестировщик, ООО 'ГРИ'**\n"
        "  Февраль 2023 – Апрель 2024\n"
        "  Разработка автотестов на языке программирования 1С (фреймворк “xUnitFor1C”).\n"
        "  - Запуск тестов через Jenkins.\n"
        "  - Проведение регрессионного тестирования на базе реализованных автотестов.\n"
        "  - Анализ прохождения тестов с помощью фреймворка Allure.\n"
        "  - Участие в создании Mock-сервера с помощью Postman для имитации взаимодействия сервисов и стабилизации тестов и тестировании API.\n"
        "  - Заведение тест-кейсов на платформе TestRail.\n"
        "  - Использование gitlab как системы контроля версий.\n"
        "  - Активное использование Jira для командной работы над проектом и в части заведения и обработки дефектов.\n\n"
        "- **Специалист автоматизированного тестирования, ООО 'РОСЛАБСИСТЕМ'**\n"
        "  Октябрь 2022 – Февраль 2023\n"
        "  Разработка и запуск автотестов для нетиповой конфигурации 1С с помощью фреймворка Vanessa automation с нуля (язык программирования Gherkin и 1С).\n"
        "  - Проведение регрессионного тестирования на базе реализованных автотестов.\n"
        "  - Анализ прохождения тестов с помощью фреймворка Allure.\n"
        "  - Заведение тест-кейсов на базе знаний wiki компании.\n"
        "  - Использование gitlab как системы контроля версий.\n"
        "  - Проведение обучения коллег работы с фреймворком Vanessa automation.\n\n"
        "- **Инженер-программист 2 категории, АО 'Промэлектроника'**\n"
        "  Ноябрь 2020 – Июнь 2022\n"
        "  - Организация работы с помощью Jira.\n"
        "  - Написание скриптов под ОС Astra Linux (#!/bin/bash).\n"
        "  - Разработка на языке Delphi.\n"
        "  - Работа с тестирующим комплексом: поиск проблем и решений, чтение логов, функциональное и регрессионное тестирование.\n"
        "  - Написание и поддержка актуальности инструкций.\n"
        "  - Работа с инструментом контроля версий (svn).\n"
        "  - Работа с разными виртуальными машинами (virtualbox).\n\n"
        "- **Тестировщик, ОАО 'Уральский приборостроительный завод'**\n"
        "  Февраль 2020 – Ноябрь 2020\n"
        "  Тестирование ПО медицинского оборудования (аппараты искусственной вентиляции легких).\n"
    ),
    'skills': (
        "🛠 **Ключевые навыки**\n"
        "- Языки: Python, Java (основы), 1С\n"
        "- Инструменты автоматизации: Selenium, Pytest, Postman, Vanessa Automation\n"
        "- CI/CD: Jenkins, GitLab CI\n"
        "- Тестирование: API, Web, Mobile, 1С\n"
        "- Базы данных: PostgreSQL, MySQL (основы)\n"
    ),
    'contacts': (
        "📩 Связаться со мной:\n"
        "- Email: wumyup@gmail.com\n"
        "- Telegram: @serezha_baller\n"
        "- Телефон: +7 (982) 147-50-94"
    )
}

# Утилитная функция для отправки сообщений
async def send_message(chat_id: int, text: str, reply_markup: InlineKeyboardMarkup, context: ContextTypes.DEFAULT_TYPE, parse_mode: str = 'Markdown') -> int:
    """Отправляет сообщение и возвращает его ID"""
    try:
        if parse_mode == 'Markdown':
            message = await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup, parse_mode=parse_mode, disable_web_page_preview=False)
        else:
            message = await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup, parse_mode=None)
    except telegram.error.BadRequest as e:
        print(f"Markdown parsing error: {e} in text: {text}")
        message = await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup, parse_mode=None)
    return message.message_id

# Утилитная функция для отправки фото
async def send_photo_message(chat_id: int, text: str, reply_markup: InlineKeyboardMarkup, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Отправляет фото с подписью или текст, возвращает ID сообщения"""
    try:
        with open(PHOTO_PATH, 'rb') as photo:
            message = await context.bot.send_photo(chat_id=chat_id, photo=photo, caption=text, reply_markup=reply_markup)
    except FileNotFoundError:
        message = await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup, parse_mode=None)
    return message.message_id

# Утилитная функция для удаления предыдущего сообщения
async def delete_previous_message(chat_id: int, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Удаляет предыдущее сообщение, если оно существует"""
    if 'last_message_id' in context.user_data:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['last_message_id'])
        except telegram.error.BadRequest:
            pass  # Игнорируем ошибку, если сообщение уже удалено

# Обработка первого сообщения
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Показывает кнопку 'Начать' при первом сообщении"""
    keyboard = [[InlineKeyboardButton("Начать", callback_data='start')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message_id = await send_message(update.message.chat_id, WELCOME_TEXT, reply_markup, context, parse_mode=None)
    context.user_data['menu_message_id'] = message_id

# Логика главного меню
async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отображает главное меню с фото"""
    query = update.callback_query if update.callback_query else None
    if query:
        await query.answer()
        chat_id = query.message.chat_id
    else:
        chat_id = update.message.chat_id

    # Удаляем сообщение с кнопкой "Начать", если оно есть
    if 'menu_message_id' in context.user_data:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=context.user_data['menu_message_id'])
        except telegram.error.BadRequest:
            pass
        del context.user_data['menu_message_id']

    reply_markup = InlineKeyboardMarkup(MAIN_MENU)
    message_id = await send_photo_message(chat_id, MENU_TEXT, reply_markup, context)
    context.user_data['menu_message_id'] = message_id

# Обработка нажатий на кнопки
async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает нажатия на кнопки, заменяя предыдущее сообщение"""
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id

    if query.data == 'start':
        await show_main_menu(update, context)
        return

    # Удаляем предыдущее сообщение с информацией, если оно есть
    await delete_previous_message(chat_id, context)

    # Формирование текста для выбранного раздела
    text = f"Вот ссылка на мое резюме:\n[{RESUME_DATA['resume']}]({RESUME_DATA['resume']})" if query.data == 'resume' else RESUME_DATA[query.data]
    parse_mode = 'Markdown' if query.data != 'contacts' else None  # Отключаем Markdown для contacts

    # Отправляем новое сообщение и сохраняем его ID
    message_id = await send_message(chat_id, text, None, context, parse_mode)
    context.user_data['last_message_id'] = message_id

# Главная функция
def main() -> None:
    """Инициализация и запуск бота"""
    app = Application.builder().token(TOKEN).build()

    # Регистрация обработчиков
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, welcome))
    app.add_handler(CommandHandler("start", show_main_menu))
    app.add_handler(CallbackQueryHandler(handle_button, pattern='^(about|resume|education|experience|skills|contacts|start)$'))

    # Запуск бота
    app.run_polling()

if __name__ == '__main__':
    main()