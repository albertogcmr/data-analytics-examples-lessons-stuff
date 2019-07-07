import unittest
from inspect import signature

from lab_vikings.vikings_clases import Soldier


class TestSoldier(unittest.TestCase):

    def setUp(self):
        self.strength = 150
        self.health = 300
        self.soldier = Soldier(self.health, self.strength)

    def test_init_has_two_params(self):
        self.assertEqual(len(signature(Soldier).parameters), 2,
                         "A Soldier's initializer (__init__ method) must accept two parameters!")

    def test_health_attr_exists(self):
        self.assertTrue(hasattr(self.soldier, 'health'), "Soldier class doesn't have a 'health' attribute!")

    def test_health_works_ok(self):
        self.assertEqual(self.soldier.health, self.health, "Something is up with the Soldier's 'health' attribute")

    def test_strenght_attr_exists(self):
        self.assertTrue(hasattr(self.soldier, 'strength'), "Soldier class doesn't have a 'strength' attribute")

    def test_strenght_works_ok(self):
        self.assertEqual(self.soldier.health, self.health, "Something is up with the Soldier's 'strength' attribute")

    def test_soldier_has_attack_method(self):
        self.assertTrue(hasattr(self.soldier, 'attack'), "Soldier class must have an 'attack' method!")

    def test_soldier_attack_is_method(self):
        self.assertTrue(callable(self.soldier.attack), "Soldier class 'attack' attribute must be a method!")

    def test_soldier_attack_method_no_args(self):
        self.assertEqual(len(signature(self.soldier.attack).parameters), 0,
                         "Soldier's method 'attack' must not accept any argument at all")

    def test_soldier_attack_returns_soldier_strenght(self):
        self.assertEqual(self.soldier.attack(), self.strength,
                         "Soldier's method 'attack' must return the soldier's strenght")

    def test_soldier_has_receive_damage_method(self):
        self.assertTrue(hasattr(self.soldier, 'receive_damage'), "Soldier must have a 'receive_damage' method")

    def test_soldier_receive_damage_is_method(self):
        self.assertTrue(callable(self.soldier.receive_damage),
                        "Soldier class 'receive_damage' attribute must be a method!")

    def test_soldier_receive_damage_accepts_one_parameter(self):
        self.assertEqual(len(signature(self.soldier.receive_damage).parameters), 1,
                         "Soldier's 'receive_damage' method must accept one argument")

    def test_receive_damage_returns_none(self):
        self.assertEqual(self.soldier.receive_damage(50), None,
                         "Soldier's 'receive_damage' method must return nothing!")

    def test_soldier_can_receive_damage(self):
        dmg = 50
        self.soldier.receive_damage(dmg)
        self.assertEqual(self.soldier.health, self.health - dmg, "Soldier 'receive_damage' doesn't work as expected")


if __name__ == '__main__':
    exit(unittest.main())
