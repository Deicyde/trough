---
declaration: def
origin: cited
lean: TauCeti.addAwayDecomposition
statement: formalized
---

# TauCeti.addAwayDecomposition

For a finite set `S` of indices, the decomposition of a
restricted product of additive groups as the plain product of the factors at `S` times the
restricted product away from `S`, coordinatewise the identity in both directions: `x` goes to
`((x i)_{i ∈ S}, (x i)_{i ∉ S})`, and `(y, z)` goes to the element with coordinate `y ⟨i, _⟩` at
`i ∈ S` and `z ⟨i, _⟩` at `i ∉ S`.

It is the composite of the reindexing along `Equiv.sumCompl (· ∈ S)`, the splitting over the sum
`S ⊕ {i // i ∉ S}`, and the collapse of the restricted product over the finite index type `S`.

```lean
TauCeti.addAwayDecomposition.{u, v} {ι : Type u} {G : ι → Type v} [(i : ι) → AddGroup (G i)]
  (S : Set ι) (hS : S.Finite) (U : (i : ι) → AddSubgroup (G i)) :
  TauCeti.RestrictedProductAddGroup U ≃+
    TauCeti.RestrictedProductAddGroupWithFactor ((i : ↑S) → G ↑i) fun j => U ↑j
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.addAwayDecomposition`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Away/Decomposition.html#TauCeti.addAwayDecomposition).

## Sources

- [Tau Ceti documentation: `TauCeti.addAwayDecomposition`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Away/Decomposition.html#TauCeti.addAwayDecomposition)
- [Source of `TauCeti.addAwayDecomposition` in TauCeti/Topology/Algebra/RestrictedProduct/Away/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/RestrictedProduct/Away/Decomposition.lean#L65)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RestrictedProducts/STATUS.md)
