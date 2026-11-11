---
declaration: def
origin: cited
lean: TauCeti.CommHopfAlgCat.kernelFppfQuotientIso
statement: formalized
---

# The fppf first isomorphism theorem for affine groups

If `f : H ⟶ K` is faithfully flat
and of finite presentation, then the fppf quotient of `Spec K` by the kernel of the represented
homomorphism `Spec K ⟶ Spec H` is represented by `Spec H`.

```lean
TauCeti.CommHopfAlgCat.kernelFppfQuotientIso.{u} {R : Type u} [CommRing R] {H K : CommHopfAlgCat R}
  (f : H ⟶ K) (hflat : (↑(CommHopfAlgCat.Hom.hom f)).FaithfullyFlat)
  (hfp : (↑(CommHopfAlgCat.Hom.hom f)).FinitePresentation) :
  TauCeti.CommHopfAlgCat.fppfQuotientSheaf K (TauCeti.CommHopfAlgCat.kernelHopfIdeal f) ⋯ ≅
    TauCeti.CommHopfAlgCat.pointsFppfGroupObject H
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CommHopfAlgCat.kernelFppfQuotientIso`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Kernel.html#TauCeti.CommHopfAlgCat.kernelFppfQuotientIso).

## Sources

- [Tau Ceti documentation: `TauCeti.CommHopfAlgCat.kernelFppfQuotientIso`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Kernel.html#TauCeti.CommHopfAlgCat.kernelFppfQuotientIso)
- [Source of `TauCeti.CommHopfAlgCat.kernelFppfQuotientIso` in TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Kernel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Kernel.lean#L201)
