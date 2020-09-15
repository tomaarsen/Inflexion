
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..')) 

from inflexion.adjective import Adjective
adjectives = ['defiant', 'homeless', 'adorable', 'delightful', 'homely', 'quaint', 'adventurous', 'depressed', 'horrible', 'aggressive', 'determined', 'hungry', 'real', 'agreeable', 'different', 'hurt', 'relieved', 'alert', 'difficult', 'repulsive', 'alive', 'disgusted', 'ill', 'rich', 'amused', 'distinct', 'important', 'angry', 'disturbed', 'impossible', 'scary', 'annoyed', 'dizzy', 'inexpensive', 'selfish', 'annoying', 'doubtful', 'innocent', 'shiny', 'anxious', 'drab', 'inquisitive', 'shy', 'arrogant', 'dull', 'itchy', 'silly', 'ashamed', 'sleepy', 'attractive', 'eager', 'jealous', 'smiling', 'average', 'easy', 'jittery', 'smoggy', 'awful', 'elated', 'jolly', 'sore', 'elegant', 'joyous', 'sparkling', 'bad', 'embarrassed', 'splendid', 'beautiful', 'enchanting', 'kind', 'spotless', 'better', 'encouraging', 'stormy', 'bewildered', 'energetic', 'lazy', 'strange', 'black', 'enthusiastic', 'light', 'stupid', 'bloody', 'envious', 'lively', 'successful', 'blue', 'evil', 'lonely', 'super', 'blue-eyed', 'excited', 'long', 'blushing', 'expensive', 'lovely', 'talented', 'bored', 'exuberant', 'lucky', 'tame', 'brainy', 'tender', 'brave', 'fair', 'magnificent', 'tense', 'breakable', 'faithful', 'misty', 'terrible', 'bright', 'famous', 'modern', 'tasty', 'busy', 'fancy', 'motionless', 'thankful', 'fantastic', 'muddy', 'thoughtful', 'calm', 'fierce', 'mushy', 'thoughtless', 'careful', 'filthy', 'mysterious', 'tired', 'cautious', 'fine', 'tough', 'charming', 'foolish', 'nasty', 'troubled', 'cheerful', 'fragile', 'naughty', 'clean', 'frail', 'nervous', 'ugliest', 'clear', 'frantic', 'nice', 'ugly', 'clever', 'friendly', 'nutty', 'uninterested', 'cloudy', 'frightened', 'unsightly', 'clumsy', 'funny', 'obedient', 'unusual', 'colorful', 'obnoxious', 'upset', 'combative', 'gentle', 'odd', 'uptight', 'comfortable', 'gifted', 'old-fashioned', 'concerned', 'glamorous', 'open', 'vast', 'condemned', 'gleaming', 'outrageous', 'victorious', 'confused', 'glorious', 'outstanding', 'vivacious', 'cooperative', 'good', 'courageous', 'gorgeous', 'panicky', 'wandering', 'crazy', 'graceful', 'perfect', 'weary', 'creepy', 'grieving', 'plain', 'wicked', 'crowded', 'grotesque', 'pleasant', 'wide-eyed', 'cruel', 'grumpy', 'poised', 'wild', 'curious', 'poor', 'witty', 'cute', 'handsome', 'powerful', 'worrisome', 'happy', 'precious', 'worried', 'dangerous', 'healthy', 'prickly', 'wrong', 'dark', 'helpful', 'proud', 'dead', 'helpless', 'putrid', 'zany', 'defeated', 'hilarious', 'puzzled', 'zealous']

for adj in adjectives:
    a = Adjective()
    print()
breakpoint()
