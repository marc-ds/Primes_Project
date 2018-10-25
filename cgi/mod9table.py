#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/triangle/mod9/<columns_number>/<rows_number>')
def triangle_mod9(columns_number, rows_number):
    n_value = 1
    s_value = 0
    range_cols = range(0, int(columns_number))
    range_rows = range(2, int(rows_number))
    rows = [list(), list()]

    for i in range_cols:
        rows[0].append(int(s_value))
        rows[1].append(int(n_value)+int(s_value))

    for r in range_rows:
        row = []
        for c in range_cols:
            if c == 0:
                value = int(n_value)
            else:
                value = row[c-1] + rows[r-1][c]
            row.append(value)

        rows.append(row)

    return render_template('triangle_mod.html', rows=rows)


@app.route('/triangle/N<n_value>s<s_value>/<columns_number>/<rows_number>')
def triangle_ns(n_value, s_value, columns_number, rows_number):

    range_cols = range(0, int(columns_number))
    range_rows = range(2, int(rows_number))
    rows = [list(), list()]

    for i in range_cols:
        rows[0].append(int(s_value))
        rows[1].append(int(n_value)+int(s_value))

    for r in range_rows:
        row = []
        for c in range_cols:
            if c == 0:
                value = int(n_value)
            else:
                value = row[c-1] + rows[r-1][c]
            row.append(value)

        rows.append(row)

    return render_template('triangle.html', rows=rows)


@app.route('/triangle-nc/N<n_value>s<s_value>/<columns_number>/<rows_number>')
def triangle_nc(n_value, s_value, columns_number, rows_number):

    range_cols = range(0, int(columns_number))
    range_rows = range(2, int(rows_number))
    rows = [list(), list()]

    for i in range_cols:
        rows[0].append(int(s_value))
        rows[1].append(int(n_value)+int(s_value))

    for r in range_rows:
        row = []
        for c in range_cols:
            if c == 0:
                value = int(n_value)
            else:
                value = row[c-1] + rows[r-1][c]
            row.append(value)

        rows.append(row)

    return render_template('triangle-nc.html', rows=rows)

