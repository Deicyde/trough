---
declaration: theorem
origin: cited
lean: SSet.Quasicategory.hornFilling_zero
statement: formalized
proof: formalized
---

# Joyal's theorem on special outer horns (HTT Proposition 1.2.4.3)

in a quasicategory, a
horn `Λ[n + 2, 0]` whose initial edge, from `0` to `1`, is an equivalence can be filled.

```lean
SSet.Quasicategory.hornFilling_zero.{u} {C : _root_.SSet} [C.Quasicategory] {n : ℕ}
  (σ₀ : (SSet.horn (n + 2) 0).toSSet ⟶ C)
  (h :
    (SSet.Edge.mk'
        ((CategoryTheory.ConcreteCategory.hom (σ₀.app (Opposite.op { len := 1 })))
          (SSet.horn.edge (n + 2) 0 0 1 ⋯ ⋯))).IsEquivalence) :
  ∃ σ, σ₀ = CategoryTheory.CategoryStruct.comp (SSet.horn (n + 2) 0).ι σ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SSet.Quasicategory.hornFilling_zero`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Quasicategory/OuterHorn.html#SSet.Quasicategory.hornFilling_zero).

## Sources

- [Tau Ceti documentation: `SSet.Quasicategory.hornFilling_zero`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Quasicategory/OuterHorn.html#SSet.Quasicategory.hornFilling_zero)
- [Source of `SSet.Quasicategory.hornFilling_zero` in TauCeti/AlgebraicTopology/Quasicategory/OuterHorn.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Quasicategory/OuterHorn.lean#L117)
