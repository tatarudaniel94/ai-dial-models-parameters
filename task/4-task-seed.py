from task.app.main import run

while True:
    seed_input = input("Enter seed value (any integer, e.g. 42): ").strip()
    try:
        seed_value = int(seed_input)
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print(f"\n Seed: {seed_value}")
print(f" Generating 5 choices to compare\n")

run(
    deployment_name='gpt-4o',
    seed=seed_value,
    n=5,
    print_request=True,
    print_only_content=False,
)