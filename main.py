import re


def decompress_string_version2c(content: str) -> int:
    if '(' not in content:
        return len(content)

    def decompress(content):
        total_length = 0
        i = 0

        while i < len(content):
            if content[i] == '(':
                end_marker = content.find(')', i)
                marker = content[i + 1:end_marker]
                a, b = map(int, marker.split('x'))
                i = end_marker + 1
                repeat_segment = content[i:i + a]
                total_length += b * decompress_string_version2c(repeat_segment)
                i += a
            else:
                total_length += 1
                i += 1

        return total_length

    return decompress(content)


# Example usage
compressed_content = "(27x12)(20x12)(13x14)(7x10)(1x12)A"
print(decompress_string_version2b(compressed_content))
