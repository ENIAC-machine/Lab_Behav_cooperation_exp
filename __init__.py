from otree.api import *
import uuid

doc = """ 

"""
#Remember add desc to doc

class C(BaseConstants):
    NAME_IN_URL = 'Experiment_1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Group(BaseGroup):
    # Для отображения в конце для игроков и выгрузки
    total_players = models.IntegerField()
    number_of_players_in = models.IntegerField()
    number_of_players_out = models.IntegerField()
    # Для выгрузки
    expectations_on_others = models.LongStringField()
    name_questionnaire = models.StringField()
    first_questionnaire = models.LongStringField()
    second_questionnaire = models.LongStringField()
    city_questionnaire = models.PositiveIntegerField()
    years_in_questionnaire = models.PositiveIntegerField()
    univ_questionnaire = models.CharField()
    risk_at_questionnaire = models.PositiveIntegerField()
    trust_questionnaire = models.PositiveIntegerField()
    satis_questionnaire = models.PositiveIntegerField()
    freedom_questionnaire = models.PositiveIntegerField()
    quiz_about_decision_1 = models.StringField()
    quiz_about_decision_2 = models.StringField()
    quiz_about_decision_3 = models.StringField()
    quiz_about_decision_4 = models.StringField()
    quiz_about_decision_5 = models.StringField()
    quiz_about_decision_6 = models.StringField()
    quiz_about_decision_7 = models.StringField()
    quiz_about_decision_8 = models.StringField()
    quiz_about_decision_9 = models.StringField()
    quiz_about_decision_10 = models.StringField()
    quiz_about_decision_11 = models.StringField()


