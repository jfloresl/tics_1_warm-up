  from django import template
  register = template.Library()

  from ..models import Banco

  @register.simple_tag
  def any():
  	return Banco.objects.count()
