SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
echo "1 Script directory: $SCRIPT_DIR"

year="$(date +%Y)"

year_dir=$(cd $SCRIPT_DIR/../AoC_$year &> /dev/null && pwd)
echo "$year_dir"