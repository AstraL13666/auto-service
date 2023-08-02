from .re_edit import edit


class Library:

    def __init__(self):
        self.services = [f'{edit.smile.top} Диагностика', f'{edit.smile.top} ТО', f'{edit.smile.top} Шиномонтаж',
                         f'{edit.smile.wqm} Иное',
                         'Автомойка,\nполировка', 'Автостекла,\nзеркала', 'Выхлопная\nсистема', 'ГБО',
                         'Двигатель', 'Детейлинг', 'Замена\nжидкостей', 'Кондиционеры,\nотопление',
                         'Кузовной\nремонт', 'Подвеска', 'Рулевое\nуправление', 'Топливная\nсистема',
                         'Тормозная\nсистема', 'Трансмиссия', 'Установка доп.\nоборудования', 'Электро -\n оборудование'
                         ]

        self.auto_service = "Test AutoService - Предоставляем услуги по диагностике, " \
                            "ремонту Вашего авто по разумным ценам\n\n" \
                            f"{edit.reformat.style(preset='iu', string='Тестовый режим')}"

        self.sign_up = "По кнопке ниже вы можете посмотреть наш ассортимент, " \
                       "выбрать нужный Вам вариант и оформить заказ 😎\n\n" \
                       f"или нажмите [{edit.smile.wqm} {edit.reformat.style(preset='bu', string='иное')} ] " \
                       f"и напишите Ваши пожелания по ремонту\n\n" \
                       f"{edit.reformat.style(preset='iu', string='Тестовый режим')}"

        self.calls = "Выбери, пожалуйста из списка наиболее подходящий вариант обратной связи: \n\n" \
                     f"{edit.reformat.style(preset='iu', string='Тестовый режим')}"

        self.call_quest = [
            f"{edit.smile.call} Заказать звонок",
            f"{edit.smile.feed} Оставить отзыв",
            f"{edit.smile.quest} Задать вопрос",
            f"{edit.smile.menu} Меню"
        ]

        self.time_call = [
            "08:00 - 09:00",
            "09:00 - 10:00",
            "10:00 - 11:00",
            "11:00 - 12:00",
            "12:00 - 13:00",
            "13:00 - 14:00",
            "14:00 - 15:00",
            "15:00 - 16:00",
            "16:00 - 17:00",
            "17:00 - 18:00",
            "18:00 - 19:00",
            "19:00 - 20:00",
            "20:00 - 21:00"
        ]

        self.feedback = "Здесь Вы можете написать отзыв о работе нашего автосервиса! " \
                        "Мы всегда рады любым честным отзывам - так Вы помогаете нам повышать уровень сервиса " \
                        "и качество нашей продукции! " \
                        "Напишите Ваш отзыв ниже ⬇\n\n" \
                        f"{edit.reformat.style(preset='iu', string='Тестовый режим')}"

        self.choice = "Чтобы задать вопрос, пожалуйста, форму и 3 коротких вопросов:\n\n" \
                      f"{edit.reformat.style(preset='iu', string='Тестовый режим')}"

        self.route = "🚘 Перейдя в карту, нажмите кнопку 'Маршруты' и выберите удобный для вас навигатор, " \
                     "чтобы построить маршрут!\n\n" \
                     "Если по какой-либо причине Вам не удалось выбрать другой навигатор, нажмите меню " \
                     "(перейдите в карту, в правом верхнем углу три точки) и выберите нужный навигатор или скопируйте" \
                     "адрес ниже:\n\n" \
                     "<code>Краснодар, микрорайон Завод Измерительных Приборов, улица Тополиная Аллея, 3</code>\n\n" \
                     "Удачной поездки и ни гвоздя, ни железа!\n\n" \
                     f"{edit.reformat.style(preset='iu', string='Тестовый режим')}"
        self.address = "Краснодар, микрорайон Завод Измерительных Приборов, улица Тополиная Аллея, 3"
        self.address_lat = 45.068233
        self.address_lon = 38.994812

        self.history = "Вы к нам обращались 7 раз\n\n" \
                       "История последних 3 заказов:\n" \
                       "1) 07.05.2023 - ТО\n" \
                       "Проведена диагностика\n" \
                       "К оплате: 5 700 р\n\n" \
                       "2) 29.03.2023 - Шиномонтаж\n" \
                       "Смена резины зима-лето\n" \
                       "К оплате: 1 500 р\n\n" \
                       "3) 25.03.2023 - Иное\n" \
                       "Замена сальников коробки\n" \
                       "К оплате: 7 500 р\n\n" \
                       f"{edit.reformat.style(preset='iu', string='Тестовый режим')}"

    def sign_up_start(self, value):
        return f"Выбрано: {value}\n\n" \
               f"Напишите комментарий к Вашему обращению\n" \
               f"здесь Вы можете описать что Вас беспокоит и на что нам обратить внимание!\n\n" \
               f"{edit.reformat.style(preset='iu', string='Тестовый режим')}"

    def sign_up_finish(self, value):
        return f"{edit.smile.info} Тип обращения:\n" \
               f"{value['title']}\n\n" \
               f"{edit.smile.problem} Комментарий клиента:\n" \
               f"{value['problem']}\n\n" \
               f"Ваше обращение зарегистрировано! Скоро с Вами свяжется наш сотрудник для уточнения деталей\n\n" \
               f"{edit.reformat.style(preset='iu', string='Тестовый режим')}"

    def call(self, value):
        txt = f"{self.call_quest[0]}\n\n" \
              f"{edit.smile.info} Информация:\n" \
              f"{edit.reformat.style(preset='b', string='Клиент:')} {value['name']}\n" \
              f"{edit.reformat.style(preset='b', string='Номер телефона:')} {value['number']}\n" \
              f"{edit.reformat.style(preset='b', string='Желаемое время:')} {value['time']}\n\n" \
              "Спасибо за обращение! С Вами скоро свяжется наш менеджер 😎\n\n" \
              f"{edit.reformat.style(preset='iu', string='Тестовый режим')}"
        return txt

    def send_fb(self, value):
        txt = f"{self.call_quest[1]}\n\n" \
              f"{edit.smile.info} Отзыв:\n" \
              f"{value['feed']}\n\n" \
              f"Спасибо за отзыв! Он уже улетел нашему руководству 😎\n\n" \
              f"{edit.reformat.style(preset='iu', string='Тестовый режим')}"
        return txt

    def send_choice(self, value):
        txt = f"{self.call_quest[2]}\n\n" \
              f"{edit.smile.info} Информация:\n" \
              f"{edit.reformat.style(preset='b', string='Клиент:')} {value['name']}\n\n" \
              f"{edit.reformat.style(preset='b', string='Номер телефона:')} {value['number']}\n\n" \
              f"{edit.reformat.style(preset='b', string='Вопрос:')}\n{value['choice']}\n\n" \
              f"Спасибо за вопрос! Скоро Вам ответим 😎\n\n" \
              f"{edit.reformat.style(preset='iu', string='Тестовый режим')}"
        return txt

    def profile(self, value=None):
        txt = f"TG ID: {value.from_user.id}\n" \
              f"Имя: {value.from_user.first_name}\n" \
              f"Телефон: 8 000 000 00 00\n\n" \
              f"Бонусы: 500 р\n" \
              f"Карта лояльности: {edit.smile.cmb}\n\n" \
              f"{edit.reformat.style(preset='iu', string='Тестовый режим')}"
        return txt


txt = Library()
