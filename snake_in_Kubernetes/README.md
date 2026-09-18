# 🐍 Kerberized Multi-Container Python Snake Game (Kubernetes & VNC)

A cloud-native, microservice-architected **Python Snake Game** written with the standard `turtle` graphics library and fully containerized to run inside a **Kubernetes cluster**. This architecture showcases advanced DevOps patterns, including a multi-container **Kerberos Key Distribution Center (KDC) sidecar**, a headless virtual frame-buffer canvas, grid-aligned gameplay, and persistent keyboard input event mapping streamed live over an isolated VNC network tunnel.

---

## 🚀 Engineering & Kubernetes Highlights

*   **Multi-Container Sidecar Pattern:** Renders your core Python game client and a fully functional Kerberos KDC Server side-by-side within a shared pod workspace. They utilize isolated loopback network pathways (`127.0.0.1`) and decoupled volume assets.
*   **Decoupled Configuration Mapping:** Abstracts enterprise authentication configurations from the container engine logic using a native Kubernetes `ConfigMap` to mount `krb5.conf` settings seamlessly into both execution layers.
*   **Headless X11 Display Emulation:** Eliminates classic POSIX container graphical errors (`_tkinter.TclError`) by injecting a virtual X11 server engine (`Xvfb`) and `python3-tk` dependencies directly inside stripped down images (`python:3.11-slim`).
*   **Isolated In-Cluster VNC Streaming:** Packages a dedicated background display broadcaster (`x11vnc`) directly into the game loop. This exposes graphic rendering engines out of headless cluster spaces over port `5900` without altering base Python game frames.
*   **Reliability Performance Optimization:** Resolves historical input buffer rendering traps and unaligned hitboxes by locking down directional keystroke frame state toggles and snapping asset generation vectors directly to strict 20-unit grid loops.

---

## 🎮 How To Play & Game Settings

1.  **Objective:** Control your snake to consume as many turtles as possible on a closed 600 × 600 pixel grid system. 
2.  **Controls:**
    *   `Arrow Keys` — Direct the snake's velocity vectors smoothly across grid points.
    *   `Spacebar` — Toggles runtime Pause and Play functions.
    *   `R Key` — Triggers an application-level reset when on the `GAME OVER` screen. This clean-wipes old graphical data structures from the memory cache and lets you replay infinitely without restarting cluster pods.
3.  **Dynamic Progressive Difficulty:** To challenge your skills, the **Pause function is permanently disabled** the moment you achieve a score of **3 or more points**. You must stay in constant motion to survive.

---

## 🐳 Step 1: Local Image Compilation

To run this application without pushing images to public registries like Docker Hub, you must build your containers locally on your host machine.

### 1. Build the Headless Snake Game Image
Create your main `Dockerfile` and compile the package:
```bash
docker build -t local-snake/game:1.0 .
```

### 2. Build the Independent Kerberos KDC Server Image
Create a file named `Kdc.dockerfile` and build the local authentication database backend:
```bash
docker build -f Kdc.dockerfile -t local-kerberos/kdc:1.0 .
```

---

## 🏗️ Step 2: Cluster Deployment Configurations

Select the deployment pathway below that matches your targeted cloud infrastructure model.

### Option A: Local Minikube Deployment (Air-Gapped Sideloading)
Minikube utilizes an isolated machine runtime engine (`containerd`). To bypass Docker Hub errors, sideload your locally built computer images directly into the internal cache of your minikube nodes.

1. **Verify Minikube Engine is Awake:**
   ```bash
   minikube start
   ```
2. **Sideload both built images into Minikube's cache:**
   ```bash
   minikube image load local-snake/game:1.0
   minikube image load local-kerberos/kdc:1.0
   ```
3. **Configure your target alias shortcuts:**
   ```bash
   alias kubectl="minikube kubectl --"
   ```
4. **Deploy the manifest infrastructure:**
   ```bash
   kubectl apply -f k8s-snake-kerberos.yaml
   ```

