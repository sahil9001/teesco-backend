from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *
from org.custom_model_field import Permissions
from slugify import slugify
from rest_framework.response import Response
import uuid
from org import responses


class CreateOrgSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=False)
    tagline = serializers.CharField(allow_blank=False)
    profile_pic = serializers.ImageField(required=False)

    def save(self):
        # get validated data from serializer
        valid_data = self.validated_data

        # generate a unique route slug
        # by prefixing it with its org.id the unquiness is ensured
        # this method makes it to be semi-readable
        last_org_id = 0
        if Org.objects.count() > 0:
            last_org_id = Org.objects.last().id + 1

        route_slug = str(last_org_id) + ' ' + valid_data['name']
        route_slug = slugify(route_slug, max_length=40)

        # create the org
        org = Org.objects.create(
            route_slug=route_slug,
            name=valid_data['name'],
            tagline=valid_data['tagline'],
            profile_pic=valid_data.get('profile_pic', None)
        )

        # create default group permissions
        volunteer_permissions = Permissions()
        admin_permissions = Permissions()

        admin_permissions.set_permissions([
            Permissions.IS_ADMIN,
            Permissions.IS_STAFF,
            Permissions.CAN_CREATE_TASKS,
            Permissions.CAN_REPLY_TO_QUERIES,
            Permissions.CAN_REVIEW_PROOFS,
        ])

        # creating invite slugs
        # this method is used because we dont need a
        # readable link this time
        admin_group_invite_slug = str(org.id)+'-'+str(uuid.uuid4())
        volunteer_group_invite_slug = str(org.id)+'-'+str(uuid.uuid4())

        # Creating default groups
        admin_group = Group.objects.create(
            name='Admin',
            role='''This group is for owners/top level members of the org. 
                Members of this group has access to every place within the org.''',
            invite_slug=admin_group_invite_slug,
            org=org,
            perm_obj=admin_permissions
        )
        volunteer_group = Group.objects.create(
            name='Volunteer',
            role='''When a person clicks join org button of his own without a 
                invite link then he will be put into this group.''',
            invite_slug=volunteer_group_invite_slug,
            org=org,
            perm_obj=volunteer_permissions,
        )
        return [org, admin_group]


class EditOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org
        fields = ('name', 'tagline', 'about')
