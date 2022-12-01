(deffunction ask-value (?question)
(print ?question)
(bind ?answer (read))
?answer
)

(deffunction ask-question (?question $?allowed-values)
(print ?question)
(bind ?answer (read))
(if (lexemep ?answer)
then (bind ?answer (lowcase ?answer))
)
(while (not (member$ ?answer ?allowed-values)) do
(print ?question)
(bind ?answer (read))
(if (lexemep ?answer)
then (bind ?answer (lowcase ?answer))
)
)
?answer
)

(deffunction yes-or-no (?question)
(bind ?response (ask-question ?question yes no y n))
(if (or (eq ?response yes) (eq ?response y))
then yes
else no
)
)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



(defrule csharp ""
(time ?t)
(or
(indie yes)
(3d yes)
)
(not (solution ?))
=>
(if (< ?t 3) 
then(assert (solution C#))
)
)

(defrule cplus ""
(time ?t)
(and
(aaa yes)
(graphics yes)
)
(not (solution ?))
=>
(if (> ?t 3) 
then(assert (solution C++))
)
)

(defrule java ""
(or
(2d yes)
(reliability yes)
(tasks yes)
)
(not (solution ?))
=>
(assert (solution Java))
)

(defrule js ""
(and
(creativity yes)
(taste yes)
)
(not (solution ?))
=>
(assert (solution JavaScript))
)

(defrule kotlin ""
(and
(compactness yes)
(new yes)
)
(not (solution ?))
=>
(assert (solution Kotlin))
)

(defrule swift ""
(and
(security yes)
(simplicity yes)
)
(not (solution ?))
=>
(assert (solution Swift))
)

(defrule r ""
(and
(science yes)
(experience yes)
)
(not (solution ?))
=>
(assert (solution R))
)

(defrule python ""
(and
(practice yes)
(versatility yes)
)
(not (solution ?))
=>
(assert (solution Python))
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



(defrule ask-browser "Браузер"
(not (solution ?))
(not (browser ?))
=>
(assert (browser (yes-or-no "Вы предпочитаете браузер сторонним приложениям?")))
)

(defrule ask-design "Дизайн"
(browser yes)
(not (solution ?))
(not (design ?))
=>
(assert (design (yes-or-no "Вам больше интересен дизайн?")))
)

(defrule ask-beauty "Внешняя красота"
(not (solution ?))
(not (beauty ?))
=>
(assert (beauty (yes-or-no "Вы считаете что внешняя красота важнее внутренней?")))
)

(defrule ask-taste "Вкус"
(and
(design yes)
(beauty yes)
)
(not (solution ?))
(not (taste ?))
=>
(assert (taste (yes-or-no "Вы обладаете художественным вкусом?")))
)

(defrule ask-creativity "Креативность"
(not (solution ?))
(not (creativity ?))
=>
(assert (creativity (yes-or-no "Вы - креативная личность?")))
)

(defrule ask-mechanism "Механизм"
(browser yes)
(not (solution ?))
(not (mechanism ?))
=>
(assert (mechanism (yes-or-no "Вам больше интересно как все работает?")))
)

(defrule ask-mechanism "Задачи"
(mechanism yes)
(not (solution ?))
(not (tasks ?))
=>
(assert (tasks (yes-or-no "Вы любите решать сложные задачи?")))
)

(defrule ask-phone "Смартфон"
(not (solution ?))
(not (phone ?))
=>
(assert (phone (yes-or-no "Вы часто пользуетесь смартфоном?")))
)

(defrule ask-android "Андроид"
(phone yes)
(not (solution ?))
(not (android ?))
=>
(assert (android (yes-or-no "У вас Андроид?")))
)

(defrule ask-experience "Опыт"
(not (solution ?))
(not (experience ?))
=>
(assert (experience (yes-or-no "У вас есть опыт в программировании?")))
)

(defrule ask-reliability "Надежность"
(and
(android yes)
(experience yes)
)
(not (solution ?))
(not (reliability ?))
=>
(assert (reliability (yes-or-no "Вы предпочитаете все надежное и проверенное?")))
)

(defrule ask-new "Современное"
(android yes)
(not (solution ?))
(not (new ?))
=>
(assert (new (yes-or-no "Вы выбираете все самое новое и современное?")))
)

(defrule ask-compactness "Компактность"
(not (solution ?))
(not (compactness ?))
=>
(assert (compactness (yes-or-no "Вам нравится компактность и читаемость кода?")))
)

(defrule ask-iphone "Айфон"
(phone yes)
(not (solution ?))
(not (iphone ?))
=>
(assert (iphone (yes-or-no "У вас Айфон?")))
)

(defrule ask-apple "Apple"
(not (solution ?))
(not (apple ?))
=>
(assert (apple (yes-or-no "Вы любите технику Apple?")))
)

(defrule ask-simplicity "Простота"
(and
(iphone yes)
(apple yes)
)
(not (solution ?))
(not (simplicity ?))
=>
(assert (simplicity (yes-or-no "Вам нравится простота и понятность?")))
)

(defrule ask-security "Безопасность"
(not (solution ?))
(not (security ?))
=>
(assert (security (yes-or-no "Безопасность для вас в приоритете?")))
)

(defrule ask-games "Игры"
(not (solution ?))
(not (games ?))
=>
(assert (games (yes-or-no "Вы любите игры?")))
)

(defrule ask-imagination "Воображение"
(not (solution ?))
(not (imagination ?))
=>
(assert (imagination (yes-or-no "У вас развито воображение?")))
)

(defrule ask-pc "ПК"
(and
(imagination yes)
(games yes)
)
(not (solution ?))
(not (pc ?))
=>
(assert (pc (yes-or-no "Вы играете на ПК или консоли?")))
)

(defrule ask-phonegames "Мобильные игры"
(games yes)
(not (solution ?))
(not (phonegames ?))
=>
(assert (phonegames (yes-or-no "Вы играете на телефоне?")))
)

(defrule ask-3d "3D игры"
(phonegames yes)
(not (solution ?))
(not (3d ?))
=>
(assert (3d (yes-or-no "Вы предпочитаете 3D игры?")))
)

(defrule ask-2d "2D игры"
(and
(phonegames yes)
)
(not (solution ?))
(not (2d ?))
=>
(assert (2d (yes-or-no "Вы предпочитаете 2D игры?")))
)

(defrule ask-easy "Легкие пути"
(and
(pc yes)
(games yes)
)
(not (solution ?))
(not (easy ?))
=>
(assert (easy (yes-or-no "Вы предпочитаете выбирать легкие пути?")))
)

(defrule ask-graphics "Графика"
(and
(pc yes)
)
(not (solution ?))
(not (graphics ?))
=>
(assert (graphics (yes-or-no "Для вас важна графика?")))
)

(defrule ask-time "Свободное время"
(pc yes)
(not (solution ?))
(not (games ?))
=>
(assert (time (ask-value "Сколько в среднем часов в день у вас есть для изучения языка?")))
)

(defrule ask-indie "Инди игры"
(not (solution ?))
(not (indie ?))
=>
(assert (indie (yes-or-no "Вам интересны инди игры?")))
)

(defrule ask-aaa "ААА игры"
(not (solution ?))
(not (aaa ?))
=>
(assert (aaa (yes-or-no "Вы играете только в ААА игры?")))
)

(defrule ask-math "Математика"
(not (solution ?))
(not (math ?))
=>
(assert (math (yes-or-no "Ваш любимый предмет - математика?")))
)

(defrule ask-ai "ИИ"
(not (solution ?))
(not (ai ?))
=>
(assert (ai (yes-or-no "Вас интересуют ИИ и нейронные сети?")))
)

(defrule ask-statistics "Статистика"
(and
(math yes)
(ai yes)
)
(not (solution ?))
(not (statistics ?))
=>
(assert (statistics (yes-or-no "Вам интересна статистика?")))
)

(defrule ask-science "Наука"
(statistics yes)
(not (solution ?))
(not (science ?))
=>
(assert (science (yes-or-no "Вас интересует теоритическая наука?")))
)

(defrule ask-practice "Практика"
(statistics yes)
(not (solution ?))
(not (practice ?))
=>
(assert (practice (yes-or-no "Вас интересует практика?")))
)

(defrule ask-versatility "Универсальность"
(not (solution ?))
(not (versatility ?))
=>
(assert (versatility (yes-or-no "Вы предпочитаете универсальность и большое количество функций?")))
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(defrule system-banner ""
=>
(println crlf "Экспертная система - рекомендация по выбору языка программирования" crlf))

(defrule print-solution ""
(solution ?item)
=>
(println crlf "Рекомендуемый язык для изучения:" crlf)
(println " " ?item crlf))