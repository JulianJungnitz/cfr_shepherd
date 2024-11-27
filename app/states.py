from FeatureCloud.app.engine.app import AppState, app_state, Role
import shepherd as shepherd
from FeatureCloud.app.engine.app import AppState, app_state


@app_state("initial")
class ExecuteState(AppState):

    def register(self):
        self.register_transition("terminal", Role.BOTH)

    def run(self):
        print("Running app state: initial")
        shepherd.main()
        return "terminal"
