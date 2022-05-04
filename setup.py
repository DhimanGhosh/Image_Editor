from setuptools import setup

with open('version.txt', 'r') as file_handler:
    VERSION = file_handler.read()

with open('requirements.txt', 'r') as f:
    requires = f.readlines()
PACKAGES = [pkg[:-1] for pkg in requires if 'Sphinx' not in pkg]

PROJECT = 'Image_Editor'
DESCRIPTION = 'Simple GUI based image editor'
PROJECT_URL = 'https://github.com/DhimanGhosh/Image_Editor'
AUTHOR = 'Dhiman Ghosh'
AUTHOR_EMAIL = 'dgkiitcsedual@gmail.com'

setup(
    name=PROJECT,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    packages=[
        'image_editor',
        'image_editor.assets',
        'image_editor.configuration',
        'image_editor.core',
        'image_editor.core.add_elements',
        'image_editor.core.image_processing',
        'image_editor.gui',
        'image_editor.utils',
        'image_editor.test',
    ],
    include_package_data=True,
    install_requires=PACKAGES,
    keywords=['python', 'image', 'image viewer', 'image editor', 'image processing'],
    url=PROJECT_URL,
    license='GPL-3.0 License',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Natural Language :: English"
    ],
    python_requires=">=3.8.5"
)
