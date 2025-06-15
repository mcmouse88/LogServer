def get_all_logs(connection):
    cursor = connection.cursor()
    query = (
        "SELECT logs_table.log_id, logs_table.tag_name, tag_info_table.priority_value, tag_info_table.priority_short, logs_table.message, logs_table.timestamp, "
        "tag_info_table.color "
        "FROM logs_table "
        "INNER JOIN tags_table ON logs_table.tag_name = tags_table.tag_name "
        "INNER JOIN tag_info_table ON tags_table.priority = tag_info_table.id;"
    )
    cursor.execute(query)
    response = []
    for (log_id, tag_name, priority, priority_short, message, timestamp, color) in cursor:
        response.append(
            {
                'log_id': log_id,
                'tag_name': tag_name,
                'priority': priority,
                'priority_short': priority_short,
                'color': color,
                'message': message,
                'timestamp': timestamp
            }
        )
    return response

def insert_new_log(connection, log):
    cursor = connection.cursor()
    query_tag = (
        "INSERT IGNORE INTO tags_table (tag_name, priority) "
        "VALUES(%s, %s);"
    )
    query_log = (
        "INSERT INTO logs_table (tag_name, message, timestamp) "
        "VALUES(%s, %s, %s);"
    )
    data_tag = (log['tag_name'], log['priority'])
    data_log = (log['tag_name'], log['message'], log['timestamp'])
    # TODO: should be one transaction
    cursor.execute(query_tag, data_tag)
    cursor.execute(query_log, data_log)

    connection.commit()
    return {'status': 200}