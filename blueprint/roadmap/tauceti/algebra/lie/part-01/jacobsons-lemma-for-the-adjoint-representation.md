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

- [Jacobson's lemma on commutators](../../../linear-algebra/other-results/jacobsons-lemma-on-commutators.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isNilpotent_ad_lie_of_lie_lie_eq_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/AdjointAction/CentralizerFiltration.html#TauCeti.isNilpotent_ad_lie_of_lie_lie_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.isNilpotent_ad_lie_of_lie_lie_eq_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/AdjointAction/CentralizerFiltration.html#TauCeti.isNilpotent_ad_lie_of_lie_lie_eq_zero)
- [Source of `TauCeti.isNilpotent_ad_lie_of_lie_lie_eq_zero` in TauCeti/Algebra/Lie/AdjointAction/CentralizerFiltration.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/AdjointAction/CentralizerFiltration.lean#L93)
