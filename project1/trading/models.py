from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length = 10, unique = True, db_index=True)
    name = models.CharField(max_length = 100)
    sector = models.CharField(max_length=50)
    market_cap = models.BigIntegerField()
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
class priceData(models.Model):
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='prices')
    date = models.DateField()
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    adj_close_price = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True)
    volume = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class momentumScore(models.Model):
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='scores')
    calculated_date = models.DateField()
    score = models.DecimalField(max_digits=10, decimal_places=2)
    rank = models.IntegerField(null = True, blank=True)
    quantile = models.DecimalField(max_digits=5, decimal_places=2)
    is_top_quantile = models.BooleanField(default = False)
    period_start_date = models.DateField()
    period_end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
class TradingSignal(models.Model):
    SIGNAL_TYPE = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
        ('HOLD', 'Hold'),
    ]
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='signals')
    signal_date = models.DateField()
    signal_type = models.CharField(max_length=10, choices=SIGNAL_TYPE)
    score = models.DecimalField(max_digits=10, decimal_places=2)
    trade_quality = models.IntegerField()
    target_value = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True) 
    reason = models.TextField(blank=True, null=True)
    is_executed = models.BooleanField(default = False)
    executed_at = models.DateTimeField(null = True, blank=True)
    execution_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    confidence = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "trading_signals"
        ordering = ['-signal_date', '-created_at']
        indexes = [models.Index(fields = ['signal_date', 'signal_type', 'is_executed'])]
class Rebalance(models.Model):
    date = models.DateField(unique = True, db_index = True)
    total_stocks_analyzed = models.IntegerField()
    buy_signals_analyzed = models.IntegerField()
    sell_signals_analyzed = models.IntegerField()
    hold_signals_analyzed = models.IntegerField()
    total_portfolio_value = models.DecimalField(max_digits=15, decimal_places=2, null = True, blank = False)
    execution_status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending'),
            ('COMPLETED', 'Completed'),
            ('FAILED', 'Failed'),
        ],
        default='PENDING'
    )
    executed_at = models.DateTimeField(null = True, blank=True)
    error_message = models.TextField(null = True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)