# Install Dependencies
pip3 install -r build.sh
python3 manage.py collectstatic --no-input
# Run Migrations
python3 manage.py migrate
