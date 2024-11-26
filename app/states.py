from FeatureCloud.app.engine.app import AppState, app_state, Role
import app.shepherd as shepherd
from FeatureCloud.app.engine.app import AppState, app_state


@app_state("initial")
class ExecuteState(AppState):

    def register(self):
        self.register_transition("terminal", Role.BOTH)

    def run(self):
        shepherd.main()
        return "terminal"
