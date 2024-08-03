from transformers import AutoModelForSequenceClassification
# from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax

# Constants
task='sentiment'
MODEL = f"cardiffnlp/twitter-roberta-base-{task}"

# tokenizer.save_pretrained("./model", from_pt=True)
# tokenizer.save_pretrained("./model")




# mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
# with urllib.request.urlopen(mapping_link) as f:
#     html = f.read().decode('utf-8').split("\n")
#     csvreader = csv.reader(html, delimiter='\t')
# labels = [row[1] for row in csvreader if len(row) > 1]
# model.save_pretrained("./model", from_pt=True)
# model.save_pretrained("./model")
class Analyzer():
    def __init__(self, task='sentiment', MODEL="cardiffnlp/twitter-roberta-base-sentiment", ) -> None:
        self.task = task
        self.MODEL = MODEL
        self.tokenizer = AutoTokenizer.from_pretrained('./model')
        self.labels = ['negative', 'neutral', 'positive']
        self.model = AutoModelForSequenceClassification.from_pretrained('./model')
    
    def preprocess(self, text):
        new_text = []
 
        for t in text.split(" "):
            t = '@user' if t.startswith('@') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            new_text.append(t)
        return " ".join(new_text)
    
    def process_tweet(self, q):

        text = q
        text = self.preprocess(text)
        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        result = {
        }
        ranking = ranking[::-1]
        for i in range(scores.shape[0]):
            l = self.labels[ranking[i]]
            s = scores[ranking[i]]
            result[l] = np.round(float(s), 4)
            # print(f"{i+1}) {l} {np.round(float(s), 4)}")
        return result































