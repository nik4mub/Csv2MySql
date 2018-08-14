import pandas as panda
from sqlalchemy import create_engine
import csv
import sys

def main(filename):

    try:
        #read file
        print("Now processing %s" % (filename))
        csvfile = panda.read_csv(filename, header=0)

        ##'mysql://username:password@localhost/dbname'
        ## Connect to DB, Change Db connection to approproate name

        print("Data being inserted")
        engine = create_engine('mysql://pop-user:pop-pw@localhost/popdb')
       
        with engine.connect() as conn, conn.begin():
            csvfile.to_sql('csv', conn, if_exists='append', index=False)
            print("starting Queries")
            conn.execute('Select MIN(POPESTIMATE2014), MAX(POPESTIMATE2013),' +
                            'Sum(POPESTIMATE2012)/length(POPESTIMATE2012),' +
                             'stddev(POPESTIMATE2012) from csv')
            conn.close()                 
        print("All Done")
    except:
        print('Something went wrong. Sorry man. Check the Source Code')
        

argument =  raw_input('Enter CSV File(include csv extension): ')
main(str(argument))
exitapp =  raw_input('Press Enter to Quit: ')

