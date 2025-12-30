# app/extensions/db.py

"""
WHY THIS FILE EXISTS?
---------------------
This file creates ONE database object
which is reused everywhere.

मराठीत:
---------
ही file database ला connect करत नाही,
फक्त database चा object बनवते.
तो object पूर्ण app मध्ये वापरला जातो.
"""

from flask_sqlalchemy import SQLAlchemy

# Single DB object (IMPORTANT)
db = SQLAlchemy()

"""
WHY NOT CONNECT HERE?
---------------------
जर इथे connect केलं तर:
- Flask app अजून तयार झालेली नसते
- Circular import होतो
- Production मध्ये error येतो

म्हणून:
DB object वेगळा
DB initialization वेगळं
"""
