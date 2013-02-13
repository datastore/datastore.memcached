# datastore-memcached

## datastore implementation for memcached

See [datastore](https://github.com/datastore/datastore).


### Install

From pypi (using pip):

    sudo pip install datastore.memcached

From pypi (using setuptools):

    sudo easy_install datastore.memcached

From source:

    git clone https://github.com/datastore/datastore.memcached/
    cd datastore.memcached
    sudo python setup.py install


### License

datastore.memcached is under the MIT License.

### Contact

datastore.memcached is written by [Juan Batiz-Benet](https://github.com/jbenet).
It was extracted from [datastore](https://github.com/datastore/datastore)
in Feb 2013.

Project Homepage:
[https://github.com/datastore/datastore.memcached](https://github.com/datastore/datastore.memcached)

Feel free to contact me. But please file issues in github first. Cheers!


### Hello World

    >>> import pylibmc
    >>> import datastore.memcached
    >>>
    >>> mc = pylibmc.Client(['127.0.0.1'])
    >>> ds = datastore.memcached.MemcachedDatastore(mc)
    >>>
    >>> hello = datastore.Key('hello')
    >>> ds.put(hello, 'world')
    >>> ds.contains(hello)
    True
    >>> ds.get(hello)
    'world'
    >>> ds.delete(hello)
    >>> ds.get(hello)
    None
