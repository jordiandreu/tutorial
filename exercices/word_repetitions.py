import re

text = "This is my first technical interview and I never had   a technical interview to access a work position before. " \
       "Nevertheless, I'm very exited about this and I will do my best."


def remove_punctuation(text):
    # return text.replace("'", '').replace(".", '').replace("'", ' ').replace(",", '').lower().split(' ')
    # remove characters
    _text = re.sub("[.,:;]", " ", text)
    # replace by space
    return [x.strip() for x in re.sub("[']", "", _text).split(" ") if len(x) > 0]

def get_histogram(text):
    print(text)
    text = remove_punctuation(text)
    print(text)

    histogram = {}

    for word in text:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram


def sorted_by_value(dct, reversed=False):
    return {k: v for k, v in sorted(dct.items(), key=lambda x: x[1], reverse=reversed)}



if __name__ == "__main__":
    result = get_histogram(text)
    result = sorted_by_value(result, reversed=True)
    for k, v in result.items():
        print(f"{k}: {v} time(s)")



