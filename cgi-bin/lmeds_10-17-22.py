#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import experiment_runner
experiment_runner.runExperiment("lmeds_10-17-22",
                                "sequence.txt",
                                "english.txt",
				individualSequences=True,
                                disableRefresh=False,
                                audioExtList=[".ogg", ".mp3"],
                                videoExtList=[".ogg", ".mp4"],
                                allowUtilityScripts=True,
                                allowUsersToRelogin=True)