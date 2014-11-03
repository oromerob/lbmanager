{% for director in directors %}
{% for backend in director.backends.all %}
backend {{ backend.name }} {
    .host = "{{ backend.server.address }}";
{% if backend.port != None %}   .port = {{ backend.port }};{% endif %}
{% if backend.first_byte_timeout != None %} .first_byte_timeout = {{ first_byte_timeout }}s;{% endif %}
{% if backend.between_bytes_timeout != None %} .between_bytes_timeout = {{ between_bytes_timeout }}s;{% endif %}
{% if backend.connect_timeout != None %} .connect_timeout = {{ connect_timeout }}s;{% endif %}
{% if backend.probe_url != None %}
    .probe= {
        .url = "{{ backend.probe_url }}";
{% if backend.probe_timeout != None %}        .timeout = {{ backend.probe_timeout }}s;{% endif %}
{% if backend.probe_interval != None %}        .interval = {{ backend.probe_interval }}s;{% endif %}
{% if backend.probe_window != None %}        .window = {{ backend.probe_window }};{% endif %}
{% if backend.probe_threshold != None %}        .threshold = {{ backend.probe_threshold }};{% endif %}
    }
{% endif %}
}
{% endfor %}
{% endfor %}

{% for director in directors %}
director {{ director.name }} {{ director.dirtype }} {
   {% for back in director.backends.all %}
   {
      .backend = "{{ back.name }}";
   }
   {% endfor %}
}
{% endfor %}
