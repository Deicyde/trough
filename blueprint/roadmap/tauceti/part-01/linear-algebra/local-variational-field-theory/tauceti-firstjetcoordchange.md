---
declaration: def
origin: cited
lean: TauCeti.firstJetCoordChange
statement: formalized
---

# TauCeti.firstJetCoordChange

Pull back first jets by a base map and a possibly nonlinear, base-dependent
fibre map. Differentiability is required by the calculus lemmas, not by this definition.

```lean
TauCeti.firstJetCoordChange.{u_1, u_2, u_3, u_5, u_6} {𝕜 : Type u_1} {E : Type u_2} {E' : Type u_3}
  {F : Type u_5} {G : Type u_6} [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [NormedAddCommGroup E'] [NormedSpace 𝕜 E'] [NormedAddCommGroup F] [NormedSpace 𝕜 F]
  [NormedAddCommGroup G] [NormedSpace 𝕜 G] (h : E' → E) (g : E' × F → G) (x : E')
  (j : F × (E →L[𝕜] F)) : G × (E' →L[𝕜] G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.firstJetCoordChange`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Jet/Nonlinear.html#TauCeti.firstJetCoordChange).

## Sources

- [Tau Ceti documentation: `TauCeti.firstJetCoordChange`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Jet/Nonlinear.html#TauCeti.firstJetCoordChange)
- [Source of `TauCeti.firstJetCoordChange` in TauCeti/Analysis/Calculus/Jet/Nonlinear.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Jet/Nonlinear.lean#L49)
- [Tau Ceti roadmap status: Local variational field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LocalVariationalFieldTheory/STATUS.md)
