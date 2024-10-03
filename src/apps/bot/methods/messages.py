from types import SimpleNamespace


class Messages(SimpleNamespace):
    start = {
        'uz': '<b>Assalomu alaykum!</b>\n\nLuxe Cleaning xizmati botiga xush kelibsiz! Bu yerda sizning buyurtmalarizni qabul qilish, ularni amalga oshirish va boshqa xizmatlarimiz haqida ma\'lumot olishingiz mumkin. Iltimos, quyidagi til tanlash tugmasini bosing.',
        'ru': '<b>Здравствуйте!</b>\n\nДобро пожаловать в бот службы Luxe Cleaning! Здесь вы можете принимать ваши заказы, выполнять их и получать информацию о наших других услугах. Пожалуйста, выберите язык, нажав на кнопку ниже.',
        'en': '<b>Hello!</b>\n\nWelcome to the Luxe Cleaning service bot! Here you can take your orders, execute them, and get information about our other services. Please select a language by pressing the button below.'
    }

    base = {
        'uz': "Menyudan kerakli bo'limni tanlang:",
        'ru': "Выберите нужный раздел из меню:",
        'en': "Choose the required section from the menu:"
    }

    base_menu = {
        'uz': ["🧾 Xizmatlar", "👮‍♂️ Biz haqimizda 🏪", "📞 Aloqa", "⚙️ Sozlamalar"],
        'ru': ["🧾 Услуги", "👮‍♂️ О нас 🏪", "📞 Контакты", "⚙️ Настройки"],
        'en': ["🧾 Services", "👮‍♂️ About us 🏪", "📞 Contacts", "⚙️ Settings"]
    }

    services = {
        'uz': 'Xizmatlar bo\'limi',
        'ru': 'Раздел услуг',
        'en': 'Services section'
    }

    about = {
        'uz': 'Biz haqimizda bo\'limi',
        'ru': 'Раздел о нас',
        'en': 'About us section'
    }

    contact = {
        'uz': 'Aloqa bo\'limi',
        'ru': 'Раздел контактов',
        'en': 'Contacts section'
    }

    settings = {
        'uz': 'Sozlamalar bo\'limi',
        'ru': 'Раздел настроек',
        'en': 'Settings section'
    }

    help = {
        'uz': 'Yordam bo\'limi',
        'ru': 'Раздел помощи',
        'en': 'Help section'
    }
