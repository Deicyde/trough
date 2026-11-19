---
declaration: theorem
origin: cited
lean: TauCeti.exists_mem_pbwFiltration_hcProjectionLinear_eq, TauCeti.exists_mem_pbwFiltration_hcProjection_eq
statement: formalized
proof: formalized
---

# Harish-Chandra surjectivity with a degree bound

A Weyl invariant `q ∈ S(H)^W` of degree
at most `n` is the linear Harish-Chandra projection of a central element of `U(L)` of PBW degree
at most `n`.

```lean
TauCeti.exists_mem_pbwFiltration_hcProjectionLinear_eq.{v} {K : Type} {L : Type v} [Field K]
  [CharZero K] [IsAlgClosed K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L]
  [FiniteDimensional K L] {H : LieSubalgebra K L} [H.IsCartanSubalgebra]
  (b : (LieAlgebra.IsKilling.rootSystem H).Base) {n : ℕ} {q : SymmetricAlgebra K ↥H}
  (hq : q ∈ TauCeti.linearInvariants H)
  (hqn : q ∈ TauCeti.Algebra.wordFiltration (SymmetricAlgebra.ι K ↥H) n) :
  ∃ z,
    ↑z ∈ TauCeti.UniversalEnvelopingAlgebra.pbwFiltration K L n ∧
      (TauCeti.hcProjectionLinear b) z = q
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy-Schwarz against a majorant](../../../../linear-algebra/part-01/bilinear-form/cauchy-schwarz-against-a-majorant.md)
- [The linear-independence half of the Poincaré--Birkhoff--Witt theorem](the-linear-independence-half-of-the-poincare-bir.md)
- [The Poincaré--Birkhoff--Witt theorem](../part-02/the-poincare-birkhoff-witt-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_mem_pbwFiltration_hcProjectionLinear_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Surjective.html#TauCeti.exists_mem_pbwFiltration_hcProjectionLinear_eq).

## Other forms

**Harish-Chandra surjectivity with a degree bound, dot form.** Formalized in Tau Ceti as [`TauCeti.exists_mem_pbwFiltration_hcProjection_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Surjective.html#TauCeti.exists_mem_pbwFiltration_hcProjection_eq).

```lean
TauCeti.exists_mem_pbwFiltration_hcProjection_eq.{v} {K : Type} {L : Type v} [Field K] [CharZero K]
  [IsAlgClosed K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [FiniteDimensional K L]
  {H : LieSubalgebra K L} [H.IsCartanSubalgebra] (b : (LieAlgebra.IsKilling.rootSystem H).Base)
  {n : ℕ} {q : SymmetricAlgebra K ↥H} (hq : q ∈ TauCeti.dotInvariants b)
  (hqn : q ∈ TauCeti.Algebra.wordFiltration (SymmetricAlgebra.ι K ↥H) n) :
  ∃ z, ↑z ∈ TauCeti.UniversalEnvelopingAlgebra.pbwFiltration K L n ∧ (TauCeti.hcProjection b) z = q
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_mem_pbwFiltration_hcProjectionLinear_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Surjective.html#TauCeti.exists_mem_pbwFiltration_hcProjectionLinear_eq)
- [Source of `TauCeti.exists_mem_pbwFiltration_hcProjectionLinear_eq` in TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Surjective.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Surjective.lean#L130)
