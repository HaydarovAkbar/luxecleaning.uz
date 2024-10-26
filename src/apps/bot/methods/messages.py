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
        'uz': ["✅ Xizmatni buyurtma qiling", "🤵🏻‍♂️ Korporativ mijozlar uchun", "💰 Narxlar", "🆕 Aksiya va sikidka",
               "🆘 FAQ", "☎️ Kontaktlar", "🗑 Mening buyurtmalarim", "⚙️ Sozlamalar", "💬 Menejer bilan bog'lanish"],
        'ru': ["✅ Заказать услугу", "🤵🏻‍♂️ Для корпоративных клиентов", "💰 Услуги", "🆕 Акции и скидки",
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
        telegram = ("<a href='{}'>📱 Telegram</a>\n".format(footer.telegram) if footer.telegram else "")
        instagram = ("<a href='{}'>📷 Instagram</a>\n".format(footer.instagram) if footer.instagram else "")
        youtube = ("<a href='{}'>📺 YouTube</a>\n".format(footer.youtube) if footer.youtube else "")
        facebook = ("<a href='{}'>📘 Facebook</a>\n".format(footer.facebook) if footer.facebook else "")

        return f"""
<b>Bizga murojaat qilganingiz uchun tashakkur!</b>
    
Biz bilan quyidagi kanallardan biri orqali bog'lanishingiz mumkin:
    
{phone1}{phone2}{email}{telegram}{instagram}{youtube}{facebook}🌐 luxecleaning.uz

{location}

O'zingiz uchun eng qulay yo'lni tanlang va biz sizga yordam berishdan xursand bo'lamiz!
    """

    @staticmethod
    def get_contact_msg_ru(footer: Footer):
        get_location = lambda: f"https://www.google.com/maps/@{footer.longitude},{footer.latitude},13z?hl=en-US&entry=ttu&g_ep=EgoyMDI0MTAwOS4wIKXMDSoASAFQAw%3D%3D" if footer.longitude and footer.latitude else ""

        phone1 = "📞 Телефон: " + (footer.phone1 if footer.phone1 else "") + "\n"
        phone2 = "📞 Телефон: " + (footer.phone2 if footer.phone2 else "") + "\n"
        email = ("📧 Электронная почта: " + footer.email if footer.email else "") + "\n"
        location = ("📍 Расположение: " + "<a href='{}'>Карта</a>".format(get_location()) if get_location() else "")
        telegram = ("<a href='{}'>📱 Telegram</a>\n".format(footer.telegram) if footer.telegram else "")
        instagram = ("<a href='{}'>📷 Instagram</a>\n".format(footer.instagram) if footer.instagram else "")
        youtube = ("<a href='{}'>📺 YouTube</a>\n".format(footer.youtube) if footer.youtube else "")
        facebook = ("<a href='{}'>📘 Facebook</a>\n".format(footer.facebook) if footer.facebook else "")

        return f"""
<b>Спасибо, что обратились к нам!</b>

Вы можете связаться с нами по одному из следующих каналов:

{phone1}{phone2}{email}{telegram}{instagram}{youtube}{facebook}🌐 luxecleaning.uz

{location}

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
        'uz': "✅ Telefon raqamingiz muvaffaqiyatli o'zgartirildi! Iltimos ismingizni yuboring.",
        'ru': "✅ Ваш номер телефона успешно изменен! Пожалуйста, отправьте свое имя."
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
        'uz': "📹 Narxni aniqroq aniqlash uchun mulk haqidagi maʼlumotlarni, shuningdek, fotosurat yoki videoni yuboring.",
        'ru': "📹 Пожалуйста, отправьте информацию об объекте, а также фото или видео для более точного определения цены."
    }

    btv = {
        'uz': "<b>Bizning xizmatimizdan foydalanish uchun</b>",
        'ru': "<b>Чтобы использовать наш сервис</b>"
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
        'uz': "📃 Iltimos! xizmatlarimizdan birini tanlang 👇",
        'ru': "📃 Пожалуйста! выберите одну из наших услуг 👇"
    }
    get_service_type_msg = {
        'uz': """
<b>🎉 Hurmatli mijoz!</b>

Biz sizga bog'lanishimiz uchun kerakli ma'lumotlarni kiriting:
    """,
        'ru': """
<b>🎉 Уважаемый клиент!</b>

Пожалуйста, введите необходимую информацию для связи с вами:
    """
    }

    def get_order_status(self, status: str, lang: str):
        if lang == 'uz':
            if status == 'pending':
                return '🕞 Kutilmoqda'
            elif status == 'completed':
                return '✅ Yakunlandi'
            elif status == 'canceled':
                return '🚫 Bekor qilindi'
        else:
            if status == 'pending':
                return '🕞 Ожидается'
            elif status == 'completed':
                return '✅ Выполнено'
            elif status == 'canceled':
                return '🚫 Отменено'

    service_price = {
        'ru': """
✳️ <b>Благодарим за интерес к нашим услугам!</b>

Услуги, которые мы предлагаем :


🔸 <b>Уборка коммерческих помещений (офисы, рестораны, отели и др.)</b>

🏢 <b>до 100 м²</b>
💰 1 000 000 – 2 000 000 сум (один раз)
💰 4 000 000 - 8 000 000 сум (регулярно)

🏢 <b>100 - 500 м²</b>
💰 2 000 000 – 4 000 000 сум (один раз)
💰 4 000 000 - 12 000 000 сум (регулярно)

🏢 <b>более 500 м²</b>
💰 4 000 000 и выше (один раз)
💰 12 000 000 и выше (регулярно)


🔸 <b>Уборка частных домов</b>

🏢 <b>до 500 м²</b>
💰 2 000 000 – 4 000 000 сум (один раз)
💰 4 000 000 - 12 000 000 сум (регулярно)

🏢 <b>более 500 м²</b>
💰 4 000 000 и выше (один раз)
💰 12 000 000 и выше (регулярно)


🔸 <b>Уборка квартир</b>

🏢 <b>1 комната</b>
💰 800 000 - 1 200 000 сум (один раз)
💰 4 000 000 - 6 000 000 сум (регулярно)

🏢 <b>2 комнаты</b>
💰 1 000 000 - 1 500 000 сум (один раз)
💰 4 000 000 - 8 000 000 сум (регулярно)

🏢 <b>3 комнаты</b>
💰 1 200 000 – 2 500 000 сум (один раз)
💰 6 000 000 и выше (регулярно)

🏢 <b>4 комнаты и больше</b>=
💰 1 600 000 и выше (один раз)
💰 6 000 000 и выше (регулярно)


🔸 <b>Уборка после ремонта</b>

🏠 <b>до 100 м²</b>
💰 1 800 000 – 3 000 000 сум

🏠 <b>100 - 500 м²</b>
💰 2 500 000 – 4 000 000 сум 

🏠 <b>более 500 м²</b>
💰 3 600 000 и выше


🔸 <b>Специальные услуги</b>

🪟 <b>Мытье окон (за м²)</b>
💰 20 000 – 30 000 сум

🏢 <b>Мытье фасадов (за м²)</b>
💰 15 000 - 25 000 сум

🧼 <b>Мытье брусчатки и цоколя (за м²)</b>
💰 15 000 - 25 000 сум

🍽 <b>Мытье посуды (за 1 час)</b>
💰 80 000 сум (один раз)


<b>Свяжитесь с нами для получения дополнительной информации или заказа услуги!</b>
""",
        'uz': """
✳️ <b>Xizmatlarimizga qiziqishingiz uchun rahmat!</b>

Bizning taklif etgan xizmatlar:

🔸 <b>Kommerciyal joylar (ofislar, restoranlar, mehmonxonalar va boshqalar) uchun tozalash</b>

🏢 <b>100 m² gacha</b>
💰 1 000 000 – 2 000 000 so'm (bir marta)
💰 4 000 000 - 8 000 000 so'm (doimiy)

🏢 <b>100 - 500 m²</b>
💰 2 000 000 – 4 000 000 so'm (bir marta)
💰 4 000 000 - 12 000 000 so'm (doimiy)

🏢 <b>500 m² dan ortiq</b>
💰 4 000 000 va yuqori (bir marta)
💰 12 000 000 va yuqori (doimiy)


🔸 <b>Xususiy uy tozalash</b>

🏢 <b>500 m² gacha</b>
💰 2 000 000 – 4 000 000 so'm (bir marta)
💰 4 000 000 - 12 000 000 so'm (doimiy)

🏢 <b>500 m² dan ortiq</b>
💰 4 000 000 va yuqori (bir marta)
💰 12 000 000 va yuqori (doimiy)


🔸 <b>Kvartira tozalash</b>

🏢 <b>1 xona</b>
💰 800 000 - 1 200 000 so'm (bir marta)
💰 4 000 000 - 6 000 000 so'm (doimiy)

🏢 <b>2 xona</b>
💰 1 000 000 - 1 500 000 so'm (bir marta)
💰 4 000 000 - 8 000 000 so'm (doimiy)

🏢 <b>3 xona</b>
💰 1 200 000 – 2 500 000 so'm (bir marta)
💰 6 000 000 va yuqori (doimiy)

🏢 <b>4 xona va undan ko'p</b>
💰 1 600 000 va yuqori (bir marta)
💰 6 000 000 va yuqori (doimiy)


🔸 <b>Remontdan so'ng tozalash</b>

🏠 <b>100 m² gacha</b>
💰 1 800 000 – 3 000 000 so'm

🏠 <b>100 - 500 m²</b>
💰 2 500 000 – 4 000 000 so'm

🏠 <b>500 m² dan ortiq</b>
💰 3 600 000 va yuqori


🔸 <b>Xususiy xizmatlar</b>

🪟 <b>Oyni yuvish (m² bo'yicha)</b>
💰 20 000 – 30 000 so'm

🏢 <b>Fasadni yuvish (m² bo'yicha)</b>
💰 15 000 - 25 000 so'm

🧼 <b>Plitani yuvish (m² bo'yicha)</b>
💰 15 000 - 25 000 so'm

🍽 <b>Boshqaruvni yuvish (1 soat)</b>
💰 80 000 so'm (bir marta)


<b>Qo'shimcha ma'lumot yoki xizmat buyurtmasi uchun biz bilan bog'laning!</b>
"""
    }
