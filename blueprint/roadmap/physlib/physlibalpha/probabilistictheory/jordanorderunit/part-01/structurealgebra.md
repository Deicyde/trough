---
declaration: module
origin: cited
lean: ProbabilisticTheory.JordanAlgebra.JordanDerivation, ProbabilisticTheory.JordanAlgebra.JordanDerivation.ext, ProbabilisticTheory.JordanAlgebra.JordanDerivation.leibniz, ProbabilisticTheory.JordanAlgebra.JordanDerivation.submodule, ProbabilisticTheory.JordanAlgebra.JordanDerivation.zero_apply, ProbabilisticTheory.JordanAlgebra.JordanDerivation.add_apply, ProbabilisticTheory.JordanAlgebra.JordanDerivation.neg_apply, ProbabilisticTheory.JordanAlgebra.JordanDerivation.smul_apply
statement: formalized
proof: formalized
---

# Jordan derivations

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.StructureAlgebra`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean): 26 declarations (11 instances with no name), 15 with a docstring.

> Jordan derivations, their commutator Lie algebra and the inner derivations `[L_a, L_b]`.

## i. Overview

> A Jordan derivation is a linear map `D` with `D (a ∘ b) = D a ∘ b + a ∘ D b`, an infinitesimal
> symmetry of the observables. Commutators `[L_a, L_b]` of multiplication operators are the inner
> derivations.

## ii. Key results

> - `JordanAlgebra.JordanDerivation` : Jordan derivations.
> - `JordanAlgebra.inner` : inner derivations.

## iv. References

> - Adapted from Cobord, `Jordan/StructureAlgebra.lean`.

## A. Jordan derivations

**`ProbabilisticTheory.JordanAlgebra.JordanDerivation`**, a structure, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L53).

> A bundled real Jordan derivation.

```lean
structure JordanDerivation (E : Type*) [NonAssocCommRing E] [Module ℝ E] where
  /-- The underlying real-linear infinitesimal generator. -/
  toLinearMap : E →ₗ[ℝ] E
  leibniz' : IsDerivation toLinearMap
```

**An instance with no name**, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L62).

```lean
instance : CoeFun (JordanDerivation E) (fun _ => E → E)
```

**An instance with no name**, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L63).

```lean
instance : Coe (JordanDerivation E) (E →ₗ[ℝ] E)
```

**`ProbabilisticTheory.JordanAlgebra.JordanDerivation.ext`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L66).

```lean
lemma ext (h : ∀ x, D₁ x = D₂ x) : D₁ = D₂
```

**`ProbabilisticTheory.JordanAlgebra.JordanDerivation.leibniz`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L75).

```lean
lemma leibniz (D : JordanDerivation E) (x y : E) :
    D (x * y) = D x * y + x * D y
```

**`ProbabilisticTheory.JordanAlgebra.JordanDerivation.submodule`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L79).

> All derivations as a submodule of linear endomorphisms.

```lean
def submodule : Submodule ℝ (E →ₗ[ℝ] E)
```

## B. The vector space of derivations

**An instance with no name**, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L88).

> The zero infinitesimal symmetry.

```lean
instance : Zero (JordanDerivation E)
```

**An instance with no name**, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L91).

> Addition of infinitesimal symmetries.

```lean
instance : Add (JordanDerivation E)
```

**An instance with no name**, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L95).

> Negation of infinitesimal symmetries.

```lean
instance : Neg (JordanDerivation E)
```

**`ProbabilisticTheory.JordanAlgebra.JordanDerivation.zero_apply`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L99).

```lean
lemma zero_apply (x : E) : (0 : JordanDerivation E) x = 0
```

**`ProbabilisticTheory.JordanAlgebra.JordanDerivation.add_apply`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L102).

```lean
lemma add_apply (D₁ D₂ : JordanDerivation E) (x : E) : (D₁ + D₂) x = D₁ x + D₂ x
```

**`ProbabilisticTheory.JordanAlgebra.JordanDerivation.neg_apply`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L105).

```lean
lemma neg_apply (D : JordanDerivation E) (x : E) : (-D) x = -D x
```

**An instance with no name**, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L108).

> Scalar multiples of infinitesimal symmetries.

```lean
instance : SMul ℝ (JordanDerivation E)
```

**`ProbabilisticTheory.JordanAlgebra.JordanDerivation.smul_apply`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L111).

```lean
lemma smul_apply (c : ℝ) (D : JordanDerivation E) (x : E) : (c • D) x = c • D x
```

**`ProbabilisticTheory.JordanAlgebra.JordanDerivation.map_one_eq_zero`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L115).

> Every infinitesimal symmetry fixes the unit to first order.

```lean
lemma map_one_eq_zero (D : JordanDerivation E) : D 1 = 0
```

**An instance with no name**, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L121).

> Jordan derivations form an additive commutative group.

```lean
instance : AddCommGroup (JordanDerivation E)
```

**An instance with no name**, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L132).

> Jordan derivations form a real vector space.

```lean
instance : Module ℝ (JordanDerivation E)
```

## C. The commutator Lie algebra

**`ProbabilisticTheory.JordanAlgebra.JordanDerivation.comm`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L153).

> The commutator of two derivations is again a derivation.

```lean
def comm (D₁ D₂ : JordanDerivation E) : JordanDerivation E
```

**`ProbabilisticTheory.JordanAlgebra.JordanDerivation.comm_apply`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L165).

```lean
lemma comm_apply (D₁ D₂ : JordanDerivation E) (x : E) :
    comm D₁ D₂ x = D₁ (D₂ x) - D₂ (D₁ x)
```

**An instance with no name**, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L169).

> Derivations carry their canonical commutator bracket.

```lean
instance : Bracket (JordanDerivation E) (JordanDerivation E)
```

**`ProbabilisticTheory.JordanAlgebra.JordanDerivation.lie_apply`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L172).

```lean
lemma lie_apply (D₁ D₂ : JordanDerivation E) (x : E) :
    ⁅D₁, D₂⁆ x = D₁ (D₂ x) - D₂ (D₁ x)
```

**An instance with no name**, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L176).

> Infinitesimal Jordan symmetries form a Lie ring under commutator.

```lean
instance : LieRing (JordanDerivation E)
```

**An instance with no name**, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L195).

> The commutator Lie ring of derivations is a real Lie algebra.

```lean
instance : LieAlgebra ℝ (JordanDerivation E)
```

## D. Inner derivations

**`ProbabilisticTheory.JordanAlgebra.inner`**, a def, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L209).

> The canonical inner Jordan derivation, generated by two observables.

```lean
def inner (a b : E) : JordanDerivation E
```

**`ProbabilisticTheory.JordanAlgebra.inner_apply`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L214).

```lean
lemma inner_apply (a b x : E) : inner a b x = a * (b * x) - b * (a * x)
```

**`ProbabilisticTheory.JordanAlgebra.inner_comm`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean#L218).

> The inner-derivation commutator law in bundled infinitesimal-symmetry form.

```lean
lemma inner_comm (a b c d : E) :
    JordanDerivation.comm (inner a b) (inner c d) =
      inner (inner a b c) d + inner c (inner a b d)
```

## Depends on

- [Derivations](../../algebra/derivation.md)
- [The fundamental formula](../part-02/quadratic-fundamental.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/StructureAlgebra.lean)
