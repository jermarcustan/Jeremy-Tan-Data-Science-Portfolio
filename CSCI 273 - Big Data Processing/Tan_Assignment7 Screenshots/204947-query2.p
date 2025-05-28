/* Jeremy Tan Query 2: Find the top 10 products that have the most individual votes*/

data = LOAD 'gs://csci273_tan/amazon_reviews_us_Wireless_v1_00.tsv.gz' AS (marketplace:chararray, customer_id:chararray, review_id:chararray, product_id:chararray, product_parent:chararray, product_title:chararray, product_category:chararray, star_rating:int, helpful_votes:int, total_votes:int, vine:chararray, verified_purchase:chararray, review_headline:chararray, review_body:chararray, review_date:chararray);

A = GROUP data BY product_title;
B = FOREACH A GENERATE 
    group AS product_title,
    COUNT(data) AS voter_count;
C = ORDER B BY voter_count DESC;
D = LIMIT C 10;
DUMP D;
