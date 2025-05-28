ADD JAR gs://csci273_tan/json-serde-1.3.8-jar-with-dependencies.jar;

DROP TABLE IF EXISTS tweets;
CREATE EXTERNAL TABLE tweets (
	interactions array<struct<
		demographic:struct<
			gender:string
		>,
		interaction:struct<
			author:struct<
				username:string,
				name:string,
				id:string
			>,
			id:bigint
		>,
		klout:struct<
			score:int
		>
	>>
)

ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 'gs://csci273_tan/KloutScore/';

-- Now query to get the top 5 authors by Klout score

SELECT 
  interaction_struct.interaction.author.username AS username,
  SUM(interaction_struct.klout.score) AS total_klout_score
FROM 
  tweets
  LATERAL VIEW EXPLODE(interactions) exploded_interactions AS interaction_struct
GROUP BY 
  interaction_struct.interaction.author.username
ORDER BY 
  total_klout_score ASC
LIMIT 5;