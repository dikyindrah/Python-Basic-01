import compileall as call

file1 = 'D:\web\Python\Python-Pemrograman-Dasar\99-Mengkompilasi File Python (.pyc)\modul\\file1.py'
direktori_file_program = 'D:\web\Python\Python-Pemrograman-Dasar\99-Mengkompilasi File Python (.pyc)\modul'

# # Mengkompilasi satu file yang ada dialam sebuah direktori
call.compile_file(file1)

# Mengkompilasi seluruh file yang ada dialam sebuah direktori
call.compile_dir(direktori_file_program)