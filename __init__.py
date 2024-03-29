# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool

from . import account

def register():
    Pool.register(
        module='account_us', type_='model')
    Pool.register(
        account.CreateChart,
        module='account_us', type_='wizard')
