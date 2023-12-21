iris_model = pickle.load(open("IrisPrediction.h5", "rb")) #rb: read binary
new_pred = iris_model.predict(X_test) # testing (examination)
dfnew_pred = pd.DataFrame({'Actual': y_test, 'Predicted': new_pred})
dfnew_pred
