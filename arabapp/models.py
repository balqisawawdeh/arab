from django.db import models
from django.utils import timezone

# ----------------------------------------------------------------------
# 1. Contact & Quote Submissions (for forms in views.py)
# ----------------------------------------------------------------------

class ContactSubmission(models.Model):
    """Stores data from the contact-us form."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-submitted_at']

    def __str__(self):
        return f"Message from {self.name} on {self.submitted_at.strftime('%Y-%m-%d')}"

class QuoteRequest(models.Model):
    """Stores data from the request-quote form."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    service_needed = models.CharField(max_length=255, help_text="e.g., Residential Construction, Infrastructure")
    details = models.TextField(verbose_name="Project Details")
    submitted_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Quote Request"
        verbose_name_plural = "Quote Requests"
        ordering = ['-submitted_at']

    def __str__(self):
        return f"Quote for {self.service_needed} by {self.name}"

# ----------------------------------------------------------------------
# 2. Company Content Models
# ----------------------------------------------------------------------

class TeamMember(models.Model):
    """Stores information about staff members for the teams page."""
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='teams/', blank=True, null=True)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)
    twitter_url = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.position}"

class Testimonial(models.Model):
    """Stores client testimonials for the testimonials page."""
    client_name = models.CharField(max_length=150)
    client_title = models.CharField(max_length=150, blank=True, null=True, help_text="e.g., CEO, Homeowner")
    quote = models.TextField()
    is_approved = models.BooleanField(default=False, help_text="Show on website if checked.")
    rating = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        default=5
    )
    date_given = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['-date_given']

    def __str__(self):
        return f"Testimonial from {self.client_name}"

# ----------------------------------------------------------------------
# 3. Portfolio Models (for portfolio views in views.py)
# ----------------------------------------------------------------------

class PortfolioCategory(models.Model):
    """Categories for organizing projects (e.g., Residential, Healthcare)."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Portfolio Category"
        verbose_name_plural = "Portfolio Categories"

    def __str__(self):
        return self.name

class Project(models.Model):
    """Stores individual project details."""
    title = models.CharField(max_length=255)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True)
    location = models.CharField(max_length=150, blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    main_image = models.ImageField(upload_to='portfolio/main/')
    
    # Matches the specific project views you had (e.g., healthcare-facility)
    is_featured = models.BooleanField(default=False) 

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-completion_date']

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    """Additional images for a project."""
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/details/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"Image for {self.project.title}"