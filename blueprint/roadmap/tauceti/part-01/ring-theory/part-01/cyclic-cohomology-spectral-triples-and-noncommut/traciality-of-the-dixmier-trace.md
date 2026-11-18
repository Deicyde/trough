---
declaration: theorem
origin: cited
lean: TauCeti.complexDixmierTrace_comp_comm
statement: formalized
proof: formalized
---

# Traciality of the Dixmier trace

When `ω` is dilation invariant, `Tr_ω(A T) = Tr_ω(T A)`
for every bounded operator `A : E →L[ℂ] E` and every `T` in `L^(1,∞)`.

```lean
TauCeti.complexDixmierTrace_comp_comm.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℂ E] [CompleteSpace E] {ω : TauCeti.GeneralizedLimit}
  (hω : ω.IsDilationInvariant) (A : E →L[ℂ] E) {T : E →L[ℂ] E}
  (hT : T ∈ ((TauCeti.OperatorIdealFamily.logarithmic ℂ).operatorGauge E E).finiteSubmodule) :
  TauCeti.complexDixmierTrace ω (A ∘SL T) = TauCeti.complexDixmierTrace ω (T ∘SL A)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ky Fan triangle inequality](../../../analysis/part-04/operator-ideal/ky-fan-triangle-inequality.md)
- [Ky Fan two-sided ideal inequality](../../../analysis/part-04/operator-ideal/ky-fan-two-sided-ideal-inequality.md)
- [Ky Fan's maximum principle](../../../analysis/part-04/operator-ideal/ky-fans-maximum-principle.md)
- [TauCeti.Complexification](../../../analysis/part-02/one-parameter-semigroups-completely-monotone-and/tauceti-complexification.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.complexDixmierTrace_comp_comm`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Linear.html#TauCeti.complexDixmierTrace_comp_comm).

## Sources

- [Tau Ceti documentation: `TauCeti.complexDixmierTrace_comp_comm`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Linear.html#TauCeti.complexDixmierTrace_comp_comm)
- [Source of `TauCeti.complexDixmierTrace_comp_comm` in TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Linear.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Linear.lean#L467)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
