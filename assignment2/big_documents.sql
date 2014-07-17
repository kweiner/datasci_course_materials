select count(*) from (
    select docid, sum(count) as num_terms from frequency group by docid having sum(count) > 300
) x;

