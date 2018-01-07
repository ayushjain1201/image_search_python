import cv2
import numpy as np
import glob

#empty list to store template images
template_data=[]
#make a list of all template images from a directory
files1= glob.glob('img/template*.jpg')

for myfile in files1:
    image = cv2.imread(myfile,0)
    template_data.append(image)

test_image=cv2.imread('img/photo1.jpg')
#test_image= cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
i=0
j=0
k=255
ct=0
l=10
imgno=1
#loop for matching
for tmp in template_data:
	#template = cv2.imread('img/template.jpg',0)
	
	i%=256
	j%=256
	k%=256
	ct=0
	w, h = tmp.shape[::-1]
	imageGray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(imageGray,tmp,cv2.TM_CCOEFF_NORMED)
	#cv2.putText(test_image,'COUNT: %r' %ct, (10,30), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 2)
	threshold = 0.8
	p= []
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
		#cv2.rectangle(test_image, pt, (pt[0] + w, pt[1] + h), (i,j,k), 2)
		#print(pt[0],pt[1])
		flag=1
		for cnt in range(len(p)):
			#print(cnt)
			if (pt[0] >= p[cnt][0]+w or p[cnt][0] >= pt[0]+w ):
				continue
			elif (pt[1] >= p[cnt][1]+h or p[cnt][1] >= pt[1] +h ):
				continue
			else:
				flag=0
				break
		if flag==1:
			cv2.rectangle(test_image, pt, (pt[0] + w, pt[1] + h), (i,j,k), 2)
			ct+=1
			p.append([pt[0],pt[1]])
	cv2.putText(test_image,'COUNT: %r' %ct, (l,300), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (i, j, k), 2)
	cv2.imshow("Template"+str(imgno), tmp)
	imgno+=1
	i=i+31
	j= j+81
	k= k+101
	l+=400
cv2.imshow('Result',test_image)
cv2.waitKey(0)