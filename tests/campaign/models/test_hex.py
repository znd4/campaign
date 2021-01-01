import pytest
from sqlalchemy.orm import SessionLocal

import campaign.api as api
import campaign.db as db


def test_hex():
    """Make sure that hex.from_orm works"""
    db_hex0 = db.models.Hex()
    api.models.Hex.from_orm(db.models.Hex(neighbors=[None, None, None, None]))
