class num2words:

    def take(self,m):           #sum of numbers from 1-19,20,30,40,50,60,70,80,90,1000
        sum=0
        for i in m:
            l=len(i)
            sum=sum+l
            #print(i,l)
        return (sum)
#****************************************************************
    def double(self,p,q):       #sum of numbers from 21-99,100,200,300,400,500,600,700,800,900
        sum=0
        for i in  p:
            for j in q:
                m=i+j
                l=len(m)
                sum=sum+l
                #print(m,l)
        return (sum)
#*****************************************************************
    def triple(self,p,q):       #sum of numbers from 101-119,201-219,301-319,401-419,501-519,601-619,701-719,801-819,901-919
        sum=0                    #110,120,130......190,210,220,230,........290,310,320,330,......410,420,430,...
        for i in p:
            for j in q:
                m = i +"hundred"+"and"+ j
                l = len(m)
                sum = sum + l
                #print(m,l)
        return (sum)

#******************************************************************
    def four_times(self,p,q,r):   #sum of numbers from 121-199,221-299,321-399..........921-999
        sum=0
        for i in p:
            for j in q:
                for k in r:
                    m=i+"hundred"+"and"+j+k
                    l=len(m)
                    sum=sum+l
                    #print(m,l)
        return (sum)
#*******************************************************************

single_digits = ["one", "two","three", "four", "five","six", "seven", "eight", "nine"]
two_digits = ["ten", "eleven", "twelve","thirteen", "fourteen","fifteen", "sixteen","seventeen", "eighteen", "nineteen"]
tens_multiple= ["twenty", "thirty", "forty", "fifty","sixty", "seventy", "eighty", "ninety"]
tens_power= ["hundred"]
thou=["onethousand"]
#****************************************************************
s=num2words()
single=s.take(single_digits)
#print(single)
teens=s.take(two_digits)
#print(teens)
tens_multi=s.take(tens_multiple)
#print(tens_multi)
thousand=s.take(thou)
#print(thousand)

#****************************************************************************
two= s.double(tens_multiple,single_digits)
#print(two)
tens=s.double(single_digits,tens_power)
#print(tens)
#**************************************************************
three= s.triple(single_digits,single_digits)
#print(three)
three_teen=s.triple(single_digits,two_digits)
#print(three_teen)
three_tee=s.triple(single_digits,tens_multiple)
#print(three_tee)
#************************************************************************
four=s.four_times(single_digits,tens_multiple,single_digits)
#print(four)
#*****************************************************

sum_of_all=single+teens+two+three+three_teen+four+tens+thousand+tens_multi+three_tee
print(sum_of_all)