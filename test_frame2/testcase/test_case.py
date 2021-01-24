from test_frame2.app import App


def test_search():
    app = App()
    app.start().goto_main().goto_market_page().goto_search().search()

