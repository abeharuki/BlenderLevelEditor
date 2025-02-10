import bpy
from .add_collider import MYADDON_OT_add_collider
from .add_filename import MYADDON_OT_add_filename
from .collider import OBJECT_PT_collider
from .create_ico_sphere import MYADDON_OT_create_ico_sphere
from .draw_collider import DrawCollider
from .export_scene import MYADDON_OT_export_scene
from .file_name import OBJECT_PT_file_name
from .my_menu import TOPBAR_MT_my_menu
from .stretch_vertex import MYADDON_OT_stretch_vertex

#ブレンダーに登録するアドオン情報
bl_info = {
   "name":"レベルエディタ",
   "author":"Abe Haruki",
   "version":(1,0),
   "blender":(3,3,1),
   "location":"",
   "description":"レベルエディタ",
   "warning":"",
   "wiki_url":"",
   "tracker_url":"",
   "category":"Object"
}

classes = (
MYADDON_OT_export_scene,
MYADDON_OT_create_ico_sphere,
MYADDON_OT_stretch_vertex,
TOPBAR_MT_my_menu,
MYADDON_OT_add_filename,
OBJECT_PT_file_name,
MYADDON_OT_add_collider,
OBJECT_PT_collider,
)


#アドオン有効時コールバック
def register():
    
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)
    DrawCollider.handle = bpy.types.SpaceView3D.draw_handler_add(DrawCollider.draw_collider,(),"WINDOW","POST_VIEW")
    print("レベルエディタが有効化されました")
    
#アドオン無効時コールバック
def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)
    bpy.types.SpaceView3D.draw_handler_remove(DrawCollider.handle,"WINDOW")
    
    
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
    print("レベルエディタが無効化されました")
    
    

if __name__ == "__main__":
    register()