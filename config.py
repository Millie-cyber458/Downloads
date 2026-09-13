CREATE DATABASE StudyZen;
Use StudyZen;
Create table LiveClass(
    id int primary key auto_increment primary key,
    title varchar(125) not null,
    start_time datetime not null,
    end_time datetime not null,
    description text,
    link varchar(255) not null);

    #---------
    insert into LiveClass(title, start_time, end_time, description, link) values('Math Class', '2024-06-01 10:00:00', '2024-06-01 11:00:00', 'This is a math class for beginners.', 'https://example.com/math-class');
    insert into LiveClass(title, start_time, end_time, description, link) values('Science Class', '2024-06-02 14:00:00', '2024-06-02 15:00:00', 'This is a science class for beginners.', 'https://example.com/science-class');

DB_CONFIG={
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'StudyZen'
}