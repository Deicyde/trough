---
declaration: theorem
origin: cited
lean: ContDiffAt.finrank_genEigenspace_shapeOperator_neg
statement: formalized
proof: formalized
---

# Paired principal curvatures

For a `C²` holomorphic map, multiplication by `I` identifies
the generalized `κ`- and `-κ`-eigenspaces of each shape operator, so they have the same
dimension. For `k = 1` these are the geometric multiplicities of the principal curvatures `κ`
and `-κ`.

```lean
ContDiffAt.finrank_genEigenspace_shapeOperator_neg.{u_1, u_2} {V : Type u_1} {E : Type u_2}
  [NormedAddCommGroup V] [NormedSpace ℂ V] [FiniteDimensional ℂ V] [NormedAddCommGroup E]
  [InnerProductSpace ℂ E] {i : V → E} {x : V} (hi : ContDiffAt ℂ 2 i x) (ν : E) (κ : ℝ) (k : ℕ∞) :
  Module.finrank ℝ ↥(((TauCeti.shapeOperator i x ν).genEigenspace (-κ)) k) =
    Module.finrank ℝ ↥(((TauCeti.shapeOperator i x ν).genEigenspace κ) k)
```

## Depends on

- [TauCeti.shapeOperator](tauceti-shapeoperator.md)

## Lean

Formalized in Tau Ceti as [`ContDiffAt.finrank_genEigenspace_shapeOperator_neg`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ShapeOperator.html#ContDiffAt.finrank_genEigenspace_shapeOperator_neg).

## Sources

- [Tau Ceti documentation: `ContDiffAt.finrank_genEigenspace_shapeOperator_neg`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ShapeOperator.html#ContDiffAt.finrank_genEigenspace_shapeOperator_neg)
- [Source of `ContDiffAt.finrank_genEigenspace_shapeOperator_neg` in TauCeti/Analysis/InnerProductSpace/ShapeOperator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/ShapeOperator.lean#L293)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
