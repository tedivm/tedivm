<div>
  {% if project.image -%}  
  <div width="220" align="center"><img src="https://projects.tedivm.com/assets/images/projects/{{ project.image }}" /></div>
  {% elif project.icon -%}  
  <div width="220" align="center"><img src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/{{ project.icon|replace('fab fa-', '')|replace('fas fa-', '') }}.svg" /></div>
  {% elif category.image -%}  
  <div width="220" align="center"><img src="https://projects.tedivm.com/assets/images/projects/{{ category.image }}" /></div>
  {% elif category.icon -%}  
  <div width="220" align="center"><img src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/{{ category.icon|replace('fab fa-', '')|replace('fas fa-', '') }}.svg" /></div>
  {%- endif -%}  
</div>
<div>
  {{ project.description }}
</div>
