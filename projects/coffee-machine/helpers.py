def prompt_str(msg) -> str:
    ans: str = ""
    while len(ans) == 0:
        ans = input(msg).strip()
    return ans


def prompt_int(msg) -> float:
    while True:
        try:
            coins: float = float(input(msg).strip())
            print(f"You entered: ${coins}")
            return coins
        except ValueError as _:
            print("Invalid input. Try again:")
