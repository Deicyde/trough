---
declaration: theorem
origin: cited
lean: TauCeti.isNilpotent_ad_lie_of_lie_lie_eq_zero
statement: formalized
proof: formalized
---

# Jacobson's lemma for the adjoint representation

In a finite-dimensional Lie algebra over
a field of characteristic zero, if `⁅e, ⁅e, a⁆⁆ = 0` then `ad ⁅e, a⁆` is nilpotent. In particular
every element of `ker (ad e) ⊓ [e, L]` is `ad`-nilpotent.

```lean
TauCeti.isNilpotent_ad_lie_of_lie_lie_eq_zero.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] {e a : L}
  (h : ⁅e, ⁅e, a⁆⁆ = 0) : IsNilpotent ((LieAlgebra.ad K L) ⁅e, a⁆)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobson's lemma on commutators](../../../../linear-algebra/part-02/other-results/jacobsons-lemma-on-commutators.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isNilpotent_ad_lie_of_lie_lie_eq_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/AdjointAction/CentralizerFiltration.html#TauCeti.isNilpotent_ad_lie_of_lie_lie_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.isNilpotent_ad_lie_of_lie_lie_eq_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/AdjointAction/CentralizerFiltration.html#TauCeti.isNilpotent_ad_lie_of_lie_lie_eq_zero)
- [Source of `TauCeti.isNilpotent_ad_lie_of_lie_lie_eq_zero` in TauCeti/Algebra/Lie/AdjointAction/CentralizerFiltration.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/AdjointAction/CentralizerFiltration.lean#L105)
