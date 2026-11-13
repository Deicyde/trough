---
declaration: module
origin: cited
lean: StandardModel.IsGaugeSector.iSup_span_singleton_le, StandardModel.IsGaugeSector.mem_iSup_span₃, StandardModel.IsGaugeSector.span_stable_of_map_eq_sum, StandardModel.IsGaugeSector.map_eq_self_of_mem_iSup_span, StandardModel.IsGaugeSector.span_singleton_mul_span_singleton_le, StandardModel.IsGaugeSector.iSup_span_mul_iSup_span_le, StandardModel.IsGaugeSector.sum_mul_sum_eq_sum_pi_two, StandardModel.IsGaugeSector.map_mul_fixed_eq_sum
statement: formalized
proof: formalized
---

# Products of two field strengths as bi-adjoint gauge tensors

The module `PhyslibAlpha.Particles.StandardModel.IsGaugeSector.MassWeight.MassDimEight`, [PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean): 124 declarations, 124 with a docstring.

## i. Overview

> A single field-strength symbol of the gauge sector carries one adjoint index of the gauge
> algebra, so a product of two of them carries two. Restricting the value index to one
> factor of the gauge group turns such a product into a family indexed by two adjoint
> indices of that factor, and the gauge transformation law of the sector says exactly that
> these families are bi-adjoint in the sense of `IsSU3BiAdjoint`, `IsSU2BiAdjoint` and
> `IsU1BiAdjoint`. The gauge invariant those propositions supply is the trace contraction,
> the Kronecker contraction of the two adjoint indices, the familiar kinetic pairing of two
> field strengths; it has mass weight eight and is fixed by the whole gauge group.
>
> Conversely the colour and isospin generators of the zero-weight piece of mass weight eight
> lie inside the spans of the underived gluon and `W`-boson families, and what does not is
> either a hypercharge invariant or carries an unpaired adjoint index of a non-abelian
> factor, which contributes nothing by `IsSU3Adjoint` and `IsSU2Adjoint`. Putting the two
> directions together classifies the gauge invariants of mass weight eight modulo any
> gauge-stable submodule: such an invariant is a combination of the three underived trace
> contractions and the twice-derived hypercharge field strengths. Both shapes carry four
> covector indices and no others, so both are quadruple Lorentz tensors, and the Lorentz
> classification cuts the combinations down further, to the four Lorentz contractions of
> each of the four families. All four families are antisymmetric in their last two slots, by
> `F_antisymm`, and that leaves two contractions of each, eight spanning generators in all
> (`lorentzContractionEightSpan_eq`).
>
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

> - `lorentzContractionEightSpan_eq` : the Lorentz contraction span is spanned by eight of its sixteen
>   generators: for each family the `(0,2)(1,3)` metric contraction and the Levi-Civita contraction
> - `mem_massWeightSubmodule_eight_sup_and_invariant_iff` : the gauge classification of mass weight
>   eight as an equivalence: an element of `massWeightSubmodule 8 ⊔ S` is gauge invariant exactly when
>   it is a combination of the three underived trace contractions and the twice-derived hypercharge
>   field strengths up to a gauge-invariant remainder in `S`
> - `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff` : the gauge and Lorentz
>   classification of mass weight eight as an equivalence: an element of `massWeightSubmodule 8 ⊔ S`
>   is fixed by both groups exactly when it is a combination of the four Lorentz contractions of the
>   four families of section H up to a remainder in `S` fixed by both groups
> - `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_reduced` : the same equivalence
>   with the eight generators of `lorentzContractionEightSpan_eq`: for each of the three underived
>   trace families its `(0,2)(1,3)` metric contraction, of the shape `η^{μρ} η^{νσ} F_{μν} F_{ρσ}`,
>   and its Levi-Civita contraction, of the shape `ε^{μνρσ} F_{μν} F_{ρσ}`, and for the twice-derived
>   hypercharge field strengths `η^{μρ} η^{νσ} ∇_μ ∇_ν B_{ρσ}` and `ε^{μνρσ} ∇_μ ∇_ν B_{ρσ}`

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

**`StandardModel.IsGaugeSector.iSup_span_singleton_le`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L129).

> A span lies in a submodule as soon as its generators do.

```lean
lemma iSup_span_singleton_le {ι : Sort*} (T : ι → B) {V : Submodule ℂ B}
    (hV : ∀ i, T i ∈ V) : (⨆ i, ℂ ∙ T i) ≤ V
```

**`StandardModel.IsGaugeSector.mem_iSup_span₃`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L134).

> A generator of a family with three indices lies in its span.

```lean
lemma mem_iSup_span₃ {α β γ : Sort*} (T : α → β → γ → B) (a : α) (b : β) (c : γ) :
    T a b c ∈ ⨆ (a) (b) (c), ℂ ∙ T a b c
```

**`StandardModel.IsGaugeSector.span_stable_of_map_eq_sum`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L141).

> A linear map moving each generator to a combination of the generators carries the span
> into itself; the transformation laws of this file all have this shape.

```lean
lemma span_stable_of_map_eq_sum {ι : Type} [Fintype ι] (T : ι → B) (f : B →ₗ[ℂ] B)
    {c : ι → ι → ℂ} (hf : ∀ l, f (T l) = ∑ a, c a l • T a) :
    ∀ y ∈ Submodule.span ℂ (Set.range T), f y ∈ Submodule.span ℂ (Set.range T)
```

**`StandardModel.IsGaugeSector.map_eq_self_of_mem_iSup_span`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L147).

> A linear map fixing each generator fixes the span pointwise.

```lean
lemma map_eq_self_of_mem_iSup_span {ι : Sort*} (T : ι → B) (f : B →ₗ[ℂ] B)
    (hf : ∀ i, f (T i) = T i) : ∀ y ∈ ⨆ i, ℂ ∙ T i, f y = y
```

**`StandardModel.IsGaugeSector.span_singleton_mul_span_singleton_le`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L154).

> The product of two lines lies in a submodule as soon as the product of the two
> generators does.

```lean
lemma span_singleton_mul_span_singleton_le {a b : B} {V : Submodule ℂ B} (hab : a * b ∈ V) :
    (ℂ ∙ a) * (ℂ ∙ b) ≤ V
```

**`StandardModel.IsGaugeSector.iSup_span_mul_iSup_span_le`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L161).

> The product of two spans lies in a submodule as soon as the products of their
> generators do.

```lean
lemma iSup_span_mul_iSup_span_le {α β γ α' β' γ' : Sort*} (T : α → β → γ → B)
    (T' : α' → β' → γ' → B) {V : Submodule ℂ B} (hV : ∀ a b c a' b' c', T a b c * T' a' b' c' ∈ V) :
    (⨆ (a) (b) (c), ℂ ∙ T a b c) * (⨆ (a) (b) (c), ℂ ∙ T' a b c) ≤ V
```

**`StandardModel.IsGaugeSector.sum_mul_sum_eq_sum_pi_two`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L170).

> A product of two combinations is a combination indexed by pairs.

```lean
lemma sum_mul_sum_eq_sum_pi_two {k : ℕ} (c₀ c₁ : Fin k → ℂ) (X Y : Fin k → B) :
    (∑ a, c₀ a • X a) * ∑ b, c₁ b • Y b
      = ∑ d : Fin 2 → Fin k, (c₀ (d 0) * c₁ (d 1)) • (X (d 0) * Y (d 1))
```

**`StandardModel.IsGaugeSector.map_mul_fixed_eq_sum`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L180).

> A multiplicative map moving a family by a matrix and fixing a vector moves the
> products of the family with that vector by the same matrix.

```lean
lemma map_mul_fixed_eq_sum {k : ℕ} {f : B →ₗ[ℂ] B} (hf : ∀ x y, f (x * y) = f x * f y)
    {c : Fin k → Fin k → ℂ} {T : Fin k → B} (hT : ∀ l, f (T l) = ∑ a, c a l • T a) {v : B}
    (hv : f v = v) (l : Fin k) : f (T l * v) = ∑ a, c a l • (T a * v)
```

**`StandardModel.IsGaugeSector.map_fixed_mul_eq_sum`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L187).

> The mirror of `map_mul_fixed_eq_sum` with the fixed vector on the left.

