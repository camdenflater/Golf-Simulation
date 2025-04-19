CREATE PROCEDURE dbo.GolfSimulationJsonParseUpload
    @GolfJson NVARCHAR(MAX)
AS
BEGIN

    DECLARE @Records TABLE (JsonValue NVARCHAR(MAX));

    INSERT INTO @Records (JsonValue)
    SELECT [value]
    FROM OPENJSON(@GolfJson)
    WITH (
        [value] NVARCHAR(MAX) '$.value'
    );

    INSERT INTO dbo.GolfSimulation (
        Record, Hole, Golfer, Stroke, Par, Yards_To_Pin, Pin_Distance, Club
    )
    SELECT 
        Record,
        Hole,
        Golfer,
        Stroke,
        Par,
        Yards_To_Pin,
        Pin_Distance,
        Club
    FROM @Records
    CROSS APPLY OPENJSON(JsonValue)
    WITH (
        Record UNIQUEIDENTIFIER,
        Hole INT,
        Golfer NVARCHAR(100),
        Stroke INT,
        Par INT,
        Yards_To_Pin INT,
        Pin_Distance INT,
        Club NVARCHAR(100)
    );
END
