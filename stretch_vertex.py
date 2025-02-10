import bpy
import gpu
import gpu_extras.batch
import copy
import mathutils

class MYADDON_OT_stretch_vertex(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_stretch_vertex"
    bl_label = "頂点を伸ばす"
    bl_description = "頂点座標系を引っ張て伸ばします"
    bl_options = {'REGISTER','UNDO'}
    
    def execute(self,context):
        bpy.data.objects["Cube"].data.vertices[0].co.x +=1.0
        print("頂点を伸ばしました")
        
        return {'FINISHED'}