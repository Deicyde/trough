---
declaration: theorem
origin: cited
lean: TauCeti.Approximation.exists_rePred_turingEquivalent_oracle_iff_exists_isModulus, TauCeti.Approximation.exists_rePred_turingEquivalent_iff_exists_isModulus, TauCeti.Approximation.exists_rePred_turingEquivalent_graph_iff_exists_isModulus
statement: formalized
proof: formalized
---

# Soare's criterion for sets

A set is Turing equivalent to a c.e. set exactly when its
characteristic function has a computable approximation with a modulus computable from the set.

```lean
TauCeti.Approximation.exists_rePred_turingEquivalent_oracle_iff_exists_isModulus {A : Set ℕ} :
  (∃ U, (REPred fun x => x ∈ U) ∧ TuringEquivalent A.oracle U.oracle) ↔
    ∃ f m,
      Computable₂ f ∧
        ComputableIn {A.oracle} m ∧ TauCeti.Approximation.IsModulus f (A.indicator 1) m
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Modulus Lemma](../computability-theory-and-finite-injury-construct/modulus-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Approximation.exists_rePred_turingEquivalent_oracle_iff_exists_isModulus`](https://taucetiproject.org/docs/TauCeti/Computability/Approximation/CEDegree.html#TauCeti.Approximation.exists_rePred_turingEquivalent_oracle_iff_exists_isModulus).

## Other forms

**Soare's criterion for c.e. degree.** Formalized in Tau Ceti as [`TauCeti.Approximation.exists_rePred_turingEquivalent_iff_exists_isModulus`](https://taucetiproject.org/docs/TauCeti/Computability/Approximation/CEDegree.html#TauCeti.Approximation.exists_rePred_turingEquivalent_iff_exists_isModulus).

```lean
TauCeti.Approximation.exists_rePred_turingEquivalent_iff_exists_isModulus {g : ℕ → ℕ} :
  (∃ U, (REPred fun x => x ∈ U) ∧ TuringEquivalent (fun x => Part.some (g x)) U.oracle) ↔
    ∃ f m,
      Computable₂ f ∧
        ComputableIn {fun x => Part.some (g x)} m ∧ TauCeti.Approximation.IsModulus f g m
```

**Soare's criterion through graph coding.** Formalized in Tau Ceti as [`TauCeti.Approximation.exists_rePred_turingEquivalent_graph_iff_exists_isModulus`](https://taucetiproject.org/docs/TauCeti/Computability/Approximation/CEDegree.html#TauCeti.Approximation.exists_rePred_turingEquivalent_graph_iff_exists_isModulus).

```lean
TauCeti.Approximation.exists_rePred_turingEquivalent_graph_iff_exists_isModulus {g : ℕ → ℕ} :
  (∃ U,
      (REPred fun x => x ∈ U) ∧
        TuringEquivalent (Nat.unpair ⁻¹' Function.graph g).oracle U.oracle) ↔
    ∃ f m,
      Computable₂ f ∧
        ComputableIn {(Nat.unpair ⁻¹' Function.graph g).oracle} m ∧
          TauCeti.Approximation.IsModulus f g m
```

## Sources

- [Tau Ceti documentation: `TauCeti.Approximation.exists_rePred_turingEquivalent_oracle_iff_exists_isModulus`](https://taucetiproject.org/docs/TauCeti/Computability/Approximation/CEDegree.html#TauCeti.Approximation.exists_rePred_turingEquivalent_oracle_iff_exists_isModulus)
- [Source of `TauCeti.Approximation.exists_rePred_turingEquivalent_oracle_iff_exists_isModulus` in TauCeti/Computability/Approximation/CEDegree.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Computability/Approximation/CEDegree.lean#L123)
