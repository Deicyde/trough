---
declaration: theorem
origin: cited
lean: TauCeti.AInfinityAlgebra.isIntrinsicallyFormal_of_forall_hochschildVanishesAt
statement: formalized
proof: formalized
---

# Kadeishvili's intrinsic formality criterion

Over a field, a graded algebra `ℋ`, presented
as a minimal `A∞` algebra without operations above arity two, is intrinsically formal when
`HH^{n, 2 - n}(H, H) = 0` for every `n ≥ 3`: every Hochschild cocycle of `ℋ` of suspended degree
one concentrated on the words of length `n` is the Hochschild differential of a cochain of
suspended degree zero concentrated on the words of length `n - 1`.

```lean
TauCeti.AInfinityAlgebra.isIntrinsicallyFormal_of_forall_hochschildVanishesAt.{uK, uA} {K : Type uK}
  {A : Type uA} [Field K] [AddCommGroup A] [_root_.Module K A] {ℋ : TauCeti.AInfinityAlgebra K A}
  (hℋ : ℋ.IsMinimal) (hm : ∀ (n : ℕ), 3 ≤ n → ℋ.m n = 0)
  (hHH : ∀ (n : ℕ) (hn : 3 ≤ n), ℋ.HochschildVanishesAt ⟨n, ⋯⟩) : ℋ.IsIntrinsicallyFormal
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.AInfinityAlgebra.minimalModel](tauceti-ainfinityalgebra-minimalmodel.md)
- [TauCeti.AInfinityAlgebra.transfer](tauceti-ainfinityalgebra-transfer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityAlgebra.isIntrinsicallyFormal_of_forall_hochschildVanishesAt`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/IntrinsicFormality/Criterion.html#TauCeti.AInfinityAlgebra.isIntrinsicallyFormal_of_forall_hochschildVanishesAt).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityAlgebra.isIntrinsicallyFormal_of_forall_hochschildVanishesAt`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/IntrinsicFormality/Criterion.html#TauCeti.AInfinityAlgebra.isIntrinsicallyFormal_of_forall_hochschildVanishesAt)
- [Source of `TauCeti.AInfinityAlgebra.isIntrinsicallyFormal_of_forall_hochschildVanishesAt` in TauCeti/Algebra/Homology/AInfinity/Algebra/IntrinsicFormality/Criterion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/AInfinity/Algebra/IntrinsicFormality/Criterion.lean#L198)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGAInfinity/STATUS.md)
