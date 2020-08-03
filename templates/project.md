<div>
  {% if project.image -%}  
  <div align="center"><img width="160" src="https://projects.tedivm.com/assets/images/projects/{{ project.image }}" /></div>
  {% elif project.image_url -%}  
  <div align="center"><img width="160" src="{{ project.image_url }}" /></div>
  {% elif project.icon -%}  
  <div align="center"><img width="160" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/{{ project.icon|replace('fab fa-', '')|replace('fas fa-', '') }}.svg" /></div>
  {% elif category.image -%}  
  <div align="center"><img width="160" src="https://projects.tedivm.com/assets/images/projects/{{ category.image }}" /></div>
  {% elif category.icon -%}  
  <div align="center"><img width="160" src="https://raw.githubusercontent.com/tedivm/tedivm/main/images/{{ category.icon|replace('fab fa-', '')|replace('fas fa-', '') }}.svg" /></div>
  {%- endif -%}  
</div>
<div>
  {{ project.description }}
</div>
