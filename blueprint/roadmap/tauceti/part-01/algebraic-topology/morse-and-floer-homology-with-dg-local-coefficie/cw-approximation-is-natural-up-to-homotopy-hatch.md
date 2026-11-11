---
declaration: theorem
origin: cited
lean: TauCeti.comp_sigmaCWApproximationLift_homotopic
statement: formalized
proof: formalized
---

# CW approximation is natural up to homotopy (Hatcher, Proposition 4.18)

`sigmaCWApproximationMap Y ∘ Γφ ≃ φ ∘ sigmaCWApproximationMap X`.

```lean
TauCeti.comp_sigmaCWApproximationLift_homotopic.{u} {X Y : TopCat} (φ : C(↑X, ↑Y)) :
  ((TopCat.Hom.hom (TauCeti.sigmaCWApproximationMap Y)).comp
        (TauCeti.sigmaCWApproximationLift φ)).Homotopic
    (φ.comp (TopCat.Hom.hom (TauCeti.sigmaCWApproximationMap X)))
```

## Depends on

- [CW approximation (Hatcher, Proposition 4.13)](cw-approximation-hatcher-proposition-4-13.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.comp_sigmaCWApproximationLift_homotopic`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/CWApproximation/Sigma.html#TauCeti.comp_sigmaCWApproximationLift_homotopic).

## Sources

- [Tau Ceti documentation: `TauCeti.comp_sigmaCWApproximationLift_homotopic`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/CWApproximation/Sigma.html#TauCeti.comp_sigmaCWApproximationLift_homotopic)
- [Source of `TauCeti.comp_sigmaCWApproximationLift_homotopic` in TauCeti/AlgebraicTopology/Homotopy/CWApproximation/Sigma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Homotopy/CWApproximation/Sigma.lean#L199)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGFloer/STATUS.md)
