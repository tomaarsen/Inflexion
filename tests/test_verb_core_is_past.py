
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
## NOTE: This module was autogenerated. ##
## Contains no user-servicable parts!!! ##
##########################################

import unittest

from inflexion import Verb


class TestVerbIsPast(unittest.TestCase):
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
        {'in': 'abided', 'out': True},
        {'in': 'ached', 'out': True},
        {'in': 'arced', 'out': True},
        {'in': 'arose', 'out': True},
        {'in': 'asked', 'out': True},
        {'in': 'ate', 'out': True},
        {'in': 'avalanched', 'out': True},
        {'in': 'awoke', 'out': True},
        {'in': 'beat', 'out': True},
        {'in': 'became', 'out': True},
        {'in': 'began', 'out': True},
        {'in': 'begot', 'out': True},
        {'in': 'beheld', 'out': True},
        {'in': 'bellyached', 'out': True},
        {'in': 'bent', 'out': True},
        {'in': 'bet', 'out': True},
        {'in': 'biased', 'out': True},
        {'in': 'bit', 'out': True},
        {'in': 'bled', 'out': True},
        {'in': 'blew', 'out': True},
        {'in': 'blitzed', 'out': True},
        {'in': 'broke', 'out': True},
        {'in': 'brought', 'out': True},
        {'in': 'built', 'out': True},
        {'in': 'burnt', 'out': True},
        {'in': 'burst', 'out': True},
        {'in': 'bused', 'out': True},
        {'in': 'bust', 'out': True},
        {'in': 'cached', 'out': True},
        {'in': 'caddied', 'out': True},
        {'in': 'came', 'out': True},
        {'in': 'canvased', 'out': True},
        {'in': 'caucused', 'out': True},
        {'in': 'caught', 'out': True},
        {'in': 'changed', 'out': True},
        {'in': 'chorused', 'out': True},
        {'in': 'chose', 'out': True},
        {'in': 'clapped', 'out': True},
        {'in': 'clung', 'out': True},
        {'in': 'continued', 'out': True},
        {'in': 'cost', 'out': True},
        {'in': 'could', 'out': True},
        {'in': 'creched', 'out': True},
        {'in': 'crept', 'out': True},
        {'in': 'dared', 'out': True},
        {'in': 'dealt', 'out': True},
        {'in': 'did', 'out': True},
        {'in': 'died', 'out': True},
        {'in': 'dissed', 'out': True},
        {'in': 'dived', 'out': True},
        {'in': 'douched', 'out': True},
        {'in': 'dragged', 'out': True},
        {'in': 'drank', 'out': True},
        {'in': 'dreamed', 'out': True},
        {'in': 'drove', 'out': True},
        {'in': 'dug', 'out': True},
        {'in': 'dwelt', 'out': True},
        {'in': 'expected', 'out': True},
        {'in': 'fell', 'out': True},
        {'in': 'felt', 'out': True},
        {'in': 'fled', 'out': True},
        {'in': 'flew', 'out': True},
        {'in': 'flung', 'out': True},
        {'in': 'focused', 'out': True},
        {'in': 'followed', 'out': True},
        {'in': 'forbade', 'out': True},
        {'in': 'foresaw', 'out': True},
        {'in': 'foretold', 'out': True},
        {'in': 'forgave', 'out': True},
        {'in': 'forgot', 'out': True},
        {'in': 'forsook', 'out': True},
        {'in': 'fought', 'out': True},
        {'in': 'found', 'out': True},
        {'in': 'gassed', 'out': True},
        {'in': 'gave', 'out': True},
        {'in': 'gilded', 'out': True},
        {'in': 'got', 'out': True},
        {'in': 'ground', 'out': True},
        {'in': 'had', 'out': True},
        {'in': 'happened', 'out': True},
        {'in': 'held', 'out': True},
        {'in': 'helped', 'out': True},
        {'in': 'hewed', 'out': True},
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
        {'in': 'knew', 'out': True},
        {'in': 'knitted', 'out': True},
        {'in': 'laid', 'out': True},
        {'in': 'lay', 'out': True},
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
        {'in': 'might', 'out': True},
        {'in': 'misled', 'out': True},
        {'in': 'mistook', 'out': True},
        {'in': 'misunderstood', 'out': True},
        {'in': 'moved', 'out': True},
        {'in': 'needed', 'out': True},
        {'in': 'niched', 'out': True},
        {'in': 'outvied', 'out': True},
        {'in': 'overdrew', 'out': True},
        {'in': 'overheard', 'out': True},
        {'in': 'overtook', 'out': True},
        {'in': 'preset', 'out': True},
        {'in': 'proved', 'out': True},
        {'in': 'provided', 'out': True},
        {'in': 'psyched', 'out': True},
        {'in': 'put', 'out': True},
        {'in': 'quit', 'out': True},
        {'in': 'quizzed', 'out': True},
        {'in': 'rang', 'out': True},
        {'in': 'reached', 'out': True},
        {'in': 'remained', 'out': True},
        {'in': 'remembered', 'out': True},
        {'in': 'rent', 'out': True},
        {'in': 'rented', 'out': True},
        {'in': 'rid', 'out': True},
        {'in': 'rived', 'out': True},
        {'in': 'rose', 'out': True},
        {'in': 'sang', 'out': True},
        {'in': 'sank', 'out': True},
        {'in': 'sat', 'out': True},
        {'in': 'sawed', 'out': True},
        {'in': 'seemed', 'out': True},
        {'in': 'shat', 'out': True},
        {'in': 'shaved', 'out': True},
        {'in': 'shed', 'out': True},
        {'in': 'shod', 'out': True},
        {'in': 'shook', 'out': True},
        {'in': 'should', 'out': True},
        {'in': 'showed', 'out': True},
        {'in': 'shrank', 'out': True},
        {'in': 'skied', 'out': True},
        {'in': 'slew', 'out': True},
        {'in': 'slid', 'out': True},
        {'in': 'slit', 'out': True},
        {'in': 'slunk', 'out': True},
        {'in': 'smelled', 'out': True},
        {'in': 'smote', 'out': True},
        {'in': 'sneaked', 'out': True},
        {'in': 'sought', 'out': True},
        {'in': 'sowed', 'out': True},
        {'in': 'spat', 'out': True},
        {'in': 'sped', 'out': True},
        {'in': 'spent', 'out': True},
        {'in': 'spoilt', 'out': True},
        {'in': 'spoke', 'out': True},
        {'in': 'sprang', 'out': True},
        {'in': 'stank', 'out': True},
        {'in': 'staved', 'out': True},
        {'in': 'stayed', 'out': True},
        {'in': 'stole', 'out': True},
        {'in': 'stood', 'out': True},
        {'in': 'stopped', 'out': True},
        {'in': 'strewed', 'out': True},
        {'in': 'stripped', 'out': True},
        {'in': 'strode', 'out': True},
        {'in': 'strove', 'out': True},
        {'in': 'stung', 'out': True},
        {'in': 'sublet', 'out': True},
        {'in': 'sunburned', 'out': True},
        {'in': 'swam', 'out': True},
        {'in': 'sweat', 'out': True},
        {'in': 'swelled', 'out': True},
        {'in': 'swept', 'out': True},
        {'in': 'swore', 'out': True},
        {'in': 'swung', 'out': True},
        {'in': 'talked', 'out': True},
        {'in': 'thrived', 'out': True},
        {'in': 'thrust', 'out': True},
        {'in': 'tore', 'out': True},
        {'in': 'trod', 'out': True},
        {'in': 'underlay', 'out': True},
        {'in': 'understood', 'out': True},
        {'in': 'undertook', 'out': True},
        {'in': 'underwent', 'out': True},
        {'in': 'upset', 'out': True},
        {'in': 'vexed', 'out': True},
        {'in': 'vied', 'out': True},
        {'in': 'waited', 'out': True},
        {'in': 'walked', 'out': True},
        {'in': 'wanted', 'out': True},
        {'in': 'was', 'out': True},
        {'in': 'watched', 'out': True},
        {'in': 'wended', 'out': True},
        {'in': 'went', 'out': True},
        {'in': 'wept', 'out': True},
        {'in': 'were', 'out': True},
        {'in': 'wised', 'out': True},
        {'in': 'withdrew', 'out': True},
        {'in': 'withheld', 'out': True},
        {'in': 'withstood', 'out': True},
        {'in': 'woke', 'out': True},
        {'in': 'won', 'out': True},
        {'in': 'wore', 'out': True},
        {'in': 'would', 'out': True},
        {'in': 'wrung', 'out': True},
    ]

    def test_verb_is_past(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {**test_case, **{
                    "desc": f"is_past({repr(test_case['in'])}) => {repr(test_case['out'])}",
                    "kwargs": dict()
                }}
                self.assertEqual(Verb(test_case["in"]).is_past(**test_case["kwargs"]), test_case["out"], test_case["desc"])


if __name__ == "__main__":
    unittest.main()
