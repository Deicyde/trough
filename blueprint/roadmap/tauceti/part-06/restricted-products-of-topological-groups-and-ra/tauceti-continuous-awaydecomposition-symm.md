---
declaration: theorem
origin: cited
lean: TauCeti.continuous_awayDecomposition_symm
statement: formalized
proof: formalized
---

# TauCeti.continuous\_awayDecomposition\_symm

The inverse of the decomposition is continuous when the reference subgroups away from `S` are
open; the reference subgroups at `S` play no role, since the finite factor carries no integrality
condition. Together with `continuous_awayDecomposition` this makes the decomposition a
homeomorphism for such families.

```lean
TauCeti.continuous_awayDecomposition_symm.{u, v} {ι : Type u} {G : ι → Type v}
  [(i : ι) → Group (G i)] (S : Set ι) (hS : S.Finite) (U : (i : ι) → Subgroup (G i))
  [(i : ι) → TopologicalSpace (G i)] (hU : ∀ i ∉ S, IsOpen ↑(U i)) :
  Continuous ⇑(TauCeti.awayDecomposition S hS U).symm
```

## Depends on

- [TauCeti.awayDecomposition](tauceti-awaydecomposition.md)

## Proof depends on

- [TauCeti.restrictedProductSum](tauceti-restrictedproductsum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.continuous_awayDecomposition_symm`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Away/Decomposition.html#TauCeti.continuous_awayDecomposition_symm).

## Sources

- [Tau Ceti documentation: `TauCeti.continuous_awayDecomposition_symm`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Away/Decomposition.html#TauCeti.continuous_awayDecomposition_symm)
- [Source of `TauCeti.continuous_awayDecomposition_symm` in TauCeti/Topology/Algebra/RestrictedProduct/Away/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/RestrictedProduct/Away/Decomposition.lean#L184)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RestrictedProducts/STATUS.md)
