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
- [Source of `TauCeti.exists_simple_low_code` in TauCeti/Computability/Simple/Lowness.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Computability/Simple/Lowness.lean#L132)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
