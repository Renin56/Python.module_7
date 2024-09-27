team1_num = 5
team2_num = 6

score_1 = 40
score_2 = 42

team1_time = 18015.2
challenge_result = 'Победа команды Мастер кода'

tasks_total = score_1 + score_2
time_avg = 350.4

print('В команде Мастера кода участников: %d!' % team1_num)
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))

print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {} с.!'.format(team1_time))

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}!')

print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу!')
