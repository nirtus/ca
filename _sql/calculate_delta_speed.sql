USE [ca]
GO

/****** Object:  StoredProcedure [dbo].[calculate_delta_speed]    Script Date: 2023-04-04 22:13:32 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[calculate_delta_speed](@ObjId INT)
AS
BEGIN
	SET NOCOUNT ON
	-- make buffer table
	SELECT
		ROW_NUMBER() OVER (ORDER BY Id) AS rn,
		Id,
		ObjId,
		CAST(ROUND(x, 2) AS float) AS x,
		CAST(ROUND(y, 2) AS float) AS y,
		CONVERT(float, RIGHT(LEFT(TimeStamp, 14), LEN(LEFT(TimeStamp, 14))-7)) AS CSeconds
	INTO #tr
	FROM traffic
	WHERE ObjId = @ObjId
	ORDER BY TimeStamp

	-- make buffer table 1
	SELECT *
	INTO #tr1
	FROM #tr
	WHERE Id <> (SELECT MIN(Id) FROM #tr)

	-- make buffer table 2
	SELECT *
	INTO #tr2
	FROM #tr
	WHERE Id <> (SELECT MAX(Id) FROM #tr)

	-- calculate delta speed
	SELECT
		#tr2.ObjId,
		#tr2.x AS x1,
		#tr2.y AS y1,
		(SELECT #tr1.x FROM #tr1 WHERE #tr1.rn = #tr2.rn + 1) AS x2,
		(SELECT #tr1.y FROM #tr1 WHERE #tr1.rn = #tr2.rn + 1) AS y2,
		ROUND(((SELECT #tr1.CSeconds FROM #tr1 WHERE #tr1.rn = #tr2.rn + 1) - #tr2.CSeconds), 3) AS DeltaTime--,
	FROM #tr2 

	-- drop buffer tables
	DROP TABLE #tr
	DROP TABLE #tr1
	DROP TABLE #tr2

END
GO

