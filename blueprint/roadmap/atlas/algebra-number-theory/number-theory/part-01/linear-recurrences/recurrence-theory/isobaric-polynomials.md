---
declaration: section
origin: cited
lean: MetaMathlibExt.isobaricWeight, MetaMathlibExt.IsIsobaric
statement: formalized
proof: formalized
---

# Isobaric polynomials

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/isobaric-polynomials/index.html).

## Isobaric weight of an exponent vector

For a natural number $k$ and an exponent vector
$\alpha = (\alpha_1, \dots, \alpha_k) \in \mathbb{N}^k$, the isobaric weight of $\alpha$ is
$\sum_{j=1}^k j \alpha_j$.

The source's condition on the monomials of an isobaric polynomial of degree $n$ is that this
weight equals $n$.

Formalized by `MetaMathlibExt.isobaricWeight`, an abbreviation declared in [MathlibExt/NumberTheory/IsobaricPolynomial.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IsobaricPolynomial.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/isobaric-polynomials/index.html#isobaric-weight).

## Isobaric polynomial

Let $k$ and $n$ be natural numbers. A polynomial
$P \in \mathbb{Z}[t_1, \dots, t_k]$ is isobaric of degree $n$ if every monomial
$t_1^{\alpha_1} \cdots t_k^{\alpha_k}$ occurring in $P$ with nonzero coefficient satisfies
$\sum_{j=1}^k j \alpha_j = n$; that is, $P$ is weighted homogeneous of degree $n$ when the
variable $t_j$ has weight $j$. In particular, the zero polynomial is isobaric of every degree.

Formalized by `MetaMathlibExt.IsIsobaric`, an abbreviation declared in [MathlibExt/NumberTheory/IsobaricPolynomial.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/IsobaricPolynomial.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/isobaric-polynomials/index.html#is-isobaric).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Isobaric polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/isobaric-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/recurrence-theory/isobaric-polynomials)
