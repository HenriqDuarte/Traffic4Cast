# -----------------------------------------------------------------
# h5 file support
# -----------------------------------------------------------------

def load_h5_file(file_path):
    """
    Given a file path to an h5 file assumed to house a tensor, 
    load that tensor into memory and return a pointer.
    """
    # load
    fr = h5py.File(file_path, 'r')
    a_group_key = list(fr.keys())[0]
    data = list(fr[a_group_key])
    # transform to appropriate numpy array 
    data=data[0:]
    data = np.stack(data, axis=0)
    return data

def print_shape(data):
    """
    print data shape
    """
    print(data.shape)

def write_data_to_h5(data, filename):
    """
    write data in gzipped h5 format
    """
    f = h5py.File(filename, 'w', libver='latest')
    dset = f.create_dataset('array', shape=(data.shape), data=data, compression='gzip', compression_opts=9)
    f.close()
