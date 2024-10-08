# ====================== BEGIN GPL LICENSE BLOCK ============================
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.	 If not, see <http://www.gnu.org/licenses/>.
#  All rights reserved.
#
# ======================= END GPL LICENSE BLOCK =============================


from . import import_module_unreal_utils
from . import config

try:
    import unreal
except ImportError:
    import unreal_engine as unreal

class ImportTaks():

    def __init__(self) -> None:
        # docs.unrealengine.com/5.4/en-US/PythonAPI/class/AssetImportTask.html
        self.task = unreal.AssetImportTask()
        self.task_option = None

        if config.force_use_interchange == "Interchange":
            self.use_interchange = True

        elif config.force_use_interchange == "FBX":
            self.use_interchange = False

        if import_module_unreal_utils.is_unreal_version_greater_or_equal(5,5):
            # Set values inside unreal.InterchangeGenericAssetsPipeline (unreal.InterchangeGenericCommonMeshesProperties or ...)
            self.use_interchange = True
        else:
            # Set values inside unreal.FbxStaticMeshImportData or ...
            self.use_interchange = False

    def set_task_option(self, new_task_option):
        self.task_option = new_task_option

    def get_task(self):
        return self.task
    
    def GetFbxImportUI(self) -> unreal.FbxImportUI:
        return self.task_option
    
    def GetAbcImportSettings(self) -> unreal.AbcImportSettings:
        return self.task_option

    def GetStaticMeshImportData(self) -> unreal.FbxStaticMeshImportData:
        return self.task_option.static_mesh_import_data

    def GetSkeletalMeshImportData(self) -> unreal.FbxSkeletalMeshImportData:
        return self.task_option.skeletal_mesh_import_data

    def GetAnimationImportData(self) -> unreal.FbxAnimSequenceImportData:
        return self.task_option.anim_sequence_import_data
    
    def GetTextureImportData(self) -> unreal.FbxTextureImportData:
        return self.task_option.texture_import_data

    def GetAlembicImportData(self):
        return self.task_option


    def GetIGAP(self):
        # unreal.InterchangeGenericAssetsPipeline
        return self.task_option
    
    def GetIGAP_Mesh(self):
        # unreal.InterchangeGenericMeshPipeline
        return self.task_option.get_editor_property('mesh_pipeline')
    
    def GetIGAP_SKMesh(self):
        # unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties
        return self.task_option.get_editor_property('common_skeletal_meshes_and_animations_properties')
    
    def GetIGAP_CommonMeshs(self):
        # unreal.InterchangeGenericCommonMeshesProperties
        return self.task_option.get_editor_property('common_meshes_properties')

    def GetIGAP_Mat(self):
        # unreal.InterchangeGenericMaterialPipeline
        return self.task_option.get_editor_property('material_pipeline')
    
    def GetIGAP_Tex(self):
        # unreal.InterchangeGenericTexturePipeline
        return self.task_option.get_editor_property('material_pipeline').get_editor_property('texture_pipeline')
    
    def GetIGAP_Anim(self):
        # unreal.InterchangeGenericAnimationPipeline
        return self.task_option.get_editor_property('animation_pipeline')
    
    def GetImportedAssets(self):
        assets = []
        for imported_object_path in self.task.imported_object_paths:
            asset = unreal.find_asset(imported_object_path)
            if asset:
                assets.append(asset)
        return assets
    
    def GetImportedStaticMeshAsset(self):
        # unreal.StaticMesh
        for imported_object_path in self.task.imported_object_paths:
            asset = unreal.find_asset(imported_object_path)
            if asset:
                if type(asset) is unreal.StaticMesh:
                    return asset
                
    def GetImportedSkeletonAsset(self):
        # unreal.Skeleton
        for imported_object_path in self.task.imported_object_paths:
            asset = unreal.find_asset(imported_object_path)
            if asset:
                if type(asset) is unreal.Skeleton:
                    return asset

    
    def GetImportedSkeletalMeshAsset(self):
        # unreal.SkeletalMesh
        for imported_object_path in self.task.imported_object_paths:
            asset = unreal.find_asset(imported_object_path)
            if asset:
                if type(asset) is unreal.SkeletalMesh:
                    return asset
    
    def GetImportedAnimSequenceAsset(self):
        # unreal.AnimSequence
        for imported_object_path in self.task.imported_object_paths:
            asset = unreal.find_asset(imported_object_path)
            if asset:
                if type(asset) is unreal.AnimSequence:
                    return asset
    
    def import_asset_task(self):
        print("import - S1")
        if self.use_interchange:
            print("import - S2")
            self.task.set_editor_property('options', unreal.InterchangePipelineStackOverride())
            self.task.get_editor_property('options').add_pipeline(self.task_option)
        else:
            print("import - S3")
            self.task.set_editor_property('options', self.task_option)

        print("import - S4")
        unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([self.task])