```lean
lemma map_fixed_mul_eq_sum {k : ℕ} {f : B →ₗ[ℂ] B} (hf : ∀ x y, f (x * y) = f x * f y)
    {c : Fin k → Fin k → ℂ} {T : Fin k → B} (hT : ∀ l, f (T l) = ∑ a, c a l • T a) {v : B}
    (hv : f v = v) (l : Fin k) : f (v * T l) = ∑ a, c a l • (v * T a)
```

## B. The gauge transformation of the gauge-factor field strengths

> The gauge law of `IsGaugeSector` moves the field-strength symbol by the coadjoint action of
> the gauge group on its argument, which on the standard basis coordinates is the adjoint
> matrix. That matrix is block diagonal, so the gluon field strengths transform among
> themselves by the `su(3)` adjoint matrix of the colour factor, the `W`-boson field
> strengths by the `su(2)` adjoint matrix of the isospin factor, and the hypercharge field
> strength is fixed. The colour factor alone fixes the `W`-boson field strengths as well.

**`StandardModel.IsGaugeSector.repGauge_F_coord`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L209).

> The field-strength symbol evaluated on a standard-basis coordinate transforms under
> the gauge group through the column of `adjointMatrix` indexed by that coordinate.

```lean
lemma repGauge_F_coord (g : GaugeGroupI) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) (c : Fin 8 ⊕ Fin 3 ⊕ Fin 1) :
    repGauge g (F l μ ν (GaugeAlgebra.stdBasis.coord c))
      = ∑ b, ((GaugeAlgebra.adjointMatrix g b c : ℝ) : ℂ) •
          F l μ ν (GaugeAlgebra.stdBasis.coord b)
```

**`StandardModel.IsGaugeSector.repGauge_gluonField`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L223).

> The gluon field strength transforms in the adjoint representation of the `su(3)`
> factor of the gauge group.

```lean
lemma repGauge_gluonField (g : GaugeGroupI) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) (c : Fin 8) :
    repGauge g (h.gluonField l μ ν c)
      = ∑ a : Fin 8, ((su3AdjointMatrix (GaugeGroupI.toSU3 g) a c : ℝ) : ℂ) •
          h.gluonField l μ ν a
```

**`StandardModel.IsGaugeSector.repGauge_wField`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L234).

> The `W`-boson field strength transforms in the adjoint representation of the `su(2)`
> factor of the gauge group.

```lean
lemma repGauge_wField (g : GaugeGroupI) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) (c : Fin 3) :
    repGauge g (h.wField l μ ν c)
      = ∑ i : Fin 3, ((su2AdjointMatrix (GaugeGroupI.toSU2 g) i c : ℝ) : ℂ) •
          h.wField l μ ν i
```

**`StandardModel.IsGaugeSector.repGauge_hyperchargeField`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L245).

> The hypercharge field strength is gauge invariant: the adjoint action of the gauge
> group on the `u(1)` factor of the gauge algebra is trivial.

```lean
lemma repGauge_hyperchargeField (g : GaugeGroupI) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) :
    repGauge g (h.hyperchargeField l μ ν) = h.hyperchargeField l μ ν
```

**`StandardModel.IsGaugeSector.repGauge_su3_wField`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L254).

> The `W`-boson field strengths are fixed by the colour factor of the gauge group: the
> `su(2)` block of the adjoint matrix reads the isospin factor alone.

```lean
lemma repGauge_su3_wField (U : specialUnitaryGroup (Fin 3) ℂ) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3) (i : Fin 3) :
    repGauge (U, 1, 1) (h.wField l μ ν i) = h.wField l μ ν i
```

**`StandardModel.IsGaugeSector.isSU3Adjoint_gluonField`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L270).

> The gluon field strengths at fixed derivative slots and covector indices form a family
> of one `su(3)` adjoint index.

```lean
lemma isSU3Adjoint_gluonField {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3) :
    IsSU3Adjoint B repGauge (h.gluonField l μ ν)
```

**`StandardModel.IsGaugeSector.isSU2Adjoint_wField`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L276).

> The `W`-boson field strengths at fixed derivative slots and covector indices form a
> family of one `su(2)` adjoint index.

```lean
lemma isSU2Adjoint_wField {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3) :
    IsSU2Adjoint B repGauge (h.wField l μ ν)
```

## C. Products of two underived field strengths as bi-adjoint families

> A product of two underived field strengths of one gauge factor, at the four covector
> indices `p`, is a family indexed by the two adjoint indices of that factor, and by section
> B and the multiplicativity of the gauge action it is a bi-adjoint family in the sense of
> `IsSU3BiAdjoint`, `IsSU2BiAdjoint` and `IsU1BiAdjoint`, with the transformation law
> holding at every gauge element and not only at those of its own factor. Its trace
> contraction, the Kronecker contraction of the two adjoint indices, is fixed by the whole
> gauge group and has mass weight eight, the sum of the mass weights of its two factors; so
> is the twice-derived hypercharge field strength, the other shape of mass weight eight.

**`StandardModel.IsGaugeSector.EightIdx`**, an abbrev, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L298).

> The index of a product of two underived field strengths: the two covector indices of
> the first factor followed by the two of the second, read as one family of four
> four-vector indices so that the Lorentz classification applies to it.

```lean
abbrev EightIdx : Type
```

**`StandardModel.IsGaugeSector.gluonPair`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L302).

> The product of two underived gluon field strengths at the covector indices `p`, indexed
> by the two `su(3)` adjoint indices it carries.

```lean
noncomputable def gluonPair (p : EightIdx) (a : Fin 2 → Fin 8) : B
```

**`StandardModel.IsGaugeSector.wPair`**, a def, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L307).

> The product of two underived `W`-boson field strengths at the covector indices `p`,
> indexed by the two `su(2)` adjoint indices it carries.

```lean
noncomputable def wPair (p : EightIdx) (a : Fin 2 → Fin 3) : B
```

**`StandardModel.IsGaugeSector.hyperchargePair`**, a def, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L312).

> The product of two underived hypercharge field strengths at the covector indices `p`,
> indexed by the two `u(1)` adjoint indices it carries.

```lean
noncomputable def hyperchargePair (p : EightIdx) (_ : Fin 2 → Fin 1) : B
```

**`StandardModel.IsGaugeSector.hyperchargeDeriv`**, a def, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L317).

> The twice-derived hypercharge field strength at the derivative slots `d 0`, `d 1` and
> the covector indices `d 2`, `d 3`.

```lean
noncomputable def hyperchargeDeriv (d : EightIdx) : B
```

**`StandardModel.IsGaugeSector.isSU3BiAdjointMat_gluonPair`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L322).

> A gauge transformation moves a gluon pair as the `SU(3)` factor of that gauge group
> element moves a tensor with two `su(3)` adjoint indices.

```lean
lemma isSU3BiAdjointMat_gluonPair (p : EightIdx) (g : GaugeGroupI) :
    IsSU3BiAdjointMat (GaugeGroupI.toSU3 g) (repGauge g) (h.gluonPair p)
```

**`StandardModel.IsGaugeSector.isSU3BiAdjoint_gluonPair`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L328).

> A gluon pair is a bi-adjoint `su(3)` tensor.

```lean
lemma isSU3BiAdjoint_gluonPair (p : EightIdx) : IsSU3BiAdjoint B repGauge (h.gluonPair p)
```

**`StandardModel.IsGaugeSector.isSU2BiAdjointMat_wPair`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L333).

> A gauge transformation moves a `W`-boson pair as the `SU(2)` factor of that gauge group
> element moves a tensor with two `su(2)` adjoint indices.

```lean
lemma isSU2BiAdjointMat_wPair (p : EightIdx) (g : GaugeGroupI) :
    IsSU2BiAdjointMat (GaugeGroupI.toSU2 g) (repGauge g) (h.wPair p)
```

**`StandardModel.IsGaugeSector.isSU2BiAdjoint_wPair`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L339).

> A `W`-boson pair is a bi-adjoint `su(2)` tensor.

```lean
lemma isSU2BiAdjoint_wPair (p : EightIdx) : IsSU2BiAdjoint B repGauge (h.wPair p)
```

**`StandardModel.IsGaugeSector.isU1BiAdjointMat_hyperchargePair`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L343).

> A gauge transformation fixes a hypercharge pair, which is the `u(1)` bi-adjoint law.

