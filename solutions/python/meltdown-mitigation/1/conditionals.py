"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    conditions = [
        temperature < 800 and neutrons_emitted > 500,
        temperature * neutrons_emitted < 500000,
    ]
    return all(conditions)


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current

    power_status = (generated_power / theoretical_max_power) * 100

    if power_status >= 80:
        return "green"
    elif power_status < 80 and power_status >= 60:
        return "orange"
    elif power_status < 60 and power_status >= 30:
        return "red"
    else:
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    level = temperature * neutrons_produced_per_second
    percent_crit = (level / threshold) * 100
    if 90 <= percent_crit <= 110:
        return "NORMAL"
    elif percent_crit < 90 and percent_crit <= 110:
        return "LOW"
    else:
        return "DANGER"
