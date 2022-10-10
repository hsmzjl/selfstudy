import os
import sys


os.getcwd()
# 返回表示当前工作目录的字符串。

os.mkdir('path')
# 创建一个名为 path 的目录，应用以数字表示的权限模式 mode。

os.remove('path')
# 移除（删除）文件 path。如果 path 是目录，则抛出 IsADirectoryError 异常。请使用 rmdir() 删除目录。
# 本函数支持 基于目录描述符的相对路径。
# 在 Windows 上，尝试删除正在使用的文件会抛出异常。而在 Unix 上，虽然该文件的条目会被删除，但分配给文件的存储空间仍然不可用，直到原始文件不再使用为止。

os.removedirs('name')
# 递归删除目录。工作方式类似于 rmdir()，不同之处在于，如果成功删除了末尾一级目录，
# removedirs() 会尝试依次删除 path 中提到的每个父目录，直到抛出错误为止（但该错误会被忽略，因为这通常表示父目录不是空目录）。
# 例如，os.removedirs('foo/bar/baz') 将首先删除目录 'foo/bar/baz'，然后如果 'foo/bar' 和 'foo' 为空，则继续删除它们。
# 如果无法成功删除末尾一级目录，则抛出 OSError 异常。

os.rename('src', 'dst')
# 将文件或目录 src 重命名为 dst。如果 dst 已存在，则下列情况下将会操作失败，并抛出 OSError 的子类：

os.renames('old', 'new')
# 递归重命名目录或文件。工作方式类似 rename()，除了会首先创建新路径所需的中间目录。重命名后，将调用 removedirs() 删除旧路径中不需要的目录。

os.replace('src', 'dst')
# 将文件或目录 src 重命名为 dst。如果 dst 是目录，将抛出 OSError 异常。
# 如果 dst 已存在且为文件，则在用户具有权限的情况下，将对其进行静默替换。
# 如果 src 和 dst 在不同的文件系统上，本操作可能会失败。如果成功，重命名操作将是一个原子操作（这是 POSIX 的要求）。

os.rmdir('path')
# 移除（删除）目录 path。如果目录不存在或不为空，则会分别抛出 FileNotFoundError 或 OSError 异常。要删除整个目录树，可以使用 shutil.rmtree()。

