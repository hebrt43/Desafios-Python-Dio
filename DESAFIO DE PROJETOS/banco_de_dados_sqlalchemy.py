import select
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect
from sqlalchemy.orm import Session, declarative_base, relationship


Base = declarative_base()


class Client(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String)
    address = Column(String)
    account = relationship("Account", back_populates="user")


def __repr__(self):
    return f"user (id={self.id}, name={self.name}, cpf={self.cpf})"


class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    agency = Column(String)
    num = Column(String)
    id_cliente = Column(Integer, ForeignKey("user_account.id"))
    
    id_cliente = relationship("id_cliente", back_populates="id_cliente")


    def __repr__(self):
        return f"account (id={self.id}, id_cliente={self.id_cliente})"


# conexão com banco de dados no banco de dados
engine = create_engine("sqlite://")

Base.metadata.create_all(engine)
# investiga o esquema do banco de dados
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    lorrany = Account(
        name="Lorrany",
        cpf="11254654600",
        id_cliente=[Account(id_cliente = "MariaAparecida@email.com")]
    )
    jessica = Account(
        name="Jessica",
        cpf="32165489797",
        id_cliente=[Account(id_cliente = "jessica@ferreira.com"),
                    Account(id_cliente = "jessica@ferreira.org")]
    )
    # enviando para o BD (presistência de dados)
    session.add_all([lorrany, jessica,])

    session.commit()

stmt = select(Account).where(Account.name.in_(["lorrany"]))
print(stmt)



