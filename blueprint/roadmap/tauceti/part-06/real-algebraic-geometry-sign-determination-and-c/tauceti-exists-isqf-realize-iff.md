---
declaration: theorem
origin: cited
lean: TauCeti.exists_isQF_realize_iff
statement: formalized
proof: formalized
---

# TauCeti.exists\_isQF\_realize\_iff

**Quantifier elimination**, given projection closure. Every formula of ordered rings whose
free variables `Sum.inl r` are assigned the parameters `r ∈ R` is equivalent, for every
assignment `v` of the remaining free variables, to a quantifier-free formula with parameters.

```lean
TauCeti.exists_isQF_realize_iff.{u_1, u_2} {R : Type u_1} [CommRing R]
  [FirstOrder.Ring.CompatibleRing R] [FirstOrder.Language.order.Structure R] [LinearOrder R]
  [IsOrderedAddMonoid R]
  [(FirstOrder.Language.ring.sum FirstOrder.Language.order).OrderedStructure R]
  [TauCeti.HasSemialgebraicProjections R] {σ : Type u_2}
  (φ : (FirstOrder.Language.ring.sum FirstOrder.Language.order).Formula (R ⊕ σ)) :
  ∃ ψ,
    FirstOrder.Language.BoundedFormula.IsQF ψ ∧
      ∀ (v : σ → R), φ.Realize (Sum.elim id v) ↔ ψ.Realize (Sum.elim id v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isQF_realize_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Semialgebraic/QuantifierElimination.html#TauCeti.exists_isQF_realize_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isQF_realize_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Semialgebraic/QuantifierElimination.html#TauCeti.exists_isQF_realize_iff)
- [Source of `TauCeti.exists_isQF_realize_iff` in TauCeti/Geometry/RealAlgebraic/Semialgebraic/QuantifierElimination.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/Semialgebraic/QuantifierElimination.lean#L198)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
