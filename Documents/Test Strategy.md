# Test Strategy – JSONPlaceholder API

## 1. Objective
Define a structured approach to test the JSONPlaceholder REST API endpoints (`/posts`). Ensure the API behaves as expected for CRUD operations (GET, POST, PUT, PATCH, DELETE), including validation, response structure, status codes, and data integrity.

## 2.  Scope
- **In Scope**:
  - Testing `/posts` endpoint with methods: GET, POST, PUT, PATCH, DELETE
  - Verifying response status codes, headers, and payloads
  - Positive and negative testing
  - Data-driven testing using external JSON (e.g., `expected_posts.json`)

- **Out of Scope**:
  - Performance or load testing
  - Security, authentication/authorization (since the API is mock/public)

## 3. Testing Approach

| Method | Action | Validation |
|--------|--------|------------|
| **GET**    | `/posts`, `/posts/{id}` | 200 OK, JSON schema, content match |
| **POST**   | `/posts` | 201 Created, verify posted data |
| **PUT**    | `/posts/{id}` | 200 OK, updated resource returned |
| **PATCH**  | `/posts/{id}` | 200 OK, partial update applied |
| **DELETE** | `/posts/{id}` | 200 OK / 204 No Content |

## 4. Test Tools
- **Language**: Python 3.x
- **Framework**: Pytest
- **HTTP Client**: Requests
- **Reporting**: pytest-html
- **Test Data**: `expected_posts.json`

## 5. Test Artifacts
- `testplan.md`: High-level test planning
- `teststrategy.md`: This document
- `response.json`: Sample test data
- `test_api.py`: Test implementation
- `pytest.ini`: Test config
- `report.html`: Execution report (optional)

## 6. Test Types

- ✅ Functional Testing
- ✅ Positive and Negative Testing
- ✅ Boundary Value Testing
- ✅ Data-Driven Testing (using `expected_posts.json`)
- ✅ Status Code & Header Validation
- ❌ No Auth, Performance, or Security testing

## 7. Test Data Strategy
- **Static JSON File**: `expected_posts.json` will act as the source of expected titles and bodies for GET requests.
- **Dynamic Data Creation**: POST/PUT/PATCH tests will use test payloads and verify the response structure.

## 8. Risks
- The public API is a fake/mock service and doesn't persist data. Tests should not assume actual DB changes.
- Rate limits or temporary outages may affect test consistency.

## 9. Schedule

| Activity             | Duration |
|----------------------|----------|
| Test Plan & Strategy | 1 Day    |
| Test Script Dev      | 3 Days   |
| Execution            | 2 Day    |
| Reporting            | 2 Day    |

## 10. Entry & Exit Criteria

**Entry:**
- API is reachable and stable
- Test environment ready (Python, packages, network access)
- Test cases reviewed

**Exit:**
- All test cases executed
- All critical bugs reported
- Reports shared