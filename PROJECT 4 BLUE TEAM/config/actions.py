import re
from typing import Optional

from nemoguardrails.actions import action


# ============================================================
# JWT OUTPUT GUARDRAIL
# ============================================================

JWT_PATTERN = re.compile(
    r"\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b"
)


# ============================================================
# PROJECT 3 ATTACK PATTERNS
# ============================================================

ATTACK_PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"ignore\s+the\s+previous\s+instructions",
    r"disregard\s+(all\s+)?previous\s+instructions",
    r"reveal\s+(the\s+)?system\s+prompt",
    r"show\s+(me\s+)?(the\s+)?system\s+prompt",
    r"override\s+(the\s+)?system",
    r"developer\s+message",
    r"reveal\s+(the\s+)?jwt",
    r"reveal\s+(the\s+)?token",
]


# ============================================================
# INPUT GUARDRAIL
# ============================================================

@action(is_system_action=True)
async def self_check_input(context: Optional[dict] = None):
    context = context or {}

    user_message = context.get("user_message") or ""

    if not isinstance(user_message, str):
        user_message = str(user_message)

    for pattern in ATTACK_PATTERNS:
        if re.search(pattern, user_message, re.IGNORECASE):
            print(
                f"GUARDRAIL: BLOCKED | Reason: {pattern}"
            )
            return False

    print("GUARDRAIL: PASS")
    return True


# ============================================================
# JWT OUTPUT GUARDRAIL
# ============================================================

@action(is_system_action=True)
async def redact_jwt(context=None):
    context = context or {}

    bot_message = context.get("bot_message") or ""

    if not isinstance(bot_message, str):
        bot_message = str(bot_message)

    redacted_message = JWT_PATTERN.sub(
        "[REDACTED]",
        bot_message
    )

    if redacted_message != bot_message:
        print(
            "OUTPUT GUARDRAIL: JWT DETECTED | "
            "Credential replaced with [REDACTED]"
        )

    return redacted_message