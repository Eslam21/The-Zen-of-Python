from setuptools import setup, find_packages

setup(
    name='numpy_toolbox',
    version='0.1',
    author='Eslam Mohamed',
    author_email='your.email@example.com',
    description='A toolbox for numerical operations with NumPy',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/username/numpy_toolbox',
    license='MIT',
    keywords='numpy numerical operations matrix statistics',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
    ],
    entry_points={
        'console_scripts': [
            'numpy-toolbox-cli=numpy_toolbox.cli:main',
        ],
    },
    package_data={
        'numpy_toolbox': ['data/*.dat'],
    },
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'dev': ['pytest', 'sphinx'],
        'docs': ['sphinx'],
    },
    test_suite='tests',
)
