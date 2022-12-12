
# Script used to copy the AoC template and run it, to download the daily input
# Then it will open VSCode to edit the solution and Firefox to see the problem


# Create vars for later use
year="$(date +%Y)"
today="$(date +%d)"

template=day00.py
fileName=day${today}.py


# Move to directory where the script is located
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR/$year

cp $template $fileName

# Replace date inside the file
sed -i "s/0/${today}/" $fileName

# # Run the file (to download the input)
python $fileName

# # Open the file and the problem statement
code .
code $fileName
firefox https://adventofcode.com/${year}/day/${today}

exit 0
