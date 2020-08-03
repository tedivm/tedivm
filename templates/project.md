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
{% if project.homepage %}<a href="{{ project.homepage }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/home.svg" title="{{ project.name }} Homepage"></a>{% endif %}
{% if project.documentation %}<a href="{{ project.documentation }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/book-open.svg" title="{{ project.name }} Documentation"></a>{% endif %}
{% if project.github %}<a href="https://github.com/{{ project.github }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/github.svg" title="{{ project.name }} on Github"></a>{% endif %}
{% if project.dockerhub %}<a href="https://hub.docker.com/r/{{ project.dockerhub }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/docker.svg" title="{{ project.name }} on Docker Hub"></a>{% endif %}
{% if project.puppet_forge %}<a href="https://forge.puppet.com/{{ project.puppet_forge }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/flask.svg" title="{{ project.name }} on Puppet Forge"></a>{% endif %}
{% if project.npm %}<a href="https://www.npmjs.com/package/{{ project.npm }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/npm.svg" title="{{ project.name }} on the NPM Registry"></a>{% endif %}
{% if project.pypi %}<a href="https://pypi.org/project/{{ project.pypi }}/"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/python.svg" title="{{ project.name }} on PyPI"></a>{% endif %}
{% if project.packagist %}<a href="https://packagist.org/packages/{{ project.packagist }}"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/php.svg" title="{{ project.name }} on Packagist"></a>{% endif %}
{% if project.rubygems %}<a href="https://rubygems.org/gems/{{ project.rubygems }}/"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/gem.svg" title="{{ project.name }} on RubyGems"></a>{% endif %}
{% if project.wordpress %}<a href="https://wordpress.org/plugins/{{ project.wordpress }}/"><img height="32" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/wordpress.svg" title="{{ project.name }} on the Wordpress Plugin Directory"></a>{% endif %}
</div>
