---
declaration: theorem
origin: cited
lean: TauCeti.infinite_totallyRamifiedOfDegree
statement: formalized
proof: formalized
---

# Infinitely many totally ramified extensions in equal characteristic

If `0 < n` and
`(n : K) = 0`, that is, `K` has characteristic `p > 0` with `p ∣ n`, then `σ_K(n)` is infinite:
its discriminant exponents are unbounded.

```lean
TauCeti.infinite_totallyRamifiedOfDegree.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} (hn : 0 < n) (hnK : ↑n = 0) :
  (TauCeti.totallyRamifiedOfDegree K n).Infinite
```

## Depends on

- [TauCeti.totallyRamifiedOfDegree](tauceti-totallyramifiedofdegree.md)

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.infinite_totallyRamifiedOfDegree`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Infinite.html#TauCeti.infinite_totallyRamifiedOfDegree).

## Sources

- [Tau Ceti documentation: `TauCeti.infinite_totallyRamifiedOfDegree`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Infinite.html#TauCeti.infinite_totallyRamifiedOfDegree)
- [Source of `TauCeti.infinite_totallyRamifiedOfDegree` in TauCeti/NumberTheory/LocalField/MassFormula/Infinite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Infinite.lean#L112)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
