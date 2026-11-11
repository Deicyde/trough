---
declaration: theorem
origin: cited
lean: TauCeti.hasWeakKernels_iff_isClosedUnderKernels
statement: formalized
proof: formalized
---

# The Freyd-Auslander criterion

A preadditive category `C` with binary biproducts has weak
kernels exactly when the finitely presented functors `Cᵒᵖ ⥤ AddCommGrpCat` are closed under
kernels in the functor category. For nonempty `C`, this makes `mod C` an abelian category, with
kernels and cokernels computed in the functor category.

```lean
TauCeti.hasWeakKernels_iff_isClosedUnderKernels.{v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasBinaryBiproducts C] :
  CategoryTheory.Limits.HasWeakKernels C ↔
    (TauCeti.isFinitelyPresentedFunctor C).IsClosedUnderKernels
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hasWeakKernels_iff_isClosedUnderKernels`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/FinitelyPresentedFunctor/WeakKernels.html#TauCeti.hasWeakKernels_iff_isClosedUnderKernels).

## Sources

- [Tau Ceti documentation: `TauCeti.hasWeakKernels_iff_isClosedUnderKernels`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/FinitelyPresentedFunctor/WeakKernels.html#TauCeti.hasWeakKernels_iff_isClosedUnderKernels)
- [Source of `TauCeti.hasWeakKernels_iff_isClosedUnderKernels` in TauCeti/CategoryTheory/FinitelyPresentedFunctor/WeakKernels.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/FinitelyPresentedFunctor/WeakKernels.lean#L156)
