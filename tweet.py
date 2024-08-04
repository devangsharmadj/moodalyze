import asyncio
from twikit import Client

USERNAME = 'moodalyze'
EMAIL = ''
PASSWORD = ''


client = Client('en-US')

async def main():
    await client.login(
        auth_info_1=USERNAME ,
        auth_info_2=EMAIL,
        password=PASSWORD
    )
    tweets = await client.search_tweet('python', 'Latest')
    print(tweets.text)

asyncio.run(main())

# if __name__ == "__main__":
#     asyncio.run(main()) 

    # tweets = await client.search_tweet('python', 'Latest')
    # print(tweets)
    

    # for j, tweet in enumerate(tweets):
    #     text = tweet.text
    #     text = preprocess(text)
    #     encoded_input = tokenizer(text, return_tensors='pt')
    #     output = model(**encoded_input)
    #     scores = output[0][0].detach().numpy()
    #     scores = softmax(scores)

    #     ranking = np.argsort(scores)
    #     print(f"Tweet #{j + 1}: {tweet.text}")
    #     ranking = ranking[::-1]
    #     for i in range(scores.shape[0]):
    #         l = labels[ranking[i]]
    #         s = scores[ranking[i]]
    #         print(f"{i+1}) {l} {np.round(float(s), 4)}")
