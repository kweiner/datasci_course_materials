create view if not exists frequency2 as SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

select j, tf from (
select a.x as i, b.y as j, sum(a.count * b.count) as tf
    from (select docid as x, term as y, count from frequency2) a, (select term as x, docid as y, count from frequency2) b
    where a.y = b.x
    and (a.x='q' or b.y='q')
    group by a.x, b.y
) where i='q' order by tf desc limit 1;
