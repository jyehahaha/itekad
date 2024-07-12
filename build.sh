echo "BUILD START"
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m pip uninstall dataclasses -y
python3 manage.py collectstatic --noinput --clear
python3 manage.py makemigrations
python3 manage.py migrate
echo "BUILD END"