import setuptools

long_description = ""
with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="bulk_renamer_tool",
	version="0.0.6",
	author="Mannix Tapawan",
	author_email="mannix.tapawan@gcash.com",
	description="Rename files with the same pattern.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://vcs.bigcorp.xyz/devops/cmd_tools_project",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: Other/Proprietary License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
	install_requires=(
	'requests',
	),
)