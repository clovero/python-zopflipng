from distutils.core import setup, Extension


# Get the relative zopflipng source location
def get_zopflipng_source(items):
    return list(map(lambda item: "zopfli/src/" + item, items))


# zopflipng sources
zopflipng_src = get_zopflipng_source([
    'zopfli/blocksplitter.c',
    'zopfli/cache.c',
    'zopfli/deflate.c',
    'zopfli/gzip_container.c',
    'zopfli/hash.c',
    'zopfli/katajainen.c',
    'zopfli/lz77.c',
    'zopfli/squeeze.c',
    'zopfli/tree.c',
    'zopfli/util.c',
    'zopfli/zlib_container.c',
    'zopfli/zopfli_lib.c',
    'zopflipng/lodepng/lodepng_util.cpp',
    'zopflipng/lodepng/lodepng.cpp',
    'zopflipng/zopflipng_lib.cc'
])

# python wrapper
zopflipng_src.extend([
    'src/py_zopflipng.cc'
])

# define module
module_zopflipng = Extension('zopflipng._clib',
                             language="c++",
                             sources=zopflipng_src,
                             include_dirs=['zopfli/src/zopfli', 'zopfli/src/zopflipng'], )

setup(name='zopflipng',
      version='1.1.1',
      description='Zopflipng wrapper for python,used for lossless compression of PNG',
      author='clovero',
      license='Apache',
      author_email='clovero@foxmail.com',
      url="https://github.com/clovero/python-zopflipng.git",
      long_description_content_type='text/markdown',
      long_description=open('README.md', encoding='utf-8').read(),
      ext_modules=[module_zopflipng],
      include_package_data=True,
      package_dir={'': 'src'},
      packages=['zopflipng'],
      platforms="any")
