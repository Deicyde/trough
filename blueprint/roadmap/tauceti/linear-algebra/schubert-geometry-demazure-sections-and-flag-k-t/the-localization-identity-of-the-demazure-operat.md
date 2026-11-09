---
declaration: theorem
origin: cited
lean: RootPairing.one_sub_single_neg_root_mul_demazureOperator
statement: formalized
proof: formalized
---

# The localization identity of the Demazure operator

`(1 - e^{-αᵢ}) Dᵢ(f) = f - e^{-αᵢ} sᵢ(f)`, where `sᵢ` reindexes `ℤ[M]` along the reflection of
`M`. Equivalently, `Dᵢ(e^x) = (e^x - e^{-αᵢ} e^{sᵢ x}) / (1 - e^{-αᵢ})`.

```lean
RootPairing.one_sub_single_neg_root_mul_demazureOperator.{u_1, u_2, u_3} {ι : Type u_1}
  {M : Type u_2} {N : Type u_3} [AddCommGroup M] [AddCommGroup N] (P : RootPairing ι ℤ M N) (i : ι)
  (f : AddMonoidAlgebra ℤ M) :
  (1 - AddMonoidAlgebra.single (-P.root i) 1) * (P.demazureOperator i) f =
    f -
      AddMonoidAlgebra.single (-P.root i) 1 *
        (AddMonoidAlgebra.mapDomainRingEquiv ℤ (P.reflection i).toAddEquiv) f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`RootPairing.one_sub_single_neg_root_mul_demazureOperator`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/Basic.html#RootPairing.one_sub_single_neg_root_mul_demazureOperator).

## Sources

- [Tau Ceti documentation: `RootPairing.one_sub_single_neg_root_mul_demazureOperator`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/Basic.html#RootPairing.one_sub_single_neg_root_mul_demazureOperator)
- [Source of `RootPairing.one_sub_single_neg_root_mul_demazureOperator` in TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/Basic.lean#L150)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchubertGeometry/STATUS.md)
