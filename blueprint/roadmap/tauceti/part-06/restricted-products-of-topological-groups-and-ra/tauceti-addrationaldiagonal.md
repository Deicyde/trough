---
declaration: def
origin: cited
lean: TauCeti.addRationalDiagonal
statement: formalized
---

# TauCeti.addRationalDiagonal

The diagonal additive homomorphism into a restricted product
induced by a family of additive homomorphisms whose values are eventually in the reference
subgroups. The eventual-integrality evidence `h` is an argument, not a consequence of the
construction.

```lean
TauCeti.addRationalDiagonal.{u, v, w} {ι : Type u} {G : ι → Type v} [(i : ι) → AddGroup (G i)]
  {Γ : Type w} [AddZeroClass Γ] (φ : (i : ι) → Γ →+ G i) (U : (i : ι) → AddSubgroup (G i))
  (h : ∀ (γ : Γ), ∀ᶠ (i : ι) in Filter.cofinite, (φ i) γ ∈ U i) :
  Γ →+ RestrictedProduct (fun i => G i) (fun i => ↑(U i)) Filter.cofinite
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.addRationalDiagonal`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Diagonal.html#TauCeti.addRationalDiagonal).

## Sources

- [Tau Ceti documentation: `TauCeti.addRationalDiagonal`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/Diagonal.html#TauCeti.addRationalDiagonal)
- [Source of `TauCeti.addRationalDiagonal` in TauCeti/Topology/Algebra/RestrictedProduct/Diagonal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/RestrictedProduct/Diagonal.lean#L58)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RestrictedProducts/STATUS.md)
