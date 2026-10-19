# sistema-defesa-v3-log
Sistema de Defesa v3.0 - Bloqueio temporário + Log auditável para SOC | Python

# 🛡️ Sistema de Defesa v3.0 - SOC Analyst Project

Sistema em Python que simula a rotina de um analista SOC N1.

### O que evoluiu do v2.0 para v3.0?
- *v1:* Bloqueio permanente
- *v2:* Bloqueio temporário com time.time()
- *v3.0 (este):* Geração de log auditável com datetime + bloqueio inteligente

### Funcionalidades
✅ Contador de falhas por IP  
✅ Bloqueio temporário de 300s  
✅ Liberação automática  
✅ Log auditável em ataques.log com timestamp  
✅ Código modular com funções

### Como rodar
python desefa_v3.py

### Exemplo de log gerado
[18/10/26 21:00:56] IP: 192.168.0.10 | STATUS: BLOQUEADO

Feito por Miguel Fernandes - Em transição para Cybersecurity | Fortaleza-CE
