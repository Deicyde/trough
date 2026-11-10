---
declaration: theorem
origin: cited
lean: RootPairing.demazureOperator_demazureOperator
statement: formalized
proof: formalized
---

# RootPairing.demazureOperator_demazureOperator

**The Demazure operator is idempotent**, `Dᵢ² = Dᵢ`.

```lean
RootPairing.demazureOperator_demazureOperator.{u_1, u_2, u_3} {ι : Type u_1} {M : Type u_2}
  {N : Type u_3} [AddCommGroup M] [AddCommGroup N] (P : RootPairing ι ℤ M N) (i : ι)
  (f : AddMonoidAlgebra ℤ M) :
  (P.demazureOperator i) ((P.demazureOperator i) f) = (P.demazureOperator i) f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [RootPairing.one_sub_single_neg_root_mul_demazureOperator](rootpairing-one-sub-single-neg-root-mul-demazure.md)

## Lean

Formalized in Tau Ceti as [`RootPairing.demazureOperator_demazureOperator`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/Basic.html#RootPairing.demazureOperator_demazureOperator).

## Sources

- [Tau Ceti documentation: `RootPairing.demazureOperator_demazureOperator`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/Basic.html#RootPairing.demazureOperator_demazureOperator)
- [Source of `RootPairing.demazureOperator_demazureOperator` in TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/Basic.lean#L230)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchubertGeometry/STATUS.md)
