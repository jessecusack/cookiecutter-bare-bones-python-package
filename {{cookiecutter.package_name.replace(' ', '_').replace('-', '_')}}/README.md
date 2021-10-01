{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.package_name.replace('-', ' ').replace('_', ' ').title() }}

{{ cookiecutter.description }}

---
{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}
