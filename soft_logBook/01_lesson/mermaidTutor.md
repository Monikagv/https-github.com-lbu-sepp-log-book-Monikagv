
## Syntax Structure

One would notice that all Diagrams definitions begin with a declaration of the diagram type, followed by the definitions
of the diagram and its contents. This declaration notifies the parser which kind of diagram the code is supposed to generate.

Example : The code below is for an Entity Relationship Diagram, specified by the erDiagram declaration. What follows is
the definition of the different Entities represented in it.

erDiagram

          CUSTOMER }|..|{ DELIVERY-ADDRESS : has
          CUSTOMER ||--o{ ORDER : places
          CUSTOMER ||--o{ INVOICE : "liable for"
          DELIVERY-ADDRESS ||--o{ ORDER : receives
          INVOICE ||--|{ ORDER : covers
          ORDER ||--|{ ORDER-ITEM : includes
          PRODUCT-CATEGORY ||--|{ PRODUCT : contains
          PRODUCT ||--o{ ORDER-ITEM : "ordered in"



Bibliograpy:
mermaid.js.org. (n.d.). Diagram Syntax | Mermaid. [online] Available at: https://mermaid.js.org/intro/syntax-reference.html.

‌