duration = int(input("duration = "))

years = duration // (3600 * 24 * 360)  # предполагаю в году 12 месяцев х 30 дней = 360 дней
months = (duration - years * 3600 * 24 * 360) // (3600 * 24 * 30)
days = (duration - years * 3600 * 24 * 360 - months * 3600 * 24 * 30) // (3600 * 24)
hours = (duration - years * 3600 * 24 * 360 - months * 3600 * 24 * 30 - days * 3600 * 24) // 3600
minutes = (duration - years * 3600 * 24 * 360 - months * 3600 * 24 * 30 - days * 3600 * 24 - hours * 3600) // 60
seconds = (duration - years * 3600 * 24 * 360 - months * 3600 * 24 * 30 - days * 3600 * 24 - hours * 3600) % 60
if years != 0 or duration >= 3600 * 24 * 360:
    print(years, " лет ", months, " мес ", days, " дн ", hours, " час ", minutes, " мин ", seconds, " сек")
elif months != 0 or duration >= 3600 * 24 * 30:
    print(months, " мес ", days, " дн ", hours, " час ", minutes, " мин ", seconds, " сек")
elif days != 0 or duration >= 3600 * 24:
    print(days, " дн ", hours, " час ", minutes, " мин ", seconds, " сек")
elif hours != 0 or duration >= 3600:
    print(hours, " час ", minutes, " мин ", seconds, " сек")
elif minutes != 0 or duration >= 60:
    print(minutes, " мин ", seconds, " сек")
else:
    print(seconds, " сек")

"""альтернативный вариант; не понравился тем, что сложен
if duration < 60:
    print(duration, " сек")
elif duration < 3600:
    print(duration // 60, " мин ", duration % 60, " сек")
elif duration <= 3600 * 24:
    print(duration // 3600, " час ", (duration % 3600) // 60, " мин", (duration - (duration // 3600) * 3600 - (duration % 3600) // 60 * 60), " сек")
"""
