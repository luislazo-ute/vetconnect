def serializar(doc):
    """Convierte el _id de ObjectId a string para poder devolverlo como JSON."""
    if doc and '_id' in doc:
        doc['_id'] = str(doc['_id'])
    return doc
