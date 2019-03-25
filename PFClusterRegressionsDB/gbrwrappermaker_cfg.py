import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

# Define a process
process = cms.Process("Demo")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )
process.source = cms.Source("EmptySource",)

# Read arguments
options = VarParsing("analysis")
options.register ('name', '', VarParsing.multiplicity.singleton, VarParsing.varType.string, "DB label (and sqlite file)")
options.register ('file', '', VarParsing.multiplicity.singleton, VarParsing.varType.string, "ROOT file")
options.register ('obj', '', VarParsing.multiplicity.singleton, VarParsing.varType.string, "GBRForestD object")
options.parseArguments()

# Load executable library
process.gbrwrappermaker = cms.EDAnalyzer('GBRWrapperMaker',
                                         payloadname = cms.string(options.name),
                                         payloadobj  = cms.string(options.obj),
                                         payloadfile = cms.string(options.file))

# Write output        
process.load("CondCore.DBCommon.CondDBCommon_cfi")
process.CondDBCommon.connect = 'sqlite_file:%s.db' % options.name
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          process.CondDBCommon,
                                          timetype = cms.untracked.string('runnumber'),
                                          toPut = cms.VPSet(
        cms.PSet(
            record = cms.string(options.name),
            tag    = cms.string(options.name)
            ),
        
        )
                                          )
# Run                                    
process.p = cms.Path(process.gbrwrappermaker)
