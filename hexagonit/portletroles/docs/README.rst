======================
hexagonit.portletroles
======================

`hexagonit.portletroles` overrides each portlets for Plone to provide different edit_view permissions to them.

Assigning different roles to those permissons happens through rolemap.xml.

Only who has permission can manage portlets through `@@manage-portlets` then.

Further Documentation URL
-------------------------

`http://packages.python.org/hexagonit.portletroles/
<http://packages.python.org/hexagonit.portletroles/>`_

Repository URL
--------------

`https://github.com/hexagonit/hexagonit.portletroles/
<https://github.com/hexagonit/hexagonit.portletroles/>`_


Example `rolemap.xml`::

    <?xml version="1.0"?>
    <rolemap>
      <permissions>
        <permission name="Portlets: Manage portlets"
                    acquire="True">
          <role name="Manager"/>
          <role name="Site Administrator"/>
          <role name="Editor" />
        </permission>
        <!-- Permission for moving and deleting portlets  -->
        <permission name="Portlets: Manage own portlets"
                acquire="True">
          <role name="Manager"/>
          <role name="Site Administrator"/>
          <role name="Editor" />
        </permission>
        <permission name="Portlets: Manage Events portlet"
                    acquire="True">
          <role name="Manager"/>
          <role name="Site Administrator"/>
          <role name="Editor" />
        </permission>
        <permission name="Portlets: Manage Login portlet"
                    acquire="True">
          <role name="Manager"/>
          <role name="Site Administrator"/>
        </permission>
        ...
      </permissions>
    </rolemap>

With this `rolemap.xml`, user who has `Editor` role can add and manage Events portlet, but not Login portlet.

You can find which permissions are registered from overrides.zcml file in the package.

Permission for deleting and moving up/down portlets is controled by permission: `Portlets: Manage own portlets`.
