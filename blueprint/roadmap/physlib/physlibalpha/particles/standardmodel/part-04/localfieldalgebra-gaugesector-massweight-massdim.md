---
declaration: module
origin: cited
lean: StandardModel.GaugeSector.iSup_span_singleton_le, StandardModel.GaugeSector.mem_iSup_span₃, StandardModel.GaugeSector.span_stable_of_map_eq_sum, StandardModel.GaugeSector.map_eq_self_of_mem_iSup_span, StandardModel.GaugeSector.span_singleton_mul_span_singleton_le, StandardModel.GaugeSector.iSup_span_mul_iSup_span_le, StandardModel.GaugeSector.sum_mul_sum_eq_sum_pi_two, StandardModel.GaugeSector.map_mul_fixed_eq_sum
statement: formalized
proof: formalized
---

# Products of two field strengths as bi-adjoint gauge tensors

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.GaugeSector.MassWeight.MassDimEight`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean): 109 declarations, 109 with a docstring.

> The gauge and Lorentz invariants of the gauge sector at mass weight eight, the kinetic and theta
> terms of the three gauge groups.

## i. Overview

> A single field-strength symbol of the gauge sector carries one adjoint index of the gauge
> algebra, so a product of two of them carries two. Restricting the value index to one
> factor of the gauge group turns such a product into a family indexed by two adjoint
> indices of that factor, and the gauge transformation law `repGauge_F` says exactly that
> the maps of these families out of the tensors with two adjoint indices are equivariant
> (`ColourAdjAdj.of_law`, `IsospinAdjAdj.of_law`), and for hypercharge the family is fixed
> outright. The gauge invariant these laws supply is the trace contraction,
> the Kronecker contraction of the two adjoint indices, the familiar kinetic pairing of two
> field strengths; it has mass weight eight and is fixed by the whole gauge group.
>
> Conversely every twice-derived field strength and every product of two underived ones,
> sorted by gauge factor, is a component of a gluon or `W`-boson pair family, a hypercharge
> invariant, or a family carrying an unpaired adjoint index of a non-abelian factor, which
> contributes nothing by `ColourAdj.reducesInvariantsTo_bot` and
> `IsospinAdj.reducesInvariantsTo_bot`. Putting the two
> directions together classifies the gauge invariants of mass weight eight modulo any
> gauge-stable submodule. Such an invariant is a combination of the three underived trace
> contractions and the twice-derived hypercharge field strengths. Both shapes carry four
> covector indices and no others, so both are quadruple Lorentz tensors, and the Lorentz
> classification cuts the combinations down further, to the four Lorentz contractions of
> each of the four families. All four families are antisymmetric in their last two slots, by
> `F_antisymm`, and that leaves two contractions of each, eight spanning generators in all
> (`lorentzContractionEightSpan_eq`).
>
> Both classifications are reductions in the sense of `ReducesInvariantsTo`, stated modulo
> any stable submodule. The converse is that each span consists of invariants of mass weight
> eight already, the gauge one because its generators are fixed by the gauge group and carry
> the right mass weight, and the Lorentz one because it sits inside the gauge span and is
> spanned by contractions that `RankFour` shows to be Lorentz invariant. Section J composes
> the two reductions and puts the two directions together as the equivalences
> `mem_massWeightSubmodule_eight_sup_and_invariant_iff` and
> `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`, the second also with the
> eight generators, `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_reduced`.

## ii. Key results

> - `lorentzContractionEightSpan_eq` : the Lorentz contraction span is spanned by eight of its
>   sixteen generators, for each family the `(0,2)(1,3)` metric contraction and the Levi-Civita
>   contraction.
> - `mem_massWeightSubmodule_eight_sup_and_invariant_iff` : the gauge classification of mass weight
>   eight as an equivalence.
> - `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff` : the gauge and Lorentz
>   classification of mass weight eight as an equivalence, with the four Lorentz contractions of
>   the four families of section H.
> - `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_reduced` : the same
>   equivalence with the eight generators of `lorentzContractionEightSpan_eq`.

## iv. References

> * None.

## A. Spans and stability

> Every subspace in this file is spanned by a finite family. Where a classifier supplies or
> consumes it, it is written `Submodule.span ℂ (Set.range T)`; where a family of lines is
> collected, it is the join `⨆ i, ℂ ∙ T i`, and `Submodule.span_range_eq_iSup` passes between
> the two. A join of lines lies in a submodule as soon as its generators do, and a linear map
> fixing each generator fixes it pointwise; a linear map moving each generator to a
> combination of the generators carries the span into itself.
>
> The classification runs through `ReducesInvariantsTo`. Each bi-adjoint family's span
> reduces, for its factor of the gauge group, to the line through its trace contraction, and
> each adjoint family's span to `⊥`; `ReducesInvariantsTo.iSup` joins the families of one
> kind, and `ReducesInvariantsTo.sup` joins the kinds.

**`StandardModel.GaugeSector.iSup_span_singleton_le`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L117).

> A span lies in a submodule as soon as its generators do.

```lean
lemma iSup_span_singleton_le {ι : Sort*} (T : ι → fieldData.LocalCovFieldAlgebra)
    {V : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (hV : ∀ i, T i ∈ V) : (⨆ i, ℂ ∙ T i) ≤ V
```

**`StandardModel.GaugeSector.mem_iSup_span₃`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L123).

> A generator of a family with three indices lies in its span.

```lean
lemma mem_iSup_span₃ {α β γ : Sort*} (T : α → β → γ → fieldData.LocalCovFieldAlgebra)
    (a : α) (b : β) (c : γ) :
    T a b c ∈ ⨆ (a) (b) (c), ℂ ∙ T a b c
```

**`StandardModel.GaugeSector.span_stable_of_map_eq_sum`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L131).

> A linear map moving each generator to a combination of the generators carries the span
> into itself; the transformation laws of this file all have this shape.

```lean
lemma span_stable_of_map_eq_sum {ι : Type} [Fintype ι] (T : ι → fieldData.LocalCovFieldAlgebra)
    (f : fieldData.LocalCovFieldAlgebra →ₗ[ℂ] fieldData.LocalCovFieldAlgebra)
    {c : ι → ι → ℂ} (hf : ∀ l, f (T l) = ∑ a, c a l • T a) :
    ∀ y ∈ Submodule.span ℂ (Set.range T), f y ∈ Submodule.span ℂ (Set.range T)
```

**`StandardModel.GaugeSector.map_eq_self_of_mem_iSup_span`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L138).

> A linear map fixing each generator fixes the span pointwise.

```lean
lemma map_eq_self_of_mem_iSup_span {ι : Sort*} (T : ι → fieldData.LocalCovFieldAlgebra)
    (f : fieldData.LocalCovFieldAlgebra →ₗ[ℂ] fieldData.LocalCovFieldAlgebra)
    (hf : ∀ i, f (T i) = T i) : ∀ y ∈ ⨆ i, ℂ ∙ T i, f y = y
```

**`StandardModel.GaugeSector.span_singleton_mul_span_singleton_le`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L146).

> The product of two lines lies in a submodule as soon as the product of the two
> generators does.

```lean
lemma span_singleton_mul_span_singleton_le {a b : fieldData.LocalCovFieldAlgebra}
    {V : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (hab : a * b ∈ V) :
    (ℂ ∙ a) * (ℂ ∙ b) ≤ V
```

**`StandardModel.GaugeSector.iSup_span_mul_iSup_span_le`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L155).

> The product of two spans lies in a submodule as soon as the products of their
> generators do.

```lean
lemma iSup_span_mul_iSup_span_le {α β γ α' β' γ' : Sort*}
    (T : α → β → γ → fieldData.LocalCovFieldAlgebra)
    (T' : α' → β' → γ' → fieldData.LocalCovFieldAlgebra)
    {V : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (hV : ∀ a b c a' b' c', T a b c * T' a' b' c' ∈ V) :
    (⨆ (a) (b) (c), ℂ ∙ T a b c) * (⨆ (a) (b) (c), ℂ ∙ T' a b c) ≤ V
```

**`StandardModel.GaugeSector.sum_mul_sum_eq_sum_pi_two`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L167).

> A product of two combinations is a combination indexed by pairs.

```lean
lemma sum_mul_sum_eq_sum_pi_two {k : ℕ} (c₀ c₁ : Fin k → ℂ)
    (X Y : Fin k → fieldData.LocalCovFieldAlgebra) :
    (∑ a, c₀ a • X a) * ∑ b, c₁ b • Y b
      = ∑ d : Fin 2 → Fin k, (c₀ (d 0) * c₁ (d 1)) • (X (d 0) * Y (d 1))
```

**`StandardModel.GaugeSector.map_mul_fixed_eq_sum`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L178).

> A multiplicative map moving a family by a matrix and fixing a vector moves the
> products of the family with that vector by the same matrix.

```lean
lemma map_mul_fixed_eq_sum {k : ℕ}
    {f : fieldData.LocalCovFieldAlgebra →ₗ[ℂ] fieldData.LocalCovFieldAlgebra}
    (hf : ∀ x y, f (x * y) = f x * f y)
    {c : Fin k → Fin k → ℂ} {T : Fin k → fieldData.LocalCovFieldAlgebra}
    (hT : ∀ l, f (T l) = ∑ a, c a l • T a) {v : fieldData.LocalCovFieldAlgebra}
    (hv : f v = v) (l : Fin k) : f (T l * v) = ∑ a, c a l • (T a * v)
```

**`StandardModel.GaugeSector.map_fixed_mul_eq_sum`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L188).

> The mirror of `map_mul_fixed_eq_sum` with the fixed vector on the left.

```lean
lemma map_fixed_mul_eq_sum {k : ℕ}
    {f : fieldData.LocalCovFieldAlgebra →ₗ[ℂ] fieldData.LocalCovFieldAlgebra}
    (hf : ∀ x y, f (x * y) = f x * f y)
    {c : Fin k → Fin k → ℂ} {T : Fin k → fieldData.LocalCovFieldAlgebra}
    (hT : ∀ l, f (T l) = ∑ a, c a l • T a) {v : fieldData.LocalCovFieldAlgebra}
    (hv : f v = v) (l : Fin k) : f (v * T l) = ∑ a, c a l • (v * T a)
```

## B. The gauge transformation of the gauge-factor field strengths

> The gauge law `repGauge_F` moves the field-strength symbol by the coadjoint action of
> the gauge group on its argument, which on the standard basis coordinates is the adjoint
> matrix. That matrix is block diagonal, so the gluon field strengths transform among
> themselves by the `su(3)` adjoint matrix of the colour factor, the `W`-boson field
> strengths by the `su(2)` adjoint matrix of the isospin factor, and the hypercharge field
> strength is fixed. The colour factor alone fixes the `W`-boson field strengths as well.

**`StandardModel.GaugeSector.repGauge_F_coord`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L212).

> The field-strength symbol evaluated on a standard-basis coordinate transforms under
> the gauge group through the column of `adjointMatrix` indexed by that coordinate.

```lean
lemma repGauge_F_coord (g : GaugeGroupI) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) (c : Fin 8 ⊕ Fin 3 ⊕ Fin 1) :
    repGaugeGroupI g (gaugeFieldStrength l μ ν (GaugeAlgebra.stdBasis.coord c))
      = ∑ b, ((GaugeAlgebra.adjointMatrix g b c : ℝ) : ℂ) •
          gaugeFieldStrength l μ ν (GaugeAlgebra.stdBasis.coord b)
```

**`StandardModel.GaugeSector.repGauge_gluonField`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L226).

> The gluon field strength transforms in the adjoint representation of the `su(3)`
> factor of the gauge group.

```lean
lemma repGauge_gluonField (g : GaugeGroupI) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) (c : Fin 8) :
    repGaugeGroupI g (gluonField l μ ν c)
      = ∑ a : Fin 8, ((su3AdjointMatrix (GaugeGroupI.toSU3 g) a c : ℝ) : ℂ) •
          gluonField l μ ν a
```

**`StandardModel.GaugeSector.repGauge_wField`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L237).

> The `W`-boson field strength transforms in the adjoint representation of the `su(2)`
> factor of the gauge group.

```lean
lemma repGauge_wField (g : GaugeGroupI) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) (c : Fin 3) :
    repGaugeGroupI g (wField l μ ν c)
      = ∑ i : Fin 3, ((su2AdjointMatrix (GaugeGroupI.toSU2 g) i c : ℝ) : ℂ) •
          wField l μ ν i
```

**`StandardModel.GaugeSector.repGauge_hyperchargeField`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L248).

> The hypercharge field strength is gauge invariant, the adjoint action of the gauge
> group on the `u(1)` factor of the gauge algebra is trivial.

```lean
lemma repGauge_hyperchargeField (g : GaugeGroupI) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) :
    repGaugeGroupI g (hyperchargeField l μ ν) = hyperchargeField l μ ν
```

**`StandardModel.GaugeSector.repGauge_su3_wField`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L257).

> The `W`-boson field strengths are fixed by the colour factor of the gauge group, since the
> `su(2)` block of the adjoint matrix reads the isospin factor alone.

```lean
lemma repGauge_su3_wField (U : specialUnitaryGroup (Fin 3) ℂ) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3) (i : Fin 3) :
    repGaugeGroupI (U, 1, 1) (wField l μ ν i) = wField l μ ν i
```

**`StandardModel.GaugeSector.isEquivariant_colourAdj_gluonField`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L273).

> The gluon field strengths at fixed derivative slots and covector indices form a family
> of one `su(3)` adjoint index.

```lean
lemma isEquivariant_colourAdj_gluonField {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3) :
    (suTensor 3).IsEquivariant ![.adj] (repGaugeGroupI.comp GaugeGroupI.ofSU3)
      (liftComponents ((gluonField l μ ν) ∘ relabelAdjIdx su3Label))
```

**`StandardModel.GaugeSector.isEquivariant_isospinAdj_wField`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L280).

> The `W`-boson field strengths at fixed derivative slots and covector indices form a
> family of one `su(2)` adjoint index.

```lean
lemma isEquivariant_isospinAdj_wField {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3) :
    (suTensor 2).IsEquivariant ![.adj] (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents ((wField l μ ν) ∘ relabelAdjIdx su2Label))
```

## C. Products of two underived field strengths as bi-adjoint families

> A product of two underived field strengths of one gauge factor, at the four covector
> indices `p`, is a family indexed by the two adjoint indices of that factor, and by section
> B and the multiplicativity of the gauge action it obeys the transformation law of a tensor
> with two adjoint indices (`repGaugeGroupI_gluonPair_eq_sum`, `repGaugeGroupI_wPair_eq_sum`,
> `repGaugeGroupI_hyperchargePair`), at every gauge element and not only at those of its own
> factor. Its trace contraction, the Kronecker contraction of the two adjoint indices, is fixed by the
> whole
> gauge group and has mass weight eight, the sum of the mass weights of its two factors; so
> is the twice-derived hypercharge field strength, the other shape of mass weight eight.

**`StandardModel.GaugeSector.EightIdx`**, an abbrev, [line 304](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L304).

> The index of a product of two underived field strengths, the two covector indices of
> the first factor followed by the two of the second, read as one family of four
> four-vector indices so that the Lorentz classification applies to it.

```lean
abbrev EightIdx : Type
```

**`StandardModel.GaugeSector.gluonPair`**, a def, [line 308](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L308).

> The product of two underived gluon field strengths at the covector indices `p`, indexed
> by the two `su(3)` adjoint indices it carries.

```lean
noncomputable def gluonPair (p : EightIdx) (a : Fin 2 → Fin 8) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.wPair`**, a def, [line 313](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L313).

> The product of two underived `W`-boson field strengths at the covector indices `p`,
> indexed by the two `su(2)` adjoint indices it carries.

```lean
noncomputable def wPair (p : EightIdx) (a : Fin 2 → Fin 3) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.hyperchargePair`**, a def, [line 318](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L318).

> The product of two underived hypercharge field strengths at the covector indices `p`,
> indexed by the two `u(1)` adjoint indices it carries.

```lean
noncomputable def hyperchargePair (p : EightIdx)
    (_ : Fin 2 → Fin 1) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.hyperchargeDeriv`**, a def, [line 324](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L324).

> The twice-derived hypercharge field strength at the derivative slots `d 0`, `d 1` and
> the covector indices `d 2`, `d 3`.

```lean
noncomputable def hyperchargeDeriv (d : EightIdx) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.repGaugeGroupI_gluonPair_eq_sum`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L329).

> A gauge transformation moves a gluon pair as the `SU(3)` factor of that gauge group
> element moves a tensor with two `su(3)` adjoint indices.

```lean
lemma repGaugeGroupI_gluonPair_eq_sum (p : EightIdx) (g : GaugeGroupI) (l : Fin 2 → Fin 8) :
    repGaugeGroupI g (gluonPair p l) = ∑ a : Fin 2 → Fin 8,
      (∏ i : Fin 2, ((su3AdjointMatrix (GaugeGroupI.toSU3 g) (a i) (l i) : ℝ) : ℂ)) •
        gluonPair p a
```

**`StandardModel.GaugeSector.isEquivariant_colourAdjAdj_gluonPair`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L337).

> A gluon pair is a bi-adjoint `su(3)` tensor.

```lean
lemma isEquivariant_colourAdjAdj_gluonPair (p : EightIdx) :
    (suTensor 3).IsEquivariant ![.adj, .adj] (repGaugeGroupI.comp GaugeGroupI.ofSU3)
      (liftComponents ((gluonPair p) ∘ relabelAdjPairIdx su3Label))
```

**`StandardModel.GaugeSector.repGaugeGroupI_wPair_eq_sum`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L344).

> A gauge transformation moves a `W`-boson pair as the `SU(2)` factor of that gauge group
> element moves a tensor with two `su(2)` adjoint indices.

```lean
lemma repGaugeGroupI_wPair_eq_sum (p : EightIdx) (g : GaugeGroupI) (l : Fin 2 → Fin 3) :
    repGaugeGroupI g (wPair p l) = ∑ a : Fin 2 → Fin 3,
      (∏ i : Fin 2, ((su2AdjointMatrix (GaugeGroupI.toSU2 g) (a i) (l i) : ℝ) : ℂ)) •
        wPair p a
```

**`StandardModel.GaugeSector.isEquivariant_isospinAdjAdj_wPair`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L352).

> A `W`-boson pair is a bi-adjoint `su(2)` tensor.

```lean
lemma isEquivariant_isospinAdjAdj_wPair (p : EightIdx) :
    (suTensor 2).IsEquivariant ![.adj, .adj] (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents ((wPair p) ∘ relabelAdjPairIdx su2Label))
```

**`StandardModel.GaugeSector.repGaugeGroupI_hyperchargePair`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L358).

> A gauge transformation fixes a hypercharge pair, which is the `u(1)` bi-adjoint law.

```lean
lemma repGaugeGroupI_hyperchargePair (p : EightIdx) (g : GaugeGroupI) (l : Fin 2 → Fin 1) :
    repGaugeGroupI g (hyperchargePair p l) = hyperchargePair p l
```

**`StandardModel.GaugeSector.gluonTrace`**, a def, [line 364](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L364).

> The gluon trace contraction at the covector indices `p`, the Kronecker contraction of
> the two colour indices of the gluon pair.

```lean
noncomputable def gluonTrace (p : EightIdx) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.wTrace`**, a def, [line 368](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L368).

> The `W`-boson trace contraction at the covector indices `p`.

```lean
noncomputable def wTrace (p : EightIdx) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.hyperchargeTrace`**, a def, [line 372](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L372).

> The hypercharge trace contraction at the covector indices `p`.

```lean
noncomputable def hyperchargeTrace (p : EightIdx) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.gluonTrace_eq`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L376).

> The gluon trace contraction is the kinetic pairing of two gluon field strengths.

```lean
lemma gluonTrace_eq (p : EightIdx) :
    gluonTrace p
      = ∑ a : Fin 8, gluonField ![] (p 0) (p 1) a * gluonField ![] (p 2) (p 3) a
```

**`StandardModel.GaugeSector.wTrace_eq`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L383).

> The `W`-boson trace contraction is the kinetic pairing of two `W`-boson field
> strengths.

```lean
lemma wTrace_eq (p : EightIdx) :
    wTrace p = ∑ i : Fin 3, wField ![] (p 0) (p 1) i * wField ![] (p 2) (p 3) i
```

**`StandardModel.GaugeSector.hyperchargeTrace_eq`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L389).

> The hypercharge trace contraction is the product of the two hypercharge field
> strengths, the `u(1)` factor being one dimensional.

```lean
lemma hyperchargeTrace_eq (p : EightIdx) :
    hyperchargeTrace p
      = hyperchargeField ![] (p 0) (p 1) * hyperchargeField ![] (p 2) (p 3)
```

**`StandardModel.GaugeSector.repGauge_gluonTrace`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L395).

> The gluon trace contraction is fixed by the whole gauge group.

```lean
lemma repGauge_gluonTrace (g : GaugeGroupI) (p : EightIdx) :
    repGaugeGroupI g (gluonTrace p) = gluonTrace p
```

**`StandardModel.GaugeSector.repGauge_wTrace`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L400).

> The `W`-boson trace contraction is fixed by the whole gauge group.

```lean
lemma repGauge_wTrace (g : GaugeGroupI) (p : EightIdx) :
    repGaugeGroupI g (wTrace p) = wTrace p
```

**`StandardModel.GaugeSector.repGauge_hyperchargeTrace`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L405).

> The hypercharge trace contraction is fixed by the whole gauge group.

```lean
lemma repGauge_hyperchargeTrace (g : GaugeGroupI) (p : EightIdx) :
    repGaugeGroupI g (hyperchargeTrace p) = hyperchargeTrace p
```

**`StandardModel.GaugeSector.repGauge_hyperchargeDeriv`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L410).

> The twice-derived hypercharge field strength is fixed by the whole gauge group.

```lean
lemma repGauge_hyperchargeDeriv (g : GaugeGroupI) (d : EightIdx) :
    repGaugeGroupI g (hyperchargeDeriv d) = hyperchargeDeriv d
```

**`StandardModel.GaugeSector.F_mem_derivSubmodule`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L416).

> Every field-strength symbol lies in the derivative submodule of its own number of
> covariant derivatives.

```lean
lemma F_mem_derivSubmodule {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) : gaugeFieldStrength l μ ν φ ∈ derivSubmodule n
```

**`StandardModel.GaugeSector.F_mem_massWeightSubmodule`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L423).

> A field-strength symbol with `n` covariant derivatives has mass weight `2 * (2 + n)`.

```lean
lemma F_mem_massWeightSubmodule {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) : gaugeFieldStrength l μ ν φ ∈ massWeightSubmodule (2 * (2 +
      n))
```

**`StandardModel.GaugeSector.F_mul_F_mem_massWeightSubmodule_eight`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L429).

> A product of two underived field-strength symbols has mass weight eight.

```lean
lemma F_mul_F_mem_massWeightSubmodule_eight (μ ν μ' ν' : Fin 1 ⊕ Fin 3)
    (φ φ' : Module.Dual ℝ GaugeAlgebra) :
    gaugeFieldStrength ![] μ ν φ * gaugeFieldStrength ![] μ' ν' φ' ∈ massWeightSubmodule 8
```

**`StandardModel.GaugeSector.gluonTrace_mem_massWeightSubmodule`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L436).

> The gluon trace contraction has mass weight eight.

```lean
lemma gluonTrace_mem_massWeightSubmodule (p : EightIdx) :
    gluonTrace p ∈ massWeightSubmodule 8
```

**`StandardModel.GaugeSector.wTrace_mem_massWeightSubmodule`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L442).

> The `W`-boson trace contraction has mass weight eight.

```lean
lemma wTrace_mem_massWeightSubmodule (p : EightIdx) : wTrace p ∈ massWeightSubmodule 8
```

**`StandardModel.GaugeSector.hyperchargeTrace_mem_massWeightSubmodule`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L447).

> The hypercharge trace contraction has mass weight eight.

```lean
lemma hyperchargeTrace_mem_massWeightSubmodule (p : EightIdx) :
    hyperchargeTrace p ∈ massWeightSubmodule 8
```

**`StandardModel.GaugeSector.hyperchargeDeriv_mem_massWeightSubmodule`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L453).

> The twice-derived hypercharge field strength has mass weight `2 * (2 + 2)`, eight.

```lean
lemma hyperchargeDeriv_mem_massWeightSubmodule (d : EightIdx) :
    hyperchargeDeriv d ∈ massWeightSubmodule 8
```

## D. The families of mass weight eight

> Mass weight eight is the twice-derived field strengths together with the products of two
> underived ones (`massWeightSubmodule_eight_eq`), and each field-strength symbol is a
> combination of its values on the twelve coordinates of the standard basis of the gauge
> algebra: eight gluon, three `W`-boson and one hypercharge direction. Sorting the symbols and
> their products by gauge factor gives five kinds of family.
>
> - Two gluon symbols form a component of a gluon pair family, and two `W`-boson symbols one of
>   a `W`-boson pair family, the bi-adjoint families of section C.
> - Two hypercharge symbols form a hypercharge trace contraction, and a twice-derived
>   hypercharge symbol is a twice-derived hypercharge field strength; both are fixed by the
>   whole gauge group.
> - A gluon symbol, alone or against a symbol of another factor, carries an unpaired `su(3)`
>   adjoint index. These are the colour families, whose maps out of `SuT[3, .adj]` are
>   equivariant: the colour factor moves the gluon index and fixes the other factor.
> - A `W`-boson symbol, alone or against a hypercharge symbol, carries an unpaired `su(2)`
>   adjoint index. These are the isospin families, with maps out of `SuT[2, .adj]`.

**`StandardModel.GaugeSector.gluonPairSpan`**, a def, [line 482](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L482).

> The join, over all covector indices, of the spans of the gluon pair families.

```lean
noncomputable def gluonPairSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.wPairSpan`**, a def, [line 486](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L486).

> The join, over all covector indices, of the spans of the `W`-boson pair families.

```lean
noncomputable def wPairSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.hyperchargeTraceSpan`**, a def, [line 490](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L490).

> The span of the hypercharge trace contractions.

```lean
noncomputable def hyperchargeTraceSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.hyperchargeDerivSpan`**, a def, [line 494](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L494).

> The span of the twice-derived hypercharge field strengths.

```lean
noncomputable def hyperchargeDerivSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.neutralVec`**, a def, [line 499](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L499).

> The underived symbols of the factors other than colour, on the `W`-boson and hypercharge
> coordinates of the standard basis.

```lean
noncomputable def neutralVec (μ ν : Fin 1 ⊕ Fin 3) (j : Fin 3 ⊕ Fin 1) :
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.repGauge_su3_neutralVec`**, a lemma, [line 505](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L505).

> The symbols of the factors other than colour are fixed by the colour factor of the gauge
> group.

```lean
lemma repGauge_su3_neutralVec (U : specialUnitaryGroup (Fin 3) ℂ) (μ ν : Fin 1 ⊕ Fin 3) :
    ∀ j, repGaugeGroupI (U, 1, 1) (neutralVec μ ν j) = neutralVec μ ν j
```

**`StandardModel.GaugeSector.DerivIdx`**, an abbrev, [line 514](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L514).

> The index of a twice-derived symbol, the two derivative slots and the two covector
> indices.

```lean
abbrev DerivIdx : Type
```

**`StandardModel.GaugeSector.MixIdx`**, an abbrev, [line 519](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L519).

> The index of a mixed product with a gluon symbol, the two covector indices of the gluon
> factor, the two of the other factor, and the coordinate of the other factor.

```lean
abbrev MixIdx : Type
```

**`StandardModel.GaugeSector.ColourIdx`**, an abbrev, [line 525](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L525).

> The index of a family carrying one unpaired `su(3)` adjoint index at mass weight
> eight, a twice-derived gluon tower, or an underived gluon field strength against an
> underived symbol of another factor on either side.

```lean
abbrev ColourIdx : Type
```

**`StandardModel.GaugeSector.colourFamily`**, a def, [line 528](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L528).

> The families carrying one unpaired `su(3)` adjoint index.

```lean
noncomputable def colourFamily : ColourIdx → Fin 8 → fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.isEquivariant_colourAdj_colourFamily`**, a lemma, [line 537](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L537).

> Each colour family is an `su(3)` adjoint family, the colour factor moves the gluon
> index and fixes the other factor.

```lean
lemma isEquivariant_colourAdj_colourFamily :
    ∀ i : ColourIdx, (suTensor 3).IsEquivariant ![.adj] (repGaugeGroupI.comp GaugeGroupI.ofSU3)
      (liftComponents ((colourFamily i) ∘ relabelAdjIdx su3Label))
```

**`StandardModel.GaugeSector.IsospinIdx`**, an abbrev, [line 549](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L549).

> The index of a family carrying one unpaired `su(2)` adjoint index at mass weight
> eight, a twice-derived `W`-boson tower, or an underived `W`-boson field strength against
> an underived hypercharge field strength on either side.

```lean
abbrev IsospinIdx : Type
```

**`StandardModel.GaugeSector.isospinFamily`**, a def, [line 552](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L552).

> The families carrying one unpaired `su(2)` adjoint index.

```lean
noncomputable def isospinFamily : IsospinIdx → Fin 3 → fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.isEquivariant_isospinAdj_isospinFamily`**, a lemma, [line 559](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L559).

> Each isospin family is an `su(2)` adjoint family, the isospin factor moves the
> `W`-boson index and fixes hypercharge.

```lean
lemma isEquivariant_isospinAdj_isospinFamily :
    ∀ i : IsospinIdx, (suTensor 2).IsEquivariant ![.adj] (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents ((isospinFamily i) ∘ relabelAdjIdx su2Label))
```

**`StandardModel.GaugeSector.repGauge_su3_isospinFamily`**, a lemma, [line 570](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L570).

> The isospin families are fixed by the colour factor, every one of their factors
> being.

```lean
lemma repGauge_su3_isospinFamily (U : specialUnitaryGroup (Fin 3) ℂ) :
    ∀ (i : IsospinIdx) (a : Fin 3),
      repGaugeGroupI (U, 1, 1) (isospinFamily i a) = isospinFamily i a
```

**`StandardModel.GaugeSector.unpairedColourSpan`**, a def, [line 580](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L580).

> The join of the spans of the colour families.

```lean
noncomputable def unpairedColourSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.unpairedIsospinSpan`**, a def, [line 584](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L584).

> The join of the spans of the isospin families.

```lean
noncomputable def unpairedIsospinSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.colourFamily_mem`**, a lemma, [line 588](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L588).

> A component of a colour family lies in the join of the colour spans.

```lean
lemma colourFamily_mem (i : ColourIdx) (a : Fin 8) : colourFamily i a ∈ unpairedColourSpan
```

**`StandardModel.GaugeSector.isospinFamily_mem`**, a lemma, [line 592](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L592).

> A component of an isospin family lies in the join of the isospin spans.

```lean
lemma isospinFamily_mem (i : IsospinIdx) (a : Fin 3) :
    isospinFamily i a ∈ unpairedIsospinSpan
```

**`StandardModel.GaugeSector.repGauge_su3_of_mem_unpairedIsospinSpan`**, a lemma, [line 597](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L597).

> The join of the isospin families is fixed pointwise by the colour factor.

```lean
lemma repGauge_su3_of_mem_unpairedIsospinSpan (U : specialUnitaryGroup (Fin 3) ℂ) :
    ∀ y ∈ unpairedIsospinSpan, repGaugeGroupI (U, 1, 1) y = y
```

## E. Mass weight eight inside the family spans

> A derivative submodule lies in a submodule as soon as the symbols on the twelve standard
> coordinates do, by `F_mem_iSup_span_coord`. Sorting the twice-derived symbols and the
> products of two underived ones by gauge factor, as in section D, bounds mass weight eight by
> the joins of the unpaired families together with the pair spans, the hypercharge trace
> contractions and the twice-derived hypercharge field strengths.

**`StandardModel.GaugeSector.derivSubmodule_le_of_coord_mem`**, a lemma, [line 616](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L616).

> A derivative submodule lies in a submodule as soon as the symbols on the standard
> coordinates do.

```lean
lemma derivSubmodule_le_of_coord_mem {n : ℕ} {V : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (hV : ∀ (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3) (c : Fin 8 ⊕ Fin 3 ⊕ Fin 1),
      gaugeFieldStrength l μ ν (GaugeAlgebra.stdBasis.coord c) ∈ V) :
    derivSubmodule n ≤ V
```

**`StandardModel.GaugeSector.derivSubmodule_two_le`**, a lemma, [line 626](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L626).

> The twice-derived symbols. A gluon or `W`-boson symbol is a component of an unpaired
> family, and the hypercharge symbol is a twice-derived hypercharge field strength.

```lean
lemma derivSubmodule_two_le :
    derivSubmodule 2 ≤ (unpairedColourSpan ⊔ unpairedIsospinSpan) ⊔ hyperchargeDerivSpan
```

**`StandardModel.GaugeSector.derivSubmodule_zero_le`**, a lemma, [line 640](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L640).

> The underived symbols lie in the join of the lines through their values on the
> standard coordinates.

```lean
lemma derivSubmodule_zero_le :
    derivSubmodule 0 ≤ ⨆ (μ : Fin 1 ⊕ Fin 3) (ν : Fin 1 ⊕ Fin 3) (c : Fin 8 ⊕ Fin 3 ⊕ Fin 1),
      ℂ ∙ gaugeFieldStrength ![] μ ν (GaugeAlgebra.stdBasis.coord c)
```

**`StandardModel.GaugeSector.F_coord_mul_F_coord_mem`**, a lemma, [line 652](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L652).

> A product of two underived symbols on standard coordinates. Two symbols of one
> non-abelian factor form a component of a pair family, two hypercharge symbols a
> hypercharge trace contraction, and every mixed product carries an unpaired non-abelian
> index.

```lean
lemma F_coord_mul_F_coord_mem (μ ν : Fin 1 ⊕ Fin 3) (c : Fin 8 ⊕ Fin 3 ⊕ Fin 1)
    (μ' ν' : Fin 1 ⊕ Fin 3) (c' : Fin 8 ⊕ Fin 3 ⊕ Fin 1) :
    gaugeFieldStrength ![] μ ν (GaugeAlgebra.stdBasis.coord c)
        * gaugeFieldStrength ![] μ' ν' (GaugeAlgebra.stdBasis.coord c')
      ∈ (unpairedColourSpan ⊔ unpairedIsospinSpan)
        ⊔ (gluonPairSpan ⊔ (wPairSpan ⊔ hyperchargeTraceSpan))
```

**`StandardModel.GaugeSector.massWeightSubmodule_eight_le`**, a lemma, [line 682](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L682).

> Mass weight eight is bounded by the joins of the unpaired families together with the
> pair spans, the hypercharge trace contractions and the twice-derived hypercharge field
> strengths.

```lean
lemma massWeightSubmodule_eight_le :
    massWeightSubmodule 8
      ≤ (unpairedColourSpan ⊔ unpairedIsospinSpan)
        ⊔ (gluonPairSpan
          ⊔ (wPairSpan ⊔ (hyperchargeTraceSpan ⊔ hyperchargeDerivSpan)))
```

## F. The unpaired non-abelian adjoint indices

> A family carrying one unpaired adjoint index of a non-abelian factor has no gauge invariant
> in its span at all, the adjoint representations of `su(3)` and `su(2)` having no invariant
> vector: `ColourAdj.reducesInvariantsTo_bot` and its `su(2)` twin reduce such a span to
> `⊥` for that factor. The colour families are reduced first, with the isospin join carried
> in the target, since the colour factor fixes every isospin family; the isospin families
> are reduced after that.

**`StandardModel.GaugeSector.reducesInvariantsTo_unpaired`**, a lemma, [line 712](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L712).

> The joins of the unpaired families reduce to `⊥` for the gauge group, the colour
> families for the colour factor, with the colour-fixed isospin join kept in the target, and
> then the isospin families for the isospin factor.

```lean
lemma reducesInvariantsTo_unpaired :
    ReducesInvariantsTo (fun g : GaugeGroupI => repGaugeGroupI g)
      (unpairedColourSpan ⊔ unpairedIsospinSpan) ⊥
```

## G. The gauge invariants of mass weight eight

> Section E bounds mass weight eight by the unpaired joins, the two non-abelian pair spans and
> the two hypercharge spans. Section F reduces the unpaired joins to `⊥`. Each pair span
> reduces to its trace contractions by `ColourAdjAdj.reducesInvariantsTo_span_traceContraction` and
> its `su(2)` twin, and the
> two hypercharge spans are fixed pointwise by the gauge group and reduce to themselves.
> `ReducesInvariantsTo.sup` joins the parts, asking stability of every part but the first and
> of the target; no independence of the parts is needed.
>
> The section closes with the converse, that the gauge span is made of gauge invariants of mass
> weight eight already.

**`StandardModel.GaugeSector.gluonTraceSpan`**, a def, [line 753](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L753).

> The span of the gluon trace contractions.

```lean
noncomputable def gluonTraceSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.wTraceSpan`**, a def, [line 757](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L757).

> The span of the `W`-boson trace contractions.

```lean
noncomputable def wTraceSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.traceContractionEightSpan`**, a def, [line 761](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L761).

> The span of the three underived trace contractions, over all covector indices, the
> gauge invariants of mass weight eight that the bi-adjoint classification produces.

```lean
noncomputable def traceContractionEightSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.isStableUnder_gluonPairSpan`**, a lemma, [line 765](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L765).

> The gluon pair spans are stable under the gauge group.

```lean
lemma isStableUnder_gluonPairSpan :
    IsStableUnder (fun g : GaugeGroupI => repGaugeGroupI g) gluonPairSpan
```

**`StandardModel.GaugeSector.isStableUnder_wPairSpan`**, a lemma, [line 771](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L771).

> The `W`-boson pair spans are stable under the gauge group.

```lean
lemma isStableUnder_wPairSpan :
    IsStableUnder (fun g : GaugeGroupI => repGaugeGroupI g) wPairSpan
```

**`StandardModel.GaugeSector.repGauge_of_mem_hyperchargeTraceSpan`**, a lemma, [line 777](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L777).

> The hypercharge trace contractions are fixed pointwise by the gauge group.

```lean
lemma repGauge_of_mem_hyperchargeTraceSpan (g : GaugeGroupI) :
    ∀ y ∈ hyperchargeTraceSpan, repGaugeGroupI g y = y
```

**`StandardModel.GaugeSector.repGauge_of_mem_hyperchargeDerivSpan`**, a lemma, [line 783](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L783).

> The twice-derived hypercharge field strengths are fixed pointwise by the gauge
> group.

```lean
lemma repGauge_of_mem_hyperchargeDerivSpan (g : GaugeGroupI) :
    ∀ y ∈ hyperchargeDerivSpan, repGaugeGroupI g y = y
```

**`StandardModel.GaugeSector.traceContractionEightSpan_sup_hyperchargeDerivSpan_le`**, a lemma, [line 790](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L790).

> The gauge span is a space of gauge invariants of mass weight eight. Each generator is
> fixed by the gauge group and has mass weight eight by section C. This is the converse of
> the classification.

```lean
lemma traceContractionEightSpan_sup_hyperchargeDerivSpan_le :
    traceContractionEightSpan ⊔ hyperchargeDerivSpan
      ≤ massWeightSubmodule 8 ⊓ repGaugeGroupI.invariants
```

**`StandardModel.GaugeSector.isFixedBy_traceContractionEightSpan_sup`**, a lemma, [line 807](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L807).

> The gauge span is fixed pointwise by the gauge group.

```lean
lemma isFixedBy_traceContractionEightSpan_sup :
    IsFixedBy (fun g : GaugeGroupI => repGaugeGroupI g)
      (traceContractionEightSpan ⊔ hyperchargeDerivSpan)
```

**`StandardModel.GaugeSector.reducesInvariantsTo_gluonPairSpan`**, a lemma, [line 815](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L815).

> The gluon pair spans reduce, for the gauge group, to the gluon trace contractions, since each
> gluon pair family is bi-adjoint for the colour factor.

```lean
lemma reducesInvariantsTo_gluonPairSpan :
    ReducesInvariantsTo (fun g : GaugeGroupI => repGaugeGroupI g) gluonPairSpan gluonTraceSpan
```

**`StandardModel.GaugeSector.reducesInvariantsTo_wPairSpan`**, a lemma, [line 827](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L827).

> The `W`-boson pair spans reduce, for the gauge group, to the `W`-boson trace contractions, since
> each `W`-boson pair family is bi-adjoint for the isospin factor.

```lean
lemma reducesInvariantsTo_wPairSpan :
    ReducesInvariantsTo (fun g : GaugeGroupI => repGaugeGroupI g) wPairSpan wTraceSpan
```

**`StandardModel.GaugeSector.reducesInvariantsTo_traceContractionEightSpan_sup`**, a lemma, [line 841](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L841).

> Mass weight eight reduces, for the gauge group, to the three underived trace
> contractions and the twice-derived hypercharge field strengths. Of the parts bounding it,
> the unpaired joins reduce to `⊥`, the pair spans to their trace contractions, and the
> hypercharge spans are already fixed.

```lean
lemma reducesInvariantsTo_traceContractionEightSpan_sup :
    ReducesInvariantsTo (fun g : GaugeGroupI => repGaugeGroupI g) (massWeightSubmodule 8)
      (traceContractionEightSpan ⊔ hyperchargeDerivSpan)
```

## H. The Lorentz classification of the mass-weight eight invariants

> A product of two underived field-strength symbols carries four covector indices and
> nothing else, so as a family indexed by those four it is a quadruple Lorentz tensor in the
> sense that its map out of `ℂT(fun _ : Fin 4 => .up)` is equivariant: `repLorentz_F` at no covariant
> derivatives moves each covector index by the Lorentz matrix of the `SL(2,ℂ)` element, and
> `repLorentzGroup_mul` carries that
> through the product. The three trace contractions are sums of such products over a gauge
> index, and a finite sum of quadruple Lorentz tensors is one again. So is the twice-derived
> hypercharge field strength, whose two derivative slots and two covector indices are four
> four-vector indices as well. The four spans of section G are exactly the spans of these
> four families, and `ComplexVector.reducesInvariantsTo_span_contractionTensor` reduces each, for the
> Lorentz group, to the span of its four contractions.
>
> What is left is spanned by the four Lorentz contractions of each family,
> `liftComponents T (RankFour.contractionTensor i)`: the metric contractions of the slot pairs
> `(0,1)(2,3)`, `(0,2)(1,3)` and `(0,3)(1,2)` and the Levi-Civita contraction. These are
> sixteen spanning vectors, `lorentzContractionEightSpan`, which is the output of the
> classification.
>
> Half of them are redundant. In each of the four families the last two slots are the two
> covector indices of one field strength: of the second factor for the three trace families,
> and of the only factor, after the two derivative slots, for the twice-derived hypercharge
> field strength. So `F_antisymm` makes each family antisymmetric under exchanging slots `2` and
> `3` (`gluonTrace_comp_swap_two_three` and its three companions), and
> `RankFour.span_range_contractionTensor_of_antisymm` then removes two contractions of each.
> The `(0,1)(2,3)` contraction vanishes, and the `(0,3)(1,2)` one is minus the `(0,2)(1,3)`
> one (`quadContractionSpan_eq_of_antisymm`). Eight spanning vectors remain
> (`lorentzContractionEightSpan_eq`).
>
> * six underived ones, quadratic in the field strengths. For each of the gluon, `W`-boson and
>   hypercharge trace families these are the `(0,2)(1,3)` metric contraction, of the kinetic
>   shape `η^{μρ} η^{νσ} F_{μν} F_{ρσ}`, and the Levi-Civita contraction, of the theta shape
>   `ε^{μνρσ} F_{μν} F_{ρσ}`, the gauge index summed in both;
> * two linear in the twice-derived hypercharge field strength, `η^{μρ} η^{νσ} ∇_μ ∇_ν B_{ρσ}`
>   and `ε^{μνρσ} ∇_μ ∇_ν B_{ρσ}`.
>
> Each is the plain component sum of `RankFour.liftComponents_contractionTensor`, repeated
> indices summed, against the integer metric `diag(1,-1,-1,-1)` or the symbol taking the value
> `1` at `(t, x, y, z)`, with no further normalisation; the shapes are not claimed to carry the
> conventional factors of an action. The last two are kept because nothing in the laws of the gauge
> sector relates the two derivative slots, no symmetry of the derivatives, no Bianchi identity, no
> equation of motion and no quotient by total derivatives. In the covariant field algebra of the
> Standard Model the hypercharge derivatives do commute and the last two vanish
> (`LocalCovFieldAlgebra.gaugeSector_lorentzContractionEightSpan_eq_traceFamilies`). The eight
> form a spanning family, not a basis. None is shown to be nonzero, and no independence among them
> is claimed.

**`StandardModel.GaugeSector.repLorentz_F_underived`**, a lemma, [line 915](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L915).

> The Lorentz transformation of an underived field-strength symbol. It is the general law
> `repLorentz_F` at no covariant derivatives, where the sum over the derivative slots is
> a single term, written with the two covector rotations gathered into one coefficient.

```lean
lemma repLorentz_F_underived (Λ : SL(2,ℂ)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) :
    repLorentzGroup Λ (gaugeFieldStrength ![] μ ν φ)
      = ∑ a : Fin 1 ⊕ Fin 3, ∑ b : Fin 1 ⊕ Fin 3,
        ((((SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) *
          (((SL2C.toLorentzGroup Λ).1 b ν : ℝ) : ℂ)) • gaugeFieldStrength ![] a b φ
```

**`StandardModel.GaugeSector.sum_mul_sum_eq_sum_pi_four`**, a lemma, [line 930](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L930).

> A product of two double combinations is a combination indexed by quadruples.

```lean
lemma sum_mul_sum_eq_sum_pi_four (c c' : (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → ℂ)
    (X Y : (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → fieldData.LocalCovFieldAlgebra) :
    (∑ a, ∑ b, c a b • X a b) * (∑ x, ∑ y, c' x y • Y x y)
      = ∑ d : Fin 4 → Fin 1 ⊕ Fin 3,
        (c (d 0) (d 1) * c' (d 2) (d 3)) • (X (d 0) (d 1) * Y (d 2) (d 3))
```

**`StandardModel.GaugeSector.isEquivariant_up_F_mul`**, a lemma, [line 943](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L943).

> A product of two underived field-strength symbols, viewed as a family indexed by the
> four covector indices it carries, is a quadruple Lorentz tensor.

```lean
lemma isEquivariant_up_F_mul (φ ψ : Module.Dual ℝ GaugeAlgebra) :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 4 => .up) repLorentzGroup
      (liftComponents
      fun d : Fin 4 → Fin 1 ⊕ Fin 3 => gaugeFieldStrength ![] (d 0) (d 1) φ * gaugeFieldStrength ![]
        (d 2) (d 3) ψ)
```

**`StandardModel.GaugeSector.isEquivariant_up_sum`**, a lemma, [line 956](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L956).

> A finite sum of quadruple Lorentz tensors is a quadruple Lorentz tensor, the
> transformation law is linear in the family.

```lean
lemma isEquivariant_up_sum {ι : Type} [Fintype ι] {T : ι → (Fin 4 → Fin 1 ⊕ Fin 3) →
    fieldData.LocalCovFieldAlgebra}
    (hT : ∀ i, complexLorentzTensor.IsEquivariant (fun _ : Fin 4 => .up) repLorentzGroup
      (liftComponents (T i))) :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 4 => .up) repLorentzGroup
      (liftComponents fun d => ∑ i, T i d)
```

**`StandardModel.GaugeSector.isEquivariant_up_of_eq_sum`**, a lemma, [line 967](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L967).

> A family of four four-vector indices whose members are sums of products of two
> underived field-strength symbols is a quadruple Lorentz tensor.

```lean
lemma isEquivariant_up_of_eq_sum {ι : Type} [Fintype ι]
    {T : EightIdx → fieldData.LocalCovFieldAlgebra}
    (φ : ι → Module.Dual ℝ GaugeAlgebra)
    (hT : ∀ d, T d = ∑ i, gaugeFieldStrength ![] (d 0) (d 1) (φ i) * gaugeFieldStrength ![] (d 2) (d
      3) (φ i)) :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 4 => .up) repLorentzGroup
      (liftComponents T)
```

**`StandardModel.GaugeSector.isEquivariant_up_gluonTrace`**, a lemma, [line 981](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L981).

> The gluon trace contractions, read as a family of four four-vector indices, form a quadruple
> Lorentz tensor, being a sum over the colour index of products of two underived field-strength
> symbols.

```lean
lemma isEquivariant_up_gluonTrace :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 4 => .up) repLorentzGroup
      (liftComponents gluonTrace)
```

**`StandardModel.GaugeSector.isEquivariant_up_wTrace`**, a lemma, [line 988](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L988).

> The `W`-boson trace contractions form a quadruple Lorentz tensor.

```lean
lemma isEquivariant_up_wTrace :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 4 => .up) repLorentzGroup
      (liftComponents wTrace)
```

**`StandardModel.GaugeSector.isEquivariant_up_hyperchargeTrace`**, a lemma, [line 995](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L995).

> The hypercharge trace contractions form a quadruple Lorentz tensor.

```lean
lemma isEquivariant_up_hyperchargeTrace :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 4 => .up) repLorentzGroup
      (liftComponents hyperchargeTrace)
```

**`StandardModel.GaugeSector.isEquivariant_up_hyperchargeDeriv`**, a lemma, [line 1008](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1008).

> The twice-derived hypercharge field strengths, read as a family of four four-vector
> indices, form a quadruple Lorentz tensor, since the two derivative slots and the two covector
> indices all rotate. This is the second shape of mass weight eight.

```lean
lemma isEquivariant_up_hyperchargeDeriv :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 4 => .up) repLorentzGroup
      (liftComponents hyperchargeDeriv)
```

**`StandardModel.GaugeSector.gluonTrace_comp_swap_two_three`**, a lemma, [line 1020](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1020).

> The gluon trace contractions are antisymmetric in the last two covector indices, by
> `F_antisymm` in the second factor.

```lean
lemma gluonTrace_comp_swap_two_three (d : EightIdx) :
    gluonTrace (d ∘ Equiv.swap 2 3) = -gluonTrace d
```

**`StandardModel.GaugeSector.wTrace_comp_swap_two_three`**, a lemma, [line 1025](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1025).

> The `W`-boson trace contractions are antisymmetric in the last two covector indices.

```lean
lemma wTrace_comp_swap_two_three (d : EightIdx) :
    wTrace (d ∘ Equiv.swap 2 3) = -wTrace d
```

**`StandardModel.GaugeSector.hyperchargeTrace_comp_swap_two_three`**, a lemma, [line 1030](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1030).

> The hypercharge trace contractions are antisymmetric in the last two covector indices.

```lean
lemma hyperchargeTrace_comp_swap_two_three (d : EightIdx) :
    hyperchargeTrace (d ∘ Equiv.swap 2 3) = -hyperchargeTrace d
```

**`StandardModel.GaugeSector.hyperchargeDeriv_comp_swap_two_three`**, a lemma, [line 1038](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1038).

> The twice-derived hypercharge field strengths are antisymmetric in their two covector
> indices, the last two slots, by `F_antisymm` at two covariant derivatives. Nothing is
> assumed about the two derivative slots.

```lean
lemma hyperchargeDeriv_comp_swap_two_three (d : EightIdx) :
    hyperchargeDeriv (d ∘ Equiv.swap 2 3) = -hyperchargeDeriv d
```

**`StandardModel.GaugeSector.quadContractionSpan`**, a def, [line 1045](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1045).

> The span of the four Lorentz contractions of a quadruple Lorentz tensor, the images of
> the three metric pairings and of the Levi-Civita symbol.

```lean
noncomputable def quadContractionSpan
    (T : (Fin 4 → Fin 1 ⊕ Fin 3) → fieldData.LocalCovFieldAlgebra) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.quadContractionSpan_le_span`**, a lemma, [line 1053](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1053).

> The span of the four Lorentz contractions of a quadruple Lorentz family lies in the
> span of its components, since each contraction is a combination of components with constant
> coefficients.

```lean
lemma quadContractionSpan_le_span {T : (Fin 4 → Fin 1 ⊕ Fin 3) → fieldData.LocalCovFieldAlgebra} :
    quadContractionSpan T ≤ Submodule.span ℂ (Set.range T)
```

**`StandardModel.GaugeSector.quadContractionSpan_le_lorentzInvariants`**, a lemma, [line 1062](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1062).

> The span of the four Lorentz contractions of a quadruple Lorentz family is a space of
> Lorentz invariants, the four contractions being invariant by `RankFour`.

```lean
lemma quadContractionSpan_le_lorentzInvariants
    {T : (Fin 4 → Fin 1 ⊕ Fin 3) → fieldData.LocalCovFieldAlgebra}
    (hT : complexLorentzTensor.IsEquivariant (fun _ : Fin 4 => .up) repLorentzGroup
      (liftComponents T)) :
    quadContractionSpan T ≤ repLorentzGroup.invariants
```

**`StandardModel.GaugeSector.quadContractionSpan_eq_of_antisymm`**, a lemma, [line 1075](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1075).

> For a quadruple family antisymmetric in its last two slots the four Lorentz contractions
> reduce to two, the `(0,2)(1,3)` metric contraction and the Levi-Civita one. The
> `(0,1)(2,3)` metric contraction vanishes and the `(0,3)(1,2)` one is minus the
> `(0,2)(1,3)` one.

```lean
lemma quadContractionSpan_eq_of_antisymm
    {T : (Fin 4 → Fin 1 ⊕ Fin 3) → fieldData.LocalCovFieldAlgebra}
    (hT : ∀ d, T (d ∘ Equiv.swap 2 3) = -T d) :
    quadContractionSpan T = Submodule.span ℂ {liftComponents T (RankFour.contractionTensor 1),
      liftComponents T (RankFour.contractionTensor 3)}
```

**`StandardModel.GaugeSector.lorentzContractionEightSpan`**, a def, [line 1085](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1085).

> The span of the four Lorentz contractions of each of the three underived
> trace-contraction families and of the twice-derived hypercharge family, the gauge and
> Lorentz invariants of mass weight eight that the two classifications together produce.

```lean
noncomputable def lorentzContractionEightSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.GaugeSector.lorentzContractionEightSpan_le_traceContractionEightSpan_sup`**, a lemma, [line 1093](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1093).

> The Lorentz contraction span sits inside the gauge span. Each of its four blocks is
> spanned by the four contractions of a quadruple Lorentz family whose components generate
> the matching block of the gauge span.

```lean
lemma lorentzContractionEightSpan_le_traceContractionEightSpan_sup :
    lorentzContractionEightSpan ≤ traceContractionEightSpan ⊔ hyperchargeDerivSpan
```

**`StandardModel.GaugeSector.lorentzContractionEightSpan_le_invariants`**, a lemma, [line 1108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1108).

> The Lorentz contraction span is a space of gauge invariants, since it lies in the gauge
> span, whose generators the gauge group fixes.

```lean
lemma lorentzContractionEightSpan_le_invariants :
    lorentzContractionEightSpan ≤ repGaugeGroupI.invariants
```

**`StandardModel.GaugeSector.lorentzContractionEightSpan_eq`**, a lemma, [line 1118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1118).

> The Lorentz contraction span is spanned by eight of its sixteen generators, for each
> family the `(0,2)(1,3)` metric contraction and the Levi-Civita contraction. All four families
> are antisymmetric in their last two slots by `F_antisymm`, which removes the other two
> contractions of each.

```lean
lemma lorentzContractionEightSpan_eq :
    lorentzContractionEightSpan
      = Submodule.span ℂ {liftComponents gluonTrace (contractionTensor 1),
          liftComponents gluonTrace (contractionTensor 3)}
        ⊔ (Submodule.span ℂ {liftComponents wTrace (contractionTensor 1),
            liftComponents wTrace (contractionTensor 3)}
          ⊔ (Submodule.span ℂ {liftComponents hyperchargeTrace (contractionTensor 1),
              liftComponents hyperchargeTrace (contractionTensor 3)}
            ⊔ Submodule.span ℂ {liftComponents hyperchargeDeriv (contractionTensor 1),
              liftComponents hyperchargeDeriv (contractionTensor 3)}))
```

## I. The Lorentz contraction span as invariants of mass weight eight

> The converse of the Lorentz classification is that the Lorentz contraction span is made of gauge
> and Lorentz invariants of mass weight eight. Its gauge invariance and its mass weight pass
> to it from the gauge span, which contains it; Lorentz invariance comes from `RankFour`
> directly, each block being spanned by the four contractions of a quadruple Lorentz family.

**`StandardModel.GaugeSector.lorentzContractionEightSpan_le_massWeightSubmodule`**, a lemma, [line 1146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1146).

> The Lorentz contraction span lies in the mass-weight eight submodule.

```lean
lemma lorentzContractionEightSpan_le_massWeightSubmodule :
    lorentzContractionEightSpan ≤ massWeightSubmodule 8
```

**`StandardModel.GaugeSector.lorentzContractionEightSpan_le_lorentzInvariants`**, a lemma, [line 1152](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1152).

> The Lorentz contraction span is a space of Lorentz invariants.

```lean
lemma lorentzContractionEightSpan_le_lorentzInvariants :
    lorentzContractionEightSpan ≤ repLorentzGroup.invariants
```

**`StandardModel.GaugeSector.isFixedBy_lorentzContractionEightSpan`**, a lemma, [line 1160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1160).

> The Lorentz contraction span is fixed pointwise by both groups.

```lean
lemma isFixedBy_lorentzContractionEightSpan :
    IsFixedBy (gaugeLorentzMaps repGaugeGroupI repLorentzGroup) lorentzContractionEightSpan
```

## J. The classifications as equivalences

> The gauge reduction of section G and the Lorentz reduction of section H compose, and the
> composite needs no stability or fixedness of the gauge span under the Lorentz group. The
> converse, sections G and I, turns each reduction into an equivalence through
> `ReducesInvariantsTo.mem_sup_and_forall_eq_self_iff`.

**`StandardModel.GaugeSector.reducesInvariantsTo_lorentzContractionEightSpan`**, a lemma, [line 1185](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1185).

> The gauge sector at mass weight eight reduces, for the gauge and Lorentz groups
> together, to the four Lorentz contractions of each of the four families. The gauge group
> leaves the trace contractions and the twice-derived hypercharge field strengths; each of
> the four spans is spanned by a quadruple Lorentz tensor and reduces, for the Lorentz
> group, to the span of its four contractions. Two of the four suffice for each family, by
> `lorentzContractionEightSpan_eq`.

```lean
lemma reducesInvariantsTo_lorentzContractionEightSpan :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup) (massWeightSubmodule 8)
      lorentzContractionEightSpan
```

**`StandardModel.GaugeSector.mem_massWeightSubmodule_eight_sup_and_invariant_iff`**, a lemma, [line 1237](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1237).

> The gauge classification of mass weight eight as an equivalence. An element of
> `massWeightSubmodule 8 ⊔ S` is gauge invariant exactly when it is a combination of the
> three underived trace contractions and the twice-derived hypercharge field strengths up
> to a gauge-invariant remainder in `S`.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_invariant_iff
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule 8 ⊔ S ∧ ∀ g : GaugeGroupI, repGaugeGroupI g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ x - y ∈ traceContractionEightSpan ⊔ hyperchargeDerivSpan
```

**`StandardModel.GaugeSector.mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 1252](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1252).

> The gauge and Lorentz classification of mass weight eight as an equivalence. An
> element of `massWeightSubmodule 8 ⊔ S` is fixed by both groups exactly when it is a
> combination of the four Lorentz contractions of the four families of section H up to a
> remainder in `S` fixed by both groups. The version with two contractions of each family is
> `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_reduced`.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x - y ∈ lorentzContractionEightSpan
```

**`StandardModel.GaugeSector.mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_reduced`**, a lemma, [line 1273](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean#L1273).

> The same equivalence with the eight generators of `lorentzContractionEightSpan_eq`, for
> each of the three underived trace families its `(0,2)(1,3)` metric contraction, of the shape
> `η^{μρ} η^{νσ} F_{μν} F_{ρσ}`, and its Levi-Civita contraction, of the shape
> `ε^{μνρσ} F_{μν} F_{ρσ}`, and for the twice-derived hypercharge field strengths
> `η^{μρ} η^{νσ} ∇_μ ∇_ν B_{ρσ}` and `ε^{μνρσ} ∇_μ ∇_ν B_{ρσ}`. The eight span; they are not
> shown to be independent or nonzero.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_reduced
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x - y ∈ Submodule.span ℂ {liftComponents gluonTrace (contractionTensor 1),
              liftComponents gluonTrace (contractionTensor 3)}
            ⊔ (Submodule.span ℂ {liftComponents wTrace (contractionTensor 1),
                liftComponents wTrace (contractionTensor 3)}
              ⊔ (Submodule.span ℂ {liftComponents hyperchargeTrace (contractionTensor 1),
                  liftComponents hyperchargeTrace (contractionTensor 3)}
                ⊔ Submodule.span ℂ {liftComponents hyperchargeDeriv (contractionTensor 1),
                  liftComponents hyperchargeDeriv (contractionTensor 3)}))
```

## Depends on

- [Families of adjoint components and their invariants](../part-02/gaugegroup-invariants-adjoint.md)
- [The mass-weight grading of the gauge sector](localfieldalgebra-gaugesector-massweight-basic.md)
- [The contraction tensors of four four-vector indices](../../../relativity/tensors/complextensor-vector-contractiontensor.md)

## Proof depends on

- [The invariants below mass weight eight (GaugeSector/MassWeight/MassDimLTEight)](localfieldalgebra-gaugesector-massweight-massdim-2.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeSector/MassWeight/MassDimEight.lean)
