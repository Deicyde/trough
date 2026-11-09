---
declaration: theorem
origin: cited
lean: TauCeti.ModularForm.valence_formula_finiteIndex
statement: formalized
proof: formalized
---

# The valence formula at general level

for a nonzero weight-`k` form on a finite-index
`Γ ≤ SL(2, ℤ)`, the interior orders — weighted by `2 / |Stab_Γ P|` — together with the orders
indexed by the cusp translation orbits add up to `k · [SL(2, ℤ) : Γ] / 12`.

This is `valence_formula_finiteIndex_norm` with its cusp term, an order at `∞` on the norm,
distributed over the cusps of `Γ`.

```lean
TauCeti.ModularForm.valence_formula_finiteIndex.{u_1} {F : Type u_1} [FunLike F UpperHalfPlane ℂ]
  {k : ℤ} {Γ : Subgroup (Matrix.SpecialLinearGroup (Fin 2) ℤ)} [Γ.FiniteIndex]
  [ModularFormClass F (Subgroup.map (Matrix.SpecialLinearGroup.mapGL ℝ) Γ) k] (f : F)
  (hf : ⇑f ≠ 0) :
  ∑ᶠ (o :
        MulAction.orbitRel.Quotient (↥(Subgroup.map (Matrix.SpecialLinearGroup.mapGL ℝ) Γ))
          UpperHalfPlane),
        TauCeti.ModularForm.weightedOrderOfVanishingOnSubgroupOrbit f o +
      ∑ c, ↑(TauCeti.ModularForm.orderAtCuspTranslationOrbit f c) =
    ↑k *
        ↑(Nat.card
            (↥(Matrix.SpecialLinearGroup.mapGL ℝ).range ⧸
              (Subgroup.map (Matrix.SpecialLinearGroup.mapGL ℝ) Γ).subgroupOf
                (Matrix.SpecialLinearGroup.mapGL ℝ).range)) /
      12
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy–Goursat for a pole-free meromorphic function](../../../analysis/part-02/contour/cauchy-goursat-for-a-pole-free-meromorphic-funct.md)
- [The generalized residue theorem on a star-shaped open set, simple-pole regime](../../../analysis/part-02/contour/the-generalized-residue-theorem-on-a-star-shaped.md)
- [Generalized winding number (HW Def 2.1)](../../../analysis/part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularForm.valence_formula_finiteIndex`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Norm/Cusps.html#TauCeti.ModularForm.valence_formula_finiteIndex).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularForm.valence_formula_finiteIndex`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Norm/Cusps.html#TauCeti.ModularForm.valence_formula_finiteIndex)
- [Source of `TauCeti.ModularForm.valence_formula_finiteIndex` in TauCeti/NumberTheory/ModularForms/Norm/Cusps.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/Norm/Cusps.lean#L511)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularForms/STATUS.md)
