import comtypes.client as cm
etabs_object=cm.GetActiveObject("CSI.ETABS.API.ETABSObject")
SapModel = etabs_object.SapModel

# Unlocking model
SapModel.SetModelIsLocked(False)
#SapModel.SetPresentUnits(14)
etabs_file=SapModel.File
#Methods: OpenFile, Save
load_pattern=SapModel.LoadPatterns
#Methods: Add, GetNameList, GetLoadType, GetAutoSeismicCode
autoseismic=load_pattern.AutoSeismic
#Methods: GetIBC2006, SetIBC2006
Analyze=SapModel.Analyze
#RunAnalysis, SetRunCaseFlag, GetCaseStatus, GetRunCaseFlag
FrameObj=SapModel.FrameObj
#Count, GetLabelNameList, SetSection, GetSection, GetLabelFromName, GetNameListOnStory, GetDesignProcedure, GetPoints
PointObj=SapModel.PointObj
#%Methods: GetCoordCartesian, GetConnectivity
LoadCases=SapModel.LoadCases
#%Methods: GetNameList, GetTypeOAPI_1,
PropFrame=SapModel.PropFrame
#%Methods: Count, GetAllFrameProperties, GetNameList, GetRebarColumn, SetISection, SetPipe, SetRectangle, SetRebarColumn, SetRebarBeam, SetTube,
PropArea=SapModel.PropArea
#%Methods: Count, GetWall, GetNameList, SetWall,
Group=SapModel.GroupDef
#%Methods: GetNameList, GetAssignments, GetGroup
Story=SapModel.Story
#%Methods: GetElevation, GetHeight, GetNameList,
DesignConcrete=SapModel.DesignConcrete
#%Methods: GetCode, GetSummaryResultsBeam, GetSummaryResultsColumn, GetSummaryResultsJoint, SetCode, SetDesignSection, StartDesign
ACI318_08_IBC2009=DesignConcrete.ACI318_08_IBC2009
#%Methods: SetOverwrite

Combination=SapModel.RespCombo
#%Methods: Add, Delete, GetNameList, GetTypeCombo, SetCaseList
DesignSteel=SapModel.DesignSteel
#%Methods: GetCode, GetComboDeflection, GetComboStrength, GetSummaryResults, GetSummaryResults_2, StartDesign, VerifyPassed,

#%Methods: SetOverwrite

AnalysisResults=SapModel.Results
#%Methods: BaseReact, BaseReactWithCentroid, GeneralizedDispl, JointDrifts, ModalParticipatingMassRatios, ModalPeriod, StoryDrifts
AnalysisResultsSetup=AnalysisResults.Setup

#%Methods: GetComboSelectedForOutput, SetCaseSelectedForOutput, SetComboSelectedForOutput, SetOptionModeShape
AreaObj=SapModel.AreaObj
#%Methods: Count, GetLabelNameList, GetNameFromLabel, GetNameListOnStory, GetPier, GetRebarDataPier, GetRebarDataSpandrel, SetDiaphragm, SetLoadUniformToFrame, SetLoadUniform, SetModifiers,
ResponseSpectrum=LoadCases.ResponseSpectrum
#%Methods: GetLoads,
Detailing=SapModel.Detailing
#%Methods: StartDetailing, GetBeamLongRebarData, GetBeamTieRebarData, GetColumnLongRebarData, GetColumnTieRebarData, GetDetailedBeamLineData, GetDetailedColumnStackData

Select=SapModel.SelectObj
#%Methods: All, Group, PreviousSelection, ClearSelection
story=SapModel.Story