```lean
lemma isU1BiAdjointMat_hyperchargePair (p : EightIdx) (g : GaugeGroupI) :
    IsU1BiAdjointMat (GaugeGroupI.toU1 g) (repGauge g) (h.hyperchargePair p)
```

**`StandardModel.IsGaugeSector.isU1BiAdjoint_hyperchargePair`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L349).

> A hypercharge pair is a bi-adjoint `u(1)` tensor.

```lean
lemma isU1BiAdjoint_hyperchargePair (p : EightIdx) :
    IsU1BiAdjoint B repGauge (h.hyperchargePair p)
```

**`StandardModel.IsGaugeSector.gluonTrace`**, a def, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L355).

> The gluon trace contraction at the covector indices `p`: the Kronecker contraction of
> the two colour indices of the gluon pair.

```lean
noncomputable def gluonTrace (p : EightIdx) : B
```

**`StandardModel.IsGaugeSector.wTrace`**, a def, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L358).

> The `W`-boson trace contraction at the covector indices `p`.

```lean
noncomputable def wTrace (p : EightIdx) : B
```

**`StandardModel.IsGaugeSector.hyperchargeTrace`**, a def, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L361).

> The hypercharge trace contraction at the covector indices `p`.

```lean
noncomputable def hyperchargeTrace (p : EightIdx) : B
```

**`StandardModel.IsGaugeSector.gluonTrace_eq`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L365).

> The gluon trace contraction is the kinetic pairing of two gluon field strengths.

```lean
lemma gluonTrace_eq (p : EightIdx) :
    h.gluonTrace p
      = ∑ a : Fin 8, h.gluonField ![] (p 0) (p 1) a * h.gluonField ![] (p 2) (p 3) a
```

**`StandardModel.IsGaugeSector.wTrace_eq`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L372).

> The `W`-boson trace contraction is the kinetic pairing of two `W`-boson field
> strengths.

```lean
lemma wTrace_eq (p : EightIdx) :
    h.wTrace p = ∑ i : Fin 3, h.wField ![] (p 0) (p 1) i * h.wField ![] (p 2) (p 3) i
```

**`StandardModel.IsGaugeSector.hyperchargeTrace_eq`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L378).

> The hypercharge trace contraction is the product of the two hypercharge field
> strengths, the `u(1)` factor being one dimensional.

```lean
lemma hyperchargeTrace_eq (p : EightIdx) :
    h.hyperchargeTrace p
      = h.hyperchargeField ![] (p 0) (p 1) * h.hyperchargeField ![] (p 2) (p 3)
```

**`StandardModel.IsGaugeSector.repGauge_gluonTrace`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L384).

> The gluon trace contraction is fixed by the whole gauge group.

```lean
lemma repGauge_gluonTrace (g : GaugeGroupI) (p : EightIdx) :
    repGauge g (h.gluonTrace p) = h.gluonTrace p
```

**`StandardModel.IsGaugeSector.repGauge_wTrace`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L389).

> The `W`-boson trace contraction is fixed by the whole gauge group.

```lean
lemma repGauge_wTrace (g : GaugeGroupI) (p : EightIdx) :
    repGauge g (h.wTrace p) = h.wTrace p
```

**`StandardModel.IsGaugeSector.repGauge_hyperchargeTrace`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L394).

> The hypercharge trace contraction is fixed by the whole gauge group.

```lean
lemma repGauge_hyperchargeTrace (g : GaugeGroupI) (p : EightIdx) :
    repGauge g (h.hyperchargeTrace p) = h.hyperchargeTrace p
```

**`StandardModel.IsGaugeSector.repGauge_hyperchargeDeriv`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L399).

> The twice-derived hypercharge field strength is fixed by the whole gauge group.

```lean
lemma repGauge_hyperchargeDeriv (g : GaugeGroupI) (d : EightIdx) :
    repGauge g (h.hyperchargeDeriv d) = h.hyperchargeDeriv d
```

**`StandardModel.IsGaugeSector.F_mem_derivSubmodule`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L405).

> Every field-strength symbol lies in the derivative submodule of its own number of
> covariant derivatives.

```lean
lemma F_mem_derivSubmodule {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) : F l μ ν φ ∈ h.derivSubmodule n
```

**`StandardModel.IsGaugeSector.F_mem_massWeightSubmodule`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L412).

> A field-strength symbol with `n` covariant derivatives has mass weight `2 * (2 + n)`.

```lean
lemma F_mem_massWeightSubmodule {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) : F l μ ν φ ∈ h.massWeightSubmodule (2 * (2 + n))
```

**`StandardModel.IsGaugeSector.F_mul_F_mem_massWeightSubmodule_eight`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L417).

> A product of two underived field-strength symbols has mass weight eight.

```lean
lemma F_mul_F_mem_massWeightSubmodule_eight (μ ν μ' ν' : Fin 1 ⊕ Fin 3)
    (φ φ' : Module.Dual ℝ GaugeAlgebra) :
    F ![] μ ν φ * F ![] μ' ν' φ' ∈ h.massWeightSubmodule 8
```

**`StandardModel.IsGaugeSector.gluonTrace_mem_massWeightSubmodule`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L424).

> The gluon trace contraction has mass weight eight.

```lean
lemma gluonTrace_mem_massWeightSubmodule (p : EightIdx) :
    h.gluonTrace p ∈ h.massWeightSubmodule 8
```

**`StandardModel.IsGaugeSector.wTrace_mem_massWeightSubmodule`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L430).

> The `W`-boson trace contraction has mass weight eight.

```lean
lemma wTrace_mem_massWeightSubmodule (p : EightIdx) : h.wTrace p ∈ h.massWeightSubmodule 8
```

**`StandardModel.IsGaugeSector.hyperchargeTrace_mem_massWeightSubmodule`**, a lemma, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L435).

> The hypercharge trace contraction has mass weight eight.

```lean
lemma hyperchargeTrace_mem_massWeightSubmodule (p : EightIdx) :
    h.hyperchargeTrace p ∈ h.massWeightSubmodule 8
```

**`StandardModel.IsGaugeSector.hyperchargeDeriv_mem_massWeightSubmodule`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L441).

> The twice-derived hypercharge field strength has mass weight `2 * (2 + 2)`, eight.

```lean
lemma hyperchargeDeriv_mem_massWeightSubmodule (d : EightIdx) :
    h.hyperchargeDeriv d ∈ h.massWeightSubmodule 8
```

## D. The weight vectors of mass weight eight inside the bi-adjoint spans

> The gauge weight decomposition of the underived tower is built from the weight vectors
> `adjVec` of one adjoint index. On a colour direction such a vector is a combination of
> gluon field strengths, on the isospin directions a combination of `W`-boson field
> strengths, and on the hypercharge direction the hypercharge field strength itself, the
> combinations being the weight coordinates `GaugeAlgebra.su3WeightCoeff` and
> `GaugeAlgebra.su2WeightCoeff`. A product of two of them is then a combination of the
> components of the matching pair family, so it lies in the span of that family. At mass weight
> eight this covers the gluon root part and the isospin root part of the zero-weight piece
> computed by `massWeightSubmoduleGaugeWeightEight_piece_zero`.

**`StandardModel.IsGaugeSector.su3AdjIdx`**, a def, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L464).

> The `su(3)` adjoint weight indices read as weight indices of the whole gauge
> algebra: the three colour roots and the two colour Cartan directions.

```lean
def su3AdjIdx : GaugeAlgebra.su3WeightIdx → Fin 4 ⊕ Fin 4 ⊕ Fin 4
```

**`StandardModel.IsGaugeSector.su2AdjIdx`**, a def, [line 471](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L471).

> The `su(2)` adjoint weight indices read as weight indices of the whole gauge
> algebra: the isospin root and the isospin Cartan direction.

```lean
def su2AdjIdx : GaugeAlgebra.su2WeightIdx → Fin 4 ⊕ Fin 4 ⊕ Fin 4
```

**`StandardModel.IsGaugeSector.sum_su3WeightCoeff_smul_gluonField`**, a lemma, [line 478](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L478).

> A weight vector of the colour part of the adjoint is the matching combination of
> gluon field strengths.

