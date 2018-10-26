import pandas as pd
import numpy as np


class MatrixFactorization():

    # Initializing the user-property rating matrix, no. of latent features, alpha and beta.
    def __init__(self, R, K, alpha, beta, iterations):
        self.R = R
        self.num_users, self.num_properties = R.shape
        self.K = K
        self.alpha = alpha
        self.beta = beta
        self.iterations = iterations


    # Ratings for user i and moive j
    def get_rating(self, i, j):
        prediction = self.b + self.b_u[i] + self.b_i[j] + self.P[i, :].dot(self.Q[j, :].T)
        return prediction


    # Full user-property rating matrix
    def full_matrix(self):
        return mf.b + mf.b_u[:,np.newaxis] + mf.b_i[np.newaxis:,] + mf.P.dot(mf.Q.T)


    # Computing total mean squared error
    def mean_square_err(self):
        xs, ys = self.R.nonzero()
        predicted = self.full_matrix()
        error = 0
        for x, y in zip(xs, ys):
            error += pow(self.R[x, y] - predicted[x, y], 2)
        return np.sqrt(error)

    # Stochastic gradient descent to get optimized P and Q matrix
    def stochastic_gradient_descent(self):
        for i, j, r in self.samples:
            prediction = self.get_rating(i, j)
            e = (r - prediction)

            self.b_u[i] += self.alpha * (e - self.beta * self.b_u[i])
            self.b_i[j] += self.alpha * (e - self.beta * self.b_i[j])

            self.P[i, :] += self.alpha * (e * self.Q[j, :] - self.beta * self.P[i,:])
            self.Q[j, :] += self.alpha * (e * self.P[i, :] - self.beta * self.Q[j,:])

    
    # Initializing user-feature and property-feature matrix 
    def train(self):
        self.P = np.random.normal(scale=1./self.K, size=(self.num_users, self.K))
        self.Q = np.random.normal(scale=1./self.K, size=(self.num_properties, self.K))

        # Initializing the bias terms
        self.b_u = np.zeros(self.num_users)
        self.b_i = np.zeros(self.num_properties)
        self.b = np.mean(self.R[np.where(self.R != 0)])

        # List of training samples
        self.samples = [
        (i, j, self.R[i, j])
        for i in range(self.num_users)
        for j in range(self.num_properties)
        if self.R[i, j] > 0
        ]

        # Stochastic gradient descent for given number of iterations
        training_process = []
        for i in range(self.iterations):
        	np.random.shuffle(self.samples)
	        self.stochastic_gradient_descent()
	        mean_square_err = self.mean_square_err()
	        training_process.append((i, mean_square_err))
	        # if (i+1) % 20 == 0:
	        #     print("Iteration: %d ; error = %.4f" % (i+1, mean_square_err))

        return training_process

    
# new matrix holds the top n index of property. Index is the user id

def topn_of_property(matrix, topn):
    new_matrix = []

    for line in matrix:
        new_line = sorted(range(len(line)), key=lambda i: line[i], reverse=True)[:topn]
        new_matrix.append(new_line)

    return new_matrix

# read rating file,
r_cols = ['property_id', 'user_id', 'rating']
ratings = pd.read_csv('reviews.csv', sep = ',', names = r_cols)



R= np.array(ratings.pivot_table(index = 'user_id', columns ='property_id', values = 'rating').fillna(0))

mf = MatrixFactorization(R, K=20, alpha=0.001, beta=0.01, iterations=200)
training_process = mf.train()

f_matrix = mf.full_matrix().tolist()

# print()
# print("P x Q:")
# print(mf.full_matrix())
# print()



# can be saved to file
# print(topn_of_property(f_matrix, 20))





