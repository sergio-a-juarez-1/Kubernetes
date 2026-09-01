# Kubernetes & Helm Masterclass: From Containers to Package Management

Welcome to the official repository for the **Kubernetes & Helm Masterclass** tracks! This combined repository hosts all the production-grade manifests, microservice architectures, and custom packaging templates spanning our dual course offerings:

1. **Course 1: Kubernetes Core & Advanced Infrastructure** (Pods, Services, Storage, Cloud Scaling, and Auto-scaling)
2. **Course 2: Helm Package Management & Architecture** (Templating Engine, Local Repositories, and Umbrella Subcharts)

---

## 📊 Combined Course Metrics
* **Total Content Scope:** 25 Sections • 142 Lectures • ~5h 39m total runtime
* **Core Competency:** Orchestrate stateful/stateless applications locally or in the cloud, and bundle them into enterprise-grade reusable Helm charts.
* **Target Platforms:** Minikube, Multi-Node Cloud Infrastructure, ChartMuseum, and Helm 3+.

---

## 📂 Combined Repository Structure

```text
├── 01-k8s-fundamentals/     # Environment engine setup (Minikube), editor plugins, and YAML challenges
├── 02-workloads-compute/    # Native primitives: Pods, ReplicaSets, and state-managed Deployments
├── 03-advanced-pods/        # Multi-container patterns, Init Containers, Liveness/Readiness network probes
├── 04-networking-traffic/   # Service routing (ClusterIP/NodePort), Ingress controllers, LoadBalancers, and Namespaces
├── 05-storage-config/       # Persistent Volumes (PV), Claims (PVC), Storage Classes, and ConfigMaps
├── 06-cluster-operations/   # Pod scheduling mechanics: Node Affinity, Taints, Tolerations, and HPA/VPA autoscaling
├── 07-helm-fundamentals/    # Helm 3 baseline installation, Chart anatomy, and base configuration templates
├── 08-helm-templating/      # Go template structures, control flow (IF/ELSE), and dynamic multi-value mappings
├── 09-chart-museum/         # Standalone enterprise artifact registry setups, chart packaging, and version pinning
├── 10-umbrella-charts/      # Monorepo architecture patterns, nested dependencies, subchart values, and globals
└── challenges/              # Hands-on challenge blocks (Web rollouts, template rendering, and multi-tier subcharts)
```

---

## 🛠️ Getting Started

### Prerequisites
* A local machine capable of running **Minikube** or access to a cloud Kubernetes cluster
* Your preferred IDE (VS Code recommended with Kubernetes and YAML syntax extensions)
* Helm 3 CLI binary installed on your local path

### Quickstart Execution Sequence
```bash
# 1. Clone the combined cluster engineering codebase
git clone https://github.com

# 2. Fire up your local container orchestration sandbox
minikube start

# 3. Navigate into the core Helm templates directory
cd k8s-helm-masterclass/07-helm-fundamentals

# 4. Dry-run and debug the template assembly engine output
helm install course-release ./my-chart --dry-run --debug

# 5. Spin up the infrastructure live onto the cluster
helm install course-release ./my-chart
```

---

## 📘 Detailed Syllabus Breakdown

### ☸️ Course 1: Kubernetes Core & Advanced Infrastructure Engine
* **Foundational Primitives:** Moving past syntax checks into building atomic **Pods**, stabilizing state with **ReplicaSets**, and executing zero-downtime rolling upgrades using declarative **Deployments**.
* **Pod Design Patterns:** Bundling complex applications using **Multi-Container** architectures, preparing host paths with **Init Containers**, and mapping self-healing nodes via **Liveness and Readiness Probes**.
* **Cluster Traffic & Routing:** Building internal/external routing layers using **Services (LoadBalancers)** and managing advanced traffic routing via **Ingress Controllers** alongside network isolation using **Namespaces**.
* **Data Storage & Contexts:** Separating compute from state using **Persistent Volumes (PV)**, **Claims (PVC)**, and dynamic **Storage Classes**, while feeding target runtimes using custom **ConfigMaps**.
* **Day-2 Operations & Auto-scaling:** Live debugging containers through logs, using structural shortcuts to generate boilerplate YAML on the fly, and defining cluster scheduling constraints with **Node Affinity**, **Taints**, and **Tolerations**.
* **Elastic Resource Metrics:** Setting up cluster elasticity profiles to handle variable traffic spikes safely using **Horizontal Pod Autoscalers (HPA)** and **Vertical Pod Autoscalers (VPA)**.

### ⛵ Course 2: Helm Package Management & Architecture Deep-Dive
* **The Package Evolution:** Breaking down the architectural migration path from legacy Helm 2 systems into modern, secure, serverless **Helm 3** runtime tracking.
* **The Templating Blueprint:** Turning static manifest text blobs into highly reusable manifests. Using custom **Go Template expressions**, looping structures, comments, and defensive configuration evaluations using **IF/ELSE** blocks.
* **Diagnostic Toolkit:** Mastering rapid local chart validation using high-utility troubleshooting flags to inspect generated YAML text blocks before deployment.
* **Enterprise Registry Deployment:** Setting up, securing, and operating an enterprise-grade artifact tracking store using **ChartMuseum** to handle secure storage packaging, version-pinning adjustments, and remote package pushes.
* **Umbrella & Monorepo Scaling:** Grouping massive application layers using nested **Subcharts** while dynamically overriding configurations downstream using **Global Values** and managing explicit structural package logs via **Dependency Resolution Engines**.
