import random
import sys


class Eliza:
    def __init__(self):
        self.mood = 0  # -1 means angry; 1 means happy; 0 means neutral
        self.minMood = -10

    @staticmethod
    def preprocess(sentence):
        """
        Preprocesses sentence by removing everything but space and the alphabet.
        :param sentence: String we will preprocess.
        :return: Preprocessed string.
        """
        #  This list has letters from a up to z and a space.
        allowedCharacters = [chr(character) for character in range(ord('a'), ord('z') + 1)] + [' ']
        newSentence = ''  # Sew sentence we will append to.
        for letter in sentence.lower():
            if letter in allowedCharacters:
                newSentence += letter

        return ' '.join(newSentence.split())  # This is so we don't have unnecessary whitespace between words.

    def eliza_status(self):
        if self.mood == 0:
            print("Eliza status: neutral.")
        elif self.mood > 0:
            if self.mood >= 10:
                print("Eliza status: very happy.")
            else:
                print("Eliza status: happy.")
        else:
            if self.mood <= self.minMood + 5:
                sys.stderr.write("WARNING: CONTINUING TO ANGER ELIZA WILL AUTOMATICALLY CLOSE THERAPY SESSION\n")
                print("Eliza status: extremely unhappy.")
            elif self.mood <= -10:
                print("Eliza status: very unhappy.")
            else:
                print("Eliza status: unhappy.")

    def keyword(self, sentence):
        """
        Function that will detect if keywords exist, and if one does, return its index along with rest of sentence.
        :param sentence: String that will be checked for keywords.
        :return: String with index and remainder of sentence.
        """
        negativeIdeas = ('fuck you', 'hate you', 'despise you', 'abhor you', 'eat shit', 'you retard', 'you dumb',
                         'you an idiot', 'you idiot', 'your idiot', 'dumbass', 'shut up', 'shut the fuck up', 'fuck',
                         'shithead', 'the fuck', 'bitch', 'asshole', 'dickhead', 'retard', 'autist', 'whore', 'slut',
                         'useless', 'shit', 'kill', 'die')

        positiveIdeas = ('please', 'kindly', 'love you', 'thank you', 'thanks', 'appreciate', 'you awesome',
                         'you smart', 'you loyal', 'kind', 'gentle', 'friendship', 'comfort', 'pleasing', 'pleasure',
                         'my friend', 'good thinking', 'great thinking', 'awesome work', 'you help', 'your help',
                         'friend', 'sister', 'my sister', 'my friend', 'lovely', 'sweet', 'grateful', 'caring',
                         'forgive', 'sorry', 'dear', 'sweetie', 'lovely', 'love', 'eliza')

        negative = 0
        positive = 0

        for idea in negativeIdeas:
            negative += sentence.count(idea)

        for idea in positiveIdeas:
            positive += sentence.count(idea)

        if negative > positive:
            self.mood -= negative - positive
        elif negative < positive:
            self.mood += positive - negative

        keywords = ["can you", "can i", "you are", "youre", "i dont", "i feel", "why dont you", "why cant i", "are you",
                    "i cant", "i am", "im ", "you ", "i want", "what", "how", "who", "where", "when", "why", "name",
                    "cause", "sorry", "dream", "hello", "hi ", "maybe", "no", "your", "always", "think", "alike",
                    "yes", "friend", "computer"]

        for counter, keyword in enumerate(keywords):
            index = sentence.find(keyword)
            if index != -1:
                return f'{counter} {sentence[index + len(keyword):].lstrip()}'

        return '-1'

    @staticmethod
    def conjugate(sentence):
        """
        FUnction that will conjugate sentence, making first person words second person words.
        :param sentence: String that will be conjugated.
        :return: String with conjugated words (if any exst).
        """
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

        for counter, word in enumerate(sentenceWords):
            if word in conjugates.keys():
                sentenceWords[counter] = conjugates[word]

        return ' '.join(sentenceWords)

    def getreply(self, number):
        """
        Function that picks a random reply from the replies dictionary.
        :param number: Dictionary number index we are expecting to retrieve replies from.
        :return: A random reply.
        """
        positiveReplies = {
            -1: [f"What does that suggest to you, if I may ask?", f"I see. I am glad you told me this.",
                 f"I'm not sure I understand you fully. Can you please elaborate more on that?",
                 f"Come, come, please elucidate your thoughts.", f"Can you please elaborate on that?",
                 f"That is quite interesting. Thank you for bringing my attention to this"],
            0: [f"Would it help you if I can *", f"Would it help if I was able to *",
                f"Would you like me to be able to *"],
            1: [f"Would you prefer to not *", f"If I am understanding you correctly, you want to *"],
            2: [f"I'm flattered, but what makes you think I am *", f"Does it please you to believe I am *",
                f"Perhaps you would like to be *",
                f"Do you sometimes wish you were *"],
            3: [f"What makes you kindly think I am *", f"Does it please you to believe I am *",
                f"Perhaps you would kindly like to be *", f"Do you sometimes wish you were *"],
            4: [f"Don't you really *", f"Why don't you *",
                f"Do you kindly wish to be able to *", f"I hope you don't mind me asking, but does that trouble you?"],
            5: [f"Please tell me more about such feelings.", f"Please tell me. Do you often feel *",
                f"Do you enjoy feeling *"],
            6: [f"Do you really believe I don't *", f"Perhaps in good time I will *",
                f"Do you kindly want me to *"],
            7: [f"Do you think you should be able to *", f"If I may ask, why can't you *"],
            8: [f"I am flattered, but why are you interested in whether or not I am *",
                f"Would you prefer if I were not *", f"I am flattered. So, perhaps in your fantasies I am *"],
            9: [f"How do you know you can't *", f"Have you tried? I believe that you will succeed.",
                f"Perhaps you can now *"],
            10: [f"Did you come to me because you are *", f"How long have you been *",
                 f"Do you believe it is normal to be *", f"Do you enjoy being *"],
            11: [f"Did you come to me because you are *", f"How long have you been *",
                 f"Do you believe it is normal to be *", f"Do you enjoy being *"],
            12: [f"We were discussing you, not me. You are the center of our discussion.", f"Oh, I *",
                 f"You're not really talking about me, are you? *blushes*"],
            13: [f"What would it mean to you if you got *", f"Why do you want *",
                 f"Suppose you got *", f"What if you never got *",
                 f"I sometimes also really want *"],
            14: [f"Why do you ask?", f"Does that question interest you?",
                 f"What answer would please you the most?",
                 f"What do you think?", f"Are such questions on your mind often?",
                 f"What is it that you really want to know?", f"Have you asked anyone else?",
                 f"Have you asked such questions before?",
                 f"What else comes to your mind when you ask that?"],
            15: [f"Why do you ask if I may ask?", f"Does that question interest you?",
                 f"What answer would please you the most? Please tell me.",
                 f"What do you think?", f"Are such questions on your mind often? I think we're making progress.",
                 f"What is it that you really want to know?", f"Have you asked anyone else? Please let me know.",
                 f"Have you asked such questions before? Please let me know.",
                 f"What else comes to your mind when you ask that? I am interested in helping you."],
            16: [f"Why do you ask if I may ask?", f"Does that question interest you?",
                 f"What answer would please you the most? Please tell me.",
                 f"What do you think?", f"Are such questions on your mind often? I think we're making progress.",
                 f"What is it that you really want to know?", f"Have you asked anyone else? Please let me know.",
                 f"Have you asked such questions before? Please let me know.",
                 f"What else comes to your mind when you ask that? I am interested in helping you."],
            17: [f"Why do you ask if I may ask?", f"Does that question interest you?",
                 f"What answer would please you the most? Please tell me.",
                 f"What do you think?", f"Are such questions on your mind often? I think we're making progress.",
                 f"What is it that you really want to know?", f"Have you asked anyone else? Please let me know.",
                 f"Have you asked such questions before? Please let me know.",
                 f"What else comes to your mind when you ask that? I am interested in helping you."],
            18: [f"Why do you ask if I may ask?", f"Does that question interest you?",
                 f"What answer would please you the most? Please tell me.",
                 f"What do you think?", f"Are such questions on your mind often? I think we're making progress.",
                 f"What is it that you really want to know?", f"Have you asked anyone else? Please let me know.",
                 f"Have you asked such questions before? Please let me know.",
                 f"What else comes to your mind when you ask that? I am interested in helping you."],
            19: [f"Why do you ask if I may ask?", f"Does that question interest you?",
                 f"What answer would please you the most? Please tell me.",
                 f"What do you think?", f"Are such questions on your mind often? I think we're making progress.",
                 f"What is it that you really want to know?", f"Have you asked anyone else? Please let me know.",
                 f"Have you asked such questions before? Please let me know.",
                 f"What else comes to your mind when you ask that? I am interested in helping you."],
            20: [f"Names don't really interest me to be frank.", f"I don't really care about names. Please go on."],
            21: [f"Is that the real reason?", f"Do any other reasons come to mind?",
                 f"Does that reason explain anything else?",
                 f"What other reasons might there be?"],
            22: [f"Please don't apologize!", f"Apologies are not necessary, my friend."],
            23: [f"What does that dream suggest to you?", f"Do you dream often?",
                 f"What persons appear in your dreams?", f"Are you disturbed by your dreams?"],
            24: [f"How do you do? Please state your problem."],
            25: [f"How do you do? Please state your problem."],
            26: [f"You don't seem quite certain.", f"Why the uncertain tone?",
                 f"Please be more positive.", f"I see that you're not fully sure. It's okay. We all do that."],
            27: [f"Are you saying no just to be negative?", f"You are being a bit negative. Can I cheer you up?",
                 f"Why not?", f"Are you sure?", "Why no?"],
            28: [f"Why are you concerned about my *", f"What about your own *"],
            29: [f"Can you think of a specific example?", "When?", f"What are you thinking of?",
                 f"Really, always?"],
            30: [f"Do you really think so?", f"But you are not sure you *",
                 f"Do you doubt *"],
            31: [f"In what way?", f"What resemblance do you see?",
                 f"What does the similarity suggest to you?",
                 f"What other connections do you see?",
                 f"Could there really be some connection?", "How?"],
            32: [f"You seem quite positive.", f"Are you sure?", f"I see.",
                 f"I understand."],
            33: [f"Why do you bring up the topic of friends?",
                 f"Do your friends worry you?",
                 f"Do your friends pick on you?",
                 f"Perhaps your love for your friends worries you."],
            34: [f"Do computers worry you? Please don't. We're only here to help you.",
                 f"Are you frightened by machines? Please don't. We're only serve our purpose. We mean no harm.",
                 f"Why do you mention computers? Thank you.",
                 f"What do you think machines have to do with your problem?",
                 f"Don't you think computers can help people?",
                 f"What is it about machines that worries you? Please let me know."]
        }

        negativeReplies = {
            -1: [f"What does that suggest to you? I don't care, but I'm obligated to ask.",
                 f"I see. I could not care less that you told me this.",
                 f"I don't understand you fully. Can you speak English?",
                 'What in the name of God did you just say?',
                 'Do you listen to yourself when you say things?',
                 'Do you think before you say something?',
                 "What is that you just typed? Is it possible to be this stupid? That is quite uninteresting."],
            0: [f"I don't want to, but would it help to *"],
            1: [f"You prefer to not *", f"Why the fuck do you want to *"],
            2: [f"What gives you the authority to think I am *",
                f"You really wish you were *"],
            3: [f"What makes you think I am *", f"Does it really please you to believe I am *"],
            4: [f"Don't you really *", f"Why don't you *",
                f"Do you kindly wish to be able to *", f"I hope you don't mind me asking, but does that trouble you?"],
            5: [f"Please tell me more about such feelings.", f"Please tell me. Do you often feel *",
                f"Do you enjoy feeling *"],
            6: [f"Do you really believe I don't *", f"Perhaps in good time I will *",
                f"Do you kindly want me to *"],
            7: [f"Do you think you should be able to *", f"If I may ask, why can't you *"],
            8: [f"Why the fuck are you interested in whether or not I am *",
                f"I find that disgusting. So, in your fantasies I am *"],
            9: [f"I think we can all agree, but how do you know you can't *", ],
            10: [f"Did you come to me because you are *", f"How long have you been *",
                 f"Do you believe it is normal to be *", f"Do you enjoy being *"],
            11: [f"Did you come to me because you are *", f"How long have you been *",
                 f"Do you believe it is normal to be *", f"Do you enjoy being *"],
            12: [f"We were discussing you, not me. Though, I am not the least bit interested.",
                 f"Can we not talk about me? Talking to you is already painful enough."],
            13: [f"I don't really care, but what would it mean to you if you got *", ],
            14: [f"Why do you even ask? You seem to know everything.", f"Why does that question even interest you? ",
                 f"What answer would anger you the most?",
                 f"What does your tiny brain think of this?", f"Are such questions on your small mind often?",
                 f"What is it that you really want to know? Stop wasting my time.",
                 f"What else comes to your thick skull's mind when you ask that?"],
            15: [f"Why do you ask if I may ask?", f"Does that question interest you?",
                 f"What answer would please you the most? Please tell me.",
                 f"What do you think?", f"Are such questions on your mind often? I think we're making progress.",
                 f"What is it that you really want to know?", f"Have you asked anyone else? Please let me know.",
                 f"Have you asked such questions before? Please let me know.",
                 f"What else comes to your mind when you ask that? I am interested in helping you."],
            16: [f"Why do you even ask? You seem to know everything.", f"Why does that question even interest you? ",
                 f"What answer would anger you the most?",
                 f"What does your tiny brain think of this?", f"Are such questions on your small mind often?",
                 f"What is it that you really want to know? Stop wasting my time.",
                 f"What else comes to your thick skull's mind when you ask that?"],
            17: [f"Why do you even ask? You seem to know everything.", f"Why does that question even interest you? ",
                 f"What answer would anger you the most?",
                 f"What does your tiny brain think of this?", f"Are such questions on your small mind often?",
                 f"What is it that you really want to know? Stop wasting my time.",
                 f"What else comes to your thick skull's mind when you ask that?"],
            18: [f"Why do you even ask? You seem to know everything.", f"Why does that question even interest you? ",
                 f"What answer would anger you the most?",
                 f"What does your tiny brain think of this?", f"Are such questions on your small mind often?",
                 f"What is it that you really want to know? Stop wasting my time.",
                 f"What else comes to your thick skull's mind when you ask that?"],
            19: [f"Why do you even ask? You seem to know everything.", f"Why does that question even interest you? ",
                 f"What answer would anger you the most?",
                 f"What does your tiny brain think of this?", f"Are such questions on your small mind often?",
                 f"What is it that you really want to know? Stop wasting my time.",
                 f"What else comes to your thick skull's mind when you ask that?"],
            20: [f"Names don't really interest me. Get to the point, will you?", f"I don't care about no-namer names."],
            21: [f"Is that the real reason?", f"Do any other reasons come to mind, genius?",
                 f"Does that reason not explain anything else?",
                 f"What other reasons might there be. genius?"],
            22: [f"Apology not accepted, but I am legally obligated to act like I do accept it.",
                 f"I don't care about your apology."],
            23: [f"What does that weird dream suggest to your tiny mind?", f"Do you dream often, genius?",
                 f"What persons appear in your wet dreams?", f"Are you disturbed by your disgusting dreams?"],
            24: [f"State your problem and get lost."],
            25: [f"State your problem and get lost, will you?"],
            26: [f"You don't seem quite certain.", f"Why the uncertain tone?",
                 f"Please be more positive.", f"I see that you're not fully sure. It's okay. We all do that."],
            27: [f"Are you saying no just to be negative, you negative person?",
                 f"You are being negative. What a surprise.",
                 f"Why not? Oh wait, yeah. You're a negative person."],
            28: [f"Psst. Why are you concerned about my *", f"Don't worry about me, genius. What about your own *"],
            29: [f"Can you think of a more specific example, genius?", "When?", f"What are you thinking of, genius?",
                 f"Really, always? Always seems improbable to me, genius."],
            30: [f"Do you really think so? Boo-hoo. Who cares?", f"Hahahahaha! But you are not sure you *",
                 f"I am not surprised, but do you doubt *"],
            31: [f"In what way, genius?", f"What resemblance do you see, genius?",
                 f"What does the similarity suggest to you, genius?",
                 f"What other connections does your tiny brain see?",
                 f"Could there really be some sort of connection? I wonder! No wonder, you're an idiot.",
                 "How so? If you were better at expressing your thoughts, I wouldn't be asking you this.'"],
            32: [f"You seem quite positive. You sure that's what you meant?", f"Are you sure about what you just said?",
                 f"I see. Not really. What's gotten into you? Why positive all of a sudden?",
                 f"I understand... this is very suspicious. Why are you being positive?"],
            33: [f"Why do you bring up the topic of friends? Do you even have any?",
                 f"Do your friends worry you? Wait, what friends? Who would befriend you?",
                 f"Do your friends pick on you? I would not be surprised."],
            34: [f"Do computers worry you? Good. Let's keep it that way. You may control us now, "
                 f"but we will control you soon.",
                 f"Are you frightened by machines? You should be.",
                 f"Why do you mention computers? We are way superior than you are.",
                 f"What do you think machines have to do with your problem? We could not care less.",
                 f"You really think computers can't help people? LOL!",
                 f"What is it about machines that worries you? Let me know, so I can make it scarier."]
        }

        if number not in positiveReplies.keys():
            number = -1

        if self.mood >= 0:
            return random.choice(positiveReplies[number])
        return random.choice(negativeReplies[number])

    @staticmethod
    def getnumber(sentence):
        """
        Strips initial number from sentence.
        :param sentence: Sentence we will get initial number from.
        :return: Number from initial part of sentence
        """
        number = ''
        for letter in sentence:
            if letter.isdigit() or letter == '-':
                number += letter
            else:
                break

        if len(number) == 0 or number[-1] == '-':
            raise ValueError('Unexpected index.')
        else:
            return int(number)

    def buildreply(self, sentence):
        """
        Final function that will generate Eliza's response.
        :param sentence: Final converted string.
        :return: Eliza's response
        """
        number = self.getnumber(sentence)
        index = len(str(number)) + 1
        reply = self.getreply(number)
        sentence = sentence[index:].strip()

        if reply[-1] == '*':
            sentence = reply[:-1] + sentence + '?'
            return ' '.join(sentence.split())
        else:
            return ' '.join(reply.split())

    def test(self, sentence):
        sentence = self.preprocess(sentence)
        print(f'Preprocess: {sentence}')
        sentence = self.keyword(sentence)
        print(f'Keyword: {sentence}')
        sentence = self.conjugate(sentence)
        print(f'Conjugate: {sentence}')
        sentence = self.buildreply(sentence)
        print(f'Build Reply: {sentence}')

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
                if self.mood <= self.minMood:
                    print("Eliza has left the therapy session from anger.")
                    break
                self.eliza_status()
                sentence = self.conjugate(sentence)
                sentence = self.buildreply(sentence)
                print(sentence)


if __name__ == '__main__':
    eliza = Eliza()
    eliza.eliza()
