import bpy
import os

class SpawnNames():

    #インデックス
    PROTOTYPE = 0
    INSTANCE = 1
    FILENAME = 2

    names = {}
    names["Enemy"] = ("PrototypeEnemySpawn","EnemySpawn","enemy/enemy.obj")
    names["Player"] = ("PrototypePlayerSpawn","PlayerSpawn","player/player.obj")

#読み込み
class MYADDON_OT_load_spawn_object(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_load_spawn_object"
    bl_label = "出現ポイントシンボルImport"
    bl_description = "出現ポイントのシンボルをImport"
    bl_options = {'REGISTER', 'UNDO'}


    def load_obj(self, type):
        print("出現ポイントのシンボルをImportします")

        # 重複防止
        spawn_object = bpy.data.objects.get(SpawnNames.names[type][SpawnNames.PROTOTYPE])
        if spawn_object is not None:
           return {'CANCELLED'}

        addon_directory = os.path.dirname(__file__)
        relative_path = SpawnNames.names[type][SpawnNames.FILENAME]
        full_path = os.path.join(addon_directory, relative_path)

         #オブジェクトのインポート
        bpy.ops.wm.obj_import('EXEC_DEFAULT',filepath = full_path,display_type='THUMBNAIL', forward_axis='Z',up_axis='Y')

        # 回転を適用
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False, properties=False, isolate_users=False)

        #アクティブなオブジェクトを取得
        object = bpy.context.active_object
        #オブジェクトの名前変更
        object.name = SpawnNames.names[type][SpawnNames.PROTOTYPE]
        #オブジェクトの種類
        object["type"] = SpawnNames.names[type][SpawnNames.INSTANCE]

        bpy.context.collection.objects.unlink(object)

        # 最後に 'FINISHED' を返す
        return {'FINISHED'}

    def execute(self,context):
        self.load_obj("Enemy")
        self.load_obj("Player")

        return {'FINISHED'}




#作成
class MYADDON_OT_make_spawn_object(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_make_spawn_object"
    bl_label = "出現ポイントシンボルの作成"
    bl_description = "出現ポイントのシンボルを作成"
    bl_options = {'REGISTER', 'UNDO'}

    type: bpy.props.StringProperty(name="Type",default="Player")

    def execute(self, context):
        # 重複防止
        spawn_object = bpy.data.objects.get(SpawnNames.names[self.type][SpawnNames.PROTOTYPE])
        if spawn_object is None:
            bpy.ops.myaddon_ot_load_spawn_object('EXEC_DEFAULT')
            #再検索
            spawn_object = bpy.data.objects.get(SpawnNames.names[self.type][SpawnNames.PROTOTYPE])

        print("出現ポイントのシンボルを作成します")
        bpy.ops.object.select_all(action='DESELECT')
       
        #オブジェクトを複製
        object = spawn_object.copy()
        #オブジェクトを現在のシーンにリンク
        bpy.context.collection.objects.link(object)
        #オブジェクトの名を変更
        object.name = SpawnNames.names[self.type][SpawnNames.INSTANCE]
       
        # 最後に 'FINISHED' を返す
        return {'FINISHED'}


class MYADDON_OT_make_player_spawn_object(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_make_player_spawn_object"
    bl_label = "プレイヤー出現ポイントシンボルの作成"
    bl_description = "プレイヤー出現ポイントのシンボルを作成"
    
    def execute(self, context):
        bpy.ops.myaddon.myaddon_ot_make_spawn_object('EXEC_DEFAULT',type = "Player")
        return{'FINISHED'}  

class MYADDON_OT_make_enemy_spawn_object(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_make_enemy_spawn_object"
    bl_label = "敵出現ポイントシンボルの作成"
    bl_description = "敵出現ポイントのシンボルを作成"
    
    def execute(self, context):
        bpy.ops.myaddon.myaddon_ot_make_spawn_object('EXEC_DEFAULT',type = "Enemy")
        return{'FINISHED'}  