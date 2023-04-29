import salt.utils.files

def copy_dir(src_dir, dest_dir):
    """
    Копирование диркетории от мастера миньону.

    :param src_dir: Путь к копируемой дериктории мастера.
    :param dest_dir: Путь назначения у миньона.
    :return: Словарь с результатом выполнения задания.
    """
    ret = {'result': False, 'comment': '', 'changes': {}}

    # Check if the source directory exists on the master
    if not __salt__['file.directory_exists'](src_dir):
        ret['comment'] = 'Путь назначения не существует'
        return ret

    # Check if the destination directory exists on the minion
    if not __salt__['file.directory_exists'](dest_dir):
        # Create the destination directory if it does not exist
        __salt__['file.mkdir'](dest_dir)

    # Copy the directory from master to minion
    try:
        salt.utils.files.copyfile(src_dir, dest_dir)
        ret['result'] = True
        ret['comment'] = 'Директория успешно скопирована'
        ret['changes'][dest_dir] = 'Скопировано'
    except Exception as e:
        ret['comment'] = 'Ошибка при копировании директории: {}'.format(str(e))

    return ret
