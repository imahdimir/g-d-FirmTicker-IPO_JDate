##


import pandas as pd

from githubdata import GithubData


btics_repo = 'https://github.com/imahdimir/d-Unique-BaseTickers-TSETMC'
ipo_rep = 'https://github.com/imahdimir/d-BaseTicker-IPOJDate'

btic = 'BaseTicker'
ipojdc = 'IPOJDate'

def main() :

  pass

  ##
  bticdb = GithubData(btics_repo)
  bticdb.clone_overwrite_last_version()

  ipodb = GithubData(ipo_rep)
  ipodb.clone_overwrite_last_version()
  ##
  fpn1 = bticdb.data_fps[0]
  bticdf = pd.read_parquet(fpn1)
  ##
  fpn0 = ipodb.data_fps[0]
  ipodf = pd.read_parquet(fpn0)
  ##
  ipodf = ipodf.sort_values(ipojdc)
  ##
  msk = ipodf.index.isin(bticdf.index)

  ipodf = ipodf[msk]
  df1 = ipodf[~ msk]
  ##
  ipodf.to_parquet(fpn0)
  ##
  commit_msg = 'only in BaseTickers db kept'
  ipodb.commit_and_push_to_github_data_target(message = commit_msg)
  ##
  bticdb.rmdir()
  ipodb.rmdir()


  ##

  ##

##