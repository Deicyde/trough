---
declaration: theorem
origin: cited
lean: ModularForm.exists_isIntegralModularForm_specialize_tateCurve_eq
statement: formalized
proof: formalized
---

# The integral lattice of level-one modular forms

A level-one modular form of weight `k`
whose `q`-expansion `P` has integer coefficients is the Tate expansion of an integral modular form
of weight `k` lying in `ℤ[c₄, c₆, Δ]`.

```lean
ModularForm.exists_isIntegralModularForm_specialize_tateCurve_eq {k : ℕ}
  (F : ModularForm (Matrix.SpecialLinearGroup.mapGL ℝ).range ↑k) {P : PowerSeries ℤ}
  (hP : UpperHalfPlane.qExpansion 1 ⇑F = (PowerSeries.map (Int.castRingHom ℂ)) P) :
  ∃
    f ∈
      ℤ[WeierstrassCurve.c₄ WeierstrassCurve.Universal.curve,
        WeierstrassCurve.c₆ WeierstrassCurve.Universal.curve,
        WeierstrassCurve.Δ WeierstrassCurve.Universal.curve],
    WeierstrassCurve.IsIntegralModularForm k f ∧ TauCeti.tateCurve.specialize f = P
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Deligne's theorem (`WeierstrassCurve.IsIntegralModularForm.mem_adjoin`)](delignes-theorem-weierstrasscurve-isintegralmodu.md)

## Lean

Formalized in Tau Ceti as [`ModularForm.exists_isIntegralModularForm_specialize_tateCurve_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/QExpansion.html#ModularForm.exists_isIntegralModularForm_specialize_tateCurve_eq).

## Sources

- [Tau Ceti documentation: `ModularForm.exists_isIntegralModularForm_specialize_tateCurve_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/QExpansion.html#ModularForm.exists_isIntegralModularForm_specialize_tateCurve_eq)
- [Source of `ModularForm.exists_isIntegralModularForm_specialize_tateCurve_eq` in TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/QExpansion.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/QExpansion.lean#L225)
- [Tau Ceti roadmap status: Elliptic cohomology and topological modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCohomology/STATUS.md)