### Option B: Production Kubernetes Deployment (Using Local Registry)
In a bare-metal or production cloud Kubernetes cluster without an air-gapped loader tool, deploy a secure local registry right inside your cluster namespace to distribute your images to working nodes.

1. **Spin up a lightweight in-cluster container registry:**
   Save as `registry.yaml` and apply:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: local-registry
     namespace: kube-system
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: local-registry
     template:
       metadata:
         labels:
           app: local-registry
       spec:
         containers:
           - name: registry
             image: registry:2
             ports:
               - containerPort: 5000
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: local-registry
     namespace: kube-system
   spec:
     ports:
       - port: 5000
         targetPort: 5000
     selector:
       app: local-registry
   ```
2. **Forward and push your images to the internal repository:**
   ```bash
   kubectl port-forward svc/local-registry 5000:5000 -n kube-system &
   
   docker tag local-snake/game:1.0 localhost:5000/local-snake/game:1.0
   docker tag local-kerberos/kdc:1.0 localhost:5000/local-kerberos/kdc:1.0
   
   docker push localhost:5000/local-snake/game:1.0
   docker push localhost:5000/local-kerberos/kdc:1.0
   ```
3. **Deploy the core application manifest:**
   *(Ensure the `image:` paths in your `k8s-snake-kerberos.yaml` reflect your node repository endpoints: `localhost:5000/...`)*
   ```bash
   kubectl apply -f k8s-snake-kerberos.yaml
   ```

---

## 📺 Step 3: Stream and Play via VNC Viewer

1. **Monitor Cluster Scheduling Stability:**
   Ensure both sidecar containers initialize cleanly into a **`2/2 Running`** status block:
   ```bash
   kubectl get pods -w
   ```
2. **Open a Secure Network Port-Forward Tunnel:**
   Forward traffic from the deployment controller straight down to port `5900`:
   ```bash
   kubectl port-forward deployment/kerberized-snake-game 5900:5900
   ```
3. **Establish a Link with Your VNC Client:**
   * Open **Remmina** (or your preferred VNC viewer).
   * Initialize a new connection pointing to: **`localhost:5900`**.
   * Left-click your cursor directly inside the freshly populated black screen viewer window to bind mouse and keyboard vectors.
   * Tap **`Spacebar`** to start and have fun playing!

---

## 🔍 Verification & Kerberos Auditing

To prove to interviewers or security auditors that your cloud-native application pod can natively interact with its secure sidecar authentication backend workspace, you can mint certificates manually right inside the running container namespace.

### 1. Request a Ticket Granting Ticket (TGT) via CLI
Force the game application container loop to request an authorized token from the KDC server container using our pre-configured administrative credentials:
```bash
kubectl exec -it deployment/kerberized-snake-game -c snake-app -- kinit admin/admin@SNAKEGAME.LOCAL
```
*(When prompted for password confirmation, enter: `Password123`)*

### 2. Audit the Cached Cryptographic Payload
Confirm the token exists and inspect its expiration metadata rules:
```bash
kubectl exec -it deployment/kerberized-snake-game -c snake-app -- klist
```
**Expected Output Validation Structure:**
```text
Ticket cache: FILE:/tmp/krb5cc_snake
Default principal: admin/admin@SNAKEGAME.LOCAL

Valid starting       Expires              Service principal
09/18/2026 05:58:12  09/19/2026 05:58:12  krbtgt/SNAKEGAME.LOCAL@SNAKEGAME.LOCAL
```

---

## 📂 Project Manifest Blueprint

```text
├── Dockerfile                  # Builds the headless python graphic loop with Xvfb & VNC
├── Kdc.dockerfile             # Sets up the automated Kerberos KDC server database 
├── k8s-snake-kerberos.yaml    # Combined ConfigMap, RBAC rules, and Pod Sidecar manifest
├── main.py                    # Coordinates the infinite game loop state & pause locks
├── snake.py                   # Handles game vector translation & input buffer tracking
├── food.py                    # Dictates colorspace transformations and strict grid snapping
└── scoreboard.py              # Drives graphic text updates & canvas resets
```
