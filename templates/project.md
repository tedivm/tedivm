<div>
  <h3 style="text-align:center"><a href="https://github.com/{{ project.github }}">{{ project.name }}</a></h3>
  {% if project.image -%}  
  <div style="text-align:center"><img src="https://projects.tedivm.com/assets/images/projects/{{ project.image }}" /></div>


  {% elif project.icon -%}  
  <div style="text-align:center"><img src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/{{ project.icon|replace('fab fa-', '')|replace('fas fa-', '') }}.svg" /></div>

  {%- endif -%}
  
</div>
<div>
  {{ project.description }}
</div>
