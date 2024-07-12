echo "BUILD START"
pip install --upgrade pip
pip uninstall dataclasses -y
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
python3.9 manage.py makemigrations
python3.9 manage.py migrate
echo "BUILD END"