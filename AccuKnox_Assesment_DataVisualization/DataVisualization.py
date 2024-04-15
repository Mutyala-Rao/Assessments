import requests
import matplotlib.pyplot as plt


def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data from the API: {e}")
        return None


def calculate_average_score(scores):
    if not scores:
        return None
    total_score = sum(score['score'] for score in scores)
    return total_score / len(scores)


def visualize_scores(scores):
    names = [score['name'] for score in scores]
    scores = [score['score'] for score in scores]

    plt.barh(names, scores, color='skyblue')
    plt.xlabel('Score')
    plt.ylabel('Student')
    plt.title('Test Scores of Students')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.gca().invert_yaxis()  # Invert y-axis for better readability
    plt.tight_layout()
    plt.show()


def main():
    api_url = "https://api.example.com/students/scores"
    scores_data = fetch_data_from_api(api_url)

    if scores_data:
        average_score = calculate_average_score(scores_data)
        if average_score:
            print(f"Average score: {average_score}")
        else:
            print("No scores found.")
        visualize_scores(scores_data)


if __name__ == "__main__":
    main()
