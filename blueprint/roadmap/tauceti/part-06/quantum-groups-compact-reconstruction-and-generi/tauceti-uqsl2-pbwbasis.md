---
declaration: def
origin: cited
lean: TauCeti.UqSl2.pbwBasis
statement: formalized
---

# TauCeti.UqSl2.pbwBasis

The Poincaré--Birkhoff--Witt basis of `UqSl2 q`, indexed by the exponents `(a, b, c)`
of the ordered monomial `F ^ a * K ^ b * E ^ c`.

```lean
TauCeti.UqSl2.pbwBasis (q : ℂ) [Fact (q ≠ 0)] : Module.Basis (ℕ × ℤ × ℕ) ℂ (TauCeti.UqSl2 q)
```

## Depends on

- [TauCeti.OreExtension](tauceti-oreextension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.pbwBasis`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/PBW.html#TauCeti.UqSl2.pbwBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.pbwBasis`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/PBW.html#TauCeti.UqSl2.pbwBasis)
- [Source of `TauCeti.UqSl2.pbwBasis` in TauCeti/QuantumGroups/UqSl2/PBW.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/QuantumGroups/UqSl2/PBW.lean#L182)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuantumGroups/STATUS.md)
