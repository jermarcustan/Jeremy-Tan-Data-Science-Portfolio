/* Jeremy Tan Query 3: Find the top 5 customers of the top 10 products with the highest ratings */

data = LOAD 'gs://csci273_tan/amazon_reviews_us_Wireless_v1_00.tsv.gz' AS (marketplace:chararray, customer_id:chararray, review_id:chararray, product_id:chararray, product_parent:chararray, product_title:chararray, product_category:chararray, star_rating:int, helpful_votes:int, total_votes:int, vine:chararray, verified_purchase:chararray, review_headline:chararray, review_body:chararray, review_date:chararray);

A = GROUP data BY product_title;
B = FOREACH A GENERATE 
    group AS product_title,
    AVG(data.star_rating) AS avg_rating;
C = ORDER B BY avg_rating DESC;
D = LIMIT C 10;
E = JOIN data BY product_title, D BY product_title;
F = GROUP E BY customer_id;
G = FOREACH F GENERATE
    group AS customer_id,
    COUNT(E) AS customer_count;
H = ORDER G BY customer_count DESC;
I = LIMIT H 5;
DUMP I;