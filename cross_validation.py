import numpy as np
def cross_validation(data, model, k=5):
    num_validation_samples = len(data) / k

    np.random.shuffle(data)

    validation_scores = []

    for fold in range(k):
        # divide data to validation & training
        validation_data = data[num_validation_samples*fold : num_validation_samples*(fold+1)]
        training_data = data[0 : num_validation_samples*fold] + data[num_validation_samples*(fold+1):]
        # get validation score
        model.train(training_data)
        validation_score = model.evaluate(validation_data)
        validation_scores.append(validation_score)
        
    return np.average(validation_score)