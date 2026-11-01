# AIMS-mini Use Case Diagram

## Actor
- User: người sử dụng ứng dụng AIMS-mini.

## Use Cases
- Add DVD to cart
- Remove DVD from cart
- View cart
- Calculate total cost
- Search DVD by title

## Diagram

```mermaid
flowchart LR
    U[User] --> A([Add DVD to cart])
    U --> B([Remove DVD from cart])
    U --> C([View cart])
    U --> D([Calculate total cost])
    U --> E([Search DVD by title])
```