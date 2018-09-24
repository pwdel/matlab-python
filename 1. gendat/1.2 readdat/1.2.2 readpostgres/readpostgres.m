% Reading & Inserting Data from an SQL Table

% Read an existing table
% https://www.mathworks.com/help/database/ug/database.odbc.connection.sqlread.html?s_tid=doc_ta

% Database function
% https://www.mathworks.com/help/database/ug/database.html

% Get the datasource, username, password and put it into the conn object

datasource = 'sample_table';
username = '';
password = '';
driver = 'org.postgresql.Driver';
url = 'postgresql://localhost:5432/matlab-python';
conn = database(datasource,username,password,driver,url))

data = sqlread(conn,tablename);


% https://www.mathworks.com/help/database/ug/database.odbc.connection.sqlwrite.html
% Append data to an existing table
sqlwrite(conn,tablename,data)
