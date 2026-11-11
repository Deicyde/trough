---
declaration: theorem
origin: cited
lean: TauCeti.exists_simple_low_code
statement: formalized
proof: formalized
---

# TauCeti.exists_simple_low_code

There is an ordinary partial computable program whose domain is simple and low.

```lean
TauCeti.exists_simple_low_code : ∃ c, {x | (c.eval x).Dom}.Simple ∧ {x | (c.eval x).Dom}.Low
```

## Depends on

- [Set.Low](set-low.md)

## Proof depends on

- [The constructed set is simple](the-constructed-set-is-simple.md)
- [TauCeti.low_lowSimpleSet](tauceti-low-lowsimpleset.md)
- [TauCeti.Oracle.Single.Code](tauceti-oracle-single-code.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_simple_low_code`](https://taucetiproject.org/docs/TauCeti/Computability/Simple/Lowness.html#TauCeti.exists_simple_low_code).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_simple_low_code`](https://taucetiproject.org/docs/TauCeti/Computability/Simple/Lowness.html#TauCeti.exists_simple_low_code)
- [Source of `TauCeti.exists_simple_low_code` in TauCeti/Computability/Simple/Lowness.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Computability/Simple/Lowness.lean#L132)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
