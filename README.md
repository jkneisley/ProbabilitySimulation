# ProbabilitySimulation

A small dice roll simulator.

## Features

- Define the number of dice (`--dice`).
- Define the die size (`--size`) and optional custom faces (`--faces`).
- Specify the number of rolls (`--rolls`).
- Roll and record outcomes.
- Add additional rolls or reset outcomes in the interactive prompt.

## Usage

```bash
python dice_simulator.py --dice 2 --size 6 --rolls 5
```

Optional custom faces:

```bash
python dice_simulator.py --dice 1 --size 6 --faces 1,1,1,6 --rolls 3
```
