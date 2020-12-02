from django.db import models

# Create your models here.
from django.db import models
from phone_field import PhoneField
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Presentation(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Presentation")
        verbose_name_plural = ("Presentations")

    def __str__(self):
        return self.title


class SiteInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    map_url = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("siteinfo")
        verbose_name_plural = ("siteinfos")

    def __str__(self):
        return self.name


class About(models.Model):
    image = models.ImageField(upload_to="images/about")
    description = models.TextField()
    title = models.CharField(max_length=250)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("about")
        verbose_name_plural = ("abouts")

    def __str__(self):
        return self.title


class Contact(models.Model):

    address = models.CharField(max_length=50)
    phone = PhoneField()
    email = models.EmailField(max_length=254)
    website = models.CharField(max_length=50)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.website


class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("ContactForm")
        verbose_name_plural = ("ContactForms")

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    description = models.TextField(default="Veuillez enregistrer votre email pour ne rein rater ")
    email = models.EmailField(max_length=254)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Newsletter")
        verbose_name_plural = ("Newsletters")

    def __str__(self):
        return self.email


class Team(models.Model):
    image = models.ImageField(upload_to="team/",)
    name = models.CharField(max_length=150)
    job = models.CharField(max_length=50)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    image = models.ImageField(upload_to="porfolio/")
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="portfolio_cat")
    slug = models.SlugField(null=True, blank=True)
    link = models.TextField(blank=True, null=True)
    description = models.TextField(default="Portfolio test blah blah blah my portfolio test")

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        self.link = self.get_absolute_url()
        return super(Portfolio, self).save()
    def get_absolute_url(self):
        return reverse("portfolio_details", kwargs={"slug": self.slug})
    


class Service(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


class Hero(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("hero")
        verbose_name_plural = ("heros")

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="clients")

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")

    def __str__(self):
        return self.name


class Feature(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    image = models.ImageField(upload_to="feature")

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Feature")
        verbose_name_plural = ("Features")

    def __str__(self):
        return self.title


class Cta(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Cta")
        verbose_name_plural = ("Ctas")

    def __str__(self):
        return self.title


class Count(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="count/")
    happy_clients = models.IntegerField(default=0)
    happy_icon = models.CharField(max_length=50)
    happy_text = models.TextField()
    projects = models.IntegerField(default=0)
    projects_icon = models.CharField(max_length=50)
    projects_text = models.TextField()
    years = models.IntegerField(default=0)
    years_icon = models.CharField(max_length=50)
    years_text = models.TextField()
    awards = models.IntegerField(default=0)
    awards_icon = models.CharField(max_length=50)
    awards_text = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Count")
        verbose_name_plural = ("Counts")

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonial/")
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    message = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Testimonial")
        verbose_name_plural = ("Testimonials")

    def __str__(self):
        return self.name
