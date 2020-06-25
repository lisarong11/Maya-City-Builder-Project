import maya.cmds as cmds
import random
import math as math
"""
This function generate two kinds of city,square and circle,with user input value of building details and city settings
The program contian three main functions:
1.generate of building in single block
2.move of blocks in square shape
3.move of blocks in circle shape
"""

def delete():
    """
    This function select all the existing object and delete
    param name: no parameters
    return value: no return value
    """
    cmds.select(all=True)
    cmds.delete()
def buildtheblock(buwidth,budepth,bugap,bucount,buxnum,buznum):
    """
    This function build the city inside the block with accepting values from UI
    param name:
    buwidth= building width(in x direction)
    budepth=building depth(in z direction)
    bugap= gap between each building
    bucount= counting value for the for loop
    buxnum= building number in x direction
    buznum= building number in z direction
    return value: no return value
    """	
    But=random.randrange(1,3)
    if But ==1:
        building_in_block(buwidth,budepth,bugap,bucount,buxnum,buznum)
    else:
        flat_in_block(buwidth,budepth,bugap,bucount,buxnum,buznum)

           
    

def selectallbuildings(buxnum,buznum): 
    """
    This function select all buildings in one block and combine them 
    param name:
    buxnum= building in x direction
    buznum= building in z direction
    return value: no return value
    """     
    #select all the individual building      
    for bucount in range(1,(buxnum*buznum)+1):
        print bucount
        buname='building'+str(bucount)
        print buname
        cmds.select(buname,add=True)
            
    cmds.polyUnite(n='block')
    cmds.delete(ch=True)
#circle calculation
def circlecal(r,div,c,buwidth,budepth,bugap,bucount,buxnum,buznum):
    """
    This function display the blocks into a circle city by accepting value from UI
    param name:
    r= initial radius of the city
    div= subdivition of each 90 degree of the circle
    c= counting value use for the for loop
    buwidth= building width(in x direction)
    budepth=building depth(in z direction)
    bugap= gap between each building
    bucount= counting value for the for loop
    buxnum= building number in x direction
    buznum= building number in z direction
    return value: no return value
    """
    for x in range(1,div+1):
        zv=math.sin(90-90/div*c)*r
        xv=math.cos(90-90/div*c)*r

        buildtheblock(buwidth,budepth,bugap,bucount,buxnum,buznum)
        cmds.move(xv,0,zv)
        buildtheblock(buwidth,budepth,bugap,bucount,buxnum,buznum)
        cmds.move(xv,0,-zv)
        buildtheblock(buwidth,budepth,bugap,bucount,buxnum,buznum)
        cmds.move(-xv,0,-zv)
        buildtheblock(buwidth,budepth,bugap,bucount,buxnum,buznum)
        cmds.move(-xv,0,zv)
        c+=1
              
 
def flat_in_block(buwidth,budepth,bugap,bucount,buxnum,buznum):
    """
    This function build low buildings in one block by recieved value from UI and randomly select from three different roof
    param name:
    buwidth= building width(in x direction)
    budepth=building depth(in z direction)
    bugap= gap between each building
    bucount= counting value for the for loop
    buxnum= building number in x direction
    buznum= building number in z direction
    return value: no return value
    """
    for x in range(0,buxnum):
        for z in range(0,buznum):
            height=random.randrange(4,9)

            Bu=cmds.polyCube(w=buwidth,d=budepth,h=height,name='building1',sx=3,sy=6,sz=4)
            cmds.move((buwidth+bugap)*x,(height+blockheight)/2,(budepth+bugap)*z)

            BUT=random.randrange(1,4)
            buname='building'+str(bucount)
            if BUT==1:
                cmds.polyExtrudeFacet(str(buname)+'.f[104:107]',translateX=-buwidth/3,translateY=-0.5)
            elif BUT==2:
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',translateY=0.5,s=(1.5,1.5,1.5))
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',translateY=3,s=(0.5,0.5,0.3))
                cmds.polyExtrudeFacet(str(buname)+'.f[19]',translateY=2)
               
            else:
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',translateY=0.5,s=(2,2,2))
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',translateY=1)
            #window               
            cmds.polyExtrudeFacet(str(buname)+'.f[97:98]',translateX=buwidth/4,s=(0.8,0.8,0.8))
            cmds.polyExtrudeFacet(str(buname)+'.f[93:94]',translateX=buwidth/4,s=(0.8,0.8,0.8))
            cmds.polyExtrudeFacet(str(buname)+'.f[69:70]',translateX=-buwidth/4,s=(0.8,0.8,0.8))
            cmds.polyExtrudeFacet(str(buname)+'.f[73:74]',translateX=-buwidth/4,s=(0.8,0.8,0.8))
            bucount+=1
            #door
            cmds.polyExtrudeFacet(str(buname)+'.f[42:43]',translateZ=buwidth/3,s=(0.8,0.8,0.8))
            cmds.polyExtrudeFacet(str(buname)+'.f[45:46]',translateZ=buwidth/3,s=(0.8,0.8,0.8))

            cmds.refresh()
    selectallbuildings(buxnum,buznum)

   
