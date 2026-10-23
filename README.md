## Design Decision

**Decision:** I used Django REST Framework's `ModelViewSet` and DefaultRouter instead of Function-Based Views (FBVs) to implement all the operations for my EventHub project.

**Why:** I chose this approach because `ModelViewSet` provides all the built-in CRUD operations with less repetitive code. It allows me to handle multiple HTTP methods under one roof, so I don't need to create separate functions for each method, as I would with Function-Based Views (FBVs). This saves both time and effort while keeping the code concise and efficient.
Additionally, `DefaultRouter` automatically generates URL patterns, making the API easier to maintain, reducing boilerplate code, and keeping the project organized.