```lean
lemma sum_su3WeightCoeff_smul_gluonField {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) (k : GaugeAlgebra.su3WeightIdx) :
    ∑ a : Fin 8, GaugeAlgebra.su3WeightCoeff k a • h.gluonField l μ ν a
      = h.adjVec l μ ν (su3AdjIdx k)
```

**`StandardModel.IsGaugeSector.sum_su2WeightCoeff_smul_wField`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L489).

> A weight vector of the isospin part of the adjoint is the matching combination of
> `W`-boson field strengths.

```lean
lemma sum_su2WeightCoeff_smul_wField {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) (k : GaugeAlgebra.su2WeightIdx) :
    ∑ i : Fin 3, GaugeAlgebra.su2WeightCoeff k i • h.wField l μ ν i
      = h.adjVec l μ ν (su2AdjIdx k)
```

**`StandardModel.IsGaugeSector.adjVec_mul_adjVec_mem_gluonPair_span`**, a lemma, [line 500](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L500).

> A product of two colour weight vectors of the adjoint lies in the span of the matching
> gluon pair family.

```lean
lemma adjVec_mul_adjVec_mem_gluonPair_span (p : EightIdx)
    (k₀ k₁ : GaugeAlgebra.su3WeightIdx) :
    h.adjVec ![] (p 0) (p 1) (su3AdjIdx k₀) * h.adjVec ![] (p 2) (p 3) (su3AdjIdx k₁)
      ∈ Submodule.span ℂ (Set.range (h.gluonPair p))
```

**`StandardModel.IsGaugeSector.adjVec_mul_adjVec_mem_wPair_span`**, a lemma, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L510).

> A product of two isospin weight vectors of the adjoint lies in the span of the matching
> `W`-boson pair family.

```lean
lemma adjVec_mul_adjVec_mem_wPair_span (p : EightIdx) (k₀ k₁ : GaugeAlgebra.su2WeightIdx) :
    h.adjVec ![] (p 0) (p 1) (su2AdjIdx k₀) * h.adjVec ![] (p 2) (p 3) (su2AdjIdx k₁)
      ∈ Submodule.span ℂ (Set.range (h.wPair p))
```

**`StandardModel.IsGaugeSector.gluonPairSpan`**, a def, [line 518](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L518).

> The join, over all covector indices, of the spans of the gluon pair families.

```lean
noncomputable def gluonPairSpan : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.wPairSpan`**, a def, [line 521](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L521).

> The join, over all covector indices, of the spans of the `W`-boson pair families.

```lean
noncomputable def wPairSpan : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.gluonRootPart_le_gluonPairSpan`**, a lemma, [line 525](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L525).

> The gluon root part of the zero-weight piece, the three products of a colour raising
> vector against the matching lowering vector, lies in the gluon pair spans.

```lean
lemma gluonRootPart_le_gluonPairSpan : h.gluonRootPart ≤ h.gluonPairSpan
```

**`StandardModel.IsGaugeSector.isospinRootPart_le_wPairSpan`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L536).

> The isospin root part of the zero-weight piece, the product of the isospin raising
> vector against the lowering vector, lies in the `W`-boson pair spans.

```lean
lemma isospinRootPart_le_wPairSpan : h.isospinRootPart ≤ h.wPairSpan
```

## E. The zero-weight piece of mass weight eight

> `massWeightSubmoduleGaugeWeightEight_piece_zero` splits the zero-weight piece into the
> twice-derived symbols on the four weight-zero directions of the adjoint, the gluon root
> part, the isospin root part and the neutral part, the products of two weight-zero
> directions. Section D puts the two root parts inside the pair spans. The neutral part
> splits by gauge group factor: a colour Cartan direction against a colour Cartan direction
> is a component of a gluon pair family, the isospin Cartan direction against itself of a
> `W`-boson pair family, and hypercharge against itself is a hypercharge trace contraction.
> What is left pairs a weight-zero direction of one factor with one of another and carries
> an unpaired adjoint index of a non-abelian factor; so does a twice-derived symbol on a
> colour or isospin Cartan direction, while the twice-derived hypercharge field strengths
> are fixed by the whole gauge group.
>
> The families with an unpaired index are collected in `colourFamily` and `isospinFamily`,
> adjoint families in the sense of `IsSU3Adjoint` and `IsSU2Adjoint`: the colour factor moves
> the gluon index of a mixed product and fixes the neutral factor. The piece is then bounded
> by the joins of these families together with the four spans of gauge invariants.

**`StandardModel.IsGaugeSector.hyperchargeTraceSpan`**, a def, [line 566](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L566).

> The span of the hypercharge trace contractions.

```lean
noncomputable def hyperchargeTraceSpan : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.hyperchargeDerivSpan`**, a def, [line 569](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L569).

> The span of the twice-derived hypercharge field strengths.

```lean
noncomputable def hyperchargeDerivSpan : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.neutralVec`**, a def, [line 573](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L573).

> The two neutral underived directions that pair with a colour index in the mixed
> neutral products: the isospin Cartan direction and hypercharge.

```lean
noncomputable def neutralVec (μ ν : Fin 1 ⊕ Fin 3) : Fin 2 → B
```

**`StandardModel.IsGaugeSector.repGauge_su3_neutralVec`**, a lemma, [line 578](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L578).

> The neutral directions are fixed by the colour factor of the gauge group.

```lean
lemma repGauge_su3_neutralVec (U : specialUnitaryGroup (Fin 3) ℂ) (μ ν : Fin 1 ⊕ Fin 3)
    (j : Fin 2) : repGauge (U, 1, 1) (h.neutralVec μ ν j) = h.neutralVec μ ν j
```

**`StandardModel.IsGaugeSector.DerivIdx`**, an abbrev, [line 586](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L586).

> The index of a twice-derived symbol: the two derivative slots and the two covector
> indices.

```lean
abbrev DerivIdx : Type
```

**`StandardModel.IsGaugeSector.MixIdx`**, an abbrev, [line 591](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L591).

> The index of a mixed neutral product: the two covector indices of the colour factor,
> the two of the neutral factor, and which of the two neutral directions it is.

```lean
abbrev MixIdx : Type
```

**`StandardModel.IsGaugeSector.ColourIdx`**, an abbrev, [line 597](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L597).

> The index of a family carrying one unpaired `su(3)` adjoint index at mass weight
> eight: a twice-derived gluon tower, or an underived gluon field strength against a
> neutral underived factor on either side.

```lean
abbrev ColourIdx : Type
```

**`StandardModel.IsGaugeSector.colourFamily`**, a def, [line 600](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L600).

> The families carrying one unpaired `su(3)` adjoint index.

```lean
noncomputable def colourFamily : ColourIdx → Fin 8 → B
```

**`StandardModel.IsGaugeSector.isSU3Adjoint_colourFamily`**, a lemma, [line 609](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L609).

> Each colour family is an `su(3)` adjoint family: the colour factor moves the gluon
> index and fixes the neutral factor.

```lean
lemma isSU3Adjoint_colourFamily : ∀ i : ColourIdx, IsSU3Adjoint B repGauge (h.colourFamily i)
```

**`StandardModel.IsGaugeSector.IsospinIdx`**, an abbrev, [line 619](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L619).

> The index of a family carrying one unpaired `su(2)` adjoint index at mass weight
> eight: a twice-derived `W`-boson tower, or an underived `W`-boson field strength against
> an underived hypercharge field strength on either side.

```lean
abbrev IsospinIdx : Type
```

**`StandardModel.IsGaugeSector.isospinFamily`**, a def, [line 622](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L622).

> The families carrying one unpaired `su(2)` adjoint index.

```lean
noncomputable def isospinFamily : IsospinIdx → Fin 3 → B
```

**`StandardModel.IsGaugeSector.isSU2Adjoint_isospinFamily`**, a lemma, [line 629](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L629).

> Each isospin family is an `su(2)` adjoint family: the isospin factor moves the
> `W`-boson index and fixes hypercharge.

```lean
lemma isSU2Adjoint_isospinFamily : ∀ i : IsospinIdx, IsSU2Adjoint B repGauge (h.isospinFamily i)
```

**`StandardModel.IsGaugeSector.repGauge_su3_isospinFamily`**, a lemma, [line 638](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L638).

> The isospin families are fixed by the colour factor, every one of their factors
> being.

