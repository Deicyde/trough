---
declaration: theorem
origin: cited
lean: Kepler.the_kepler_conjecture_e2e, Kepler.Assembly.lpArchiveCertificatesDebt
statement: formalized
---

# The Kepler Conjecture, Re-Proven in Lean 4

[lispc/kepler-conjecture-lean4](https://github.com/lispc/kepler-conjecture-lean4) at commit [6654a964](https://github.com/lispc/kepler-conjecture-lean4/tree/6654a964c5c5b6bf483b9537cf0f80ecd83a8390), 2026-11-17.

## Depends on

- [Ball](../../topology/metric-spaces/ball.md)
- [Set](../sets/set.md)

## Proof depends on

- [Affine span](../../geometry/affine-and-euclidean-geometry/affine-span.md)
- [Cross product](../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/low-dimensions/cross-product.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Rank of a set of vectors](../../../undergraduate/linear-algebra/finite-dimensional-vector-spaces/rank-of-a-set-of-vectors.md)
- [Sin (extension of trigonometric functions to the complex plane)](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/sin.md)
- [Inverse trigonometric functions](../../analysis/special-functions/inverse-trigonometric-functions.md)
- [Trigonometric functions](../../analysis/special-functions/trigonometric-functions.md)
- [Determinant of endomorphisms](../../../undergraduate/linear-algebra/multilinearity/determinant-of-endomorphisms.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Kepler.the_kepler_conjecture_e2e`](https://github.com/lispc/kepler-conjecture-lean4/blob/6654a964c5c5b6bf483b9537cf0f80ecd83a8390/lean/Kepler/Final.lean#L22) (theorem)
- [`Kepler.Assembly.lpArchiveCertificatesDebt`](https://github.com/lispc/kepler-conjecture-lean4/blob/6654a964c5c5b6bf483b9537cf0f80ecd83a8390/lean/Kepler/Assembly.lean#L7106) (theorem, its text holds `sorry`)

Of the files its headlines import, directly or not, `lean/Kepler/Assembly.lean` hold `sorry` or `admit`.

## Project

- Lean v4.32.2.
- 20,776 .lean files; its Lean libraries `Kepler` hold 5,000 (the first read), declaring 11,999 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- No license file; facts only.

## Placement

Of its imports of Mathlib modules in an overview area, 14 of 24 are in Data structures, 4.1 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (14 of 24 imports, 4.1×), Analysis (3 of 24 imports, 0.5×), General algebra (3 of 24 imports, 0.4×). *Proof depends on* names 8 of the 36 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [lispc/kepler-conjecture-lean4 at 6654a964](https://github.com/lispc/kepler-conjecture-lean4/tree/6654a964c5c5b6bf483b9537cf0f80ecd83a8390)
