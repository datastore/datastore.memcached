
__version__ = '0.1.1'
__author__ = 'Juan Batiz-Benet'
__email__ = 'juan@benet.ai'
__doc__ = '''
memcached datastore implementation.

Tested with:
  * datastore 0.3.0
  * memcached 1.4.5
  * libmemcached 0.50
  * pylibmc 1.2.2

'''

#TODO: Implements queries using a key index.
#TODO: Implement TTL (and key configurations)

import datastore.core


class MemcachedDatastore(datastore.InterfaceMappingDatastore):
  '''Flat memcached datastore. Does not support queries.

  This datastore is implemented as an InterfaceMappingDatastore, as the
  memcached interface is very similar to datastore's.

  The only differences (which InterfaceMappingDatastore takes care of) are:
  - keys should be converted into strings
  - `put` calls should be mapped to `set`


  Hello World:

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

  '''

  def __init__(self, memcached):
    '''Initialize the datastore with given memcached client `memcached`.

    Args:
      memcached: A memcached client to use. Must implement the basic memcached
          interface: set, get, delete. This datastore keeps the interface so
          basic in order to work with any memcached client (or pool of clients).
    '''
    super(MemcachedDatastore, self).__init__(memcached, put='set', key=str)

  def query(self, query):
    '''Returns an iterable of objects matching criteria expressed in `query`

    Args:
      query: Query object describing the objects to return.

    Raturns:
      Cursor with all objects matching criteria
    '''
    #TODO
    raise NotImplementedError
