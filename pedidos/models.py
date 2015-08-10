#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=200)
    data_inclusao = models.DateTimeField('Data de Inclusão')

class Pedido(models.Model):
    data_pedido = models.DateTimeField('Data do Pedido')

class Item_Pedido(models.Model):
    pedido = models.ForeignKey(Pedido)
    produto = models.ForeignKey(Produto)
    quatidade = models.FloatField()
    valor = models.FloatField()

