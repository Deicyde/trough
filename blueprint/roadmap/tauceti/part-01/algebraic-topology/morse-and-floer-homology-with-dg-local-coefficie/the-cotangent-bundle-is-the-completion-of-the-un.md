---
declaration: theorem
origin: cited
lean: TauCeti.CotangentBundle.isLiouvilleCompletion_codiscBundle
statement: formalized
proof: formalized
---

# The cotangent bundle is the completion of the unit codisc bundle

For a compact smooth
Riemannian manifold `M` without boundary, `T*M` is a completion of the Liouville domain `D*M`: the
flow `p ↦ e^t p` of its Liouville field `p ∂_p` is defined for all time, and carries every
covector into `D*M`.

```lean
TauCeti.CotangentBundle.isLiouvilleCompletion_codiscBundle.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] [CompactSpace M] [T2Space M] :
  TauCeti.IsLiouvilleCompletion (TauCeti.CotangentBundle.symplecticForm I M)
    (-TauCeti.CotangentBundle.liouvilleForm I M) (TauCeti.CotangentBundle.codiscBundle I M)
```

## Depends on

- [TauCeti.IsLiouvilleCompletion](tauceti-isliouvillecompletion.md)

## Proof depends on

- [The unit codisc bundle is a Liouville domain](the-unit-codisc-bundle-is-a-liouville-domain.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CotangentBundle.isLiouvilleCompletion_codiscBundle`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Domain.html#TauCeti.CotangentBundle.isLiouvilleCompletion_codiscBundle).

## Sources

- [Tau Ceti documentation: `TauCeti.CotangentBundle.isLiouvilleCompletion_codiscBundle`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Domain.html#TauCeti.CotangentBundle.isLiouvilleCompletion_codiscBundle)
- [Source of `TauCeti.CotangentBundle.isLiouvilleCompletion_codiscBundle` in TauCeti/Geometry/Symplectic/Cotangent/Bundle/Domain.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Domain.lean#L90)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGFloer/STATUS.md)
