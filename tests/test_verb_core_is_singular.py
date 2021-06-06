
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
## NOTE: This module was autogenerated. ##
## Contains no user-servicable parts!!! ##
##########################################

import unittest

from inflex import Verb


class TestVerbIsSingular(unittest.TestCase):
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
        {'in': 'Abides', 'out': True},
        {'in': 'Aches', 'out': True},
        {'in': 'Arcs', 'out': True},
        {'in': 'Arises', 'out': True},
        {'in': 'Asks', 'out': True},
        {'in': 'Avalanches', 'out': True},
        {'in': 'Awakes', 'out': True},
        {'in': 'Beats', 'out': True},
        {'in': 'Becomes', 'out': True},
        {'in': 'Begets', 'out': True},
        {'in': 'Begins', 'out': True},
        {'in': 'Beholds', 'out': True},
        {'in': 'Bellyaches', 'out': True},
        {'in': 'Bends', 'out': True},
        {'in': 'Bets', 'out': True},
        {'in': 'Biases', 'out': True},
        {'in': 'Bites', 'out': True},
        {'in': 'Bleeds', 'out': True},
        {'in': 'Blitzes', 'out': True},
        {'in': 'Blows', 'out': True},
        {'in': 'Breaks', 'out': True},
        {'in': 'Brings', 'out': True},
        {'in': 'Builds', 'out': True},
        {'in': 'Burns', 'out': True},
        {'in': 'Bursts', 'out': True},
        {'in': 'Buses', 'out': True},
        {'in': 'Busts', 'out': True},
        {'in': 'Caches', 'out': True},
        {'in': 'Caddies', 'out': True},
        {'in': 'Can', 'out': True},
        {'in': 'Canvases', 'out': True},
        {'in': 'Catches', 'out': True},
        {'in': 'Caucuses', 'out': True},
        {'in': 'Changes', 'out': True},
        {'in': 'Chooses', 'out': True},
        {'in': 'Choruses', 'out': True},
        {'in': 'Claps', 'out': True},
        {'in': 'Clings', 'out': True},
        {'in': 'Comes', 'out': True},
        {'in': 'Continues', 'out': True},
        {'in': 'Costs', 'out': True},
        {'in': 'Could', 'out': True},
        {'in': 'Creches', 'out': True},
        {'in': 'Creeps', 'out': True},
        {'in': 'Dares', 'out': True},
        {'in': 'Deals', 'out': True},
        {'in': 'Dies', 'out': True},
        {'in': 'Digs', 'out': True},
        {'in': 'Disses', 'out': True},
        {'in': 'Dives', 'out': True},
        {'in': 'Does', 'out': True},
        {'in': 'Douches', 'out': True},
        {'in': 'Drags', 'out': True},
        {'in': 'Dreams', 'out': True},
        {'in': 'Drinks', 'out': True},
        {'in': 'Drives', 'out': True},
        {'in': 'Dwells', 'out': True},
        {'in': 'Eats', 'out': True},
        {'in': 'Expects', 'out': True},
        {'in': 'Falls', 'out': True},
        {'in': 'Feels', 'out': True},
        {'in': 'Fights', 'out': True},
        {'in': 'Finds', 'out': True},
        {'in': 'Flees', 'out': True},
        {'in': 'Flies', 'out': True},
        {'in': 'Flings', 'out': True},
        {'in': 'Focuses', 'out': True},
        {'in': 'Follows', 'out': True},
        {'in': 'Forbids', 'out': True},
        {'in': 'Foresees', 'out': True},
        {'in': 'Foretells', 'out': True},
        {'in': 'Forgets', 'out': True},
        {'in': 'Forgives', 'out': True},
        {'in': 'Forsakes', 'out': True},
        {'in': 'Gases', 'out': True},
        {'in': 'Gets', 'out': True},
        {'in': 'Gilds', 'out': True},
        {'in': 'Gives', 'out': True},
        {'in': 'Goes', 'out': True},
        {'in': 'Grinds', 'out': True},
        {'in': 'Happens', 'out': True},
        {'in': 'Has', 'out': True},
        {'in': 'Helps', 'out': True},
        {'in': 'Hews', 'out': True},
        {'in': 'Hies', 'out': True},
        {'in': 'Hits', 'out': True},
        {'in': 'Hocuses', 'out': True},
        {'in': 'Holds', 'out': True},
        {'in': 'Hurts', 'out': True},
        {'in': 'Inlays', 'out': True},
        {'in': 'Insists', 'out': True},
        {'in': 'Interlays', 'out': True},
        {'in': 'Irises', 'out': True},
        {'in': 'Keeps', 'out': True},
        {'in': 'Kills', 'out': True},
        {'in': 'Kneels', 'out': True},
        {'in': 'Knits', 'out': True},
        {'in': 'Knows', 'out': True},
        {'in': 'Lays', 'out': True},
        {'in': 'Leads', 'out': True},
        {'in': 'Leans', 'out': True},
        {'in': 'Leaps', 'out': True},
        {'in': 'Learns', 'out': True},
        {'in': 'Leaves', 'out': True},
        {'in': 'Lets', 'out': True},
        {'in': 'Lies', 'out': True},
        {'in': 'Likes', 'out': True},
        {'in': 'Lives', 'out': True},
        {'in': 'Looks', 'out': True},
        {'in': 'Loses', 'out': True},
        {'in': 'Loves', 'out': True},
        {'in': 'May', 'out': True},
        {'in': 'Means', 'out': True},
        {'in': 'Meets', 'out': True},
        {'in': 'Menus', 'out': True},
        {'in': 'Might', 'out': True},
        {'in': 'Misleads', 'out': True},
        {'in': 'Mistakes', 'out': True},
        {'in': 'Misunderstands', 'out': True},
        {'in': 'Moves', 'out': True},
        {'in': 'Must', 'out': True},
        {'in': 'Needs', 'out': True},
        {'in': 'Niches', 'out': True},
        {'in': 'Ought', 'out': True},
        {'in': 'Outvies', 'out': True},
        {'in': 'Overdraws', 'out': True},
        {'in': 'Overhears', 'out': True},
        {'in': 'Overtakes', 'out': True},
        {'in': 'Presets', 'out': True},
        {'in': 'Proves', 'out': True},
        {'in': 'Provides', 'out': True},
        {'in': 'Psyches', 'out': True},
        {'in': 'Puts', 'out': True},
        {'in': 'Quits', 'out': True},
        {'in': 'Quizzes', 'out': True},
        {'in': 'Reaches', 'out': True},
        {'in': 'Remains', 'out': True},
        {'in': 'Remembers', 'out': True},
        {'in': 'Rends', 'out': True},
        {'in': 'Rents', 'out': True},
        {'in': 'Rids', 'out': True},
        {'in': 'Rings', 'out': True},
        {'in': 'Rises', 'out': True},
        {'in': 'Rives', 'out': True},
        {'in': 'S', 'out': True},
        {'in': 'Saws', 'out': True},
        {'in': 'Seeks', 'out': True},
        {'in': 'Seems', 'out': True},
        {'in': 'Shakes', 'out': True},
        {'in': 'Shall', 'out': True},
        {'in': 'Shaves', 'out': True},
        {'in': 'Sheds', 'out': True},
        {'in': 'Shits', 'out': True},
        {'in': 'Shoes', 'out': True},
        {'in': 'Should', 'out': True},
        {'in': 'Shows', 'out': True},
        {'in': 'Shrinks', 'out': True},
        {'in': 'Sings', 'out': True},
        {'in': 'Sinks', 'out': True},
        {'in': 'Sits', 'out': True},
        {'in': 'Skis', 'out': True},
        {'in': 'Slays', 'out': True},
        {'in': 'Slides', 'out': True},
        {'in': 'Slinks', 'out': True},
        {'in': 'Slits', 'out': True},
        {'in': 'Smells', 'out': True},
        {'in': 'Smites', 'out': True},
        {'in': 'Sneaks', 'out': True},
        {'in': 'Sows', 'out': True},
        {'in': 'Speaks', 'out': True},
        {'in': 'Speeds', 'out': True},
        {'in': 'Spends', 'out': True},
        {'in': 'Spits', 'out': True},
        {'in': 'Spoils', 'out': True},
        {'in': 'Springs', 'out': True},
        {'in': 'Stands', 'out': True},
        {'in': 'Staves', 'out': True},
        {'in': 'Stays', 'out': True},
        {'in': 'Steals', 'out': True},
        {'in': 'Stings', 'out': True},
        {'in': 'Stinks', 'out': True},
        {'in': 'Stops', 'out': True},
        {'in': 'Strews', 'out': True},
        {'in': 'Strides', 'out': True},
        {'in': 'Strips', 'out': True},
        {'in': 'Strives', 'out': True},
        {'in': 'Sublets', 'out': True},
        {'in': 'Sunburns', 'out': True},
        {'in': 'Swears', 'out': True},
        {'in': 'Sweats', 'out': True},
        {'in': 'Sweeps', 'out': True},
        {'in': 'Swells', 'out': True},
        {'in': 'Swims', 'out': True},
        {'in': 'Swings', 'out': True},
        {'in': 'Talks', 'out': True},
        {'in': 'Tears', 'out': True},
        {'in': 'Thrives', 'out': True},
        {'in': 'Thrusts', 'out': True},
        {'in': 'Treads', 'out': True},
        {'in': 'Undergoes', 'out': True},
        {'in': 'Underlies', 'out': True},
        {'in': 'Understands', 'out': True},
        {'in': 'Undertakes', 'out': True},
        {'in': 'Upsets', 'out': True},
        {'in': 'Vexes', 'out': True},
        {'in': 'Vies', 'out': True},
        {'in': 'Waits', 'out': True},
        {'in': 'Wakes', 'out': True},
        {'in': 'Walks', 'out': True},
        {'in': 'Wants', 'out': True},
        {'in': 'Was', 'out': True},
        {'in': 'Watches', 'out': True},
        {'in': 'Wears', 'out': True},
        {'in': 'Weeps', 'out': True},
        {'in': 'Wends', 'out': True},
        {'in': 'Will', 'out': True},
        {'in': 'Wins', 'out': True},
        {'in': 'Wises', 'out': True},
        {'in': 'Withdraws', 'out': True},
        {'in': 'Withholds', 'out': True},
        {'in': 'Withstands', 'out': True},
        {'in': 'Would', 'out': True},
        {'in': 'Wrings', 'out': True},
        {'in': 'abides', 'out': True},
        {'in': 'aches', 'out': True},
        {'in': 'arcs', 'out': True},
        {'in': 'arises', 'out': True},
        {'in': 'asks', 'out': True},
        {'in': 'avalanches', 'out': True},
        {'in': 'awakes', 'out': True},
        {'in': 'beats', 'out': True},
        {'in': 'becomes', 'out': True},
        {'in': 'begets', 'out': True},
        {'in': 'begins', 'out': True},
        {'in': 'beholds', 'out': True},
        {'in': 'bellyaches', 'out': True},
        {'in': 'bends', 'out': True},
        {'in': 'bets', 'out': True},
        {'in': 'biases', 'out': True},
        {'in': 'bites', 'out': True},
        {'in': 'bleeds', 'out': True},
        {'in': 'blitzes', 'out': True},
        {'in': 'blows', 'out': True},
        {'in': 'breaks', 'out': True},
        {'in': 'brings', 'out': True},
        {'in': 'builds', 'out': True},
        {'in': 'burns', 'out': True},
        {'in': 'bursts', 'out': True},
        {'in': 'buses', 'out': True},
        {'in': 'busts', 'out': True},
        {'in': 'caches', 'out': True},
        {'in': 'caddies', 'out': True},
        {'in': 'can', 'out': True},
        {'in': 'canvases', 'out': True},
        {'in': 'catches', 'out': True},
        {'in': 'caucuses', 'out': True},
        {'in': 'changes', 'out': True},
        {'in': 'chooses', 'out': True},
        {'in': 'choruses', 'out': True},
        {'in': 'claps', 'out': True},
        {'in': 'clings', 'out': True},
        {'in': 'comes', 'out': True},
        {'in': 'continues', 'out': True},
        {'in': 'costs', 'out': True},
        {'in': 'could', 'out': True},
        {'in': 'creches', 'out': True},
        {'in': 'creeps', 'out': True},
        {'in': 'dares', 'out': True},
        {'in': 'deals', 'out': True},
        {'in': 'dies', 'out': True},
        {'in': 'digs', 'out': True},
        {'in': 'disses', 'out': True},
        {'in': 'dives', 'out': True},
        {'in': 'does', 'out': True},
        {'in': 'douches', 'out': True},
        {'in': 'drags', 'out': True},
        {'in': 'dreams', 'out': True},
        {'in': 'drinks', 'out': True},
        {'in': 'drives', 'out': True},
        {'in': 'dwells', 'out': True},
        {'in': 'eats', 'out': True},
        {'in': 'expects', 'out': True},
        {'in': 'falls', 'out': True},
        {'in': 'feels', 'out': True},
        {'in': 'fights', 'out': True},
        {'in': 'finds', 'out': True},
        {'in': 'flees', 'out': True},
        {'in': 'flies', 'out': True},
        {'in': 'flings', 'out': True},
        {'in': 'focuses', 'out': True},
        {'in': 'follows', 'out': True},
        {'in': 'forbids', 'out': True},
        {'in': 'foresees', 'out': True},
        {'in': 'foretells', 'out': True},
        {'in': 'forgets', 'out': True},
        {'in': 'forgives', 'out': True},
        {'in': 'forsakes', 'out': True},
        {'in': 'gases', 'out': True},
        {'in': 'gets', 'out': True},
        {'in': 'gilds', 'out': True},
        {'in': 'gives', 'out': True},
        {'in': 'goes', 'out': True},
        {'in': 'grinds', 'out': True},
        {'in': 'happens', 'out': True},
        {'in': 'has', 'out': True},
        {'in': 'helps', 'out': True},
        {'in': 'hews', 'out': True},
        {'in': 'hies', 'out': True},
        {'in': 'hits', 'out': True},
        {'in': 'hocuses', 'out': True},
        {'in': 'holds', 'out': True},
        {'in': 'hurts', 'out': True},
        {'in': 'inlays', 'out': True},
        {'in': 'insists', 'out': True},
        {'in': 'interlays', 'out': True},
        {'in': 'irises', 'out': True},
        {'in': 'keeps', 'out': True},
        {'in': 'kills', 'out': True},
        {'in': 'kneels', 'out': True},
        {'in': 'knits', 'out': True},
        {'in': 'knows', 'out': True},
        {'in': 'lays', 'out': True},
        {'in': 'leads', 'out': True},
        {'in': 'leans', 'out': True},
        {'in': 'leaps', 'out': True},
        {'in': 'learns', 'out': True},
        {'in': 'leaves', 'out': True},
        {'in': 'lets', 'out': True},
        {'in': 'lies', 'out': True},
        {'in': 'likes', 'out': True},
        {'in': 'lives', 'out': True},
        {'in': 'looks', 'out': True},
        {'in': 'loses', 'out': True},
        {'in': 'loves', 'out': True},
        {'in': 'may', 'out': True},
        {'in': 'means', 'out': True},
        {'in': 'meets', 'out': True},
        {'in': 'menus', 'out': True},
        {'in': 'might', 'out': True},
        {'in': 'misleads', 'out': True},
        {'in': 'mistakes', 'out': True},
        {'in': 'misunderstands', 'out': True},
        {'in': 'moves', 'out': True},
        {'in': 'must', 'out': True},
        {'in': 'needs', 'out': True},
        {'in': 'niches', 'out': True},
        {'in': 'ought', 'out': True},
        {'in': 'outvies', 'out': True},
        {'in': 'overdraws', 'out': True},
        {'in': 'overhears', 'out': True},
        {'in': 'overtakes', 'out': True},
        {'in': 'presets', 'out': True},
        {'in': 'proves', 'out': True},
        {'in': 'provides', 'out': True},
        {'in': 'psyches', 'out': True},
        {'in': 'puts', 'out': True},
        {'in': 'quits', 'out': True},
        {'in': 'quizzes', 'out': True},
        {'in': 'reaches', 'out': True},
        {'in': 'remains', 'out': True},
        {'in': 'remembers', 'out': True},
        {'in': 'rends', 'out': True},
        {'in': 'rents', 'out': True},
        {'in': 'rids', 'out': True},
        {'in': 'rings', 'out': True},
        {'in': 'rises', 'out': True},
        {'in': 'rives', 'out': True},
        {'in': 's', 'out': True},
        {'in': 'saws', 'out': True},
        {'in': 'seeks', 'out': True},
        {'in': 'seems', 'out': True},
        {'in': 'shakes', 'out': True},
        {'in': 'shall', 'out': True},
        {'in': 'shaves', 'out': True},
        {'in': 'sheds', 'out': True},
        {'in': 'shits', 'out': True},
        {'in': 'shoes', 'out': True},
        {'in': 'should', 'out': True},
        {'in': 'shows', 'out': True},
        {'in': 'shrinks', 'out': True},
        {'in': 'sings', 'out': True},
        {'in': 'sinks', 'out': True},
        {'in': 'sits', 'out': True},
        {'in': 'skis', 'out': True},
        {'in': 'slays', 'out': True},
        {'in': 'slides', 'out': True},
        {'in': 'slinks', 'out': True},
        {'in': 'slits', 'out': True},
        {'in': 'smells', 'out': True},
        {'in': 'smites', 'out': True},
        {'in': 'sneaks', 'out': True},
        {'in': 'sows', 'out': True},
        {'in': 'speaks', 'out': True},
        {'in': 'speeds', 'out': True},
        {'in': 'spends', 'out': True},
        {'in': 'spits', 'out': True},
        {'in': 'spoils', 'out': True},
        {'in': 'springs', 'out': True},
        {'in': 'stands', 'out': True},
        {'in': 'staves', 'out': True},
        {'in': 'stays', 'out': True},
        {'in': 'steals', 'out': True},
        {'in': 'stings', 'out': True},
        {'in': 'stinks', 'out': True},
        {'in': 'stops', 'out': True},
        {'in': 'strews', 'out': True},
        {'in': 'strides', 'out': True},
        {'in': 'strips', 'out': True},
        {'in': 'strives', 'out': True},
        {'in': 'sublets', 'out': True},
        {'in': 'sunburns', 'out': True},
        {'in': 'swears', 'out': True},
        {'in': 'sweats', 'out': True},
        {'in': 'sweeps', 'out': True},
        {'in': 'swells', 'out': True},
        {'in': 'swims', 'out': True},
        {'in': 'swings', 'out': True},
        {'in': 'talks', 'out': True},
        {'in': 'tears', 'out': True},
        {'in': 'thrives', 'out': True},
        {'in': 'thrusts', 'out': True},
        {'in': 'treads', 'out': True},
        {'in': 'undergoes', 'out': True},
        {'in': 'underlies', 'out': True},
        {'in': 'understands', 'out': True},
        {'in': 'undertakes', 'out': True},
        {'in': 'upsets', 'out': True},
        {'in': 'vexes', 'out': True},
        {'in': 'vies', 'out': True},
        {'in': 'waits', 'out': True},
        {'in': 'wakes', 'out': True},
        {'in': 'walks', 'out': True},
        {'in': 'wants', 'out': True},
        {'in': 'was', 'out': True},
        {'in': 'watches', 'out': True},
        {'in': 'wears', 'out': True},
        {'in': 'weeps', 'out': True},
        {'in': 'wends', 'out': True},
        {'in': 'will', 'out': True},
        {'in': 'wins', 'out': True},
        {'in': 'wises', 'out': True},
        {'in': 'withdraws', 'out': True},
        {'in': 'withholds', 'out': True},
        {'in': 'withstands', 'out': True},
        {'in': 'would', 'out': True},
        {'in': 'wrings', 'out': True},
    ]

    def test_verb_is_singular(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {**test_case, **{
                    "desc": f"is_singular({repr(test_case['in'])}) => {repr(test_case['out'])}",
                    "kwargs": {}
                }}
                self.assertEqual(Verb(test_case["in"]).is_singular(**test_case["kwargs"]), test_case["out"], test_case["desc"])


if __name__ == "__main__":
    unittest.main()
