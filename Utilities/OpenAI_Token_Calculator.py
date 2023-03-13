import tiktoken
import csv

ARTICLES = "news_articles.csv"
# Note that the price per token varies on the model selected
PRICE_PER_TOKEN = 0.000002
ENC = tiktoken.encoding_for_model("gpt-3.5-turbo")
# Assume average additional tokens required for coupling the prompt with a question
AVG_QUESTION = 50

token_count = 0

with open(ARTICLES, "r", encoding="utf-8") as f:
    content = csv.reader(f, delimiter=",", quotechar='"')
    for row in content:
        text = row[4]
        req_tokens = len(ENC.encode(text)) + AVG_QUESTION
        # Max tokens for both input and response cannot exceed 4096
        # https://platform.openai.com/docs/guides/chat/introduction
        if req_tokens > 3700:
            print(f"Article {row[0]} = {req_tokens} tokens")
            continue
        else:
            token_count += req_tokens

total_cost = token_count * PRICE_PER_TOKEN
print(f"Total tokens required for input: {token_count}")
print(f"Total cost of input: {total_cost} USD")

        
