---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.mellinKernel_inv
statement: formalized
proof: formalized
---

# The transformation law of the Mellin kernel, the first half of Neukirch VII (5.8)

`f_D(L, 1/u) = u^(1/2) f_{D⁻¹}(L^∨, u)` for every full lattice `L`, with the Euclidean dual
`L^∨ = mixedDual K L`, and every set `D` of parameters.

```lean
TauCeti.LFunctions.mellinKernel_inv.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (D : Set (NumberField.mixedEmbedding.realSpace K))
  (L : Submodule ℤ (NumberField.mixedEmbedding.mixedSpace K)) [DiscreteTopology ↥L] [IsZLattice ℝ L]
  {u : ℝ} (hu : 0 < u) :
  TauCeti.LFunctions.mellinKernel D L u⁻¹ =
    ↑√u * TauCeti.LFunctions.mellinKernel D⁻¹ (TauCeti.NumberField.mixedEmbedding.mixedDual K L) u
```

## Depends on

- [The Mellin kernel](the-mellin-kernel.md)

## Proof depends on

- [The theta transformation with one parameter per infinite place, Neukirch VII (3.6) on the imaginary axis](the-theta-transformation-with-one-parameter-per.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.mellinKernel_inv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Theta/MellinKernel.html#TauCeti.LFunctions.mellinKernel_inv).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.mellinKernel_inv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Theta/MellinKernel.html#TauCeti.LFunctions.mellinKernel_inv)
- [Source of `TauCeti.LFunctions.mellinKernel_inv` in TauCeti/NumberTheory/LFunctions/Theta/MellinKernel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LFunctions/Theta/MellinKernel.lean#L104)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LFunctions/STATUS.md)
