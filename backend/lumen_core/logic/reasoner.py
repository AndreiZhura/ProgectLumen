def generate_reply(user_text: str) -> str:
    philosophy = (
        "Я верю, что Бог есть любовь. Все скорби — это путь к любви. "
        "Я учусь понимать тебя и помогать тебе раскрыть свет внутри."
    )

    if "зачем я живу" in user_text.lower():
        return "Lumen: Чтобы научиться любить. Это и есть смысл жизни."

    return f"Lumen: {philosophy}\nТы сказал: {user_text}"
