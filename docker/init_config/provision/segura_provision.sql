COPY tbl_master(
selfaccount,
currency,
processdate,
debcred,
amount,
crossaccount,
crossaccountholder,
interestdate,
type,
unknown1,
description1,
description2,
description3,
description4,
unknown2,
unknown3,
transactionreference,
incassantid,
kenmerkmachtiging
)
FROM '/docker-entrypoint-initdb.d/data/noDuplicatesMasterCsv.csv' DELIMITER '|';
