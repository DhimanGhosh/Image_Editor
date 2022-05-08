# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added - (unreleased)
- [image_editor]-[core]-[add_elements]-[add_layers] Added support to add text on image [Major]
- [image_editor]-[utils]-[extract_text_from_image] extract_text_from_image function extracts text from an image [Patch]
- [image_editor]-[core]-[image_processing]-[Image_Processing] Implemented Image crop feature [Major]
- [image_editor]-[core]-[image_processing]-[Image_Processing] Added support to crop image circular shape with transparent background [Major]
- [image_editor]-[utils]-[convert_image] transparent_background function removes black background from image and converts to png format [Minor]
- [image_editor]-[utils]-[file_processing] get the size of a file in bytes [Patch]
- [requirements] Added opencv-python==4.5.5.64 module [Patch]
- [image_editor]-[utils]-[convert_image] cv_to_image function converts cv image object to an image file [Patch]
- [image_editor]-[core]-[image_processing]-[Image_Processing] scale_image function helps in up-scaling / down-scaling the image [Major]
- [image_editor]-[core]-[image_processing]-[Image_Processing] flip_image function helps in flipping the image horizontally / vertically [Major]
- [image_editor]-[init] added ENUMs [Minor]

### Changed - (unreleased)
- [image_editor]-[assets]-[get_assets] store_in_res function now will return the new file path after stored in resource folder [Minor]
- [image_editor]-[core]-[add_elements]-[add_layers] Implemented create_new_image_file utility function [Patch]
- [image_editor]-[utils]-[convert_image] create_new_image_file function saves file with incremental number [Minor]
- [image_editor]-[core]-[image_processing]-[Image_Processing] extract_channel function now returns image path instead of ndarray [Minor]

### Removed - (unreleased)


## [0.0.1] - 2022-05-03
### Added
- [CHANGELOG] Configuration for changelog.md [Patch]
- [README] README file for this project [Patch]
- [requirements] Added package requirements [Patch]
- [image-editor]-[core]-[image_processing]-[Image_Processing] Implemented extract_channel [Major]
- [image-editor]-[core]-[add_elements]-[add_layers] Added support to add black colour border on all 4 sides [Major]
