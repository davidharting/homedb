select
    t.id,
    t.date,
    t.amount / 1000 as amount,
    t.memo,
    case
        when transaction_id is not null then true
        else false
    end as has_parent,
    transaction_id as parent_transaction_id,
    case
        t.cleared
        when 'uncleared' then false
        when 'cleared' then true
        else false
    end as is_cleared,
    approved as is_approved,
    case
        when amount > 0 then true
        else false
    end as is_income,
    case
        when amount < 0 then true
        else false
    end as is_expense,
    flag_color,
    account_id,
    account_name,
    payee_id,
    payee_name,
    category_id,
    category_name,
    transfer_account_id,
    transfer_transaction_id,
    extract(year from date) as year,
    extract(month from date) as month,
    extract(day from date) as day_of_month,
    extract(dayofweek from date) as day_of_week,
    extract(dayofyear from date) as day_of_year,
    extract(week from date) as week_of_year,
    extract(quarter from date) as quarter_of_year
from
    `sodium-hangar-272923`.source.ynab_transactions as t
where
    deleted = false
