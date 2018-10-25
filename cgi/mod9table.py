#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/mod9table')
def mod9table():
    rows_number = 400
    columns_number = 400
    rg_cols = range(0, columns_number)
    rg_rows = range(2, rows_number)
    rows = [list(), list()]

    for i in rg_cols:
        rows[0].append(0)
        rows[1].append(1)

    for a in rg_rows:
        row = []
        for b in rg_cols:
            if b == 0:
                value = 1
            else:
                value = row[b-1] + rows[a-1][b]
            row.append(value)

        rows.append(row)

    return render_template('mod9table.html', rows=rows)


@app.route('/table')
def abstable():
    rows_number = 200
    columns_number = 200
    rg_cols = range(0, columns_number)
    rg_rows = range(2, rows_number)
    rows = [list(), list()]

    for i in rg_cols:
        rows[0].append(0)
        rows[1].append(1)

    for a in rg_rows:
        row = []
        for b in rg_cols:
            if b == 0:
                value = 1
            else:
                value = row[b-1] + rows[a-1][b]
            row.append(value)

        rows.append(row)

    return render_template('table.html', rows=rows)