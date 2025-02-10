import bpy
import mathutils
    

class MYADDON_OT_add_collider(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_add_collider"
    bl_label = "コライダー追加"
    bl_description = "['collider']カスタムプロパティを追加します"
    bl_options = {"REGISTER","UNDO"}
    
    def execute(self,context):
        context.object["collider"] = "BOX"
        context.object["collider_center"] = mathutils.Vector((0,0,0))
        context.object["collider_size"] = mathutils.Vector((2,2,2))
        
        return {"FINISHED"}

class OBJECT_PT_collider(bpy.types.Panel):
    """"オブジェクトのファイルネームパネル"""
    bl_idname = "OBJECT_PT_collider"
    bl_label = "Collider"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"
    
    def draw(self,context):
        if "collider" in context.object:
            self.layout.prop(context.object,'["collider"]',text = "Type")
            self.layout.prop(context.object,'["collider_center"]',text = "Center")
            self.layout.prop(context.object,'["collider_size"]',text = "Size")
        else:
            self.layout.operator(MYADDON_OT_add_collider.bl_idname)