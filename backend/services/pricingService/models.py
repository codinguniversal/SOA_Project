from database import db

class PricingRule(db.Model):
    __tablename__ = 'pricing_rules'

    rule_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, nullable=False)
    min_quantity = db.Column(db.Integer, nullable=False)
    discount_percentage = db.Column(db.Numeric(5, 2), nullable=False)

class TaxRate(db.Model):
    __tablename__ = 'tax_rates'

    region = db.Column(db.String(50), primary_key=True)
    tax_rate = db.Column(db.Numeric(5, 2), nullable=False)