'''
Script to modify Image Links, Outgoing Links & Callouts in Markdown Files

Markdown Link Regex:
https://davidwells.io/snippets/regex-match-markdown-links
https://stephencharlesweiss.com/regex-markdown-link

Kramdown Syntax:
https://kramdown.gettalong.org/syntax.html

Callout Block Regex:
https://github.com/sondregronas/mkdocs-callouts/blob/main/src/mkdocs_callouts/utils.py
https://github.com/Pseudonium/Obsidian_to_Anki/issues/332
'''

from __future__ import annotations
from io import BytesIO
import re
import os
import glob
import argparse

import frontmatter


def get_image_paths(image_directory: str, image_extensions: tuple[str]) -> list[str]:
    """
    Function to find all images in a directory
    """

    image_paths = []
    for extension in image_extensions:
        image_paths.extend(glob.glob(os.path.join(image_directory, '**', f'*{extension}'), recursive=True))
    return image_paths


def fetch_image_path(image_name: str, image_path_list: list[str]) -> str | None:
    """
    Function to find full path of image
    """

    if os.path.dirname(image_name) != '':
        last_directory = os.path.basename(os.path.dirname(image_name))
        file_name = os.path.basename(image_name)
        image_name = os.path.join(last_directory, file_name)

    image_name = os.path.normpath(image_name)
    for image_path in image_path_list:
        image_path = os.path.normpath(image_path)
        if (
            image_name in image_path and
            os.path.basename(image_name) == os.path.basename(image_path)
        ):
            image_path = os.path.join(*image_path.split(os.sep)[1:])
            return image_path.replace("\\", "/")

    return None


def perform_file_transformation(
    source_filepath: str, link_regex_pattern: str, callout_regex_pattern: str,
    image_extensions: tuple[str], image_paths: list[str], blog_type: str
) -> None:
    """
    Main function to call the transformation logic
    """

    with open(source_filepath, "r", encoding='utf-8') as input_file_pointer:
        source_file = frontmatter.load(input_file_pointer)

    file_content = source_file.content

    # Adding Description
    # file_description = source_file.metadata.get('description')
    # if file_description and file_content.find(file_description):
    #     file_content = f'{file_description}\n\n{file_content}'

    # Process Links
    links_from_file = re.finditer(link_regex_pattern, file_content, flags=re.I)
    for link in links_from_file:
        # print(link.groups())

        # Don't process links if Kramdown syntax is found
        if link.groups()[-1]:
            continue

        image_link_condition = (
            (
                link.group(0).startswith("![[") and link.group(0).endswith("]]") and
                link.group(2).rsplit("|", maxsplit=1)[0].endswith(image_extensions)
            )
            or
            (
                link.group(0).startswith("![") and link.group(0).endswith(")") and
                link.group(6).endswith(image_extensions)
            )
        )

        if image_link_condition:
            file_content = process_images(file_content, link, source_file, image_paths, blog_type)
        else:
            file_content = process_outgoing_links(file_content, link, blog_type)

    # Process Callouts
    callout_mapping = {
        'tip': ['tip', 'hint', 'important'],
        'info': ['info', 'note'],
        'warning': ['warning', 'caution', 'attention'],
        'danger': ['danger', 'error']
    }

    callouts_from_file = re.finditer(callout_regex_pattern, file_content, flags=re.I | re.M)
    for callout in callouts_from_file:
        file_content = process_callouts(file_content, callout, callout_mapping)

    # Remove consecutive empty lines
    source_file.content = re.sub(r'\n\s*\n', '\n\n', file_content)

    output_buffer = BytesIO()
    frontmatter.dump(source_file, output_buffer)
    with open(source_filepath, mode='wb') as output_file:
        output_buffer.seek(0)
        output_file.write(output_buffer.read())


def process_callouts(
    file_content: str, callout_match: re.Match, callout_mapping: dict[str, list[str]]
) -> str:
    """
    Function to modify callouts
    """

    if callout_match.group(5):
        return file_content

    callout_type = callout_match.group(2).lower()
    callout_title = callout_match.group(3).strip() if callout_match.group(3).strip() else ''
    callout_body = callout_match.group(4)

    kramdown_type = None
    for chirpy_type, obsidian_types in callout_mapping.items():
        if callout_type in obsidian_types:
            kramdown_type = chirpy_type
    kramdown_type = kramdown_type if kramdown_type else 'info'
    kramdown_attributes = f'{{: .prompt-{kramdown_type} }}'

    if callout_title:
        modified_callout = f'> **{callout_title}**  \n{callout_body}\n{kramdown_attributes}'
    else:
        modified_callout = f'{callout_body}\n{kramdown_attributes}'

    original_callout = callout_match.group(1)
    file_content = file_content.replace(original_callout, modified_callout)
    return file_content


