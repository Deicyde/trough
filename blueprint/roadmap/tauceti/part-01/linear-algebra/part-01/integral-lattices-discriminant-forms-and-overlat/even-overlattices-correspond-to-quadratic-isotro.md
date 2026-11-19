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

- [TauCeti.FiniteQuadraticModule](../../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](tauceti-integrallattice-discriminantquadraticmod.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.evenIntermediateCarrierOrderIsoIsotropicSubgroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Overlattice/Isotropic.html#TauCeti.IntegralLattice.evenIntermediateCarrierOrderIsoIsotropicSubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.evenIntermediateCarrierOrderIsoIsotropicSubgroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Overlattice/Isotropic.html#TauCeti.IntegralLattice.evenIntermediateCarrierOrderIsoIsotropicSubgroup)
- [Source of `TauCeti.IntegralLattice.evenIntermediateCarrierOrderIsoIsotropicSubgroup` in TauCeti/LinearAlgebra/IntegralLattice/Overlattice/Isotropic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/IntegralLattice/Overlattice/Isotropic.lean#L376)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/IntegralLattices/STATUS.md)
