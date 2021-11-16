# How to run this Application

First go to the project folder

## 1. Creating the virtual environment

```bash
python -m venv venv
```

or

```bash
python3 -m venv venv
```

## 2. Activating the virtual environment

**on Linux:**
```bash
source venv/bin/activate
```

**on Windows:**
```bash
\env\Scripts\activate.bat
```

## 3. Installing the requirements

```bash
pip install -r requirements.txt
```

## 4. Running the Application

### 4.1 Setting environment variables


- **MAXIMUM\_CACHE_TIME:** maximum time in seconds that a cached query result is saved. By default the value is 300 seconds (5 minutes). 
- **MAX\_NUMBER:** max number of results returned on the `/temperature` endpoint. The default value is 5.  

**on Linux:**  

```bash
export CACHE_TTL={MAXIMUM_CACHE_TIME}
export DEFAULT_MAX_NUMBER={MAX_NUMBER}
```

**on Windows:**
```bash
set CACHE_TTL={MAXIMUM_CACHE_TIME}
set DEFAULT_MAX_NUMBER={MAX_NUMBER}
```

### 4.2 Starting the Application

**on Linux:**
```bash
sh run.sh
```

**on Windows:**
```bash
python app\endpoints.py
```

# Testing

**on Linux:**
```bash
sh test_run.sh
```

**on Windows:**
```bash
python -m pytest test
```

---

- [Architecture](./docs/architecture.md)

---

