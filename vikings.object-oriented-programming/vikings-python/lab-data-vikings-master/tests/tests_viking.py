import unittest
from inspect import signature

from lab_vikings.vikings_clases import Viking


class TestViking(unittest.TestCase):

    def setUp(self):
        self.name = 'Harald'
        self.strength = 150
        self.health = 300
        self.viking = Viking(self.name, self.health, self.strength)

    def testShouldReciveThreeParams(self):
        self.assertEqual(len(signature(Viking).parameters), 3)

    def testName(self):
        self.assertEqual(self.viking.name, self.name)

    def testHealth(self):
        self.assertEqual(self.viking.health, self.health)

    def testStrenght(self):
        self.assertEqual(self.viking.strength, self.strength)

    def testAttackShouldBeFunction(self):
        self.assertEqual(callable(self.viking.attack), True)

    def testAttackReciveNoParameters(self):
        self.assertEqual(len(signature(self.viking.attack).parameters), 0)

    def testAttackSouldReturnStrength(self):
        self.assertEqual(self.viking.attack(), self.strength)

    def testReceiveDamageIsFunction(self):
        self.assertEqual(callable(self.viking.receive_damage), True)

    def testReceiveDamageReciveOneParam(self):
        self.assertEqual(len(signature(self.viking.receive_damage).parameters), 1)

    def testReciveDamageShouldRestHealth(self):
        self.viking.receive_damage(50)
        self.assertEqual(self.viking.health, self.health - 50)

    def testReciveDamageShouldReturnString50(self):
        self.assertEqual(self.viking.receive_damage(50), f'{self.name} has received 50 points of damage')

    def testReciveDamageShouldReturnString70(self):
        self.assertEqual(self.viking.receive_damage(70), f'{self.name} has received 70 points of damage')

    def testReceiveDamageShouldReturnStringDeath(self):
        self.assertEqual(self.viking.receive_damage(self.health), f'{self.name} has died in act of combat')

    def testBattleCry(self):
        self.assertTrue(callable(self.viking.battle_cry))

    def testBattleCryReturnString(self):
        self.assertEqual(self.viking.battle_cry(), 'Odin Owns You All!')


if __name__ == '__main__':
    unittest.main()
