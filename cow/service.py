# # Copyright 2012-2014 eNovance <licensing@enovance.com>
# #
# # Licensed under the Apache License, Version 2.0 (the "License"); you may
# # not use this file except in compliance with the License. You may obtain
# # a copy of the License at
# #
# #      http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# # License for the specific language governing permissions and limitations
# # under the License.

import time

# import sys

# from oslo_config import cfg
# import oslo_i18n
# from oslo_log import log
# from oslo_reports import guru_meditation_report as gmr

# #from cow import keystone_client
# from cow import messaging
# from cow import opts
# #from cow import sample
# from cow import utils
# from cow import version


# def prepare_service(argv=None, config_files=None, conf=None):
#     if argv is None:
#         argv = sys.argv

#     if conf is None:
#         conf = cfg.ConfigOpts()

#     oslo_i18n.enable_lazy()
#     for group, options in opts.list_opts():
#         conf.register_opts(list(options),
#                            group=None if group == "DEFAULT" else group)
#     keystone_client.register_keystoneauth_opts(conf)
#     log.register_options(conf)
#     log_levels = (conf.default_log_levels +
#                   ['futurist=INFO', 'neutronclient=INFO',
#                    'keystoneclient=INFO'])
#     log.set_defaults(default_log_levels=log_levels)

#     conf(argv[1:], project='cow', validate_default_values=True,
#          version=version.version_info.version_string(),
#          default_config_files=config_files)

#     keystone_client.post_register_keystoneauth_opts(conf)

#     log.setup(conf, 'cow')
#     utils.setup_root_helper(conf)
#     # sample.setup(conf)

#     # gmr.TextGuruMeditation.setup_autorun(version)
#     messaging.setup()
#     return conf

while True:
    print('agent')
    time.sleep(5)