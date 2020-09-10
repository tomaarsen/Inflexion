
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
## NOTE: This module was autogenerated. ##
## Contains no user-servicable parts!!! ##
##########################################

# Temporary imports for hack, will be reworked once this becomes a package!!!
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..')) 
# End of hack

import unittest

from verb_output import convert_to_plural

class TestVerbToPlural(unittest.TestCase):
    # test_args has the format [{
    #    "in":     ..., # (required)
    #    "out":    ..., # (required)
    #    "desc":   ..., # (optional) 
    #    "kwargs": ...  # (optional)
    # }, ...
    # ]
    test_args = [
        {'in': 'is', 'out': 'are'},
        {'in': 'are', 'out': 'are'},
        {'in': 'am', 'out': 'are'},
        {'in': 'was', 'out': 'were'},
        {'in': 'can', 'out': 'can'},
        {'in': 'could', 'out': 'could'},
        {'in': 'may', 'out': 'may'},
        {'in': 'might', 'out': 'might'},
        {'in': 'must', 'out': 'must'},
        {'in': 'ought', 'out': 'ought'},
        {'in': 'will', 'out': 'will'},
        {'in': 'shall', 'out': 'shall'},
        {'in': 'should', 'out': 'should'},
        {'in': 'would', 'out': 'would'},
        {'in': 'aches', 'out': 'ache'},
        {'in': 'arises', 'out': 'arise'},
        {'in': 'asks', 'out': 'ask'},
        {'in': 'avalanches', 'out': 'avalanche'},
        {'in': 'awakes', 'out': 'awake'},
        {'in': 'beats', 'out': 'beat'},
        {'in': 'becomes', 'out': 'become'},
        {'in': 'begets', 'out': 'beget'},
        {'in': 'begins', 'out': 'begin'},
        {'in': 'beholds', 'out': 'behold'},
        {'in': 'bellyaches', 'out': 'bellyache'},
        {'in': 'bends', 'out': 'bend'},
        {'in': 'bets', 'out': 'bet'},
        {'in': 'binds', 'out': 'bind'},
        {'in': 'bites', 'out': 'bite'},
        {'in': 'blitzes', 'out': 'blitz'},
        {'in': 'bleeds', 'out': 'bleed'},
        {'in': 'blows', 'out': 'blow'},
        {'in': 'breaks', 'out': 'break'},
        {'in': 'breeds', 'out': 'breed'},
        {'in': 'brings', 'out': 'bring'},
        {'in': 'builds', 'out': 'build'},
        {'in': 'burns', 'out': 'burn'},
        {'in': 'bursts', 'out': 'burst'},
        {'in': 'busts', 'out': 'bust'},
        {'in': 'caches', 'out': 'cache'},
        {'in': 'catches', 'out': 'catch'},
        {'in': 'chooses', 'out': 'choose'},
        {'in': 'clings', 'out': 'cling'},
        {'in': 'comes', 'out': 'come'},
        {'in': 'costs', 'out': 'cost'},
        {'in': 'creches', 'out': 'creche'},
        {'in': 'creeps', 'out': 'creep'},
        {'in': 'deals', 'out': 'deal'},
        {'in': 'digs', 'out': 'dig'},
        {'in': 'dives', 'out': 'dive'},
        {'in': 'douches', 'out': 'douche'},
        {'in': 'drags', 'out': 'drag'},
        {'in': 'drinks', 'out': 'drink'},
        {'in': 'drives', 'out': 'drive'},
        {'in': 'dwells', 'out': 'dwell'},
        {'in': 'eats', 'out': 'eat'},
        {'in': 'falls', 'out': 'fall'},
        {'in': 'feels', 'out': 'feel'},
        {'in': 'fights', 'out': 'fight'},
        {'in': 'finds', 'out': 'find'},
        {'in': 'flees', 'out': 'flee'},
        {'in': 'flies', 'out': 'fly'},
        {'in': 'flings', 'out': 'fling'},
        {'in': 'forbids', 'out': 'forbid'},
        {'in': 'foresees', 'out': 'foresee'},
        {'in': 'foretells', 'out': 'foretell'},
        {'in': 'forgets', 'out': 'forget'},
        {'in': 'forgives', 'out': 'forgive'},
        {'in': 'forsakes', 'out': 'forsake'},
        {'in': 'gets', 'out': 'get'},
        {'in': 'gilds', 'out': 'gild'},
        {'in': 'gives', 'out': 'give'},
        {'in': 'goes', 'out': 'go'},
        {'in': 'grinds', 'out': 'grind'},
        {'in': 'has', 'out': 'have'},
        {'in': 'hews', 'out': 'hew'},
        {'in': 'hits', 'out': 'hit'},
        {'in': 'holds', 'out': 'hold'},
        {'in': 'hurts', 'out': 'hurt'},
        {'in': 'inlays', 'out': 'inlay'},
        {'in': 'insists', 'out': 'insist'},
        {'in': 'interlays', 'out': 'interlay'},
        {'in': 'irises', 'out': 'iris'},
        {'in': 'keeps', 'out': 'keep'},
        {'in': 'kneels', 'out': 'kneel'},
        {'in': 'knows', 'out': 'know'},
        {'in': 'lays', 'out': 'lay'},
        {'in': 'leads', 'out': 'lead'},
        {'in': 'leans', 'out': 'lean'},
        {'in': 'leaps', 'out': 'leap'},
        {'in': 'leaves', 'out': 'leave'},
        {'in': 'lies', 'out': 'lie'},
        {'in': 'loses', 'out': 'lose'},
        {'in': 'means', 'out': 'mean'},
        {'in': 'meets', 'out': 'meet'},
        {'in': 'menus', 'out': 'menu'},
        {'in': 'misleads', 'out': 'mislead'},
        {'in': 'mistakes', 'out': 'mistake'},
        {'in': 'moves', 'out': 'move'},
        {'in': 'niches', 'out': 'niche'},
        {'in': 'overdraws', 'out': 'overdraw'},
        {'in': 'overhears', 'out': 'overhear'},
        {'in': 'overtakes', 'out': 'overtake'},
        {'in': 'presets', 'out': 'preset'},
        {'in': 'proves', 'out': 'prove'},
        {'in': 'psyches', 'out': 'psyche'},
        {'in': 'puts', 'out': 'put'},
        {'in': 'quits', 'out': 'quit'},
        {'in': 'quizzes', 'out': 'quiz'},
        {'in': 'rends', 'out': 'rend'},
        {'in': 'rides', 'out': 'ride'},
        {'in': 'rids', 'out': 'rid'},
        {'in': 'rings', 'out': 'ring'},
        {'in': 'rises', 'out': 'rise'},
        {'in': 'rives', 'out': 'rive'},
        {'in': 'runs', 'out': 'run'},
        {'in': 'saws', 'out': 'saw'},
        {'in': 'seeks', 'out': 'seek'},
        {'in': 'shakes', 'out': 'shake'},
        {'in': 'shaves', 'out': 'shave'},
        {'in': 'sheds', 'out': 'shed'},
        {'in': 'shits', 'out': 'shit'},
        {'in': 'shoes', 'out': 'shoe'},
        {'in': 'shows', 'out': 'show'},
        {'in': 'shrinks', 'out': 'shrink'},
        {'in': 'sings', 'out': 'sing'},
        {'in': 'sinks', 'out': 'sink'},
        {'in': 'sits', 'out': 'sit'},
        {'in': 'slays', 'out': 'slay'},
        {'in': 'slides', 'out': 'slide'},
        {'in': 'slinks', 'out': 'slink'},
        {'in': 'slits', 'out': 'slit'},
        {'in': 'smells', 'out': 'smell'},
        {'in': 'smites', 'out': 'smite'},
        {'in': 'sows', 'out': 'sow'},
        {'in': 'speaks', 'out': 'speak'},
        {'in': 'speeds', 'out': 'speed'},
        {'in': 'spends', 'out': 'spend'},
        {'in': 'spits', 'out': 'spit'},
        {'in': 'spoils', 'out': 'spoil'},
        {'in': 'springs', 'out': 'spring'},
        {'in': 'stands', 'out': 'stand'},
        {'in': 'staves', 'out': 'stave'},
        {'in': 'steals', 'out': 'steal'},
        {'in': 'stings', 'out': 'sting'},
        {'in': 'stinks', 'out': 'stink'},
        {'in': 'strews', 'out': 'strew'},
        {'in': 'strides', 'out': 'stride'},
        {'in': 'strives', 'out': 'strive'},
        {'in': 'sublets', 'out': 'sublet'},
        {'in': 'swears', 'out': 'swear'},
        {'in': 'sweats', 'out': 'sweat'},
        {'in': 'sweeps', 'out': 'sweep'},
        {'in': 'swells', 'out': 'swell'},
        {'in': 'swims', 'out': 'swim'},
        {'in': 'swings', 'out': 'swing'},
        {'in': 'tears', 'out': 'tear'},
        {'in': 'thrusts', 'out': 'thrust'},
        {'in': 'treads', 'out': 'tread'},
        {'in': 'undergoes', 'out': 'undergo'},
        {'in': 'understands', 'out': 'understand'},
        {'in': 'undertakes', 'out': 'undertake'},
        {'in': 'upsets', 'out': 'upset'},
        {'in': 'wakes', 'out': 'wake'},
        {'in': 'wears', 'out': 'wear'},
        {'in': 'weeps', 'out': 'weep'},
        {'in': 'wends', 'out': 'wend'},
        {'in': 'wins', 'out': 'win'},
        {'in': 'withdraws', 'out': 'withdraw'},
        {'in': 'withholds', 'out': 'withhold'},
        {'in': 'withstands', 'out': 'withstand'},
        {'in': 'wrings', 'out': 'wring'},
        {'in': 'abides', 'out': 'abide'},
        {'in': 'changes', 'out': 'change'},
        {'in': 'claps', 'out': 'clap'},
        {'in': 'continues', 'out': 'continue'},
        {'in': 'dares', 'out': 'dare'},
        {'in': 'dies', 'out': 'die'},
        {'in': 'dreams', 'out': 'dream'},
        {'in': 'expects', 'out': 'expect'},
        {'in': 'follows', 'out': 'follow'},
        {'in': 'happens', 'out': 'happen'},
        {'in': 'helps', 'out': 'help'},
        {'in': 'kills', 'out': 'kill'},
        {'in': 'knits', 'out': 'knit'},
        {'in': 'learns', 'out': 'learn'},
        {'in': 'likes', 'out': 'like'},
        {'in': 'lives', 'out': 'live'},
        {'in': 'looks', 'out': 'look'},
        {'in': 'loves', 'out': 'love'},
        {'in': 'misunderstands', 'out': 'misunderstand'},
        {'in': 'needs', 'out': 'need'},
        {'in': 'provides', 'out': 'provide'},
        {'in': 'reaches', 'out': 'reach'},
        {'in': 'remains', 'out': 'remain'},
        {'in': 'remembers', 'out': 'remember'},
        {'in': 'seems', 'out': 'seem'},
        {'in': 'skis', 'out': 'ski'},
        {'in': 'sneaks', 'out': 'sneak'},
        {'in': 'stays', 'out': 'stay'},
        {'in': 'stops', 'out': 'stop'},
        {'in': 'strips', 'out': 'strip'},
        {'in': 'sunburns', 'out': 'sunburn'},
        {'in': 'talks', 'out': 'talk'},
        {'in': 'thrives', 'out': 'thrive'},
        {'in': 'vexes', 'out': 'vex'},
        {'in': 'waits', 'out': 'wait'},
        {'in': 'walks', 'out': 'walk'},
        {'in': 'wants', 'out': 'want'},
        {'in': 'watches', 'out': 'watch'},
        {'in': 's', 'out': ''},
    ]

    def test_convert_to_plural(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {**test_case, **{
                    "desc": f"convert_to_plural({repr(test_case['in'])}) => {repr(test_case['out'])}",
                    "kwargs": dict()
                }}
                self.assertEqual(convert_to_plural(test_case["in"], **test_case["kwargs"]), test_case["out"], test_case["desc"])

if __name__ == "__main__":
    unittest.main()
