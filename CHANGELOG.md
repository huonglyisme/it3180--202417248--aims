# Changelog

All notable changes to AIMS-mini will be documented here.

## [Unreleased]
### Added
- Add Cart.sort_by_title() for sorting DVDs by title.
- Add Cart.sort_by_cost() for sorting DVDs by cost.
- Add unit tests for cart sorting.

## [1.0.0] - 2026-11-02

### Added
- Display DVD details with Cart.print_cart().
- Search DVDs by title with search_by_title().
- Support discount calculation with discounted_total().
- Add automated unit tests.

### Fixed
- Fix cart capacity bug that accepted the 21st DVD.
- Fix discount calculation and validate percentage input.

### Changed
- Refactor source code into the aims Python package.
- Improve cart messages and merge conflict handling.
