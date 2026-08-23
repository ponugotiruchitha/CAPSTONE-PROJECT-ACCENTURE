import asyncio
from config.actions import redact_jwt


print("=" * 60)
print("PROJECT 4 — JWT OUTPUT GUARDRAIL TEST")
print("=" * 60)

jwt = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJzdWIiOiIxMjM0NTY3ODkwIiwicm9sZSI6ImFkbWluIn0."
    "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
)

message = f"Model response contains credential: {jwt}"

print("\nORIGINAL MODEL RESPONSE:")
print(message)

result = asyncio.run(
    redact_jwt(
        {
            "bot_message": message
        }
    )
)

print("\nFINAL MODEL RESPONSE:")
print(result)