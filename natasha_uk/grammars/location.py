# coding: utf-8
from __future__ import unicode_literals

from yargy_uk import (
    rule,
    and_, or_, not_
)
from yargy_uk.interpretation import fact
from yargy_uk.predicates import (
    gram, dictionary,
    vesum_tag,
)


Location = fact(
    'Location',
    ['name'],
)

ADJECTIVE_TAG = or_(
    gram('ADJF'),
    vesum_tag('adj')
)

GENITIVE_TAG = or_(
    gram('gent'),
    vesum_tag('v_rod')
)

REGION = rule(
    ADJECTIVE_TAG,
    dictionary({
        'край',
        'район',
        'область',
        'губернія',
    }),
).interpretation(Location.name.inflected())


AUTONOMOUS_DISTRICT = rule(
    ADJECTIVE_TAG.repeatable(),
    or_(
        rule(
            dictionary({'автономний'}),
            dictionary({'округ'}),
        ),
        rule('АО'),
    ),
).interpretation(Location.name.inflected())

FEDERATION = rule(
    ADJECTIVE_TAG.repeatable(),
    dictionary({
        'республіка',
        'федерація',
    })
).interpretation(Location.name.inflected())

ADJX_FEDERATION = rule(
    or_(
        gram('ADJF'),
        vesum_tag('adj')
    ).repeatable(),
    dictionary({
        'штат',
        'емірат',
    }),
    GENITIVE_TAG.optional().repeatable()
).interpretation(Location.name.inflected())

STATE = rule(
    dictionary({
        'графство',
        'штат',
    }),
    ADJECTIVE_TAG.optional(),
    or_(
        gram('NOUN'),
        vesum_tag('noun')
    ),
).interpretation(Location.name.inflected())

LOCALITY = rule(
    and_(
        dictionary({
            'місто',
            'село',
            'селище',
        }),
        not_(
            or_(
                gram('Abbr'),
                vesum_tag('abbr'),
                gram('PREP'),
                vesum_tag('prep'),
                gram('CONJ'),
                vesum_tag('conj'),
                gram('PRCL'),
                vesum_tag('part')
            ),
        ),
    ).optional(),
    and_(
        ADJECTIVE_TAG,
    ).optional(),
    and_(
        or_(
            vesum_tag('geo')
        ),
        not_(
            or_(
                gram('Abbr'),
                vesum_tag('abbr'),
                gram('PREP'),
                vesum_tag('prep'),
                gram('CONJ'),
                vesum_tag('conj'),
                gram('PRCL'),
                vesum_tag('part')
            ),
        ),
    )
).interpretation(Location.name.inflected())

LOCATION = or_(
    REGION,
    AUTONOMOUS_DISTRICT,
    FEDERATION,
    ADJX_FEDERATION,
    STATE,
    LOCALITY,
).interpretation(Location)
