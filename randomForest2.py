from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. 데이터 불러오기
iris = load_iris()
X = iris.data        # 꽃받침/꽃잎의 길이와 너비
y = iris.target      # 품종 (0, 1, 2)

# 2. 학습용/테스트용 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 랜덤 포레스트 분류기 생성 (기본 트리 100개)
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# 4. 학습
clf.fit(X_train, y_train)

# 5. 예측
y_pred = clf.predict(X_test)

# 6. 정확도 출력
print("정확도: {:.2f}%".format(accuracy_score(y_test, y_pred) * 100))
