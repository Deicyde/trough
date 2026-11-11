---
declaration: theorem
origin: cited
lean: TauCeti.configurationCount_eq_coeff_rayTorusWeightSeries
statement: formalized
proof: formalized
---

# The ray count is the ray series

For a pairwise compatible family `T` of tori on the ray
of a class `A₀` that is not torsion, the torus `c` having class `m c • A₀` and the four-twist
weights `w c = w_(σ c, i c)`, the count in class `j • A₀` of the configurations supported in `T`
is the `j`-th coefficient of the ray series `∏ c ∈ s, f_(σ c, i c)(t ^ m c)`, for every finite
subfamily `s` containing the tori of class at most `j • A₀`.

```lean
TauCeti.configurationCount_eq_coeff_rayTorusWeightSeries.{u_1, u_2} {ι : Type u_1} {H : Type u_2}
  [AddCommMonoid H] {r : ι → ι → Prop} {cls : ι → H} {T : Set ι} {A₀ : H} {m : ι → ℕ+}
  {w : ι → ℕ → ℤ} (hT : T.Pairwise r) (hcls : ∀ c ∈ T, cls c = ↑(m c) • A₀)
  (hA₀ : Function.Injective fun n => n • A₀) {σ : ι → Bool} {i : ι → Fin 4}
  (hw : ∀ c ∈ T, w c = TauCeti.torusWeight (σ c) (i c)) {s : Finset ι} (hsT : ↑s ⊆ T) {j : ℕ}
  (hs : ∀ c ∈ T, ↑(m c) ≤ j → c ∈ s) :
  TauCeti.configurationCount r cls w T (j • A₀) =
    (PowerSeries.coeff j) (TauCeti.rayTorusWeightSeries s m σ i)
```

## Depends on

- [TauCeti.configurationCount](tauceti-configurationcount.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.configurationCount_eq_coeff_rayTorusWeightSeries`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/ConfigurationCount.html#TauCeti.configurationCount_eq_coeff_rayTorusWeightSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.configurationCount_eq_coeff_rayTorusWeightSeries`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/ConfigurationCount.html#TauCeti.configurationCount_eq_coeff_rayTorusWeightSeries)
- [Source of `TauCeti.configurationCount_eq_coeff_rayTorusWeightSeries` in TauCeti/Geometry/Symplectic/JHolomorphic/ConfigurationCount.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/JHolomorphic/ConfigurationCount.lean#L654)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TaubesGromov/STATUS.md)
