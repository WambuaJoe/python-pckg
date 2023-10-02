import unittest

from funct import calculate


class TestPricing(unittest.TestCase):
    def test_calculate(self):
        items = (
            {'case': 'No tax, no discount', 'price': 10, 'tax': 0,
                                    'discount': 0, 'net_price': 10},
            {'case': 'Has tax, no discount', 'price': 10, 'tax': 0.1,
                                    'discount': 0, 'net_price': 10},
            {'case': 'No tax, has discount', 'price': 10, 'tax': 0,
                                    'discount': 1, 'net_price': 10},
            {'case': 'Has tax, has discount', 'price': 10, 'tax': 0.1,
                                    'discount': 1, 'net_price': 9.9},
        )

        for item in items:
            with self.subTest(item['case']):
                net_price = calculate(
                    item['price'],
                    item['tax'],
                    item['discount']
                )
                self.assertEqual(
                    net_price,
                    item['net_price']
                )


if __name__ == '__main__':
    unittest.main(verbosity=1)
