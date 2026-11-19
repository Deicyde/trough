---
declaration: theorem
origin: cited
lean: DedekindZetaZeroFree.dedekindZeta_ne_zero
statement: formalized
proof: formalized
---

# Dedekind Zeta Zero-Free Region

[AxiomMath/DedekindZetaZeroFree](https://github.com/AxiomMath/DedekindZetaZeroFree) at commit [09afbb4c](https://github.com/AxiomMath/DedekindZetaZeroFree/tree/09afbb4ce6570c1615d58509dc197fc9f0956b7d), 2026-10-13.

> This is a Lean formalization of Theorem 1.1 and Corollary 1.2 of [A quasi-Riemann hypothesis for Dedekind zeta functions](https://hexagonmath.org/2610.00200v1).

*Quoted from [README.md](https://github.com/AxiomMath/DedekindZetaZeroFree/blob/09afbb4ce6570c1615d58509dc197fc9f0956b7d/README.md), Apache-2.0.*

## Depends on

- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Field](../../../general-algebra/field-theory/field.md)
- [Set](../../../data-structures/sets/set.md)

## Proof depends on

- [Category of finite-dimensional representations](../../../general-algebra/representation-theory/category-of-finite-dimensional-representations.md)
- [Character](../../../general-algebra/representation-theory/character.md)
- [Monotone convergence theorem (1000+ theorems)](../../../../thousand-plus/analysis/26-real-functions/part-01/monotone-convergence-theorem.md)
- [Finiteness of the class number](../../../general-algebra/algebraic-number-theory/finiteness-of-the-class-number.md)
- [Jacobson density theorem](../../../../thousand-plus/algebra/13-commutative-algebra/jacobson-density-theorem.md)
- [Special unitary group](../../../../undergraduate/group-theory/classical-automorphism-groups/special-unitary-group.md)
- [Rational functions](../../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/rational-functions.md)
- [Minkowski’s Fundamental Theorem](../../../../hundred-theorems/part-02/minkowskis-fundamental-theorem.md)

## Main results

Its Lean names are the theorems of its top-level module named Main, MainTheorem(s) or Statement(s):

- [`DedekindZetaZeroFree.dedekindZeta_ne_zero`](https://github.com/AxiomMath/DedekindZetaZeroFree/blob/09afbb4ce6570c1615d58509dc197fc9f0956b7d/DedekindZetaZeroFree/Main.lean#L9) (theorem)

No file its headlines import, directly or not (3842 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc3, Mathlib at [0493595e](https://github.com/leanprover-community/mathlib4/tree/0493595ecd5da8ef14742febab99728f98e948e8).
- 5,528 .lean files; its Lean libraries `DedekindZetaZeroFree`, `DedekindZetaChallenge`, `DedekindZetaSolution` hold 3,870, declaring 27,782 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/DedekindZetaZeroFree/blob/09afbb4ce6570c1615d58509dc197fc9f0956b7d/LICENSE)).

## Builds on

- Mathlib, at [0493595e](https://github.com/leanprover-community/mathlib4/tree/0493595ecd5da8ef14742febab99728f98e948e8).
- `FiniteAbelianGlobalReciprocityv2`.
- `TauCeti` (https://github.com/TauCetiProject/TauCeti.git) at `c197d7bd`.

## Placement

Of its imports of Mathlib modules in an overview area, 78 of 610 are in Linear algebra, 2.2 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Linear algebra (78 of 610 imports, 2.2×), Analysis (281 of 610 imports, 1.7×), General algebra (176 of 610 imports, 0.8×). *Proof depends on* names 8 of the 205 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [AxiomMath/DedekindZetaZeroFree at 09afbb4c](https://github.com/AxiomMath/DedekindZetaZeroFree/tree/09afbb4ce6570c1615d58509dc197fc9f0956b7d)
