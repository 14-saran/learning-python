# Decorator ตรวจสอบวงเงินก่อนทำธุรกรรม   #กลับมาทวนด้วย#
from dataclasses import fields


def check_balance(min_balance):
    def decorator(func):
        def wrapper(account, amount, *args, **kwargs):
            if account['balance'] < min_balance:
                print("❌ วงเงินไม่พอ ทำรายการไม่ได้")
                return
            return func(account, amount, *args, **kwargs)
        return wrapper
    return decorator

@check_balance(min_balance=100)
def withdraw(account, amount):
    account['balance'] -= amount
    print(f"✅ ถอนเงิน {amount} บาท, คงเหลือ {account['balance']} บาท")

# ทดลองใช้
acc = {'balance': 80}
withdraw(acc, 50)

acc['balance'] = 500
withdraw(acc, 200)

print('----------------------------------------------------------')

#Decorator บวก Vat/Tax อัตโนมัติ
def add_vat(rate=0.07):
    def decorator(func):
        def wrapper(price, *args, **kwargs):
            total = price * (1 + rate)
            print(f"ราคา {price} + VAT {rate*100}% = {total:.2f}")
            return func(total, *args, **kwargs)
        return wrapper
    return decorator

@add_vat(0.1)  # VAT 10%
def pay(amount):
    print(f"💰 ชำระเงิน {amount} บาท")

pay(1000)


print('----------------------------------------------------------')

#Decorator ในการ "รับรู้รายได้"
def require_active_subscription(func):
    def wrapper(self, *args, **kwargs):
        if self.state != 'active':
            raise KeyError("Subscription ยังไม่ active")
        return func(self, *args, **kwargs)
    return wrapper

def log_monthly_recognition(func):
    def wrapper(self, *args, **kwargs):
        _logger.info(f"[Subscription Revenue] Sub: {self.name}, Month: {fields.Date.today().month}, By user: {self.env.user.name}") # type: ignore
        return func(self, *args, **kwargs)
    return wrapper

class SaleSubscription(models.Model): # type: ignore
    _inherit = 'sale.subscription'

    @require_active_subscription
    @log_monthly_recognition
    def action_recognize_monthly_revenue(self):
        """ รับรู้รายได้ของเดือนนี้ """
        # Logic:
        # 1. เช็คว่ารอบนี้ถึงรอบรับรู้หรือยัง
        # 2. สร้าง journal entry
        # 3. เปลี่ยนสถานะ revenue_recognized = True
        journal = self.env['account.journal'].search([('type','=','general')], limit=1)
        move = self.env['account.move'].create({
            'journal_id': journal.id,
            'move_type': 'entry',
            'ref': f'Revenue Recognition {self.name} {fields.Date.today()}',
            'line_ids': [
                (0, 0, {
                    'name': 'Revenue',
                    'account_id': self.product_id.categ_id.property_account_income_categ_id.id,
                    'debit': 0.0,
                    'credit': self.recurring_total,
                }),
                (0, 0, {
                    'name': 'Deferred Revenue',
                    'account_id': self.env.ref('account.data_account_type_deferred_revenue').id,
                    'debit': self.recurring_total,
                    'credit': 0.0,
                }),
            ],
        })
        move.post()
        self.revenue_recognized_months += 1
