#wrote total votes to txt file

# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initializa a total vote counter.
total_votes = 0

#Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}
# Track Winning Candidate, Winning Count, and Winning Percentage
winning_candidate = " "
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Get the candidate name from each row. 
        candidate_name = row[2]

        #If the candidate doesn't match any existing candidate 
        #add it to the candidate list
        if candidate_name not in candidate_options:
           # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

         # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        #save results to the text file
        with open(file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal.
            election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
            print(election_results, end="")
            
            # Save the final vote count to the text file.
            txt_file.write(election_results)


            for candidate_name in candidate_votes:
                # Retrieve vote count and percentage of a candidate.
                votes = candidate_votes[candidate_name]
                vote_percentage = float(votes) / float(total_votes) * 100

                # Print out each candidate's name, vote count, and 
                # percentage of votes to the terminal
                #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

                #Determine winning vote count, winning percentage, and candidate
                if (votes>winning_count) and (vote_percentage>winning_percentage):
                    winning_count = votes
                    winning_candidate = candidate_name
                    winning_percentage = vote_percentage

            winning_candidate_summary = (
                f"------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage: .1f}%\n"
                f"-------------------------\n")
            #print(winning_candidate_summary)