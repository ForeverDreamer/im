import click

from web.app import app


@app.cli.command('hello_1')
@click.option('--name', default='World')
def hello_command_1(name):
    click.echo(f'Hello, {name}!')


def test_hello_command_1():
    runner = app.test_cli_runner()

    # invoke the command directly
    result = runner.invoke(hello_command_1, ['--name', 'Flask'])
    assert 'Hello, Flask' in result.output

    # or by name
    result = runner.invoke(args=['hello_1'])
    assert 'World' in result.output


def upper(ctx, param, value):
    if value is not None:
        return value.upper()


@app.cli.command('hello_2')
@click.option('--name', default='World', callback=upper)
def hello_command_2(name):
    click.echo(f'Hello, {name}!')


def test_hello_params():
    context = hello_command_2.make_context('hello_2', ['--name', 'flask'])
    assert context.params['name'] == 'FLASK'
