# -*- coding: utf-8 -*-
#######################
import data
import noclosecmd
#######################
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#######################

#usinp = (raw_input('-> '))#ввод имени, открываемого файла
usinp = "10-10-1.CSV"

#print "user input: ", type(usinp)
len_usinp = len(str(usinp))
#print type(len_usinp)
usinp_e = usinp[0:-4] + 'e' + usinp[-4:len_usinp]
#print usinp_e
#название файла без разширения, для отображения на граффике
#usinp_title = usinp[0:-4]
print(u"Введите наименование для спектрограммы")
usinp_title = (raw_input('\n -> '))#ввод имени для отображения на графике
#
s = open(usinp).read()#прочитали исходный файл

#блок замен
s = s.replace('"Peak"', '0')#заменяем значения "Peak" на ноль
s = s.replace('"', '')#удаляем кавычки


#создаем новый файл для записи изменений в него
f = open(usinp_e, 'w')#открыли файл (создали)
f.write(s)#записали
f.close()#закрыли

#создаем датафрэйм
frame = pd.read_csv(usinp_e, sep = ",", header = None, names = ['Wavelength', 'Abs', 'Peak'], skiprows = 18)

allarray = np.array(frame)
print allarray
Wavelength = np.array(frame['Wavelength'])
#print x
Abs = np.array(frame['Abs'])
#print y
Peak = np.array(frame['Peak'])
#print Abs
data = Abs


#зона вывода графф
plt.figure(num = 1, figsize=(10,6), dpi= 300)
plt.suptitle(usinp_title, fontsize=16)
plt.subplots_adjust(hspace=0.4)#
#первый графф
plt.subplot(2,1,1)
plt.plot(Wavelength, Abs) 
#plt.xlabel('time, sec')
#plt.ylabel('I, mA')
#plt.title(u'Изменение тока по времени', fontsize=12)
plt.grid(True)

plt.plot(Wavelength, Peak)



#второй графф
#plt.subplot(2,1,2)
#plt.plot(mv, ma, '-r')
#plt.xlabel('Volts, mV')
#plt.ylabel('I, mA')
#plt.title(u'Вольт-амперная характеристика', fontsize=12)
#plt.grid(True)
#вывод
plt.figure(1).savefig(usinp_title + 'e' + '.png')
plt.figure(1).savefig(usinp_title + 'e' + '.pdf')
plt.show()


noclosecmd.noclosecmd()