```lean
lemma repGauge_su3_isospinFamily (U : specialUnitaryGroup (Fin 3) ℂ) :
    ∀ (i : IsospinIdx) (a : Fin 3),
      repGauge (U, 1, 1) (h.isospinFamily i a) = h.isospinFamily i a
```

**`StandardModel.IsGaugeSector.unpairedColourSpan`**, a def, [line 648](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L648).

> The join of the spans of the colour families.

```lean
noncomputable def unpairedColourSpan : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.unpairedIsospinSpan`**, a def, [line 652](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L652).

> The join of the spans of the isospin families.

```lean
noncomputable def unpairedIsospinSpan : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.colourFamily_mem`**, a lemma, [line 656](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L656).

> A component of a colour family lies in the join of the colour spans.

```lean
lemma colourFamily_mem (i : ColourIdx) (a : Fin 8) : h.colourFamily i a ∈ h.unpairedColourSpan
```

**`StandardModel.IsGaugeSector.isospinFamily_mem`**, a lemma, [line 660](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L660).

> A component of an isospin family lies in the join of the isospin spans.

```lean
lemma isospinFamily_mem (i : IsospinIdx) (a : Fin 3) :
    h.isospinFamily i a ∈ h.unpairedIsospinSpan
```

**`StandardModel.IsGaugeSector.repGauge_su3_of_mem_unpairedIsospinSpan`**, a lemma, [line 665](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L665).

> The join of the isospin families is fixed pointwise by the colour factor.

```lean
lemma repGauge_su3_of_mem_unpairedIsospinSpan (U : specialUnitaryGroup (Fin 3) ℂ) :
    ∀ y ∈ h.unpairedIsospinSpan, repGauge (U, 1, 1) y = y
```

**`StandardModel.IsGaugeSector.colourCartanSpan`**, a def, [line 672](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L672).

> The colour Cartan directions of the underived tower: the two weight-zero directions of
> the `su(3)` factor.

```lean
noncomputable def colourCartanSpan : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.neutralSpan`**, a def, [line 678](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L678).

> The neutral directions of the underived tower: the isospin Cartan direction and
> hypercharge.

```lean
noncomputable def neutralSpan : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.adjVec_colourCartan`**, a lemma, [line 683](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L683).

> A colour Cartan weight vector is the gluon field strength on the matching Cartan
> direction of `su(3)`.

```lean
lemma adjVec_colourCartan {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (c : Fin 2) :
    h.adjVec l μ ν (Sum.inr (Sum.inr c.castSucc.castSucc))
      = h.gluonField l μ ν (GaugeAlgebra.su3CartanId c)
```

**`StandardModel.IsGaugeSector.cartanSpan_le`**, a lemma, [line 692](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L692).

> The weight-zero directions of the adjoint are the colour Cartan directions and the
> neutral directions.

```lean
lemma cartanSpan_le : h.cartanSpan ≤ h.colourCartanSpan ⊔ h.neutralSpan
```

**`StandardModel.IsGaugeSector.colourCartanSpan_mul_colourCartanSpan_le`**, a lemma, [line 702](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L702).

> A product of two colour Cartan directions is a component of a gluon pair family.

```lean
lemma colourCartanSpan_mul_colourCartanSpan_le :
    h.colourCartanSpan * h.colourCartanSpan ≤ h.gluonPairSpan
```

**`StandardModel.IsGaugeSector.colourCartanSpan_mul_neutralSpan_le`**, a lemma, [line 710](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L710).

> A colour Cartan direction against a neutral direction is a component of a colour
> family.

```lean
lemma colourCartanSpan_mul_neutralSpan_le :
    h.colourCartanSpan * h.neutralSpan ≤ h.unpairedColourSpan
```

**`StandardModel.IsGaugeSector.neutralSpan_mul_colourCartanSpan_le`**, a lemma, [line 718](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L718).

> A neutral direction against a colour Cartan direction is a component of a colour
> family.

```lean
lemma neutralSpan_mul_colourCartanSpan_le :
    h.neutralSpan * h.colourCartanSpan ≤ h.unpairedColourSpan
```

**`StandardModel.IsGaugeSector.neutralSpan_mul_neutralSpan_le`**, a lemma, [line 727](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L727).

> A product of two neutral directions: isospin against isospin is a component of a
> `W`-boson pair family, hypercharge against hypercharge is a hypercharge trace
> contraction, and the two mixed products are components of isospin families.

```lean
lemma neutralSpan_mul_neutralSpan_le :
    h.neutralSpan * h.neutralSpan
      ≤ h.unpairedIsospinSpan ⊔ (h.wPairSpan ⊔ h.hyperchargeTraceSpan)
```

**`StandardModel.IsGaugeSector.neutralCartanPart_le`**, a lemma, [line 746](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L746).

> The neutral part of the zero-weight piece: the products pairing a factor with itself
> are components of the pair families or hypercharge trace contractions, and the mixed
> products carry an unpaired non-abelian index.

```lean
lemma neutralCartanPart_le :
    h.neutralCartanPart ≤ (h.unpairedColourSpan ⊔ h.unpairedIsospinSpan)
      ⊔ (h.gluonPairSpan ⊔ (h.wPairSpan ⊔ h.hyperchargeTraceSpan))
```

**`StandardModel.IsGaugeSector.derivCartanSpan_le`**, a lemma, [line 762](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L762).

> The twice-derived symbols on the weight-zero directions: on a colour or isospin Cartan
> direction a component of an adjoint family, on hypercharge a twice-derived hypercharge
> field strength.

```lean
lemma derivCartanSpan_le :
    (⨆ (l : Fin 2 → Fin 1 ⊕ Fin 3) (μ : Fin 1 ⊕ Fin 3) (ν : Fin 1 ⊕ Fin 3) (c : Fin 4),
        ℂ ∙ F l μ ν (GaugeAlgebra.stdBasis.coord (GaugeAlgebra.cartanIdx c)))
      ≤ (h.unpairedColourSpan ⊔ h.unpairedIsospinSpan) ⊔ h.hyperchargeDerivSpan
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightEight_piece_zero_le`**, a lemma, [line 782](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L782).

> The zero-weight piece of mass weight eight is bounded by the joins of the unpaired
> families together with the pair spans, the hypercharge trace contractions and the
> twice-derived hypercharge field strengths.

```lean
lemma massWeightSubmoduleGaugeWeightEight_piece_zero_le :
    (h.massWeightSubmoduleGaugeWeightEight).piece 0
      ≤ (h.unpairedColourSpan ⊔ h.unpairedIsospinSpan)
        ⊔ (h.gluonPairSpan
          ⊔ (h.wPairSpan ⊔ (h.hyperchargeTraceSpan ⊔ h.hyperchargeDerivSpan)))
```

## F. The unpaired non-abelian adjoint indices

> A family carrying one unpaired adjoint index of a non-abelian factor has no gauge invariant
> in its span at all, the adjoint representations of `su(3)` and `su(2)` having no invariant
> vector: `IsSU3Adjoint.reducesInvariantsTo_bot` and its `su(2)` twin reduce such a span to
> `⊥` for that factor. The colour families are reduced first, with the isospin join carried
> in the target, since the colour factor fixes every isospin family; the isospin families
> are reduced after that.

**`StandardModel.IsGaugeSector.reducesInvariantsTo_unpaired`**, a lemma, [line 813](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L813).

> The joins of the unpaired families reduce to `⊥` for the gauge group: the colour
> families for the colour factor, with the colour-fixed isospin join kept in the target, and
> then the isospin families for the isospin factor.

```lean
lemma reducesInvariantsTo_unpaired :
    ReducesInvariantsTo (fun g : GaugeGroupI => repGauge g)
      (h.unpairedColourSpan ⊔ h.unpairedIsospinSpan) ⊥
```

## G. The gauge invariants of mass weight eight

> A gauge invariant of mass weight eight lies, modulo any gauge-stable submodule, in the
> zero-weight piece of the gauge weight decomposition
> (`GaugeWeightDecomposition.reducesInvariantsTo_piece_zero`), which section E bounds by the
> unpaired joins, the two non-abelian pair spans and the two hypercharge spans. Section F
> reduces the unpaired joins to `⊥`. Each pair span reduces to its trace contractions by
> `IsSU3BiAdjoint.reducesInvariantsTo_span_traceContraction` and its `su(2)` twin, and the two
> hypercharge spans are fixed pointwise by the gauge group and reduce to themselves.
> `ReducesInvariantsTo.sup` joins the parts, asking stability of every part but the first and
> of the target; no independence of the parts is needed.
>
> The section closes with the converse: the gauge span is made of gauge invariants of mass
> weight eight already.

