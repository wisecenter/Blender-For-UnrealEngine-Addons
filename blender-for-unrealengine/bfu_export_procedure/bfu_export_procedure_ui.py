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

import bpy
from .. import bfu_utils

def draw_object_export_procedure(layout, obj: bpy.types.Object):
    if bfu_utils.GetAssetType(obj) == "SkeletalMesh":
        export_procedure_prop = layout.column()
        export_procedure_prop.prop(obj, 'bfu_skeleton_export_procedure')
    elif obj.bfu_export_as_alembic:
        export_procedure_prop = layout.column()
        export_procedure_prop.prop(obj, 'bfu_alembic_export_procedure')
    elif obj.type == "CAMERA":
        export_procedure_prop = layout.column()
        export_procedure_prop.prop(obj, 'bfu_camera_export_procedure')
    else:
        export_procedure_prop = layout.column()
        export_procedure_prop.prop(obj, 'bfu_static_export_procedure')

def draw_collection_export_procedure(layout, col: bpy.types.Collection):
    export_procedure_prop = layout.column()
    export_procedure_prop.prop(col, 'bfu_collection_export_procedure')


classes = (
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)