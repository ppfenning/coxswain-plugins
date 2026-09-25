from agent_tools import sources

from coxswain_plugins.sources import asana, jira


def test_cox_finds_both_adapters_by_name_once_this_package_is_installed():
    assert (sources.adapter_for("jira"), sources.adapter_for("asana")) == (jira, asana)
