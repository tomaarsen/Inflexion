
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
## NOTE: This module was autogenerated. ##
## Contains no user-servicable parts!!! ##
##########################################

import unittest

from inflex import Verb


class TestVerbIsPastPart(unittest.TestCase):
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
        {'in': 'Abided', 'out': True},
        {'in': 'Ached', 'out': True},
        {'in': 'Arced', 'out': True},
        {'in': 'Arisen', 'out': True},
        {'in': 'Asked', 'out': True},
        {'in': 'Avalanched', 'out': True},
        {'in': 'Awoken', 'out': True},
        {'in': 'Beaten', 'out': True},
        {'in': 'Become', 'out': True},
        {'in': 'Been', 'out': True},
        {'in': 'Begotten', 'out': True},
        {'in': 'Begun', 'out': True},
        {'in': 'Beheld', 'out': True},
        {'in': 'Bellyached', 'out': True},
        {'in': 'Bent', 'out': True},
        {'in': 'Bet', 'out': True},
        {'in': 'Biased', 'out': True},
        {'in': 'Bitten', 'out': True},
        {'in': 'Bled', 'out': True},
        {'in': 'Blitzed', 'out': True},
        {'in': 'Blown', 'out': True},
        {'in': 'Broken', 'out': True},
        {'in': 'Brought', 'out': True},
        {'in': 'Built', 'out': True},
        {'in': 'Burnt', 'out': True},
        {'in': 'Burst', 'out': True},
        {'in': 'Bused', 'out': True},
        {'in': 'Bust', 'out': True},
        {'in': 'Cached', 'out': True},
        {'in': 'Caddied', 'out': True},
        {'in': 'Canvased', 'out': True},
        {'in': 'Caucused', 'out': True},
        {'in': 'Caught', 'out': True},
        {'in': 'Changed', 'out': True},
        {'in': 'Chorused', 'out': True},
        {'in': 'Chosen', 'out': True},
        {'in': 'Clapped', 'out': True},
        {'in': 'Clung', 'out': True},
        {'in': 'Come', 'out': True},
        {'in': 'Continued', 'out': True},
        {'in': 'Cost', 'out': True},
        {'in': 'Creched', 'out': True},
        {'in': 'Crept', 'out': True},
        {'in': 'Dared', 'out': True},
        {'in': 'Dealt', 'out': True},
        {'in': 'Died', 'out': True},
        {'in': 'Dissed', 'out': True},
        {'in': 'Dived', 'out': True},
        {'in': 'Done', 'out': True},
        {'in': 'Douched', 'out': True},
        {'in': 'Dragged', 'out': True},
        {'in': 'Dreamed', 'out': True},
        {'in': 'Driven', 'out': True},
        {'in': 'Drunk', 'out': True},
        {'in': 'Dug', 'out': True},
        {'in': 'Dwelt', 'out': True},
        {'in': 'Eaten', 'out': True},
        {'in': 'Expected', 'out': True},
        {'in': 'Fallen', 'out': True},
        {'in': 'Felt', 'out': True},
        {'in': 'Fled', 'out': True},
        {'in': 'Flown', 'out': True},
        {'in': 'Flung', 'out': True},
        {'in': 'Focused', 'out': True},
        {'in': 'Followed', 'out': True},
        {'in': 'Forbidden', 'out': True},
        {'in': 'Foreseen', 'out': True},
        {'in': 'Foretold', 'out': True},
        {'in': 'Forgiven', 'out': True},
        {'in': 'Forgotten', 'out': True},
        {'in': 'Forsaken', 'out': True},
        {'in': 'Fought', 'out': True},
        {'in': 'Found', 'out': True},
        {'in': 'Gassed', 'out': True},
        {'in': 'Gilded', 'out': True},
        {'in': 'Given', 'out': True},
        {'in': 'Gone', 'out': True},
        {'in': 'Gotten', 'out': True},
        {'in': 'Ground', 'out': True},
        {'in': 'Had', 'out': True},
        {'in': 'Happened', 'out': True},
        {'in': 'Held', 'out': True},
        {'in': 'Helped', 'out': True},
        {'in': 'Hewn', 'out': True},
        {'in': 'Hied', 'out': True},
        {'in': 'Hit', 'out': True},
        {'in': 'Hocused', 'out': True},
        {'in': 'Hurt', 'out': True},
        {'in': 'Inlaid', 'out': True},
        {'in': 'Insisted', 'out': True},
        {'in': 'Interlaid', 'out': True},
        {'in': 'Irised', 'out': True},
        {'in': 'Kept', 'out': True},
        {'in': 'Killed', 'out': True},
        {'in': 'Knelt', 'out': True},
        {'in': 'Knitted', 'out': True},
        {'in': 'Known', 'out': True},
        {'in': 'Laid', 'out': True},
        {'in': 'Lain', 'out': True},
        {'in': 'Leaned', 'out': True},
        {'in': 'Leapt', 'out': True},
        {'in': 'Learned', 'out': True},
        {'in': 'Led', 'out': True},
        {'in': 'Left', 'out': True},
        {'in': 'Let', 'out': True},
        {'in': 'Liked', 'out': True},
        {'in': 'Lived', 'out': True},
        {'in': 'Looked', 'out': True},
        {'in': 'Lost', 'out': True},
        {'in': 'Loved', 'out': True},
        {'in': 'Meant', 'out': True},
        {'in': 'Menued', 'out': True},
        {'in': 'Met', 'out': True},
        {'in': 'Misled', 'out': True},
        {'in': 'Mistaken', 'out': True},
        {'in': 'Misunderstood', 'out': True},
        {'in': 'Moved', 'out': True},
        {'in': 'Needed', 'out': True},
        {'in': 'Niched', 'out': True},
        {'in': 'Outvied', 'out': True},
        {'in': 'Overdrawn', 'out': True},
        {'in': 'Overheard', 'out': True},
        {'in': 'Overtaken', 'out': True},
        {'in': 'Preset', 'out': True},
        {'in': 'Proved', 'out': True},
        {'in': 'Proven', 'out': True},
        {'in': 'Provided', 'out': True},
        {'in': 'Psyched', 'out': True},
        {'in': 'Put', 'out': True},
        {'in': 'Quit', 'out': True},
        {'in': 'Quizzed', 'out': True},
        {'in': 'Reached', 'out': True},
        {'in': 'Remained', 'out': True},
        {'in': 'Remembered', 'out': True},
        {'in': 'Rent', 'out': True},
        {'in': 'Rented', 'out': True},
        {'in': 'Rid', 'out': True},
        {'in': 'Risen', 'out': True},
        {'in': 'Riven', 'out': True},
        {'in': 'Rung', 'out': True},
        {'in': 'Sat', 'out': True},
        {'in': 'Sawn', 'out': True},
        {'in': 'Seemed', 'out': True},
        {'in': 'Shaken', 'out': True},
        {'in': 'Shaved', 'out': True},
        {'in': 'Shed', 'out': True},
        {'in': 'Shitted', 'out': True},
        {'in': 'Shod', 'out': True},
        {'in': 'Shown', 'out': True},
        {'in': 'Shrunk', 'out': True},
        {'in': 'Skied', 'out': True},
        {'in': 'Slain', 'out': True},
        {'in': 'Slid', 'out': True},
        {'in': 'Slit', 'out': True},
        {'in': 'Slunk', 'out': True},
        {'in': 'Smelled', 'out': True},
        {'in': 'Smitten', 'out': True},
        {'in': 'Sneaked', 'out': True},
        {'in': 'Sought', 'out': True},
        {'in': 'Sown', 'out': True},
        {'in': 'Spat', 'out': True},
        {'in': 'Sped', 'out': True},
        {'in': 'Spent', 'out': True},
        {'in': 'Spoiled', 'out': True},
        {'in': 'Spoken', 'out': True},
        {'in': 'Sprung', 'out': True},
        {'in': 'Staved', 'out': True},
        {'in': 'Stayed', 'out': True},
        {'in': 'Stolen', 'out': True},
        {'in': 'Stood', 'out': True},
        {'in': 'Stopped', 'out': True},
        {'in': 'Strewn', 'out': True},
        {'in': 'Stripped', 'out': True},
        {'in': 'Strived', 'out': True},
        {'in': 'Strode', 'out': True},
        {'in': 'Stung', 'out': True},
        {'in': 'Stunk', 'out': True},
        {'in': 'Sublet', 'out': True},
        {'in': 'Sunburned', 'out': True},
        {'in': 'Sung', 'out': True},
        {'in': 'Sunk', 'out': True},
        {'in': 'Sweated', 'out': True},
        {'in': 'Swept', 'out': True},
        {'in': 'Swollen', 'out': True},
        {'in': 'Sworn', 'out': True},
        {'in': 'Swum', 'out': True},
        {'in': 'Swung', 'out': True},
        {'in': 'Talked', 'out': True},
        {'in': 'Thrived', 'out': True},
        {'in': 'Thrust', 'out': True},
        {'in': 'Torn', 'out': True},
        {'in': 'Trodden', 'out': True},
        {'in': 'Undergone', 'out': True},
        {'in': 'Underlain', 'out': True},
        {'in': 'Understood', 'out': True},
        {'in': 'Undertaken', 'out': True},
        {'in': 'Upset', 'out': True},
        {'in': 'Vexed', 'out': True},
        {'in': 'Vied', 'out': True},
        {'in': 'Waited', 'out': True},
        {'in': 'Walked', 'out': True},
        {'in': 'Wanted', 'out': True},
        {'in': 'Watched', 'out': True},
        {'in': 'Wended', 'out': True},
        {'in': 'Wept', 'out': True},
        {'in': 'Wised', 'out': True},
        {'in': 'Withdrawn', 'out': True},
        {'in': 'Withheld', 'out': True},
        {'in': 'Withstood', 'out': True},
        {'in': 'Woken', 'out': True},
        {'in': 'Won', 'out': True},
        {'in': 'Worn', 'out': True},
        {'in': 'Wrung', 'out': True},
        {'in': 'abided', 'out': True},
        {'in': 'ached', 'out': True},
        {'in': 'arced', 'out': True},
        {'in': 'arisen', 'out': True},
        {'in': 'asked', 'out': True},
        {'in': 'avalanched', 'out': True},
        {'in': 'awoken', 'out': True},
        {'in': 'beaten', 'out': True},
        {'in': 'become', 'out': True},
        {'in': 'been', 'out': True},
        {'in': 'begotten', 'out': True},
        {'in': 'begun', 'out': True},
        {'in': 'beheld', 'out': True},
        {'in': 'bellyached', 'out': True},
        {'in': 'bent', 'out': True},
        {'in': 'bet', 'out': True},
        {'in': 'biased', 'out': True},
        {'in': 'bitten', 'out': True},
        {'in': 'bled', 'out': True},
        {'in': 'blitzed', 'out': True},
        {'in': 'blown', 'out': True},
        {'in': 'broken', 'out': True},
        {'in': 'brought', 'out': True},
        {'in': 'built', 'out': True},
        {'in': 'burnt', 'out': True},
        {'in': 'burst', 'out': True},
        {'in': 'bused', 'out': True},
        {'in': 'bust', 'out': True},
        {'in': 'cached', 'out': True},
        {'in': 'caddied', 'out': True},
        {'in': 'canvased', 'out': True},
        {'in': 'caucused', 'out': True},
        {'in': 'caught', 'out': True},
        {'in': 'changed', 'out': True},
        {'in': 'chorused', 'out': True},
        {'in': 'chosen', 'out': True},
        {'in': 'clapped', 'out': True},
        {'in': 'clung', 'out': True},
        {'in': 'come', 'out': True},
        {'in': 'continued', 'out': True},
        {'in': 'cost', 'out': True},
        {'in': 'creched', 'out': True},
        {'in': 'crept', 'out': True},
        {'in': 'dared', 'out': True},
        {'in': 'dealt', 'out': True},
        {'in': 'died', 'out': True},
        {'in': 'dissed', 'out': True},
        {'in': 'dived', 'out': True},
        {'in': 'done', 'out': True},
        {'in': 'douched', 'out': True},
        {'in': 'dragged', 'out': True},
        {'in': 'dreamed', 'out': True},
        {'in': 'driven', 'out': True},
        {'in': 'drunk', 'out': True},
        {'in': 'dug', 'out': True},
        {'in': 'dwelt', 'out': True},
        {'in': 'eaten', 'out': True},
        {'in': 'expected', 'out': True},
        {'in': 'fallen', 'out': True},
        {'in': 'felt', 'out': True},
        {'in': 'fled', 'out': True},
        {'in': 'flown', 'out': True},
        {'in': 'flung', 'out': True},
        {'in': 'focused', 'out': True},
        {'in': 'followed', 'out': True},
        {'in': 'forbidden', 'out': True},
        {'in': 'foreseen', 'out': True},
        {'in': 'foretold', 'out': True},
        {'in': 'forgiven', 'out': True},
        {'in': 'forgotten', 'out': True},
        {'in': 'forsaken', 'out': True},
        {'in': 'fought', 'out': True},
        {'in': 'found', 'out': True},
        {'in': 'gassed', 'out': True},
        {'in': 'gilded', 'out': True},
        {'in': 'given', 'out': True},
        {'in': 'gone', 'out': True},
        {'in': 'gotten', 'out': True},
        {'in': 'ground', 'out': True},
        {'in': 'had', 'out': True},
        {'in': 'happened', 'out': True},
        {'in': 'held', 'out': True},
        {'in': 'helped', 'out': True},
        {'in': 'hewn', 'out': True},
        {'in': 'hied', 'out': True},
        {'in': 'hit', 'out': True},
        {'in': 'hocused', 'out': True},
        {'in': 'hurt', 'out': True},
        {'in': 'inlaid', 'out': True},
        {'in': 'insisted', 'out': True},
        {'in': 'interlaid', 'out': True},
        {'in': 'irised', 'out': True},
        {'in': 'kept', 'out': True},
        {'in': 'killed', 'out': True},
        {'in': 'knelt', 'out': True},
        {'in': 'knitted', 'out': True},
        {'in': 'known', 'out': True},
        {'in': 'laid', 'out': True},
        {'in': 'lain', 'out': True},
        {'in': 'leaned', 'out': True},
        {'in': 'leapt', 'out': True},
        {'in': 'learned', 'out': True},
        {'in': 'led', 'out': True},
        {'in': 'left', 'out': True},
        {'in': 'let', 'out': True},
        {'in': 'liked', 'out': True},
        {'in': 'lived', 'out': True},
        {'in': 'looked', 'out': True},
        {'in': 'lost', 'out': True},
        {'in': 'loved', 'out': True},
        {'in': 'meant', 'out': True},
        {'in': 'menued', 'out': True},
        {'in': 'met', 'out': True},
        {'in': 'misled', 'out': True},
        {'in': 'mistaken', 'out': True},
        {'in': 'misunderstood', 'out': True},
        {'in': 'moved', 'out': True},
        {'in': 'needed', 'out': True},
        {'in': 'niched', 'out': True},
        {'in': 'outvied', 'out': True},
        {'in': 'overdrawn', 'out': True},
        {'in': 'overheard', 'out': True},
        {'in': 'overtaken', 'out': True},
        {'in': 'preset', 'out': True},
        {'in': 'proved', 'out': True},
        {'in': 'proven', 'out': True},
        {'in': 'provided', 'out': True},
        {'in': 'psyched', 'out': True},
        {'in': 'put', 'out': True},
        {'in': 'quit', 'out': True},
        {'in': 'quizzed', 'out': True},
        {'in': 'reached', 'out': True},
        {'in': 'remained', 'out': True},
        {'in': 'remembered', 'out': True},
        {'in': 'rent', 'out': True},
        {'in': 'rented', 'out': True},
        {'in': 'rid', 'out': True},
        {'in': 'risen', 'out': True},
        {'in': 'riven', 'out': True},
        {'in': 'rung', 'out': True},
        {'in': 'sat', 'out': True},
        {'in': 'sawn', 'out': True},
        {'in': 'seemed', 'out': True},
        {'in': 'shaken', 'out': True},
        {'in': 'shaved', 'out': True},
        {'in': 'shed', 'out': True},
        {'in': 'shitted', 'out': True},
        {'in': 'shod', 'out': True},
        {'in': 'shown', 'out': True},
        {'in': 'shrunk', 'out': True},
        {'in': 'skied', 'out': True},
        {'in': 'slain', 'out': True},
        {'in': 'slid', 'out': True},
        {'in': 'slit', 'out': True},
        {'in': 'slunk', 'out': True},
        {'in': 'smelled', 'out': True},
        {'in': 'smitten', 'out': True},
        {'in': 'sneaked', 'out': True},
        {'in': 'sought', 'out': True},
        {'in': 'sown', 'out': True},
        {'in': 'spat', 'out': True},
        {'in': 'sped', 'out': True},
        {'in': 'spent', 'out': True},
        {'in': 'spoiled', 'out': True},
        {'in': 'spoken', 'out': True},
        {'in': 'sprung', 'out': True},
        {'in': 'staved', 'out': True},
        {'in': 'stayed', 'out': True},
        {'in': 'stolen', 'out': True},
        {'in': 'stood', 'out': True},
        {'in': 'stopped', 'out': True},
        {'in': 'strewn', 'out': True},
        {'in': 'stripped', 'out': True},
        {'in': 'strived', 'out': True},
        {'in': 'strode', 'out': True},
        {'in': 'stung', 'out': True},
        {'in': 'stunk', 'out': True},
        {'in': 'sublet', 'out': True},
        {'in': 'sunburned', 'out': True},
        {'in': 'sung', 'out': True},
        {'in': 'sunk', 'out': True},
        {'in': 'sweated', 'out': True},
        {'in': 'swept', 'out': True},
        {'in': 'swollen', 'out': True},
        {'in': 'sworn', 'out': True},
        {'in': 'swum', 'out': True},
        {'in': 'swung', 'out': True},
        {'in': 'talked', 'out': True},
        {'in': 'thrived', 'out': True},
        {'in': 'thrust', 'out': True},
        {'in': 'torn', 'out': True},
        {'in': 'trodden', 'out': True},
        {'in': 'undergone', 'out': True},
        {'in': 'underlain', 'out': True},
        {'in': 'understood', 'out': True},
        {'in': 'undertaken', 'out': True},
        {'in': 'upset', 'out': True},
        {'in': 'vexed', 'out': True},
        {'in': 'vied', 'out': True},
        {'in': 'waited', 'out': True},
        {'in': 'walked', 'out': True},
        {'in': 'wanted', 'out': True},
        {'in': 'watched', 'out': True},
        {'in': 'wended', 'out': True},
        {'in': 'wept', 'out': True},
        {'in': 'wised', 'out': True},
        {'in': 'withdrawn', 'out': True},
        {'in': 'withheld', 'out': True},
        {'in': 'withstood', 'out': True},
        {'in': 'woken', 'out': True},
        {'in': 'won', 'out': True},
        {'in': 'worn', 'out': True},
        {'in': 'wrung', 'out': True},
    ]

    def test_verb_is_past_part(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {**test_case, **{
                    "desc": f"is_past_part({repr(test_case['in'])}) => {repr(test_case['out'])}",
                    "kwargs": {}
                }}
                self.assertEqual(Verb(test_case["in"]).is_past_part(**test_case["kwargs"]), test_case["out"], test_case["desc"])


if __name__ == "__main__":
    unittest.main()
