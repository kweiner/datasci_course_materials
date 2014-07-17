select v from (
    select a.row_num as i, b.col_num as j, sum(a.value * b.value) as v
    from a, b
    where a.col_num = b.row_num
    group by a.row_num, b.col_num
) where i=2 and j=3;
