# coding: utf-8
from __future__ import unicode_literals

from yargy_uk import (
    rule,
    and_, or_
)
from yargy_uk.interpretation import fact, attribute
from yargy_uk.predicates import (
    eq, gte, lte, length_eq,
    dictionary, normalized,
)


Date = fact(
    'Date',
    ['year', 'month', 'day', attribute('current_era', True)]
)


MONTHS = {
    'січень': 1,
    'лютий': 2,
    'березень': 3,
    'квітень': 4,
    'травень': 5,
    'червень': 6,
    'липень': 7,
    'серпень': 8,
    'вересень': 9,
    'жовтень': 10,
    'листопад': 11,
    'грудень': 12,
}


MONTH_NAME = dictionary(MONTHS).interpretation(
    Date.month.normalized().custom(MONTHS.__getitem__)
)

MONTH = and_(
    gte(1),
    lte(12)
).interpretation(
    Date.month.custom(int)
)

DAY = and_(
    gte(1),
    lte(31)
).interpretation(
    Date.day.custom(int)
)

YEAR_WORD = or_(
    rule('р', eq('.').optional()),
    rule(normalized('рік'))
)

YEAR = and_(
    gte(1000),
    lte(2100)
).interpretation(
    Date.year.custom(int)
)

YEAR_SHORT = and_(
    length_eq(2),
    gte(0),
    lte(99)
).interpretation(
    Date.year.custom(lambda _: 1900 + int(_))
)

ERA_YEAR = and_(
    gte(1),
    lte(100000)
).interpretation(
    Date.year.custom(int)
)

ERA_WORD = rule(
    eq('до'),
    or_(
        rule('н', eq('.'), 'е', eq('.').optional()),
        rule(normalized('наша'), normalized('ера'))
    )
).interpretation(
    Date.current_era.const(False)
)

DATE = or_(
    rule(
        DAY,
        '.',
        MONTH,
        '.',
        or_(
            YEAR,
            YEAR_SHORT
        ),
        YEAR_WORD.optional()
    ),
    rule(
        YEAR,
        YEAR_WORD
    ),
    rule(
        DAY,
        MONTH_NAME
    ),
    rule(
        MONTH_NAME,
        YEAR,
        YEAR_WORD.optional()
    ),
    rule(
        DAY,
        MONTH_NAME,
        YEAR,
        YEAR_WORD.optional()
    ),
    rule(
        ERA_YEAR,
        YEAR_WORD,
        ERA_WORD,
    )
).interpretation(
    Date
)
