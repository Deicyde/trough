---
declaration: def
origin: cited
lean: IsBaseChange.bilinForm
statement: formalized
---

# IsBaseChange.bilinForm

Extend a bilinear form to an abstract base change, transporting Mathlib's tensor-product
base change along the canonical equivalence.

```lean
IsBaseChange.bilinForm.{u_1, u_2, u_3, u_4} {R : Type u_1} {A : Type u_2} {M : Type u_3}
  {N : Type u_4} [CommSemiring R] [CommSemiring A] [Algebra R A] [AddCommMonoid M]
  [_root_.Module R M] [AddCommMonoid N] [_root_.Module R N] [_root_.Module A N]
  [IsScalarTower R A N] {f : M →ₗ[R] N} (h : IsBaseChange A f) (B : LinearMap.BilinForm R M) :
  LinearMap.BilinForm A N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsBaseChange.bilinForm`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/BilinearForm/BaseChange.html#IsBaseChange.bilinForm).

## Sources

- [Tau Ceti documentation: `IsBaseChange.bilinForm`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/BilinearForm/BaseChange.html#IsBaseChange.bilinForm)
- [Source of `IsBaseChange.bilinForm` in TauCeti/LinearAlgebra/BilinearForm/BaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/BilinearForm/BaseChange.lean#L208)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HodgeStructures/STATUS.md)
