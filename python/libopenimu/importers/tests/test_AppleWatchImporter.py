"""

    test_AppleWatchImporter
    @authors Dominic Létourneau, Simon Brière
    @date 30/05/2018

"""


import unittest
import numpy as np
import datetime
import libopenimu.importers.wimu as wimu
from libopenimu.importers.AppleWatchImporter import AppleWatchImporter
from libopenimu.models.Participant import Participant
from libopenimu.db.DBManager import DBManager


class AppleWatchImporterTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_load_file(self):
        pass

    def test_load_zip_file(self):
        # Testing

        manager = DBManager('applewatch.db', overwrite=True)
        participant = Participant(name='My Participant', description='Participant Description')
        manager.update_participant(participant)
        importer = AppleWatchImporter(manager, participant)

        results = importer.load('../../../resources/samples/AppleWatch.zip')
        # print('results', results)
        importer.import_to_database(results)