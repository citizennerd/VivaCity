VivaCity
========

The platform for Civic Open Data Integration

Introduction
--------
In the last year there has been a lot of talking about the smart city concept. Big vendors have come to offer their solutions to the governance and the municipalities. But the main aspect that always remains in the corner is that you can install all the magic sensors in the world, but i'ts not going to bring a real solution. They cost a lot and they don't really solve problems.

What does is knowledge...

With a few friends we started analyzing open data and Linked Open Data.

The first approach has a very liquid structure if it has a structure at all, while the second approache has a very structured approach (too structured, some times). So we thought the real deal was in the middle: A de-structured approach with some structural functionalities.

But what the real issue were the instruments.

Socrata in the USA has created the city portal for the open data, but every information is given separately. Not even the LOD approach connects the info. And the instuments offered by the Big Vendors are incredibly UGLY!!!

The only way to interact with local data is through a map.

What was a thing that enabled users to feel empathy with the city itself? It was a Game: SimCity

As the Sim City developer blog states, the first versions of SC were basically only enormous data-visualization tools with simulated data generated all the time.

Vivacity
--------
So here comes VivaCity: A sim-city-esque interface for a complex data-model that fetches more or less real-time data from the remote data-providers and enables the user to "live" the data.

Vivacity is composed of three main parts:

- PostDoc, the model manager
- Semanticizer, the semantics engine
- VivaCity itself, the user interface

### PostDoc

PostDoc represents a meta-model engine for postgres. Optimizations are obviously due and will be made, but the ideal would obviously be using a nosql database, at least for the instances.

### Semanticizer

Semanticizer is the connector to the outer world. It enables a semantic translation between various types of files (at the moment csv and anything readable by OGR and then zipped) and the model described by PostDoc. Sometimes a translation needs more than just a renaming of columns. For that reason there is a small transformation language which enables the modification of a single value.

If the data is very de-structured, it could be necessary to connect the core of the information with elements that are a few logic steps away. For this reason it is possible to define semantic paths to create simple "model graphs" that the importer will respect and recreate in the system

### VivaCity

Vivacity takes the SimCity experience on simulated worlds and brings the best of it to be used in a new open-data based approach. Every information is explorable, everything can be drilled-down/drilled-across.

Oh, and because I want the project to live long, prosper and to be used and evolved, you are welcome to Fork it and add new data-providers or new visualization methods or anything!!! Or new importable datasets or expand the model...
VivaCity is a product by Marco Montanari