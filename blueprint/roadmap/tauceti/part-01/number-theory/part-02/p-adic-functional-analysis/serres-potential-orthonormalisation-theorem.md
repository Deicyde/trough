---
declaration: theorem
origin: cited
lean: TauCeti.isPotentiallyONable_of_discrete_norm
statement: formalized
proof: formalized
---

# Serre's potential orthonormalisation theorem

Every Banach module over a complete
ultrametric norm-one commutative ring with discrete scalar norms and field residue ring is
continuously linearly equivalent to a native model space `C₀(I, R)`. In particular this applies
to complete discretely normed fields. The index type need not be countable.

```lean
TauCeti.isPotentiallyONable_of_discrete_norm.{u_3, u_4} {R : Type u_3} [NormedCommRing R]
  [NormOneClass R] [IsUltrametricDist R] [CompleteSpace R] [(TauCeti.unitBallIdeal R).IsMaximal]
  {E : Type u_4} [NormedAddCommGroup E] [_root_.Module R E] [IsBoundedSMul R E]
  [IsUltrametricDist E] [CompleteSpace E] (ϖ : TauCeti.NormedRing.PseudoUniformizer R)
  (hR : ∀ (a : R), TauCeti.zpowCeil ‖↑ϖ.unit‖ ‖a‖ = ‖a‖) : TauCeti.IsPotentiallyONable R E
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Serre's criterion over a field](../../../analysis/part-01/compact-operators-and-nonarchimedean-fredholm-th/serres-criterion-over-a-field.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isPotentiallyONable_of_discrete_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/DiscreteNorm.html#TauCeti.isPotentiallyONable_of_discrete_norm).

## Sources

- [Tau Ceti documentation: `TauCeti.isPotentiallyONable_of_discrete_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/DiscreteNorm.html#TauCeti.isPotentiallyONable_of_discrete_norm)
- [Source of `TauCeti.isPotentiallyONable_of_discrete_norm` in TauCeti/Analysis/Normed/Module/Bases/DiscreteNorm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/Bases/DiscreteNorm.lean#L63)
