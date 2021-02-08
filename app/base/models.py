# -*- encoding: utf-8 -*-
"""
License: Commercial
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String, Float, Date, ForeignKey
from app import db, login_manager
from app.base.util import hash_pass
from marshmallow import Schema, fields, post_load

from sqlalchemy.orm import relationship


class User(db.Model, UserMixin):

    __tablename__ = 'usuarios'
    __table_args__ = {'extend_existing': True}

    id       = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    email    = Column(String, unique=True)
    password = Column(Binary)
    level    = Column(Integer, nullable = True, default = 0)
    pedidos  = relationship("Pedido",  back_populates="User")
    #pvp      = Column(Float, nullable = False, default = 0)


    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass( value ) # we need bytes here (not plain str)
                
            setattr(self, property, value)

    def __repr__(self):
        return str(self.email)


    @post_load
    def create_person(self, data, **kwargs):
        return User(**data)



class Pedido(db.Model):
    __tablename__ = 'pedidos'
    __table_args__ = {'extend_existing': True}

    id_pedido      = Column(Integer, primary_key = True)
    estado         = Column(String,  nullable = True)
    id_cliente     = Column(Integer, ForeignKey('usuarios.id'))
    fecha_pedido   = Column(Date,    nullable = False)
    fecha_medicion = Column(Date,    nullable = True)
    fecha_entrega  = Column(Date,    nullable = True)
    User           = relationship("User", back_populates="pedidos")
    Encimeras_compradas  = relationship("Encimeras_compradas",  back_populates="Pedido")

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]


            setattr(self, property, value)

    def __repr__(self):
        return str(self.id_pedido)







class Inventario(db.Model):
    __tablename__ = 'inventario'
    __table_args__ = {'extend_existing': True}

    id            = Column(Integer, primary_key = True)
    MATERIAL      = Column(String,  nullable = False)
    COLOR         = Column(String,  nullable = False)
    ACABADO       = Column(String,  nullable = True)
    GROSOR        = Column(String,  nullable = True)
    MEDIDA        = Column(String,  nullable = True)
    PRECIO_M2     = Column(Float,   nullable = True)
    PRECIO_TABLA  = Column(Float,   nullable = True)
    FECHA_ENTRADA = Column(Date,    nullable = True)
    FECHA_SALIDA  = Column(Date,    nullable = True)
    ESTADO        = Column(Integer, nullable = True)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]


            setattr(self, property, value)

    def __repr__(self):
        return str(self.id)




class Encimeras(db.Model):
    __tablename__ = 'encimeras'
    __table_args__ = {'extend_existing': True}

    ID                = Column(Integer, primary_key=True)
    MATERIAL          = Column(String,  nullable=False)
    COLOR             = Column(String,  nullable=True)
    GROSOR            = Column(String,  nullable=True)
    ACABADO           = Column(String,  nullable=True)
    MIN_ML            = Column(Integer, nullable=True)
    PRECIO_ML         = Column(Float,   nullable=False)
    PRECIO_M2         = Column(Float,   nullable=False)
    PRECIO_FRENTES_M2 = Column(Float,   nullable=False)
    COSTE_ML          = Column(Float,   nullable=False)
    COSTE_M2          = Column(Float,   nullable=False)
    COSTE_FRENTES_M2  = Column(Float,   nullable=False)
    MEDIDA_TABLA      = Column(Float,   nullable=False)
    MAXIMO_SOBRANTE   = Column(Float,   nullable=False)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]


            setattr(self, property, value)

    def __repr__(self):
        return str(self.ID)



class Encimeras_compradas(db.Model):
    __tablename__ = 'Encimeras_compradas'
    __table_args__ = {'extend_existing': True}


    column_not_exist_in_db = Column(Integer, primary_key=True)
    id_pedido     = Column(Integer, ForeignKey(Pedido.id_pedido))
    MATERIAL      = Column(String,  nullable = False)
    COLOR         = Column(String,  nullable = False)
    ACABADO       = Column(String,  nullable = True)
    GROSOR        = Column(String,  nullable = True)
    MEDIDA        = Column(String,  nullable = True)
    TOTAL         = Column(Float,   nullable = True)
    Pedido        = relationship("Pedido", back_populates="Encimeras_compradas")


    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]


            setattr(self, property, value)

    def __repr__(self):
        return str(self.id_pedido)


class Tablas_compradas(db.Model):
    __tablename__ = 'Tablas_compradas'
    __table_args__ = {'extend_existing': True}


    column_not_exist_in_db = Column(Integer, primary_key=True)
    id_pedido = Column(Integer, nullable = False)
    id        = Column(Integer, nullable = False)
    MATERIAL  = Column(String, nullable=False)
    COLOR     = Column(String, nullable=False)
    ACABADO   = Column(String, nullable=True)
    GROSOR    = Column(String, nullable=True)
    MEDIDA    = Column(String, nullable=True)
    TOTAL     = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return str(self.id)


@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    return user if user else None
