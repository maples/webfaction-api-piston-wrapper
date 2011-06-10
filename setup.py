from setuptools import setup, find_packages

setup(name='webfaction_api_piston_wrapper',
        version='0.6',
        description='Webfaction API Piston Wrapper',
        author='Marcos Machado',
        packages=find_packages(),
        classifiers=['Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Utilities'],
    include_package_data=True,
    install_requires=['setuptools'],
)