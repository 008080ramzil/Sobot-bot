from setuptools import setup, find_packages

setup(
    name='sobriety-bot',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'aiogram==3.0.1',
        'apscheduler==3.10.4',
        'openai==1.30.1',
        'python-dotenv==1.0.0',
        'aiohttp==3.9.3'
    ],
)
