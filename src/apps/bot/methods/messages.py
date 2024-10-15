from types import SimpleNamespace
from apps.models import Footer


class Messages(SimpleNamespace):
    numbers = {
        '1': '1️⃣',
        '2': '2️⃣',
        '3': '3️⃣',
        '4': '4️⃣',
        '5': '5️⃣',
        '6': '6️⃣',
        '7': '7️⃣',
        '8': '8️⃣',
        '9': '9️⃣',
        '0': '0️⃣',
    }
    start = {
        'uz': '<b>Assalomu alaykum!</b>\n\nLuxe Cleaning xizmati botiga xush kelibsiz! Bu yerda sizning buyurtmalarizni qabul qilish, ularni amalga oshirish va boshqa xizmatlarimiz haqida ma\'lumot olishingiz mumkin. Iltimos, quyidagi til tanlash tugmasini bosing.',
        'ru': '<b>Здравствуйте!</b>\n\nДобро пожаловать в бот службы Luxe Cleaning! Здесь вы можете принимать ваши заказы, выполнять их и получать информацию о наших других услугах. Пожалуйста, выберите язык, нажав на кнопку ниже.',
        'en': '<b>Hello!</b>\n\nWelcome to the Luxe Cleaning service bot! Here you can take your orders, execute them, and get information about our other services. Please select a language by pressing the button below.'
    }

    back = {
        'uz': '⬅️ Orqaga',
        'ru': '⬅️ Назад',
        'en': '⬅️ Back'
    }

    base = {
        'uz': "Menyudan kerakli bo'limni tanlang: 👇",
        'ru': "Выберите нужный раздел из меню: 👇",
        'en': "Choose the required section from the menu: 👇"
    }

    succes_msg = {
        'uz': "Vazifa muvaffaqiyatli amalga oshirildi!",
        'ru': "Задание успешно выполнено!",
        'en': "The task was successfully completed!"
    }

    base_menu = {
        'uz': ["✅ Xizmatni buyurtma qiling", "🤵🏻‍♂️ Korporativ mijozlar uchun", "💰 Xizmatlar va narxlar", "🆕 Aksiya",
               "🆘 FAQ-Menejer bilan bog'lanish", "☎️ Kontaktlar", "🗑 Mening buyurtmalarim", "⚙️ Sozlamalar"],
        'ru': ["✅ Оформить заказ", "🤵🏻‍♂️ Для корпоративных клиентов", "💰 Услуги и цены", "🆕 Акция",
               "🆘 FAQ-Связаться с менеджером", "☎️ Контакты", "🗑 Мои заказы", "⚙️ Настройки"],
        'en': ["✅ Place an order", "🤵🏻‍♂️ For corporate clients", "💰 Services and prices", "🆕 Promotion",
               "🆘 FAQ-Contact the manager", "☎️ Contacts", "🗑 My orders", "⚙️ Settings"]
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

    settings = {
        'uz': '<i>⚙️ Sozlamalar bo\'limiga xush kelibsiz!</i>',
        'ru': '<i>⚙️ Добро пожаловать в раздел настроек!</i>',
        'en': '<i>⚙️ Welcome to the settings section!</i>'
    }

    choose_language = {
        'uz': '<i>🌍 Tilni tanlang</i>',
        'ru': '<i>🌍 Выберите язык</i>',
        'en': '<i>🌍Choose language</i>'
    }

    help = {
        'uz': 'Yordam bo\'limi',
        'ru': 'Раздел помощи',
        'en': 'Help section'
    }

    corporate_clients = {
        'uz': """
💼 <b>Korporativ mijozlar bo'limiga xush kelibsiz !</b>

Hurmatli <code>{}</code>,

Korporativ mijozlar bo'limiga murojaat qilganingiz uchun tashakkur. Biz sizning biznesingizni qadrlaymiz va sizning maxsus ehtiyojlaringiz bo'yicha sizga yordam berishga tayyormiz.

Iltimos, <code>{}</code> ga qo'ng'iroq qilish orqali biz bilan bevosita bog'laning. Agar xohlasangiz, ushbu xatga oddiygina javob berishingiz mumkin va biz siz bilan eng qisqa vaqt ichida bog'lanamiz.

Biz sizning biznesingizni qo'llab-quvvatlashni intiqlik bilan kutamiz!

<i>Eng yaxshi ezgu tilaklar bilan</i>: <code>Luxe Cleaning</code>
""",
        'ru': """
💼 <b>Добро пожаловать в раздел корпоративных клиентов!</b>

Уважаемый {},

Спасибо за обращение в раздел корпоративных клиентов. Мы ценим ваш бизнес и готовы помочь вам в решении ваших специальных потребностей.

Пожалуйста, свяжитесь с нами напрямую, позвонив по номеру {}. Если хотите, вы можете просто ответить на это сообщение и мы свяжемся с вами в кратчайшие сроки.

Мы с нетерпением ждем возможности поддержать ваш бизнес!

С наилучшими пожеланиями,

Luxe Cleaning
""",
    }

    succesfuly_corporate_clients = {
        'uz': "✅ Xabaringiz muvaffaqiyatli qabul qilindi! Biz tez orada siz bilan bog'lanamiz.",
        'ru': "✅ Ваше сообщение успешно получено! Мы свяжемся с вами в ближайшее время.",
        'en': "✅ Your message has been successfully received! We will contact you shortly."
    }

    send_phone_keyb = {
        'uz': "📞 Telefon raqamni yuborish",
        'ru': "📞 Отправить номер телефона",
        'en': "📞 Send phone number"
    }

    discount = {
        'uz': """
<b>Chegirmalar bo'limiga xush kelibsiz! 🎉</b>

Mana siz uchun hozirgi maxsus takliflarimiz:

{}

Eng yaxshi ezgu tilaklar bilan,<code> Luxe Cleaning</code>
""",
        'ru': """
<b>Добро пожаловать в раздел скидок! 🎉</b>

Вот наши текущие специальные предложения:

{}
С наилучшими пожеланиями, <code>Luxe Cleaning</code>
"""
    }

    faq_and_connection = {
        'uz': """
🆘 <b>FAQ-Menejer bilan bog'lanish</b>

Tez-tez so'raladigan savollar bo'yicha ma'lumot:

{}

Agar sizda boshqa savollar bo'lsa, iltimos, biz bilan bog'laning: <code>{}</code>

Eng yaxshi ezgu tilaklar bilan,<code> Luxe Cleaning</code>
""",
        'ru': """
🆘 <b>FAQ-Связаться с менеджером</b>
        
Информация по часто задаваемым вопросам:

{}
Если у вас есть другие вопросы, пожалуйста, свяжитесь с нами: <code>{}</code>
        
С наилучшими пожеланиями, <code>Luxe Cleaning</code>
"""
    }

    @staticmethod
    def get_contact_msg_uz(footer: Footer):
        get_location = lambda: f"https://www.google.com/maps/@{footer.longitude},{footer.latitude},13z?hl=en-US&entry=ttu&g_ep=EgoyMDI0MTAwOS4wIKXMDSoASAFQAw%3D%3D" if footer.longitude and footer.latitude else ""

        phone1 = "📞 Telefon: " + (footer.phone1 if footer.phone1 else "") + "\n"
        phone2 = "📞 Telefon: " + (footer.phone2 if footer.phone2 else "") + "\n"
        email = ("📧 Elektron pochta: " + footer.email if footer.email else "") + "\n"
        location = ("📍 Joylashuv: " + "<a href='{}'>Xarita</a>".format(get_location()) if get_location() else "")
        telegram = ("<a href='{}'>📱 Telegram</a>".format(footer.telegram) if footer.telegram else "") + "\n"
        instagram = ("<a href='{}'>📷 Instagram</a>".format(footer.instagram) if footer.instagram else "") + "\n"
        youtube = ("<a href='{}'>📺 YouTube</a>".format(footer.youtube) if footer.youtube else "") + "\n"
        facebook = ("<a href='{}'>📘 Facebook</a>".format(footer.facebook) if footer.facebook else "") + "\n"

        return f"""
<b>Bizga murojaat qilganingiz uchun tashakkur!</b>
    
Biz bilan quyidagi kanallardan biri orqali bog'lanishingiz mumkin:
    
{phone1}{phone2}{email}{telegram}{instagram}{youtube}{facebook}{location}
🌐 Veb-sayt: luxecleaning.uz
O'zingiz uchun eng qulay yo'lni tanlang va biz sizga yordam berishdan xursand bo'lamiz!
    
Eng yaxshi ezgu tilaklar bilan, <code>Luxe Cleaning</code>
    """

    @staticmethod
    def get_contact_msg_ru(footer: Footer):
        get_location = lambda: f"https://www.google.com/maps/@{footer.longitude},{footer.latitude},13z?hl=en-US&entry=ttu&g_ep=EgoyMDI0MTAwOS4wIKXMDSoASAFQAw%3D%3D" if footer.longitude and footer.latitude else ""

        phone1 = "📞 Телефон: " + (footer.phone1 if footer.phone1 else "") + "\n"
        phone2 = "📞 Телефон: " + (footer.phone2 if footer.phone2 else "") + "\n"
        email = ("📧 Электронная почта: " + footer.email if footer.email else "") + "\n"
        location = ("📍 Местонахождение: " + "<a href='{}'>Карта</a>".format(get_location()) if get_location() else "")
        telegram = ("<a href='{}'>📱 Telegram</a>".format(footer.telegram) if footer.telegram else "") + "\n"
        instagram = ("<a href='{}'>📷 Instagram</a>".format(footer.instagram) if footer.instagram else "") + "\n"
        youtube = ("<a href='{}'>📺 YouTube</a>".format(footer.youtube) if footer.youtube else "") + "\n"
        facebook = ("<a href='{}'>📘 Facebook</a>".format(footer.facebook) if footer.facebook else "") + "\n"

        return f"""
<b>Спасибо, что обратились к нам!</b>

Вы можете связаться с нами по одному из следующих каналов:

{phone1}{phone2}{email}{telegram}{instagram}{youtube}{facebook}{location}
🌐 Сайт: luxecleaning.uz
Выбирайте наиболее удобный для вас способ и мы будем рады вам помочь!

С наилучшими пожеланиями, <code>Luxe Cleaning</code>
            """