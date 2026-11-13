---
declaration: module
origin: cited
lean: StandardModel.biUnion_univ_const, StandardModel.IsGaugeSector.real_smul_eq, StandardModel.IsGaugeSector.repGauge_pair_add, StandardModel.IsGaugeSector.repGauge_pair_sub, StandardModel.IsGaugeSector.repGauge_fixed, StandardModel.IsGaugeSector.adjVec, StandardModel.IsGaugeSector.adjWeight, StandardModel.IsGaugeSector.repGauge_adjVec
statement: formalized
proof: formalized
---

# The gauge weight decomposition of the gauge sector

The module `PhyslibAlpha.Particles.StandardModel.IsGaugeSector.Deriv.GaugeWeight`, [PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean): 21 declarations, 17 with a docstring.

## i. Overview

> The field strength takes values in the *adjoint* representation, where — unlike the
> fundamental representations carrying the fermions — the standard (Gell-Mann and Pauli)
> basis is not a basis of torus eigenvectors.  The eigenvectors appear only after
> complexification: the torus scales the matrix entry `(j, k)` of the `su(3)` and `su(2)`
> blocks by `d j * star (d k)`, so the combinations `φ ± i ψ` of the real and imaginary
> parts of an entry functional are eigenvectors, while the Cartan and `u(1)` directions
> are fixed.
>
> This file collects that computation: the torus elements act by conjugation with the
> diagonal matrices `torusSU3Diag` and `torusSU2Diag`, `dualMap_pair_of_entry` turns an
> entrywise scaling into the rotation of a real pair of coordinate functionals, and
> `repGauge_pair_add` / `repGauge_pair_sub` / `repGauge_fixed` convert those into
> eigenvector statements for the field-strength symbols in the algebra `B`.

## ii. Key results

> - `repGauge_pair_add`
> - `repGauge_pair_sub`
> - `repGauge_fixed`

## iv. References

> * None.

**`StandardModel.biUnion_univ_const`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L54).

> A join over a nonempty index of a constant family of supports is that support.

```lean
lemma biUnion_univ_const {ι : Type*} [Fintype ι] [Nonempty ι] (t : Finset GaugeWeight) :
    (Finset.univ : Finset ι).biUnion (fun _ => t) = t
```

## A. Eigenvectors of the gauge action among the field-strength symbols

**`StandardModel.IsGaugeSector.real_smul_eq`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L80).

```lean
lemma real_smul_eq (r : ℝ) (b : B) : r • b = ((r : ℂ)) • b
```

**`StandardModel.IsGaugeSector.repGauge_pair_add`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L84).

```lean
lemma repGauge_pair_add (g : GaugeGroupI) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) (φ₁ φ₂ : Module.Dual ℝ GaugeAlgebra) (z : ℂ)
    (h1 : (GaugeAlgebra.adjointMap g⁻¹).dualMap φ₁ = z.re • φ₁ - z.im • φ₂)
    (h2 : (GaugeAlgebra.adjointMap g⁻¹).dualMap φ₂ = z.im • φ₁ + z.re • φ₂) :
    repGauge g (F l μ ν φ₁ + Complex.I • F l μ ν φ₂)
      = z • (F l μ ν φ₁ + Complex.I • F l μ ν φ₂)
```

**`StandardModel.IsGaugeSector.repGauge_pair_sub`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L97).

```lean
lemma repGauge_pair_sub (g : GaugeGroupI) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) (φ₁ φ₂ : Module.Dual ℝ GaugeAlgebra) (z : ℂ)
    (h1 : (GaugeAlgebra.adjointMap g⁻¹).dualMap φ₁ = z.re • φ₁ - z.im • φ₂)
    (h2 : (GaugeAlgebra.adjointMap g⁻¹).dualMap φ₂ = z.im • φ₁ + z.re • φ₂) :
    repGauge g (F l μ ν φ₁ - Complex.I • F l μ ν φ₂)
      = (starRingEnd ℂ z) • (F l μ ν φ₁ - Complex.I • F l μ ν φ₂)
```

**`StandardModel.IsGaugeSector.repGauge_fixed`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L111).

```lean
lemma repGauge_fixed (g : GaugeGroupI) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ GaugeAlgebra)
    (h1 : (GaugeAlgebra.adjointMap g⁻¹).dualMap φ = φ) :
    repGauge g (F l μ ν φ) = F l μ ν φ
```

