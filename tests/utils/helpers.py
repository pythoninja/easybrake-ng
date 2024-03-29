from pathlib import Path


def get_input(_for: str):
    match _for:
        case "year_ok":
            return [
                [Path("/dummy/subdir/Season 02/Title with spaces.1991 (Random words).HDRIP.2160p.mkv")],
                [Path("/dummy/New Title/Film 1991 (Words).releaseGroup.mkv")],
                [Path("/dummy/subdir/Season 01/Video.Example.1992.BDRIP.1080p.mp4")],
            ]
        case "year_fail":
            return [
                [Path("/dummy/Video.with.dots.mp4")],
                [Path("/dummy/Video with spaces.m4v")],
                [Path("/dummy/New Title/Video.without.year.1080p_with_upper_extension.MKV")],
                [Path("/dummy/New Title/Video.without.year.720p.mkv")],
            ]
        case "quality_ok":
            return [
                [Path("/dummy/subdir/Season 02/Title with spaces.1991 (Random words).HDRIP.2160p.mkv")],
                [Path("/dummy/New Title/Video.without.year.1080p_with_upper_extension.MKV")],
                [Path("/dummy/subdir/Season 01/Video.Example.1991.BDRIP.1080p.mp4")],
                [Path("/dummy/New Title/Video.without.year.720p.mkv")],
            ]
        case "quality_fail":
            return [
                [Path("/dummy/Video.with.dots.mp4")],
                [Path("/dummy/Video with spaces.m4v")],
                [Path("/dummy/New Title/Film 1991 (Words).releaseGroup.mkv")],
            ]
        case "title_expected_fail":
            return [[Path("/dummy/New Title/Film 1991 (Words).releaseGroup.mkv")]]
