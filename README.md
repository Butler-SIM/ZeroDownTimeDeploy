# ZeroDownTimeDeploy

flow

GitHubAction -> EC2 -> NginxProxy 8000-> Gunicorn(Django-images_01) -> deploy_pull.sh(comtainer Git Pull -> comtainer restart
                              Gunicorn Down ↘︎  
                                  8001  Gunicorn2(Django-images_02) -> deploy_pull.sh(comtainer Git Pull -> comtainer restart
