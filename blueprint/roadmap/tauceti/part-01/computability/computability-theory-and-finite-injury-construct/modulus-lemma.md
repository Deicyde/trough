---
declaration: theorem
origin: cited
lean: TauCeti.Approximation.computableIn_iff_exists_isModulus_of_rePred
statement: formalized
proof: formalized
---

# Modulus Lemma

For a c.e. oracle `Z`, a total natural-valued function is computable in
`Z` exactly when it has a computable approximation with a `Z`-computable modulus. In particular,
no computable modulus is asserted when `Z` itself is noncomputable.

```lean
TauCeti.Approximation.computableIn_iff_exists_isModulus_of_rePred {g : ℕ → ℕ} {Z : Set ℕ}
  (hZ : REPred fun x => x ∈ Z) :
  ComputableIn {Z.oracle} g ↔
    ∃ f m, Computable₂ f ∧ ComputableIn {Z.oracle} m ∧ TauCeti.Approximation.IsModulus f g m
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Adequacy](adequacy.md)
- [TauCeti.Oracle.Single.Code](tauceti-oracle-single-code.md)
- [The use principle](the-use-principle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Approximation.computableIn_iff_exists_isModulus_of_rePred`](https://taucetiproject.org/docs/TauCeti/Computability/Approximation/CEOracle.html#TauCeti.Approximation.computableIn_iff_exists_isModulus_of_rePred).

## Sources

- [Tau Ceti documentation: `TauCeti.Approximation.computableIn_iff_exists_isModulus_of_rePred`](https://taucetiproject.org/docs/TauCeti/Computability/Approximation/CEOracle.html#TauCeti.Approximation.computableIn_iff_exists_isModulus_of_rePred)
- [Source of `TauCeti.Approximation.computableIn_iff_exists_isModulus_of_rePred` in TauCeti/Computability/Approximation/CEOracle.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Computability/Approximation/CEOracle.lean#L164)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
