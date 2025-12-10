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
print(f"\n✓ Using model: {selected_model}\n")

run(
    deployment_name=selected_model,
    print_request=True,
    print_only_content=False,
)