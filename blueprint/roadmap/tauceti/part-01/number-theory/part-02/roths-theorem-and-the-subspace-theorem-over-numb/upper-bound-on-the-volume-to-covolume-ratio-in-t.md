---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.volume_div_covolume_le
statement: formalized
proof: formalized
---

# Upper bound on the volume-to-covolume ratio in terms of `Q ^ approxWeight S₀ c`

since
`v.floorValue t ≤ t`, the ratio is at most `approxConst S₀ L * Q ^ approxWeight S₀ c`.

```lean
TauCeti.NumberField.volume_div_covolume_le.{u_1, u_2} {K : Type u_1} [Field K] [NumberField K]
  {ι : Type u_2} [Fintype ι] {S₀ : Finset (NumberField.FinitePlace K)}
  {L : AbsoluteValue K ℝ → ι → Module.Dual K (ι → K)}
  (hLInf : ∀ (v : NumberField.InfinitePlace K), LinearIndependent K (L ↑v))
  (hLFin : ∀ v ∈ S₀, LinearIndependent K (L ↑v)) (c : AbsoluteValue K ℝ → ι → ℝ) {Q : ℝ}
  (hQ : 0 < Q) :
  MeasureTheory.volume.real (TauCeti.NumberField.approxBody L c Q) /
      ZLattice.covolume (TauCeti.NumberField.approxModule S₀ L c Q).mixedImage
        MeasureTheory.volume ≤
    TauCeti.NumberField.approxConst S₀ L * Q ^ TauCeti.NumberField.approxWeight S₀ c
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The covolume of an `𝓞 K`-module, read at the finite places](the-covolume-of-an-o-k-module-read-at-the-finite.md)
- [Ultrametric Hadamard bound, row form](../../../linear-algebra/part-01/polynomial-interpolation-and-arithmetic-determin/ultrametric-hadamard-bound-row-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.volume_div_covolume_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Subspace/Volume.html#TauCeti.NumberField.volume_div_covolume_le).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.volume_div_covolume_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Subspace/Volume.html#TauCeti.NumberField.volume_div_covolume_le)
- [Source of `TauCeti.NumberField.volume_div_covolume_le` in TauCeti/NumberTheory/DiophantineApproximation/Subspace/Volume.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/DiophantineApproximation/Subspace/Volume.lean#L743)
- [Tau Ceti roadmap status: Roth's theorem and the Subspace Theorem over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SubspaceTheorem/STATUS.md)
