#!/usr/bin/env python
# -*- coding: utf-8 -*-

import experiment_runner
experiment_runner.runExperiment("lmeds_explore",
                                "sequence.txt",
                                "english.txt",
                                disableRefresh=False,
                                audioExtList=[".mp3"],
                                videoExtList=[".mp4"],
                                allowUtilityScripts=True,
                                allowUsersToRelogin=True)
