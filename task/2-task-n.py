from task.app.main import run

# Models to try:
MODELS = {
    '1': 'gpt-4o',
    '2': 'claude-3-7-sonnet@20250219',
    '3': 'gemini-2.5-pro',
}

print("Select a model:")
for key, model in MODELS.items():
    print(f"  {key}. {model}")

choice = input("\nEnter your choice (1-3): ").strip()

if choice not in MODELS:
    print("Invalid choice. Defaulting to gpt-4o")
    choice = '1'

selected_model = MODELS[choice]

# Get n value from user
while True:
    n_input = input("\nEnter number of choices to generate (1-5): ").strip()
    try:
        n_value = int(n_input)
        if 1 <= n_value <= 5:
            break
        print("Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")

print(f"\n Using model: {selected_model}")
print(f" Generating {n_value} choice(s)\n")

run(
    deployment_name=selected_model,
    n=n_value,
    print_request=True,
    print_only_content=False,
)
