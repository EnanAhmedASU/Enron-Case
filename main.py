import pickle 

enron_data = pickle.load(open(r"C:\Users\Owner\OneDrive\Documents\Github\Enron-Case\enron_data_unix.pkl","rb"))
print("No people int he data", len(enron_data))