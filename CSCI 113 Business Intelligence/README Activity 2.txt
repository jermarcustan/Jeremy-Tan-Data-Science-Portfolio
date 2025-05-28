Activity 2: OLAP Design
Members: 
* Alegarbes, Brynx Junil
   * Added dimension tables
   * Contributed fact tables
   * Organizing and Structuring the placement of the tables
* Deekimcheng, Michael Kenard
   * Wrote Readme.txt
   * Edited some attributes in the tables
* Felipe, Harvey
   * Fixed some of the tables
   * Designed the layout of the schema
* Lee, Ellyn
   * Added tables
   * Organizing and structuring 
   * Conceptualized and designed the OLAP schema
* Tan, Jeremy Marcus
   * Added dimension and fact tables
   * Wrote Readme.txt


README.TXT
Before reading, untouched paragraphs means that tables have been explained (you can read through it). Suggestions highlighted in yellow with comments.


Dimensions:
Branch: This dimension table contains information about all the branches in the organization, including their general name, account_type, branch_key (for unique identification), the cluster they belong to, and the area they are located in. The information above can identify which branch belonged to a specific area or cluster.


Cluster: This dimension table contains information about all the clusters in the organization, including the region name, cluster key, and area key. This information can be used to group branches together and analyze data by cluster. The cluster key can link to the branches that make up the cluster. The area key can identify which area the cluster belongs to.


Area: This dimension table contains information about all the areas in the organization, including the area key, name, and branch key. This information can be used to group branches together and analyze data by area.


Client: This dimension table contains information about all the clients in the organization, including the client key, first name, last name, savings account key, insurance account key, and equity account key. The first three identifies the user who owns the accounts. Furthermore, each of the latter three attributes map the user to their respective accounts. The information can be used to group accounts for each client.


Time: This dimension table contains relevant information regarding the time of a transaction. The data includes time_key, day (referring to the day of the month), day of the week, week of the month, month, quarter, and year. The data can be grouped to access date-specific transactional information for a client, branch, cluster, or area.


Deposits/ Withdrawals: These two dimension tables contain information on the amount of money a client has deposited or withdrawn from his or her account. The attributes of each table include deposit_key or withdrawal_key, the unique identifier, the client_key, which links the account to the owner’s information, the account_key, which specifies the account of the client in which the transaction was made, the branch_key, and the amount of the transaction. These dimension tables will enable the analyst to gather insights on the transactions of a client. The data on deposits and withdrawals are separated into two different tables to make it easier to analyze the data on deposits or withdrawals only. 


Account: This dimension table condenses and organizes the information from the deposit and withdrawal tables. It assigns a unique account_key for each account in the organization’s database; this account_key contains an identifier for the type of account: savings, insurance, or equity. This account key will be a universal identifier for any account type, which the company can use in any specific query. For instance, the organization can analyze the daily branch performance per account type on a given date. 


Savings/Insurance/Equity Accounts: These three dimension tables contain all relevant information regarding the three possible types of accounts a client may possess with the organization. Each of the three dimension tables have a unique primary key, and contain information about the current balance and running balance inside the account, the branch_key where the account was opened, and the client_key of the owner. This information can be used to analyze the percentage of capital a client allocates and transfers between the three types of accounts. Moreover, the data can be used to compare the balances of different clients in a certain type of account. 




Facts:
Transaction Fact Table: This fact table contains information about all the transactions made by clients for a given day, including the branch key, cluster key, area key, client key, day, amount, transaction type, account key, and the starting and ending balance of the account. This information can group data based on client key, and thus be used to analyze daily transaction volumes, as well as to track changes in account balances over time.


Savings Balance Fact Table: This fact table contains information about the savings balance of each client per month, including the month, the client key, and the current balance and running balance of the client. This information can be used to track changes in savings balances over time and compare the savings balances of different clients.


Insurance Balance Fact Table: This fact table contains information about the insurance balance of each client per month, including the month, the client key, the current balance, and the running balance. This information can be used to track changes in insurance balances over time and compare the insurance balances of different clients.


Equity Balance Fact Table: This fact table contains information about the equity balance of each client per month, including the month, the client key, the current balance and the running balance. This information can be used to track changes in equity balances over time and compare the equity balances of different clients.


Client Insurance Deposits: This fact table contains information about the number of insurance deposits made by each client per week, including the time key (which links to the week of the month), the client key, account key, linked to the insurance account, deposit key, and using a count function, the number of deposits. This information can be used to track changes in the frequency of insurance deposits over time and compare the deposit behavior of different clients. The sum of deposits per client for a given week can easily be queried. 


Deposits and Withdrawals per client per day/quarter/year Fact Table: This fact table contains information about the deposits and withdrawals per client, which can be grouped according to time. The table includes the client key and time key. Using the sum function on the deposit and withdrawal amounts per client, we can get the total amount withdrawn and deposited in a specific time period.  The data can be used to compare the deposits and withdrawals per client, or be tailored to group by the day, quarter, or year. 


Deposits and Withdrawals for an area Fact Table: This fact table contains information about the deposits and withdrawals per area, which can be grouped according to time. The table includes the area key, time key, and using the sum function on the amounts of the deposits and withdrawals, the total deposits and withdrawals done in an area for a given time period. The data can be utilized to compare transactions and help identify patterns and trends among multiple areas.


Transaction History of a Client per day Fact Table: This fact table includes information identifying the transactional history for a client during a particular day, containing the client key, time key, amount, current balance, and running balance. Under the amount category, a positive value classifies as a deposit and a negative value refers to a withdrawal. Note that each entry also classifies as one transaction, either a deposit or withdrawal. As such, the information can be grouped by client and day to determine the net amount transacted. 


Daily Branch Performance Fact Table: This fact table contains information about the daily performance of each branch in terms of the amount of withdrawals and deposits made per account type, including the branch key, the time key, the account_key, with information on the account type, along with the total deposit and withdrawal amounts. This information can be used to compare the performance of different branches, group by the account type, model growth (or decline) over time, and identify areas for improvement.