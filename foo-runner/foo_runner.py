from tox.plugin import impl
from tox.tox_env.python.virtual_env.runner import VirtualEnvRunner
from tox.tox_env.register import ToxEnvRegister


class FooRunner(VirtualEnvRunner):

    @staticmethod
    def id() -> str:
        return "foo"


@impl
def tox_register_tox_env(register: ToxEnvRegister) -> None:
    register.add_run_env(FooRunner)
