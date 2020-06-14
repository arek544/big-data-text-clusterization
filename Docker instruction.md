1. Install Docker tool (or Docker desctop)  
   Follow the instructions:
   - Windows: https://docs.docker.com/toolbox/toolbox_install_windows/#how-to-uninstall-toolbox
2. Sign up for an account on page [docker.com](https://hub.docker.com/signup)
3. Launch: Docker Quickstart terminal  
4. Go to directory of your project
   ```bash
   cd "your path"
   ```
5. Run command: 
   ```bash
   docker pull jupyter/pyspark-notebook
   ```
6. Run command:
   ```bash
   docker run -it -p 8888:8888 -v "$(pwd):/home/jovyan/work" jupyter/pyspark-notebook  --name spark
   ```
7. To stop docker: 
   ```bash
   docker stop spark
   ```
8. Open Kitematic and manage container (launch notebooks, run scripts etc.)
9. To access jupyter server runing inside container you have to use IP address of docker (192.168.99.100)

---

To run script from Docker Quickstart terminal
   ```bash
   docker exec -it spark <path to script>
   ```


