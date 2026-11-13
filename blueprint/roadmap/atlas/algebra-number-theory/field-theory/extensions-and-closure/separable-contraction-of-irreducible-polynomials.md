---
declaration: section
origin: cited
lean: Polynomial.exists_irreducible_separable_expand_eq, Polynomial.unique_irreducible_separable_expand_eq, Polynomial.exists_unique_irreducible_separable_expand_eq
statement: formalized
proof: formalized
---

# Separable contraction of irreducible polynomials

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-contraction-of-irreducible-polynomials/index.html).

## Irreducible polynomials are expansions of separable irreducibles

Let $K$ be a field
of characteristic $p$ (with $p = 0$ in characteristic zero) and let $f \in K[x]$ be irreducible.
Then there exist $n \in \mathbb{N}$ and an irreducible separable polynomial $g \in K[x]$ such
that $f(x) = g(x^{p^n})$, where $0^0 = 1$.

## Sources

- ATLAS NumberTheoryI, Corollary 4.5 (existence).

Formalized by `Polynomial.exists_irreducible_separable_expand_eq`, a theorem declared in [MathlibExt/Algebra/Polynomial/SeparableExpand.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/SeparableExpand.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-contraction-of-irreducible-polynomials/index.html#exists-irreducible-separable-expand-eq).

## The separable irreducible underlying an irreducible polynomial is unique

Let $K$ be a
field of characteristic $p$ (with $p = 0$ in characteristic zero) and let $f \in K[x]$ be
irreducible. If $n_1, n_2 \in \mathbb{N}$ and irreducible separable polynomials
$g_1, g_2 \in K[x]$ satisfy $f(x) = g_1(x^{p^{n_1}})$ and $f(x) = g_2(x^{p^{n_2}})$, where
$0^0 = 1$, then $n_1 = n_2$ and $g_1 = g_2$.

## Sources

- ATLAS NumberTheoryI, Corollary 4.5 (uniqueness).

Formalized by `Polynomial.unique_irreducible_separable_expand_eq`, a theorem declared in [MathlibExt/Algebra/Polynomial/SeparableExpand.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/SeparableExpand.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-contraction-of-irreducible-polynomials/index.html#unique-irreducible-separable-expand-eq).

## Irreducible polynomials are uniquely expansions of separable irreducibles

Let $K$ be a
field of characteristic $p$ (with $p = 0$ in characteristic zero, and $0^0 = 1$) and let
$f \in K[x]$ be irreducible. Then there exist $n \in \mathbb{N}$ and an
irreducible separable polynomial $g \in K[x]$ with $f(x) = g(x^{p^n})$, and for every
$n' \in \mathbb{N}$ and every irreducible separable polynomial $g' \in K[x]$ with
$f(x) = g'(x^{p^{n'}})$ we have $n' = n$ and $g' = g$.

## Sources

- ATLAS NumberTheoryI, Corollary 4.5.

Formalized by `Polynomial.exists_unique_irreducible_separable_expand_eq`, a theorem declared in [MathlibExt/Algebra/Polynomial/SeparableExpand.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/SeparableExpand.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-contraction-of-irreducible-polynomials/index.html#exists-unique-irreducible-separable-expa).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Separable contraction of irreducible polynomials](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-contraction-of-irreducible-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/FieldTheory/extensions-and-closure/separable-contraction-of-irreducible-polynomials)
