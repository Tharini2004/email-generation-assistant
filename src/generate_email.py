def generate_email(intent, facts, tone):
    return {
        "subject": "Sample Subject",
        "body": "Generated email based on input."
    }

if __name__ == "__main__":
    print(generate_email(
        "Follow up after interview",
        "Interviewed April 10",
        "Polite"
    ))
