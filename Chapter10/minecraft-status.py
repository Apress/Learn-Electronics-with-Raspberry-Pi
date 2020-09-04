from mcpi.minecraft import Minecraft

mc = Minecraft.create()

position = mc.player.getTilePos()

print ("X position :"+str(position.x)+", Y position :"+str(position.y)+", Z position:"+str(position.z))