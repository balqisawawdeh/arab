from django.contrib import admin
from .models import (
    ContactSubmission,
    QuoteRequest,
    TeamMember,
    Testimonial,
    PortfolioCategory,
    Project,
    ProjectImage
)

# --- 1. Submissions ---

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('submitted_at',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'submitted_at')
    # Prevent editing/deleting submissions after viewing
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message', 'submitted_at')
        }),
    )
    def has_add_permission(self, request):
        return False # Users shouldn't add contact messages manually

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_needed', 'submitted_at')
    search_fields = ('name', 'email', 'service_needed', 'details')
    list_filter = ('service_needed', 'submitted_at')
    readonly_fields = ('name', 'email', 'phone', 'service_needed', 'details', 'submitted_at')
    def has_add_permission(self, request):
        return False


# --- 2. Company Content ---

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'linkedin_url')
    search_fields = ('name', 'position')
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_title', 'rating', 'is_approved')
    list_filter = ('is_approved', 'rating')
    search_fields = ('client_name', 'quote')


# --- 3. Portfolio ---

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # Auto-fill slug when typing name

class ProjectImageInline(admin.TabularInline):
    # Allows adding/editing images directly on the Project edit page
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'is_featured', 'completion_date')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'description', 'location')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline] # Include the images inline
    
# Since ProjectImage is managed via the Project Inline, we don't need to register it separately.