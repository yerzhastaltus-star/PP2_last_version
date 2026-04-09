CREATE OR REPLACE FUNCTION search_pattern(p_pattern TEXT)
RETURNS TABLE(name VARCHAR, surname VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.name, p.surname, p.phone
    FROM phonebook p
    WHERE p.name ILIKE '%' || p_pattern || '%'
       OR p.surname ILIKE '%' || p_pattern || '%'
       OR p.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(name VARCHAR, surname VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.name, p.surname, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;