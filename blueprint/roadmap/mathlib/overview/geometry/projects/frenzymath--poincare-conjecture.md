---
declaration: module
origin: cited
lean: PoincareConjecture, PoincareLib
statement: formalized
---

# The conjecture

[frenzymath/Poincare-Conjecture](https://github.com/frenzymath/Poincare-Conjecture) at commit [08f06794](https://github.com/frenzymath/Poincare-Conjecture/tree/08f06794dd88b786ae560b5db1116f50322c4629), 2026-11-04.

> The formalization has passed a full Lean build and Comparator verification. Comparator accepted both public targets at commit `1876d7dc`, with checks by Nanoda and Lean's default kernel. See the [verification evidence](https://github.com/frenzymath/Poincare-Conjecture/blob/08f06794dd88b786ae560b5db1116f50322c4629/archive/PoincareConjecture/references/ricci-flow/mapher/integration-verification/README.md) for the exact revisions, verifier configuration, and logs.

*Quoted from [README.md](https://github.com/frenzymath/Poincare-Conjecture/blob/08f06794dd88b786ae560b5db1116f50322c4629/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Change of variable](../../../undergraduate/single-variable-real-analysis/integration/change-of-variable.md)
- [Riemann-Lebesgue lemma (Analysis)](../../analysis/fourier-analysis/riemann-lebesgue-lemma.md)
- [Integral curves](../differentiable-manifolds/part-01/integral-curves.md)
- [Riemannian/bundle metric](../riemannian-manifolds/riemannian-bundle-metric.md)
- [Whitney embedding theorem](../../../thousand-plus/geometry-and-topology/57-manifolds-and-cell-complexes/whitney-embedding-theorem.md)
- [Positive cone](../convex-geometry/positive-cone.md)
- [Uniqueness of integral curves](../differentiable-manifolds/part-01/uniqueness-of-integral-curves.md)
- [Local extrema](../../analysis/differentiability/local-extrema.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`PoincareConjecture`](https://github.com/frenzymath/Poincare-Conjecture/blob/08f06794dd88b786ae560b5db1116f50322c4629/PoincareConjecture/PoincareConjecture.lean), [`PoincareLib`](https://github.com/frenzymath/Poincare-Conjecture/blob/08f06794dd88b786ae560b5db1116f50322c4629/PoincareConjecture/PoincareLib.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `PoincareConjecture/Comparator/Challenge.lean` holds `sorry` or `admit`.

## Project

- Lean v4.33.1, Mathlib at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).
- 24,195 .lean files; its Lean libraries `PoincareLib`, `PoincareConjecture`, `Challenge`, `Statements`, `Solution` hold 5,000 (the first read), declaring 16,595 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/frenzymath/Poincare-Conjecture/blob/08f06794dd88b786ae560b5db1116f50322c4629/LICENSE)).

## Builds on

- Mathlib, at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).
- `Comparator` (https://github.com/leanprover/comparator) at `3927ad38`.
- `lean4export` (https://github.com/leanprover/lean4export) at `15f6055e`.

## Placement

Of its imports of Mathlib modules in an overview area, 237 of 2242 are in Geometry, 4.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (237 of 2242 imports, 4.5×), Topology (464 of 2242 imports, 2.8×), Analysis (1332 of 2242 imports, 2.2×). *Proof depends on* lists 8 of the 182 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [frenzymath/Poincare-Conjecture at 08f06794](https://github.com/frenzymath/Poincare-Conjecture/tree/08f06794dd88b786ae560b5db1116f50322c4629)