**`StandardModel.IsGaugeSector.gluonTraceSpan`**, a def, [line 856](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L856).

> The span of the gluon trace contractions.

```lean
noncomputable def gluonTraceSpan : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.wTraceSpan`**, a def, [line 859](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L859).

> The span of the `W`-boson trace contractions.

```lean
noncomputable def wTraceSpan : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.traceContractionEightSpan`**, a def, [line 863](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L863).

> The span of the three underived trace contractions, over all covector indices: the
> gauge invariants of mass weight eight that the bi-adjoint classification produces.

```lean
noncomputable def traceContractionEightSpan : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.isStableUnder_gluonPairSpan`**, a lemma, [line 867](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L867).

> The gluon pair spans are stable under the gauge group.

```lean
lemma isStableUnder_gluonPairSpan :
    IsStableUnder (fun g : GaugeGroupI => repGauge g) h.gluonPairSpan
```

**`StandardModel.IsGaugeSector.isStableUnder_wPairSpan`**, a lemma, [line 873](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L873).

> The `W`-boson pair spans are stable under the gauge group.

```lean
lemma isStableUnder_wPairSpan :
    IsStableUnder (fun g : GaugeGroupI => repGauge g) h.wPairSpan
```

**`StandardModel.IsGaugeSector.repGauge_of_mem_hyperchargeTraceSpan`**, a lemma, [line 879](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L879).

> The hypercharge trace contractions are fixed pointwise by the gauge group.

```lean
lemma repGauge_of_mem_hyperchargeTraceSpan (g : GaugeGroupI) :
    ∀ y ∈ h.hyperchargeTraceSpan, repGauge g y = y
```

**`StandardModel.IsGaugeSector.repGauge_of_mem_hyperchargeDerivSpan`**, a lemma, [line 885](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L885).

> The twice-derived hypercharge field strengths are fixed pointwise by the gauge
> group.

```lean
lemma repGauge_of_mem_hyperchargeDerivSpan (g : GaugeGroupI) :
    ∀ y ∈ h.hyperchargeDerivSpan, repGauge g y = y
```

**`StandardModel.IsGaugeSector.traceContractionEightSpan_sup_hyperchargeDerivSpan_le`**, a lemma, [line 892](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L892).

> The gauge span is a space of gauge invariants of mass weight eight: each generator is
> fixed by the gauge group and has mass weight eight by section C. This is the converse of
> the classification.

```lean
lemma traceContractionEightSpan_sup_hyperchargeDerivSpan_le :
    h.traceContractionEightSpan ⊔ h.hyperchargeDerivSpan
      ≤ h.massWeightSubmodule 8 ⊓ repGauge.invariants
```

**`StandardModel.IsGaugeSector.isFixedBy_traceContractionEightSpan_sup`**, a lemma, [line 909](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L909).

> The gauge span is fixed pointwise by the gauge group.

```lean
lemma isFixedBy_traceContractionEightSpan_sup :
    IsFixedBy (fun g : GaugeGroupI => repGauge g)
      (h.traceContractionEightSpan ⊔ h.hyperchargeDerivSpan)
```

**`StandardModel.IsGaugeSector.reducesInvariantsTo_gluonPairSpan`**, a lemma, [line 917](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L917).

> The gluon pair spans reduce, for the gauge group, to the gluon trace contractions: each
> gluon pair family is bi-adjoint for the colour factor.

```lean
lemma reducesInvariantsTo_gluonPairSpan :
    ReducesInvariantsTo (fun g : GaugeGroupI => repGauge g) h.gluonPairSpan h.gluonTraceSpan
```

**`StandardModel.IsGaugeSector.reducesInvariantsTo_wPairSpan`**, a lemma, [line 929](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L929).

> The `W`-boson pair spans reduce, for the gauge group, to the `W`-boson trace
> contractions: each `W`-boson pair family is bi-adjoint for the isospin factor.

```lean
lemma reducesInvariantsTo_wPairSpan :
    ReducesInvariantsTo (fun g : GaugeGroupI => repGauge g) h.wPairSpan h.wTraceSpan
```

**`StandardModel.IsGaugeSector.reducesInvariantsTo_traceContractionEightSpan_sup`**, a lemma, [line 944](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L944).

> Mass weight eight reduces, for the gauge group, to the three underived trace
> contractions and the twice-derived hypercharge field strengths. The torus puts a gauge
> invariant in the zero-weight piece; of the parts bounding it, the unpaired joins reduce to
> `⊥`, the pair spans to their trace contractions, and the hypercharge spans are already
> fixed.

```lean
lemma reducesInvariantsTo_traceContractionEightSpan_sup :
    ReducesInvariantsTo (fun g : GaugeGroupI => repGauge g) (h.massWeightSubmodule 8)
      (h.traceContractionEightSpan ⊔ h.hyperchargeDerivSpan)
```

## H. The Lorentz classification of the mass-weight eight invariants

> A product of two underived field-strength symbols carries four covector indices and
> nothing else, so as a family indexed by those four it is a quadruple Lorentz tensor in the
> sense of `IsLorentzCovariant 4`: `repLorentz_F` at no covariant derivatives moves each covector
> index by the Lorentz matrix of the `SL(2,ℂ)` element, and `hrepLorentz_mul` carries that
> through the product. The three trace contractions are sums of such products over a gauge
> index, and a finite sum of quadruple Lorentz tensors is one again. So is the twice-derived
> hypercharge field strength, whose two derivative slots and two covector indices are four
> four-vector indices as well. The four spans of section G are exactly the spans of these
> four families, and `RankFour.reducesInvariantsTo_span_contractionTensor` reduces each, for the
> Lorentz group, to the span of its four contractions.
>
> What is left is spanned by the four Lorentz contractions of each family,
> `ofComponents T (RankFour.contractionTensor i)`: the metric contractions of the slot pairs
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
> (`lorentzContractionEightSpan_eq`):
>
> * six underived ones, quadratic in the field strengths. For each of the gluon, `W`-boson and
>   hypercharge trace families these are the `(0,2)(1,3)` metric contraction, of the kinetic
>   shape `η^{μρ} η^{νσ} F_{μν} F_{ρσ}`, and the Levi-Civita contraction, of the theta shape
>   `ε^{μνρσ} F_{μν} F_{ρσ}`, the gauge index summed in both;
> * two linear in the twice-derived hypercharge field strength: `η^{μρ} η^{νσ} ∇_μ ∇_ν B_{ρσ}`
>   and `ε^{μνρσ} ∇_μ ∇_ν B_{ρσ}`.
>
> Each is the plain component sum of `RankFour.ofComponents_contractionTensor`, repeated
> indices summed, against the integer metric `diag(1,-1,-1,-1)` or the symbol taking the value
> `1` at `(t, x, y, z)`, with no further normalisation; the shapes are not claimed to carry the
> conventional factors of an action. The last two are kept because nothing in `IsGaugeSector`
> relates the two derivative slots: no symmetry of the derivatives, no Bianchi identity, no
> equation of motion and no quotient by total derivatives. In a covariant realization the
> hypercharge derivatives do commute and the last two vanish
> (`CovAlgebraRealization.isGaugeSector_lorentzContractionEightSpan_eq_traceFamilies`). The eight
> form a spanning family, not a basis: none is shown to be nonzero, and no independence among them
> is claimed.

**`StandardModel.IsGaugeSector.repLorentz_F_underived`**, a lemma, [line 1020](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1020).

> The Lorentz transformation of an underived field-strength symbol: the general law of
> `IsGaugeSector` at no covariant derivatives, where the sum over the derivative slots is
> a single term, written with the two covector rotations gathered into one coefficient.

```lean
lemma repLorentz_F_underived (Λ : SL(2,ℂ)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) :
    repLorentz Λ (F ![] μ ν φ)
      = ∑ a : Fin 1 ⊕ Fin 3, ∑ b : Fin 1 ⊕ Fin 3,
        ((((SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) *
          (((SL2C.toLorentzGroup Λ).1 b ν : ℝ) : ℂ)) • F ![] a b φ
```

