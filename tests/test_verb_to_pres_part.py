
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

from verb_output import convert_to_pres_part

class TestVerbToPresPart(unittest.TestCase):
    # test_args has the format [{
    #    "in":     ..., # (required)
    #    "out":    ..., # (required)
    #    "desc":   ..., # (optional) 
    #    "kwargs": ...  # (optional)
    # }, ...
    # ]
    test_args = [
        {'in': 'is', 'out': 'being'},
        {'in': 'are', 'out': 'being'},
        {'in': 'was', 'out': 'being'},
        {'in': 'being', 'out': 'being'},
        {'in': 'been', 'out': 'being'},
        {'in': 'were', 'out': 'being'},
        {'in': 'am', 'out': 'being'},
        {'in': 'aches', 'out': 'aching'},
        {'in': 'ache', 'out': 'aching'},
        {'in': 'ached', 'out': 'aching'},
        {'in': 'aching', 'out': 'aching'},
        {'in': 'arises', 'out': 'arising'},
        {'in': 'arise', 'out': 'arising'},
        {'in': 'arose', 'out': 'arising'},
        {'in': 'arising', 'out': 'arising'},
        {'in': 'arisen', 'out': 'arising'},
        {'in': 'asks', 'out': 'asking'},
        {'in': 'ask', 'out': 'asking'},
        {'in': 'asked', 'out': 'asking'},
        {'in': 'asking', 'out': 'asking'},
        {'in': 'avalanches', 'out': 'avalanching'},
        {'in': 'avalanche', 'out': 'avalanching'},
        {'in': 'avalanched', 'out': 'avalanching'},
        {'in': 'avalanching', 'out': 'avalanching'},
        {'in': 'awakes', 'out': 'awakening'},
        {'in': 'awake', 'out': 'awakening'},
        {'in': 'awoke', 'out': 'awakening'},
        {'in': 'awakening', 'out': 'awakening'},
        {'in': 'awoken', 'out': 'awakening'},
        {'in': 'beats', 'out': 'beating'},
        {'in': 'beat', 'out': 'beating'},
        {'in': 'beating', 'out': 'beating'},
        {'in': 'beaten', 'out': 'beating'},
        {'in': 'becomes', 'out': 'becoming'},
        {'in': 'become', 'out': 'becoming'},
        {'in': 'became', 'out': 'becoming'},
        {'in': 'becoming', 'out': 'becoming'},
        {'in': 'begets', 'out': 'begetting'},
        {'in': 'beget', 'out': 'begetting'},
        {'in': 'begot', 'out': 'begetting'},
        {'in': 'begetting', 'out': 'begetting'},
        {'in': 'begotten', 'out': 'begetting'},
        {'in': 'begins', 'out': 'beginning'},
        {'in': 'begin', 'out': 'beginning'},
        {'in': 'began', 'out': 'beginning'},
        {'in': 'beginning', 'out': 'beginning'},
        {'in': 'begun', 'out': 'beginning'},
        {'in': 'beholds', 'out': 'beholding'},
        {'in': 'behold', 'out': 'beholding'},
        {'in': 'beheld', 'out': 'beholding'},
        {'in': 'beholding', 'out': 'beholding'},
        {'in': 'bellyaches', 'out': 'bellyaching'},
        {'in': 'bellyache', 'out': 'bellyaching'},
        {'in': 'bellyached', 'out': 'bellyaching'},
        {'in': 'bellyaching', 'out': 'bellyaching'},
        {'in': 'bends', 'out': 'bending'},
        {'in': 'bend', 'out': 'bending'},
        {'in': 'bent', 'out': 'bending'},
        {'in': 'bending', 'out': 'bending'},
        {'in': 'bets', 'out': 'betting'},
        {'in': 'bet', 'out': 'betting'},
        {'in': 'betting', 'out': 'betting'},
        {'in': 'binds', 'out': 'binding'},
        {'in': 'bind', 'out': 'binding'},
        {'in': 'bound', 'out': 'binding'},
        {'in': 'binding', 'out': 'binding'},
        {'in': 'bites', 'out': 'biting'},
        {'in': 'bite', 'out': 'biting'},
        {'in': 'bit', 'out': 'biting'},
        {'in': 'biting', 'out': 'biting'},
        {'in': 'bitten', 'out': 'biting'},
        {'in': 'blitzes', 'out': 'blitzing'},
        {'in': 'blitz', 'out': 'blitzing'},
        {'in': 'blitzed', 'out': 'blitzing'},
        {'in': 'blitzing', 'out': 'blitzing'},
        {'in': 'bleeds', 'out': 'bleeding'},
        {'in': 'bleed', 'out': 'bleeding'},
        {'in': 'bled', 'out': 'bleeding'},
        {'in': 'bleeding', 'out': 'bleeding'},
        {'in': 'blows', 'out': 'blowing'},
        {'in': 'blow', 'out': 'blowing'},
        {'in': 'blew', 'out': 'blowing'},
        {'in': 'blowing', 'out': 'blowing'},
        {'in': 'blown', 'out': 'blowing'},
        {'in': 'breaks', 'out': 'breaking'},
        {'in': 'break', 'out': 'breaking'},
        {'in': 'broke', 'out': 'breaking'},
        {'in': 'breaking', 'out': 'breaking'},
        {'in': 'broken', 'out': 'breaking'},
        {'in': 'breeds', 'out': 'breeding'},
        {'in': 'breed', 'out': 'breeding'},
        {'in': 'bred', 'out': 'breeding'},
        {'in': 'breeding', 'out': 'breeding'},
        {'in': 'brings', 'out': 'bringing'},
        {'in': 'bring', 'out': 'bringing'},
        {'in': 'brought', 'out': 'bringing'},
        {'in': 'bringing', 'out': 'bringing'},
        {'in': 'builds', 'out': 'building'},
        {'in': 'build', 'out': 'building'},
        {'in': 'built', 'out': 'building'},
        {'in': 'building', 'out': 'building'},
        {'in': 'burns', 'out': 'burning'},
        {'in': 'burn', 'out': 'burning'},
        {'in': 'burnt', 'out': 'burning'},
        {'in': 'burning', 'out': 'burning'},
        {'in': 'bursts', 'out': 'bursting'},
        {'in': 'burst', 'out': 'bursting'},
        {'in': 'bursting', 'out': 'bursting'},
        {'in': 'busts', 'out': 'busting'},
        {'in': 'bust', 'out': 'busting'},
        {'in': 'busting', 'out': 'busting'},
        {'in': 'caches', 'out': 'caching'},
        {'in': 'cache', 'out': 'caching'},
        {'in': 'cached', 'out': 'caching'},
        {'in': 'caching', 'out': 'caching'},
        {'in': 'catches', 'out': 'catching'},
        {'in': 'catch', 'out': 'catching'},
        {'in': 'caught', 'out': 'catching'},
        {'in': 'catching', 'out': 'catching'},
        {'in': 'chooses', 'out': 'choosing'},
        {'in': 'choose', 'out': 'choosing'},
        {'in': 'chose', 'out': 'choosing'},
        {'in': 'choosing', 'out': 'choosing'},
        {'in': 'chosen', 'out': 'choosing'},
        {'in': 'clings', 'out': 'clinging'},
        {'in': 'cling', 'out': 'clinging'},
        {'in': 'clung', 'out': 'clinging'},
        {'in': 'clinging', 'out': 'clinging'},
        {'in': 'comes', 'out': 'coming'},
        {'in': 'come', 'out': 'coming'},
        {'in': 'came', 'out': 'coming'},
        {'in': 'coming', 'out': 'coming'},
        {'in': 'costs', 'out': 'costing'},
        {'in': 'cost', 'out': 'costing'},
        {'in': 'costing', 'out': 'costing'},
        {'in': 'creches', 'out': 'creching'},
        {'in': 'creche', 'out': 'creching'},
        {'in': 'creched', 'out': 'creching'},
        {'in': 'creching', 'out': 'creching'},
        {'in': 'creeps', 'out': 'creeping'},
        {'in': 'creep', 'out': 'creeping'},
        {'in': 'crept', 'out': 'creeping'},
        {'in': 'creeping', 'out': 'creeping'},
        {'in': 'deals', 'out': 'dealing'},
        {'in': 'deal', 'out': 'dealing'},
        {'in': 'dealt', 'out': 'dealing'},
        {'in': 'dealing', 'out': 'dealing'},
        {'in': 'digs', 'out': 'digging'},
        {'in': 'dig', 'out': 'digging'},
        {'in': 'dug', 'out': 'digging'},
        {'in': 'digging', 'out': 'digging'},
        {'in': 'dives', 'out': 'diving'},
        {'in': 'dive', 'out': 'diving'},
        {'in': 'dived', 'out': 'diving'},
        {'in': 'diving', 'out': 'diving'},
        {'in': 'douches', 'out': 'douching'},
        {'in': 'douche', 'out': 'douching'},
        {'in': 'douched', 'out': 'douching'},
        {'in': 'douching', 'out': 'douching'},
        {'in': 'drags', 'out': 'dragging'},
        {'in': 'drag', 'out': 'dragging'},
        {'in': 'dragged', 'out': 'dragging'},
        {'in': 'dragging', 'out': 'dragging'},
        {'in': 'drinks', 'out': 'drinking'},
        {'in': 'drink', 'out': 'drinking'},
        {'in': 'drank', 'out': 'drinking'},
        {'in': 'drinking', 'out': 'drinking'},
        {'in': 'drunk', 'out': 'drinking'},
        {'in': 'drives', 'out': 'driving'},
        {'in': 'drive', 'out': 'driving'},
        {'in': 'drove', 'out': 'driving'},
        {'in': 'driving', 'out': 'driving'},
        {'in': 'driven', 'out': 'driving'},
        {'in': 'dwells', 'out': 'dwelling'},
        {'in': 'dwell', 'out': 'dwelling'},
        {'in': 'dwelt', 'out': 'dwelling'},
        {'in': 'dwelling', 'out': 'dwelling'},
        {'in': 'eats', 'out': 'eating'},
        {'in': 'eat', 'out': 'eating'},
        {'in': 'ate', 'out': 'eating'},
        {'in': 'eating', 'out': 'eating'},
        {'in': 'eaten', 'out': 'eating'},
        {'in': 'falls', 'out': 'falling'},
        {'in': 'fall', 'out': 'falling'},
        {'in': 'fell', 'out': 'falling'},
        {'in': 'falling', 'out': 'falling'},
        {'in': 'fallen', 'out': 'falling'},
        {'in': 'feels', 'out': 'feeling'},
        {'in': 'feel', 'out': 'feeling'},
        {'in': 'felt', 'out': 'feeling'},
        {'in': 'feeling', 'out': 'feeling'},
        {'in': 'fights', 'out': 'fighting'},
        {'in': 'fight', 'out': 'fighting'},
        {'in': 'fought', 'out': 'fighting'},
        {'in': 'fighting', 'out': 'fighting'},
        {'in': 'finds', 'out': 'finding'},
        {'in': 'find', 'out': 'finding'},
        {'in': 'found', 'out': 'finding'},
        {'in': 'finding', 'out': 'finding'},
        {'in': 'flees', 'out': 'fleeing'},
        {'in': 'flee', 'out': 'fleeing'},
        {'in': 'fled', 'out': 'fleeing'},
        {'in': 'fleeing', 'out': 'fleeing'},
        {'in': 'flies', 'out': 'flying'},
        {'in': 'fly', 'out': 'flying'},
        {'in': 'flew', 'out': 'flying'},
        {'in': 'flying', 'out': 'flying'},
        {'in': 'flown', 'out': 'flying'},
        {'in': 'flings', 'out': 'flinging'},
        {'in': 'fling', 'out': 'flinging'},
        {'in': 'flung', 'out': 'flinging'},
        {'in': 'flinging', 'out': 'flinging'},
        {'in': 'forbids', 'out': 'forbidding'},
        {'in': 'forbid', 'out': 'forbidding'},
        {'in': 'forbade', 'out': 'forbidding'},
        {'in': 'forbidding', 'out': 'forbidding'},
        {'in': 'forbidden', 'out': 'forbidding'},
        {'in': 'foresees', 'out': 'foreseeing'},
        {'in': 'foresee', 'out': 'foreseeing'},
        {'in': 'foresaw', 'out': 'foreseeing'},
        {'in': 'foreseeing', 'out': 'foreseeing'},
        {'in': 'foreseen', 'out': 'foreseeing'},
        {'in': 'foretells', 'out': 'foretelling'},
        {'in': 'foretell', 'out': 'foretelling'},
        {'in': 'foretold', 'out': 'foretelling'},
        {'in': 'foretelling', 'out': 'foretelling'},
        {'in': 'forgets', 'out': 'forgetting'},
        {'in': 'forget', 'out': 'forgetting'},
        {'in': 'forgot', 'out': 'forgetting'},
        {'in': 'forgetting', 'out': 'forgetting'},
        {'in': 'forgotten', 'out': 'forgetting'},
        {'in': 'forgives', 'out': 'forgiving'},
        {'in': 'forgive', 'out': 'forgiving'},
        {'in': 'forgave', 'out': 'forgiving'},
        {'in': 'forgiving', 'out': 'forgiving'},
        {'in': 'forgiven', 'out': 'forgiving'},
        {'in': 'forsakes', 'out': 'forsaking'},
        {'in': 'forsake', 'out': 'forsaking'},
        {'in': 'forsook', 'out': 'forsaking'},
        {'in': 'forsaking', 'out': 'forsaking'},
        {'in': 'forsaken', 'out': 'forsaking'},
        {'in': 'gets', 'out': 'getting'},
        {'in': 'get', 'out': 'getting'},
        {'in': 'got', 'out': 'getting'},
        {'in': 'getting', 'out': 'getting'},
        {'in': 'gotten', 'out': 'getting'},
        {'in': 'gilds', 'out': 'gilding'},
        {'in': 'gild', 'out': 'gilding'},
        {'in': 'gilded', 'out': 'gilding'},
        {'in': 'gilding', 'out': 'gilding'},
        {'in': 'gives', 'out': 'giving'},
        {'in': 'give', 'out': 'giving'},
        {'in': 'gave', 'out': 'giving'},
        {'in': 'giving', 'out': 'giving'},
        {'in': 'given', 'out': 'giving'},
        {'in': 'goes', 'out': 'going'},
        {'in': 'go', 'out': 'going'},
        {'in': 'went', 'out': 'going'},
        {'in': 'going', 'out': 'going'},
        {'in': 'gone', 'out': 'going'},
        {'in': 'grinds', 'out': 'grinding'},
        {'in': 'grind', 'out': 'grinding'},
        {'in': 'ground', 'out': 'grinding'},
        {'in': 'grinding', 'out': 'grinding'},
        {'in': 'has', 'out': 'having'},
        {'in': 'have', 'out': 'having'},
        {'in': 'had', 'out': 'having'},
        {'in': 'having', 'out': 'having'},
        {'in': 'hews', 'out': 'hewing'},
        {'in': 'hew', 'out': 'hewing'},
        {'in': 'hewed', 'out': 'hewing'},
        {'in': 'hewing', 'out': 'hewing'},
        {'in': 'hewn', 'out': 'hewing'},
        {'in': 'hits', 'out': 'hitting'},
        {'in': 'hit', 'out': 'hitting'},
        {'in': 'hitting', 'out': 'hitting'},
        {'in': 'holds', 'out': 'holding'},
        {'in': 'hold', 'out': 'holding'},
        {'in': 'held', 'out': 'holding'},
        {'in': 'holding', 'out': 'holding'},
        {'in': 'hurts', 'out': 'hurting'},
        {'in': 'hurt', 'out': 'hurting'},
        {'in': 'hurting', 'out': 'hurting'},
        {'in': 'inlays', 'out': 'inlaying'},
        {'in': 'inlay', 'out': 'inlaying'},
        {'in': 'inlaid', 'out': 'inlaying'},
        {'in': 'inlaying', 'out': 'inlaying'},
        {'in': 'insists', 'out': 'insisting'},
        {'in': 'insist', 'out': 'insisting'},
        {'in': 'insisted', 'out': 'insisting'},
        {'in': 'insisting', 'out': 'insisting'},
        {'in': 'interlays', 'out': 'interlaying'},
        {'in': 'interlay', 'out': 'interlaying'},
        {'in': 'interlaid', 'out': 'interlaying'},
        {'in': 'interlaying', 'out': 'interlaying'},
        {'in': 'irises', 'out': 'irising'},
        {'in': 'iris', 'out': 'irising'},
        {'in': 'irised', 'out': 'irising'},
        {'in': 'irising', 'out': 'irising'},
        {'in': 'keeps', 'out': 'keeping'},
        {'in': 'keep', 'out': 'keeping'},
        {'in': 'kept', 'out': 'keeping'},
        {'in': 'keeping', 'out': 'keeping'},
        {'in': 'kneels', 'out': 'kneeling'},
        {'in': 'kneel', 'out': 'kneeling'},
        {'in': 'knelt', 'out': 'kneeling'},
        {'in': 'kneeling', 'out': 'kneeling'},
        {'in': 'knows', 'out': 'knowing'},
        {'in': 'know', 'out': 'knowing'},
        {'in': 'knew', 'out': 'knowing'},
        {'in': 'knowing', 'out': 'knowing'},
        {'in': 'known', 'out': 'knowing'},
        {'in': 'lays', 'out': 'laying'},
        {'in': 'lay', 'out': 'lying'},
        {'in': 'laid', 'out': 'laying'},
        {'in': 'laying', 'out': 'laying'},
        {'in': 'leads', 'out': 'leading'},
        {'in': 'lead', 'out': 'leading'},
        {'in': 'led', 'out': 'leading'},
        {'in': 'leading', 'out': 'leading'},
        {'in': 'leans', 'out': 'leaning'},
        {'in': 'lean', 'out': 'leaning'},
        {'in': 'leaned', 'out': 'leaning'},
        {'in': 'leaning', 'out': 'leaning'},
        {'in': 'leaps', 'out': 'leaping'},
        {'in': 'leap', 'out': 'leaping'},
        {'in': 'leapt', 'out': 'leaping'},
        {'in': 'leaping', 'out': 'leaping'},
        {'in': 'leaves', 'out': 'leaving'},
        {'in': 'leave', 'out': 'leaving'},
        {'in': 'left', 'out': 'leaving'},
        {'in': 'leaving', 'out': 'leaving'},
        {'in': 'lies', 'out': 'lying'},
        {'in': 'lie', 'out': 'lying'},
        {'in': 'lying', 'out': 'lying'},
        {'in': 'lain', 'out': 'lying'},
        {'in': 'loses', 'out': 'losing'},
        {'in': 'lose', 'out': 'losing'},
        {'in': 'lost', 'out': 'losing'},
        {'in': 'losing', 'out': 'losing'},
        {'in': 'means', 'out': 'meaning'},
        {'in': 'mean', 'out': 'meaning'},
        {'in': 'meant', 'out': 'meaning'},
        {'in': 'meaning', 'out': 'meaning'},
        {'in': 'meets', 'out': 'meeting'},
        {'in': 'meet', 'out': 'meeting'},
        {'in': 'met', 'out': 'meeting'},
        {'in': 'meeting', 'out': 'meeting'},
        {'in': 'menus', 'out': 'menuing'},
        {'in': 'menu', 'out': 'menuing'},
        {'in': 'menued', 'out': 'menuing'},
        {'in': 'menuing', 'out': 'menuing'},
        {'in': 'misleads', 'out': 'misleading'},
        {'in': 'mislead', 'out': 'misleading'},
        {'in': 'misled', 'out': 'misleading'},
        {'in': 'misleading', 'out': 'misleading'},
        {'in': 'mistakes', 'out': 'mistaking'},
        {'in': 'mistake', 'out': 'mistaking'},
        {'in': 'mistook', 'out': 'mistaking'},
        {'in': 'mistaking', 'out': 'mistaking'},
        {'in': 'mistaken', 'out': 'mistaking'},
        {'in': 'moves', 'out': 'moving'},
        {'in': 'move', 'out': 'moving'},
        {'in': 'moved', 'out': 'moving'},
        {'in': 'moving', 'out': 'moving'},
        {'in': 'niches', 'out': 'nicheing'},
        {'in': 'niche', 'out': 'nicheing'},
        {'in': 'niched', 'out': 'nicheing'},
        {'in': 'nicheing', 'out': 'nicheing'},
        {'in': 'overdraws', 'out': 'overdrawing'},
        {'in': 'overdraw', 'out': 'overdrawing'},
        {'in': 'overdrew', 'out': 'overdrawing'},
        {'in': 'overdrawing', 'out': 'overdrawing'},
        {'in': 'overdrawn', 'out': 'overdrawing'},
        {'in': 'overhears', 'out': 'overhearing'},
        {'in': 'overhear', 'out': 'overhearing'},
        {'in': 'overheard', 'out': 'overhearing'},
        {'in': 'overhearing', 'out': 'overhearing'},
        {'in': 'overtakes', 'out': 'overtaking'},
        {'in': 'overtake', 'out': 'overtaking'},
        {'in': 'overtook', 'out': 'overtaking'},
        {'in': 'overtaking', 'out': 'overtaking'},
        {'in': 'overtaken', 'out': 'overtaking'},
        {'in': 'presets', 'out': 'presetting'},
        {'in': 'preset', 'out': 'presetting'},
        {'in': 'presetting', 'out': 'presetting'},
        {'in': 'proves', 'out': 'proving'},
        {'in': 'prove', 'out': 'proving'},
        {'in': 'proved', 'out': 'proving'},
        {'in': 'proving', 'out': 'proving'},
        {'in': 'proven', 'out': 'proving'},
        {'in': 'psyches', 'out': 'psyching'},
        {'in': 'psyche', 'out': 'psyching'},
        {'in': 'psyched', 'out': 'psyching'},
        {'in': 'psyching', 'out': 'psyching'},
        {'in': 'puts', 'out': 'putting'},
        {'in': 'put', 'out': 'putting'},
        {'in': 'putting', 'out': 'putting'},
        {'in': 'quits', 'out': 'quitting'},
        {'in': 'quit', 'out': 'quitting'},
        {'in': 'quitting', 'out': 'quitting'},
        {'in': 'quizzes', 'out': 'quizzing'},
        {'in': 'quiz', 'out': 'quizzing'},
        {'in': 'quizzed', 'out': 'quizzing'},
        {'in': 'quizzing', 'out': 'quizzing'},
        {'in': 'rends', 'out': 'rending'},
        {'in': 'rend', 'out': 'rending'},
        {'in': 'rent', 'out': 'rending'},
        {'in': 'rending', 'out': 'rending'},
        {'in': 'rides', 'out': 'riding'},
        {'in': 'ride', 'out': 'riding'},
        {'in': 'rode', 'out': 'riding'},
        {'in': 'riding', 'out': 'riding'},
        {'in': 'ridden', 'out': 'riding'},
        {'in': 'rids', 'out': 'ridding'},
        {'in': 'rid', 'out': 'ridding'},
        {'in': 'ridding', 'out': 'ridding'},
        {'in': 'rings', 'out': 'ringing'},
        {'in': 'ring', 'out': 'ringing'},
        {'in': 'rang', 'out': 'ringing'},
        {'in': 'ringing', 'out': 'ringing'},
        {'in': 'rung', 'out': 'ringing'},
        {'in': 'rises', 'out': 'rising'},
        {'in': 'rise', 'out': 'rising'},
        {'in': 'rose', 'out': 'rising'},
        {'in': 'rising', 'out': 'rising'},
        {'in': 'risen', 'out': 'rising'},
        {'in': 'rives', 'out': 'riving'},
        {'in': 'rive', 'out': 'riving'},
        {'in': 'rived', 'out': 'riving'},
        {'in': 'riving', 'out': 'riving'},
        {'in': 'riven', 'out': 'riving'},
        {'in': 'runs', 'out': 'running'},
        {'in': 'run', 'out': 'running'},
        {'in': 'ran', 'out': 'running'},
        {'in': 'running', 'out': 'running'},
        {'in': 'saws', 'out': 'sawing'},
        {'in': 'saw', 'out': 'sawing'},
        {'in': 'sawed', 'out': 'sawing'},
        {'in': 'sawing', 'out': 'sawing'},
        {'in': 'sawn', 'out': 'sawing'},
        {'in': 'seeks', 'out': 'seeking'},
        {'in': 'seek', 'out': 'seeking'},
        {'in': 'sought', 'out': 'seeking'},
        {'in': 'seeking', 'out': 'seeking'},
        {'in': 'shakes', 'out': 'shaking'},
        {'in': 'shake', 'out': 'shaking'},
        {'in': 'shook', 'out': 'shaking'},
        {'in': 'shaking', 'out': 'shaking'},
        {'in': 'shaken', 'out': 'shaking'},
        {'in': 'shaves', 'out': 'shaving'},
        {'in': 'shave', 'out': 'shaving'},
        {'in': 'shaved', 'out': 'shaving'},
        {'in': 'shaving', 'out': 'shaving'},
        {'in': 'sheds', 'out': 'shedding'},
        {'in': 'shed', 'out': 'shedding'},
        {'in': 'shedding', 'out': 'shedding'},
        {'in': 'shits', 'out': 'shitting'},
        {'in': 'shit', 'out': 'shitting'},
        {'in': 'shat', 'out': 'shitting'},
        {'in': 'shitting', 'out': 'shitting'},
        {'in': 'shitted', 'out': 'shitting'},
        {'in': 'shoes', 'out': 'shoeing'},
        {'in': 'shoe', 'out': 'shoeing'},
        {'in': 'shod', 'out': 'shoeing'},
        {'in': 'shoeing', 'out': 'shoeing'},
        {'in': 'shows', 'out': 'showing'},
        {'in': 'show', 'out': 'showing'},
        {'in': 'showed', 'out': 'showing'},
        {'in': 'showing', 'out': 'showing'},
        {'in': 'shown', 'out': 'showing'},
        {'in': 'shrinks', 'out': 'shrinking'},
        {'in': 'shrink', 'out': 'shrinking'},
        {'in': 'shrank', 'out': 'shrinking'},
        {'in': 'shrinking', 'out': 'shrinking'},
        {'in': 'shrunk', 'out': 'shrinking'},
        {'in': 'sings', 'out': 'singing'},
        {'in': 'sing', 'out': 'singing'},
        {'in': 'sang', 'out': 'singing'},
        {'in': 'singing', 'out': 'singing'},
        {'in': 'sung', 'out': 'singing'},
        {'in': 'sinks', 'out': 'sinking'},
        {'in': 'sink', 'out': 'sinking'},
        {'in': 'sank', 'out': 'sinking'},
        {'in': 'sinking', 'out': 'sinking'},
        {'in': 'sunk', 'out': 'sinking'},
        {'in': 'sits', 'out': 'sitting'},
        {'in': 'sit', 'out': 'sitting'},
        {'in': 'sat', 'out': 'sitting'},
        {'in': 'sitting', 'out': 'sitting'},
        {'in': 'slays', 'out': 'slaying'},
        {'in': 'slay', 'out': 'slaying'},
        {'in': 'slew', 'out': 'slaying'},
        {'in': 'slaying', 'out': 'slaying'},
        {'in': 'slain', 'out': 'slaying'},
        {'in': 'slides', 'out': 'sliding'},
        {'in': 'slide', 'out': 'sliding'},
        {'in': 'slid', 'out': 'sliding'},
        {'in': 'sliding', 'out': 'sliding'},
        {'in': 'slinks', 'out': 'slinking'},
        {'in': 'slink', 'out': 'slinking'},
        {'in': 'slunk', 'out': 'slinking'},
        {'in': 'slinking', 'out': 'slinking'},
        {'in': 'slits', 'out': 'slitting'},
        {'in': 'slit', 'out': 'slitting'},
        {'in': 'slitting', 'out': 'slitting'},
        {'in': 'smells', 'out': 'smelling'},
        {'in': 'smell', 'out': 'smelling'},
        {'in': 'smelled', 'out': 'smelling'},
        {'in': 'smelling', 'out': 'smelling'},
        {'in': 'smites', 'out': 'smiting'},
        {'in': 'smite', 'out': 'smiting'},
        {'in': 'smote', 'out': 'smiting'},
        {'in': 'smiting', 'out': 'smiting'},
        {'in': 'smitten', 'out': 'smiting'},
        {'in': 'sows', 'out': 'sowing'},
        {'in': 'sow', 'out': 'sowing'},
        {'in': 'sowed', 'out': 'sowing'},
        {'in': 'sowing', 'out': 'sowing'},
        {'in': 'sown', 'out': 'sowing'},
        {'in': 'speaks', 'out': 'speaking'},
        {'in': 'speak', 'out': 'speaking'},
        {'in': 'spoke', 'out': 'speaking'},
        {'in': 'speaking', 'out': 'speaking'},
        {'in': 'spoken', 'out': 'speaking'},
        {'in': 'speeds', 'out': 'speeding'},
        {'in': 'speed', 'out': 'speeding'},
        {'in': 'sped', 'out': 'speeding'},
        {'in': 'speeding', 'out': 'speeding'},
        {'in': 'spends', 'out': 'spending'},
        {'in': 'spend', 'out': 'spending'},
        {'in': 'spent', 'out': 'spending'},
        {'in': 'spending', 'out': 'spending'},
        {'in': 'spits', 'out': 'spitting'},
        {'in': 'spit', 'out': 'spitting'},
        {'in': 'spat', 'out': 'spitting'},
        {'in': 'spitting', 'out': 'spitting'},
        {'in': 'spoils', 'out': 'spoiling'},
        {'in': 'spoil', 'out': 'spoiling'},
        {'in': 'spoilt', 'out': 'spoiling'},
        {'in': 'spoiling', 'out': 'spoiling'},
        {'in': 'spoiled', 'out': 'spoiling'},
        {'in': 'springs', 'out': 'springing'},
        {'in': 'spring', 'out': 'springing'},
        {'in': 'sprang', 'out': 'springing'},
        {'in': 'springing', 'out': 'springing'},
        {'in': 'sprung', 'out': 'springing'},
        {'in': 'stands', 'out': 'standing'},
        {'in': 'stand', 'out': 'standing'},
        {'in': 'stood', 'out': 'standing'},
        {'in': 'standing', 'out': 'standing'},
        {'in': 'staves', 'out': 'staving'},
        {'in': 'stave', 'out': 'staving'},
        {'in': 'staved', 'out': 'staving'},
        {'in': 'staving', 'out': 'staving'},
        {'in': 'steals', 'out': 'stealing'},
        {'in': 'steal', 'out': 'stealing'},
        {'in': 'stole', 'out': 'stealing'},
        {'in': 'stealing', 'out': 'stealing'},
        {'in': 'stolen', 'out': 'stealing'},
        {'in': 'stings', 'out': 'stinging'},
        {'in': 'sting', 'out': 'stinging'},
        {'in': 'stung', 'out': 'stinging'},
        {'in': 'stinging', 'out': 'stinging'},
        {'in': 'stinks', 'out': 'stinking'},
        {'in': 'stink', 'out': 'stinking'},
        {'in': 'stank', 'out': 'stinking'},
        {'in': 'stinking', 'out': 'stinking'},
        {'in': 'stunk', 'out': 'stinking'},
        {'in': 'strews', 'out': 'strewing'},
        {'in': 'strew', 'out': 'strewing'},
        {'in': 'strewed', 'out': 'strewing'},
        {'in': 'strewing', 'out': 'strewing'},
        {'in': 'strewn', 'out': 'strewing'},
        {'in': 'strides', 'out': 'striding'},
        {'in': 'stride', 'out': 'striding'},
        {'in': 'strode', 'out': 'striding'},
        {'in': 'striding', 'out': 'striding'},
        {'in': 'strives', 'out': 'striving'},
        {'in': 'strive', 'out': 'striving'},
        {'in': 'strove', 'out': 'striving'},
        {'in': 'striving', 'out': 'striving'},
        {'in': 'strived', 'out': 'striving'},
        {'in': 'sublets', 'out': 'subletting'},
        {'in': 'sublet', 'out': 'subletting'},
        {'in': 'subletting', 'out': 'subletting'},
        {'in': 'swears', 'out': 'swearing'},
        {'in': 'swear', 'out': 'swearing'},
        {'in': 'swore', 'out': 'swearing'},
        {'in': 'swearing', 'out': 'swearing'},
        {'in': 'sworn', 'out': 'swearing'},
        {'in': 'sweats', 'out': 'sweating'},
        {'in': 'sweat', 'out': 'sweating'},
        {'in': 'sweating', 'out': 'sweating'},
        {'in': 'sweated', 'out': 'sweating'},
        {'in': 'sweeps', 'out': 'sweeping'},
        {'in': 'sweep', 'out': 'sweeping'},
        {'in': 'swept', 'out': 'sweeping'},
        {'in': 'sweeping', 'out': 'sweeping'},
        {'in': 'swells', 'out': 'swelling'},
        {'in': 'swell', 'out': 'swelling'},
        {'in': 'swelled', 'out': 'swelling'},
        {'in': 'swelling', 'out': 'swelling'},
        {'in': 'swollen', 'out': 'swelling'},
        {'in': 'swims', 'out': 'swimming'},
        {'in': 'swim', 'out': 'swimming'},
        {'in': 'swam', 'out': 'swimming'},
        {'in': 'swimming', 'out': 'swimming'},
        {'in': 'swum', 'out': 'swimming'},
        {'in': 'swings', 'out': 'swinging'},
        {'in': 'swing', 'out': 'swinging'},
        {'in': 'swung', 'out': 'swinging'},
        {'in': 'swinging', 'out': 'swinging'},
        {'in': 'tears', 'out': 'tearing'},
        {'in': 'tear', 'out': 'tearing'},
        {'in': 'tore', 'out': 'tearing'},
        {'in': 'tearing', 'out': 'tearing'},
        {'in': 'torn', 'out': 'tearing'},
        {'in': 'thrusts', 'out': 'thrusting'},
        {'in': 'thrust', 'out': 'thrusting'},
        {'in': 'thrusting', 'out': 'thrusting'},
        {'in': 'treads', 'out': 'treading'},
        {'in': 'tread', 'out': 'treading'},
        {'in': 'trod', 'out': 'treading'},
        {'in': 'treading', 'out': 'treading'},
        {'in': 'trodden', 'out': 'treading'},
        {'in': 'undergoes', 'out': 'undergoing'},
        {'in': 'undergo', 'out': 'undergoing'},
        {'in': 'underwent', 'out': 'undergoing'},
        {'in': 'undergoing', 'out': 'undergoing'},
        {'in': 'undergone', 'out': 'undergoing'},
        {'in': 'understands', 'out': 'understanding'},
        {'in': 'understand', 'out': 'understanding'},
        {'in': 'understood', 'out': 'understanding'},
        {'in': 'understanding', 'out': 'understanding'},
        {'in': 'undertakes', 'out': 'undertaking'},
        {'in': 'undertake', 'out': 'undertaking'},
        {'in': 'undertook', 'out': 'undertaking'},
        {'in': 'undertaking', 'out': 'undertaking'},
        {'in': 'undertaken', 'out': 'undertaking'},
        {'in': 'upsets', 'out': 'upsetting'},
        {'in': 'upset', 'out': 'upsetting'},
        {'in': 'upsetting', 'out': 'upsetting'},
        {'in': 'wakes', 'out': 'waking'},
        {'in': 'wake', 'out': 'waking'},
        {'in': 'woke', 'out': 'waking'},
        {'in': 'waking', 'out': 'waking'},
        {'in': 'woken', 'out': 'waking'},
        {'in': 'wears', 'out': 'wearing'},
        {'in': 'wear', 'out': 'wearing'},
        {'in': 'wore', 'out': 'wearing'},
        {'in': 'wearing', 'out': 'wearing'},
        {'in': 'worn', 'out': 'wearing'},
        {'in': 'weeps', 'out': 'weeping'},
        {'in': 'weep', 'out': 'weeping'},
        {'in': 'wept', 'out': 'weeping'},
        {'in': 'weeping', 'out': 'weeping'},
        {'in': 'wends', 'out': 'wending'},
        {'in': 'wend', 'out': 'wending'},
        {'in': 'wended', 'out': 'wending'},
        {'in': 'wending', 'out': 'wending'},
        {'in': 'wins', 'out': 'winning'},
        {'in': 'win', 'out': 'winning'},
        {'in': 'won', 'out': 'winning'},
        {'in': 'winning', 'out': 'winning'},
        {'in': 'withdraws', 'out': 'withdrawing'},
        {'in': 'withdraw', 'out': 'withdrawing'},
        {'in': 'withdrew', 'out': 'withdrawing'},
        {'in': 'withdrawing', 'out': 'withdrawing'},
        {'in': 'withdrawn', 'out': 'withdrawing'},
        {'in': 'withholds', 'out': 'withholding'},
        {'in': 'withhold', 'out': 'withholding'},
        {'in': 'withheld', 'out': 'withholding'},
        {'in': 'withholding', 'out': 'withholding'},
        {'in': 'withstands', 'out': 'withstanding'},
        {'in': 'withstand', 'out': 'withstanding'},
        {'in': 'withstood', 'out': 'withstanding'},
        {'in': 'withstanding', 'out': 'withstanding'},
        {'in': 'wrings', 'out': 'wringing'},
        {'in': 'wring', 'out': 'wringing'},
        {'in': 'wrung', 'out': 'wringing'},
        {'in': 'wringing', 'out': 'wringing'},
        {'in': 'abides', 'out': 'abiding'},
        {'in': 'abide', 'out': 'abiding'},
        {'in': 'abided', 'out': 'abiding'},
        {'in': 'abiding', 'out': 'abiding'},
        {'in': 'changes', 'out': 'changing'},
        {'in': 'change', 'out': 'changing'},
        {'in': 'changed', 'out': 'changing'},
        {'in': 'changing', 'out': 'changing'},
        {'in': 'claps', 'out': 'clapping'},
        {'in': 'clap', 'out': 'clapping'},
        {'in': 'clapped', 'out': 'clapping'},
        {'in': 'clapping', 'out': 'clapping'},
        {'in': 'continues', 'out': 'continuing'},
        {'in': 'continue', 'out': 'continuing'},
        {'in': 'continued', 'out': 'continuing'},
        {'in': 'continuing', 'out': 'continuing'},
        {'in': 'dares', 'out': 'daring'},
        {'in': 'dare', 'out': 'daring'},
        {'in': 'dared', 'out': 'daring'},
        {'in': 'daring', 'out': 'daring'},
        {'in': 'dies', 'out': 'dying'},
        {'in': 'die', 'out': 'dying'},
        {'in': 'died', 'out': 'dying'},
        {'in': 'dying', 'out': 'dying'},
        {'in': 'dreams', 'out': 'dreaming'},
        {'in': 'dream', 'out': 'dreaming'},
        {'in': 'dreamed', 'out': 'dreaming'},
        {'in': 'dreaming', 'out': 'dreaming'},
        {'in': 'expects', 'out': 'expecting'},
        {'in': 'expect', 'out': 'expecting'},
        {'in': 'expected', 'out': 'expecting'},
        {'in': 'expecting', 'out': 'expecting'},
        {'in': 'follows', 'out': 'following'},
        {'in': 'follow', 'out': 'following'},
        {'in': 'followed', 'out': 'following'},
        {'in': 'following', 'out': 'following'},
        {'in': 'happens', 'out': 'happening'},
        {'in': 'happen', 'out': 'happening'},
        {'in': 'happened', 'out': 'happening'},
        {'in': 'happening', 'out': 'happening'},
        {'in': 'helps', 'out': 'helping'},
        {'in': 'help', 'out': 'helping'},
        {'in': 'helped', 'out': 'helping'},
        {'in': 'helping', 'out': 'helping'},
        {'in': 'kills', 'out': 'killing'},
        {'in': 'kill', 'out': 'killing'},
        {'in': 'killed', 'out': 'killing'},
        {'in': 'killing', 'out': 'killing'},
        {'in': 'knits', 'out': 'knitting'},
        {'in': 'knit', 'out': 'knitting'},
        {'in': 'knitted', 'out': 'knitting'},
        {'in': 'knitting', 'out': 'knitting'},
        {'in': 'learns', 'out': 'learning'},
        {'in': 'learn', 'out': 'learning'},
        {'in': 'learned', 'out': 'learning'},
        {'in': 'learning', 'out': 'learning'},
        {'in': 'likes', 'out': 'liking'},
        {'in': 'like', 'out': 'liking'},
        {'in': 'liked', 'out': 'liking'},
        {'in': 'liking', 'out': 'liking'},
        {'in': 'lives', 'out': 'living'},
        {'in': 'live', 'out': 'living'},
        {'in': 'lived', 'out': 'living'},
        {'in': 'living', 'out': 'living'},
        {'in': 'looks', 'out': 'looking'},
        {'in': 'look', 'out': 'looking'},
        {'in': 'looked', 'out': 'looking'},
        {'in': 'looking', 'out': 'looking'},
        {'in': 'loves', 'out': 'loving'},
        {'in': 'love', 'out': 'loving'},
        {'in': 'loved', 'out': 'loving'},
        {'in': 'loving', 'out': 'loving'},
        {'in': 'misunderstands', 'out': 'misunderstanding'},
        {'in': 'misunderstand', 'out': 'misunderstanding'},
        {'in': 'misunderstood', 'out': 'misunderstanding'},
        {'in': 'misunderstanding', 'out': 'misunderstanding'},
        {'in': 'needs', 'out': 'needing'},
        {'in': 'need', 'out': 'needing'},
        {'in': 'needed', 'out': 'needing'},
        {'in': 'needing', 'out': 'needing'},
        {'in': 'provides', 'out': 'providing'},
        {'in': 'provide', 'out': 'providing'},
        {'in': 'provided', 'out': 'providing'},
        {'in': 'providing', 'out': 'providing'},
        {'in': 'reaches', 'out': 'reaching'},
        {'in': 'reach', 'out': 'reaching'},
        {'in': 'reached', 'out': 'reaching'},
        {'in': 'reaching', 'out': 'reaching'},
        {'in': 'remains', 'out': 'remaining'},
        {'in': 'remain', 'out': 'remaining'},
        {'in': 'remained', 'out': 'remaining'},
        {'in': 'remaining', 'out': 'remaining'},
        {'in': 'remembers', 'out': 'remembering'},
        {'in': 'remember', 'out': 'remembering'},
        {'in': 'remembered', 'out': 'remembering'},
        {'in': 'remembering', 'out': 'remembering'},
        {'in': 'seems', 'out': 'seeming'},
        {'in': 'seem', 'out': 'seeming'},
        {'in': 'seemed', 'out': 'seeming'},
        {'in': 'seeming', 'out': 'seeming'},
        {'in': 'skis', 'out': 'skiing'},
        {'in': 'ski', 'out': 'skiing'},
        {'in': 'skied', 'out': 'skiing'},
        {'in': 'skiing', 'out': 'skiing'},
        {'in': 'sneaks', 'out': 'sneaking'},
        {'in': 'sneak', 'out': 'sneaking'},
        {'in': 'sneaked', 'out': 'sneaking'},
        {'in': 'sneaking', 'out': 'sneaking'},
        {'in': 'stays', 'out': 'staying'},
        {'in': 'stay', 'out': 'staying'},
        {'in': 'stayed', 'out': 'staying'},
        {'in': 'staying', 'out': 'staying'},
        {'in': 'stops', 'out': 'stopping'},
        {'in': 'stop', 'out': 'stopping'},
        {'in': 'stopped', 'out': 'stopping'},
        {'in': 'stopping', 'out': 'stopping'},
        {'in': 'strips', 'out': 'stripping'},
        {'in': 'strip', 'out': 'stripping'},
        {'in': 'stripped', 'out': 'stripping'},
        {'in': 'stripping', 'out': 'stripping'},
        {'in': 'sunburns', 'out': 'sunburning'},
        {'in': 'sunburn', 'out': 'sunburning'},
        {'in': 'sunburned', 'out': 'sunburning'},
        {'in': 'sunburning', 'out': 'sunburning'},
        {'in': 'talks', 'out': 'talking'},
        {'in': 'talk', 'out': 'talking'},
        {'in': 'talked', 'out': 'talking'},
        {'in': 'talking', 'out': 'talking'},
        {'in': 'thrives', 'out': 'thriving'},
        {'in': 'thrive', 'out': 'thriving'},
        {'in': 'thrived', 'out': 'thriving'},
        {'in': 'thriving', 'out': 'thriving'},
        {'in': 'vexes', 'out': 'vexing'},
        {'in': 'vex', 'out': 'vexing'},
        {'in': 'vexed', 'out': 'vexing'},
        {'in': 'vexing', 'out': 'vexing'},
        {'in': 'waits', 'out': 'waiting'},
        {'in': 'wait', 'out': 'waiting'},
        {'in': 'waited', 'out': 'waiting'},
        {'in': 'waiting', 'out': 'waiting'},
        {'in': 'walks', 'out': 'walking'},
        {'in': 'walk', 'out': 'walking'},
        {'in': 'walked', 'out': 'walking'},
        {'in': 'walking', 'out': 'walking'},
        {'in': 'wants', 'out': 'wanting'},
        {'in': 'want', 'out': 'wanting'},
        {'in': 'wanted', 'out': 'wanting'},
        {'in': 'wanting', 'out': 'wanting'},
        {'in': 'watches', 'out': 'watching'},
        {'in': 'watch', 'out': 'watching'},
        {'in': 'watched', 'out': 'watching'},
        {'in': 'watching', 'out': 'watching'},
    ]

    def test_convert_to_pres_part(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {**test_case, **{
                    "desc": f"convert_to_pres_part({repr(test_case['in'])}) => {repr(test_case['out'])}",
                    "kwargs": dict()
                }}
                self.assertEqual(convert_to_pres_part(test_case["in"], **test_case["kwargs"]), test_case["out"], test_case["desc"])

if __name__ == "__main__":
    unittest.main()
