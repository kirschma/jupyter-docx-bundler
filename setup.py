from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(
    author='Marco Rossi',
    author_email='developer@marco-rossi.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Jupyter',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description='Jupyter bundler extension to export notebook as a docx file',
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
            'pillow',
            'matplotlib',
            'nbformat',
            'numpy',
            'requests',
        ],
    },
    install_requires=[
        'nbconvert>=5.3.1',
        'pypandoc>=1.4',
        'notebook>=5.0',
    ],
    keywords=[
        'jupyter',
        'docx',
        'bundler',
    ],
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='jupyter_docx_bundler',
    packages=[
        'jupyter_docx_bundler',
        'jupyter_docx_bundler.test',
    ],
    python_requires='>=3.6',
    setup_requires=[
        'setuptools>=38.6.0',
        'setuptools_scm',
    ],
    url='https://github.com/m-rossi/jupyter_docx_bundler',
    use_scm_version=True,
    entry_points={
        'nbconvert.exporters': [
            'docx = jupyter_docx_bundler:DocxExporter',
        ],
    }
)
