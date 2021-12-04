DJANGO VERCEL
================================================================================

1. Deployment Database ServerLess:
----------------------------------
- Connect Supabase with Github
- Goto Supabase Dashboard
  https://app.supabase.io/
  
- Create New Project
- Get Connection String

2. Deployment Service:
----------------------
2.1. BASE SERVER base Ubuntu 20.00
- Clone repository
  git clone https://github.com/herbew/django_vercel.git

- Ubuntu server stup  
  sudo apt-get install language-pack-id
  sudo dpkg-reconfigure locales

- Enviroment
  sudo apt-get install -y python3 python3-pip 
  sudo apt-get install -y python3-venv

  python3 -m pip install --user pipenv

- Link repository
  sudo ln -s </root--fullpath>/django_vercel /opt/django_vercel

- Service environment
  python3 -m venv envdjangovercel
  
- Activate
  source envdjangovercel/bin/activate
  
2.2. INSTALL DJANGO

- cd /opt
  sudo ./django_vercel/utility/install_os_dependencies.sh install
  
- source envdjangovercel/bin/activate
  cd django_vercel
  ./utility/install_python_dependencies.sh
  
  ./manage.py makemigrations
  
  ./manage.py migrate sites
  ./manage.py makemigrations users
  ./manage.py migrate
  
  ./manage.py collectstatic
  ./manage.py createsuperuser
  


2.2. BASE SERVERLESS
