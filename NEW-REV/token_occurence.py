from document_reference import DocumentReference


class TokenOccurence(DocumentReference):

    def __init__(self, DocumentReference, count):
        self.document_reference = DocumentReference
        self.count = count
