import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase
cred = credentials.Certificate('firebase/firebase-service-account.json')
firebase_admin.initialize_app(cred)

# Access Firestore
db = firestore.client()

# Authenticate and download data from a collection
def get_data_from_collection(collection_name):
    collection_ref = db.collection(collection_name)
    docs = collection_ref.stream()

    data = {}
    for doc in docs:
        doc_data = doc.to_dict()
        data[doc.id] = doc_data

    return data

# Replace 'your_collection_name' with the name of the collection you want to access
courses = get_data_from_collection('courses')
lessons = get_data_from_collection('lessons')
pages = get_data_from_collection('pages')

def get_data_from_reference(doc_ref):
    doc = doc_ref.get()
    if doc.exists:
        doc_data = doc.to_dict()
        doc_data['id'] = doc.id
        return doc_data
    else:
        print('No such document!')
        return None

def get_data_from_path(doc_path):
    doc_ref = db.document(doc_path)
    doc = doc_ref.get()
    if doc.exists:
        doc_data = doc.to_dict()
        doc_data['id'] = doc.id
        return doc_data
    else:
        print('No such document!')
        return None


def get_tasks():
    tasks = []

    for course in courses:
        lessons = courses[course]['lessons']

        for lesson in lessons:
            _lesson_data = get_data_from_reference(lesson)
            thumbnail = _lesson_data['thumbnail']
            title = _lesson_data['title']

            for page in pages:
                _page_data = get_data_from_path('pages/' + page)
                _page_data = _page_data['page']
                if "type" in _page_data:
                    if _page_data['type'] == 'build_sentence':
                        sentence = _page_data['data']
                        tasks.append(
                            {
                                "illustration": thumbnail,
                                "title": title,
                                "sentence": sentence,
                                "type": "build_sentence"
                            }
                        )
                    elif _page_data['type'] == 'selection_text':
                        correct_answer = _page_data['answer']
                        questions = _page_data['question']
                        options = _page_data['questions']

                        tasks.append(
                            {
                                "illustration": thumbnail,
                                "title": title,
                                "question": questions,
                                "options": options,
                                "answer": correct_answer,  # zero indexed
                                "type": "selection_text"
                            }
                        )
                    else :
                        print(_page_data)

    return tasks