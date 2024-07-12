echo "BUILD START"

# Build the project
echo "Building the project..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip uninstall dataclasses -y

echo "Make Migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect Static..."
python manage.py collectstatic --noinput --clear

echo "BUILD END"