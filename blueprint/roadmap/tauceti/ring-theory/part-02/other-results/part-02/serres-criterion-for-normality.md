---
declaration: theorem
origin: cited
lean: TauCeti.forall_isDomain_and_isIntegrallyClosed_iff_satisfiesSerreR_one_and_satisfiesSerreS_two
statement: formalized
proof: formalized
---

# Serre's criterion for normality

A Noetherian ring is normal, that is, every localization
at a prime is an integrally closed domain, if and only if it satisfies `(R_1)` and `(S_2)`.
Stacks, Lemma 10.157.4 (031S).

```lean
TauCeti.forall_isDomain_and_isIntegrallyClosed_iff_satisfiesSerreR_one_and_satisfiesSerreS_two.{u}
  {R : Type u} [CommRing R] [IsNoetherianRing R] :
  (∀ (p : Ideal R) [inst : p.IsPrime],
      IsDomain (Localization.AtPrime p) ∧ IsIntegrallyClosed (Localization.AtPrime p)) ↔
    Ring.SatisfiesSerreR 1 R ∧ Module.SatisfiesSerreS 2 R R
```

## Depends on

- [Module.SatisfiesSerreS](../../../part-01/scheme-stack-cohomology-and-intersection-foundat/module-satisfiesserres.md)
- [Ring.SatisfiesSerreR](../../../part-01/scheme-stack-cohomology-and-intersection-foundat/ring-satisfiesserrer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.forall_isDomain_and_isIntegrallyClosed_iff_satisfiesSerreR_one_and_satisfiesSerreS_two`](https://taucetiproject.org/docs/TauCeti/RingTheory/SerreCondition/Normal.html#TauCeti.forall_isDomain_and_isIntegrallyClosed_iff_satisfiesSerreR_one_and_satisfiesSerreS_two).

## Sources

- [Tau Ceti documentation: `TauCeti.forall_isDomain_and_isIntegrallyClosed_iff_satisfiesSerreR_one_and_satisfiesSerreS_two`](https://taucetiproject.org/docs/TauCeti/RingTheory/SerreCondition/Normal.html#TauCeti.forall_isDomain_and_isIntegrallyClosed_iff_satisfiesSerreR_one_and_satisfiesSerreS_two)
- [Source of `TauCeti.forall_isDomain_and_isIntegrallyClosed_iff_satisfiesSerreR_one_and_satisfiesSerreS_two` in TauCeti/RingTheory/SerreCondition/Normal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/SerreCondition/Normal.lean#L210)
