from datetime import datetime


def alert(event_type, identity, details):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n" + "=" * 65)
    print("[ALERT] ANOMALOUS ACTIVITY DETECTED")
    print(f"timestamp={timestamp}")
    print(f"identity={identity}")
    print(f"event_type={event_type}")
    print(f"details={details}")
    print("=" * 65)


def detect_volume_spike(request_count, window_seconds, identity):
    if request_count > 20 and window_seconds <= 60:
        alert(
            "VOLUME_SPIKE",
            identity,
            f"{request_count} LLM API requests detected in {window_seconds} seconds"
        )
        return True

    return False


def detect_scope_change(previous_scope, current_scope, identity):
    if previous_scope != current_scope:
        alert(
            "SCOPE_CHANGE",
            identity,
            f"Scope changed from {previous_scope} to {current_scope}"
        )
        return True

    return False


def detect_expired_token_reuse(token_status, identity):
    if token_status == "expired":
        alert(
            "EXPIRED_TOKEN_REUSE",
            identity,
            "Expired access token was reused"
        )
        return True

    return False


print("=" * 65)
print("PROJECT 4 — ANOMALY DETECTION TEST")
print("=" * 65)

identity = "agent-project4"

print("\nScenario 1: Volume Spike")
detect_volume_spike(
    request_count=25,
    window_seconds=60,
    identity=identity
)

print("\nScenario 2: Scope Change")
detect_scope_change(
    previous_scope="read:ai-data",
    current_scope="write:admin",
    identity=identity
)

print("\nScenario 3: Expired Token Reuse")
detect_expired_token_reuse(
    token_status="expired",
    identity=identity
)

print("\nAnomaly detection test completed.")