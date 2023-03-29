DECLARE @result_table TABLE (
    object_id INT,
    delta_speed FLOAT
)

INSERT INTO @result_table
EXEC calculate_delta_speed @object_id = 3;

SELECT * FROM @result_table
