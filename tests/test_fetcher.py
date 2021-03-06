import requests
from webwatcher.fetcher import fetch


def test_server_is_alive(target):
    """Sanity check, that test environment is properly setup"""
    response = requests.get("http://{0}:{1}/index.html".format(*target))
    assert response.status_code == 200


def test_simple_fetcher(target, json_conf):
    ok, content = fetch(json_conf)
    assert ok is True
    assert content == (
        '{\n'
        ' "key": "value"\n'
        '}'
    )


def test_browser_text_fetcher(target, html_text_conf):
    html_text_conf.update({
        'tag': 'div',
    })
    ok, content = fetch(html_text_conf)
    assert ok is True
    assert content == 'Hello world!'


def test_browser_xpath(target, html_text_conf):
    html_text_conf.update({
        'xpath': '//*[contains(@class, "footer")]',
    })
    ok, content = fetch(html_text_conf)
    assert ok is True
    assert content == 'Footer content'


def test_scenario(target, html_text_conf):
    html_text_conf.update({
        'scenario': 'driver.find_element_by_id("page-link").click()'
    })
    ok, content = fetch(html_text_conf)
    assert ok is True
    assert content == 'Another page'
