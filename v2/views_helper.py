
def print_table(obj, f0=False, inv=False):

    if inv:
        y_range = obj.y_range_inv
    else:
        y_range = obj.y_range

    for y in y_range:
        print('<tr id="y{:d}" class="y">'.format(y))
        print('<th class="y"> {} </th>'.format(y))

        if y >= -1 and y <=1:
            for item in obj(y):
                if f0:
                    print('<td class="{}" id="data">{}</td>'.format(item.type0(True), item.when_f0()))
                else:
                    print('<td class="{}" id="data">{}</td>'.format(item.type(True), item()))
        else:
            for item in obj(y):
                if f0:
                    print('<td class="{}" id="data">{}</td>'.format(item.type0(), item.when_f0()))
                else:
                    print('<td class="{}" id="data">{}</td>'.format(item.type(), item()))

def print_density(bbuster_obj, den_range):
    pos_list = list()
    neg_list = list()
    print('<tr id="den_pos_abs" class="density">')
    print('<th id="den_pos_abs">#Primes y&gt;0 </th>')
    for item in bbuster_obj(0):
        pos_list.append(item.density_pos(den_range))
        print('<td class="density" id="density">{:.2f}</td>'.format(pos_list[-1]))
    print('</tr>')

    print('<tr id="den_pos_rel" class="density">')
    print('<th id="den_pos_rel">%Primes y&gt;0 </th>')
    for i in range(0, 4):
        print('<td class="density" id="density">{:.2f}%</td>'.format((pos_list[i] / float(den_range)) * 100))
    print('</tr>')

    print('<tr id="density_neg" class="density">')
    print('<th id="density_neg">#Primes y&le;0</th>')
    for item in bbuster_obj(0):
        neg_list.append(item.density_neg(den_range))
        print('<td class="density" id="density">{:.2f}</td>'.format(neg_list[-1]))
    print('</tr>')

    print('<tr id="den_neg_rel" class="density">')
    print('<th id="den_neg_rel">%Primes y&gt;0 </th>')
    for i in range(0, 4):
        print('<td class="density" id="density">{:.2f}%</td>'.format((neg_list[i] / float(den_range)) * 100))
    print('</tr>')

    print('<tr id="den_total_abs" class="density">')
    print('<th id="den_total_abs">#Primes total</th>')
    for i in range(0, 4):
        print('<td class="density" id="density">{:.2f}</td>'.format(neg_list[i] + pos_list[i]))
    print('</tr>')

    print('<tr id="den_total_rel" class="density">')
    print('<th id="den_total_rel">%Primes total</th>')
    for i in range(0, 4):
        print('<td class="density" id="density">{:.2f}%</td>'.format(((neg_list[i] + pos_list[i]) / (float(den_range)*2)) * 100))
    print('</tr>')

def show_table(bbuster_obj, name, den_range, f0=False, inv=False):

    if f0:

        print('<table id="{}">'.format(name))

        print('<tr id="y_vertex">')
        print('<th id="y_vertex"> y_vertex&ordm; </th>')
        for item in bbuster_obj.y_vertex():
            print('<td class="{}" id="y_vertex">{:.4g}</td>'.format(item.yv_type0(), item.y_vertex0))
        print('</tr>')

        print('<tr id="offset">')
        print('<th id="offset"> offset&ordm; </th>')
        for item in bbuster_obj.offset():
            print('<td class="{}" id="offset">{:.2g}</td>'.format(item.f_type0(), item.offset0))
        print('</tr>')

        print('<tr id="delta">')
        print('<th id="delta"> &Delta;&ordm; </th>')
        for item in bbuster_obj.delta():
            print('<td class="{}" id="delta">{:d}</td>'.format(item.d_type0(), item.delta0))
        print('</tr>')

        print('<tr id="c_g">')
        print('<th id="c_g"> C.G.&ordm; </th>')
        for item in bbuster_obj.c_g():
            print('<td class="{}" id="c_g">{:.3g}</td>'.format(item.cg_type0(), item.c_g0))
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

        print_table(bbuster_obj, f0, inv)

        if den_range: print_density(bbuster_obj, den_range)


    else:
        """Start if f0 is not true"""
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

        print_table(bbuster_obj, f0, inv)

        if den_range: print_density(bbuster_obj, den_range)

    print('</tr>')
    print('</table>')
