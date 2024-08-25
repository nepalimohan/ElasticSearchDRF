from django.core.management.base import BaseCommand
from quotation.models import SalesQuotation
import faker

class Command(BaseCommand):
    help = 'Insert 100 books into the database'

    def handle(self, *args, **kwargs):
        fake = faker.Faker()

        quotations = []
        for _ in range(1000000):
            book = SalesQuotation(
                title=fake.sentence(nb_words=5),
                quotation_number=fake.numerify(),
                quotation_date=fake.date(),
                valid_till=fake.date(),
                narration=fake.text()
            )
            quotations.append(book)
        
        SalesQuotation.objects.bulk_create(quotations)
        self.stdout.write(self.style.SUCCESS('Successfully inserted 100000 quotations'))