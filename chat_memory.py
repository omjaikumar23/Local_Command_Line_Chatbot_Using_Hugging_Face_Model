class ChatMemory:
    """
    Sliding window memory for conversation history storing alternating User and Bot messages.
    """
    def __init__(self, max_turns=5):
        self.max_turns = max_turns
        self.history = []  # List of strings like "User: text" or "Bot: text"

    def add_user_message(self, message: str):
        self.history.append(f"User: {message}")
        self._truncate()

    def add_bot_message(self, message: str):
        self.history.append(f"Bot: {message}")
        self._truncate()

    def _truncate(self):
        # Keep only the last max_turns*2 entries (user+bot pairs)
        if len(self.history) > self.max_turns * 2:
            self.history = self.history[-self.max_turns*2:]

    def get_context(self) -> str:
        # Join history into a single string, separated by newlines
        return "\n".join(self.history)
