from django.db import models
from trading.models import Stock

class Portfolio(models.Model):
    name = models.CharField()
    description = models.TextField()
    initial_capital = models.DecimalField(max_digits=15, decimal_places=2)
    current_value = models.DecimalField(max_digits=15, decimal_places=2)
    total_value = models.DecimalField(max_digits = 15, decimal_places = 2, default=0)
    snaptrade_user_id = models.CharField(max_length=100, blank=True)
    snaptrade_portfolio_id = models.CharField(max_length=100, blank=True)
    snaptrade_user_secret = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "portfolios"
        ordering = ['-created_at']

class Position(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='positions')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='positions')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    average_cost = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unrealized_pl = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unrealized_pl_pct = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_value = models.DecimalField(max_digits = 10, decimal_places = 2, default=0)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "positions"
        unique_together = ('portfolio', 'stock')
        ordering = ['-current_value']
        

class Trade(models.Model):
    ORDER_TYPE_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUBMITTED', 'Submitted'),
        ('FILLED', 'Filled'),
        ('PARTIALLY_FILLED', 'Partially Filled'),
        ('CANCELLED', 'Cancelled'),
        ('REJECTED', 'Rejected'),
    ]
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='trades')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='trades')
    order_type = models.CharField(max_length=10, choices=ORDER_TYPE_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    execution_date = models.DateTimeField(auto_now_add=True)
    filled_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    filled_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    external_order_id = models.CharField(max_length=100, blank=True)
    snaptrade_order_id = models.CharField(max_length=100, blank=True)
    commission = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    error_message = models.TextField(null=True, blank=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    filled_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    rejected_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "trades"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields = ['status']),
            models.Index(fields = ['created_at'])
        ]
        

class PerformanceMetric(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='performance_metrics')
    date = models.DateField()
    total_value = models.DecimalField(max_digits=15, decimal_places=2)
    cash_value = models.DecimalField(max_digits=15, decimal_places=2)
    position_value = models.DecimalField(max_digits=15, decimal_places=2)
    daily_return = models.DecimalField(max_digits=15, decimal_places=2)
    cumilative_return = models.DecimalField(max_digits=15, decimal_places=2)
    total_return = models.DecimalField(max_digits=15, decimal_places=2)
    winning_trades = models.IntegerField()
    losing_trades = models.IntegerField()
    total_trades = models.IntegerField()
    win_rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "performance_metrics"
        unique_together = ('portfolio', 'date')
        ordering = ['-date']
        indexes = [
            models.Index(fields = ['portfolio', 'date']),
        ]