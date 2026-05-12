from datasets import load_dataset

def get_dataset():
    dataset = load_dataset("zeroshot/twitter-financial-news-sentiment")
    return dataset

if __name__ == "__main__":
    dataset = get_dataset()
    train = dataset["train"]

    for i in range(5):
        print(f"Tweet {i+1}:")
        print("Text:", train[i]["text"])
        print("Label:", train[i]["label"])
        print("-" * 50)

        