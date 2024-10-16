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

    continiue_msg = {
        'uz': 'Davom etish ➡️',
        'ru': 'Продолжить ➡️',
        'en': 'Continue ➡️'
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
        'uz': ["✅ Xizmatni buyurtma qiling", "🤵🏻‍♂️ Korporativ mijozlar uchun", "💰 Narxlar", "🆕 Aksiya",
               "🆘 FAQ", "☎️ Kontaktlar", "🗑 Mening buyurtmalarim", "⚙️ Sozlamalar", "💬 Menejer bilan bog'lanish"],
        'ru': ["✅ Заказать услугу", "🤵🏻‍♂️ Для корпоративных клиентов", "💰 Цены", "🆕 Акция",
               "🆘 FAQ", "☎️ Контакты", "🗑 Мои заказы", "⚙️ Настройки", "💬 Связаться с менеджером"],
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
""",
        'ru': """
💼 <b>Добро пожаловать в раздел корпоративных клиентов!</b>

Уважаемый {},

Спасибо за обращение в раздел корпоративных клиентов. Мы ценим ваш бизнес и готовы помочь вам в решении ваших специальных потребностей.

Пожалуйста, свяжитесь с нами напрямую, позвонив по номеру {}. Если хотите, вы можете просто ответить на это сообщение и мы свяжемся с вами в кратчайшие сроки.

Мы с нетерпением ждем возможности поддержать ваш бизнес!
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
""",
        'ru': """
<b>Добро пожаловать в раздел скидок! 🎉</b>

Вот наши текущие специальные предложения:

{}
"""
    }

    faq_and_connection = {
        'uz': """
🆘 <b>Tez-tez tushadigan savollarga javoblar:</b>

{}
""",
        'ru': """
🆘 <b>Ответы на часто задаваемые вопросы:</b>

{}
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
    """

    @staticmethod
    def get_contact_msg_ru(footer: Footer):
        get_location = lambda: f"https://www.google.com/maps/@{footer.longitude},{footer.latitude},13z?hl=en-US&entry=ttu&g_ep=EgoyMDI0MTAwOS4wIKXMDSoASAFQAw%3D%3D" if footer.longitude and footer.latitude else ""

        phone1 = "📞 Телефон: " + (footer.phone1 if footer.phone1 else "") + "\n"
        phone2 = "📞 Телефон: " + (footer.phone2 if footer.phone2 else "") + "\n"
        email = ("📧 Электронная почта: " + footer.email if footer.email else "") + "\n"
        location = ("📍 Расположение: " + "<a href='{}'>Карта</a>".format(get_location()) if get_location() else "")
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
            """

    use_service = {
        'uz': "Xizmatni buyurtma qilish ✅",
        'ru': "Оформить заказ ✅",
        'en': "Place an order ✅"
    }

    use_of_service_if_phone = {
        'uz': """
📝 <b>Xizmatni buyurtma qilish</b>

Iltimos, telefon raqamingiz to'g'riligini tekshiring!

☎️ Telefon raqam: {}

Agar raqam to'g'ri bo'lsa, quyidagi tugmani bosing. Aks holda, raqamingizni qayta yuboring.
""",
        'ru': """
📝 <b>Оформить заказ</b>
        
Пожалуйста, проверьте правильность вашего номера телефона!
        
☎️ Номер телефона: {}
        
Если номер верный, нажмите на кнопку ниже. В противном случае, отправьте свой номер еще раз.
""",
    }

    use_of_service_if_not_phone = {
        'uz': """
📝 <b>Xizmatni buyurtma qilish</b>
        
Iltimos, telefon raqamingizni yuboring!
""",
        'ru': """
📝 <b>Оформить заказ</b>
        
Пожалуйста, отправьте свой номер телефона!
""",
    }
    wrong_phone = {
        'uz': "❌ Noto'g'ri telefon raqam! Iltimos, raqamingizni qayta yuboring.",
        'ru': "❌ Неверный номер телефона! Пожалуйста, отправьте свой номер еще раз."
    }

    change_phone_success = {
        'uz': "✅ Telefon raqamingiz muvaffaqiyatli o'zgartirildi! Iltimos ism va familiyangizni yuboring.",
        'ru': "✅ Ваш номер телефона успешно изменен! Пожалуйста, отправьте свое имя и фамилию."
    }

    get_full_name = {
        'uz': "Iltimos, ism va familiyangizni yuboring.",
        'ru': "Пожалуйста, отправьте свое имя и фамилию."
    }
    succesfuly_order = {
        'uz': "✅ Buyurtmangiz muvaffaqiyatli qabul qilindi! Biz tez orada siz bilan bog'lanamiz.",
        'ru': "✅ Ваш заказ успешно принят! Мы свяжемся с вами в ближайшее время."
    }
    get_video = {
        'uz': "📹 Video yuboring, video orqali biz sizga aniqroq xizmatlarimizni taklif etamiz.",
        'ru': "📹 Отправьте видео, и мы предложим вам наши услуги более точно."
    }

    connection_with_admin = {
        'uz': """
<b>Xizmatlarimizni tanlaganingiz uchun tashakkur! 🎉</b>

Murojaatingizga tezda javob beramiz. Sizga yordam berishdan xursandmiz! 💬
""",
        'ru': """
<b>Спасибо за выбор наших услуг! 🎉</b>

Мы ответим на ваш запрос в ближайшее время. Мы рады помочь вам! 💬
"""
    }
    get_service_type = {
        'uz': "<b>Iltimos! xizmatlarimizdan birini tanlang</b>",
        'ru': "<b>Пожалуйста! выберите одну из наших услуг</b>"
    }
    get_service_type_msg = {
        'uz': """
<b>🎉 Hurmatli mijoz!</b>

Biz sizga bog'lanishimiz uchun kerakli ma'lumotlarni kiriting:

👉🏻 <b>Iltimos, telefon raqamingizni yuboring!</b>
    """,
        'ru': """
<b>🎉 Уважаемый клиент!</b>

Пожалуйста, введите необходимую информацию для связи с вами:

👉🏻 <b> Пожалуйста, пришлите свой номер телефона! </b>
    """
    }
