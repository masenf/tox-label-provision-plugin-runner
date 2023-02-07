When a tox environment has a runner derived from a plugin that is named in the `requires` key,
the environment cannot appear in a top-level label expression.

# dummy plugin

This plugin registers a virtualenv runner called "foo", but otherwise does
nothing else.

Source in [`./foo-runner`](./foo-runner). The wheel and pre-cached index are
already built in [`./index`](./index).

# repro

```
export PIP_EXTRA_INDEX_URL=file://$(realpath $(pwd))/index/simple
```

## Using `envlist`

```
tox
```

```
ROOT: will run in automatically provisioned tox, host /home/mfurer/.pytools/bin/python is missing [requires (has)]: foo-runner
ROOT: provision> .tox/.tox/bin/python -m tox
bar: OK ✔ in 0.14 seconds
  bar: OK (0.14 seconds)
  baz: OK (0.01 seconds)
  congratulations :) (0.53 seconds)
```

## Using `labels`

```
tox -m foo
```

```
ROOT: will run in automatically provisioned tox, host /home/mfurer/.pytools/bin/python is missing [requires (has)]: foo-runner
Traceback (most recent call last):
  File "/home/mfurer/.pytools/bin/tox", line 8, in <module>
    sys.exit(run())
  File "/home/mfurer/.pytools/lib/python3.8/site-packages/tox/run.py", line 19, in run
    result = main(sys.argv[1:] if args is None else args)
  File "/home/mfurer/.pytools/lib/python3.8/site-packages/tox/run.py", line 41, in main
    result = provision(state)
  File "/home/mfurer/.pytools/lib/python3.8/site-packages/tox/provision.py", line 126, in provision
    return run_provision(provision_tox_env, state)
  File "/home/mfurer/.pytools/lib/python3.8/site-packages/tox/provision.py", line 144, in run_provision
    tox_env: PythonRun = cast(PythonRun, state.envs[name])
  File "/home/mfurer/.pytools/lib/python3.8/site-packages/tox/session/env_select.py", line 337, in __getitem__
    return self._defined_envs[item].env
  File "/home/mfurer/.pytools/lib/python3.8/site-packages/tox/session/env_select.py", line 233, in _defined_envs
    self._mark_active()
  File "/home/mfurer/.pytools/lib/python3.8/site-packages/tox/session/env_select.py", line 321, in _mark_active
    self._defined_envs_[env_name].is_active = True
KeyError: 'bar'
```
