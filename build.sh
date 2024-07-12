echo "BUILD START"

# Build the project
echo "Building the project..."
python3.10 -m pip install --upgrade pip
python3.10 -m pip install -r requirements.txt
python3.10 -m pip uninstall dataclasses -y

echo "Make Migration..."
python3.10 manage.py makemigrations --noinput
python3.10 manage.py migrate --noinput

echo "Collect Static..."
python3.10 manage.py collectstatic --noinput --clear

echo "BUILD END"