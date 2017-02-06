#test3
import matplotlib.pyplot as plt

Wavelength = [1,2,3,4,5,6,7,8,9,10]
Abs = [10,25,40,55,60,75,80,95,100,115]
#зона вывода графф
plt.figure(num = 1, dpi= 150)
plt.suptitle("title", fontsize=16)
plt.subplots_adjust(hspace=0.4)#
#первый графф
plt.subplot(2,1,1)
plt.plot(Wavelength, Abs) #,'-gD', markevery=markers_on
#plt.xlabel('time, sec')
#plt.ylabel('I, mA')
#plt.title(u'Изменение тока по времени', fontsize=12)
plt.grid(True)

#вывод
plt.show()
