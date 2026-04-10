CREATE OR REPLACE PROCEDURE insert_or_update_user(
    p_first_name VARCHAR,
    p_surname VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM pphonebook
        WHERE first_name = p_first_name
          AND surname = p_surname
    ) THEN
        UPDATE pphonebook
        SET phone = p_phone
        WHERE first_name = p_first_name
          AND surname = p_surname;
    ELSE
        INSERT INTO pphonebook(first_name, surname, phone)
        VALUES (p_first_name, p_surname, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_user(
    p_value VARCHAR,
    p_by VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_by = 'name' THEN
        DELETE FROM pphonebook
        WHERE first_name = p_value;
    ELSIF p_by = 'phone' THEN
        DELETE FROM pphonebook
        WHERE phone = p_value;
    END IF;
END;
$$;