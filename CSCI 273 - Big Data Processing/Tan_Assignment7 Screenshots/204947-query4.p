/* Jeremy Tan Query 4: Find the top 10 rated products by product title */


data = LOAD 'gs://csci273_tan/amazon_reviews_us_Wireless_v1_00.tsv.gz' AS (marketplace:chararray, customer_id:chararray, review_id:chararray, product_id:chararray, product_parent:chararray, product_title:chararray, product_category:chararray, star_rating:int, helpful_votes:int, total_votes:int, vine:chararray, verified_purchase:chararray, review_headline:chararray, review_body:chararray, review_date:chararray);

A = FILTER data BY star_rating == 5;
B = GROUP A BY (product_parent, product_title);
C = FOREACH B GENERATE 
    group.product_parent AS product_parent,
    group.product_title AS product_title,
    COUNT(A) AS five_star_count;
D = ORDER C BY five_star_count DESC;
E = LIMIT D 10;
DUMP E;