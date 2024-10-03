# Instance Configuration

## Steps to setting up the instance as required for the proyect
<p align="justify">
1. First you need to access to your instance.
</p>

---

<p align="justify">
2. Install <code>git</code> and clone the repository.
</p>

```
sudo apt install git
```
```
git clone https://github.com/Gjloz009/rag_system_for_traffic_regulations_cdmx
```
---

<p align="justify">
4. Install <code>Docker</code>. I'm using wsl2 I'll show how to install it for this particular case and also in a more general case.
</p>

<p align="justify">
4.1 Typicall case 
</p>

Please update the libraries.

```
sudo apt-get update
```
Now install docker 

```
sudo apt-get install docker.io
```

If you don´t want to preface the docker command with sudo, create a Unix group called docker and add users to it.

```
sudo groupadd docker
```

add user to the docker group

```
sudo usermod -aG docker $USER
```

Log out and log back in so the changes persist.

Verifiy that you can run docker commands without sudo.

```
docker run hello-world
```
Please refer to the docker docs for faq or any doubt if I was not clear.

> https://docs.docker.com/engine/install/linux-postinstall/

<p align="justify">
4.2 <code>WSL</code> case 
</p>

If you are working with wsl you have to download the docker for windows package and install it, the docker desktop will connect with your distribution in wsl. You have to initalize docker desktop every time you want to use it .

Please add user to docker group

```
sudo usermod -aG docker $USER
```

> https://docs.docker.com/desktop/install/windows-install/

If you have problems using docker in your wsl environment please check the access settings on the docker desktop in enabled.

<p align="center">
  <img src="images\docker_desktop_1.png">
</p>
