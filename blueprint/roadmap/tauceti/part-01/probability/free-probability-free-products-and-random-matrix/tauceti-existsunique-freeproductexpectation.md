---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_freeProductExpectation
statement: formalized
proof: formalized
---

# TauCeti.existsUnique_freeProductExpectation

Existence and uniqueness of the universal free-product expectation on
`LinearAlgebra.FreeProduct R A`.

```lean
TauCeti.existsUnique_freeProductExpectation.{u_1, u_2, u_3} {I : Type u_1} {R : Type u_2}
  [DecidableEq I] [CommRing R] {A : I → Type u_3} [(i : I) → Ring (A i)] [(i : I) → Algebra R (A i)]
  (φ : (i : I) → A i →ₗ[R] R) (hφ : ∀ (i : I), (φ i) 1 = 1) :
  ∃! ψ,
    ψ 1 = 1 ∧
      (TauCeti.IsFreelyIndependent ψ fun i => (LinearAlgebra.FreeProduct.ι R A i).range) ∧
        ∀ (i : I), ψ ∘ₗ (LinearAlgebra.FreeProduct.ι R A i).toLinearMap = φ i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_freeProductExpectation`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/FreeProduct/Basic.html#TauCeti.existsUnique_freeProductExpectation).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_freeProductExpectation`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/FreeProduct/Basic.html#TauCeti.existsUnique_freeProductExpectation)
- [Source of `TauCeti.existsUnique_freeProductExpectation` in TauCeti/Probability/FreeProbability/FreeProduct/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/FreeProbability/FreeProduct/Basic.lean#L154)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
