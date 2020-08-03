<div>
  <h3 align="center"><a href="https://github.com/{{ project.github }}">{{ project.name }}</a></h3>
  {% if project.image -%}  
  <div height="120" align="center"><img height src="https://projects.tedivm.com/assets/images/projects/{{ project.image }}" /></div>
  {% elif project.icon -%}  
  <div height="120" align="center"><img src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/{{ project.icon|replace('fab fa-', '')|replace('fas fa-', '') }}.svg" /></div>
  {% elif category.image -%}  
  <div height="120" align="center"><img src="https://projects.tedivm.com/assets/images/projects/{{ category.image }}" /></div>
  {% elif category.icon -%}  
  <div height="120" align="center"><img src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/{{ category.icon|replace('fab fa-', '')|replace('fas fa-', '') }}.svg" /></div>
  {%- endif -%}  
</div>
<div>
  {{ project.description }}
</div>
<div>
<table>
<tr>
{% if project.homepage %}<td><a href="{{ project.homepage }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/home.svg" title="{{ project.name }} Homepage"></a></td>{% endif %}
{% if project.documentation %}<td><a href="{{ project.documentation }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/book-open.svg" title="{{ project.name }} Documentation"></a></td>{% endif %}
{% if project.github %}<td><a href="https://github.com/{{ project.github }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/github.svg" title="{{ project.name }} on Github"></a></td>{% endif %}
{% if project.dockerhub %}<td><a href="https://hub.docker.com/r/{{ project.dockerhub }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/docker.svg" title="{{ project.name }} on Docker Hub"></a></td>{% endif %}
{% if project.puppet_forge %}<td><a href="https://forge.puppet.com/{{ project.puppet_forge }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/flask.svg" title="{{ project.name }} on Puppet Forge"></a></td>{% endif %}
{% if project.npm %}<td><a href="https://www.npmjs.com/package/{{ project.npm }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/npm.svg" title="{{ project.name }} on the NPM Registry"></a></td>{% endif %}
{% if project.pypi %}<td><a href="https://pypi.org/project/{{ project.pypi }}/"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/python.svg" title="{{ project.name }} on PyPI"></a></td>{% endif %}
{% if project.packagist %}<td><a href="https://packagist.org/packages/{{ project.packagist }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/php.svg" title="{{ project.name }} on Packagist"></a></td>{% endif %}
{% if project.rubygems %}<td><a href="https://rubygems.org/gems/{{ project.rubygems }}/"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/gem.svg" title="{{ project.name }} on RubyGems"></a></td>{% endif %}
{% if project.wordpress %}<td><a href="https://wordpress.org/plugins/{{ project.wordpress }}/"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/wordpress.svg" title="{{ project.name }} on the Wordpress Plugin Directory"></a></td>{% endif %}
</tr>
</table>
</div>
