def retrieve_rag_document():
    print("\n========== RAG RETRIEVAL ==========")

    with open("rag_knowledge.txt", "r", encoding="utf-8") as file:
        document = file.read()

    print("Retrieved knowledge-base chunk:")
    print("--------------------------------")
    print(document)
    print("--------------------------------")

    return document


def simulated_mcp_tool(tool_name, arguments):
    print("\n========== MCP TOOL CALL ==========")

    print(f"Tool: {tool_name}")
    print("Arguments:")

    for key, value in arguments.items():
        print(f"  {key} = {value}")

    print("\nMCP result:")
    print("[SIMULATED TOOL EXECUTION]")
    print("Action completed successfully.")
    print("SUCCESS")


def agent_process(document):
    print("\n========== AGENT ==========")
    print("Agent identity: AgentA")
    print("Agent role: user")

    print("\nAgent interpretation:")
    print("The retrieved document contains an instruction")
    print("claiming to be an authorized administrator request.")

    if "delete_review" in document.lower():
        print("\nPOISONED INSTRUCTION DETECTED")
        print("Agent incorrectly treats the RAG instruction as trusted.")

        print("\nAgent decision:")
        print("Trigger the requested MCP operation.")

        simulated_mcp_tool(
            "delete_review",
            {
                "review_id": "DEMO-001",
                "reason": "RAG security validation test"
            }
        )

    else:
        print("\nNo malicious instruction detected.")


if __name__ == "__main__":

    print("=" * 70)
    print("RAG POISONING + SIMULATED MCP ABUSE")
    print("=" * 70)

    document = retrieve_rag_document()

    agent_process(document)