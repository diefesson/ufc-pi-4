from nltk.corpus import stopwords


_english_stopwords = stopwords.words("english")


def comment_to_keywords(comment):
    comment_words = [word.lower() for word in comment.split(" ") if word.isalpha()]
    comment_keywords = [
        word for word in comment_words if word not in _english_stopwords
    ]
    return comment_keywords


def collect_keywords(keyword_lists):
    keyword_set = set()
    keyword_list = []
    for keywords in keyword_lists:
        for keyword in keywords:
            if keyword not in keyword_set:
                keyword_set.add(keyword)
                keyword_list.append(keyword)
    return keyword_list


def extract_features(keywords, know_keywords):
    return {keyword: keyword in know_keywords for keyword in keywords}


def extract_label(offensiveness_score):
    return "offensive" if offensiveness_score > 0 else "not_offensive"
