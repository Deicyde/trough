---
declaration: theorem
origin: cited
lean: MirekThiele.localT1, MirekThiele.localTb_all, MirekThiele.globalTb_all, MirekThiele.carlesonEmbedding
statement: formalized
proof: formalized
---

# Perfect multilinear local T(b) theorems

> Proves the perfect multilinear local T(1) and T(b) theorems with interdependent testing families. Develops dyadic stopping times, pruning, outer-measure interpolation and Carleson embedding. Also proves a global variant for locally dyadic testing functions with scale-normalized weak boundedness and finite-Hardy-norm BMO testing.

*Quoted from the card [LeanPool/projects/mirek-thiele.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/mirek-thiele.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`MirekThiele.localT1`](https://leanpool.github.io/lean-pool/LeanPool/MirekThiele/T1Theorem.html#MirekThiele.localT1) (theorem; a main declaration), declared in [LeanPool/MirekThiele/T1Theorem.lean, line 4676](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MirekThiele/T1Theorem.lean#L4676): “In positive dimension, a perfect multilinear Calderón–Zygmund form satisfying the local T(1) testing bound obeys a uniform Hölder bound on all dyadic test tuples, with a constant depending only on dimension, arity, exponents and testing bound.”
- [`MirekThiele.localTb_all`](https://leanpool.github.io/lean-pool/LeanPool/MirekThiele/T1Theorem.html#MirekThiele.localTb_all) (theorem; a main declaration), declared in [LeanPool/MirekThiele/T1Theorem.lean, line 4706](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MirekThiele/T1Theorem.lean#L4706): “In positive dimension, admissible collections of paths and testing functions satisfying the support, mean, norm, interdependence and local testing conditions imply the uniform Hölder bound, for every path length between one and the arity.”
- [`MirekThiele.globalTb_all`](https://leanpool.github.io/lean-pool/LeanPool/MirekThiele/T1Theorem.html#MirekThiele.globalTb_all) (theorem; a main declaration), declared in [LeanPool/MirekThiele/T1Theorem.lean, line 4712](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MirekThiele/T1Theorem.lean#L4712): “In positive dimension, locally dyadic, bounded pseudo-accretive testing functions satisfying scale-normalized weak boundedness and BMO testing on functions with integrable dyadic square function imply a uniform Hölder bound for the perfect form.”
- [`MirekThiele.carlesonEmbedding`](https://leanpool.github.io/lean-pool/LeanPool/MirekThiele/Estimates.html#MirekThiele.carlesonEmbedding) (theorem; a main declaration), declared in [LeanPool/MirekThiele/Estimates.lean, line 4889](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MirekThiele/Estimates.lean#L4889): “In positive dimension, dyadic martingale averages and differences satisfy outer Lp bounds for every finite exponent greater than one, with constants depending only on the dimension and exponent.”

## Project

- Authors: Stefanos Lappas.
- Source: *A local T(b) theorem for perfect multilinear Calderón–Zygmund operators*, [doi:10.1112/plms.12000](https://doi.org/10.1112/plms.12000), [arXiv:1506.01264](https://arxiv.org/abs/1506.01264).
- Project repository: [slappas94/Mirek-Thiele-local-tb](https://github.com/slappas94/Mirek-Thiele-local-tb), at commit [939d7c25](https://github.com/slappas94/Mirek-Thiele-local-tb/tree/939d7c25149c80219fddfe356eb043fff4504dbd).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 42B20, 42B25.
- In Lean Pool: [LeanPool/MirekThiele](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MirekThiele), from the card [LeanPool/projects/mirek-thiele.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/mirek-thiele.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/mirek-thiele.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/mirek-thiele.yaml)
- [Lean Pool at 701389c0: LeanPool/MirekThiele](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MirekThiele)
