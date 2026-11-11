# 🧱 Object-Oriented Programming in Python — for ML Engineering

A hands-on study of OOP in Python, applied to the building blocks of a machine learning workflow: datasets, configs, data cleaners, models, and pipelines.

## 📚 Core concepts

| File | Concept |
|---|---|
| [`1_encapsulation.py`](1_encapsulation.py) | Encapsulation and private attributes |
| [`2_abstraction.py`](2_abstraction.py) | Abstraction with abstract base classes |
| [`3_inheritance.py`](3_inheritance.py) | Inheritance and method overriding |
| [`4_polymorphism.py`](4_polymorphism.py) | Polymorphism and duck typing |
| [`bank_account.py`](bank_account.py) | Mini project: a bank account class |

## 🗓️ Daily progression

| Day | Topic |
|---|---|
| [Day 01](DAY%2001) | `Dataset` class: modeling data as objects |
| [Day 02](DAY%2002) | `Config` class: centralizing settings |
| [Day 03](DAY%2003) | `DataCleaner`: encapsulated preprocessing |
| [Day 04](DAY%2004) | `BaseModel`: abstraction and inheritance for models |
| [Day 05](DAY%2005) | Composition over inheritance |
| [Day 06](DAY%2006) | **Capstone:** a modular ML pipeline with interchangeable models |

## ▶️ Run the capstone

```bash
cd "DAY 06"
python main.py
```

`Pipeline` takes any model that implements the `BaseModel` interface, so you can swap models without changing pipeline code.
