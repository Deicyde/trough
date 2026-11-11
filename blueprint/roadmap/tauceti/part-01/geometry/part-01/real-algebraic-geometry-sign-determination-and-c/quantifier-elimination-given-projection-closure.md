---
declaration: theorem
origin: cited
lean: TauCeti.exists_isQF_realize_iff
statement: formalized
proof: formalized
---

# Quantifier elimination, given projection closure

Every formula of ordered rings whose
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
- [Source of `TauCeti.exists_isQF_realize_iff` in TauCeti/Geometry/RealAlgebraic/Semialgebraic/QuantifierElimination.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/Semialgebraic/QuantifierElimination.lean#L198)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RealAlgebraicGeometry/STATUS.md)
