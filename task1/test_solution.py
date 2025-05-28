import unittest
from solution import strict

class TestStrictDecorator(unittest.TestCase):
    #проверка на корректность позиционных аргументов
    def test_correct_types_positional(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b
        self.assertEqual(sum_two(1, 2), 3)

    def test_incorrect_types_positional(self):
         #проверка на некорректность позиционных аргументов
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)

    def test_correct_types_keyword(self):
        #проверка на корректность ключевых аргументов
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b
        self.assertEqual(sum_two(a=1, b=2), 3)

    def test_incorrect_types_keyword(self):
        #проверка на некорректность ключевых аргументов
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b
        with self.assertRaises(TypeError):
            sum_two(a=1, b=2.4)

    def test_mixed_arguments_correct(self):
        #проверка на корректность смешанных аргументов
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b
        self.assertEqual(sum_two(1, b=2), 3)

    def test_mixed_arguments_incorrect(self):
        #проверка на некорректность смешанных аргументов
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b
        with self.assertRaises(TypeError):
            sum_two(1, b=2.4)

    def test_unannotated_parameter(self):
        # Проверка, что аннотация параметра не обязательна
        @strict
        def example(a: int, b) -> int:  
            return a
        # Проверка, что b не проверяется
        self.assertEqual(example(1, "two"), 1)
        self.assertEqual(example(1, 2), 1)

if __name__ == "__main__":
    unittest.main()