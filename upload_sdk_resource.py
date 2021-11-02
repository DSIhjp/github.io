import os

from qiniu import Auth, put_file

# QINIU_CONFIG = {
#     'QINIU_SECRET_KEY': 'jTJLOOBdqK0twf93DcVPzXSaecq6i2TD-z2OguOx',
#     'QINIU_ACCESS_KEY': 'Si90ojma7MpLndO-MyBFIrHbtEdjPWEA38hAN8tV',
#     'QINIU_BUCKET_NAME': 'res-youyunad-cdnsource-test',
# }

QINIU_CONFIG = {
    'QINIU_SECRET_KEY': 'jTJLOOBdqK0twf93DcVPzXSaecq6i2TD-z2OguOx',
    'QINIU_ACCESS_KEY': 'Si90ojma7MpLndO-MyBFIrHbtEdjPWEA38hAN8tV',
    'QINIU_BUCKET_NAME': 'res-youyunad-cdnsource',
}


def upload_file(source_file, target_file):
    access_key = QINIU_CONFIG.get('QINIU_ACCESS_KEY')
    secret_key = QINIU_CONFIG.get('QINIU_SECRET_KEY')
    bucket_name = QINIU_CONFIG.get('QINIU_BUCKET_NAME')
    key = target_file
    auth = Auth(access_key, secret_key)
    token = auth.upload_token(bucket_name, key, 3600)
    ret, info = put_file(token, key, source_file)
    return info


def parse_argument():
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument('-p', '--platform', choices=['android', 'iOS'], required=True,
                        help='the sdk resource of the platform')
    parser.add_argument('-f', '--source_file', required=True, help='the full path of sdk resource, '
                                                                   'the file type require Zip archive data')
    _args = parser.parse_args()
    return _args


if __name__ == '__main__':
    args = parse_argument()
    platform = args.platform
    _source_file = args.source_file
    _target_file = os.path.join('sdk_res', platform, _source_file.split('/')[-1])
    file_type = os.path.splitext(_target_file)[-1]
    if file_type != '.zip':
        raise Exception('invalid file type:{0}, the file type require Zip archive data'.format(file_type))
    if not os.path.exists(_source_file):
        raise Exception('{0} not exists'.format(_source_file))

    print('platform is {0}'.format(platform))
    print('_source_file is {0}'.format(_source_file))
    print('_target_file is {0}'.format(_target_file))
    _info = upload_file(_source_file, _target_file)
    if _info.status_code == 200:
        print('file upload success, the download url is {0}'.format('http://res.youyunad.com/{0}'.format(_target_file)))
    else:
        raise Exception('{0} upload fail'.format(_source_file))
