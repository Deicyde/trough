---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.OeisA002897Wanted.a, MathlibExt.NumberTheory.OeisA002897Wanted.Vars, MathlibExt.NumberTheory.OeisA002897Wanted.xyzPowN, MathlibExt.NumberTheory.OeisA002897Wanted.pPoly, MathlibExt.NumberTheory.OeisA002897Wanted.a_eq_coeff, MathlibExt.NumberTheory.OeisA002897Wanted.a_eq_coeff_holds
statement: formalized
---

# Cubed central binomial coefficients

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/cubed-central-binomial-coefficients/index.html).

## Cubed central binomial coefficients

For a natural number $n$, $a(n) = \binom{2n}{n}^3$.

Formalized by `MathlibExt.NumberTheory.OeisA002897Wanted.a`, a definition declared in [WantedExt/NumberTheory/OeisA002897Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisA002897Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/cubed-central-binomial-coefficients/index.html#a).

## Indices for three variables

Three polynomial variables are indexed by the set
$\{0, 1, 2\}$.

Formalized by `MathlibExt.NumberTheory.OeisA002897Wanted.Vars`, an abbreviation declared in [WantedExt/NumberTheory/OeisA002897Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisA002897Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/cubed-central-binomial-coefficients/index.html#vars).

## Exponent vector of $x^n y^n z^n$

For a natural number $n$, the exponent vector assigning
exponent $n$ to each of the three variables $x, y, z$, that is, the monomial $x^n y^n z^n$.

Formalized by `MathlibExt.NumberTheory.OeisA002897Wanted.xyzPowN`, a definition declared in [WantedExt/NumberTheory/OeisA002897Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisA002897Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/cubed-central-binomial-coefficients/index.html#xyz-pow-n).

## Product polynomial for the cubed central binomial coefficients

For a natural number $n$,
this is the polynomial $(1 + x + y + z)^{2n} (1 + x + y - z)^n (1 + x - y + z)^n$ in three
variables $x, y, z$ (indexed by $0, 1, 2$) with integer coefficients.

Formalized by `MathlibExt.NumberTheory.OeisA002897Wanted.pPoly`, a definition declared in [WantedExt/NumberTheory/OeisA002897Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisA002897Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/cubed-central-binomial-coefficients/index.html#p-poly).

## Diagonal-coefficient property of the cubed central binomial coefficients

This is the
proposition that for every natural number $n$, the coefficient of $x^n y^n z^n$ in the
polynomial $(1 + x + y + z)^{2n} (1 + x + y - z)^n (1 + x - y + z)^n$ in three variables
$x, y, z$ with integer coefficients equals $\binom{2n}{n}^3$.

Formalized by `MathlibExt.NumberTheory.OeisA002897Wanted.a_eq_coeff`, a definition declared in [WantedExt/NumberTheory/OeisA002897Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisA002897Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/cubed-central-binomial-coefficients/index.html#a-eq-coeff).

## Cubed central binomial coefficients as diagonal coefficients

For every natural number $n$,
the coefficient of $x^n y^n z^n$ in the polynomial
$(1 + x + y + z)^{2n} (1 + x + y - z)^n (1 + x - y + z)^n$ in three variables $x, y, z$ with
integer coefficients equals $\binom{2n}{n}^3$.

## Sources

- Formal proof of the A002897 diagonal-coefficient identity (methods of Tsoukalas et al. [arXiv/2605.22763]), https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/2897.wip.lean#L408.

Stated but not proved: `MathlibExt.NumberTheory.OeisA002897Wanted.a_eq_coeff_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/OeisA002897Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisA002897Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/cubed-central-binomial-coefficients/index.html#a-eq-coeff-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cubed central binomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/cubed-central-binomial-coefficients/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/binomial-coefficients/cubed-central-binomial-coefficients)
