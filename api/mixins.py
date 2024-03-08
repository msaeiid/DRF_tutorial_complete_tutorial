from rest_framework.permissions import IsAdminUser

from api.permissions import IsStaffEditorPermission


class IsStaffEditorPermissionMixin():
    permission_classes = [IsAdminUser, IsStaffEditorPermission, ]
