from permission.logics import AuthorPermissionLogic
from permission.logics import CollaboratorsPermissionLogic

PERMISSION_LOGICS = (
    ('permiso.permiso', AuthorPermissionLogic()),
    ('permiso.permiso', CollaboratorsPermissionLogic()),
)