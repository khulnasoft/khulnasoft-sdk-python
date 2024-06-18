khulnasoftlib.searchcommands
------------------------

.. automodule:: khulnasoftlib.searchcommands

.. autofunction:: dispatch(command_class[, argv=sys.argv, input_file=sys.stdin, output_file=sys.stdout, module_name=None, allow_empty_input=True])

.. autoclass:: EventingCommand
    :members:
    :inherited-members:
    :exclude-members: ConfigurationSettings, process, transform

    .. autoclass:: khulnasoftlib.searchcommands::EventingCommand.ConfigurationSettings
        :members:
        :inherited-members:
        :exclude-members: configuration_settings, fix_up, items, keys

    .. automethod:: khulnasoftlib.searchcommands::EventingCommand.transform

    .. automethod:: khulnasoftlib.searchcommands::EventingCommand.process(args=sys.argv[, input_file=sys.stdin, output_file=sys.stdout])

.. autoclass:: GeneratingCommand
    :members:
    :inherited-members:
    :exclude-members: ConfigurationSettings, generate, process

    .. autoclass:: khulnasoftlib.searchcommands::GeneratingCommand.ConfigurationSettings
        :members:
        :inherited-members:
        :exclude-members: configuration_settings, fix_up, items, keys

    .. automethod:: khulnasoftlib.searchcommands::GeneratingCommand.generate

    .. automethod:: khulnasoftlib.searchcommands::GeneratingCommand.process(args=sys.argv[, input_file=sys.stdin, output_file=sys.stdout, allow_empty_input=True])

.. autoclass:: ReportingCommand
    :members:
    :inherited-members:
    :exclude-members: ConfigurationSettings, map, process, reduce

    .. autoclass:: khulnasoftlib.searchcommands::ReportingCommand.ConfigurationSettings
        :members:
        :inherited-members:
        :exclude-members: configuration_settings, fix_up, items, keys

    .. automethod:: khulnasoftlib.searchcommands::ReportingCommand.map

    .. automethod:: khulnasoftlib.searchcommands::ReportingCommand.process(args=sys.argv[, input_file=sys.stdin, output_file=sys.stdout])

    .. automethod:: khulnasoftlib.searchcommands::ReportingCommand.reduce

.. autoclass:: StreamingCommand
    :members:
    :inherited-members:
    :exclude-members: ConfigurationSettings, process, stream

    .. autoclass:: khulnasoftlib.searchcommands::StreamingCommand.ConfigurationSettings
        :members:
        :inherited-members:
        :exclude-members: configuration_settings, fix_up, items, keys

    .. automethod:: khulnasoftlib.searchcommands::StreamingCommand.process(args=sys.argv[, input_file=sys.stdin, output_file=sys.stdout, allow_empty_input=True])

    .. automethod:: khulnasoftlib.searchcommands::StreamingCommand.stream

.. autoclass:: Configuration
    :members:
    :inherited-members:

.. autoclass:: Option
    :members:
    :inherited-members:
    :exclude-members: Item, View, fix_up

.. autoclass:: Boolean
    :members:
    :inherited-members:

.. autoclass:: Duration
    :members:
    :inherited-members:

.. autoclass:: File
    :members:
    :inherited-members:

.. autoclass:: Integer
    :members:
    :inherited-members:

.. autoclass:: Float
    :members:
    :inherited-members:

.. autoclass:: RegularExpression
    :members:
    :inherited-members:

.. autoclass:: Set
    :members:
    :inherited-members:

