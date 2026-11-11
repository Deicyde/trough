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
- [Source of `TauCeti.Oracle.Single.Code.exists_code` in TauCeti/Computability/SingleOracle/Code.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Computability/SingleOracle/Code.lean#L450)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
