"""


  """
##
import pandas as pd

from githubdata import GithubData
from mirutil.df_utils import read_data_according_to_type as read_data
from mirutil.string_funcs import normalize_fa_str_completely as norm_comp
from mirutil.tsetmc import search_tsetmc_ret_df as srch_tsetmc
from mirutil.df_utils import save_as_prq_wo_index as save_as_prq
from mirutil import utils as mu
from persiantools.jdatetime import JalaliDate


targ_url = 'imahdimir/d-firms-IPO-date'

cipojd = 'IPO_JDate'
cftic = 'FirmTicker'
cdt = 'Date'

def main() :
  pass
  ##
  rp_ipo = GithubData(targ_url)
  rp_ipo.clone()
  ##
  dipp = rp_ipo.data_fp
  dip = read_data(dipp)
  ##
  dip[cdt] = dip[
    cipojd].apply(lambda x : JalaliDate.fromisoformat(x).to_gregorian())
  ##
  assert dip[cftic].is_unique
  ##
  save_as_prq(dip , dipp)
  ##
  tokp = '/Users/mahdi/Dropbox/tok.txt'
  tok = mu.get_tok_if_accessible(tokp)
  ##
  msg = 'for duplicated firm tickers kept the earlier date'
  rp_ipo.commit_and_push(msg , user = rp_ipo.user_name , token = tok)

  ##


  rp_ipo.rmdir()


  ##


  ##

##


if __name__ == '__main__' :
  main()

##