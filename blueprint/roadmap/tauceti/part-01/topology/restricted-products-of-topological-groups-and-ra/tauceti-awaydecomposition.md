---
declaration: def
origin: cited
lean: TauCeti.awayDecomposition
statement: formalized
---

# TauCeti.awayDecomposition

For a finite set `S` of indices, the decomposition of a restricted product as the plain
product of the factors at `S` times the restricted product away from `S`, coordinatewise the
identity in both directions: `x` goes to `((x i)_{i ∈ S}, (x i)_{i ∉ S})`, and `(y, z)` goes to
the element with coordinate `y ⟨i, _⟩` at `i ∈ S` and `z ⟨i, _⟩` at `i ∉ S`.

It is the composite of the reindexing along `Equiv.sumCompl (· ∈ S)`, the splitting over the sum
`S ⊕ {i // i ∉ S}`, and the collapse of the restricted product over the finite index type `S`.

```lean
TauCeti.awayDecomposition.{u, v} {ι : Type u} {G : ι → Type v} [(i : ι) → Group (G i)] (S : Set ι)
  (hS : S.Finite) (U : (i : ι) → Subgroup (G i)) :
  TauCeti.RestrictedProductGroup U ≃*
    TauCeti.RestrictedProductGroupWithFactor ((i : ↑S) → G ↑i) fun j => U ↑j
```

## Depends on

- [TauCeti.restrictedProductSum](tauceti-restrictedproductsum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.awayDecomposition`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Away/Decomposition.html#TauCeti.awayDecomposition).

## Sources

- [Tau Ceti documentation: `TauCeti.awayDecomposition`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Away/Decomposition.html#TauCeti.awayDecomposition)
- [Source of `TauCeti.awayDecomposition` in TauCeti/Topology/Algebra/RestrictedProduct/Away/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/RestrictedProduct/Away/Decomposition.lean#L58)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RestrictedProducts/STATUS.md)
