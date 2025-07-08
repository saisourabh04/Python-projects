import csv

def read_csv(file_name):
    try:

        with open(file_name) as file:
            data=csv.reader(file)
            return list(data)

        data=read_csv('Data2.csv')
        # with open('data2.txt','w') as file:
        #     for row in data[1:]:
        #         print(row[1])
        #         age=int(row[1])
        #         if age>=20 and age<=25:
        #              file.write(' '.join(row)+'\n')

        with open('data2.csv','w',newline='') as file:
            csv_writer=csv.writer(file)
            csv_writer.writerow(['country','Age','Zip code','Purchased item'])
            for row in data[1:]:

                age=int(row[1])
                if age>=20 and age<=25:
                     csv_writer.writerow(row)
    except:
        print('file not found')



#Homework, Find the records where age is between 20-25 years and you have to print their names in a txt file.