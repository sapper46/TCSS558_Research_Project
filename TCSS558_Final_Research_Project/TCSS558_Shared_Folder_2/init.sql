-- filepath: /home/dave/TCSS558_Shared_Folder_2/init.sql
CREATE TABLE report_table (
    id SERIAL PRIMARY KEY,
    A TEXT,
    B TEXT,
    C TEXT,
    D TEXT,
    E TEXT
);

CREATE TABLE view_table (
    id SERIAL PRIMARY KEY,
    A INTEGER,
    B INTEGER,
    C INTEGER,
    D INTEGER,
    E INTEGER
);

CREATE TABLE target_table (
    id SERIAL PRIMARY KEY,
    A INTEGER,
    B INTEGER,
    C INTEGER,
    D INTEGER,
    E INTEGER
);

CREATE TABLE permission_table (
    id SERIAL PRIMARY KEY,
    A INTEGER,
    B INTEGER,
    C INTEGER,
    D INTEGER,
    E INTEGER
);

-- Initialize the first five rows in all tables with "0"
INSERT INTO report_table (A, B, C, D, E) VALUES ('ZERO', 'ZERO', 'ZERO', 'NA', 'NA');
INSERT INTO report_table (A, B, C, D, E) VALUES ('ZERO', 'ZERO', 'ZERO', 'NA', 'NA');
INSERT INTO report_table (A, B, C, D, E) VALUES ('ZERO', 'ZERO', 'ZERO', 'NA', 'NA');
INSERT INTO report_table (A, B, C, D, E) VALUES ('ZERO', 'ZERO', 'ZERO', 'NA', 'NA');
INSERT INTO report_table (A, B, C, D, E) VALUES ('NA', 'NA', 'NA', 'NA', 'NA');

-- Initialize the view_table with the current time in seconds since the epoch
INSERT INTO view_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);
INSERT INTO view_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);
INSERT INTO view_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);
INSERT INTO view_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);
INSERT INTO view_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);

INSERT INTO target_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);
INSERT INTO target_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);
INSERT INTO target_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);
INSERT INTO target_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);
INSERT INTO target_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);

INSERT INTO permission_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);
INSERT INTO permission_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);
INSERT INTO permission_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);
INSERT INTO permission_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);
INSERT INTO permission_table (A, B, C, D, E) VALUES (0, 0, 0, 0, 0);





--INSERT INTO view_table (A, B, C, D, E) VALUES (1, 2, 3, 4, 5);
--INSERT INTO view_table (A, B, C, D, E) VALUES (1, 2, 3, 4, 5);
--INSERT INTO view_table (A, B, C, D, E) VALUES (1, 2, 3, 4, 5);
--INSERT INTO view_table (A, B, C, D, E) VALUES (1, 2, 3, 4, 5);
--INSERT INTO view_table (A, B, C, D, E) VALUES (1, 2, 3, 4, 5);

--INSERT INTO view_table (A, B, C, D, E) VALUES (EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()));
--INSERT INTO view_table (A, B, C, D, E) VALUES (EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()));
--INSERT INTO view_table (A, B, C, D, E) VALUES (EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()));
--INSERT INTO view_table (A, B, C, D, E) VALUES (EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()));
--INSERT INTO view_table (A, B, C, D, E) VALUES (EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()), EXTRACT(EPOCH FROM NOW()));