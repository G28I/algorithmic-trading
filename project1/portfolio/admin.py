from django.contrib import admin
from portfolio.models import Portfolio, Position, Trade, PerformanceMetric

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'initial_capital', 'current_value', 'total_value', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['portfolio', 'stock', 'quantity', 'average_cost', 'current_price', 'current_value', 'unrealized_pl', 'unrealized_pl_pct', 'total_value', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'updated_at']
    search_fields = ['portfolio__name', 'stock__name']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ['portfolio', 'stock', 'order_type', 'quantity', 'price', 'execution_date', 'filled_quantity', 'filled_price', 'order_value', 'status', 'external_order_id', 'snaptrade_order_id', 'commission', 'error_message', 'submitted_at', 'filled_at', 'cancelled_at', 'rejected_at', 'created_at', 'updated_at']
    list_filter = ['status', 'order_type', 'execution_date', 'created_at', 'updated_at']
    search_fields = ['portfolio__name', 'stock__name', 'external_order_id', 'snaptrade_order_id']
    ordering = ['-created_at']
    readonly_fields = ['execution_date', 'order_value', 'commission', 'error_message', 'submitted_at', 'filled_at', 'cancelled_at', 'rejected_at']
    date_hierarchy = 'execution_date'

@admin.register(PerformanceMetric)
class PerformanceMetricAdmin(admin.ModelAdmin):
    list_display = ['portfolio', 'date', 'total_value', 'cash_value', 'position_value', 'daily_return', 'cumilative_return', 'total_return', 'winning_trades', 'losing_trades', 'total_trades', 'win_rate', 'created_at', 'updated_at']
    list_filter = ['date', 'created_at', 'updated_at']
    search_fields = ['portfolio__name']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'date'
    ordering = ['-date']