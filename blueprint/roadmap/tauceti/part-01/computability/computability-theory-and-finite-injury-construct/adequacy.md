---
declaration: theorem
origin: cited
lean: TauCeti.Oracle.Single.Code.exists_code
statement: formalized
proof: formalized
---

# Adequacy

For every oracle `O`, a partial function is recursive in `O` exactly when some
program computes it relative to `O`.

```lean
TauCeti.Oracle.Single.Code.exists_code {O f : ℕ →. ℕ} :
  Nat.RecursiveIn {O} f ↔ ∃ c, TauCeti.Oracle.Single.Code.eval O c = f
```

## Depends on

- [TauCeti.Oracle.Single.Code](tauceti-oracle-single-code.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Oracle.Single.Code.exists_code`](https://taucetiproject.org/docs/TauCeti/Computability/SingleOracle/Code.html#TauCeti.Oracle.Single.Code.exists_code).

## Sources

- [Tau Ceti documentation: `TauCeti.Oracle.Single.Code.exists_code`](https://taucetiproject.org/docs/TauCeti/Computability/SingleOracle/Code.html#TauCeti.Oracle.Single.Code.exists_code)
- [Source of `TauCeti.Oracle.Single.Code.exists_code` in TauCeti/Computability/SingleOracle/Code.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Computability/SingleOracle/Code.lean#L448)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
