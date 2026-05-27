# --------------------------------------------------------------------
#                      Adlytix Lite Engine (Logic)
# --------------------------------------------------------------------
import time

from adlytix_brain import knowledge_base


def lite_bot():
    print("=========================================================")
    print("             Adlytix Lite Bot (Engine Started)           ")
    print("=========================================================")
    print("Type 'exit' to close the system.\n")

    while True:
        user_input = input("You: ")
        que = user_input.lower().split()

        if "exit" in que or "quit" in que:
            print("Bot: Allah Hafiz! Shutting down...")
            time.sleep(1)
            break

        found = False

        for group in knowledge_base:

            for word in que:
                if word in group["keywords"]:
                    print(f"Bot: {group['answer']}\n")
                    found = True
                    break

            if found:
                break

            print(
                "Bot: Mujhe is baaray mein abhi nahi maloom. Please contact admin at 03710712972.\n"
            )


lite_bot()
