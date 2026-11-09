---
declaration: theorem
origin: cited
lean: TauCeti.ConstructionB.four_le_form_self
statement: formalized
proof: formalized
---

# Construction B vectors have norm at least four

If every nonzero codeword of `C` has
weight at least eight, every nonzero vector of the Construction B carrier has Construction A norm,
the dot product halved, at least `4`.

```lean
TauCeti.ConstructionB.four_le_form_self.{u_1} {ι : Type u_1} [Fintype ι]
  {C : TauCeti.LinearCode (ZMod 2) ι} (hC : ∀ c ∈ C, c ≠ 0 → 8 ≤ hammingNorm c) {x : ι → ℚ}
  (hx : x ∈ TauCeti.ConstructionB.lattice C) (hne : x ≠ 0) :
  4 ≤ ((TauCeti.ConstructionA.form 2) x) x
```

## Depends on

- [TauCeti.ConstructionA.lattice](../algebraic-codes-and-code-lattice-constructions/tauceti-constructiona-lattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ConstructionB.four_le_form_self`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionB/Minimum.html#TauCeti.ConstructionB.four_le_form_self).

## Sources

- [Tau Ceti documentation: `TauCeti.ConstructionB.four_le_form_self`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionB/Minimum.html#TauCeti.ConstructionB.four_le_form_self)
- [Source of `TauCeti.ConstructionB.four_le_form_self` in TauCeti/LinearAlgebra/IntegralLattice/ConstructionB/Minimum.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/ConstructionB/Minimum.lean#L87)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
