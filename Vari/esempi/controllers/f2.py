def form():
    id_rows = db(db.testdata).select(db.testdata.id)
    rows = []
    for record_row in id_rows:
        sqlf = LOAD(f='load_row', vars={'row_id':record_row.id}, ajax=True)
        rows.append( sqlf )

    f = TABLE()
    for row in rows:
        f.append( TR(row) )
    return {'f':f}    

def _table_row_serializer(form, fields):
    row = TR()
    form_name = form.attributes['_name']
    form_id = form.attributes['_id']

    for id, label, controls, help in fields:
        #logger.debug('field data: id=[{}] label=[{}] controls=[{}] help=[{}]'.format(id, label, controls, help))
        #add onchange event       
        if isinstance(controls, INPUT) and controls.attributes['_type'] == 'submit':
            controls.attributes['_id'] = '{form_id}_submit'.format(form_id = form_id)
            controls.attributes['_style'] = 'display:none;'
        '''
        #not needed, add onchange event to each field
        if not (isinstance(controls, INPUT) and controls.attributes['_type'] == 'submit'):
            #new_onchange = '{form_id}.submit()'.format(form_id = form_id)
            new_onchange = 'document.getElementById("{form_id}").click()'.format(form_id = form_id)
            if '_onchange' in controls.attributes:
                controls.attributes['_onchange'] = controls.attributes['_onchange'] + ';' + new_onchange
            else:
                controls.attributes['_onchange'] = new_onchange
        '''

        row.append( TD( controls ) )

    return row

def load_row():
    #logger.debug('load_row {}'.format(request.vars))

    row_id = request.vars.row_id
    
    if row_id != None:
        record = db.testdata(row_id)
        form_name = 'row_form_{}'.format(row_id)
        form_id = 'row_form_{}'.format(row_id)
        form_onchange = "document.getElementById('{form_id}_submit').click()".format(form_id = form_id)
        form = SQLFORM(db.testdata, record,  formstyle=_table_row_serializer, _name=form_name, _id=form_id, showid=False    )    
        form['_onchange'] = form_onchange

    else:
        form = None

    if form:
        #TODO add additional processing if needed as by http://web2py.com/books/default/chapter/29/07/forms-and-validators#The-process-method
        if form.process().accepted:
            response.flash = 'form accepted'
        elif form.errors:
            response.flash = 'form has errors'
        else:
            response.flash = 'please fill out the form'

    #logger.debug('form: {}'.format(form))
    return form