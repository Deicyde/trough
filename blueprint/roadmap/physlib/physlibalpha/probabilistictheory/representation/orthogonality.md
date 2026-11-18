---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.rationalCircle, ProbabilisticTheory.QuantumMechanics.rationalCircle_eq_zero, ProbabilisticTheory.QuantumMechanics.exists_character_apply_ne_one, ProbabilisticTheory.QuantumMechanics.dualHaar, ProbabilisticTheory.QuantumMechanics.integral_character_dualHaar
statement: formalized
proof: formalized
---

# Orthogonality of characters

The module `PhyslibAlpha.ProbabilisticTheory.Representation.Orthogonality`, [PhyslibAlpha/ProbabilisticTheory/Representation/Orthogonality.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Orthogonality.lean): 7 declarations (2 instances with no name), 4 with a docstring.

> Characters separate the points of a discrete abelian group, and the normalized Haar measure of the
> dual group makes the characters orthogonal.

## i. Overview

> For a discrete abelian group `G` and `g ≠ 0` there is a unitary character `χ` of `G` with
> `χ(g) ≠ 1`. This comes from the injectivity of the circle: a character into `ℚ/ℤ` separating `g`
> from `0`, composed with the injection `ℚ/ℤ → S¹`, `q ↦ e^{2πi q}`. The Pontryagin dual `Ĝ` is a
> compact abelian group, so it carries a Haar probability measure `μ`. The evaluation `χ ↦ χ(g)` is a
> nontrivial character of `Ĝ` for `g ≠ 0`, so by translation invariance
> `∫ χ(g) dμ(χ) = 0`, and `= 1` for `g = 0`: the characters are orthonormal.

## ii. Key results

> - `exists_character_apply_ne_one` : characters separate points.
> - `dualHaar` : the Haar probability measure of the dual group.
> - `integral_character_dualHaar` : `∫ χ(g) dμ(χ) = 1` for `g = 0` and `0` otherwise.

## iv. References

> * None.

## A. Characters separate points

**`ProbabilisticTheory.QuantumMechanics.rationalCircle`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Orthogonality.lean#L58).

> The injection of `ℚ/ℤ` into the circle, `q ↦ e^{2πi q}`.

```lean
def rationalCircle : AddCircle (1 : ℚ) →+ Additive Circle
```

**`ProbabilisticTheory.QuantumMechanics.rationalCircle_eq_zero`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Orthogonality.lean#L71).

```lean
lemma rationalCircle_eq_zero {x : AddCircle (1 : ℚ)} (h : rationalCircle x = 0) : x = 0
```

**`ProbabilisticTheory.QuantumMechanics.exists_character_apply_ne_one`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Orthogonality.lean#L89).

> **Characters separate the points of a discrete abelian group.**

```lean
lemma exists_character_apply_ne_one [TopologicalSpace G] [DiscreteTopology G] {g : G}
    (hg : g ≠ 0) : ∃ χ : PontryaginDual (Multiplicative G), χ (Multiplicative.ofAdd g) ≠ 1
```

## B. The Haar measure of the dual group

**`ProbabilisticTheory.QuantumMechanics.dualHaar`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Orthogonality.lean#L111).

> The normalized Haar measure of the compact dual group.

```lean
def dualHaar : Measure (PontryaginDual (Multiplicative G))
```

**An instance with no name**, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Orthogonality.lean#L114).

```lean
instance : (dualHaar (G := G)).IsHaarMeasure
```

**An instance with no name**, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Orthogonality.lean#L117).

```lean
instance : IsProbabilityMeasure (dualHaar (G := G))
```

**`ProbabilisticTheory.QuantumMechanics.integral_character_dualHaar`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Orthogonality.lean#L126).

> **Orthogonality of characters**: the evaluation characters are orthonormal for the Haar
> probability measure of the dual group.

```lean
lemma integral_character_dualHaar (g : G) :
    ∫ χ, ((χ (Multiplicative.ofAdd g) : Circle) : ℂ) ∂(dualHaar (G := G)) =
      if g = 0 then 1 else 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/Orthogonality.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Orthogonality.lean)
