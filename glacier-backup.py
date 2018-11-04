"""
TODO
"""
import boto3
print('hello')

# compress the target file
# ========================
# NOTE subprocess call to 7zip to create password protected zip archive
# NOTE can make it read password out of env var (PASS_VAR)
# rc = subprocess.call(['7z', 'a', '-p$PASS_VAR', '-y', 'myarchive.zip'] +
#                      ['first_file.txt', 'second.file'])
# TODO return file size
# NOTE can do this:    return os.stat(filename).st_size (this is in bytes)
# NOTE or use seek?:   file_size = file_to_upload.seek(0, 2) (this requires the file to be opened) (also in bytes)

# upload to glacier
# =================
def upload_to_glacier():
    """
    TODO
    """
    glacier = boto3.resource('glacier')

    # TODO check if its a small file

    # NOTE multipart if it's a big file (>4 mb)
    multipart_upload = glacier.MultipartUpload(
        'account_id',
        'vault_name',
        'id')

    # TODO madness with multipart checksums and tree hash?!

    # TODO complete the multipart upload
    response = glacier.complete_multipart_upload(
        vaultName='string',
        uploadId='string',
        archiveSize='string',
        checksum='string'

    # TODO write information to file as json for future checking
)
## if vault doesn't exist, create it
## if vault does exist
### if file is smaller than 100mb, upload
### if file is bigger than 100mb, multi-part upload
