CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS users ( 
                    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                    first_name VARCHAR(100) NOT NULL,
                    last_name VARCHAR(100) NOT NULL, 
                    telegram_id BIGINT UNIQUE NOT NULL,
                    solves INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS problems (
                    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                    problem_number VARCHAR(3) UNIQUE NOT NULL, 
                    assigned_to DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS users_problems_map (
                    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
                    problem_id UUID REFERENCES problems(id) ON DELETE CASCADE
);