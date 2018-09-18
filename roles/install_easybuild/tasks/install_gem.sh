gpg2 --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -L get.rvm.io | bash -s stable
source /etc/profile.d/rvm.sh

# install ruby 1.9.3
rvm requirements
rvm install 1.9.3
rvm use 1.9.3 --default

# install rubygems
rvm rubygems current

#gem install fpm