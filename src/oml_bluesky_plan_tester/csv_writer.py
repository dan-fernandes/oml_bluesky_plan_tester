from typing import cast

from event_model.documents import DocumentType, Event, EventDescriptor


def make_csv(docs: list[DocumentType]) -> str:
    """
    Takes a list of RunEngine output docs and converts to CSV format

    Args:
        docs: A list of RunEngine docs

    Returms:
        A string of given list's csv equivalent
    """
    csv_dict = {}
    headers = []

    for doc in docs:
        if type(doc) is EventDescriptor:
            doc = cast(EventDescriptor, doc)
            headers = list(doc.get("data_keys"))
            headers.sort()
            for header in headers:
                csv_dict[header] = []

        elif type(doc) is Event:
            doc = cast(Event, doc)
            for header in doc["data"]:
                csv_dict[header].append(str(doc["data"][header]))

    csv_str = ",".join(headers) + "\n"

    csv_str += "\n".join(
        [
            ",".join(row)
            for row in zip(*[csv_dict[header] for header in headers], strict=False)
        ]
    )

    # return csv_str
    return csv_str
