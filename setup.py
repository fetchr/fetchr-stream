from setuptools  import setup

setup(
    name = "fetchr_stream",
    packages = ["fetchr_stream"],
    version = "0.1",
    description = "Wrapper for pushing the data into streams",
    author = "Manoj Kumar",
    author_email = "harish224227@gmail.com",
    url = "https://https://github.com/fetchr/fetchr-stream",
    keywords = ["streams", "kinesis"],
    setup_requires = ["pytest-runner"],
    install_requires = ["boto3==1.4.1"],
    tests_requires = ["pytest==3.0.5","moto==0.4.30","sure==1.4.0"],
    licence = 'MIT'
)