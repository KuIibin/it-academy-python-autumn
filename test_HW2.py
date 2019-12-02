#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


def total_prices(rubles, cents, c_purchases):
    if rubles > 0 and cents > 0 and c_purchases > 0:
        r_cents = cents / 100
        price = rubles + r_cents
        total_price = price * c_purchases
        return total_price
    else:
        pass
        # print('Данные неверны.')


def element_less_5(lst):
    # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    result_lst = []
    for element in range(len(lst)):
        if 0 < lst[element] <= 5:
            result_lst.append(lst[element])
    return result_lst


def divided_by_17(number):
    divided_number = number % 17
    if divided_number == 0:
        print('Поздравляю! Это число делится на 17')
    else:
        print('Очень жаль. Я надеюсь, в следующий раз тебе повезет')
    return divided_number


class TestTotalPrices(unittest.TestCase):

    def test_normal(self):
        result = total_prices(3, 20, 3)
        self.assertEqual(result, 9.600000000000001)

    def test_negative(self):
        result = total_prices(-3, 20, 3)
        self.assertEqual(result, None)


class TestElemLess5(unittest.TestCase):

    def test_normal(self):
        result = element_less_5([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        self.assertEqual(result, [1, 1, 2, 3, 5])

    def test_negative(self):
        result = element_less_5([1, 1, -2, 3, -5, 8, 13, 21, 34, 55, 89])
        self.assertEqual(result, [1, 1, 3])


class TestDividedBy17(unittest.TestCase):

    def test_normal(self):
        result = divided_by_17(17)
        self.assertEqual(result, 0)

    def test_negative(self):
        result = divided_by_17(-17)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
