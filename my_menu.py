import bpy

class TOPBAR_MT_my_menu(bpy.types.Menu):
    bl_idname = "TOPBAR_MT_my_menu"
    bl_label = "MyMenu"
    bl_description = "拡張メニュー by" + bl_info["author"]
    
    def draw(self,context):
        self.layout.operator(MYADDON_OT_stretch_vertex.bl_idname,text = MYADDON_OT_stretch_vertex.bl_label)
        self.layout.operator(MYADDON_OT_create_ico_sphere.bl_idname,text = MYADDON_OT_create_ico_sphere.bl_label)
        self.layout.operator(MYADDON_OT_export_scene.bl_idname,text = MYADDON_OT_export_scene.bl_label)
        #self.layout.operator(MYADDON_OT_add_filename.bl_idname,text = MYADDON_OT_add_filename.bl_label)
      
        
        
    def submenu(self,context):
        self.layout.menu(TOPBAR_MT_my_menu.bl_idname)