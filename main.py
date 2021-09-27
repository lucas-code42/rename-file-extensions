import os


def main():
    print()
    print('Digite o endereço da pasta que deseja alterar os arquivos:')
    path_folder = input(r'')
   
    print()
    print('Local: {}'.format(path_folder))
    print()
    old_extension = '.' + input('Digite a extensão antiga: (txt, pdf, docx, csv, xlsx, jpg, png) --> ')
    new_extension = '.' + input('Digite a nova extensão: (txt, pdf, docx, csv, xlsx, jpg, png) --> ')
    print()

    files_counter = 0

    with os.scandir(path_folder) as files_and_folders:
        for element in files_and_folders:
            if element.is_file():
                # tuple_root_ext = os.path.splitext(element.path)
                # root = tuple_root_ext[0]
                # ext = tuple_root_ext[1]

                root, ext = os.path.splitext(element.path)
                if ext == old_extension:
                    new_path = root + new_extension
                    os.rename(element.path, new_path)
                    files_counter += 1

    print('---- Alterações ----')
    print()
    print('Número de arquivos processados: {}'.format(files_counter))
    print('Extensão: De ({}) Para ({})'.format(old_extension, new_extension))
    print()
    print('Digite enter para finalizar.')
    finish = input()
    return

main()
