---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.exists_isDistinguished_isUnit_of_isDistinguished_one
statement: formalized
proof: formalized
---

# Radius selection for distinguished overconvergent series

Let `g` be an overconvergent
series in the variables `Option σ` which, as a series in `Y = X none` over the Tate algebra in the
variables `σ`, is distinguished of degree `s` at radius `1` with a unit coefficient `g_s`. Then for
every `ρ₀ > 1` there are radii `1 < ρ ≤ r ≤ ρ₀` such that `g` is restricted at `r`, and its
coefficient slices `gₘ`, which are restricted at `ρ`, form a series `G = ∑ₘ gₘ Yᵐ` over the
series restricted at `ρ` that is distinguished of degree `s` at radius `r`, with `g_s` a unit.

This is the radius selection behind Weierstrass division by `g` inside the Monsky–Washnitzer
algebra. A single common radius `ρ = r > 1` does not suffice in general.

```lean
TauCeti.Dagger.exists_isDistinguished_isUnit_of_isDistinguished_one.{u_1, u_3} {σ : Type u_1}
  {K : Type u_3} [NormedField K] [IsUltrametricDist K] [CompleteSpace K]
  {g : ↥(TauCeti.Dagger.washnitzerAlgebra (Option σ) K)} {s : ℕ}
  (hg :
    TauCeti.PowerSeries.IsDistinguished 1 s
      ↑(MvPowerSeries.restrictedOptionEquiv
          ((TauCeti.Dagger.washnitzerAlgebra.toTate (Option σ) K) g)))
  (hu :
    IsUnit
      ((PowerSeries.coeff s)
        ↑(MvPowerSeries.restrictedOptionEquiv
            ((TauCeti.Dagger.washnitzerAlgebra.toTate (Option σ) K) g))))
  {ρ₀ : ℝ} (hρ₀ : 1 < ρ₀) :
  ∃ ρ,
    ∃ (x : Fact (0 < ρ)),
      ∃ r,
        1 < ρ ∧
          ρ ≤ r ∧
            r ≤ ρ₀ ∧
              MvPowerSeries.IsRestricted (fun x => r) ↑g ∧
                ∃ G,
                  (∀ (m : ℕ),
                      ↑((PowerSeries.coeff m) G) =
                        (PowerSeries.coeff m) ((MvPowerSeries.optionEquivLeft σ K) ↑g)) ∧
                    TauCeti.PowerSeries.IsDistinguished r s G ∧ IsUnit ((PowerSeries.coeff s) G)
```

## Depends on

- [TauCeti.Dagger.washnitzerAlgebra](tauceti-dagger-washnitzeralgebra.md)
- [TauCeti.Dagger.washnitzerAlgebra.toTate](tauceti-dagger-washnitzeralgebra-totate.md)

## Proof depends on

- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../mv-power-series/neumann-series-criterion-mvpowerseries-isnormmul.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.exists_isDistinguished_isUnit_of_isDistinguished_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Distinguished.html#TauCeti.Dagger.exists_isDistinguished_isUnit_of_isDistinguished_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.exists_isDistinguished_isUnit_of_isDistinguished_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Distinguished.html#TauCeti.Dagger.exists_isDistinguished_isUnit_of_isDistinguished_one)
- [Source of `TauCeti.Dagger.exists_isDistinguished_isUnit_of_isDistinguished_one` in TauCeti/RingTheory/Dagger/Distinguished.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Dagger/Distinguished.lean#L290)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
