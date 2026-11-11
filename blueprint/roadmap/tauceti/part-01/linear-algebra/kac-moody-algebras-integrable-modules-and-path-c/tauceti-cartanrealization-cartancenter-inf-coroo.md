---
declaration: theorem
origin: cited
lean: TauCeti.CartanRealization.cartanCenter_inf_corootSpan
statement: formalized
proof: formalized
---

# TauCeti.CartanRealization.cartanCenter_inf_corootSpan

The intersection of the Cartan center and the coroot span is exactly the image of the
left kernel of the matrix under the coroot embedding.

```lean
TauCeti.CartanRealization.cartanCenter_inf_corootSpan.{u_1, u_2, u_3} {I : Type u_1} {K : Type u_2}
  {H : Type u_3} [Fintype I] [Field K] [AddCommGroup H] [_root_.Module K H] {A : Matrix I I K}
  (R : TauCeti.CartanRealization A H) :
  R.cartanCenter ⊓ R.corootSpan = Submodule.map R.corootMap A.transpose.mulVecLin.ker
```

## Depends on

- [TauCeti.CartanRealization](tauceti-cartanrealization.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CartanRealization.cartanCenter_inf_corootSpan`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.html#TauCeti.CartanRealization.cartanCenter_inf_corootSpan).

## Sources

- [Tau Ceti documentation: `TauCeti.CartanRealization.cartanCenter_inf_corootSpan`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.html#TauCeti.CartanRealization.cartanCenter_inf_corootSpan)
- [Source of `TauCeti.CartanRealization.cartanCenter_inf_corootSpan` in TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean#L150)
- [Tau Ceti roadmap status: Kac–Moody algebras, integrable modules and path crystals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/KacMoody/STATUS.md)
