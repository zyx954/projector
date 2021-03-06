import pickle
import numpy as np
from sklearn import preprocessing
import os

# import os


def test(trainingPercentage,
                       validationPercentage,testingPercentage):
    boardOneOnDataset = trainingPercentage / 100.0
    boardTwoOnDataset = (trainingPercentage + validationPercentage) / 100.0
    print boardOneOnDataset
    print boardTwoOnDataset
    # print "hee "
def dataProcess(trainingPercentage,
                       validationPercentage,testingPercentage,pickleFileName):
    #get data and target
    try:
        print "####enter dataPrecess before f "
        # f = open('./tweetsFeatureData.pkl', 'rb')
        f = open('./' + pickleFileName + '.pkl', 'rb')
        print "enter dataPrecess"

        data = pickle.load(f)
        target = pickle.load(f)
        IDs =  pickle.load(f)

        print(data.shape, data.dtype)
        print(target.shape, target.dtype)
        print data[1:100]
        print target[1:100]
        print IDs[1]
        # print test.shape

        i=0
        for id in IDs:
            if(id == 330029892479639553):
                print "this is target *****" + str(i)
                print str(data[i])
                print IDs[i]
                print "********end ****"
            i=i+1


        #shufflers(needs to match the data and target)
        r = np.random.permutation(len(target))
        print r
        data = data[r, :]
        target = target[r]
        IDs = IDs[r]
        print  type(data)
        print  (target)

        print(data.shape, data.dtype)
        print(target.shape, target.dtype)

        print data[1:100]
        print target[1:100]


        #there no missing value


        #
        # #normalize data with norm "l2"
        # data = preprocessing.normalize(data,norm="l2")


        #creat train_data , validatiaon_data , test_data
        boardOneOnDataset = trainingPercentage / 100.0
        boardTwoOnDataset = (trainingPercentage + validationPercentage) / 100.0
        train_data, validation_data, test_data = np.split(data, [int(boardOneOnDataset*len(data)),int(boardTwoOnDataset*len(data))])
        train_target, validation_target, test_target = np.split(target, [int(boardOneOnDataset*len(target)),int(boardTwoOnDataset*len(target))])
        train_IDs, validation_IDs, test_IDs = np.split(IDs, [int(boardOneOnDataset*len(IDs)),int(boardTwoOnDataset*len(IDs))])

        print train_data.shape,validation_data.shape,test_data.shape
        print train_target.shape,validation_target.shape,test_target.shape
        print train_IDs.shape,validation_IDs.shape,test_IDs.shape

        #


        # save data to pickle formate
        data_pickle={"train_data":train_data,"validation_data":validation_data,"test_data":test_data}
        target_pickle={"train_target":train_target,"validation_target":validation_target,"test_target":test_target}
        IDs_pickle={"train_IDs":train_IDs,"validation_IDs":validation_IDs,"test_IDs":test_IDs}


        if(os.path.isfile('data_pickle.pkl')):
            os.remove("data_pickle.pkl")
            print "data_pickle.pkl removed"
        if(os.path.isfile('target_pickle.pkl')):
            os.remove('target_pickle.pkl')
            print "target_pickle.pkl removed"
        if (os.path.isfile('IDs_pickle.pkl')):
            os.remove('IDs_pickle.pkl')
            print "IDs_pickle.pkl removed"

        output_data = open('data_pickle.pkl', 'wb')
        output_target = open('target_pickle.pkl', 'wb')
        output_IDs = open('IDs_pickle.pkl', 'wb')



        pickle.dump(data_pickle, output_data)

        pickle.dump(target_pickle, output_target)
        pickle.dump(IDs_pickle, output_IDs)

        return len(train_data),len(validation_data),len(test_data)

    finally:
        f.close()
        output_data.close()
        output_target.close();
        print "all files closed "

# if __name__ == '__main__'and __package__ is None:
#     __package__ = "Training.DataPreprocess"
#     print ' test '