class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    expectations_on_others = models.LongStringField(
        label='Ваши ожидания касательно действий других'
    )
    decision = models.IntegerField(
        label='Ваше решение',
        choices= [
            [1, 'In'],[0, 'Out']
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    quiz_on_instruction_understanding = models.StringField(
        label='Какой вариант вы выберите, если захотите кооперироваться с остальными участниками?',
        choices= ['In', 'Out'],
        widget=widgets.RadioSelectHorizontal
    )
    name_questionnaire = models.StringField(
        verbose_name= '''Ваше имя и фамилия'''
    )

    first_questionnaire = models.LongStringField(
        verbose_name= '''Опишите вкратце Вашу стратегию в первой части игры'''
    )

    second_questionnaire = models.LongStringField(
        verbose_name= '''Как изменилась Ваша стратегия во второй части игры, и почему'''
    )
    city_questionnaire = models.PositiveIntegerField(
        verbose_name='''
        Сколько человек (приблизительно) проживало в том населенном пункте, где Вы жили в возрасте 16 лет.''',
        min = 1, max=30000000,
        initial = None)

    years_in_questionnaire = models.PositiveIntegerField(
        verbose_name='''
        Укажите, сколько лет Вы живете в Москве? Впишите число, округленное до ближайшего целого числа 
        лет.''',
        min = 0, max=95,
        initial = None)
    univ_questionnaire = models.CharField(
        verbose_name= '''Укажите Ваш средний балл за время учебы.'''
    )
    risk_at_questionnaire = models.PositiveIntegerField(
        verbose_name='''Вы любите риск или боитесь риска?''',
        choices = [
            [1, 'Очень люблю рисковать'],
            [2, 'Скорее люблю рисковать'],
            [3, 'Нейтрален к риску'],
            [4, 'Скорее боюсь рисковать'],
            [5, 'Очень боюсь рисковать'],
        ],
        widget = widgets.RadioSelect()
    )
    trust_questionnaire = models.PositiveIntegerField(
        verbose_name ='''Как Вы считаете, в целом большинству людей можно доверять, или же при общении с другими людьми 
            осторожность никогда не повредит? Пожалуйста, отметьте позицию на шкале, где 1 означает "Нужно быть очень осторожным с другими людьми" и 10
            означает "Большинству людей можно вполне доверять" ''',
        choices=[1,2,3,4,5,6,7,8,9,10],
        widget=widgets.RadioSelectHorizontal()
    )

    satis_questionnaire = models.PositiveIntegerField(
        verbose_name='''Учитывая все обстоятельства, насколько Вы удовлетворены вашей жизнью в целом в эти дни? (от 1 «полностью не удовлетворен» до 10 «полностью удовлетворен»)''',
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget = widgets.RadioSelectHorizontal()
    )

    freedom_questionnaire = models.PositiveIntegerField(
        verbose_name='''Некоторые люди чувствуют, что они обладают полной свободой выбора и контролируют свою жизнь, в
        то время как другие люди чувствуют, что то, что они делают, не имеет реального влияния на происходящее с ними. До какой степени эти
        характеристики применимы к Вам и Вашей жизни? Пожалуйста, отметьте позицию на шкале, где 1 означает "у меня нет свободы выбора" и 10
        означает "у меня полная свобода выбора".
        ''',
        choices=[1,2,3,4,5,6,7,8,9,10],
        widget=widgets.RadioSelectHorizontal()
    )
    quiz_about_decision_1 = models.StringField(
        label='0 человек',
        choices=[
            ['In' , 'In'], ['Out', 'Out']
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    quiz_about_decision_2 = models.StringField(
        label='5 человек',
        choices=[
            ['In' , 'In'], ['Out', 'Out']
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    quiz_about_decision_3 = models.StringField(
        label='10 человек',
        choices=[
            ['In' , 'In'], ['Out', 'Out']
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    quiz_about_decision_4 = models.StringField(
        label='15 человек',
        choices=[
            ['In' , 'In'], ['Out', 'Out']
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    quiz_about_decision_5 = models.StringField(
        label='20 человек',
        choices=[
            ['In' , 'In'], ['Out', 'Out']
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    quiz_about_decision_6 = models.StringField(
        label='25 человек',
        choices=[
            ['In' , 'In'], ['Out', 'Out']
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    quiz_about_decision_7 = models.StringField(
        label='30 человек',
        choices=[
            ['In' , 'In'], ['Out', 'Out']
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    quiz_about_decision_8 = models.StringField(
        label='35 человек',
        choices=[
            ['In' , 'In'], ['Out', 'Out']
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    quiz_about_decision_9 = models.StringField(
        label='40 человек',
        choices=[
            ['In' , 'In'], ['Out', 'Out']
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    quiz_about_decision_10 = models.StringField(
        label='45 человек',
        choices=[
            ['In' , 'In'], ['Out', 'Out']
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    quiz_about_decision_11 = models.StringField(
        label='49 человек',
        choices=[
            ['In' , 'In'], ['Out', 'Out']
        ],
        widget=widgets.RadioSelectHorizontal,
    )


def aggregating_data(group: Group):
    #Переменные, которые выводятся для игроков в конце и для выгрузки
    players = group.get_players()
    decisions = [player.decision for player in players]
    group.total_players = len(players)
    group.number_of_players_in = sum(decisions)
    group.number_of_players_out = group.total_players - group.number_of_players_in
    #Переменные для выгрузки
    print(players)

#PAGES
class Introduction(Page):
    pass

class Instructions(Page):
    pass

class Quiz(Page):
    form_model = 'player'
    form_fields = ['quiz_on_instruction_understanding']

class Expectations_about_the_decisions_of_others(Page):
    form_model = 'player'
    form_fields = ['expectations_on_others']

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

class Decision_Strategy_Method(Page):
    form_model = 'player'
    form_fields = ['quiz_about_decision_1', 'quiz_about_decision_2', 'quiz_about_decision_3',
                   'quiz_about_decision_4', 'quiz_about_decision_5', 'quiz_about_decision_6',
                   'quiz_about_decision_7', 'quiz_about_decision_8', 'quiz_about_decision_9',
                   'quiz_about_decision_10', 'quiz_about_decision_11']

class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['name_questionnaire', 'first_questionnaire', 'second_questionnaire',
                   'city_questionnaire', 'years_in_questionnaire', 'univ_questionnaire',
                   'risk_at_questionnaire', 'trust_questionnaire', 'satis_questionnaire',
                   'freedom_questionnaire']

class Thank_you(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        list_of_decsions = [player.decision for player in group.get_players()]
        number_of_people_in = sum(list_of_decsions)
        number_of_people_out = len(list_of_decsions) - number_of_people_in
        return dict(number_of_people_in=number_of_people_in, number_of_people_out=number_of_people_out)


page_sequence = [Introduction, Instructions, Decision, ResultsWaitPage, Results]

# page_sequence = [Introduction, Instructions, Quiz, Expectations_about_the_decisions_of_others, Decision,
#                   Decision_Strategy_Method, Questionnaire, Thank_you, ResultsWaitPage, Results]
