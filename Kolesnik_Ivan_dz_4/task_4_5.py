import sys
import task_4_2 as t42

_, currency = sys.argv
print(*t42.currency_rates(currency), sep=', ')
