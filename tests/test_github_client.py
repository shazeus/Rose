import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "launcher" / "update" / "github_client.py"
SPEC = importlib.util.spec_from_file_location("github_client_under_test", MODULE_PATH)
github_client = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(github_client)


def test_release_api_defaults_to_aurelia_fork(monkeypatch):
    monkeypatch.delenv("AURELIA_RELEASE_API", raising=False)
    monkeypatch.delenv("AURELIA_RELEASE_REPO", raising=False)

    assert github_client.GITHUB_RELEASE_API == "https://api.github.com/repos/aurelia/Aurelia/releases/latest"
    assert github_client.get_release_api_url() == "https://api.github.com/repos/aurelia/Aurelia/releases/latest"


def test_release_api_accepts_repo_override(monkeypatch):
    monkeypatch.delenv("AURELIA_RELEASE_API", raising=False)
    monkeypatch.setenv("AURELIA_RELEASE_REPO", "example/Fork")

    assert github_client.get_release_api_url() == "https://api.github.com/repos/example/Fork/releases/latest"


def test_release_api_accepts_full_url_override(monkeypatch):
    monkeypatch.setenv("AURELIA_RELEASE_API", "https://example.test/releases/latest")
    monkeypatch.setenv("AURELIA_RELEASE_REPO", "example/Fork")

    assert github_client.get_release_api_url() == "https://example.test/releases/latest"