## B. The gauge weight decomposition

**`StandardModel.IsGaugeSector.adjVec`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L128).

> The weight vectors of the adjoint: for each root the two complex combinations of
> the paired coordinate symbols, and for each Cartan direction the symbol itself.

```lean
noncomputable def adjVec (h : IsGaugeSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul F massWeightPoly) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) : Fin 4 ⊕ Fin 4 ⊕ Fin 4 → B
```

**`StandardModel.IsGaugeSector.adjWeight`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L138).

> The gauge weight of each adjoint weight vector.

```lean
def adjWeight : Fin 4 ⊕ Fin 4 ⊕ Fin 4 → GaugeWeight
```

**`StandardModel.IsGaugeSector.repGauge_adjVec`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L145).

> Each adjoint weight vector is a simultaneous eigenvector of the gauge torus.

```lean
lemma repGauge_adjVec {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (k : Fin 4 ⊕ Fin 4 ⊕ Fin 4) (i : Fin 4) :
    repGauge (gaugeTorusGen i) (h.adjVec l μ ν k)
      = ((expI : ℂ) ^ GaugeWeight.coord (adjWeight k) i) • h.adjVec l μ ν k
```

**`StandardModel.IsGaugeSector.F_coord_rootIdx_fst`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L175).

> The first symbol of a root pair, recovered from the two weight vectors.

```lean
lemma F_coord_rootIdx_fst {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (r : Fin 4) :
    F l μ ν (stdBasis.coord (rootIdx r).1)
      = (2 : ℂ)⁻¹ • (h.adjVec l μ ν (Sum.inl r)
        + h.adjVec l μ ν (Sum.inr (Sum.inl r)))
```

**`StandardModel.IsGaugeSector.F_coord_rootIdx_snd`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L188).

> The second symbol of a root pair, recovered from the two weight vectors.

```lean
lemma F_coord_rootIdx_snd {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (r : Fin 4) :
    F l μ ν (stdBasis.coord (rootIdx r).2)
      = (-(Complex.I / 2)) • (h.adjVec l μ ν (Sum.inl r)
        - h.adjVec l μ ν (Sum.inr (Sum.inl r)))
```

**`StandardModel.IsGaugeSector.F_coord_mem_iSup`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L201).

> Every standard coordinate symbol lies in the join of the weight-vector lines.

```lean
lemma F_coord_mem_iSup {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (a : Fin 8 ⊕ Fin 3 ⊕ Fin 1) :
    F l μ ν (stdBasis.coord a)
      ∈ ⨆ k, Submodule.span ℂ {h.adjVec l μ ν k}
```

**`StandardModel.IsGaugeSector.span_range_eq_iSup`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L239).

> The span of the field-strength symbols is the join of the twelve weight lines.

```lean
lemma span_range_eq_iSup {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3) :
    Submodule.span ℂ (Set.range (F l μ ν))
      = ⨆ k, Submodule.span ℂ {h.adjVec l μ ν k}
```

**`StandardModel.IsGaugeSector.rangeGaugeWeight`**, a def, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L260).

> The gauge weight decomposition of the span of one field-strength symbol map.

```lean
noncomputable def rangeGaugeWeight {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (Submodule.span ℂ (Set.range (F l μ ν)))
```

**`StandardModel.IsGaugeSector.derivSubmoduleGaugeWeight`**, an instance, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L272).

> **The gauge weight decomposition of the gauge derivative submodules**, for any
> number of covariant derivatives.

```lean
noncomputable instance derivSubmoduleGaugeWeight (n : ℕ) :
    GaugeWeightDecomposition repGauge (h.derivSubmodule n)
```

**`StandardModel.IsGaugeSector.rangeGaugeWeight_supp`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L283).

> The support of the decomposition of one symbol map: the image of `adjWeight`.

```lean
lemma rangeGaugeWeight_supp {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3) :
    (h.rangeGaugeWeight l μ ν).supp
      = Finset.univ.biUnion fun k : Fin 4 ⊕ Fin 4 ⊕ Fin 4 =>
        ({adjWeight k} : Finset GaugeWeight)
```

**`StandardModel.IsGaugeSector.derivSubmoduleGaugeWeight_supp`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L293).

