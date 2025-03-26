# Test Automation for DQE environment preparation 

Configure Jenkins to Use the Pipeline from Git:
**In Jenkins, create a new job or edit an existing job.**
1) Choose Pipeline as the job type;
2) Under the Pipeline section, select Pipeline script from SCM;
3) Configure the SCM settings to point to your Git repository:
* SCM: Git
* Repository URL: https://github.com/DanyaHDanny/tafordqe
* Branch: */main (or the branch where your Jenkinsfile is stored)
* Script Path: Jenkinsfile (or the name of the file you saved)