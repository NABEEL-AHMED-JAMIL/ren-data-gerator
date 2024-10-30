import random
from faker import Faker
import string

fake = Faker(use_weighting=False)

# random string
def random_string(len=15):
    lst = [random.choice(string.hexdigits) for n in range(len)]
    return "".join(lst)

def number():
    return random.randrange(-1000, 1000)

def small_positive_integer():
    return random.randrange(1, 100)

def positive_integer():
    return random.randrange(1, 1000)

def number_employees():
    return random.randrange(1, 10000)

def long_text():
    return fake.paragraph(nb_sentences=1)

def product_name():
    return fake.text(max_nb_chars=30)

def full_name():
    return "{} {}".format(fake.first_name(), fake.last_name())

def sex():
    return random.choice(["Male", "Female"])

def department():
    # https://www.quora.com/What-are-the-main-departments-in-a-company
    return random.choice(["Marketing & Proposals Department", "sales Department",
        "Project Department", "Designing Department", "Production Department", "Maintenance Department",
        "Store Department", "Procurement Department", "Quality Department", "Inspection department",
        "Packaging Department", "Finance Department", "Dispatch Department", "Account Department",
        "Research & Development Department", "Information Technology Department",
        "Human Resource Department", "Security Department", "Administration department"
    ])

def industry():
    # https://gist.github.com/mbejda/19012b99a12e9d014389
    return random.choice(["Accounting", "Airlines / Aviation",
        "Alternative Dispute Resolution", "Alternative Medicine",
        "Animation", "Apparel / Fashion", "Architecture / Planning",
        "Arts / Crafts", "Automotive", "Aviation / Aerospace",
        "Banking / Mortgage", "Biotechnology / Greentech", "Broadcast Media",
        "Building Materials", "Business Supplies / Equipment",
        "Capital Markets / Hedge Fund / Private Equity",
        "Chemicals", "Civic / Social Organization",
        "Civil Engineering", "Commercial Real Estate",
        "Computer Games", "Computer Hardware",
        "Computer Networking", "Computer Software / Engineering",
        "Computer / Network Security", "Construction",
        "Consumer Electronics", "Consumer Goods",
        "Consumer Services", "Cosmetics",
        "Dairy", "Defense / Space", "Design",
        "E - Learning", "Education Management"])

TYPES_TO_GENERATORS = {
    'id': random_string,
    'first_name': fake.first_name,
    'last_name': fake.last_name,
    'full_name': full_name,  # fake.name,
    'company': fake.company,
    'industry': industry,
    'business_department': department,
    'company_desc': fake.catch_phrase,
    'company_number_employees': number_employees,
    'city': fake.city,
    'country': fake.country,
    'sex': sex,
    'ean': fake.ean,
    'url': fake.url,
    'email': fake.email,
    'business_email': fake.company_email,
    'website': fake.url,
    'job': fake.job,
    'number': number,
    'small_positive_integer': small_positive_integer,
    'positive_integer': positive_integer,
    'product_name': product_name,
    'date': fake.date,
    'year': fake.year,
    'datetime': fake.date_time,
    'date_this_decade': fake.date_this_decade,
    'date_of_birth': fake.date_of_birth,
    'long_text': long_text,
    'address': fake.address,
    'phone': fake.phone_number
}