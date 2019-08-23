# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
import os
import sys
import shutil
import fire
try:
    from dash.development.build_process import BuildProcess
except ModuleNotFoundError:
    print("you need to run `pip install dash` first", file=sys.stderr)
    sys.exit(1)


class DCC(BuildProcess):
    def __init__(self):
        super(DCC, self).__init__(
            self._concat(os.path.dirname(__file__), os.pardir),
            (("plotly.js-dist", None, "plotly.js", "plotly-{}.min.js"),),
        )
        self.asset_paths = self.asset_paths + (
            self._concat(self.main, "R"),
            self._concat(self.main, "inst"),
        )

    def _bundles_extra(self):
        shutil.copyfile(
            self._concat(self.main, "assets", "highlight.pack.js"),
            self._concat(self.build_folder, "highlight.pack.js"),
        )
        self.logger.info("copy the customized highligh js")


if __name__ == "__main__":
    fire.Fire(DCC)