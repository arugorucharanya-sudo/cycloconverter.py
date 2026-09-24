Cycloconverter Calculator
Power Electronics - Electrical Engineering
Single-Phase Cycloconverter
Calculates output frequency and frequency ratio.

import math

def calculate_cycloconverter(input_frequency, output_frequency):
"""
Calculate cycloconverter frequency parameters.

input_frequency  : Input AC frequency in Hz
output_frequency : Desired output AC frequency in Hz

Returns:
    Frequency ratio
    Output period
    Input cycles required for one output cycle
"""

frequency_ratio = output_frequency / input_frequency
output_period = 1 / output_frequency
input_cycles = input_frequency / output_frequency

return frequency_ratio, output_period, input_cycles


print("=" * 60)
print(" CYCLOCONVERTER CALCULATOR")
print(" POWER ELECTRONICS")
print("=" * 60)

try:
input_frequency = float(
input("Enter input AC frequency (Hz): ")
)

output_frequency = float(
    input("Enter desired output frequency (Hz): ")
)

input_voltage = float(
    input("Enter input voltage RMS (V): ")
)

firing_angle = float(
    input("Enter firing angle α (degrees): ")
)

# Input validation
if input_frequency <= 0:
    raise ValueError("Input frequency must be positive.")

if output_frequency <= 0:
    raise ValueError("Output frequency must be positive.")

if input_voltage <= 0:
    raise ValueError("Input voltage must be positive.")

if firing_angle < 0 or firing_angle > 180:
    raise ValueError("Firing angle must be between 0° and 180°.")

if output_frequency >= input_frequency:
    raise ValueError(
        "For a conventional cycloconverter, "
        "output frequency should be lower than input frequency."
    )

# Calculate frequency parameters
frequency_ratio, output_period, input_cycles = (
    calculate_cycloconverter(
        input_frequency,
        output_frequency
    )
)

# Convert firing angle to radians
alpha_rad = math.radians(firing_angle)

# Approximate maximum output voltage
# Vout(max) ≈ (2 * Vm / π) cos(α)
Vm = math.sqrt(2) * input_voltage
maximum_output_voltage = (
    (2 * Vm / math.pi) * math.cos(alpha_rad)
)

print("\n" + "=" * 60)
print("                       RESULTS")
print("=" * 60)

print(f"Input Frequency          : {input_frequency:.2f} Hz")
print(f"Output Frequency         : {output_frequency:.2f} Hz")
print(f"Frequency Ratio (fo/fi)  : {frequency_ratio:.4f}")
print(f"Output Period            : {output_period:.4f} s")
print(f"Input Cycles/Output Cycle: {input_cycles:.2f}")
print(f"Firing Angle             : {firing_angle:.2f}°")
print(f"Approx. Maximum Output V : {maximum_output_voltage:.2f} V")

print("=" * 60)


except ValueError as error:
print(f"\nError: {error}")
