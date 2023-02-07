# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE
import awkward as ak
import ROOT

def test_fun():
    df = ROOT.RDataFrame('Events', 'root://eospublic.cern.ch//eos/opendata/cms/derived-data/AOD2NanoAODOutreachTool/Run2012BC_DoubleMuParked_Muons.root')
    array = ak.from_rdataframe(df, columns="nMuon")

if __name__ == '__main__':
    test_fun()

