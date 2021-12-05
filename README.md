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
----------------------------------


INSTALL SERVER Environment
----------------------------

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
  

INSTALL DJANGO Environment
-----------------------------

- cd /opt
  sudo ./django_vercel/utility/install_os_dependencies.sh install
  

INSTALL DJANGO Environment
-----------------------------
  
- source envdjangovercel/bin/activate
  cd django_vercel
  ./utility/install_python_dependencies.sh
  

DJANGO Initialize
-----------------------------
  ./manage.py makemigrations
  
  ./manage.py migrate sites
  ./manage.py makemigrations users
  ./manage.py migrate
  
  ./manage.py collectstatic
  ./manage.py createsuperuser
  


2.2. BASE SERVERLESS
--------------------------
- Ubuntu Instant cloud development
  #Ref: https://vercel.com/cli
  
- Create Project
  --name project
  --Env variable
    DATABASE_URL
    DJANGO_ADMIN_URL 
    DJANGO_SETTINGS_MODULE
    DJANGO_SECRET_KEY
    DJANGO_SECURE_SSL_REDIRECT
    DJANGO_DEBUG
    DJANGO_DEFAULT_FROM_EMAIL
    DJANGO_EMAIL_SUBJECT_PREFIX
    DJANGO_EMAIL_BACKEND
    MAILJET_API_KEY
    MAILJET_SECRET_KEY
    DJANGO_ALLOWED_HOSTS
    REDIS_URL
    
    
  ::Ubuntu
  
  sudo apt-get install npm
  sudo npm i -g vercel
  
  IF notsup Unsupported engine for vercel@23.1.2: wanted: {"node":">= 12"} (current: {"node":"10.19.0","npm":"6.14.4"})
  #Ref: https://joshtronic.com/2021/05/09/how-to-install-nodejs-16-on-ubuntu-2004-lts/
  
  - curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
  - sudo apt-get install -y nodejs
  - node --version
  
  
- Server less deployment
  Ref: https://github.com/jayhale/vercel-django-example
  
  ::
  cd django_vercel
  
  vercel
  
  > Log in to Vercel github
  > Please visit the following URL in your web browser:
  > https://vercel.com/api/registration/login-with-github?mode=login&next=https%3A%2F%2Fvercel.com%2Fnotifications%2Fcli-login-oob

  > After login is complete, enter the verification code printed in your browser.
  
  Vercel CLI 23.1.2
  > > No existing credentials found. Please log in:
  > Log in to Vercel github
  > Success! GitHub authentication complete for herbew@gmail.com
  ? Set up and deploy “~/django_vercel”? [Y/n]
  
  ? Which scope do you want to deploy to? 
  
  

