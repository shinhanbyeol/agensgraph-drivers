AgensGraph Drivers
==================

Welcome to the *AgensGraph Drivers* repository! This repository serves as the central hub for all officially supported and community-contributed drivers that enable applications to connect with [AgensGraph](https://github.com/skaiworldwide-oss/agensgraph), a multi-model database built on PostgreSQL with support for both relational and graph data.

# 📌 Why Drivers Matter
Database drivers are essential for application development — they act as the bridge between your code and the database, enabling applications to:
* Establish secure connections to the database
* Execute SQL and Cypher queries
* Retrieve and process data
* Handle transactions and errors efficiently

Without a driver, applications cannot communicate directly with a database. Drivers abstract the low-level communication protocol and provide a clean API tailored to your programming language.

# 🧠 AgensGraph Driver Support
AgensGraph is fully compatible with all standard PostgreSQL drivers, which means you can use any PostgreSQL client library to connect and run SQL queries.

However, these official AgensGraph drivers provide enhanced support for graph-specific features, including:

* Extended support for Cypher queries
* Graph result parsing and handling
* Graph-aware data types
* Integration with graph processing libraries and tools

If you're developing graph-centric applications using AgensGraph, these drivers will significantly improve your development experience and productivity.

Each subdirectory contains the source code, documentation, and usage examples for the corresponding language driver.

# ✅ Supported Languages

|Language |	Driver Name | Documentation |
|-------- |------------ |--------------- |
|Python |	agensgraph-python |	 [README](./python/README.md) |
|Java |	agensgraph-jdbc | [README](./jdbc/README.md) |
|Node.js |	agensgraph-js | [README](./nodejs/README.md) |
|Go |	agensgraph-go | [README](./golang/README.md) |
> 💡 PostgreSQL-compatible drivers work out-of-the-box with AgensGraph, but these enhanced drivers make graph development simpler and more powerful.

# 🛠 Getting Started

To get started with a specific driver, navigate to its subdirectory and follow the instructions in the README.md.

Example:
```
pip install agensgraph-python
```
You can also explore examples and usage guides in each subdirectory.


# 📚 Resources

* [AgensGraph Official Documentation](https://www.skaiworldwide.com/resource)
* [Cypher Query Language](https://opencypher.org/)
* [PostgreSQL Documentation](https://www.postgresql.org/docs/)

# 📄 License
This repository is licensed under the [Apache License 2.0](./python/LICENSE).

# 📬 Contact
Want to contribute a driver for another language? [Open an issue](https://github.com/skaiworldwide-oss/agensgraph-drivers/issues) or check our Contributing Guide!

