from django.http import HttpResponse

def whoami_view(request):
    return HttpResponse("""
    <html>
    <body>
        <div class="content">
            <h2>台北商業大學</h2>
            <h3>五專資管科</h3>
            <p>11256023</p>
            <p>簡聿喬</p>
        </div>
    </body>
    </html>
    """)
