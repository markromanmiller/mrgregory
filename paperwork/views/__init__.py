"""
Module for all the paperwork views. They are split into three main groups,
clients, deliverables, and tasks. There are others.
"""

from paperwork.views.clients import client_info_types, view_clients
from paperwork.views.deliverables import view_deliverables, \
    new_deliverable, view_deliverable
from paperwork.views.tasks import view_tasks, dpc, make_tasks
from paperwork.views.server import home, login_page
