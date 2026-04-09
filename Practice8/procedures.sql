CREATE OR REPLACE PROCEDURE insert_or_update_user(
    p_name VARCHAR,
    p_surname VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM phonebook
        WHERE name = p_name AND surname = p_surname
    ) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE name = p_name AND surname = p_surname;
    ELSE
        INSERT INTO phonebook(name, surname, phone)
        VALUES (p_name, p_surname, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_many_users(
    p_names TEXT[],
    p_surnames TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        IF p_phones[i] ~ '^[0-9]{11}$' THEN
            INSERT INTO phonebook(name, surname, phone)
            VALUES (p_names[i], p_surnames[i], p_phones[i]);
        ELSE
            RAISE NOTICE 'Wrong phone: %', p_phones[i];
        END IF;
    END LOOP;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_user(p_value VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = p_value OR phone = p_value;
END;
$$;