def building_in_block(buwidth,budepth,bugap,bucount,buxnum,buznum):
    """
    This function build tall buildings in one block by recieved value from UI and randomly select from three different roof
    param name:
    buwidth= building width(in x direction)
    budepth=building depth(in z direction)
    bugap= gap between each building
    bucount= counting value for the for loop
    buxnum= building number in x direction
    buznum= building number in z direction
    return value: no return value
    """
    for x in range(0,buxnum):
        for z in range(0,buznum):
            #cube for building
            height=random.randrange(10,20)
            Bu=cmds.polyCube(w=buwidth,d=budepth,h=height,name='building1',sx=3,sy=6,sz=4)
            cmds.move((buwidth+bugap)*x,height/2,(budepth+bugap)*z)
            #random choose of roof
            BUT=random.randrange(1,4)
            buname='building'+str(bucount)
            if BUT==1:
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',offset=0.2,translateY=height/16)
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',translateY=height/14,s=(0.5,0.5,0.5))
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',offset=0.1,translateY=height/5)
                
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',s=(0.2,0.2,0.2),translateY=height/8)
            elif BUT==2:
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',offset=0.1)
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',s=(0.8,0.8,0.8),translateY=-1)
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',offset=0.3) 
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',translateY=2,s=(0.5,0.5,0.5)) 
            else:
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',ls=(0.1,0.1,0.1),t=(0.5,1,0),offset=0.3)
                cmds.polyExtrudeFacet(str(buname)+'.f[18:29]',s=(0.1,0.5,1),t=(0.5,2,0))
   
            cmds.polyExtrudeFacet(str(buname)+'.f[3:17]',offset=0.2,kft=False,translateZ=-0.08)
            cmds.polyExtrudeFacet(str(buname)+'.f[30:44]',offset=0.2,kft=False,translateZ=0.08)
            cmds.polyExtrudeFacet(str(buname)+'.f[64:83]',offset=0.2,kft=False,translateX=-0.08)   
            cmds.polyExtrudeFacet(str(buname)+'.f[88:107]',offset=0.2,kft=False,translateX=0.08)  
            bucount+=1
            cmds.refresh()
    selectallbuildings(buxnum,buznum)
def street_streetlight(blockwidth,buwidth,blockdepth,budepth,blockxnum,blockznum,street):
    """
    This function build the street and street light and move them into the corresponding place
    param name:
    blockwidth= block width(in x direction) 
    buwidth= building width(in x direction)
    blockdepth=block depth(in z direction)
    budepth=building depth(in z direction)
    blockxnum= block number in x direction
    blockznum= block number in z direction
    street= street width
    return value: no return value
    """
    streetxin=blockwidth-buwidth/2+street/2
    streetzin=blockdepth-budepth/2+street/2
    for a in range(0,blockznum):
        
          Bu=cmds.polyCube(w=1.1*(blockwidth*blockxnum+street*(blockxnum-1)),d=street*1.3,h=streetheight,name='street')
          cmds.move(((blockxnum)*(blockwidth+street)-buwidth)/2,0,streetzin+a*(blockdepth+street))
    for b in range(0,blockxnum):
          Bu=cmds.polyCube(w=street*1.3,d=1.1*(blockdepth*blockznum+street*(blockznum-1)),h=streetheight,name='street')
          cmds.move(streetxin+b*(street+blockwidth),0,((blockdepth*blockznum+(blockznum-1)*street)-budepth)/2)

    strhcount=1
    for a in range(0,blockznum):
        for b in range(0,blockxnum+1):
            
            buname='streetlight'+str(strhcount)
            Bu=cmds.polyCube(w=0.4,d=0.4,h=2,name='streetlight1')
            cmds.polyExtrudeFacet(str(buname)+'.f[1]',translateY=0.5)
            cmds.polyExtrudeFacet(str(buname)+'.f[6]',translateZ=1)
            cmds.move(b*blockwidth-buwidth/2,streetheight+1,blockdepth+a*(blockdepth+street)-budepth/2,str(buname))
            strhcount+=1
    strhcountr=1
    for a in range(0,blockznum):
        for b in range(0,blockxnum+2):
            buname='streetlightr'+str(strhcountr)
            Bu=cmds.polyCube(w=0.4,d=0.4,h=2,name='streetlightr1')
            cmds.polyExtrudeFacet(str(buname)+'.f[1]',translateY=0.5)
            cmds.polyExtrudeFacet(str(buname)+'.f[8]',translateZ=-1)
            cmds.move(b*blockwidth-buwidth/2,streetheight+1,blockdepth+a*(blockdepth+street)-budepth/2+street*4/5,str(buname))
            strhcountr+=1

blockheight=4
streetheight=1

