#!/bin/bash

# Generate a random number between 1 and 100
target_number=$(( (RANDOM % 100) + 1 ))

# Counter for attempts
attempts=0

# Maximum number of attempts
max_attempts=5

while true; do
    # Increase the attempts counter
    ((attempts++))

    # Check the number of attempts
    if [ $attempts -gt $max_attempts ]; then
        echo "Sorry, you've run out of attempts. The correct number was $target_number."
        break
    fi

    # Ask the user to guess the number
    read -p "Guess the number (between 1 and 100): " guess

    # Check if the guess is correct
    if [ $guess -eq $target_number ]; then
        echo "Congratulations! You guessed the right number."
        break
    elif [ $guess -lt $target_number ]; then
        echo "Too low. Try again."
    else
        echo "Too high. Try again."
    fi
done
