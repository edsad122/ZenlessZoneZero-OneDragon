from typing import Optional, Callable

from one_dragon.base.operation.application_base import Application
from one_dragon.base.operation.application_run_record import AppRunRecord
from one_dragon.base.operation.operation_base import OperationResult
from zzz_od.context.zzz_context import ZContext
from zzz_od.operation.enter_game import OpenAndEnterGame


class ZApplication(Application):

    def __init__(self, ctx: ZContext, app_id: str,
                 node_max_retry_times: int = 1,
                 op_name: str = None,
                 timeout_seconds: float = -1,
                 op_callback: Optional[Callable[[OperationResult], None]] = None,
                 check_game_win: bool = True,
                 init_context_before_start: bool = True,
                 stop_context_after_stop: bool = True,
                 run_record: Optional[AppRunRecord] = None):
        self.ctx: ZContext = ctx
        op_to_enter_game = OpenAndEnterGame(ctx)
        Application.__init__(self,
                             ctx=ctx, app_id=app_id,
                             node_max_retry_times=node_max_retry_times,
                             op_name=op_name,
                             timeout_seconds=timeout_seconds,
                             op_callback=op_callback,
                             check_game_win=check_game_win,
                             op_to_enter_game=op_to_enter_game,
                             init_context_before_start=init_context_before_start,
                             stop_context_after_stop=stop_context_after_stop,
                             run_record=run_record
                             )

    def handle_resume(self) -> None:
        self.ctx.controller.active_window()
