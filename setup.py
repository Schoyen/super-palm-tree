from setuptools import setup, find_packages
from setuptools_rust import RustExtension, Binding


setup(
    name="super-palm-tree",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    rust_extensions=[
        RustExtension(
            "super_palm_tree.spt_lib",
            "Cargo.toml",
            binding=Binding.PyO3,
        ),
    ],
    zip_safe=False,
)
