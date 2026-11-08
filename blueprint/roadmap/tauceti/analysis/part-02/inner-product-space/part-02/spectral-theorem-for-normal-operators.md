---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.borelCalculus_restrict_id, LinearMap.exists_orthonormalBasis_apply_eq_smul_of_isStarNormal
statement: formalized
proof: formalized
---

# Spectral theorem for normal operators

The Borel calculus of the coordinate function on
the spectrum is `a` itself, that is, `a = ∫ z dP(z)`.

```lean
ContinuousLinearMap.borelCalculus_restrict_id.{u_1} {H : Type u_1} [NormedAddCommGroup H]
  [InnerProductSpace ℂ H] [CompleteSpace H] (a : H →L[ℂ] H) [IsStarNormal a] :
  a.borelCalculus
      (TauCeti.BoundedBorelFunction.ofContinuousMap
        (ContinuousMap.restrict (spectrum ℂ a) (ContinuousMap.id ℂ))) =
    a
```

## Depends on

- [TauCeti.ProjValMeasure](../../../part-01/operator-theory/part-01/tauceti-projvalmeasure.md)
- [TauCeti.ProjValMeasure.integral](../../../part-01/operator-theory/part-01/tauceti-projvalmeasure-integral.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.borelCalculus_restrict_id`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/BorelCalculus/Basic.html#ContinuousLinearMap.borelCalculus_restrict_id).

## Other forms

**The spectral theorem for normal operators.** Formalized in Tau Ceti as [`LinearMap.exists_orthonormalBasis_apply_eq_smul_of_isStarNormal`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/NormalOperator.html#LinearMap.exists_orthonormalBasis_apply_eq_smul_of_isStarNormal).

```lean
LinearMap.exists_orthonormalBasis_apply_eq_smul_of_isStarNormal.{u_3, u_4} {E : Type u_3}
  [NormedAddCommGroup E] [InnerProductSpace ℂ E] [FiniteDimensional ℂ E] (T : E →ₗ[ℂ] E)
  [IsStarNormal T] {ι : Type u_4} [Fintype ι] (hι : Fintype.card ι = Module.finrank ℂ E) :
  ∃ b μ, ∀ (i : ι), T (b i) = μ i • b i
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.borelCalculus_restrict_id`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/BorelCalculus/Basic.html#ContinuousLinearMap.borelCalculus_restrict_id)
- [Source of `ContinuousLinearMap.borelCalculus_restrict_id` in TauCeti/Analysis/InnerProductSpace/BorelCalculus/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/BorelCalculus/Basic.lean#L110)
