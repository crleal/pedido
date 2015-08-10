#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.contrib import admin

from .models import Produto, Pedido, Item_Pedido

admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Item_Pedido)
