'''
Script to get list of articles to be published to Medium

References:
https://docs.python.org/3/library/xml.etree.elementtree.html
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
https://dev.to/cicirello/how-to-patch-the-deprecated-set-output-in-github-workflows-and-in-container-actions-9co
'''

from __future__ import annotations
from typing import Mapping
import os
import sys
from datetime import datetime
import xml.etree.ElementTree as ET
import glob

import requests
import frontmatter


def set_action_outputs(output_pairs: Mapping[str, str | int]) -> None:
    '''
    Sets Output Variable for GitHub Action
    In CLI mode output will be logged to terminal
    '''

    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding='utf-8') as file:
            for key, value in output_pairs.items():
                print(f"{key}={value}", file=file)
    else:
        for key, value in output_pairs.items():
            print(f"{key}={value}")


def get_latest_post_details() -> datetime.date | None:
    '''
    Function to get the details of latest post using Medium RSS Feed
    '''

    response = requests.get('https://medium.com/feed/@david-varghese', timeout=60)  # noqa: E501

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        latest_post = root.find('./channel/item[1]')

        latest_post_title = latest_post.find('title').text
        latest_post_date = datetime.strptime(
            latest_post.find('pubDate').text, '%a, %d %b %Y %H:%M:%S %Z').date()  # noqa: E501

        print(f'Title: {latest_post_title}\nPosted on: {latest_post_date}')
        return latest_post_date

    return None


def identify_files_to_publish(
    source_file_path: str, latest_post_date: datetime.date
) -> list[str]:
    '''
    Function to Identity files that need to be posted to Medium
    '''

    publish_list = []
    for filepath in glob.iglob(source_file_path, recursive=True):
        normalized_filepath = os.path.normpath(filepath)

        filename = os.path.basename(normalized_filepath)
        file_metadata_date = datetime.strptime(
            '-'.join(filename.split('-', 3)[:3]), '%Y-%m-%d').date()

        if file_metadata_date > latest_post_date:
            metadata = frontmatter.load(normalized_filepath).metadata
            if metadata.get('published') is True:
                absolute_filepath = os.path.realpath(normalized_filepath)
                publish_list.append(absolute_filepath)

    return publish_list


def write_list_to_file(publish_list: list[str], output_filepath: str) -> None:
    '''
    Write Path of Files to Upload to Disk
    '''

    print(publish_list)
    with open(output_filepath, 'w+', encoding='utf-8') as output:
        output.write('\n'.join(publish_list))


def main() -> None:
    '''
    Main Driver Function
    '''

    source_file_path = sys.argv[1]
    output_file_path = 'upload_list.txt'
    latest_post_date = get_latest_post_details()

    if not latest_post_date:
        set_action_outputs({'rss_fetch': 'failure', 'output_filepath': ''})  # noqa: E501
        return

    publish_list = identify_files_to_publish(source_file_path, latest_post_date)  # noqa: E501
    if not publish_list:
        set_action_outputs({'rss_fetch': 'success', 'output_filepath': ''})  # noqa: E501
        return

    write_list_to_file(publish_list, output_file_path)
    set_action_outputs({
        'rss_fetch': 'success', 'output_filepath': os.path.realpath(output_file_path)  # noqa: E501
    })
    return


if __name__ == '__main__':
    main()
