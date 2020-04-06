select
    year,
    month,
    sum(case when is_income = true then amount else 0 end) as income,
    sum(case when is_expense = true then (0 - amount) else 0 end) as expense,
    sum(case when is_income then amount else 0 end) - sum(case when is_expense then 0 - amount else 0 end) as cashflow
from {{ ref('transactions') }}
group by year, month
