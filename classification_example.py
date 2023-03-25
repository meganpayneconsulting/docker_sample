from sklearn.model_selection import train_test_split
from pandas import read_csv
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from joblib import dump
import numpy as np

df = read_csv("penguins_size.csv")
scaler = StandardScaler()
log_reg = LogisticRegression()

# the NA rows aren't helpful. 
df.dropna(how="any", inplace=True)

x_variables = ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']
X_train, X_test, y_train, y_test = train_test_split(df[x_variables], df['species'], random_state=42)


## Let's save some data to predict on. 
X_test.to_csv("penguin_data_to_predict.csv")
X_test.head()

def train_model(X_train, y_train, x_variables):
    """ This takes X_train, y_train and returns a trained model. 
        Vars are numeric and should be scaled first. """
    X_train = scaler.fit_transform(X_train[x_variables].to_numpy())
    return log_reg.fit(X_train, y_train)

def predict_from_model(new_data, model):
    new_data = np.array(new_data).reshape(1, -1)
    return model.predict(new_data)

# Train the model and run a sample prediction
model = train_model(X_train, y_train, x_variables)
predict_from_model([0.576190, 0.108108, 0.584906, 0.650000], model)

# Save and load the model and the scaler fit using joblib
dump(model, 'final_model.sav')
dump(scaler, 'scaler_fit.sav', compress=True)