# 📌 **Projeto Django CRUD**

Este é um projeto simples de CRUD (Create, Read, Update, Delete) desenvolvido com **Django**.
Com fins de aprendizado da tecnologia.

---

## 🚀 **Como Rodar o Projeto**

Siga os passos abaixo para configurar e executar o projeto localmente:

---

### **1. Clone o repositório**

```bash
git clone (https://github.com/olimontes/django-basic-crud.git)
cd <pasta-do-repositorio>
```

---

### **2. Crie um ambiente virtual**

```bash
python -m venv venv
```

---

### **3. Ative o ambiente virtual**

#### Windows:

```bash
venv\Scripts\activate
```

#### Linux/macOS:

```bash
source venv/bin/activate
```

---

### **4. Instale as dependências**

```bash
pip install -r requirements.txt
```

---

### **5. Execute as migrações**

```bash
python manage.py migrate
```

---

### **6. Inicie o servidor de desenvolvimento**

```bash
python manage.py runserver
```

---

## 🌐 **Acessando a Aplicação**

Com o servidor rodando, abra seu navegador e acesse:

```
http://127.0.0.1:8000/tarefas/
```

A rota **/tarefas** é onde está o formulário e onde todas as operações do CRUD podem ser realizadas.

---

## 🛠 **Tecnologias Utilizadas**

* Python
* Django
* SQLite (padrão)
* HTML + Templates Django

---

## 📄 **Licença**

Este projeto é open-source e pode ser utilizado livremente para estudos e fins educacionais.

---
