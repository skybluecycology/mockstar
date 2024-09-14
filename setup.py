from setuptools import setup, find_packages

setup(
    name='mock_data_generator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    description='A library for generating mock data for fact and dimension tables based on metadata.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/mock_data_generator',  # Replace with your actual URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
