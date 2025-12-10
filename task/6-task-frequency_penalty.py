from task.app.main import run

print("Frequency penalty controls repetition:")
print("-2.0 = very repetitive (can cause loops!)")
print("0.0 = neutral (default)")
print("2.0 = avoids repetition")

while True:
    penalty_input = input("\nEnter frequency_penalty (-2.0 to 2.0): ").strip()
    try:
        frequency_penalty = float(penalty_input)
        if -2.0 <= frequency_penalty <= 2.0:
            break
        print("Please enter a value between -2.0 and 2.0")
    except ValueError:
        print("Invalid input. Please enter a number between -2.0 and 2.0")

print(f"\n Frequency penalty: {frequency_penalty}\n")

run(
    deployment_name='gpt-4o',
    frequency_penalty=frequency_penalty,
    print_request=True,
    print_only_content=True,
)