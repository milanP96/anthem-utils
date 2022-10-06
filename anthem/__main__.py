import os


def main():
    envs = [
        os.getenv('AWS_S3_REGION_NAME'),
        os.getenv('AWS_ACCESS_KEY_ID'),
        os.getenv('AWS_SECRET_ACCESS_KEY'),
        os.getenv('ENV_KEY')
    ]

    missing = filter(lambda x: not x, envs)

    if len(list(missing)):
        raise ValueError("Missing env variables")


if __name__ == "__main__":
    main()