def process_outgoing_links(file_content: str, link_match: re.Match, blog_type: str) -> str:
    """
    Function to modify the outgoing hyperlinks
    """

    original_link = link_match.group(0)

    if blog_type == "medium":
        return file_content

    if not link_match.group(6).startswith(("http", "https")):
        return file_content

    kramdown_attributes = '{: target="_blank" rel="noopener noreferrer" }'

    description = link_match.group(5)
    outgoing_link = link_match.group(6)

    modified_link = f'[{description}]({outgoing_link}){kramdown_attributes}'

    file_content = file_content.replace(original_link, modified_link)
    return file_content


def process_images(
    file_content: str, image_match: re.Match, source_file: frontmatter.Post,
    image_paths: list[str], blog_type: str
) -> str:
    """
    Function to Convert Markdown Image links to Kramdown Image Links
    """

    original_image: str = image_match.group(0)

    if blog_type == "medium" and original_image.startswith("![") and original_image.endswith(")"):
        return file_content

    if original_image.startswith("![[") and original_image.endswith("]]"):
        image_name = image_match.group(3).rsplit('|', maxsplit=1)
        image_link = fetch_image_path(image_name[0], image_paths)
        image_name[0] = os.path.splitext(image_name[0])[0]
    else:
        image_name = image_match.group(5).rsplit('|', maxsplit=1)
        image_link = image_match.group(6)

    # Move Banner to Frontmatter
    if blog_type == "jekyll" and "banner" in image_link and not source_file.metadata.get('image'):
        source_file.metadata['image'] = image_link
        file_content = file_content.replace(original_image, "")
        return file_content

    if blog_type == "jekyll":
        if len(image_name) > 1:
            modified_image = f'![{image_name[0]}]({image_link}){{: width="{image_name[1]}" .shadow }}'
        else:
            modified_image = f'![{image_name[0]}]({image_link}){{: width="640" .shadow }}'
    else:
        modified_image = f'![{image_name[0]}]({image_link})'

    file_content = file_content.replace(original_image, modified_image)
    return file_content


def parse_user_inputs() -> argparse.Namespace:
    """Returns input parameters provided on command line by user"""

    parser = argparse.ArgumentParser(description="Automate Modifying Markdown Files")

    parser.add_argument(
        '-b', '--base', required=False, default='_posts',
        help="Path to Markdown files", type=str
    )

    parser.add_argument(
        '-s', '--site', required=False, default='jekyll',
        help="Blog Type", type=str, choices=['medium', 'jekyll']
    )

    user_arguments = parser.parse_args()
    return user_arguments


def main() -> None:
    """
    Main driver function
    """

    print('Starting: "modify_links" script...')

    links_regex_pattern = (
        r'(!?(\[\[([^\]]*)\]\](\|\d+)?|\[([^\]]*)\]\(((?:https?://)?[A-Za-z0-9:/.%&#-_ ]+?)(?:"(.+)")?\)))({:(?:.+)})?'
    )
    callout_regex_pattern = r'((?:>+) *\[!([^\]]*)\](.*)?\n(.+(?:\n(?:^.{1,3}$|^.{4}(?<!<!--).*))*))({:(?:.+)})?'
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg')

    user_arguments = parse_user_inputs()

    base_path = user_arguments.base
    source_file_path = os.path.join(base_path, '**', '*.md')

    image_directory = os.path.join(base_path, "images", "")
    image_paths = get_image_paths(image_directory, image_extensions)
    # print(image_paths)

    for filepath in glob.iglob(source_file_path, recursive=True):
        print(filepath)
        perform_file_transformation(
            filepath, links_regex_pattern, callout_regex_pattern,
            image_extensions, image_paths, user_arguments.site
        )

    print('Completed: "modify_links" script...')


if __name__ == '__main__':
    main()
