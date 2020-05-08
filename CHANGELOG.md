# Changelog for elabapy

## Version 0.6.0

### BREAKING CHANGE

* The `dev` keyword passed to `Manager` has been replaced by `verify`

### Fixed

* Fix the `get_upload()` function to return binary data instead of trying to parse a JSON response

### Added

* Add function `add_link_to_item()` to add a link to an item in database
* Add `get_bookable()`
* Add `create_event()`
* Add `get_event()`
* Add `destroy_event()`
* Add type hinting
* Add GitHub actions

## Version 0.5.1

### Added

* Get backup zip

## Version 0.5.0

### Added

* Create item
* Get items types
* Get status
* Add tags
* Add link

## Version 0.4.0

### Added

* Create experiment

## Version 0.3.0

### Added

* File upload (fix #2)
* Update instructions in README

## Version 0.2.0

### Added

* Function to POST data (fix elabftw/elabftw#378)

### Changed

* Remove the documentation from the README as it's on doc.elabftw.net
