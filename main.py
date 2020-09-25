import random


class Eliza:
    def __init__(self):
        self.mood = 0  # Negative numbers mean angry; positive mean happy.

    @staticmethod
    def preprocess(sentence):
        #  This list has letters from a up to z and a space.
        allowedCharacters = [chr(character) for character in range(ord('a'), ord('z') + 1)] + [' ']
        newSentence = ''  # Sew sentence we will append to.
        for letter in sentence.lower():
            if letter in allowedCharacters:
                newSentence += letter

        return ' '.join(newSentence.split())  # This is so we don't have unnecessary whitespace.

    @staticmethod
    def keyword(sentence):
        keywords = ["can you", "can i", "you are", "youre", "i dont", "i feel", "why dont you", "why cant i", "are you",
                    "i cant", "i am", "im ", "you ", "i want", "what", "how", "who", "where", "when", "why", "name",
                    "cause", "sorry", "dream", "hello", "hi ", "maybe", "no", "your", "always", "think", "alike",
                    "yes", "friend", "computer"]

        for counter, keyword in enumerate(keywords):
            tempWord = f'{keyword} '
            index = sentence.find(tempWord)
            if index != -1:
                return f'{counter}{sentence[index + len(keyword):]}'

        return '-1'

    @staticmethod
    def conjugate(sentence):
        conjugates = {
            'are': 'am',
            'am': 'are',
            'were': 'was',
            'was': 'were',
            'you': 'I',
            'i': 'you',
            'your': 'my',
            'my': 'your',
            'ive': "you've",
            'youve': "I've",
            'im': "you're",
            'youre': "I'm",
            'me': 'you'
        }

        sentenceWords = sentence.split()
        newSentenceList = []

        for word in sentenceWords:
            if word in conjugates.keys():
                newSentenceList.append(conjugates[word])
            else:
                newSentenceList.append(word)

        return ' '.join(newSentenceList)

    @staticmethod
    def getreply(number):
        replies = {
            -1: ["What does that suggest to you?", "I see.", "I'm not sure I understand you fully.",
                 "Come, come, elucidate your thoughts.", "Can you elaborate on that?", "That is quite interesting."],
            0: ["Don't you believe that I can *", "Perhaps you would like me to be able to *",
                "You want me to be able to *"],
            1: ["Perhaps you don't want to *", "Do you want to be able to *"],
            2: ["What makes you think I am *", "Does it please you to believe I am *", "Perhaps you would like to be *",
                "Do you sometimes wish you were *"],
            3: ["What makes you think I am *", "Does it please you to believe I am *", "Perhaps you would like to be *",
                "Do you sometimes wish you were *"],
            4: ["Don't you really *", "Why don't you *", "Do you wish to be able to *", "Does that trouble you?"],
            5: ["Tell me more about such feelings.", "Do you often feel *", "Do you enjoy feeling *"],
            6: ["Do you really believe I don't *", "Perhaps in good time I will *", "Do you want me to *"],
            7: ["Do you think you should be able to *", "Why can't you *"],
            8: ["Why are you interested in whether or not I am *", "Would you prefer if I were not *",
                "Perhaps in your fantasies I am *"],
            9: ["How do you know you can't *", "Have you tried?", "Perhaps you can now *"],
            10: ["Did you come to me because you are *", "How long have you been *",
                 "Do you believe it is normal to be *", "Do you enjoy being *"],
            11: ["Did you come to me because you are *", "How long have you been *",
                 "Do you believe it is normal to be *", "Do you enjoy being *"],
            12: ["We were discussing you, not me.", "Oh, I *", "You're not really talking about me, are you?"],
            13: ["What would it mean to you if you got *", "Why do you want *", "Suppose you got *",
                 "What if you never got *", "I sometimes also want *"],
            14: ["Why do you ask?", "Does that question interest you?", "What answer would please you the most?",
                 "What do you think?", "Are such questions on your mind often?",
                 "What is it that you really want to know?", "Have you asked anyone else?",
                 "Have you asked such questions before?", "What else comes to your mind when you ask that?"],
            15: ["Why do you ask?", "Does that question interest you?", "What answer would please you the most?",
                 "What do you think?", "Are such questions on your mind often?",
                 "What is it that you really want to know?", "Have you asked anyone else?",
                 "Have you asked such questions before?", "What else comes to your mind when you ask that?"],
            16: ["Why do you ask?", "Does that question interest you?", "What answer would please you the most?",
                 "What do you think?", "Are such questions on your mind often?",
                 "What is it that you really want to know?", "Have you asked anyone else?",
                 "Have you asked such questions before?", "What else comes to your mind when you ask that?"],
            17: ["Why do you ask?", "Does that question interest you?", "What answer would please you the most?",
                 "What do you think?", "Are such questions on your mind often?",
                 "What is it that you really want to know?", "Have you asked anyone else?",
                 "Have you asked such questions before?", "What else comes to your mind when you ask that?"],
            18: ["Why do you ask?", "Does that question interest you?", "What answer would please you the most?",
                 "What do you think?", "Are such questions on your mind often?",
                 "What is it that you really want to know?", "Have you asked anyone else?",
                 "Have you asked such questions before?", "What else comes to your mind when you ask that?"],
            19: ["Why do you ask?", "Does that question interest you?", "What answer would please you the most?",
                 "What do you think?", "Are such questions on your mind often?",
                 "What is it that you really want to know?", "Have you asked anyone else?",
                 "Have you asked such questions before?", "What else comes to your mind when you ask that?"],
            20: ["Names don't interest me.", "I don't care about names.  Please go on."],
            21: ["Is that the real reason?", "Don't any other reasons come to mind?",
                 "Does that reason explain anything else?", "What other reasons might there be?"],
            22: ["Please don't apologize!", "Apologies are not necessary."],
            23: ["What does that dream suggest to you?", "Do you dream often?", "What persons appear in your dreams?",
                 "Are you disturbed by your dreams?"],
            24: ["How do you do.  Please state your problem."],
            25: ["How do you do.  Please state your problem."],
            26: ["You don't seem quite certain.", "Why the uncertain tone?", "Can't you be more positive?",
                 "You aren't sure?", "Don't you know?"],
            27: ["Are you saying no just to be negative?", "You are being a bit negative.", "Why not?", "Are you sure?",
                 "Why no?"],
            28: ["Why are you concerned about my *", "What about your own *"],
            29: ["Can you think of a specific example?", "When?", "What are you thinking of?", "Really, always?"],
            30: ["Do you really think so?", "But you are not sure you *", "Do you doubt *"],
            31: ["In what way?", "What resemblance do you see?", "What does the similarity suggest to you?",
                 "What other connections do you see?", "Could there really be some connection?", "How?"],
            32: ["You seem quite positive.", "Are you sure?", "I see.", "I understand."],
            33: ["Why do you bring up the topic of friends?", "Do your friends worry you?",
                 "Do your friends pick on you?", "Are you sure you have any friends?", "Do you impose on your friends?",
                 "Perhaps your love for your friends worries you."],
            34: ["Do computers worry you?", "Are you frightened by machines?", "Why do you mention computers?",
                 "What do you think machines have to do with your problem?",
                 "Don't you think computers can help people?", "What is it about machines that worries you?"]
        }

        if number not in replies.keys():
            number = -1

        return random.choice(replies[number])

    def buildreply(self, sentence):
        try:
            number = int(sentence[:2])
            index = 2
        except ValueError:
            number = int(sentence[0])
            index = 1

        reply = self.getreply(number)
        sentence = sentence[index:].strip()

        if reply[-1] == '*':
            return reply[:-1] + sentence + '?'
        else:
            return reply

    def test(self, sentence):
        sentence = self.preprocess(sentence)
        print(f'Preprocess: {sentence}')
        sentence = self.keyword(sentence)
        print(f'Keyword: {sentence}')
        sentence = self.conjugate(sentence)
        print(f'Conjugate: {sentence}')
        sentence = self.buildreply(sentence)
        print(sentence)

    def eliza(self):
        print("Hello, I am Eliza.  Tell me your problems.")
        while True:
            sentence = input(">")
            if sentence.lower() in ('bye', 'shut up'):
                break
            else:
                # self.test(sentence)
                sentence = self.preprocess(sentence)
                sentence = self.keyword(sentence)
                sentence = self.conjugate(sentence)
                sentence = self.buildreply(sentence)
                print(sentence)


if __name__ == '__main__':
    eliza = Eliza()
    eliza.eliza()
