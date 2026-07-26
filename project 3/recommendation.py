from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

jobs = {
    "Data Scientist":
        "python machine learning statistics pandas numpy data analysis",

    "Web Developer":
        "html css javascript react node web frontend backend",

    "AI Engineer":
        "python deep learning tensorflow pytorch artificial intelligence",

    "Cloud Engineer":
        "aws azure cloud docker kubernetes linux",

    "Cyber Security":
        "network security ethical hacking kali penetration testing"
}

print("=" * 60)
print("AI TECH STACK RECOMMENDATION SYSTEM")
print("=" * 60)

skills = input("\nEnter your skills (comma separated): ").lower()

documents = list(jobs.values())
documents.append(skills)

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(documents)

user_vector = tfidf[-1]
job_vectors = tfidf[:-1]

similarity = cosine_similarity(user_vector, job_vectors)

scores = similarity.flatten()

results = list(zip(jobs.keys(), scores))

results.sort(key=lambda x: x[1], reverse=True)

print("\nTop Recommendations\n")

for job, score in results:
    print(f"{job} ---> Match Score: {score:.2f}")