# Quando usar módulos
# 1° - Separar funcionalidades relacionadas
# 2° - Não acoplar o codigo
# 3° - Não ter um arquivo gigante
from banco_de_dados import buscar_usuario
from configuracoes import senha

buscar_usuario()
