---
declaration: section
origin: cited
lean: MathlibExt.FieldTheory.ComplexPartialFractionsWanted.ratFunc_partial_fractions_complex, MathlibExt.FieldTheory.RealPartialFractionsWanted.ratFunc_partial_fractions_real
statement: formalized
---

# Partial fraction decomposition

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/partial-fraction-decomposition/index.html).

## Partial fraction decomposition over $\mathbb{C}$

For every complex rational function
$f \in \mathbb{C}(X)$ there exist a polynomial $q \in \mathbb{C}[X]$, a finite set $S$ of monic
polynomials of degree $1$ in $\mathbb{C}[X]$, and, for each $p \in S$, a natural number $m_p$
and polynomials $g_{p,k} \in \mathbb{C}[X]$ for $k < m_p$, each of degree less than the degree
of $p$, such that, in $\mathbb{C}(X)$,

$$f = q + \sum_{p \in S} \sum_{k=0}^{m_p - 1} \frac{g_{p,k}}{p^{k+1}}.$$

Only existence is stated: the standard uniqueness of the decomposition (support and
multiplicities fixed by the denominator's irreducible factors) is not, so a witness may include
polynomials $p \in S$ with $m_p = 0$ or zero numerators $g_{p,k}$.

## Sources

- S. Lang, Algebra, rev. 3rd ed., Springer, 2002, Ch. IV, §5 (Partial fractions), p. 187; https://en.wikipedia.org/wiki/Partial_fraction_decomposition#Statement

Stated but not proved: `MathlibExt.FieldTheory.ComplexPartialFractionsWanted.ratFunc_partial_fractions_complex` is written with `theorem_wanted` in [WantedExt/FieldTheory/ComplexPartialFractionsWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/FieldTheory/ComplexPartialFractionsWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/partial-fraction-decomposition/index.html#rat-func-partial-fractions-complex).

## Partial fraction decomposition over $\mathbb{R}$

For every real rational function
$f \in \mathbb{R}(X)$ there exist a polynomial $q \in \mathbb{R}[X]$, a finite set $S$ of monic
polynomials in $\mathbb{R}[X]$, each of degree $1$ or irreducible of degree $2$, and, for each
$p \in S$, a natural number $m_p$ and polynomials $g_{p,k} \in \mathbb{R}[X]$ for $k < m_p$, each
of degree less than the degree of $p$, such that, in $\mathbb{R}(X)$,

$$f = q + \sum_{p \in S} \sum_{k=0}^{m_p - 1} \frac{g_{p,k}}{p^{k+1}}.$$

Only existence is stated: the standard uniqueness of the decomposition (support and
multiplicities fixed by the denominator's irreducible factors) is not, so a witness may include
polynomials $p \in S$ with $m_p = 0$ or zero numerators $g_{p,k}$.

## Sources

- S. Lang, Algebra, rev. 3rd ed., Springer, 2002, Ch. IV, §5 (Partial fractions), p. 187; https://en.wikipedia.org/wiki/Partial_fraction_decomposition#General_result

Stated but not proved: `MathlibExt.FieldTheory.RealPartialFractionsWanted.ratFunc_partial_fractions_real` is written with `theorem_wanted` in [WantedExt/FieldTheory/RealPartialFractionsWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/FieldTheory/RealPartialFractionsWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/partial-fraction-decomposition/index.html#rat-func-partial-fractions-real).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partial fraction decomposition](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/partial-fraction-decomposition/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/polynomials/partial-fraction-decomposition)
