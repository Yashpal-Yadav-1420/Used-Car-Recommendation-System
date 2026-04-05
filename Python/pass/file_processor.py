# file_processor.py

def process_marks():

    try:
        with open("marks.txt", "r") as infile, open("processed_results.txt", "w") as outfile:

            for line in infile:
                line = line.strip()

                if not line:
                    continue

                name, score = line.split(",")

                score = int(score)

                # calculate new value (add 5 bonus marks)
                new_score = score + 5

                result = f"{name}, Original: {score}, Updated: {new_score}\n"

                outfile.write(result)

        print("Processing complete. Results saved in processed_results.txt")

    except FileNotFoundError:
        print("marks.txt file not found.")


if __name__ == "__main__":
    process_marks()