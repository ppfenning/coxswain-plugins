# coxswain-plugins

Coxswain integrations that name a vendor. Coxswain's core repositories stay free of any vendor or employer
name, and their CI enforces it. Each integration here registers under an entry-point group that core looks
up by name, so installing this package beside `cox` is all it takes:

```sh
uv tool install coxswain-tools --with "coxswain-plugins @ git+https://github.com/ppfenning/coxswain-plugins"
```

| Kind | Entry-point group | Plugins |
| --- | --- | --- |
| Intake sources for `cox route pull` | `coxswain.sources` | `jira`, `asana` |
| System-one backends for coxswain-graphs | `coxswain.system_one` | `jev` (`pip install "coxswain-plugins[jev]"`) |

Runners are planned to register here too (Coxswain roadmap 0.18.0).

## System-one backends

`jev` is TypeSafe AI's hosted System One model: typed yes/no, choice and score answers with calibrated
confidence, over up to 64K tokens of state. Configure it in a provider profile's `system_one:` block with
`backend: jev`, a pinned `model` (e.g. `jev-1.13.0`) and `key_env`, the environment variable that holds
the TypeSafe key. Graphs reads the key from `key_env` only, never the provider's own key, and runs the
backend in shadow until `cox stats system-one` says it has graduated.

## Intake sources

An adapter reads a tracker and files intake tickets. It never moves a tracker's state; its one write back
is a comment naming the intake file. The token is read from the environment variable the profile's
`sources.<name>.token_env` names; the value is never stored.

| Source | Listing | Filter (`sources.<name>.filter`) | Token |
| --- | --- | --- | --- |
| `jira` | Jira Data Center `/rest/api/2/search` (Cloud's basic auth is not handled) | `status:<name>` or `label:<name>` | `JIRA_TOKEN` |
| `asana` | `https://app.asana.com/api/1.0/tasks?project=<gid>`; repos are project gids | `tag:<name>` or `section:<name>` (default `tag:intake`) | the profile's `token_env` |

These adapters moved here from `ppfenning/coxswain-sources`, now archived.
