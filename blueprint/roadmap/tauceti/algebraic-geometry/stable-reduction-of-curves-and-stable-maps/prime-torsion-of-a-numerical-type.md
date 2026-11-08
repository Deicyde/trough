---
declaration: theorem
origin: cited
lean: TauCeti.NumericalType.finrank_torsion_le_arithmeticGenus
statement: formalized
proof: formalized
---

# Prime torsion of a numerical type

In a numerical type of genus `g ≥ 2`, every prime
`ℓ > 768g - 768` satisfies `dim_{𝔽_ℓ} Pic(T)[ℓ] ≤ g`. In particular this holds for every prime
`ℓ > 768g`, which is [Stacks, Proposition 55.7.4](https://stacks.math.columbia.edu/tag/0C9X).

```lean
TauCeti.NumericalType.finrank_torsion_le_arithmeticGenus.{u} {T : TauCeti.NumericalType}
  (hg : 2 ≤ T.arithmeticGenus) (ℓ : ℕ) [Fact (Nat.Prime ℓ)]
  (hℓ : 768 * T.arithmeticGenus - 768 < ↑ℓ) :
  ↑(Module.finrank (ZMod ℓ) ↥(T.torsion ℓ)) ≤ T.arithmeticGenus
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Sylvester's rank inequality](../../number-theory/part-01/heights-units-and-s-units-of-number-fields/part-02/sylvesters-rank-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumericalType.finrank_torsion_le_arithmeticGenus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/StableReduction/Picard/Torsion/Genus/Basic.html#TauCeti.NumericalType.finrank_torsion_le_arithmeticGenus).

## Sources

- [Tau Ceti documentation: `TauCeti.NumericalType.finrank_torsion_le_arithmeticGenus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/StableReduction/Picard/Torsion/Genus/Basic.html#TauCeti.NumericalType.finrank_torsion_le_arithmeticGenus)
- [Source of `TauCeti.NumericalType.finrank_torsion_le_arithmeticGenus` in TauCeti/AlgebraicGeometry/Curves/StableReduction/Picard/Torsion/Genus/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/StableReduction/Picard/Torsion/Genus/Basic.lean#L113)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StableReduction/STATUS.md)
