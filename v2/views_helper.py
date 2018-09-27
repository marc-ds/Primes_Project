
def show_table(bbuster_obj, name, f0='no', inv='no'):

    if f0 == 'f0':

        print('<table id="{}">'.format(name))

        print('<tr id="y_vertex">')
        print('<th id="y_vertex"> y_vertex&ordm; </th>')
        for item in bbuster_obj.y_vertex():
            print('<td class="{}" id="y_vertex">{:.4g}</td>'.format(item.yv_type(), item.y_vertex0))
        print('</tr>')

        print('<tr id="offset">')
        print('<th id="offset"> offset&ordm; </th>')
        for item in bbuster_obj.offset():
            print('<td class="{}" id="offset">{:.2g}</td>'.format(item.f_type(), item.offset0))
        print('</tr>')

        print('<tr id="delta">')
        print('<th id="delta"> &Delta;&ordm; </th>')
        for item in bbuster_obj.delta():
            print('<td class="{}" id="delta">{:d}</td>'.format(item.d_type(), item.delta0))
        print('</tr>')

        print('<tr id="c_g">')
        print('<th id="c_g"> C.G.&ordm; </th>')
        for item in bbuster_obj.c_g():
            print('<td class="{}" id="c_g">{:.3g}</td>'.format(item.cg_type(), item.c_g0))
        print('</tr>')

        print('<tr id="a" >')
        print('<th id="a"> a&ordm; </th>')
        for item in bbuster_obj.a():
            print('<td class="a" id="a">{:.2g}</td>'.format(item.a0))
        print('</tr>')

        print('<tr id="b">')
        print('<th id="b"> b&ordm; </th>')
        for item in bbuster_obj.b():
            print('<td class="b" id="b">{:.2g}</td>'.format(item.b0))
        print('</tr>')

        print('<tr id="c">')
        print('<th id="c"> c&ordm; </th>')
        for item in bbuster_obj.c():
            print('<td class="c" id="c">{:.2g}</td>'.format(item.c0))
        print('</tr>')

        if inv == 'inv':
            for y in bbuster_obj.y_range_inv:
                print('<tr id="y{:d}" class="y">'.format(y))
                print('<th class="y"> {} </th>'.format(y))
                for item in bbuster_obj(y):
                    print('<td class="{}" id="data">{}</td>'.format(item.type(), item.when_f0()))

        else:
            for y in bbuster_obj.y_range:
                print('<tr id="y{:d}" class="y">'.format(y))
                print('<th class="y"> {} </th>'.format(y))
                for item in bbuster_obj(y):
                    print('<td class="{}" id="data">{}</td>'.format(item.type(), item.when_f0()))

    else:
        print('<table id="{}">'.format(name))
        print('<tr id="y_vertex">')
        print('<th id="y_vertex"> y_vertex </th>')
        for item in bbuster_obj.y_vertex():
            print('<td class="{}" id="y_vertex">{:.4g}</td>'.format(item.yv_type(), item.y_vertex))
        print('</tr>')

        print('<tr id="offset">')
        print('<th id="offset"> offset </th>')
        for item in bbuster_obj.offset():
            print('<td class="{}" id="offset">{:.2g}</td>'.format(item.f_type(), item.offset))
        print('</tr>')

        print('<tr id="delta">')
        print('<th id="delta"> &Delta; </th>')
        for item in bbuster_obj.delta():
            print('<td class="{}" id="delta">{:d}</td>'.format(item.d_type(), item.delta))
        print('</tr>')

        print('<tr id="c_g">')
        print('<th id="c_g"> C.G. </th>')
        for item in bbuster_obj.c_g():
            print('<td class="{}" id="c_g">{:.3g}</td>'.format(item.cg_type(), item.c_g))
        print('</tr>')

        print('<tr id="a" >')
        print('<th id="a"> a </th>')
        for item in bbuster_obj.a():
            print('<td class="a" id="a">{:.2g}</td>'.format(item.a))
        print('</tr>')

        print('<tr id="b">')
        print('<th id="b"> b </th>')
        for item in bbuster_obj.b():
            print('<td class="b" id="b">{:.2g}</td>'.format(item.b))
        print('</tr>')

        print('<tr id="c">')
        print('<th id="c"> c </th>')
        for item in bbuster_obj.c():
            print('<td class="c" id="c">{:.2g}</td>'.format(item.c))
        print('</tr>')

        if inv == 'inv':
            for y in bbuster_obj.y_range_inv:
                print('<tr id="y{:d}" class="y">'.format(y))
                print('<th class="y"> {} </th>'.format(y))
                for item in bbuster_obj(y):
                    print('<td class="{}" id="data">{}</td>'.format(item.type(), item()))

        else:
            for y in bbuster_obj.y_range:
                print('<tr id="y{:d}" class="y">'.format(y))
                print('<th class="y"> {} </th>'.format(y))
                for item in bbuster_obj(y):
                    print('<td class="{}" id="data">{}</td>'.format(item.type(), item()))


    print('</tr>')
    print('</table>')
