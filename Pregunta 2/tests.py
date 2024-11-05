import unittest
from expression import ExpressionEvaluator


class TestExpressionEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = ExpressionEvaluator()

    def test_eval_prefix(self):
        self.assertEqual(self.evaluator.eval_prefix(['+', '*', '+', '3', '4', '5', '7']), 42)
        self.assertEqual(self.evaluator.eval_prefix(['/', '12', '4']), 3)
        self.assertEqual(self.evaluator.eval_prefix(['-', '8', '3']), 5)
        self.assertEqual(self.evaluator.eval_prefix(['*', '2', '+', '5', '3']), 16)

    def test_eval_postfix(self):
        self.assertEqual(self.evaluator.eval_postfix(['8', '3', '-', '8', '4', '4', '+', '*', '+']), 69)
        self.assertEqual(self.evaluator.eval_postfix(['12', '4', '/']), 3)
        self.assertEqual(self.evaluator.eval_postfix(['3', '4', '5', '7', '+', '*', '+']), 51)
        self.assertEqual(self.evaluator.eval_postfix(['2', '5', '3', '+', '*']), 16)

    def test_infix_from_prefix(self):
        self.assertEqual(self.evaluator.infix_from_prefix(['+', '*', '+', '3', '4', '5', '7']), '(3 + 4) * 5 + 7')
        self.assertEqual(self.evaluator.infix_from_prefix(['-', '8', '3']), '8 - 3')
        self.assertEqual(self.evaluator.infix_from_prefix(['*', '2', '+', '5', '3']), '2 * (5 + 3)')

    def test_infix_from_postfix(self):
        self.assertEqual(self.evaluator.infix_from_postfix(['8', '3', '-', '8', '4', '4', '+', '*', '+']), '8 - 3 + 8 * (4 + 4)')
        self.assertEqual(self.evaluator.infix_from_postfix(['3', '4', '+', '5', '*', '7', '+']), '(3 + 4) * 5 + 7')


if __name__ == '__main__':
    unittest.main()
