---
declaration: theorem
origin: cited
lean: TauCeti.tensorMultiplicity_eq_coeff_formalCharacter_mul_weylNumerator, TauCeti.tensorMultiplicity_eq_sum_weylSign_mul_formalCharacter_coeff
statement: formalized
proof: formalized
---

# The Racah–Speiser formula, in group-algebra form

for dominant integral weights `lam`,
`mu`, and `nu`, the tensor multiplicity `c^nu_{lam mu}` of `L(nu)` in `L(lam) ⊗ L(mu)` is the
coefficient at `nu` of `ch L(mu) · N(lam)`.

This is the Brauer–Klimyk formula
`TauCeti.isotypicMultiplicity_tensor_eq_coeff_formalCharacter_mul_weylNumerator` for
`M = L(mu)`.

```lean
TauCeti.tensorMultiplicity_eq_coeff_formalCharacter_mul_weylNumerator.{u, v} {K : Type u}
  {L : Type v} [Field K] [CharZero K] [IsAlgClosed K] [LieRing L] [LieAlgebra K L]
  [LieAlgebra.IsKilling K L] [FiniteDimensional K L] {H : LieSubalgebra K L} [H.IsCartanSubalgebra]
  (b : (LieAlgebra.IsKilling.rootSystem H).Base)
  [Fintype ↥(LieAlgebra.IsKilling.rootSystem H).weylGroup] {lam mu nu : Module.Dual K ↥H}
  (hlam : TauCeti.IsDominantIntegral b lam) (hmu : TauCeti.IsDominantIntegral b mu)
  (hnu : TauCeti.IsDominantIntegral b nu) :
  ↑(TauCeti.tensorMultiplicity b lam mu nu) =
    (TauCeti.formalCharacter K (↥H) (TauCeti.irreducibleQuotient b mu) *
          TauCeti.weylNumerator (LieAlgebra.IsKilling.rootSystem H) b lam).coeff
      nu
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Brauer–Klimyk formula, in group-algebra form](the-brauer-klimyk-formula-in-group-algebra-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tensorMultiplicity_eq_coeff_formalCharacter_mul_weylNumerator`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/RacahSpeiser.html#TauCeti.tensorMultiplicity_eq_coeff_formalCharacter_mul_weylNumerator).

## Other forms

**The Racah–Speiser formula, expanded over the Weyl group.** Formalized in Tau Ceti as [`TauCeti.tensorMultiplicity_eq_sum_weylSign_mul_formalCharacter_coeff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/RacahSpeiser.html#TauCeti.tensorMultiplicity_eq_sum_weylSign_mul_formalCharacter_coeff).

```lean
TauCeti.tensorMultiplicity_eq_sum_weylSign_mul_formalCharacter_coeff.{u, v} {K : Type u}
  {L : Type v} [Field K] [CharZero K] [IsAlgClosed K] [LieRing L] [LieAlgebra K L]
  [LieAlgebra.IsKilling K L] [FiniteDimensional K L] {H : LieSubalgebra K L} [H.IsCartanSubalgebra]
  (b : (LieAlgebra.IsKilling.rootSystem H).Base)
  [Fintype ↥(LieAlgebra.IsKilling.rootSystem H).weylGroup] {lam mu nu : Module.Dual K ↥H}
  (hlam : TauCeti.IsDominantIntegral b lam) (hmu : TauCeti.IsDominantIntegral b mu)
  (hnu : TauCeti.IsDominantIntegral b nu) :
  ↑(TauCeti.tensorMultiplicity b lam mu nu) =
    ∑ w,
      ↑((TauCeti.weylSign (LieAlgebra.IsKilling.rootSystem H) b) w) *
        (TauCeti.formalCharacter K (↥H) (TauCeti.irreducibleQuotient b mu)).coeff
          (nu - TauCeti.dotAction (LieAlgebra.IsKilling.rootSystem H) b w lam)
```

## Sources

- [Tau Ceti documentation: `TauCeti.tensorMultiplicity_eq_coeff_formalCharacter_mul_weylNumerator`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/RacahSpeiser.html#TauCeti.tensorMultiplicity_eq_coeff_formalCharacter_mul_weylNumerator)
- [Source of `TauCeti.tensorMultiplicity_eq_coeff_formalCharacter_mul_weylNumerator` in TauCeti/Algebra/Lie/HighestWeight/RacahSpeiser.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/HighestWeight/RacahSpeiser.lean#L115)
