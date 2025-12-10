from task.app.main import run

while True:
    temp_input = input("\nEnter temperature (0.0 - 2.0): ").strip()
    try:
        temperature = float(temp_input)
        if 0.0 <= temperature <= 2.0:
            break
        print("Please enter a value between 0.0 and 2.0")
    except ValueError:
        print("Invalid input. Please enter a number between 0.0 and 2.0")

print(f"\n Temperature: {temperature}\n")

run(
    deployment_name='gpt-4o',
    temperature=temperature,
    print_request=True,
    print_only_content=True,
)