from setuptools import setup
from pip.req import parse_requirements

version_file = open('VERSION')
version = version_file.read().strip()

install_reqs = parse_requirements('requirements.txt', session=False)
dependencies = [str(ir.req) for ir in install_reqs]

setup(
    name='truth-or-dare-lockdownstyle',
    version=version,
    url='https://github.com/jlfcapps/Truth-or-Dare-Lockdown-Style',
    license='MIT',
    author='JOSE LUIS FLOREZ CASTRO',
    author_email='jlfc1988@gmail.com',
    description='An Alexa skill to play Truth or Dare Lockdown Style.',
    packages=['tod'],
    include_package_data=True,
    install_requires=dependencies,
    test_suite='tests'
)
