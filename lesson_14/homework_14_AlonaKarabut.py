# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод setattr.

class Rhomb():

    def __setattr__(self, side_a, angle_a):
        print(f"Rhomb side equals {side_a} cm, angle a equals {angle_a} degrees")
        super().__setattr__(side_a, angle_a)

    def calculate(self):
        if isinstance(self.side_a, int):
            if self.side_a > 0:
                if isinstance(self.angle_a, int):
                    if self.angle_a > 0:
                        angle_b = 180 - self.angle_a
                        return f"Angle b equals {angle_b} cm"
                    else:
                        return "Angle a must be > 0"
                else:
                    return "Angle a must be an integer"
            else:
                return "Side a must be > 0"
        else:
            return "Side a must be an integer"

rhomb1 = Rhomb()

rhomb1.side_a = 15
rhomb1.angle_a = 45

print(rhomb1.calculate())


