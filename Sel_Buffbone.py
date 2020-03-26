import maya.cmds as cmds

cmds.window()
cmds.paneLayout( configuration='quad' )
#cmds.button()
cmds.textScrollList( append=['BuffboneJ(0)', 'BuffboneJ(1)', 'BuffboneJ()'] )
#cmds.scrollField()
cmds.scrollLayout()
cmds.scrollLayout()
#cmds.columnLayout()

cmds.showWindow()

BuffboneJ = cmds.select(cmds.ls('Buffbone*' , type='joint'))
print BuffboneJ


def BuffboneJ():
    cmds.select(cmds.ls('Buffbone*' , type='joint'))
    return
    
    
BuffboneJ = cmds.ls('Buffbone*' , type='joint')