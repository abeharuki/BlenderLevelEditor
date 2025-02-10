import bpy
import bpy.ops
import os

#読み込み
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

#作成
class MYADDON_OT_make_spawn_object(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_make_spawn_object"
    bl_label = "出現ポイントシンボルの作成"
    bl_description = "出現ポイントのシンボルを作成"
    bl_options = {'REGISTER', 'UNDO'}

    prototype_object_name = "ProttypePlayesSpawn"
    object_name = "PlayerSpawn"

    def execute(self, context):
        # 重複防止
        spawn_object = bpy.data.objects.get(MYADDON_OT_make_spawn_object.prototype_object_name)
        if spawn_object is None:
            bpy.ops.myaddon_ot_make_spawn_object('EXEC_DEFAULT')
            #再検索
            spawn_object = bpy.data.objects.get(MYADDON_OT_make_spawn_object.prototype_object_name)

        print("出現ポイントのシンボルを作成します")
        bpy.ops.object.select_all(action='DESELECT')
       
        #オブジェクトを複製
        object = spawn_object.copy()
        #オブジェクトを現在のシーンにリンク
        bpy.context.collection.objects.link(object)
        #オブジェクトの名を変更
        object.name = MYADDON_OT_make_spawn_object.object_name
       
        # 最後に 'FINISHED' を返す
        return {'FINISHED'}