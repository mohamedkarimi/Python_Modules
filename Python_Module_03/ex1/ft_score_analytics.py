import sys
print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1>"
          " <score2> ...")
else:
    scores = []
    i = 1

    try:
        while i < len(sys.argv):
            scores.append(int(sys.argv[i]))
            i += 1
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    except ValueError:
        i = 1
        while i < len(sys.argv):
            print(f"Invalid parameter: {sys.argv[i]}")
            i += 1
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py <score1>"
            " <score2> ...")
