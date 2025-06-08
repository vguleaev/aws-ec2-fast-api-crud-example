import pytest
from unittest.mock import MagicMock
from app.crud import todo_crud
from app.models import Todo
from app.schemas import TodoCreate
from pytest_mock import MockerFixture


@pytest.fixture
def mock_db_session(mocker: MockerFixture) -> MagicMock:
    """Fixture that provides a mocked database session"""
    mock_session = mocker.MagicMock()
    mock_session_context = mocker.MagicMock()
    mock_session_context.__enter__.return_value = mock_session
    mock_session_context.__exit__.return_value = None

    mocker.patch("app.crud.Session", return_value=mock_session_context)
    return mock_session


def test_create_todo(mock_db_session: MagicMock):
    """Test creating a todo with mocked database"""

    # Setup mock behavior for this specific test
    mock_db_session.refresh.side_effect = lambda todo: setattr(todo, "id", 1)

    todo_data = TodoCreate(
        title="Test Todo", description="Test Description", completed=False
    )

    result = todo_crud.create_todo(todo_data)

    assert result.title == "Test Todo"
    assert result.description == "Test Description"
    assert result.completed is False
    assert result.id == 1
    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once()


def test_read_todos(mock_db_session: MagicMock):
    """Test reading all todos with mocked database"""

    # Setup mock behavior for this specific test
    mock_db_session.exec.return_value.all.return_value = [
        Todo(id=1, title="Test Todo",
             description="Test Description", completed=False),
        Todo(
            id=2, title="Test Todo 2", description="Test Description 2", completed=True
        ),
    ]

    result = todo_crud.read_todos()

    assert len(result) == 2
    assert result[0].id == 1
    assert result[1].id == 2


def test_read_todo(mock_db_session: MagicMock):
    """Test reading a single todo with mocked database"""

    # Setup mock behavior for this specific test
    test_todo = Todo(
        id=1, title="Test Todo", description="Test Description", completed=False
    )
    mock_db_session.exec.return_value.first.return_value = test_todo

    result = todo_crud.read_todo(1)

    assert result is not None
    assert result.id == 1
