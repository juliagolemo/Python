from typing import Any

database_api = {
    1: ["lew", "tygrys", "słoń", "żółw", "koala"],
    2: ["wilk", "lis", "zając", "jelen", "niedźwiedź"],
    3: ["orzeł", "sokół", "kruk", "papuga", "pingwin"],
    4: ["pies", "kot", "świnka morska", "chomik", "papuga"],
    5: ["delfin", "rekin", "ośmiornica", "meduza", "krewetka"]
}

def get_request_api(batch_id: int) -> dict[str, Any]:
    batch = database_api.get(batch_id)
    next_batch_id = batch_id + 1 if batch_id + 1 in database_api.keys() else None
    return {
        'batch': batch,
        'next': next_batch_id
    }

def fetch_all_animals() -> list[str]:
    all_animals = []
    batch_id = 1

    while batch_id is not None:
        data = get_request_api(batch_id)
        all_animals.extend(data['batch'])
        batch_id = data['next']

    return all_animals

if __name__ == '__main__':
    animals = fetch_all_animals()
    print("Pełna lista zwierząt:", animals)
