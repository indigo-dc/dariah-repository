# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Test Zenodo Deposit API."""

from __future__ import absolute_import, print_function

from copy import deepcopy

from helpers import publish_and_expunge


def test_basic_deposit_edit(app, db, communities, deposit, deposit_file):
    """Test simple deposit publishing."""
    deposit = publish_and_expunge(db, deposit)
    pid, record = deposit.fetch_published()
    initial_oai = deepcopy(record['_oai'])

    # Create some potential corruptions to protected fields
    deposit = deposit.edit()
    deposit['_files'][0]['bucket'] = record['_buckets']['deposit']
    deposit['_oai'] = {}
    deposit = publish_and_expunge(db, deposit)
    pid, record = deposit.fetch_published()
    assert record['_oai'] == initial_oai
    assert record['_files'][0]['bucket'] == record['_buckets']['record']
