from stock_tracker import StockTracker

stock_tracker = StockTracker()
percent_difference = stock_tracker.get_percent_difference()
if percent_difference >= 5:
    stock_tracker.get_news()
    stock_tracker.notify()
