# Задание 5

revenue = int(input("Введите сумму выручки компании за период: "))
costs = int(input("Введите сумму затрат компании за период: "))
result = revenue - costs
if result < 0:
    print("Убыток компании за период составил", result)
elif result > 0:
    revenue_return = (result / revenue) * 100
    print("Прибыль компании за период составила:", result,)
    print("Рентабельность выручки составила: %.2f" % revenue_return, "процентов")
    employees = int(input("Введите численность сотрудников компании:"))
    avg_result = result / employees
    print("Прибыль компании в расчёте на одного сотрудника составила: %.2f" % avg_result)
else:
    print("Финансовый результат деятельности компании за период равен нулю")


