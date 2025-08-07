# Test Plan for JSONPlaceholder API

## Objective
To validate the functionality, reliability, and correctness of the public API: [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts) using Python and Pytest.

## Scope
The scope includes testing the following endpoints:
- `GET /posts`
- `GET /posts/{id}`
- `POST /posts`
- `PUT /posts/{id}`
- `PATCH /posts/{id}`
- `DELETE /posts/{id}`

## Test Approach
We will use:
- **Python** as the scripting language
- **Pytest** as the testing framework
- **Requests** library for HTTP requests
- Tests will be grouped by method and endpoint

## Test Types
- **Positive tests**: Validate successful responses with valid inputs
- **Negative tests**: Verify the API handles invalid inputs gracefully (e.g., invalid IDs)
- **Data validation tests**: Ensure fields like `userId`, `id`, `title`, and `body` are correct

## Test Cases (High-Level)
### GET /posts
- Verify status code is 200
- Verify response is a list of 100 posts
- Verify each post has fields: `userId`, `id`, `title`, `body`
- Verify specific post by ID

### POST /posts
- Create a new post
- Validate response code is 201
- Verify response contains posted data

### PUT /posts/{id}
- Replace post by ID
- Validate full update is applied
- Check status code 200

### PATCH /posts/{id}
- Partially update post
- Validate only specified fields are updated
- Check status code 200

### DELETE /posts/{id}
- Delete post by ID
- Verify status code is 200 or 204
- Confirm resource is no longer accessible

### Negative Tests
- GET, PUT, PATCH, DELETE with invalid or non-existent IDs (e.g., `/posts/9999`)
- POST with missing required fields

### Tools
- Python 3.x
- Pytest
- Requests
- All dependencies listed in requirements.txt

### Deliverables
- Test code for all CRUD operations
- One negative test per method
- Setup and run instructions in README.md

### Risks
- The API is a public dummy API; changes are not persisted.
- DELETE, PUT, and POST may appear successful but not affect data.

### Entry Conditions
These are the prerequisites that must be met before test execution begins:
- API endpoint https://jsonplaceholder.typicode.com/posts is accessible.
- Test environment is set up with:
- Python 3.x installed
- Required packages installed (requests, pytest)
- All test data and configurations are prepared (e.g., sample JSON payloads).
- Internet connection is stable (since this is a public API).
- Test scripts are written and placed correctly under the tests/ folder.
- The team has access to the test plan and understands the objective.

### Exit Conditions
These are the conditions that signify testing is complete:
- All planned test cases have been executed (both positive and negative).
- All critical and major bugs (if any) have been identified, documented, and communicated.
- All test scripts pass without failure (or known issues are accepted by stakeholders).
- Test report is generated and shared.
- Test summary and results are documented in the final report or README.



### References
- https://jsonplaceholder.typicode.com/guide/
