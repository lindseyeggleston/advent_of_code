def calculate_fuel_required(weight: int) -> int:
    return max(int(weight // 3) - 2, 0)


def calculate_total_fuel_required_for_modules(weight_file: str) -> int:
    total_fuel = 0
    with open(weight_file, "r") as f:
        for line in f:
            weight = int(line.strip())
            total_fuel += calculate_fuel_required(weight)
    return total_fuel


def calculate_total_fuel_required(weight_file: str) -> int:
    total_fuel = 0
    with open(weight_file, "r") as f:
        for line in f:
            weight = int(line.strip())
            fuel = calculate_fuel_required(weight)
            while fuel > 0:
                total_fuel += fuel
                fuel = calculate_fuel_required(fuel)
    return total_fuel


if __name__ == "__main__":
    print(calculate_total_fuel_required("input.txt"))
