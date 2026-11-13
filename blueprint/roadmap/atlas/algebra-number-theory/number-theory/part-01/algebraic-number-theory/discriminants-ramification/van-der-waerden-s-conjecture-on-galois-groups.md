---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.VanDerWaerdenConjectureWanted.vanDerWaerdenConjecture.E, MathlibExt.NumberTheory.VanDerWaerdenConjectureWanted.vanDerWaerdenConjecture.theorem_1
statement: formalized
---

# Van der Waerden's conjecture on Galois groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/van-der-waerden-s-conjecture-on-galois-groups/index.html).

## Monic integer polynomials whose Galois group is not $S_n$

For natural numbers $n$ and
$H$, $E_n(H)$ is the number of monic polynomials $f(x) = x^n + a_1 x^{n-1} + \dots + a_n$ of
degree $n$ with integer coefficients and $|a_i| \le H$ for $i = 1, \dots, n$ whose Galois group
over $\mathbb{Q}$ has order less than $n!$, that is, is not the full symmetric group $S_n$.

Formalized by `MathlibExt.NumberTheory.VanDerWaerdenConjectureWanted.vanDerWaerdenConjecture.E`, a definition declared in [WantedExt/NumberTheory/VanDerWaerdenConjectureWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/VanDerWaerdenConjectureWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/van-der-waerden-s-conjecture-on-galois-groups/index.html#e).

## Van der Waerden's conjecture (Bhargava)

For every natural number $n \ge 3$ there is a
constant $C$ such that $E_n(H) \le C H^{n-1}$ for all sufficiently large natural numbers $H$,
where $E_n(H)$ is the number of monic polynomials of degree $n$ with integer coefficients, all
non-leading coefficients of absolute value at most $H$, whose Galois group over $\mathbb{Q}$
has order less than $n!$.

The degree restriction is necessary: the statement is false for $n = 2$.

## Sources

- M. Bhargava, `Galois groups of random integer polynomials and van der Waerden's Conjecture`, Annals of Math, 201 (2) 2025. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_van_der_waerden_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.VanDerWaerdenConjectureWanted.vanDerWaerdenConjecture.theorem_1` is written with `theorem_wanted` in [WantedExt/NumberTheory/VanDerWaerdenConjectureWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/VanDerWaerdenConjectureWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/van-der-waerden-s-conjecture-on-galois-groups/index.html#theorem-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Van der Waerden's conjecture on Galois groups](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/van-der-waerden-s-conjecture-on-galois-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/van-der-waerden-s-conjecture-on-galois-groups)
