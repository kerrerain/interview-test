from onepoint.katas.mexican import wave


def test_wave_should_return_hello():
    # Given
    input = "hello"

    # When
    actual = wave(input)

    # Then
    assert actual == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
