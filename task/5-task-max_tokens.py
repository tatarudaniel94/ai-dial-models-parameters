from task.app.main import run

while True:
    tokens_input = input("Enter max_tokens value (e.g. 10, 50, 100): ").strip()
    try:
        max_tokens = int(tokens_input)
        if max_tokens > 0:
            break
        print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

print(f"\n Max tokens: {max_tokens}\n")

run(
    deployment_name='gpt-4o',
    max_tokens=max_tokens,
    print_request=True,
    print_only_content=False,
)