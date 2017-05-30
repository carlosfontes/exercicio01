   1 # despdom2.py - Calculadora de despesas domesticas - versao 2
   2 # COMENTARIO MODIFICADO
   3 print 'Balanco de despesas domesticas'
   4 ana = float(raw_input('Quanto gastou Ana? '))
   5 bia = float(raw_input('Quanto gastou Bia? '))
   6 print
   7 total = ana + bia
   8 print 'Total de gastos: R$ %s' % total
   9 media = total/2
  10 print 'Gastos por pessoa: R$ %s' % media
  11 if ana < media:
  12     diferenca = media - ana
  13     print 'Ana deve pagar: R$ %s' %diferenca
  14 else:
  15     diferenca = media - bia
  16     print 'Bia deve pagar: R$ %s' % diferenca
