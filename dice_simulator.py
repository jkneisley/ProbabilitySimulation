import argparse
import random
from dataclasses import dataclass, field
from typing import List, Sequence


@dataclass
class DiceRollSimulator:
    number_of_dice: int
    die_size: int
    faces: Sequence[int] | None = None
    outcomes: List[List[int]] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.number_of_dice < 1:
            raise ValueError("number_of_dice must be at least 1")
        if self.die_size < 1:
            raise ValueError("die_size must be at least 1")

        if self.faces is None:
            self.faces = list(range(1, self.die_size + 1))
        elif not self.faces:
            raise ValueError("faces must not be empty")

    def roll(self, number_of_rolls: int) -> List[List[int]]:
        if number_of_rolls < 1:
            raise ValueError("number_of_rolls must be at least 1")

        new_outcomes = [
            [random.choice(self.faces) for _ in range(self.number_of_dice)]
            for _ in range(number_of_rolls)
        ]
        self.outcomes.extend(new_outcomes)
        return new_outcomes

    def add_rolls(self, number_of_rolls: int) -> List[List[int]]:
        return self.roll(number_of_rolls)

    def reset(self) -> None:
        self.outcomes.clear()


def _parse_faces(raw_faces: str | None) -> List[int] | None:
    if raw_faces is None:
        return None

    parsed_faces = [int(face.strip()) for face in raw_faces.split(",") if face.strip()]
    if not parsed_faces:
        raise ValueError("faces must contain at least one value")
    return parsed_faces


def main() -> None:
    parser = argparse.ArgumentParser(description="Dice roll simulator")
    parser.add_argument("--dice", type=int, default=1, help="Number of dice")
    parser.add_argument("--size", type=int, default=6, help="Die size")
    parser.add_argument(
        "--faces",
        type=str,
        default=None,
        help="Comma-separated face values (overrides --size values)",
    )
    parser.add_argument("--rolls", type=int, default=1, help="Number of initial rolls")
    args = parser.parse_args()

    simulator = DiceRollSimulator(
        number_of_dice=args.dice,
        die_size=args.size,
        faces=_parse_faces(args.faces),
    )

    initial_outcomes = simulator.roll(args.rolls)
    print(f"Initial outcomes: {initial_outcomes}")

    while True:
        action = input("Choose action: [a]dd rolls, [r]eset, [q]uit: ").strip().lower()
        if action == "q":
            print(f"Final recorded outcomes: {simulator.outcomes}")
            break
        if action == "r":
            simulator.reset()
            print("Outcomes reset.")
            continue
        if action == "a":
            additional_rolls = int(input("How many additional rolls? ").strip())
            added_outcomes = simulator.add_rolls(additional_rolls)
            print(f"Added outcomes: {added_outcomes}")
            print(f"All recorded outcomes: {simulator.outcomes}")
            continue
        print("Unknown action. Choose a, r, or q.")


if __name__ == "__main__":
    main()
