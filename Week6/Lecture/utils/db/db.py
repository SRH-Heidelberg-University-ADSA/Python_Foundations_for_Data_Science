print("module called")
print(__name__)


def insert_db():
    print("insert")


def read_db():
    print("read")


def _init_db():
    print("init")


if __name__ == "__main__":
    _init_db()
