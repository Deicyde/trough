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

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.borelCalculus_restrict_id`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/BorelCalculus/Basic.html#ContinuousLinearMap.borelCalculus_restrict_id).

## Other forms

**The spectral theorem for normal operators.** Formalized in Tau Ceti as [`LinearMap.exists_orthonormalBasis_apply_eq_smul_of_isStarNormal`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/NormalOperator.html#LinearMap.exists_orthonormalBasis_apply_eq_smul_of_isStarNormal).

```lean
LinearMap.exists_orthonormalBasis_apply_eq_smul_of_isStarNormal.{u_1, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℂ E] [FiniteDimensional ℂ E] (T : E →ₗ[ℂ] E)
  [IsStarNormal T] {ι : Type u_3} [Fintype ι] (hι : Fintype.card ι = Module.finrank ℂ E) :
  ∃ b μ, ∀ (i : ι), T (b i) = μ i • b i
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.borelCalculus_restrict_id`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/BorelCalculus/Basic.html#ContinuousLinearMap.borelCalculus_restrict_id)
- [Source of `ContinuousLinearMap.borelCalculus_restrict_id` in TauCeti/Analysis/InnerProductSpace/BorelCalculus/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/BorelCalculus/Basic.lean#L110)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorTheory/STATUS.md)
