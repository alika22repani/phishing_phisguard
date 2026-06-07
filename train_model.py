import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Baca dataset
df = pd.read_csv("dataset/phishing.csv")

# Fitur yang dipakai
features = [
    'NumDots', 'UrlLength', 'NumDash', 'NoHttps', 'IpAddress',
    'HostnameLength', 'PathLength', 'QueryLength', 
    'NumSensitiveWords', 'NumNumericChars'
]

X = df[features]
y = df['CLASS_LABEL']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# NORMALISASI (ini penting!)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model KNN dengan K=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# Prediksi
y_pred = knn.predict(X_test_scaled)

# Akurasi
accuracy = accuracy_score(y_test, y_pred)
print("Akurasi:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Simpan model dan scaler
joblib.dump(knn, "model/knn_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("\n✅ Model dan scaler berhasil disimpan!")