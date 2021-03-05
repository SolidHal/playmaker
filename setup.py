from setuptools import setup

setup(name='playmaker',
      version='0.6.4',
      description='Apk manager with web interface based on aurora stores GPlayApi',
      url='https://github.com/SolidHal/playmaker',
      author='SolidHal',
      author_email='hal@halemmerich.com',
      license='MIT',
      packages=['playmaker'],
      package_data={
          'playmaker': [
              'index.html',
              'static/*',
              'static/css/*',
              'static/fonts/*',
              'static/js/*',
              'views/*'
          ],
      },
      install_requires=[
            'pyaxmlparser',
            'pycryptodome',
            'tornado<5',
            'pyjnius',
            'tornado-crontab'
      ],
      scripts=['pm-server']
)