**`StandardModel.IsGaugeSector.sum_mul_sum_eq_sum_pi_four`**, a lemma, [line 1035](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1035).

> A product of two double combinations is a combination indexed by quadruples.

```lean
lemma sum_mul_sum_eq_sum_pi_four (c c' : (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → ℂ)
    (X Y : (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → B) :
    (∑ a, ∑ b, c a b • X a b) * (∑ x, ∑ y, c' x y • Y x y)
      = ∑ d : Fin 4 → Fin 1 ⊕ Fin 3,
        (c (d 0) (d 1) * c' (d 2) (d 3)) • (X (d 0) (d 1) * Y (d 2) (d 3))
```

**`StandardModel.IsGaugeSector.isLorentzCovariant_F_mul`**, a lemma, [line 1049](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1049).

> A product of two underived field-strength symbols, viewed as a family indexed by the
> four covector indices it carries, is a quadruple Lorentz tensor.

```lean
lemma isLorentzCovariant_F_mul (φ ψ : Module.Dual ℝ GaugeAlgebra) :
    IsLorentzCovariant 4 B repLorentz (ofComponents
      fun d : Fin 4 → Fin 1 ⊕ Fin 3 => F ![] (d 0) (d 1) φ * F ![] (d 2) (d 3) ψ)
```

**`StandardModel.IsGaugeSector.isLorentzCovariant_sum`**, a lemma, [line 1060](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1060).

> A finite sum of quadruple Lorentz tensors is a quadruple Lorentz tensor: the
> transformation law is linear in the family.

```lean
lemma isLorentzCovariant_sum {ι : Type} [Fintype ι] {T : ι → (Fin 4 → Fin 1 ⊕ Fin 3) → B}
    (hT : ∀ i, IsLorentzCovariant 4 B repLorentz (ofComponents (T i))) :
    IsLorentzCovariant 4 B repLorentz (ofComponents fun d => ∑ i, T i d)
```

**`StandardModel.IsGaugeSector.isLorentzCovariant_of_eq_sum`**, a lemma, [line 1069](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1069).

> A family of four four-vector indices whose members are sums of products of two
> underived field-strength symbols is a quadruple Lorentz tensor.

```lean
lemma isLorentzCovariant_of_eq_sum {ι : Type} [Fintype ι] {T : EightIdx → B}
    (φ : ι → Module.Dual ℝ GaugeAlgebra)
    (hT : ∀ d, T d = ∑ i, F ![] (d 0) (d 1) (φ i) * F ![] (d 2) (d 3) (φ i)) :
    IsLorentzCovariant 4 B repLorentz (ofComponents T)
```

**`StandardModel.IsGaugeSector.isLorentzCovariant_gluonTrace`**, a lemma, [line 1079](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1079).

> The gluon trace contractions, read as a family of four four-vector indices, form a
> quadruple Lorentz tensor: a sum over the colour index of products of two underived
> field-strength symbols.

```lean
lemma isLorentzCovariant_gluonTrace :
    IsLorentzCovariant 4 B repLorentz (ofComponents h.gluonTrace)
```

**`StandardModel.IsGaugeSector.isLorentzCovariant_wTrace`**, a lemma, [line 1085](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1085).

> The `W`-boson trace contractions form a quadruple Lorentz tensor.

```lean
lemma isLorentzCovariant_wTrace : IsLorentzCovariant 4 B repLorentz (ofComponents h.wTrace)
```

**`StandardModel.IsGaugeSector.isLorentzCovariant_hyperchargeTrace`**, a lemma, [line 1090](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1090).

> The hypercharge trace contractions form a quadruple Lorentz tensor.

```lean
lemma isLorentzCovariant_hyperchargeTrace :
    IsLorentzCovariant 4 B repLorentz (ofComponents h.hyperchargeTrace)
```

**`StandardModel.IsGaugeSector.isLorentzCovariant_hyperchargeDeriv`**, a lemma, [line 1101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1101).

> The twice-derived hypercharge field strengths, read as a family of four four-vector
> indices, form a quadruple Lorentz tensor: the two derivative slots and the two covector
> indices all rotate. This is the second shape of mass weight eight.

```lean
lemma isLorentzCovariant_hyperchargeDeriv :
    IsLorentzCovariant 4 B repLorentz (ofComponents h.hyperchargeDeriv)
```

**`StandardModel.IsGaugeSector.gluonTrace_comp_swap_two_three`**, a lemma, [line 1112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1112).

> The gluon trace contractions are antisymmetric in the last two covector indices, by
> `F_antisymm` in the second factor.

```lean
lemma gluonTrace_comp_swap_two_three (d : EightIdx) :
    h.gluonTrace (d ∘ Equiv.swap 2 3) = -h.gluonTrace d
```

**`StandardModel.IsGaugeSector.wTrace_comp_swap_two_three`**, a lemma, [line 1117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1117).

> The `W`-boson trace contractions are antisymmetric in the last two covector indices.

```lean
lemma wTrace_comp_swap_two_three (d : EightIdx) :
    h.wTrace (d ∘ Equiv.swap 2 3) = -h.wTrace d
```

**`StandardModel.IsGaugeSector.hyperchargeTrace_comp_swap_two_three`**, a lemma, [line 1122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1122).

> The hypercharge trace contractions are antisymmetric in the last two covector indices.

```lean
lemma hyperchargeTrace_comp_swap_two_three (d : EightIdx) :
    h.hyperchargeTrace (d ∘ Equiv.swap 2 3) = -h.hyperchargeTrace d
```

**`StandardModel.IsGaugeSector.hyperchargeDeriv_comp_swap_two_three`**, a lemma, [line 1130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1130).

> The twice-derived hypercharge field strengths are antisymmetric in their two covector
> indices, the last two slots, by `F_antisymm` at two covariant derivatives. Nothing is
> assumed about the two derivative slots.

```lean
lemma hyperchargeDeriv_comp_swap_two_three (d : EightIdx) :
    h.hyperchargeDeriv (d ∘ Equiv.swap 2 3) = -h.hyperchargeDeriv d
```

**`StandardModel.IsGaugeSector.quadContractionSpan`**, a def, [line 1137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1137).

> The span of the four Lorentz contractions of a quadruple Lorentz tensor: the images of
> the three metric pairings and of the Levi-Civita symbol.

```lean
noncomputable def quadContractionSpan (T : (Fin 4 → Fin 1 ⊕ Fin 3) → B) : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.quadContractionSpan_le_span`**, a lemma, [line 1143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1143).

> The span of the four Lorentz contractions of a quadruple Lorentz family lies in the
> span of its components: each contraction is a combination of components with constant
> coefficients.

```lean
lemma quadContractionSpan_le_span {T : (Fin 4 → Fin 1 ⊕ Fin 3) → B} :
    quadContractionSpan T ≤ Submodule.span ℂ (Set.range T)
```

**`StandardModel.IsGaugeSector.quadContractionSpan_le_lorentzInvariants`**, a lemma, [line 1151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1151).

> The span of the four Lorentz contractions of a quadruple Lorentz family is a space of
> Lorentz invariants, the four contractions being invariant by `RankFour`.

```lean
lemma quadContractionSpan_le_lorentzInvariants {T : (Fin 4 → Fin 1 ⊕ Fin 3) → B}
    (hT : IsLorentzCovariant 4 B repLorentz (ofComponents T)) :
    quadContractionSpan T ≤ repLorentz.invariants
```

**`StandardModel.IsGaugeSector.quadContractionSpan_eq_of_antisymm`**, a lemma, [line 1162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1162).

> For a quadruple family antisymmetric in its last two slots the four Lorentz contractions
> reduce to two, the `(0,2)(1,3)` metric contraction and the Levi-Civita one: the
> `(0,1)(2,3)` metric contraction vanishes and the `(0,3)(1,2)` one is minus the
> `(0,2)(1,3)` one.

```lean
lemma quadContractionSpan_eq_of_antisymm {T : (Fin 4 → Fin 1 ⊕ Fin 3) → B}
    (hT : ∀ d, T (d ∘ Equiv.swap 2 3) = -T d) :
    quadContractionSpan T = Submodule.span ℂ {ofComponents T (RankFour.contractionTensor 1),
      ofComponents T (RankFour.contractionTensor 3)}
```

