import unittest

from dice_simulator import DiceRollSimulator


class DiceRollSimulatorTests(unittest.TestCase):
    def test_roll_records_expected_number_of_results(self):
        simulator = DiceRollSimulator(number_of_dice=2, die_size=6)

        new_outcomes = simulator.roll(3)

        self.assertEqual(3, len(new_outcomes))
        self.assertEqual(3, len(simulator.outcomes))
        for roll in new_outcomes:
            self.assertEqual(2, len(roll))
            for value in roll:
                self.assertTrue(1 <= value <= 6)

    def test_custom_faces_are_used(self):
        simulator = DiceRollSimulator(number_of_dice=1, die_size=6, faces=[2, 4])

        new_outcomes = simulator.roll(10)

        self.assertTrue(all(roll[0] in {2, 4} for roll in new_outcomes))

    def test_add_rolls_appends_results(self):
        simulator = DiceRollSimulator(number_of_dice=1, die_size=6)

        simulator.roll(2)
        simulator.add_rolls(3)

        self.assertEqual(5, len(simulator.outcomes))

    def test_reset_clears_outcomes(self):
        simulator = DiceRollSimulator(number_of_dice=1, die_size=6)

        simulator.roll(2)
        simulator.reset()

        self.assertEqual([], simulator.outcomes)


if __name__ == "__main__":
    unittest.main()
