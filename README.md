# Maya_Tools
Outliner_joint
import pymel.core as pm

# Create a new regular outliner in its own window
#
pm.window()
# Result: ui.Window('window1') #
pm.frameLayout( labelVisible=False )
# Result: ui.FrameLayout('window1|frameLayout15') #
panel = pm.outlinerPanel()
outliner = pm.outlinerPanel(panel, query=True,outlinerEditor=True)
pm.outlinerEditor( outliner, edit=True, mainListConnection='worldList', selectionConnection='modelList',\
 showShapes=False, showReferenceNodes=False, showReferenceMembers=False, showAttributes=False, showConnected=False, \
 showAnimCurvesOnly=False, autoExpand=False, showDagOnly=True, ignoreDagHierarchy=False, expandConnections=False, \
 showNamespace=True, showCompounds=True, showNumericAttrsOnly=False, highlightActive=True, autoSelectNewObjects=False, \
 doNotSelectNewObjects=False, transmitFilters=False, showSetMembers=True, setFilter='defaultSetFilter' )
# Result: ui.OutlinerEditor('window1|frameLayout15|outlinerPanel2|outlinerPanel2|outlinerPanel2|outlinerPanel2') #
pm.showWindow()
