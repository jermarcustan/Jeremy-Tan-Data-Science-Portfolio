/* Jeremy Tan Query 1: Find the top 5 customers that made the most verified purchases*/

data = LOAD 'gs://csci273_tan/amazon_reviews_us_Wireless_v1_00.tsv.gz' AS (marketplace:chararray, customer_id:chararray, review_id:chararray, product_id:chararray, product_parent:chararray, product_title:chararray, product_category:chararray, star_rating:int, helpful_votes:int, total_votes:int, vine:chararray, verified_purchase:chararray, review_headline:chararray, review_body:chararray, review_date:chararray);

A = FILTER data BY verified_purchase == 'Y';
B = GROUP A BY customer_id;
C = FOREACH B GENERATE 
    group AS customer_id,
    COUNT(A) AS purchase_count;
D = ORDER C BY purchase_count DESC;
E = LIMIT D 5;
DUMP E;
