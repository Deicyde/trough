---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.latticeTheta_inv
statement: formalized
proof: formalized
---

# The theta transformation with one parameter per infinite place, Neukirch VII (3.6) on the imaginary axis

for every full lattice `L` of the mixed space and every positive parameter `y`,
`θ_L(y) = covol(L)⁻¹ N(y)^(-1/2) θ_{L^∨}(y⁻¹)`, the dual being the Euclidean dual `mixedDual`.

```lean
TauCeti.LFunctions.latticeTheta_inv.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (L : Submodule ℤ (NumberField.mixedEmbedding.mixedSpace K)) [DiscreteTopology ↥L] [IsZLattice ℝ L]
  (y : NumberField.mixedEmbedding.realSpace K) (hy : ∀ (w : NumberField.InfinitePlace K), 0 < y w) :
  TauCeti.LFunctions.latticeTheta L y =
    (↑(ZLattice.covolume L MeasureTheory.volume))⁻¹ * ↑(√(TauCeti.LFunctions.archNorm y))⁻¹ *
      TauCeti.LFunctions.latticeTheta (TauCeti.NumberField.mixedEmbedding.mixedDual K L) y⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Poisson's summation formula](../../../analysis/part-02/fourier/poissons-summation-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.latticeTheta_inv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Theta/Inversion.html#TauCeti.LFunctions.latticeTheta_inv).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.latticeTheta_inv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Theta/Inversion.html#TauCeti.LFunctions.latticeTheta_inv)
- [Source of `TauCeti.LFunctions.latticeTheta_inv` in TauCeti/NumberTheory/LFunctions/Theta/Inversion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LFunctions/Theta/Inversion.lean#L106)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LFunctions/STATUS.md)
