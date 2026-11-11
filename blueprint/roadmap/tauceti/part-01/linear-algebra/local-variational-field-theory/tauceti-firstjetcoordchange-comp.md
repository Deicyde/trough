---
declaration: theorem
origin: cited
lean: TauCeti.firstJetCoordChange_comp
statement: formalized
proof: formalized
---

# TauCeti.firstJetCoordChange_comp

The cocycle law for nonlinear fibre-coordinate changes, with both base and
fibre derivatives evaluated at their actual intermediate points.

```lean
TauCeti.firstJetCoordChange_comp.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {𝕜 : Type u_1} {E : Type u_2}
  {E' : Type u_3} {E'' : Type u_4} {F : Type u_5} {G : Type u_6} {H : Type u_7}
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup E']
  [NormedSpace 𝕜 E'] [NormedAddCommGroup E''] [NormedSpace 𝕜 E''] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [NormedAddCommGroup G] [NormedSpace 𝕜 G] [NormedAddCommGroup H]
  [NormedSpace 𝕜 H] {h : E' → E} {k : E'' → E'} {g : E' × F → G} {l : E'' × G → H} {y : E''}
  (j : F × (E →L[𝕜] F)) (hh : DifferentiableAt 𝕜 h (k y)) (hk : DifferentiableAt 𝕜 k y)
  (hg : DifferentiableAt 𝕜 g (k y, j.1)) (hl : DifferentiableAt 𝕜 l (y, g (k y, j.1))) :
  TauCeti.firstJetCoordChange k l y (TauCeti.firstJetCoordChange h g (k y) j) =
    TauCeti.firstJetCoordChange (h ∘ k) (fun p => l (p.1, g (k p.1, p.2))) y j
```

## Depends on

- [TauCeti.firstJetCoordChange](tauceti-firstjetcoordchange.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.firstJetCoordChange_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Jet/Nonlinear.html#TauCeti.firstJetCoordChange_comp).

## Sources

- [Tau Ceti documentation: `TauCeti.firstJetCoordChange_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Jet/Nonlinear.html#TauCeti.firstJetCoordChange_comp)
- [Source of `TauCeti.firstJetCoordChange_comp` in TauCeti/Analysis/Calculus/Jet/Nonlinear.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Jet/Nonlinear.lean#L102)
- [Tau Ceti roadmap status: Local variational field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LocalVariationalFieldTheory/STATUS.md)
