---
declaration: theorem
origin: cited
lean: TauCeti.exists_eqOn_unitDiscStandardAutomorphismFormula_comp
statement: formalized
proof: formalized
---

# Uniqueness in the Riemann mapping theorem, up to a disc automorphism

If `f` and `g` are
holomorphic injections from an open set `U` onto the open unit disc, then there are `u` on the
unit circle and `a` in the unit disc such that

`g z = u * (f z - a) / (1 - conj a * f z)`

for every `z ∈ U`.

```lean
TauCeti.exists_eqOn_unitDiscStandardAutomorphismFormula_comp {U : Set ℂ} (hU : IsOpen U)
  {f g : ℂ → ℂ} (hf : DifferentiableOn ℂ f U) (hg : DifferentiableOn ℂ g U) (hfi : Set.InjOn f U)
  (hgi : Set.InjOn g U) (hfimage : f '' U = Metric.ball 0 1) (hgimage : g '' U = Metric.ball 0 1) :
  ∃ u a, Set.EqOn g (fun z => ↑u * ((f z - ↑a) / (1 - (starRingEnd ℂ) ↑a * f z))) U
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rouché's theorem for a disc, classical form](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-02/rouches-theorem-for-a-disc-classical-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eqOn_unitDiscStandardAutomorphismFormula_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Uniqueness.html#TauCeti.exists_eqOn_unitDiscStandardAutomorphismFormula_comp).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eqOn_unitDiscStandardAutomorphismFormula_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Uniqueness.html#TauCeti.exists_eqOn_unitDiscStandardAutomorphismFormula_comp)
- [Source of `TauCeti.exists_eqOn_unitDiscStandardAutomorphismFormula_comp` in TauCeti/Analysis/Complex/Conformal/RiemannMapping/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/RiemannMapping/Uniqueness.lean#L52)
