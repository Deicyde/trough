---
declaration: theorem
origin: cited
lean: TauCeti.CotangentBundle.isLiouvilleDomain_codiscBundle
statement: formalized
proof: formalized
---

# The unit codisc bundle is a Liouville domain

For a compact smooth Riemannian manifold
`M` without boundary, the unit codisc bundle `D*M` is a Liouville domain in `T*M` for the
canonical symplectic form `ω = -dλ`, with primitive `-λ`: its Liouville field, the radial field
`p ∂_p`, points strictly outwards along the unit cosphere bundle, the level `‖p‖ = 1` of the norm
of covectors.

```lean
TauCeti.CotangentBundle.isLiouvilleDomain_codiscBundle.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] [CompactSpace M] :
  TauCeti.IsLiouvilleDomain (TauCeti.CotangentBundle.symplecticForm I M)
    (-TauCeti.CotangentBundle.liouvilleForm I M) (TauCeti.CotangentBundle.codiscBundle I M)
```

## Depends on

- [TauCeti.CotangentBundle](../../part-06/symplectic-geometry-and-hamiltonian-mechanics/tauceti-cotangentbundle.md)
- [TauCeti.IsLiouvilleDomain](tauceti-isliouvilledomain.md)

## Proof depends on

- [Chart formula for the canonical symplectic form](../../part-06/symplectic-geometry-and-hamiltonian-mechanics/chart-formula-for-the-canonical-symplectic-form.md)
- [TauCeti.CotangentBundle.isSymplectic\_symplecticForm](../../part-06/symplectic-geometry-and-hamiltonian-mechanics/tauceti-cotangentbundle-issymplectic-symplecticf.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CotangentBundle.isLiouvilleDomain_codiscBundle`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Domain.html#TauCeti.CotangentBundle.isLiouvilleDomain_codiscBundle).

## Sources

- [Tau Ceti documentation: `TauCeti.CotangentBundle.isLiouvilleDomain_codiscBundle`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Domain.html#TauCeti.CotangentBundle.isLiouvilleDomain_codiscBundle)
- [Source of `TauCeti.CotangentBundle.isLiouvilleDomain_codiscBundle` in TauCeti/Geometry/Symplectic/Cotangent/Bundle/Domain.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Domain.lean#L68)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGFloer/STATUS.md)
