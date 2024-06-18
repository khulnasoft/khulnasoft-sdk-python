Welcome to the API reference for the Khulnasoft SDK for Python, which describes the modules that are included in the SDK.
For more information, see the `Khulnasoft Developer Portal <http://dev.khulnasoft.com/view/python-sdk/SP-CAAAEBB>`_.

.. toctree::
   :maxdepth: 2
   :name: SDK for Python API Reference

   binding
   client
   data
   results
   modularinput
   searchcommands
   searchcommandsvalidators


:doc:`binding`
--------------

    :func:`~khulnasoftlib.binding.connect` function

    :func:`~khulnasoftlib.binding.namespace` function

    :class:`~khulnasoftlib.binding.Context` class

    :class:`~khulnasoftlib.binding.ResponseReader` class


    **Exceptions**

    :func:`~khulnasoftlib.binding.handler` function

    :class:`~khulnasoftlib.binding.AuthenticationError` class

    **Custom HTTP handler**

    :class:`~khulnasoftlib.binding.HTTPError` class

    :class:`~khulnasoftlib.binding.HttpLib` class


:doc:`client`
-------------

    :func:`~khulnasoftlib.client.connect` function

    :class:`~khulnasoftlib.client.Service` class

    :class:`~khulnasoftlib.client.Endpoint` base class


    **Entities and collections**

    :class:`~khulnasoftlib.client.Entity` class

    :class:`~khulnasoftlib.client.Collection` class

    :class:`~khulnasoftlib.client.ReadOnlyCollection` class

    :class:`~khulnasoftlib.client.Application` class

    :class:`~khulnasoftlib.client.AlertGroup` class

    :class:`~khulnasoftlib.client.ConfigurationFile` class

    :class:`~khulnasoftlib.client.Stanza` class

    :class:`~khulnasoftlib.client.Configurations` class

    :class:`~khulnasoftlib.client.Index` class

    :class:`~khulnasoftlib.client.Indexes` class

    :class:`~khulnasoftlib.client.Input` class

    :class:`~khulnasoftlib.client.Inputs` class

    :class:`~khulnasoftlib.client.Job` class

    :class:`~khulnasoftlib.client.Jobs` class

    :class:`~khulnasoftlib.client.KVStoreCollection` class

    :class:`~khulnasoftlib.client.KVStoreCollectionData` class

    :class:`~khulnasoftlib.client.KVStoreCollections` class

    :class:`~khulnasoftlib.client.Loggers` class

    :class:`~khulnasoftlib.client.Message` class

    :class:`~khulnasoftlib.client.ModularInputKind` class

    :class:`~khulnasoftlib.client.Role` class

    :class:`~khulnasoftlib.client.Roles` class

    :class:`~khulnasoftlib.client.SavedSearch` class

    :class:`~khulnasoftlib.client.SavedSearches` class

    :class:`~khulnasoftlib.client.Settings` class

    :class:`~khulnasoftlib.client.StoragePassword` class

    :class:`~khulnasoftlib.client.StoragePasswords` class

    :class:`~khulnasoftlib.client.User` class

    :class:`~khulnasoftlib.client.Users` class


    **Exceptions**

    :class:`~khulnasoftlib.client.AmbiguousReferenceException` class

    :class:`~khulnasoftlib.client.IllegalOperationException` class

    :class:`~khulnasoftlib.client.IncomparableException` class

    :class:`~khulnasoftlib.client.InvalidNameException` class

    :class:`~khulnasoftlib.client.NoSuchCapability` class

    :class:`~khulnasoftlib.client.NotSupportedError` class

    :class:`~khulnasoftlib.client.OperationError` class


:doc:`data`
-----------

    :func:`~khulnasoftlib.data.load` function

    :func:`~khulnasoftlib.data.record` function

    :class:`~khulnasoftlib.data.Record` class

:doc:`results`
--------------

    :class:`~khulnasoftlib.results.ResultsReader` class

    :class:`~khulnasoftlib.results.Message` class

:doc:`modularinput`
-------------------

    :class:`~khulnasoftlib.modularinput.Argument` class

    :class:`~khulnasoftlib.modularinput.Event` class

    :class:`~khulnasoftlib.modularinput.EventWriter` class

    :class:`~khulnasoftlib.modularinput.InputDefinition` class

    :class:`~khulnasoftlib.modularinput.Scheme` class

    :class:`~khulnasoftlib.modularinput.Script` class

    :class:`~khulnasoftlib.modularinput.ValidationDefinition` class

:doc:`searchcommands`
---------------------

    :class:`~khulnasoftlib.searchcommands.EventingCommand` class

    :class:`~khulnasoftlib.searchcommands.GeneratingCommand` class

    :class:`~khulnasoftlib.searchcommands.ReportingCommand` class

    :class:`~khulnasoftlib.searchcommands.StreamingCommand` class

    :class:`~khulnasoftlib.searchcommands.Option` class
