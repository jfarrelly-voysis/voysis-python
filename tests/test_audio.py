import io

from voysis.audio.audio import AudioFile


def test_16khz_file():
    audio_file = AudioFile(io.BytesIO(b'\x52\x49\x46\x46\x22\xe2\x01\x00\x57\x41\x56\x45\x66\x6d\x74\x20\x10\x00'
                                      b'\x00\x00\x01\x00\x01\x00\x80\x3e\x00\x00\x00\x7d\x00\x00\x02\x00\x10\x00'
                                      b'\x64\x61\x74\x61\xfe\xe1\x01\x00'))
    assert audio_file.header.bits_per_sample == 16
    assert audio_file.header.sample_rate == 16000


def test_48khz_file():
    audio_file = AudioFile(io.BytesIO(b'\x52\x49\x46\x46\x32\x00\x0a\x00\x57\x41\x56\x45\x66\x6d\x74\x20\x12\x00'
                                      b'\x00\x00\x03\x00\x01\x00\x80\xbb\x00\x00\x00\xee\x02\x00\x04\x00\x20\x00'
                                      b'\x00\x00\x66\x61\x63\x74\x04\x00'))
    assert audio_file.header.bits_per_sample == 32
    assert audio_file.header.sample_rate == 48000


def test_raw_audio():
    audio_file = AudioFile(io.BytesIO(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                                      b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                                      b'\x00\x00\x00\x00\x00\x00\x00\x00'))
    assert audio_file.header.bits_per_sample == 16
    assert audio_file.header.sample_rate == 16000
