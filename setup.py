import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="soniox",
    version="1.3.1",
    author="Soniox Inc",
    author_email="support@soniox.com",
    description="Soniox speech recognition service client library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://soniox.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["grpcio", "protobuf", "numpy", "SoundCard"],
    package_data={
        "soniox": [
            "roots.pem",
            "test_data_files/test_audio_long.flac",
            "test_data_files/test_audio_long.raw",
            "test_data_files/test_audio_multi_channel.flac",
            "test_data_files/test_audio_profanity.mp3",
            "test_data_files/test_audio_sd_spk1.flac",
            "test_data_files/test_audio_sd_spk2.flac",
            "test_data_files/test_audio_sd.flac",
            "test_data_files/test_audio_sd.raw",
            "test_data_files/test_audio_speech_adaptation.flac",
            "test_data_files/test_audio.flac",
            "test_data_files/test_audio.raw",
            "test_data_files/test_audio.wav",
        ],
    },
)
