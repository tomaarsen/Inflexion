
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
## NOTE: This module was autogenerated. ##
## Contains no user-servicable parts!!! ##
##########################################

import unittest

from inflex import Verb


class TestVerbIsPlural(unittest.TestCase):
    '''
    test_args has the format [
        {
            "in":     ..., # (required)
            "out":    ..., # (required)
            "desc":   ..., # (optional)
            "kwargs": ...  # (optional)
        }, ...
    ]
    '''
    test_args = [
        {'in': 'Abide', 'out': True},
        {'in': 'Ache', 'out': True},
        {'in': 'Arc', 'out': True},
        {'in': 'Arise', 'out': True},
        {'in': 'Ask', 'out': True},
        {'in': 'Avalanche', 'out': True},
        {'in': 'Awake', 'out': True},
        {'in': 'Be', 'out': True},
        {'in': 'Beat', 'out': True},
        {'in': 'Become', 'out': True},
        {'in': 'Beget', 'out': True},
        {'in': 'Begin', 'out': True},
        {'in': 'Behold', 'out': True},
        {'in': 'Bellyache', 'out': True},
        {'in': 'Bend', 'out': True},
        {'in': 'Bet', 'out': True},
        {'in': 'Bias', 'out': True},
        {'in': 'Bite', 'out': True},
        {'in': 'Bleed', 'out': True},
        {'in': 'Blitz', 'out': True},
        {'in': 'Blow', 'out': True},
        {'in': 'Break', 'out': True},
        {'in': 'Bring', 'out': True},
        {'in': 'Build', 'out': True},
        {'in': 'Burn', 'out': True},
        {'in': 'Burst', 'out': True},
        {'in': 'Bus', 'out': True},
        {'in': 'Bust', 'out': True},
        {'in': 'Cache', 'out': True},
        {'in': 'Caddie', 'out': True},
        {'in': 'Can', 'out': True},
        {'in': 'Canvas', 'out': True},
        {'in': 'Catch', 'out': True},
        {'in': 'Caucus', 'out': True},
        {'in': 'Change', 'out': True},
        {'in': 'Choose', 'out': True},
        {'in': 'Chorus', 'out': True},
        {'in': 'Clap', 'out': True},
        {'in': 'Cling', 'out': True},
        {'in': 'Come', 'out': True},
        {'in': 'Continue', 'out': True},
        {'in': 'Cost', 'out': True},
        {'in': 'Could', 'out': True},
        {'in': 'Creche', 'out': True},
        {'in': 'Creep', 'out': True},
        {'in': 'Dare', 'out': True},
        {'in': 'Deal', 'out': True},
        {'in': 'Die', 'out': True},
        {'in': 'Dig', 'out': True},
        {'in': 'Dis', 'out': True},
        {'in': 'Dive', 'out': True},
        {'in': 'Do', 'out': True},
        {'in': 'Douche', 'out': True},
        {'in': 'Drag', 'out': True},
        {'in': 'Dream', 'out': True},
        {'in': 'Drink', 'out': True},
        {'in': 'Drive', 'out': True},
        {'in': 'Dwell', 'out': True},
        {'in': 'Eat', 'out': True},
        {'in': 'Expect', 'out': True},
        {'in': 'Fall', 'out': True},
        {'in': 'Feel', 'out': True},
        {'in': 'Fight', 'out': True},
        {'in': 'Find', 'out': True},
        {'in': 'Flee', 'out': True},
        {'in': 'Fling', 'out': True},
        {'in': 'Fly', 'out': True},
        {'in': 'Focus', 'out': True},
        {'in': 'Follow', 'out': True},
        {'in': 'Forbid', 'out': True},
        {'in': 'Foresee', 'out': True},
        {'in': 'Foretell', 'out': True},
        {'in': 'Forget', 'out': True},
        {'in': 'Forgive', 'out': True},
        {'in': 'Forsake', 'out': True},
        {'in': 'Gas', 'out': True},
        {'in': 'Get', 'out': True},
        {'in': 'Gild', 'out': True},
        {'in': 'Give', 'out': True},
        {'in': 'Go', 'out': True},
        {'in': 'Grind', 'out': True},
        {'in': 'Happen', 'out': True},
        {'in': 'Have', 'out': True},
        {'in': 'Help', 'out': True},
        {'in': 'Hew', 'out': True},
        {'in': 'Hie', 'out': True},
        {'in': 'Hit', 'out': True},
        {'in': 'Hocus', 'out': True},
        {'in': 'Hold', 'out': True},
        {'in': 'Hurt', 'out': True},
        {'in': 'Inlay', 'out': True},
        {'in': 'Insist', 'out': True},
        {'in': 'Interlay', 'out': True},
        {'in': 'Iris', 'out': True},
        {'in': 'Keep', 'out': True},
        {'in': 'Kill', 'out': True},
        {'in': 'Kneel', 'out': True},
        {'in': 'Knit', 'out': True},
        {'in': 'Know', 'out': True},
        {'in': 'Lay', 'out': True},
        {'in': 'Lead', 'out': True},
        {'in': 'Lean', 'out': True},
        {'in': 'Leap', 'out': True},
        {'in': 'Learn', 'out': True},
        {'in': 'Leave', 'out': True},
        {'in': 'Let', 'out': True},
        {'in': 'Lie', 'out': True},
        {'in': 'Like', 'out': True},
        {'in': 'Live', 'out': True},
        {'in': 'Look', 'out': True},
        {'in': 'Lose', 'out': True},
        {'in': 'Love', 'out': True},
        {'in': 'May', 'out': True},
        {'in': 'Mean', 'out': True},
        {'in': 'Meet', 'out': True},
        {'in': 'Menu', 'out': True},
        {'in': 'Might', 'out': True},
        {'in': 'Mislead', 'out': True},
        {'in': 'Mistake', 'out': True},
        {'in': 'Misunderstand', 'out': True},
        {'in': 'Move', 'out': True},
        {'in': 'Must', 'out': True},
        {'in': 'Need', 'out': True},
        {'in': 'Niche', 'out': True},
        {'in': 'Ought', 'out': True},
        {'in': 'Outvie', 'out': True},
        {'in': 'Overdraw', 'out': True},
        {'in': 'Overhear', 'out': True},
        {'in': 'Overtake', 'out': True},
        {'in': 'Preset', 'out': True},
        {'in': 'Prove', 'out': True},
        {'in': 'Provide', 'out': True},
        {'in': 'Psyche', 'out': True},
        {'in': 'Put', 'out': True},
        {'in': 'Quit', 'out': True},
        {'in': 'Quiz', 'out': True},
        {'in': 'Reach', 'out': True},
        {'in': 'Remain', 'out': True},
        {'in': 'Remember', 'out': True},
        {'in': 'Rend', 'out': True},
        {'in': 'Rent', 'out': True},
        {'in': 'Rid', 'out': True},
        {'in': 'Ring', 'out': True},
        {'in': 'Rise', 'out': True},
        {'in': 'Rive', 'out': True},
        {'in': 'Saw', 'out': True},
        {'in': 'Seek', 'out': True},
        {'in': 'Seem', 'out': True},
        {'in': 'Shake', 'out': True},
        {'in': 'Shall', 'out': True},
        {'in': 'Shave', 'out': True},
        {'in': 'Shed', 'out': True},
        {'in': 'Shit', 'out': True},
        {'in': 'Shoe', 'out': True},
        {'in': 'Should', 'out': True},
        {'in': 'Show', 'out': True},
        {'in': 'Shrink', 'out': True},
        {'in': 'Sing', 'out': True},
        {'in': 'Sink', 'out': True},
        {'in': 'Sit', 'out': True},
        {'in': 'Ski', 'out': True},
        {'in': 'Slay', 'out': True},
        {'in': 'Slide', 'out': True},
        {'in': 'Slink', 'out': True},
        {'in': 'Slit', 'out': True},
        {'in': 'Smell', 'out': True},
        {'in': 'Smite', 'out': True},
        {'in': 'Sneak', 'out': True},
        {'in': 'Sow', 'out': True},
        {'in': 'Speak', 'out': True},
        {'in': 'Speed', 'out': True},
        {'in': 'Spend', 'out': True},
        {'in': 'Spit', 'out': True},
        {'in': 'Spoil', 'out': True},
        {'in': 'Spring', 'out': True},
        {'in': 'Stand', 'out': True},
        {'in': 'Stave', 'out': True},
        {'in': 'Stay', 'out': True},
        {'in': 'Steal', 'out': True},
        {'in': 'Sting', 'out': True},
        {'in': 'Stink', 'out': True},
        {'in': 'Stop', 'out': True},
        {'in': 'Strew', 'out': True},
        {'in': 'Stride', 'out': True},
        {'in': 'Strip', 'out': True},
        {'in': 'Strive', 'out': True},
        {'in': 'Sublet', 'out': True},
        {'in': 'Sunburn', 'out': True},
        {'in': 'Swear', 'out': True},
        {'in': 'Sweat', 'out': True},
        {'in': 'Sweep', 'out': True},
        {'in': 'Swell', 'out': True},
        {'in': 'Swim', 'out': True},
        {'in': 'Swing', 'out': True},
        {'in': 'Talk', 'out': True},
        {'in': 'Tear', 'out': True},
        {'in': 'Thrive', 'out': True},
        {'in': 'Thrust', 'out': True},
        {'in': 'Tread', 'out': True},
        {'in': 'Undergo', 'out': True},
        {'in': 'Underlie', 'out': True},
        {'in': 'Understand', 'out': True},
        {'in': 'Undertake', 'out': True},
        {'in': 'Upset', 'out': True},
        {'in': 'Vex', 'out': True},
        {'in': 'Vie', 'out': True},
        {'in': 'Wait', 'out': True},
        {'in': 'Wake', 'out': True},
        {'in': 'Walk', 'out': True},
        {'in': 'Want', 'out': True},
        {'in': 'Watch', 'out': True},
        {'in': 'Wear', 'out': True},
        {'in': 'Weep', 'out': True},
        {'in': 'Wend', 'out': True},
        {'in': 'Were', 'out': True},
        {'in': 'Will', 'out': True},
        {'in': 'Win', 'out': True},
        {'in': 'Wis', 'out': True},
        {'in': 'Withdraw', 'out': True},
        {'in': 'Withhold', 'out': True},
        {'in': 'Withstand', 'out': True},
        {'in': 'Would', 'out': True},
        {'in': 'Wring', 'out': True},
        {'in': 'abide', 'out': True},
        {'in': 'ache', 'out': True},
        {'in': 'arc', 'out': True},
        {'in': 'arise', 'out': True},
        {'in': 'ask', 'out': True},
        {'in': 'avalanche', 'out': True},
        {'in': 'awake', 'out': True},
        {'in': 'be', 'out': True},
        {'in': 'beat', 'out': True},
        {'in': 'become', 'out': True},
        {'in': 'beget', 'out': True},
        {'in': 'begin', 'out': True},
        {'in': 'behold', 'out': True},
        {'in': 'bellyache', 'out': True},
        {'in': 'bend', 'out': True},
        {'in': 'bet', 'out': True},
        {'in': 'bias', 'out': True},
        {'in': 'bite', 'out': True},
        {'in': 'bleed', 'out': True},
        {'in': 'blitz', 'out': True},
        {'in': 'blow', 'out': True},
        {'in': 'break', 'out': True},
        {'in': 'bring', 'out': True},
        {'in': 'build', 'out': True},
        {'in': 'burn', 'out': True},
        {'in': 'burst', 'out': True},
        {'in': 'bus', 'out': True},
        {'in': 'bust', 'out': True},
        {'in': 'cache', 'out': True},
        {'in': 'caddie', 'out': True},
        {'in': 'can', 'out': True},
        {'in': 'canvas', 'out': True},
        {'in': 'catch', 'out': True},
        {'in': 'caucus', 'out': True},
        {'in': 'change', 'out': True},
        {'in': 'choose', 'out': True},
        {'in': 'chorus', 'out': True},
        {'in': 'clap', 'out': True},
        {'in': 'cling', 'out': True},
        {'in': 'come', 'out': True},
        {'in': 'continue', 'out': True},
        {'in': 'cost', 'out': True},
        {'in': 'could', 'out': True},
        {'in': 'creche', 'out': True},
        {'in': 'creep', 'out': True},
        {'in': 'dare', 'out': True},
        {'in': 'deal', 'out': True},
        {'in': 'die', 'out': True},
        {'in': 'dig', 'out': True},
        {'in': 'dis', 'out': True},
        {'in': 'dive', 'out': True},
        {'in': 'do', 'out': True},
        {'in': 'douche', 'out': True},
        {'in': 'drag', 'out': True},
        {'in': 'dream', 'out': True},
        {'in': 'drink', 'out': True},
        {'in': 'drive', 'out': True},
        {'in': 'dwell', 'out': True},
        {'in': 'eat', 'out': True},
        {'in': 'expect', 'out': True},
        {'in': 'fall', 'out': True},
        {'in': 'feel', 'out': True},
        {'in': 'fight', 'out': True},
        {'in': 'find', 'out': True},
        {'in': 'flee', 'out': True},
        {'in': 'fling', 'out': True},
        {'in': 'fly', 'out': True},
        {'in': 'focus', 'out': True},
        {'in': 'follow', 'out': True},
        {'in': 'forbid', 'out': True},
        {'in': 'foresee', 'out': True},
        {'in': 'foretell', 'out': True},
        {'in': 'forget', 'out': True},
        {'in': 'forgive', 'out': True},
        {'in': 'forsake', 'out': True},
        {'in': 'gas', 'out': True},
        {'in': 'get', 'out': True},
        {'in': 'gild', 'out': True},
        {'in': 'give', 'out': True},
        {'in': 'go', 'out': True},
        {'in': 'grind', 'out': True},
        {'in': 'happen', 'out': True},
        {'in': 'have', 'out': True},
        {'in': 'help', 'out': True},
        {'in': 'hew', 'out': True},
        {'in': 'hie', 'out': True},
        {'in': 'hit', 'out': True},
        {'in': 'hocus', 'out': True},
        {'in': 'hold', 'out': True},
        {'in': 'hurt', 'out': True},
        {'in': 'inlay', 'out': True},
        {'in': 'insist', 'out': True},
        {'in': 'interlay', 'out': True},
        {'in': 'iris', 'out': True},
        {'in': 'keep', 'out': True},
        {'in': 'kill', 'out': True},
        {'in': 'kneel', 'out': True},
        {'in': 'knit', 'out': True},
        {'in': 'know', 'out': True},
        {'in': 'lay', 'out': True},
        {'in': 'lead', 'out': True},
        {'in': 'lean', 'out': True},
        {'in': 'leap', 'out': True},
        {'in': 'learn', 'out': True},
        {'in': 'leave', 'out': True},
        {'in': 'let', 'out': True},
        {'in': 'lie', 'out': True},
        {'in': 'like', 'out': True},
        {'in': 'live', 'out': True},
        {'in': 'look', 'out': True},
        {'in': 'lose', 'out': True},
        {'in': 'love', 'out': True},
        {'in': 'may', 'out': True},
        {'in': 'mean', 'out': True},
        {'in': 'meet', 'out': True},
        {'in': 'menu', 'out': True},
        {'in': 'might', 'out': True},
        {'in': 'mislead', 'out': True},
        {'in': 'mistake', 'out': True},
        {'in': 'misunderstand', 'out': True},
        {'in': 'move', 'out': True},
        {'in': 'must', 'out': True},
        {'in': 'need', 'out': True},
        {'in': 'niche', 'out': True},
        {'in': 'ought', 'out': True},
        {'in': 'outvie', 'out': True},
        {'in': 'overdraw', 'out': True},
        {'in': 'overhear', 'out': True},
        {'in': 'overtake', 'out': True},
        {'in': 'preset', 'out': True},
        {'in': 'prove', 'out': True},
        {'in': 'provide', 'out': True},
        {'in': 'psyche', 'out': True},
        {'in': 'put', 'out': True},
        {'in': 'quit', 'out': True},
        {'in': 'quiz', 'out': True},
        {'in': 'reach', 'out': True},
        {'in': 'remain', 'out': True},
        {'in': 'remember', 'out': True},
        {'in': 'rend', 'out': True},
        {'in': 'rent', 'out': True},
        {'in': 'rid', 'out': True},
        {'in': 'ring', 'out': True},
        {'in': 'rise', 'out': True},
        {'in': 'rive', 'out': True},
        {'in': 'saw', 'out': True},
        {'in': 'seek', 'out': True},
        {'in': 'seem', 'out': True},
        {'in': 'shake', 'out': True},
        {'in': 'shall', 'out': True},
        {'in': 'shave', 'out': True},
        {'in': 'shed', 'out': True},
        {'in': 'shit', 'out': True},
        {'in': 'shoe', 'out': True},
        {'in': 'should', 'out': True},
        {'in': 'show', 'out': True},
        {'in': 'shrink', 'out': True},
        {'in': 'sing', 'out': True},
        {'in': 'sink', 'out': True},
        {'in': 'sit', 'out': True},
        {'in': 'ski', 'out': True},
        {'in': 'slay', 'out': True},
        {'in': 'slide', 'out': True},
        {'in': 'slink', 'out': True},
        {'in': 'slit', 'out': True},
        {'in': 'smell', 'out': True},
        {'in': 'smite', 'out': True},
        {'in': 'sneak', 'out': True},
        {'in': 'sow', 'out': True},
        {'in': 'speak', 'out': True},
        {'in': 'speed', 'out': True},
        {'in': 'spend', 'out': True},
        {'in': 'spit', 'out': True},
        {'in': 'spoil', 'out': True},
        {'in': 'spring', 'out': True},
        {'in': 'stand', 'out': True},
        {'in': 'stave', 'out': True},
        {'in': 'stay', 'out': True},
        {'in': 'steal', 'out': True},
        {'in': 'sting', 'out': True},
        {'in': 'stink', 'out': True},
        {'in': 'stop', 'out': True},
        {'in': 'strew', 'out': True},
        {'in': 'stride', 'out': True},
        {'in': 'strip', 'out': True},
        {'in': 'strive', 'out': True},
        {'in': 'sublet', 'out': True},
        {'in': 'sunburn', 'out': True},
        {'in': 'swear', 'out': True},
        {'in': 'sweat', 'out': True},
        {'in': 'sweep', 'out': True},
        {'in': 'swell', 'out': True},
        {'in': 'swim', 'out': True},
        {'in': 'swing', 'out': True},
        {'in': 'talk', 'out': True},
        {'in': 'tear', 'out': True},
        {'in': 'thrive', 'out': True},
        {'in': 'thrust', 'out': True},
        {'in': 'tread', 'out': True},
        {'in': 'undergo', 'out': True},
        {'in': 'underlie', 'out': True},
        {'in': 'understand', 'out': True},
        {'in': 'undertake', 'out': True},
        {'in': 'upset', 'out': True},
        {'in': 'vex', 'out': True},
        {'in': 'vie', 'out': True},
        {'in': 'wait', 'out': True},
        {'in': 'wake', 'out': True},
        {'in': 'walk', 'out': True},
        {'in': 'want', 'out': True},
        {'in': 'watch', 'out': True},
        {'in': 'wear', 'out': True},
        {'in': 'weep', 'out': True},
        {'in': 'wend', 'out': True},
        {'in': 'were', 'out': True},
        {'in': 'will', 'out': True},
        {'in': 'win', 'out': True},
        {'in': 'wis', 'out': True},
        {'in': 'withdraw', 'out': True},
        {'in': 'withhold', 'out': True},
        {'in': 'withstand', 'out': True},
        {'in': 'would', 'out': True},
        {'in': 'wring', 'out': True},
    ]

    def test_verb_is_plural(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {**test_case, **{
                    "desc": f"is_plural({repr(test_case['in'])}) => {repr(test_case['out'])}",
                    "kwargs": {}
                }}
                self.assertEqual(Verb(test_case["in"]).is_plural(**test_case["kwargs"]), test_case["out"], test_case["desc"])


if __name__ == "__main__":
    unittest.main()
