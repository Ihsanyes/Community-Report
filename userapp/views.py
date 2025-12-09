from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from .models import CustomUser, IssueReport
from .permission import login_required, admin_required

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")   # FIXED
        confirm_password = request.POST.get("password2")  # FIXED
        print(username)
        print(email)
        print(password)
        print(confirm_password)


        # Required fields check
        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required")
            return redirect("/signup/")

        # Password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("/signup/")

        # Username exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("/signup/")

        # Email exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("/signup/")

        # Create user
        user = CustomUser.objects.create_user(username=username, email=email)
        user.set_password(password)  # No validator issues
        user.save()

        messages.success(request, "Registration successful!")
        return redirect("/login/")

    return render(request, "userapp/signup.html")




def login_view(request):
    if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            print(username, password)
            if not username or not password:
                messages.error(request, "Both fields are required")
                return redirect("/login/")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
    return render(request, "userapp/login.html")


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('/login/')


def home(request):
    #oakgdpfokgaodkg
    return render(request, 'userapp/home.html')

@login_required
def report_issue(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')

        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        address = request.POST.get('address')
        contry = request.POST.get('contry')
        state = request.POST.get('state')
        city = request.POST.get('city')
        landmark = request.POST.get('landmark')

        status = request.POST.get('status')
        description = request.POST.get('description')
        # Additional fields can be captured similarly

        print(title)
        print(category)
        print(latitude)
        print(longitude)
        print(address)
        print(contry)
        print(state)
        print(city)
        print(landmark)
        print(status)
        print(description)

        if not title or not category or not description:
            messages.error(request, "Title, Category, and Description are required.")
            return redirect('/report-issue/')
            
        if not latitude or not longitude or not address or not contry or not state or not city or not landmark:
            messages.error(request, "Latitude and Longitude are required.")

        create, issue_report = IssueReport.objects.get_or_create(
            title=title,
            category=category,
            latitude=latitude,
            longitude=longitude,
            address=address,
            contry=contry,
            state=state,
            city=city,
            landmark=landmark,
            description=description,
            user=request.user
        )

        if create:
            messages.success(request, "Issue reported successfully!")
            return redirect('/issue-success/')




        
    return render(request, 'userapp/report_issue.html')

@login_required
@admin_required
def admin_dashboard(request):
    issues = IssueReport.objects.all()

    category = request.GET.get("category")
    status = request.GET.get("status")

    if category:
        issues = issues.filter(category=category)

    if status:
        issues = issues.filter(status=status)

    context = {
        "issues": issues,
        "total": IssueReport.objects.count(),
        "open_count": IssueReport.objects.filter(status="Open").count(),
        "in_progress": IssueReport.objects.filter(status="In Progress").count(),
        "closed": IssueReport.objects.filter(status="Closed").count(),
    }

    return render(request, 'userapp/admin_dashboard.html', context)


# ✅ ISSUE DETAIL PAGE
@login_required
@admin_required
def issue_detail(request, id):
    issue = get_object_or_404(IssueReport, id=id)

    return render(request, "userapp/issue_detail.html", {
        "issue": issue
    })

# ✅ STATUS UPDATE (ADMIN ONLY)
@login_required
@admin_required
def update_issue_status(request, id):
    if request.method == "POST":
        issue = get_object_or_404(IssueReport, id=id)
        new_status = request.POST.get("status")

        if new_status in ["Open", "In Progress", "Closed"]:
            issue.status = new_status
            issue.save()

        return redirect(f"/issue/{id}/")
    
def issue_success(request):
    return render(request, "userapp/issue_success.html")
