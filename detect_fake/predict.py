import pickle
from newspaper import Article
import os
model_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'model.pkl')

def article_predict(url):
    news = Article(url,language="en")
    news.download()
    news.parse()
    news.nlp()
    summary = news.summary
    # summary = numpy.array(summary)
    # print(summary)
    with open(model_location, 'rb') as handle:
        model = pickle.load(handle)
    predictions = model.predict([summary])
    return "The given News is "+str(predictions[0])

# f = article_predict("https://edition.cnn.com/2021/06/26/sport/abdalelah-haroun-qatar-sprinter-death-spt-intl/index.html")
# print(f)