> **The gauge weights occurring in the gauge derivative submodules**: the six `su(3)`
> roots, the two `su(2)` roots and the zero weight carried by the Cartan and `u(1)`
> directions.  The weights do not depend on the number of covariant derivatives, and
> every one of them has vanishing hypercharge.

```lean
lemma derivSubmoduleGaugeWeight_supp (n : ℕ) :
    (h.derivSubmoduleGaugeWeight n).supp
      = {((2, -1, 0, 0) : GaugeWeight), (1, 1, 0, 0), (-1, 2, 0, 0), (0, 0, 2, 0),
        (-2, 1, 0, 0), (-1, -1, 0, 0), (1, -2, 0, 0), (0, 0, -2, 0), (0, 0, 0, 0)}
```

## C. The pieces of the decomposition

**`StandardModel.IsGaugeSector.derivSubmoduleGaugeWeight_piece`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L317).

> **The pieces of the gauge weight decomposition.**  The weight-`w` piece is the join,
> over the derivative slots and the two covector indices, of the lines spanned by those
> weight vectors whose weight is `w`.

```lean
lemma derivSubmoduleGaugeWeight_piece (n : ℕ) (w : GaugeWeight) :
    (h.derivSubmoduleGaugeWeight n).piece w
      = ⨆ (l : Fin n → Fin 1 ⊕ Fin 3) (μ : Fin 1 ⊕ Fin 3) (ν : Fin 1 ⊕ Fin 3)
        (k : Fin 4 ⊕ Fin 4 ⊕ Fin 4),
        (if w = adjWeight k then ℂ ∙ h.adjVec l μ ν k else ⊥)
```

**`StandardModel.IsGaugeSector.derivSubmoduleGaugeWeight_piece_rootWeight`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L324).

> The piece at a root weight: the `+` combination for that root alone.

```lean
lemma derivSubmoduleGaugeWeight_piece_rootWeight (n : ℕ) (r : Fin 4) :
    (h.derivSubmoduleGaugeWeight n).piece (GaugeAlgebra.rootWeight r)
      = ⨆ (l : Fin n → Fin 1 ⊕ Fin 3) (μ : Fin 1 ⊕ Fin 3) (ν : Fin 1 ⊕ Fin 3),
        ℂ ∙ h.adjVec l μ ν (Sum.inl r)
```

**`StandardModel.IsGaugeSector.derivSubmoduleGaugeWeight_piece_neg_rootWeight`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L345).

> The piece at the opposite of a root weight: the `-` combination for that root.

```lean
lemma derivSubmoduleGaugeWeight_piece_neg_rootWeight (n : ℕ) (r : Fin 4) :
    (h.derivSubmoduleGaugeWeight n).piece (-(GaugeAlgebra.rootWeight r))
      = ⨆ (l : Fin n → Fin 1 ⊕ Fin 3) (μ : Fin 1 ⊕ Fin 3) (ν : Fin 1 ⊕ Fin 3),
        ℂ ∙ h.adjVec l μ ν (Sum.inr (Sum.inl r))
```

**`StandardModel.IsGaugeSector.derivSubmoduleGaugeWeight_piece_zero'`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L367).

> The weight-zero piece: the two `su(3)` Cartan generators, the `su(2)` Cartan
> generator and the `u(1)` generator, the only directions the torus fixes.

```lean
lemma derivSubmoduleGaugeWeight_piece_zero' (n : ℕ) :
    (h.derivSubmoduleGaugeWeight n).piece 0
      = ⨆ (l : Fin n → Fin 1 ⊕ Fin 3) (μ : Fin 1 ⊕ Fin 3) (ν : Fin 1 ⊕ Fin 3)
          (c : Fin 4),
        ℂ ∙ h.adjVec l μ ν (Sum.inr (Sum.inr c))
```

**`StandardModel.IsGaugeSector.derivSubmoduleGaugeWeight_piece_eq_bot`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean#L382).

> Every other weight has a trivial piece.

```lean
lemma derivSubmoduleGaugeWeight_piece_eq_bot (n : ℕ) {w : GaugeWeight}
    (hw : w ∉ (h.derivSubmoduleGaugeWeight n).supp) :
    (h.derivSubmoduleGaugeWeight n).piece w = ⊥
```

## Depends on

- [The root decomposition of the gauge algebra](../part-04/gaugealgebra-rootdecomposition.md)
- [The gauge sector](isgaugesector-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/GaugeWeight.lean)
