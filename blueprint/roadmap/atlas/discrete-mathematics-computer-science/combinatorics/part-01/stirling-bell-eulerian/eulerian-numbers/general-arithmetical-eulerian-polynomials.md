---
declaration: section
origin: cited
lean: MetaMathlibExt.generalArithmeticalEulerianNumber, MetaMathlibExt.generalArithmeticalEulerianPolynomial
statement: formalized
proof: formalized
---

# General arithmetical Eulerian polynomials

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/general-arithmetical-eulerian-polynomials/index.html).

## General arithmetical Eulerian number

Let $R$ be a ring, let $n$ and $k$ be natural
numbers, and let $a, d \in R$. The general arithmetical Eulerian number $A_{n,k}(a,d) \in R$ is

$$A_{n,k}(a,d) = \sum_{i=0}^{k} (-1)^i \binom{n+1}{i} \bigl((k+1-i)\,d - a\bigr)^n.$$

Formalized by `MetaMathlibExt.generalArithmeticalEulerianNumber`, a definition declared in [MathlibExt/NumberTheory/GeneralArithmeticalEulerianPolynomial.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralArithmeticalEulerianPolynomial.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/general-arithmetical-eulerian-polynomials/index.html#general-arithmetical-eulerian-number).

## General arithmetical Eulerian polynomial

Let $R$ be a ring, let $n$ be a natural number,
and let $a, d \in R$. For each natural number $k$, write $A_{n,k}(a,d) \in R$ for the general
arithmetical Eulerian number. The general arithmetical Eulerian polynomial is the polynomial
in the indeterminate $t$

$$P_n(t;a,d) = \sum_{k=0}^{n} A_{n,k}(a,d)\, t^k \in R[t].$$

Formalized by `MetaMathlibExt.generalArithmeticalEulerianPolynomial`, a definition declared in [MathlibExt/NumberTheory/GeneralArithmeticalEulerianPolynomial.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralArithmeticalEulerianPolynomial.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/general-arithmetical-eulerian-polynomials/index.html#general-arithmetical-eulerian-polynomial).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: General arithmetical Eulerian polynomials](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/general-arithmetical-eulerian-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/general-arithmetical-eulerian-polynomials)
