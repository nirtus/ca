USE [ca]
GO
/****** Object:  StoredProcedure [dbo].[calculate_delta_speed]    Script Date: 2023-03-28 21:47:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[calculate_delta_speed](@object_id INT)
AS
BEGIN
	SELECT
		*,

        t1.ObjId AS object_id,
        (SQRT(POWER(t2.x - t1.x, 2) + POWER(t2.y - t1.y, 2)) / (CAST(t2.TimeStamp AS FLOAT) - CAST(t1.TimeStamp AS FLOAT))) AS delta_speed
    FROM 
        traffic t0
        JOIN traffic t1 ON t1.ObjId = @object_id AND CAST(t1.TimeStamp AS FLOAT) > CAST(t0.TimeStamp AS FLOAT)
        JOIN traffic t2 ON t2.ObjId = @object_id AND CAST(t2.TimeStamp AS FLOAT) > CAST(t1.TimeStamp AS FLOAT)
    WHERE 
        t0.ObjId = @object_id AND CAST(t0.TimeStamp AS FLOAT) < CAST(t1.TimeStamp AS FLOAT)

END
