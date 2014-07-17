select tf from (
select a.x as i, b.y as j, sum(a.count * b.count) as tf
    from (select docid as x, term as y, count from frequency) a, (select term as x, docid as y, count from frequency) b
    where a.y = b.x
    and (a.x='10080_txt_crude' or b.y='10080_txt_crude' or a.x='17035_txt_earn' or b.y='17035_txt_earn')
    group by a.x, b.y
) where j='10080_txt_crude' and i='17035_txt_earn';
