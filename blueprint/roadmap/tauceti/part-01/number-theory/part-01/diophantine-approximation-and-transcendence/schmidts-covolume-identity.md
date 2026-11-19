---
declaration: theorem
origin: cited
lean: Submodule.covolume_integerLattice, Submodule.covolume_integerLattice_eq_covolume_pow_mul_relativeSubspaceArakelovHeight
statement: formalized
proof: formalized
---

# Schmidt's covolume identity

For a `K`-subspace `W` of `ι → K`, the covolume of the
saturated lattice `W.integerLattice` (`W ∩ 𝓞_K^ι`) in the Euclidean Minkowski span `W.euclideanSpan`
is `((2⁻¹) ^ nrComplexPlaces K * √|discr K|) ^ finrank K W * W.subspaceHeight ^ finrank ℚ K`.

```lean
Submodule.covolume_integerLattice.{u_1, u_2} {K : Type u_1} [Field K] [NumberField K] {ι : Type u_2}
  [Fintype ι] [LinearOrder ι] (W : Submodule K (ι → K)) :
  ZLattice.covolume W.integerLattice MeasureTheory.volume =
    (2⁻¹ ^ NumberField.InfinitePlace.nrComplexPlaces K * √|↑(NumberField.discr K)|) ^
        Module.finrank K ↥W *
      W.subspaceHeight ^ Module.finrank ℚ K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Binet formula](../../../linear-algebra/part-02/other-results/the-cauchy-binet-formula.md)
- [Pseudo-bases over a Dedekind domain](../../part-02/roths-theorem-and-the-subspace-theorem-over-numb/pseudo-bases-over-a-dedekind-domain.md)
- [Ultrametric Hadamard bound, row form](../../../linear-algebra/part-01/polynomial-interpolation-and-arithmetic-determin/ultrametric-hadamard-bound-row-form.md)

## Lean

Formalized in Tau Ceti as [`Submodule.covolume_integerLattice`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/Subspace/Covolume.html#Submodule.covolume_integerLattice).

## Other forms

**Schmidt's covolume identity (relative form).** Formalized in Tau Ceti as [`Submodule.covolume_integerLattice_eq_covolume_pow_mul_relativeSubspaceArakelovHeight`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/Subspace/Covolume.html#Submodule.covolume_integerLattice_eq_covolume_pow_mul_relativeSubspaceArakelovHeight).

```lean
Submodule.covolume_integerLattice_eq_covolume_pow_mul_relativeSubspaceArakelovHeight.{u_1, u_2}
  {K : Type u_1} [Field K] [NumberField K] {ι : Type u_2} [Fintype ι] [LinearOrder ι]
  (W : Submodule K (ι → K)) :
  ZLattice.covolume W.integerLattice MeasureTheory.volume =
    ZLattice.covolume (NumberField.mixedEmbedding.integerLattice K) MeasureTheory.volume ^
        Module.finrank K ↥W *
      W.relativeSubspaceArakelovHeight
```

## Sources

- [Tau Ceti documentation: `Submodule.covolume_integerLattice`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/Subspace/Covolume.html#Submodule.covolume_integerLattice)
- [Source of `Submodule.covolume_integerLattice` in TauCeti/NumberTheory/Height/Arakelov/Subspace/Covolume.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Height/Arakelov/Subspace/Covolume.lean#L546)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
