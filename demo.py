import json
import tempfile
from fixtures import sample_packet
from packet_preview import preview


def main():
    with tempfile.TemporaryDirectory() as directory:
        for branch in ['base', 'a', 'b']:
            print(json.dumps(preview(sample_packet(branch, with_photo=branch != 'a'), directory), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