**`StandardModel.IsGaugeSector.lorentzContractionEightSpan`**, a def, [line 1171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1171).

> The span of the four Lorentz contractions of each of the three underived
> trace-contraction families and of the twice-derived hypercharge family: the gauge and
> Lorentz invariants of mass weight eight that the two classifications together produce.

```lean
noncomputable def lorentzContractionEightSpan : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.lorentzContractionEightSpan_le_traceContractionEightSpan_sup`**, a lemma, [line 1179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1179).

> The Lorentz contraction span sits inside the gauge span: each of its four blocks is
> spanned by the four contractions of a quadruple Lorentz family whose components generate
> the matching block of the gauge span.

```lean
lemma lorentzContractionEightSpan_le_traceContractionEightSpan_sup :
    h.lorentzContractionEightSpan ≤ h.traceContractionEightSpan ⊔ h.hyperchargeDerivSpan
```

**`StandardModel.IsGaugeSector.lorentzContractionEightSpan_le_invariants`**, a lemma, [line 1194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1194).

> The Lorentz contraction span is a space of gauge invariants: it lies in the gauge
> span, whose generators the gauge group fixes.

```lean
lemma lorentzContractionEightSpan_le_invariants :
    h.lorentzContractionEightSpan ≤ repGauge.invariants
```

**`StandardModel.IsGaugeSector.lorentzContractionEightSpan_eq`**, a lemma, [line 1204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1204).

> The Lorentz contraction span is spanned by eight of its sixteen generators: for each
> family the `(0,2)(1,3)` metric contraction and the Levi-Civita contraction. All four families
> are antisymmetric in their last two slots by `F_antisymm`, which removes the other two
> contractions of each.

```lean
lemma lorentzContractionEightSpan_eq :
    h.lorentzContractionEightSpan
      = Submodule.span ℂ {ofComponents h.gluonTrace (contractionTensor 1),
          ofComponents h.gluonTrace (contractionTensor 3)}
        ⊔ (Submodule.span ℂ {ofComponents h.wTrace (contractionTensor 1),
            ofComponents h.wTrace (contractionTensor 3)}
          ⊔ (Submodule.span ℂ {ofComponents h.hyperchargeTrace (contractionTensor 1),
              ofComponents h.hyperchargeTrace (contractionTensor 3)}
            ⊔ Submodule.span ℂ {ofComponents h.hyperchargeDeriv (contractionTensor 1),
              ofComponents h.hyperchargeDeriv (contractionTensor 3)}))
```

## I. The Lorentz contraction span as invariants of mass weight eight

> The converse of the Lorentz classification: the Lorentz contraction span is made of gauge
> and Lorentz invariants of mass weight eight. Its gauge invariance and its mass weight pass
> to it from the gauge span, which contains it; Lorentz invariance comes from `RankFour`
> directly, each block being spanned by the four contractions of a quadruple Lorentz family.

**`StandardModel.IsGaugeSector.lorentzContractionEightSpan_le_massWeightSubmodule`**, a lemma, [line 1232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1232).

> The Lorentz contraction span lies in the mass-weight eight submodule.

```lean
lemma lorentzContractionEightSpan_le_massWeightSubmodule :
    h.lorentzContractionEightSpan ≤ h.massWeightSubmodule 8
```

**`StandardModel.IsGaugeSector.lorentzContractionEightSpan_le_lorentzInvariants`**, a lemma, [line 1238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1238).

> The Lorentz contraction span is a space of Lorentz invariants.

```lean
lemma lorentzContractionEightSpan_le_lorentzInvariants :
    h.lorentzContractionEightSpan ≤ repLorentz.invariants
```

**`StandardModel.IsGaugeSector.isFixedBy_lorentzContractionEightSpan`**, a lemma, [line 1246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1246).

> The Lorentz contraction span is fixed pointwise by both groups.

```lean
lemma isFixedBy_lorentzContractionEightSpan :
    IsFixedBy (gaugeLorentzMaps repGauge repLorentz) h.lorentzContractionEightSpan
```

## J. The classifications as equivalences

> The gauge reduction of section G and the Lorentz reduction of section H compose, and the
> composite needs no stability or fixedness of the gauge span under the Lorentz group. The
> converse, sections G and I, turns each reduction into an equivalence through
> `ReducesInvariantsTo.mem_sup_and_forall_eq_self_iff`.

**`StandardModel.IsGaugeSector.reducesInvariantsTo_lorentzContractionEightSpan`**, a lemma, [line 1271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1271).

> The gauge sector at mass weight eight reduces, for the gauge and Lorentz groups
> together, to the four Lorentz contractions of each of the four families. The gauge group
> leaves the trace contractions and the twice-derived hypercharge field strengths; each of
> the four spans is spanned by a quadruple Lorentz tensor and reduces, for the Lorentz
> group, to the span of its four contractions. Two of the four suffice for each family, by
> `lorentzContractionEightSpan_eq`.

```lean
lemma reducesInvariantsTo_lorentzContractionEightSpan :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.massWeightSubmodule 8)
      h.lorentzContractionEightSpan
```

**`StandardModel.IsGaugeSector.mem_massWeightSubmodule_eight_sup_and_invariant_iff`**, a lemma, [line 1321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1321).

> The gauge classification of mass weight eight as an equivalence: an element of
> `massWeightSubmodule 8 ⊔ S` is gauge invariant exactly when it is a combination of the
> three underived trace contractions and the twice-derived hypercharge field strengths up
> to a gauge-invariant remainder in `S`.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_invariant_iff (S : Submodule ℂ B)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule 8 ⊔ S ∧ ∀ g : GaugeGroupI, repGauge g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ x - y ∈ h.traceContractionEightSpan ⊔ h.hyperchargeDerivSpan
```

**`StandardModel.IsGaugeSector.mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 1335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1335).

> The gauge and Lorentz classification of mass weight eight as an equivalence: an
> element of `massWeightSubmodule 8 ⊔ S` is fixed by both groups exactly when it is a
> combination of the four Lorentz contractions of the four families of section H up to a
> remainder in `S` fixed by both groups. The version with two contractions of each family is
> `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_reduced`.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff
    (S : Submodule ℂ B) (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ h.lorentzContractionEightSpan
```

**`StandardModel.IsGaugeSector.mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_reduced`**, a lemma, [line 1355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean#L1355).

> The same equivalence with the eight generators of `lorentzContractionEightSpan_eq`: for
> each of the three underived trace families its `(0,2)(1,3)` metric contraction, of the shape
> `η^{μρ} η^{νσ} F_{μν} F_{ρσ}`, and its Levi-Civita contraction, of the shape
> `ε^{μνρσ} F_{μν} F_{ρσ}`, and for the twice-derived hypercharge field strengths
> `η^{μρ} η^{νσ} ∇_μ ∇_ν B_{ρσ}` and `ε^{μνρσ} ∇_μ ∇_ν B_{ρσ}`. The eight span; they are not
> shown to be independent or nonzero.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_reduced
    (S : Submodule ℂ B) (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ Submodule.span ℂ {ofComponents h.gluonTrace (contractionTensor 1),
              ofComponents h.gluonTrace (contractionTensor 3)}
            ⊔ (Submodule.span ℂ {ofComponents h.wTrace (contractionTensor 1),
                ofComponents h.wTrace (contractionTensor 3)}
              ⊔ (Submodule.span ℂ {ofComponents h.hyperchargeTrace (contractionTensor 1),
                  ofComponents h.hyperchargeTrace (contractionTensor 3)}
                ⊔ Submodule.span ℂ {ofComponents h.hyperchargeDeriv (contractionTensor 1),
                  ofComponents h.hyperchargeDeriv (contractionTensor 3)}))
```

## Depends on

- [Families of adjoint components and their invariants](../part-04/gaugegroup-invariants-adjoint.md)
- [Families with two `u(1)` adjoint indices](../part-04/gaugegroup-invariants-isu1biadjoint.md)
- [Invariant reduction for the gauge and Lorentz groups](../part-01/invariantreduction.md)
- [The gauge weight decomposition of the gauge mass-weight submodules](../part-06/isgaugesector-massweight-gaugeweight.md)
- [Lorentz invariants of a rank-four tensor](../../../relativity/lorentzgroup/invariants-rankfour.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimEight.lean)
