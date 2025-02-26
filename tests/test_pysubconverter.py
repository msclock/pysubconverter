from __future__ import annotations

from concurrent.futures import Future, ProcessPoolExecutor, as_completed

from pysubconverter import config_context, subconverter


def _convert(arguments: dict[str, str]) -> str:
    with config_context():
        return subconverter(arguments)


def test_subconverter():
    """Convert basic subscripition links to clash format."""
    fake_sub = [
        "ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@127.0.0.1:0123#fake 1",
        "ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@127.0.0.1:0123#fake 2",
        "ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@127.0.0.1:0123#fake 3",
    ]
    arguments: dict[str, str] = {
        "target": "clash",
        "url": "|".join(fake_sub),
    }
    result = _convert(arguments)
    assert "proxies" in result
    assert "fake 1" in result
    assert "fake 2" in result
    assert "fake 3" in result


def test_multi_process_convert():
    """Mulit process conversion test."""
    with ProcessPoolExecutor(max_workers=4) as executor:
        f_to_index: dict[Future[str], int] = {}
        for i in range(2):
            arguments = {
                "target": "clash",
                "url": f"ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@127.0.0.1:0123#fake {i}",
            }
            f_to_index[executor.submit(_convert, arguments)] = i
        for f in as_completed(f_to_index):
            result = f.result()
            assert "proxies" in result
            assert f"fake {f_to_index[f]}" in result
