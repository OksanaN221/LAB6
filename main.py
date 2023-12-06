class Empl:
    className = 'Employee'

    def __init__(self, work_hours, bid, k_bonus):
        self._work_hours = work_hours
        self._bid = bid
        self._k_bonus = k_bonus

    def size_k_bonus(self):
        return self._work_hours * self._bid * self._k_bonus


class Big_empl(Empl):
    className = 'Старший сотрудник'

    def __init__(self, work_hours, bid, k_bonus, salary):
        super().__init__(work_hours, bid, k_bonus)
        self.salary = salary

    def ratio_salary_to_work_hours(self):
        return self.salary / self._work_hours


class Director(Empl):
    className = 'Директор'

    def __init__(self, work_hours, bid, k_bonus, salary):
        super().__init__(work_hours, bid, k_bonus)
        self.salary = salary

    def ratio_salary_to_work_hours(self):
        return self.salary / self._work_hours


print('Введите количество рабочих часов старшего сотрудника:')
work_hours1 = int(input())
print('Введите ставку старшего сотрудника:')
bid1 = int(input())
print('Введите коэффициент премии старшего сотрудника:')
k_bonus1 = float(input())
print('Введите зарплату старшего сотрудника:')
salary1 = int(input())

big_empl =(Big_empl(work_hours1, bid1, k_bonus1, salary1))
print(f'Сотрудник: {Big_empl.className}')
print(f'Размер премии: {big_empl.size_k_bonus()} рублей')
print(f'Соотношение зарплаты к рабочим часам: {big_empl.ratio_salary_to_work_hours()}')

print('\n')

print('Введите количество рабочих часов директора:')
work_hours2 = int(input())
print('Введите ставку директора:')
bid2 = int(input())
print('Введите коэффициент премии директора:')
k_bonus2 = float(input())
print('Введите зарплату директора:')
salary2 = int(input())

director = Director(work_hours2, bid2, k_bonus2, salary2)
print(f'Сотдруник: {Director.className}')
print(f'Размер премии:{director.size_k_bonus()} рублей')
print(f'Соотношение зарплаты к рабочим часам: {director.ratio_salary_to_work_hours()}')
