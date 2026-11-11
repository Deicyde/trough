---
declaration: theorem
origin: cited
lean: TauCeti.Oracle.Single.Code.evaln_eq_some_of_eqOn
statement: formalized
proof: formalized
---

# The use principle

A successful run against the answers `σ` succeeds with the same output
and use against any answers `τ` agreeing with `σ` below its use.

```lean
TauCeti.Oracle.Single.Code.evaln_eq_some_of_eqOn {σ τ : ℕ → Option ℕ} {k : ℕ}
  {c : TauCeti.Oracle.Single.Code} {n : ℕ} {d : TauCeti.Oracle.Single.Code.Halt} :
  TauCeti.Oracle.Single.Code.evaln σ k c n = some d →
    Set.EqOn σ τ (Set.Iio d.use) → TauCeti.Oracle.Single.Code.evaln τ k c n = some d
```

## Depends on

- [TauCeti.Oracle.Single.Code](tauceti-oracle-single-code.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Oracle.Single.Code.evaln_eq_some_of_eqOn`](https://taucetiproject.org/docs/TauCeti/Computability/SingleOracle/Evaln.html#TauCeti.Oracle.Single.Code.evaln_eq_some_of_eqOn).

## Sources

- [Tau Ceti documentation: `TauCeti.Oracle.Single.Code.evaln_eq_some_of_eqOn`](https://taucetiproject.org/docs/TauCeti/Computability/SingleOracle/Evaln.html#TauCeti.Oracle.Single.Code.evaln_eq_some_of_eqOn)
- [Source of `TauCeti.Oracle.Single.Code.evaln_eq_some_of_eqOn` in TauCeti/Computability/SingleOracle/Evaln.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Computability/SingleOracle/Evaln.lean#L359)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
