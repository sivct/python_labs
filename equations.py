from abc import ABC, abstractmethod
import math



class Equation(ABC):
    @abstractmethod
    def solve(self) -> None:
        pass

    @abstractmethod
    def print(self) -> None:
        pass




class LinearEquation(Equation):
    def __init__(self, a: float = 1.0, b: float = 0.0) -> None:
        self._a = float(a)
        self._b = float(b)

    @property
    def a(self) -> float:
        return self._a
    @property
    def b(self) -> float:
        return self._b



    def solve(self) -> None:
        print(" Корень: ", end="")
        if self._a != 0:
            print((-self._b) / self._a)
        elif self._b == 0:
            print("бесконечно много решений.")
        else:
            print("решений нет.")


    def print(self) -> None:
        coeff = []
        if self._a != 0:
            coeff.append(f"{self._a}x")
        if self._b != 0:
            sign = '+' if self._b > 0 else '-'
            coeff.append(f"{sign} {abs(self._b)}")
        
        print(*coeff)






class QuadraticEquation(Equation):
    def __init__(self, a: float = 1.0, b: float = 0.0, c: float = 0.0) -> None:
        if a == 0:
            raise ValueError("Это не квадратное уравнение(коэффициент a не может быть 0)")
        self._a = float(a)
        self._b = float(b)
        self._c = float(c)

    @property
    def a(self) -> float:
        return self._a
    @property
    def b(self) -> float:
        return self._b
    @property
    def c(self) -> float:
        return self._c

    def disc(self) -> float:
        return self._b * self._b - 4 * self._a * self._c

    def solve(self) -> None:
        d = self.disc()
        print(" Корни: ", end="")
        if d > 0:
            x1 = (-self._b + math.sqrt(d)) / (2 * self._a)
            x2 = (-self._b - math.sqrt(d)) / (2 * self._a)
            print(f"x1 = {x1}; x2 = {x2}")
        elif d == 0:
            x = -self._b / (2 * self._a)
            print(f"x = {x}")
        else:
            print("нет вещественных решений.")

    def print(self) -> None:
        coeff = []
        if self._a != 0:
            coeff.append(f"{self._a}x^2")
        if self._b != 0:
            sign = '+' if self._b > 0 else '-'
            coeff.append(f"{sign} {abs(self._b)}x")
        if self._c != 0:
            sign = '+' if self._c > 0 else '-'
            coeff.append(f"{sign} {abs(self._c)}")

        print(*coeff)







