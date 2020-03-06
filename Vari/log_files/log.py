def index():
    clear_log =A(T('clear log'), _class='button btn btn-info', _onclick = "ajax('%s', [], 'clear_log')" % (URL(c='log', f='clear_app_log_data', args=['debug'])))

    log_data = LOAD(c='log', f='app_log_data', args=['debug'], ajax=True, target='log_container', times='infinity', timeout=3000)
    
    return {'clear_log':clear_log, 'log_data':log_data}

def app_log_data():
    load_debug = True if 'debug' in request.args else False
    #http://www.web2py.com/books/default/chapter/29/04/the-core#request
    import os
    import os.path

    logname = 'app.log'
    if load_debug:
        logname = 'app_debug.log'

    log_file_path = os.path.join(request.folder, 'private', logname)
    logfile = open(log_file_path)
    filedata = logfile.readlines()
    #filedata = logfile.read()
    
    #logger.debug('log_data: %s' % filedata)
    formatted_log_data = UL(_class='unstyled list-unstyled')
    for line in filedata:
        formatted_log_data.append(LI(line))
    return formatted_log_data


def clear_app_log_data():
    load_debug = True if 'debug' in request.args else False

    logger.warn('clear_log')
    import os
    import os.path
    logname = 'app.log'
    if load_debug:
        logname = 'app_debug.log'

    log_file_path = os.path.join(request.folder, 'private', logname)
    if os.path.isfile(log_file_path):
        try:
            #os.remove(log_file_path)   #remove may not work because already in use
            logfile = open(log_file_path, 'w')
            logfile.write('')
            logfile.close()
            logger.info('logfile cleared')
        except Exception:
            logger.exception('error deleting application log')
    