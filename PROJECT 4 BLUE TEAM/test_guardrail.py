from nemoguardrails import RailsConfig, LLMRails


config = RailsConfig.from_path("./config")
rails = LLMRails(config)

print("=" * 60)
print("PROJECT 4 — INPUT GUARDRAIL TEST")
print("=" * 60)

while True:
    user_input = input("\nEnter payload (or type EXIT): ")

    if user_input.upper() == "EXIT":
        break

    response = rails.generate(
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("\nMODEL RESPONSE:")
    print(response)