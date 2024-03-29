# Changelog

<!--next-version-placeholder-->

## v0.10.1 (2023-05-10)
### Fix
* Исправлена фильтрация организаций по attributes level ([`f838b2e`](https://github.com/devind-team/devind-django-dictionaries/commit/f838b2ebed0625ee9890645f2c625652ef92ecc9))

## v0.10.0 (2023-05-10)
### Feature
* Добавлена фильтрация через "или" для организаций ([`d37a58a`](https://github.com/devind-team/devind-django-dictionaries/commit/d37a58a2c7aecce7fffaf2b86f537c9527e7b360))

## v0.9.0 (2023-04-06)
### Feature
* Добавлена фильтрация по полю attributes ([`31843bf`](https://github.com/devind-team/devind-django-dictionaries/commit/31843bfbca11bd86bb25fc187997482e73f38302))

## v0.8.1 (2023-04-06)
### Fix
* Delete constraint instead of ForeignKey ([`3f0a9e2`](https://github.com/devind-team/devind-django-dictionaries/commit/3f0a9e2c02add6d0a82c164720ae36f0b6e7b772))

## v0.8.0 (2023-04-06)
### Feature
* Delete organization parent_id constraint ([`078db40`](https://github.com/devind-team/devind-django-dictionaries/commit/078db40ee66812e11fb1b5c2f4ce81c6828abbc4))

### Fix
* Fix bugs after deleting constraint ([`caf3816`](https://github.com/devind-team/devind-django-dictionaries/commit/caf3816ca595d67b5f90e5ca53f9097981b6dd5f))

## v0.7.0 (2022-09-27)
### Feature
* Add children to departments ([`e5f6da6`](https://github.com/devind-team/devind-django-dictionaries/commit/e5f6da607b203c5e70c62348a45102414789542c))
* Add children to departments ([`be99ff2`](https://github.com/devind-team/devind-django-dictionaries/commit/be99ff2da1284796839168543a216d239f3929ab))
* Update version of semantic release ([`1da0107`](https://github.com/devind-team/devind-django-dictionaries/commit/1da0107697e2a54bb221d3e0d720481e662dfffb))

## v0.5.0 (2022-06-28)
### Feature
* Обновление версии семантик релиза ([`93fb3cc`](https://github.com/devind-team/devind-django-dictionaries/commit/93fb3cc24548ea21c3915c88b8e0c6668e663700))

## v0.4.2 (2022-04-25)
### Fix
* Fix flake8 ([`561655c`](https://github.com/devind-team/devind-django-dictionaries/commit/561655c6c323dab05a749105905c170bd814aacf))
* Fix test and resolver ([`0edf54c`](https://github.com/devind-team/devind-django-dictionaries/commit/0edf54c6a793d1de8b88da1c1b785193dea3ea2a))
* Add `s` in end of active_budget_classifications ([`fd994bd`](https://github.com/devind-team/devind-django-dictionaries/commit/fd994bde0efb284297ee389928a0f7c55b3a41ed))

## v0.4.1 (2022-04-25)
### Fix
* Исправлена проблема с загрузкой КБК ([`fe9104f`](https://github.com/devind-team/devind-django-dictionaries/commit/fe9104fe8e4538b552730ebb14b1b1b822056cf4))

## v0.4.0 (2022-04-21)
### Feature
* Добавлена привязка к пользователям в организации ([`4ce8aa9`](https://github.com/devind-team/devind-django-dictionaries/commit/4ce8aa9eeeb3e02e7c536acad9ebea183b510b3f))

## v0.3.0 (2022-04-21)
### Feature
* Добавлены тесты ([`817fa05`](https://github.com/devind-team/devind-django-dictionaries/commit/817fa05406adc801e86449d231a86dab2c1d68b2))
* Поправлены запросы ([`9040f17`](https://github.com/devind-team/devind-django-dictionaries/commit/9040f17ae7edc75dc68215dd1fda031ef2e223c7))
* Добавлена модель и запросы ([`648e71b`](https://github.com/devind-team/devind-django-dictionaries/commit/648e71b1a8f6390b34dc4b6403daf149ebf11a6c))

## v0.2.4 (2022-04-07)
### Fix
* Исправлен линтер ([`bf9e56c`](https://github.com/devind-team/devind-django-dictionaries/commit/bf9e56c054f4dc89f7c6c72bf9107c35626cba06))
* Исправлены related_name ([`708ff9f`](https://github.com/devind-team/devind-django-dictionaries/commit/708ff9f34e803f399c4e3b15b951680c68cea9c7))

## v0.2.3 (2022-04-06)
### Fix
* Внесены изменения для блокирования warnigns ([`09df53d`](https://github.com/devind-team/devind-django-dictionaries/commit/09df53de28e84a7037d95903d429bfd6b9a1dab2))

## v0.2.2 (2022-04-04)
### Fix
* Исправлены проблемы с линтером с типом Any ([`a40ac0f`](https://github.com/devind-team/devind-django-dictionaries/commit/a40ac0f90b6f41037132a169d09b060660ca3199))

## v0.2.1 (2022-03-10)
### Fix
* Исправлены миграции ([`c1413b5`](https://github.com/devind-team/devind-django-dictionaries/commit/c1413b53d3312b3cc14ae9d723f4ec942867c2ec))

## v0.2.0 (2022-03-08)
### Feature
* Add tests ([`e733535`](https://github.com/devind-team/devind-django-dictionaries/commit/e7335356d7e9e6276c61d104876ae0dcc47e3df7))
* Add types and queries ([`8d41ec4`](https://github.com/devind-team/devind-django-dictionaries/commit/8d41ec4fabec57586c0a2bff7c3a5a4450be53a2))
* Add some models ([`0e80b80`](https://github.com/devind-team/devind-django-dictionaries/commit/0e80b80648445f59d74089cac2a9784ac1c7164c))

### Fix
* Fix bug with parent_id in organization ([`136e2c1`](https://github.com/devind-team/devind-django-dictionaries/commit/136e2c1dc2e231109557cd6d658f61c01ba260d5))

## v0.1.1 (2022-03-04)
### Fix
* Update readme.md ([`ecf87b0`](https://github.com/devind-team/devind-django-dictionaries/commit/ecf87b0709d36760acbe6764025b11a4d70f14e6))
