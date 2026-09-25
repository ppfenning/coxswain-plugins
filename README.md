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

System-one backends and runners are planned to register here too (Coxswain roadmap 0.18.0).

## Intake sources

An adapter reads a tracker and files intake tickets. It never moves a tracker's state; its one write back
is a comment naming the intake file. The token is read from the environment variable the profile's
`sources.<name>.token_env` names; the value is never stored.

| Source | Listing | Filter (`sources.<name>.filter`) | Token |
| --- | --- | --- | --- |
| `jira` | Jira Data Center `/rest/api/2/search` (Cloud's basic auth is not handled) | `status:<name>` or `label:<name>` | `JIRA_TOKEN` |
| `asana` | `https://app.asana.com/api/1.0/tasks?project=<gid>`; repos are project gids | `tag:<name>` or `section:<name>` (default `tag:intake`) | the profile's `token_env` |

These adapters moved here from `ppfenning/coxswain-sources`, now archived.
