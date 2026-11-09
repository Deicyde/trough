---
declaration: def
origin: cited
lean: TauCeti.IntegralLattice.evenIntermediateCarrierOrderIsoIsotropicSubgroup
statement: formalized
---

# Even overlattices correspond to quadratic-isotropic subgroups

For an even lattice, the
intermediate-carrier order isomorphism restricts to the even carriers on one side and the
quadratic-isotropic subgroups of the discriminant group on the other.

```lean
TauCeti.IntegralLattice.evenIntermediateCarrierOrderIsoIsotropicSubgroup.{u} {V : Type u}
  [AddCommGroup V] [_root_.Module ℚ V] (L : TauCeti.IntegralLattice V) [L.IsNondegenerate]
  (hL : L.IsEven) :
  { M // TauCeti.IntegralLattice.IntermediateCarrier.IsEven M } ≃o
    { H // (L.discriminantQuadraticModule hL).IsIsotropic H }
```

## Depends on

- [TauCeti.FiniteQuadraticModule](../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](tauceti-integrallattice-discriminantquadraticmod.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.evenIntermediateCarrierOrderIsoIsotropicSubgroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Overlattice/Isotropic.html#TauCeti.IntegralLattice.evenIntermediateCarrierOrderIsoIsotropicSubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.evenIntermediateCarrierOrderIsoIsotropicSubgroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Overlattice/Isotropic.html#TauCeti.IntegralLattice.evenIntermediateCarrierOrderIsoIsotropicSubgroup)
- [Source of `TauCeti.IntegralLattice.evenIntermediateCarrierOrderIsoIsotropicSubgroup` in TauCeti/LinearAlgebra/IntegralLattice/Overlattice/Isotropic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/Overlattice/Isotropic.lean#L378)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/IntegralLattices/STATUS.md)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/IntegralLattices/STATUS.md)
