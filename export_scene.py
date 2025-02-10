import bpy
import bpy_extras

class MYADDON_OT_export_scene(bpy.types.Operator,bpy_extras.io_utils.ExportHelper):
    bl_idname = "myaddon.myaddon_ot_export_scene"
    bl_label = "シーンの出力"
    bl_description = "シーン情報をExportします"
    
    filename_ext = ".scene"
    
    def parse_scene_recursive(self,file,object,level):
        """シーン解析用再起関数"""
        
        indent = ''
        for i in range(level):
            indent += "\t"
        
        self.write_and_print(file, indent + object.type)
        #self.write_and_print(file, indent + object.type + " - " + object.name)
        trans, rot, scale = object.matrix_local.decompose()
        rot = rot.to_euler()
         
        rot.x = math.degrees(rot.x)
        rot.y = math.degrees(rot.y)
        rot.z = math.degrees(rot.z)
         
        self.write_and_print(file,indent + "Trans(%f,%f,%f)" % (trans.x,trans.y,trans.z))
        self.write_and_print(file,indent + "Rot(%f,%f,%f)" % (rot.x,rot.y,rot.z))
        self.write_and_print(file,indent +  "Scale(%f,%f,%f)" % (scale.x,scale.y,scale.z))
        if "file_name" in object:
             self.write_and_print(file,indent + "Name %s" % object["file_name"])
        self.write_and_print(file, indent + 'END')
        self.write_and_print(file, '')
        
        for child in object.children:
            self.parse_scene_recursive(file,child,level + 1)
                 
    def write_and_print(self,file,str):
        print(str)
        
        file.write(str)
        file.write('\n')
        
    def export(self):
        """ファイルに出力"""
        print("シーン情報出力開始. . . %r" % self.filepath)
        
        
        with open(self.filepath, "wt") as file:
            file.write("SCENE\n")
            
            for object in bpy.context.scene.objects:
                if(object.parent):
                    continue
                self.parse_scene_recursive(file,object,0)
                
    
    def execute(self,context):
        
        
        print("シーン情報をExportします")
        
        self.export()
        
        self.report({'INFO'},"シーン情報をExportします")
        return {'FINISHED'}





