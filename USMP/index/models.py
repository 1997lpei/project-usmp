# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LdevList(models.Model):
    serial = models.CharField(max_length=255, blank=True, null=True)
    ldev = models.CharField(max_length=255, blank=True, null=True)
    vol_capacity = models.IntegerField(db_column='VOL_Capacity', blank=True, null=True)  # Field name made lowercase.
    ports = models.CharField(db_column='PORTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    raid_level = models.CharField(db_column='RAID_LEVEL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    raid_type = models.CharField(db_column='RAID_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    raid_groups = models.CharField(db_column='RAID_GROUPS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hostname = models.CharField(db_column='HOSTNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hlun_id = models.IntegerField(db_column='HLUN_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ldev_list'


class NasAggregate(models.Model):
    uuid = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    clusterid = models.ForeignKey('NasCluster', models.DO_NOTHING, db_column='clusterId')  # Field name made lowercase.
    nodeid = models.ForeignKey('NasNode', models.DO_NOTHING, db_column='nodeId')  # Field name made lowercase.
    state = models.CharField(max_length=255)
    sizetotal = models.CharField(db_column='sizeTotal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sizeused = models.CharField(db_column='sizeUsed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sizeusedpercent = models.FloatField(db_column='sizeUsedPercent', blank=True, null=True)  # Field name made lowercase.
    sizeavail = models.CharField(db_column='sizeAvail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sizeavailpercent = models.FloatField(db_column='sizeAvailPercent', blank=True, null=True)  # Field name made lowercase.
    raidtype = models.CharField(db_column='raidType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    raidsize = models.CharField(db_column='raidSize', max_length=10, blank=True, null=True)  # Field name made lowercase.
    isrootaggregate = models.CharField(db_column='isRootAggregate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nas_aggregate'


class NasCluster(models.Model):
    uuid = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    serialnumber = models.CharField(db_column='serialNumber', max_length=255)  # Field name made lowercase.
    managementip = models.CharField(db_column='managementIp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=255, blank=True, null=True)
    rawdiskbytestotal = models.CharField(db_column='rawDiskBytesTotal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rawdiskbytesused = models.CharField(db_column='rawDiskBytesUsed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nas_cluster'


class NasNode(models.Model):
    uuid = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    clusterid = models.ForeignKey(NasCluster, models.DO_NOTHING, db_column='clusterId')  # Field name made lowercase.
    serialnumber = models.CharField(db_column='serialNumber', max_length=255)  # Field name made lowercase.
    state = models.CharField(max_length=255, blank=True, null=True)
    rawdiskbytestotal = models.CharField(db_column='rawDiskBytesTotal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rawdiskbytesused = models.CharField(db_column='rawDiskBytesUsed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    aggregatebytestotal = models.CharField(db_column='aggregateBytesTotal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    aggregatebytesused = models.CharField(db_column='aggregateBytesUsed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isfailoverenabled = models.IntegerField(db_column='isFailoverEnabled', blank=True, null=True)  # Field name made lowercase.
    istakeoverpossible = models.IntegerField(db_column='isTakeOverPossible', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nas_node'


class NasVolume(models.Model):
    uuid = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    clusterid = models.ForeignKey(NasCluster, models.DO_NOTHING, db_column='clusterId')  # Field name made lowercase.
    vserverid = models.ForeignKey('NasVserver', models.DO_NOTHING, db_column='vserverId')  # Field name made lowercase.
    nodeid = models.ForeignKey(NasNode, models.DO_NOTHING, db_column='nodeId')  # Field name made lowercase.
    aggregateid = models.ForeignKey(NasAggregate, models.DO_NOTHING, db_column='aggregateId')  # Field name made lowercase.
    sizetotal = models.CharField(db_column='sizeTotal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sizeused = models.CharField(db_column='sizeUsed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sizeusedpercent = models.FloatField(db_column='sizeUsedPercent', blank=True, null=True)  # Field name made lowercase.
    sizeavail = models.CharField(db_column='sizeAvail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sizeavailpercent = models.FloatField(db_column='sizeAvailPercent', blank=True, null=True)  # Field name made lowercase.
    isvserverroot = models.CharField(db_column='isVserverRoot', max_length=10, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=255, blank=True, null=True)
    junctionpath = models.CharField(db_column='junctionPath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nas_volume'


class NasVserver(models.Model):
    uuid = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    volumebytesused = models.CharField(db_column='volumeBytesUsed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    volumebytesavail = models.CharField(db_column='volumeBytesAvail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    volumebytestotal = models.CharField(db_column='volumeBytesTotal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clusterid = models.ForeignKey(NasCluster, models.DO_NOTHING, db_column='clusterId')  # Field name made lowercase.
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nas_vserver'
