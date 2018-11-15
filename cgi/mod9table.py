#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
from flask import Flask, render_template
from decimal import Decimal
app = Flask(__name__)


@app.route('/triangle/mod9/<columns_number>/<rows_number>')
def triangle_mod9(columns_number, rows_number):
    n_value = 1
    s_value = 0
    range_cols = range(0, int(columns_number))  # range das colunas.
    range_rows = range(2, int(rows_number))  # range das linhas.
    rows = [list(), list()]

    for i in range_cols:
        rows[0].append(int(s_value))  # faz a primeira linha só com elementos 0.
        if i == 0:
            rows[1].append(0)
        else:
            rows[1].append(int(n_value) + int(s_value))  # faz a segunda linha so com elementos 1.

    for r in range_rows:  # loop de qtd de linhas.
        row = []  # limpa a linha a cada iteração.
        for c in range_cols:  # loop de qtd de colunas.
            if c == 0:  # verifica se é a primeira coluna,
                value = int(s_value)  # se for define valor como 1.
            elif c == 1:
                value = int(n_value)
            else:
                value = row[c - 1] + rows[r - 1][c]
            row.append(value)  # adiciona o valor a linha atual.

        rows.append(row)  # adiciona a linha atual ao conjunto de linhas.

    return render_template('triangle_mod.html', rows=rows)


@app.route('/triangle/N<n_value>s<s_value>/<columns_number>/<rows_number>')
def triangle_ns(n_value, s_value, columns_number, rows_number):

    range_cols = range(0, int(columns_number))  # range das colunas.
    range_rows = range(2, int(rows_number))  # range das linhas.
    rows = [list(), list()]

    for i in range_cols:
        rows[0].append(int(s_value))  # faz a primeira linha só com elementos 0.
        if i == 0:
            rows[1].append(0)
        else:
            rows[1].append(int(n_value) + int(s_value))  # faz a segunda linha so com elementos 1.

    for r in range_rows:  # loop de qtd de linhas.
        row = []  # limpa a linha a cada iteração.
        for c in range_cols:  # loop de qtd de colunas.
            if c == 0:  # verifica se é a primeira coluna,
                value = int(s_value)  # se for define valor como 1.
            elif c == 1:
                value = int(n_value)
            else:
                value = row[c - 1] + rows[r - 1][c]
            row.append(value)  # adiciona o valor a linha atual.

        rows.append(row)  # adiciona a linha atual ao conjunto de linhas.
    return render_template('triangle.html', rows=rows)


@app.route('/triangle-nc/N<n_value>s<s_value>/<columns_number>/<rows_number>')
def triangle_nc(n_value, s_value, columns_number, rows_number):

    range_cols = range(0, int(columns_number))  # range das colunas.
    range_rows = range(2, int(rows_number))     # range das linhas.
    rows = [list(), list()]

    for i in range_cols:
        rows[0].append(int(s_value))                # faz a primeira linha só com elementos 0.
        if i == 0:
            rows[1].append(0)
        else:
            rows[1].append(int(n_value)+int(s_value))   # faz a segunda linha so com elementos 1.

    for r in range_rows:  # loop de qtd de linhas.
        row = []  # limpa a linha a cada iteração.
        for c in range_cols:  # loop de qtd de colunas.
            if c == 0:                  # verifica se é a primeira coluna,
                value = int(s_value)    # se for define valor como 1.
            elif c ==1:
                value = int(n_value)
            else:
                value = row[c-1] + rows[r-1][c]
            row.append(value)  # adiciona o valor a linha atual.

        rows.append(row)  # adiciona a linha atual ao conjunto de linhas.

    return render_template('triangle-nc.html', rows=rows)


@app.route('/RepUnitPowers/<columns_number>/<rows_number>')
def rep_unit_powers(columns_number, rows_number):

    range_cols = range(0, int(columns_number)+1)  # range das colunas.
    range_rows = range(1, int(rows_number)+1)     # range das linhas.
    rows = [list(), list()]
    row = ['t']
    for c in range_cols:
        row.append('{}'.format(c))
    rows.append(row)

    row = ['Index(y)']
    for c in range_cols:
        row.append('(R_y)^{}'.format(c))
    rows.append(row)

    for r in range_rows:
        row = []
        y = r
        svalue = int('1' * y)
        row.append(f'{y}')
        for c in range_cols:
            row.append(svalue**c)
        rows.append(row)

    return render_template('rep_unit_powers.html', rows=rows)


@app.route('/RepUnitPowers/mod9/<columns_number>/<rows_number>')
def rep_unit_powers_mod9(columns_number, rows_number):

    range_cols = range(0, int(columns_number)+1)  # range das colunas.
    range_rows = range(1, int(rows_number)+1)     # range das linhas.
    rows = [list(), list()]
    row = [' ']
    for c in range_cols:
        row.append('{}'.format(c))
    rows.append(row)

    for r in range_rows:
        row = []
        y = r
        svalue = int('1' * y)
        row.append(f'{y}')
        for c in range_cols:
            row.append((svalue**c) % 9)
        rows.append(row)

    return render_template('rep_unit_powers_mod9.html', rows=rows)
