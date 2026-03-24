import torch
import torch.nn as nn
import torch.nn.functional as F

     

# Create a Model Class that inherits nn.Module
class Model(nn.Module):
  # Input layer (chaque noeud est une case 0 si mur, 1 si accessible, puis on donne la position sur 2 noeud (x, y) pour chacun des 3 individus P1, P2, V, puis on donne le rayon d'action avec 1 si case dedans, 0 sinon)
  #(pour un labyrinthe 10*10 on a 2*100+6 neurones dans la couche
  #et on rajoute un des neurones pour indiquer les déplacements possibles
  #)-->
  # Hidden Layer1  -->
  # H2 --> H3 --> H4 --> (on essaiera d'aller à 10 mais on verra plus tard)
  # output (5 options de déplacement)
  def __init__(self, in_features=67, h1=200, h2=200,h3=200, h4=200, out_features=5):
    super().__init__() # instantiate our nn.Module
    self.fc1 = nn.Linear(in_features, h1)
    self.fc2 = nn.Linear(h1, h2)
    self.fc3 = nn.Linear(h2, h3)
    self.fc4 = nn.Linear(h3, h4)
    self.out = nn.Linear(h4, out_features)

  def forward(self, x):
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = F.relu(self.fc3(x))
    x = F.relu(self.fc4(x))
    x = F.softmax(self.out(x))
    return x

     

# Pick a manual seed for randomization
torch.manual_seed(41)
# Create an instance of model
model = Model()


#Couche entrée sera un tensor d'entiers on utilisera torch.IntTensor(array) pour convertir un Numpy array
X = #tenseurs de couches d'entrées, donc les différents états avant chaque dépalcements
y = #tenseurs de couche de sortie attendues, c'est-à-dire le bons déplacement qui est à faire

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41) #divise entre les données qu'on va utiliser pour entrainer et celle qu'on va utiliser pour vérifier que l'entrainement donne de bons résultat

# Set the criterion of model to measure the error, how far off the predictions are from the data
criterion = nn.CrossEntropyLoss()
# Choose Adam Optimizer, lr = learning rate (if error doesn't go down after a bunch of iterations (epochs), lower our learning rate)
optimizer = torch.optim.Adam(model.parameters(), lr=1)
     
# Train our model! (Pour le moment, cet entrainement a besoin qu'on sache exactement le bon coup, et non pas seulement qu'un était mauvais)
# Epochs? (one run thru all the training data in our network)
epochs = 100
losses = []
for i in range(epochs):
  # Go forward and get a prediction
  y_pred = model.forward(X_train) # Get predicted results

  # Measure the loss/error, gonna be high at first
  loss = criterion(y_pred, y_train) # predicted values vs the y_train

  # Keep Track of our losses
  losses.append(loss.detach().numpy())

  # print every 10 epoch
  if i % 10 == 0:
    print(f'Epoch: {i} and loss: {loss}')

  # Do some back propagation: take the error rate of forward propagation and feed it back
  # thru the network to fine tune the weights
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()






#Donner une prédiction à partir d'une entrée
donnees_entrees = torch.tensor([contenu])
     

with torch.no_grad():
  predi = (model(donnees_entrees))
     



# Save our NN Model
torch.save(model.state_dict(), 'my_really_awesome_iris_model.pt')
     

# Load the Saved Model
new_model = Model()
new_model.load_state_dict(torch.load('my_really_awesome_iris_model.pt'))
     

<All keys matched successfully>


# Make sure it loaded correctly
new_model.eval()
     

