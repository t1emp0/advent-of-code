
# Script used to copy the AoC template and run it, to download the daily input
# Then it will open VSCode to edit the solution and web browser to see the problem


# Create vars for later use
year="$(date +%Y)"
today_without_zeros="$(date +%-d)"
today_with_zeros="$(date +%d)"

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# echo "$script_dir"
year_dir=$(cd $SCRIPT_DIR/../AoC_$year &> /dev/null && pwd)
# echo "$year_dir"

template_name=AoC_Template.py
file_name=AoC${year}_Day$today_with_zeros.py

# Move to directory where the script is located
cd "$year_dir"
cp $"$script_dir/$template_name" $"$file_name"

# Replace date inside the file
sed -i "s/0/$today_without_zeros/" $"$file_name"
# sed -i "s/\=0/\=/" $"$file_name"

# Run the file (to download the input)
python $"$file_name"

# # Open the file and the problem statement
code .
code $"$file_name"
start https://adventofcode.com/${year}/day/${today_without_zeros}

# exit 0
