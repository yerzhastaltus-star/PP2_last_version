CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE (
    id INT,
    first_name VARCHAR,
    surname VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.first_name, pb.surname, pb.phone
    FROM pphonebook pb
    WHERE pb.first_name ILIKE '%' || p_pattern || '%'
       OR pb.surname ILIKE '%' || p_pattern || '%'
       OR pb.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION insert_many_users(
    p_first_names TEXT[],
    p_surnames TEXT[],
    p_phones TEXT[]
)
RETURNS TABLE (
    bad_first_name TEXT,
    bad_surname TEXT,
    bad_phone TEXT
)
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1 .. array_length(p_first_names, 1)
    LOOP
        IF p_phones[i] ~ '^[0-9]{11}$' THEN
            IF EXISTS (
                SELECT 1
                FROM pphonebook
                WHERE first_name = p_first_names[i]
                  AND surname = p_surnames[i]
            ) THEN
                UPDATE pphonebook
                SET phone = p_phones[i]
                WHERE first_name = p_first_names[i]
                  AND surname = p_surnames[i];
            ELSE
                INSERT INTO pphonebook(first_name, surname, phone)
                VALUES (p_first_names[i], p_surnames[i], p_phones[i]);
            END IF;
        ELSE
            bad_first_name := p_first_names[i];
            bad_surname := p_surnames[i];
            bad_phone := p_phones[i];
            RETURN NEXT;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE (
    id INT,
    first_name VARCHAR,
    surname VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.first_name, pb.surname, pb.phone
    FROM pphonebook pb
    ORDER BY pb.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;