# from decouple import config
import os

# from pathlib import Path

import psycopg2
from django.core.management.base import BaseCommand
from dotenv import load_dotenv
from psycopg2 import sql

load_dotenv()


class Command(BaseCommand):
    help = "Создание новой базы данных в PostgreSQL"

    def handle(self, *args, **kwargs):
        db_name = os.getenv("POSTGRES_DB")
        db_user = os.getenv("POSTGRES_USER")
        db_password = os.getenv("POSTGRES_PASSWORD")
        db_host = os.getenv("POSTGRES_HOST")
        db_port = os.getenv("POSTGRES_PORT", default="5432")

        try:
            # Подключение к серверу PostgreSQL с базой данных 'postgres'
            conn = psycopg2.connect(
                dbname="postgres",
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            conn.autocommit = True  # Включаем автокоммит для выполнения команд SQL без явного вызова commit()

            with conn.cursor() as cursor:
                # Проверяем, существует ли уже база данных с таким именем
                cursor.execute(
                    sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"),
                    [db_name],
                )
                exists = cursor.fetchone()

                if not exists:
                    # Если база данных не существует, создаем её
                    cursor.execute(
                        sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name))
                    )
                    self.stdout.write(
                        self.style.SUCCESS(f'База данных "{db_name}" успешно создана.')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'База данных "{db_name}" уже существует.')
                    )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Произошла ошибка: {e}"))
        finally:
            if conn:
                conn.close()
