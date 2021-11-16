# How to run this Application

## 1. Activating the virtual enviroment

**on Linux:**
```bash
source venv/bin/activate
```

**on Windows:**
```bash
\env\Scripts\activate.bat
```

## 2. Installing the requirements

```bash
pip install -r requirements.txt
```

## 3. Running the Application

### 3.1 Setting environment variables


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

### 3.2 Starting the Application

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