bucount=1
def GUI():
    """
    THis function design the interface of the program
    """
    if cmds.window('citybuilder',exists=True):
        cmds.deleteUI('citybuilder')
    window1=cmds.window('citybuilder',w=400,h=200)
    cmds.columnLayout(columnAttach=('right',10),rs=30,cw=200,adjustableColumn=True)

    budepth=cmds.intSliderGrp('bud',label='building depth',minValue=2,maxValue=10,value=6,field=True)
    buwidth=cmds.intSliderGrp('buw',label='building width',minValue=2,maxValue=10,value=6,field=True)
    buwxnum=cmds.intSliderGrp('bux',label='building x number',minValue=2,maxValue=10,value=6,field=True)
    buznum=cmds.intSliderGrp('buz',label='building z number',minValue=2,maxValue=10,value=6,field=True)
    bugap=cmds.intSliderGrp('bg',label='building gap',minValue=2,maxValue=20,value=6,field=True)

    blockxnum=cmds.intSliderGrp('blx',label='block x number',minValue=2,maxValue=10,value=6,field=True)
    blockznum=cmds.intSliderGrp('blz',label='block z number',minValue=2,maxValue=10,value=6,field=True)
    street=cmds.intSliderGrp('sw',label='street width',minValue=2,maxValue=20,value=6,field=True)

    circlegap=cmds.intSliderGrp('cg',label='circle gap',minValue=30,maxValue=80,value=65,field=True)
    initialradius=cmds.intSliderGrp('ir',label='initial radius',minValue=50,maxValue=100,value=80,field=True)
    circletime=cmds.intSliderGrp('ct',label='circlet ime',minValue=2,maxValue=6,value=4,field=True)
    divition=cmds.intSliderGrp('div',label='circle divitions',minValue=2,maxValue=6,value=4,field=True)

    cors=cmds.optionMenu('cors',w=300,label='circle or square')
    cmds.menuItem(label='')
    cmds.menuItem(label='circle')
    cmds.menuItem(label='square')

    cmds.button(label='ok',c='start()')
    cmds.button(label='delete',c='delete()')
    cmds.button(label='random')
    cmds.showWindow(window1)
if __name__=="__main__":
	GUI()
def start():
    """
    This function recived value from GUI and make selction between square and circle city 
    param name: no parameter
    return value: no return value
    """
    div=cmds.intSliderGrp('div',query=True,value=True)
    time=cmds.intSliderGrp('ct',query=True,value=True)
    r=cmds.intSliderGrp('ir',query=True,value=True)
    circlegap=cmds.intSliderGrp('cg',query=True,value=True)

    blocktype=cmds.optionMenu('cors',query=True,value=True)

    budepth=cmds.intSliderGrp('bud',query=True,value=True)
    buwidth=cmds.intSliderGrp('buw',query=True,value=True)
    buxnum=cmds.intSliderGrp('bux',query=True,value=True)
    buznum=cmds.intSliderGrp('buz',query=True,value=True)

    blockxnum=cmds.intSliderGrp('blx',query=True,value=True)
    blockznum=cmds.intSliderGrp('blz',query=True,value=True)
    street=cmds.intSliderGrp('sw',query=True,value=True)
    bugap=cmds.intSliderGrp('bg',query=True,value=True)
    blockdepth=buznum*budepth+(buxnum)*bugap
    blockwidth=buxnum*buwidth+(buxnum)*bugap
    if blocktype=='square':
        print 'square is select'
        for a in range(0,blockxnum):
            for b in range(0,blockznum):
               
                cmds.polyCube(w=blockwidth,d=blockdepth,h=blockheight,n='plane') 
                cmds.move(blockwidth/2-buwidth+a*(blockwidth+street),0,blockdepth/2-budepth/2+b*(blockdepth+street))
                cmds.refresh()
                But=random.randrange(1,3)
                if But ==1:
                    building_in_block(buwidth,budepth,bugap,bucount,buxnum,buznum)
                else:
                    flat_in_block(buwidth,budepth,bugap,bucount,buxnum,buznum)
 
                cmds.move(a*(blockwidth+street),0,b*(blockdepth+street))
                    
               
                cmds.refresh()

        street_streetlight(blockwidth,buwidth,blockdepth,budepth,blockxnum,blockznum,street)
        cmds.refresh()    
    else:
       print'circle is select'
       for a in range(0,time):
          buildtheblock(buwidth,budepth,bugap,bucount,buxnum,buznum)
          print'first block done'
          cmds.move(r,0,0)
          buildtheblock(buwidth,budepth,bugap,bucount,buxnum,buznum)
          cmds.move(-r,0,0)
          buildtheblock(buwidth,budepth,bugap,bucount,buxnum,buznum)
          cmds.move(0,0,r)
          buildtheblock(buwidth,budepth,bugap,bucount,buxnum,buznum)
          cmds.move(0,0,-r)
          circlecal(r,div,1,buwidth,budepth,bugap,bucount,buxnum,buznum)
          div+=1
          r+=circlegap
          
           
