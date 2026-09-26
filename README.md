# VALSE Webinar Slides 2 (2020 archive)

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-D4A017.svg)](LICENSE)

Historical Python downloader for the VALSE webinar slide index as it existed in 2020. The original notes recorded 320 items totaling about 6.40 GB.

## Usage and Limitations

Run `python valse_slides.py` from a directory where downloaded slides may be created. The script uses only the Python 3 standard library, writes its discovered links to `slides_info`, and downloads into date-based directories.

The code targets plain HTTP pages under `valser.org/webinar/slide/`. Those endpoints may have moved or stopped responding, and the script has no request timeout, retry policy, checksum verification, or rate limiting. Review the URLs and storage requirements before running; no live download was attempted during this documentation update.

## Related Project

- [VALSE-Webinar-Slides](https://github.com/yuzhounh/VALSE-Webinar-Slides): earlier two-script downloader and historical 150-item archive notes.

## License

See the existing [GNU General Public License, version 3](LICENSE).
