from setuptools import setup, find_packages

setup(
    name='schedulizer',
    version='0.1.0',
    author='@xwsein',
    author_email='hire-hussein@proton.me',
    description='SCHEDULIZER is a Python package for simulating and visualizing classic CPU scheduling algorithms. It is designed for educational use, enabling students, educators, and enthusiasts to explore how different algorithms schedule processes based on arrival time, burst time, and priority.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xwsein/schedulizer',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

