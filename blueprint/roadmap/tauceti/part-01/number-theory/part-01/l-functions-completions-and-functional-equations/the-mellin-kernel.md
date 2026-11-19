---
declaration: def
origin: cited
lean: TauCeti.LFunctions.mellinKernel
statement: formalized
---

# The Mellin kernel

**The Mellin kernel** of a lattice `L` over a set `D` of parameters, Neukirch VII (5.5):
`f_D(L, u) = (2^r₂ / w) ∫_D θ_L(x (u / V_L²)^(1/n)) d*x`, the theta series of `L` averaged over
the points `x` of `D` on the norm-one hypersurface at the norm `u / V_L²`, with `V_L` the covolume
of `L` and `d*x = surfaceHaar K`.

```lean
TauCeti.LFunctions.mellinKernel.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (D : Set (NumberField.mixedEmbedding.realSpace K))
  (L : Submodule ℤ (NumberField.mixedEmbedding.mixedSpace K)) (u : ℝ) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.mellinKernel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Theta/Mellin/Kernel.html#TauCeti.LFunctions.mellinKernel).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.mellinKernel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Theta/Mellin/Kernel.html#TauCeti.LFunctions.mellinKernel)
- [Source of `TauCeti.LFunctions.mellinKernel` in TauCeti/NumberTheory/LFunctions/Theta/Mellin/Kernel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LFunctions/Theta/Mellin/Kernel.lean#L68)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LFunctions/STATUS.md)
