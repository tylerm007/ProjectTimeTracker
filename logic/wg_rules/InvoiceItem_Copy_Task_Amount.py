
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.copy(derive=InvoiceItem.task_amount, from_parent=Task.total_task_amount_billed)
