from django.contrib import admin
from trading.models import Stock, priceData, momentumScore, TradingSignal, Rebalance

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'name', 'asset_type', 'market', 'is_active', 'created_at', 'updated_at']
    list_filter = ['asset_type', 'market', 'is_active', 'created_at', 'updated_at']
    search_fields = ['symbol', 'name']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']

@admin.register(priceData)
class priceDataAdmin(admin.ModelAdmin):
    list_display = ['ticker', 'date', 'open', 'high', 'low', 'close', 'volume', 'is_active']
    list_filter = ['ticker', 'date', 'is_active', 'created_at', 'updated_at']
    search_fields = ['stock_ticker']
    date_hierarchy = 'date'
    readonly_fields = ['created_at', 'updated_at']

@admin.register(momentumScore)
class momentumScoreAdmin(admin.ModelAdmin):
    list_display = ['ticker', 'calculated_date', 'score', 'rank', 'quantile', 'is_top_quantile', 'created_at', 'updated_at']
    list_filter = ['calculated_date', 'quantile', 'is_top_quantile', 'created_at', 'updated_at']
    search_fields = ['stock_ticker']
    date_hierarchy = 'calculated_date'
    readonly_fields = ['created_at', 'updated_at']

@admin.register(TradingSignal)
class TradingSignalAdmin(admin.ModelAdmin):
    list_display = ['ticker', 'signal_date', 'signal_type', 'score', 'rank', 'quantile', 'is_top_quantile', 'created_at', 'updated_at']
    list_filter = ['signal_date', 'signal_type', 'is_top_quantile', 'created_at', 'updated_at']
    search_fields = ['stock_ticker']
    date_hierarchy = 'signal_date'
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Rebalance)
class RebalanceAdmin(admin.ModelAdmin):
    list_display = ['date','execution_status', 'total_stocks_analyzed', 'buy_signal_generated', 'sell_signal_generated', 'created_at', 'updated_at']
    list_filter = ['date', 'execution_status','buy_signal_generated','sell_signal_generated']
    search_fields = ['date', 'execution_status']
    date_hierarchy = 'date'
    readonly_fields = ['created_at', 'updated_at']