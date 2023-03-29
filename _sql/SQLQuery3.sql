USE [ca]
GO

/****** Object:  Table [dbo].[traffic]    Script Date: 2023-03-28 19:33:42 ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[traffic]') AND type in (N'U'))
DROP TABLE [dbo].[traffic2]
GO

/****** Object:  Table [dbo].[traffic]    Script Date: 2023-03-28 19:33:42 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[traffic](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[x] [real] NULL,
	[y] [real] NULL,
	[x1] [real] NULL,
	[y1] [real] NULL,
	[x2] [real] NULL,
	[y2] [real] NULL,
	[TimeStamp] [nvarchar](50) NULL,
	[ObjId] [int] NULL,
	[ObjType] [int] NULL,
	[ObjConf] [real] NULL,
	CONSTRAINT [PK_traffic] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


