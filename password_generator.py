import secrets
import string


def generate_password(length=16):
    alphabet = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()-_=+"
    )
    return "".join(secrets.choice(alphabet) for _ in range(length))


if __name__ == "__main__":
    print("Generated password:")
    print(generate_password())
