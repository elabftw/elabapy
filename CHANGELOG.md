# Changelog for elabapy

## Version 0.8.2

* Allow using limit and offset for get_all methods (#28 by @JAC28)

## Version 0.8.1

* Publish new releases automatically with GitHub Action (#27 by Niels Cautaerts)

## Version 0.8.0

* Add proxies option (#25 by Jean-Luc Parouty)
* Add experiments templates endpoint (#19 by @m6121)

## Version 0.7.1

* Add `get_tags()`

## Version 0.7.0

* Add `get_all_events()`

## Version 0.6.2

* Fix the backup_zip function

## Version 0.6.1

* Fix create experiment/items not sending POST requests

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
