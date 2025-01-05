


from app.database import get_db

from functools import wraps
from typing import Callable

def db_select(func: Callable) -> Callable:
    """
    Декоратор чтения данных из ДБ    
    Сгоздает объект сессии и передает в функцию в качестве аргумента
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            session = get_db()
            result = func(*args, db=session, **kwargs)

        except Exception as e:

            print('При работе с БД произошла ошибка', e)
            raise e
        
        finally:
            session.close()

        return result

    return wrapper


def db_transaction(func: Callable) -> Callable:
    """
    Декоратор для взаимодействия с ДБ
    Попытка выполнить функцию-запрос к БД
    В случае успеха делает commit, в случае неудачи - rollback
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        session = get_db()

        try:
            res = func(*args, db=session, **kwargs)
            session.commit()
                    
        except Exception as e:

            session.rollback()
            print('При работе с БД произошла ошибка', e)
            
            raise e
                
        finally:
            session.close()

        return res
    
    return wrapper