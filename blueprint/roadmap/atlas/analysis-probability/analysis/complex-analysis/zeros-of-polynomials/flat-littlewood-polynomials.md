---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FlatLittlewoodPolyWanted.FlatLittlewoodPoly.IsLittlewoodPolynomial, MathlibExt.Analysis.FlatLittlewoodPolyWanted.FlatLittlewoodPoly.theorem_1_1
statement: formalized
---

# Flat Littlewood polynomials

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/flat-littlewood-polynomials/index.html).

## Littlewood polynomials

A polynomial $P$ over a ring $F$, of degree $n$ (with the zero
polynomial taken to have degree $0$), is a Littlewood polynomial if each of its coefficients of
$X^0, X^1, \ldots, X^n$ is $1$ or $-1$.

Formalized by `MathlibExt.Analysis.FlatLittlewoodPolyWanted.FlatLittlewoodPoly.IsLittlewoodPolynomial`, a definition declared in [WantedExt/Analysis/FlatLittlewoodPolyWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FlatLittlewoodPolyWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/flat-littlewood-polynomials/index.html#is-littlewood-polynomial).

## Flat Littlewood polynomials exist

There exist real constants $\Delta > \delta > 0$ such
that for every natural number $n \ge 2$ there is a Littlewood polynomial $P$ with complex
coefficients and of degree $n$ such that $\delta \sqrt{n} \le |P(z)| \le \Delta \sqrt{n}$ for all
$z \in \mathbb{C}$ with $|z| = 1$.

## Sources

- P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe, and M. Tiba, `Flat Littlewood polynomials exist`, Annals of Math, 192 (3) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_flat_littlewood_poly` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.FlatLittlewoodPolyWanted.FlatLittlewoodPoly.theorem_1_1` is written with `theorem_wanted` in [WantedExt/Analysis/FlatLittlewoodPolyWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FlatLittlewoodPolyWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/flat-littlewood-polynomials/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Flat Littlewood polynomials](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/flat-littlewood-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/zeros-of-polynomials/flat-littlewood-polynomials)
