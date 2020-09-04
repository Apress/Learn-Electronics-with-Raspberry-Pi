from mcpi.minecraft import Minecraft
import mcpi.block as block

# Find nearest empty block based on an x, z position
def getSafePos(x_pos, y_pos, z_pos):
    block_id = mc.getBlock(x_pos, y_pos, z_pos)
    # If y position is in the air then move down to find the first non-air block
    if (block_id == block.AIR.id):
        while (block_id == block.AIR.id):
            y_pos = y_pos - 1
            block_id = mc.getBlock(x_pos, y_pos, z_pos)
        # we have found the first solid block - we want to go one above that on the first air block
        y_pos = y_pos + 1
    # If y position is underground then count up to find the first air block
    else :
        while (block_id != block.AIR.id):
            y_pos = y_pos + 1
            block_id = mc.getBlock(x_pos, y_pos, z_pos)
    # Return full address
    return (x_pos, y_pos, z_pos)

mc = Minecraft.create()
mc.player.setPos(getSafePos(0, 0, 0))