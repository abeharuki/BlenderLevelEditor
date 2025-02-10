import bpy
import bpy.ops
import os

class MYADDON_OT_load_spawn_object(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_load_spawn_object"
    bl_label = "出現ポイントシンボルImport"
    bl_description = "出現ポイントのシンボルをImport"
    bl_options = {'REGISTER','UNDO'}

    prototype_object_name = "ProttypePlayesSpawn"
    object_name = "PlayerSpawn"

    def execute(self,context):
      print("出現ポイントのシンボルをImportします")

      #重複防止
      spawn_object = bpy.data.objects.get(MYADDON_OT_load_spawn_object.prototype_object_name)
      if spawn_object is not None:
         return{'CANCELLED'}

      addon_directory = os.path.dirname(__file__)
           relative_path = "player/player.obj"
           full_path = os.path.join(addon_directory,relative_path)

      #オブジェクトのインポート
      bpy.ops.wm.obj_import('EXEC_DEFAULT',
           filepath = full_path,display_type='THUMBNAIL',
           forward_axis='Z',up_axis='Y')
            
      #回転を適用
      bpy.ops.object.transform_apply(location=False,
          rotation=True,scale=False,properties=False,
          isolate_users=False)
      

      

      return {'FINISHED'}

class MYADDON_OT_load_spawn_object(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_load_spawn_object"
    bl_label = "出現ポイントシンボルImport"
    bl_description = "出現ポイントのシンボルをImport"
    bl_options = {'REGISTER', 'UNDO'}

    prototype_object_name = "ProttypePlayesSpawn"
    object_name = "PlayerSpawn"

    def execute(self, context):
        print("出現ポイントのシンボルをImportします")

        # 重複防止
        spawn_object = bpy.data.objects.get(MYADDON_OT_load_spawn_object.prototype_object_name)
        if spawn_object is not None:
            return {'CANCELLED'}

        addon_directory = os.path.dirname(__file__)
        relative_path = "player/player.obj"
        full_path = os.path.join(addon_directory, relative_path)

         #オブジェクトのインポート
        bpy.ops.wm.obj_import('EXEC_DEFAULT',filepath = full_path,display_type='THUMBNAIL', forward_axis='Z',up_axis='Y')

        # 回転を適用
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False, properties=False, isolate_users=False)

        #アクティブなオブジェクトを取得
        object = bpy.context.active_object
        #オブジェクトの名前変更
        object.name = MYADDON_OT_load_spawn_object.prototype_object_name
        #オブジェクトの種類
        object["type"] = MYADDON_OT_load_spawn_object.object_name

        bpy.context.collection.objects.unlink(object)

        # 最後に 'FINISHED' を返す
        return {'FINISHED'}