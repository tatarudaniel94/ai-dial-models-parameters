from task.app.main import run

print("Stop sequences - AI stops when it encounters these:")
print("1. Double newline (\\n\\n)")
print("2. Specific topics [\"**Embedding Layer**\", \"**Transformer Blocks**\", \"**Training**\"]")
print("3. No stop sequence (full response)")

while True:
    choice = input("\nSelect stop option (1-3): ").strip()
    if choice in ['1', '2', '3']:
        break
    print("Please enter 1, 2, or 3")

if choice == '1':
    stop_value = "\n\n"
    print(f"\n Stop sequence: \\n\\n")
elif choice == '2':
    stop_value = ["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]
    print(f"\n Stop sequences: {stop_value}")
else:
    stop_value = None
    print("\n No stop sequence")

print()

run(
    deployment_name='gpt-4o',
    stop=stop_value,
    print_request=True,
    print_only_content=False,
)