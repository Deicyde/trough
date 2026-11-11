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

Formalized in Tau Ceti as [`TauCeti.LFunctions.mellinKernel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Theta/MellinKernel.html#TauCeti.LFunctions.mellinKernel).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.mellinKernel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Theta/MellinKernel.html#TauCeti.LFunctions.mellinKernel)
- [Source of `TauCeti.LFunctions.mellinKernel` in TauCeti/NumberTheory/LFunctions/Theta/MellinKernel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LFunctions/Theta/MellinKernel.lean#L64)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LFunctions/STATUS.md)
