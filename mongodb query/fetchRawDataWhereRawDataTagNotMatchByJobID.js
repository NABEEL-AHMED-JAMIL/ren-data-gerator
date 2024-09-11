db.rawData.aggregate([
    {
        $lookup: {
            from: "fileInfo",
            localField: "tag",
            foreignField: "remoteFileTag",
            as: "matchingFiles"
        }
    },
    {
        $match: {
            matchingFiles: {
                $not: {
                    $elemMatch: { jobId: 1558 }
                }
            }
        }
    },
    {
        $project: {
            _id: 1,
            folderPath: 1,
            filePath: 1,
            tag: 1,
            created: 1
        }
    },
    {
        $limit: 5000
    }
]);