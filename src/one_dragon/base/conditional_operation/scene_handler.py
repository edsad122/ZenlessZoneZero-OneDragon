from typing import List, Optional

from one_dragon.base.conditional_operation.atomic_op import AtomicOp
from one_dragon.base.conditional_operation.state_handler import StateHandler


class SceneHandler:

    def __init__(self, interval_seconds: float, state_handlers: List[StateHandler]):
        self.interval_seconds: float = interval_seconds
        self.state_handlers: List[StateHandler] = state_handlers

    def get_operations(self, trigger_time: float) -> Optional[List[AtomicOp]]:
        """
        根据触发时间 和优先级 获取符合条件的场景下的指令
        :param trigger_time: 触发时间
        :return:
        """
        for sh in self.state_handlers:
            ops = sh.get_operations(trigger_time)
            if ops is not None:
                return ops
        return None

    def dispose(self) -> None:
        """
        销毁
        :return:
        """
        if self.state_handlers is not None:
            for handler in self.state_handlers:
                handler.dispose()
