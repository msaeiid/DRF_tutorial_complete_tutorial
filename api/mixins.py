from rest_framework.permissions import IsAdminUser

from api.permissions import IsStaffEditorPermission


class IsStaffEditorPermissionMixin():
    permission_classes = [IsAdminUser, IsStaffEditorPermission, ]





class UserQuerySetMixin():
    user_field='owner'
    allow_staff_view=False

    def get_queryset(self):
        user=self.request.user
        look_up={self.user_field:user}
        qs=super().get_queryset()
        # conflict with permission which allows staff to update all if they have permission so below addresses this issue
        if self.allow_staff_view and self.request.user.is_staff:
            return qs
        else:
            return qs.filter(**look_up)