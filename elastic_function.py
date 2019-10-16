from elasic_client import Session

se = Session()

def update_to_elastic(id, sentimentality):
    response = se.update(id, sentimentality)
    print(response["_shards"])

update_to_elastic("Fk_60G0BMDBbXu8z4S65", "positive")