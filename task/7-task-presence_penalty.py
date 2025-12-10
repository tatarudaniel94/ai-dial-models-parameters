from task.app.main import run

# The `presence_penalty` parameter encourages talking about new topics.
# Range: -2.0 to 2.0, Default: 0.0
# Note: For Anthropic and Gemini this parameter will be ignored!

print("Presence penalty controls topic diversity:")
print("-2.0 = stays focused on same concepts")
print("0.0 = neutral (default)")
print("2.0 = explores new/related topics")

while True:
    penalty_input = input("\nEnter presence_penalty (-2.0 to 2.0): ").strip()
    try:
        presence_penalty = float(penalty_input)
        if -2.0 <= presence_penalty <= 2.0:
            break
        print("Please enter a value between -2.0 and 2.0")
    except ValueError:
        print("Invalid input. Please enter a number between -2.0 and 2.0")

print(f"\n Presence penalty: {presence_penalty}\n")

run(
    deployment_name='gpt-4o',
    presence_penalty=presence_penalty,
    print_request=True,
    print_only_content=True,
)