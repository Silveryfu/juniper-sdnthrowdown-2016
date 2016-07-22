import sys_constant
from sys_ep_request import Ep_request
import pprint

if __name__ == "__main__":
    er = Ep_request()
    response = er.ep_update_lsp_ero('GROUP_ONE_SF_NY_LSP3')
    if isinstance(response, str):
        print response
    else:
        pprint.pprint(response.text)

    response = er.ep_read_lsp_by_name('GROUP_ONE_SF_NY_LSP3')
    pprint.pprint(response)