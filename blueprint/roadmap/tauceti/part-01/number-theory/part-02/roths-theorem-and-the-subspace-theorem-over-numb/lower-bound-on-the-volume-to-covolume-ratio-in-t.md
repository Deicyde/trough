---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.le_volume_div_covolume
statement: formalized
proof: formalized
---

# Lower bound on the volume-to-covolume ratio in terms of `Q ^ approxWeight S₀ c`

rounding
each finite-place bound down to the value group of `v ∈ S₀` loses strictly less than `N 𝔭_v` per
coordinate, so the ratio is at least
`approxConst S₀ L / (∏ v ∈ S₀, N 𝔭_v ^ card ι) * Q ^ approxWeight S₀ c`.

```lean
TauCeti.NumberField.le_volume_div_covolume.{u_1, u_2} {K : Type u_1} [Field K] [NumberField K]
  {ι : Type u_2} [Fintype ι] {S₀ : Finset (NumberField.FinitePlace K)}
  {L : AbsoluteValue K ℝ → ι → Module.Dual K (ι → K)}
  (hLInf : ∀ (v : NumberField.InfinitePlace K), LinearIndependent K (L ↑v))
  (hLFin : ∀ v ∈ S₀, LinearIndependent K (L ↑v)) (c : AbsoluteValue K ℝ → ι → ℝ) {Q : ℝ}
  (hQ : 0 < Q) :
  (TauCeti.NumberField.approxConst S₀ L /
        ∏ v ∈ S₀, ↑(Ideal.absNorm v.maximalIdeal.asIdeal) ^ Fintype.card ι) *
      Q ^ TauCeti.NumberField.approxWeight S₀ c ≤
    MeasureTheory.volume.real (TauCeti.NumberField.approxBody L c Q) /
      ZLattice.covolume (TauCeti.NumberField.approxModule S₀ L c Q).mixedImage MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The covolume of an `𝓞 K`-module, read at the finite places](the-covolume-of-an-o-k-module-read-at-the-finite.md)
- [Ultrametric Hadamard bound, row form](../../../linear-algebra/matrix/ultrametric-hadamard-bound-row-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.le_volume_div_covolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Subspace/Volume.html#TauCeti.NumberField.le_volume_div_covolume).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.le_volume_div_covolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Subspace/Volume.html#TauCeti.NumberField.le_volume_div_covolume)
- [Source of `TauCeti.NumberField.le_volume_div_covolume` in TauCeti/NumberTheory/DiophantineApproximation/Subspace/Volume.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/DiophantineApproximation/Subspace/Volume.lean#L764)
- [Tau Ceti roadmap status: Roth's theorem and the Subspace Theorem over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SubspaceTheorem/STATUS.md)
