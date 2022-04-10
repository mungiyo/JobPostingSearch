#!/bin/bash

sleep 10 | echo "Waiting for the servers to start..."

mongo mongodb://mongo1:27017/${POSTING_DB} <<-EOF
    rs.initiate({
        _id: "replication",
        members: [
        { _id: 0, host: "mongo1:27017", priority:300 },
        { _id: 1, host: "mongo2:27017", priority:200 },
        { _id: 2, host: "mongo3:27017", priority:100 }
        ],
    })
EOF
echo "Initiated replica set"

# sleep 5

# mongosh mongodb://mongo1:27017/${MONGO_ADMIN} <<-EOF
#     db.createUser({
#         user: "${MONGO_ADMIN}",
#         pwd: "${MONGO_ADMIN}",
#         roles: [ { role: "userAdminAnyDatabase", db: "${MONGO_ADMIN}" } ]
#     })
# EOF

# mongosh -u ${MONGO_ADMIN} -p ${MONGO_ADMIN} mongodb://mongo1:27017/${MONGO_ADMIN} <<EOF
#     db.createUser({
#         user: ${POSTING_USER},
#         pwd: ${POSTING_USER},
#         roles: [ 
#             { role: "readWrite", db: "${POSTING_DB}" },
#             { role: "read", db: "local" },
#             { role: "read", db: "config" },
#             { role: "read", db: "${MONGO_ADMIN}" },
#         ]
#     })
# EOF