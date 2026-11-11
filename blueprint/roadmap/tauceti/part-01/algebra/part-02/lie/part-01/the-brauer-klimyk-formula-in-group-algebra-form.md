---
declaration: theorem
origin: cited
lean: TauCeti.isotypicMultiplicity_tensor_eq_coeff_formalCharacter_mul_weylNumerator, TauCeti.isotypicMultiplicity_tensor_eq_sum_weylSign_mul_formalCharacter_coeff
statement: formalized
proof: formalized
---

# The Brauer–Klimyk formula, in group-algebra form

for dominant integral weights `lam` and
`nu` and a finite-dimensional `L`-module `M`, the multiplicity of `L(nu)` in `L(lam) ⊗ M` is the
coefficient at `nu` of `ch M · N(lam)`.

This combines Weyl-alternating inversion
(`TauCeti.coeff_formalCharacter_mul_weylDenominator_eq_isotypicMultiplicity`) on `L(lam) ⊗ M`,
multiplicativity of formal characters (`TauCeti.formalCharacter_tensor`), and the Weyl character
formula `ch L(lam) · Δ = N(lam)`.

```lean
TauCeti.isotypicMultiplicity_tensor_eq_coeff_formalCharacter_mul_weylNumerator.{u, v, w}
  {K : Type u} {L : Type v} [Field K] [CharZero K] [IsAlgClosed K] [LieRing L] [LieAlgebra K L]
  [LieAlgebra.IsKilling K L] [FiniteDimensional K L] {H : LieSubalgebra K L} [H.IsCartanSubalgebra]
  (b : (LieAlgebra.IsKilling.rootSystem H).Base) {M : Type w} [AddCommGroup M] [_root_.Module K M]
  [LieRingModule L M] [LieModule K L M] [FiniteDimensional K M]
  [Fintype ↥(LieAlgebra.IsKilling.rootSystem H).weylGroup] {lam nu : Module.Dual K ↥H}
  (hlam : TauCeti.IsDominantIntegral b lam) (hnu : TauCeti.IsDominantIntegral b nu) :
  ↑(LieModule.isotypicMultiplicity K L (TensorProduct K (TauCeti.irreducibleQuotient b lam) M)
        (TauCeti.irreducibleQuotient b nu)) =
    (TauCeti.formalCharacter K (↥H) M *
          TauCeti.weylNumerator (LieAlgebra.IsKilling.rootSystem H) b lam).coeff
      nu
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy-Schwarz against a majorant](../../../../linear-algebra/bilinear-form/cauchy-schwarz-against-a-majorant.md)
- [Freudenthal's multiplicity formula](freudenthals-multiplicity-formula.md)
- [The lattice form of Weyl's theorem](the-lattice-form-of-weyls-theorem.md)
- [Schur's lemma for Lie modules](../part-02/schurs-lemma-for-lie-modules.md)
- [The Weyl character formula](../part-02/the-weyl-character-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isotypicMultiplicity_tensor_eq_coeff_formalCharacter_mul_weylNumerator`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/RacahSpeiser.html#TauCeti.isotypicMultiplicity_tensor_eq_coeff_formalCharacter_mul_weylNumerator).

## Other forms

**The Brauer–Klimyk formula, expanded over the Weyl group.** Formalized in Tau Ceti as [`TauCeti.isotypicMultiplicity_tensor_eq_sum_weylSign_mul_formalCharacter_coeff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/RacahSpeiser.html#TauCeti.isotypicMultiplicity_tensor_eq_sum_weylSign_mul_formalCharacter_coeff).

```lean
TauCeti.isotypicMultiplicity_tensor_eq_sum_weylSign_mul_formalCharacter_coeff.{u, v, w} {K : Type u}
  {L : Type v} [Field K] [CharZero K] [IsAlgClosed K] [LieRing L] [LieAlgebra K L]
  [LieAlgebra.IsKilling K L] [FiniteDimensional K L] {H : LieSubalgebra K L} [H.IsCartanSubalgebra]
  (b : (LieAlgebra.IsKilling.rootSystem H).Base) {M : Type w} [AddCommGroup M] [_root_.Module K M]
  [LieRingModule L M] [LieModule K L M] [FiniteDimensional K M]
  [Fintype ↥(LieAlgebra.IsKilling.rootSystem H).weylGroup] {lam nu : Module.Dual K ↥H}
  (hlam : TauCeti.IsDominantIntegral b lam) (hnu : TauCeti.IsDominantIntegral b nu) :
  ↑(LieModule.isotypicMultiplicity K L (TensorProduct K (TauCeti.irreducibleQuotient b lam) M)
        (TauCeti.irreducibleQuotient b nu)) =
    ∑ w,
      ↑((TauCeti.weylSign (LieAlgebra.IsKilling.rootSystem H) b) w) *
        (TauCeti.formalCharacter K (↥H) M).coeff
          (nu - TauCeti.dotAction (LieAlgebra.IsKilling.rootSystem H) b w lam)
```

## Sources

- [Tau Ceti documentation: `TauCeti.isotypicMultiplicity_tensor_eq_coeff_formalCharacter_mul_weylNumerator`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/RacahSpeiser.html#TauCeti.isotypicMultiplicity_tensor_eq_coeff_formalCharacter_mul_weylNumerator)
- [Source of `TauCeti.isotypicMultiplicity_tensor_eq_coeff_formalCharacter_mul_weylNumerator` in TauCeti/Algebra/Lie/HighestWeight/RacahSpeiser.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/HighestWeight/RacahSpeiser.lean#L71)
