---
declaration: theorem
origin: cited
lean: TauCeti.UniversalEnvelopingAlgebra.kostantRootSubgroupParam_mul_mul_eq_kostantCoordinateCocharacter_mul_kostantWeylGL
statement: formalized
proof: formalized
---

# Chevalley's rank-one identity

**Chevalley's rank-one identity** `xᵢ(u) xⱼ(-u⁻¹) xᵢ(u) = h_c(u) n`, over every value ring
and at every unit `u`. Here `(eᵢ, eⱼ)` is a root pair whose `sl₂` triple has Cartan index `c`,
`h_c(u)` is the coordinate cocharacter at `c` and `n = xᵢ(1) xⱼ(-1) xᵢ(1)` is the Weyl
representative, and `α` is the weight of `eᵢ`, so that `eⱼ` has weight `-α`.

```lean
TauCeti.UniversalEnvelopingAlgebra.kostantRootSubgroupParam_mul_mul_eq_kostantCoordinateCocharacter_mul_kostantWeylGL.{u,
    v, w, u_1, u_2, u_3}
  {L : Type u} [LieRing L] [LieAlgebra ℚ L] {ι : Type u_1} {κ : Type u_2} {V : Type v}
  [AddCommGroup V] [_root_.Module ℚ V] (e : ι → L) (h : κ → L)
  (ρ : UniversalEnvelopingAlgebra ℚ L →ₐ[ℚ] Module.End ℚ V) (M : AddSubgroup V)
  (hM : ∀ u ∈ TauCeti.UniversalEnvelopingAlgebra.kostantForm e h, ∀ v ∈ M, (ρ u) v ∈ M)
  {η : Type u_3} (b : Module.Basis η ℤ ↥M) (wt : η → κ → ℤ) [Fintype κ] [DecidableEq κ]
  (hwt : ∀ (x : η), TauCeti.UniversalEnvelopingAlgebra.IsCartanWeightVector h ρ (wt x) ↑(b x))
  {i j : ι} {c : κ} {α : κ → ℤ}
  (hT :
    IsSl2Triple (ρ ((UniversalEnvelopingAlgebra.ι ℚ) (h c)))
      (ρ ((UniversalEnvelopingAlgebra.ι ℚ) (e i))) (ρ ((UniversalEnvelopingAlgebra.ι ℚ) (e j))))
  (hi : IsNilpotent (ρ ((UniversalEnvelopingAlgebra.ι ℚ) (e i))))
  (hj : IsNilpotent (ρ ((UniversalEnvelopingAlgebra.ι ℚ) (e j))))
  (hα : ∀ (j' : κ), ⁅h j', e i⁆ = ↑(α j') • e i)
  (hαneg : ∀ (j' : κ), ⁅h j', e j⁆ = -(↑(α j') • e j)) (A : CommAlgCat ℤ) (u : (↑A)ˣ) :
  (TauCeti.UniversalEnvelopingAlgebra.kostantRootSubgroupParam e h ρ M hM i hi A)
          (Multiplicative.ofAdd ↑u) *
        (TauCeti.UniversalEnvelopingAlgebra.kostantRootSubgroupParam e h ρ M hM j hj A)
          (Multiplicative.ofAdd (-↑u⁻¹)) *
      (TauCeti.UniversalEnvelopingAlgebra.kostantRootSubgroupParam e h ρ M hM i hi A)
        (Multiplicative.ofAdd ↑u) =
    (TauCeti.UniversalEnvelopingAlgebra.kostantCoordinateCocharacter M b wt (↑A) c) u *
      TauCeti.UniversalEnvelopingAlgebra.kostantWeylGL e h ρ M hM hi hj ↑A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UniversalEnvelopingAlgebra.kostantRootSubgroupParam_mul_mul_eq_kostantCoordinateCocharacter_mul_kostantWeylGL`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/Kostant/RootSubgroup/Torus/Coroot.html#TauCeti.UniversalEnvelopingAlgebra.kostantRootSubgroupParam_mul_mul_eq_kostantCoordinateCocharacter_mul_kostantWeylGL).

## Sources

- [Tau Ceti documentation: `TauCeti.UniversalEnvelopingAlgebra.kostantRootSubgroupParam_mul_mul_eq_kostantCoordinateCocharacter_mul_kostantWeylGL`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/Kostant/RootSubgroup/Torus/Coroot.html#TauCeti.UniversalEnvelopingAlgebra.kostantRootSubgroupParam_mul_mul_eq_kostantCoordinateCocharacter_mul_kostantWeylGL)
- [Source of `TauCeti.UniversalEnvelopingAlgebra.kostantRootSubgroupParam_mul_mul_eq_kostantCoordinateCocharacter_mul_kostantWeylGL` in TauCeti/Algebra/Lie/UniversalEnveloping/Kostant/RootSubgroup/Torus/Coroot.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/UniversalEnveloping/Kostant/RootSubgroup/Torus/Coroot.lean#L184)
