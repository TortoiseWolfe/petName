def api_helper_get_data():
    print("API Helper: Get Data")


def api_helper_parse_data():
    print("API Helper: Parse Data")


def excel_helper_read_file():
    print("Excel Helper: Read File")


def excel_helper_write_file():
    print("Excel Helper: Write File")


def database_helper_connect():
    print("Database Helper: Connect")


def database_helper_query():
    print("Database Helper: Query")


def database_helper_insert():
    print("Database Helper: Insert")


def database_helper_update():
    print("Database Helper: Update")


def main():
    print("Starting main function")
    api_helper_get_data()
    api_helper_parse_data()
    excel_helper_read_file()
    excel_helper_write_file()
    database_helper_connect()
    database_helper_query()
    database_helper_insert()
    database_helper_update()
    print("Finished main function")


if __name__ == "__main__":
    main()
