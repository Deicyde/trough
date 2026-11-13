---
declaration: section
origin: cited
lean: CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantWith, CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantInd, CategoryTheory.EssentiallyConstantPro.IsEssentiallyConstantPro, CategoryTheory.IsEssentiallyConstantSystem, CategoryTheory.IsEssentiallyConstantInverseSystem, CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantInd.hasColimit, CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantInd.exists_retraction_colimit, CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantInd.hasLimit_of_op
statement: formalized
proof: formalized
---

# 4.22 Essentially constant systems

Section 4.22 of the Stacks Project, [Tag 05PT](https://stacks.math.columbia.edu/tag/05PT). 10 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05PU, a definition

[Tag 05PU](https://stacks.math.columbia.edu/tag/05PU) in the Stacks Project.

**`CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantWith`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/IndObject.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/IndObject.lean#L68). The attribute's comment: “(1), filtered case, conditions (a) and (b) with value t.pt”. References: SGA 4 I (8.4.4).

> `M` is essentially constant as an ind-object with value `t.pt`, with respect
> to the cocone `t`, witnessed by an index `i` and a morphism `r : t.pt ⟶ M i`, if
> `r` splits the coprojection `c_i` and is cofinal.

```lean
structure IsEssentiallyConstantWith (M : J ⥤ C) (t : Cocone M) (i : J)
    (r : t.pt ⟶ M.obj i) : Prop
```

**`CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantInd`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/IndObject.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/IndObject.lean#L84). The attribute's comment: “(1), filtered case: the predicate that M is essentially constant”. References: SGA 4 I (8.4.4); SGA 4 I (8.7.1.7).

> `M` is an *essentially constant ind-object* if there exist a cocone `t`, an
> index `i`, and a morphism `r : t.pt ⟶ M i` witnessing it.

```lean
def IsEssentiallyConstantInd (M : I ⥤ C) : Prop
```

**`CategoryTheory.EssentiallyConstantPro.IsEssentiallyConstantPro`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/ProObject.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/ProObject.lean#L78). The attribute's comment: “(2), cofiltered case: the predicate that M is essentially constant”.

> `M` is an *essentially constant pro-object* if there exist a cone `c`, an
> index `i`, and a morphism `s : M i ⟶ c.pt` witnessing it.

```lean
def IsEssentiallyConstantPro (M : I ⥤ C) : Prop
```

## Tag 05PV, a definition

[Tag 05PV](https://stacks.math.columbia.edu/tag/05PV) in the Stacks Project.

**`CategoryTheory.IsEssentiallyConstantSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Defs.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/Defs.lean#L79). The attribute's comment: “directed system”.

> A directed system `(M_i, f_ii')`, i.e. a functor `M : I ⥤ 𝒞` on a directed set, is an
> *essentially constant system* when the diagram `M` is essentially constant.

```lean
def IsEssentiallyConstantSystem (M : I ⥤ C) : Prop
```

**`CategoryTheory.IsEssentiallyConstantInverseSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Defs.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/Defs.lean#L87). The attribute's comment: “directed inverse system”.

> A directed inverse system `(M_i, f_ii')`, i.e. a functor `M : Iᵒᵖ ⥤ 𝒞` on the opposite of a
> directed set, is an *essentially constant inverse system* when the diagram `M` is essentially
> constant as a pro-object, i.e. when the opposite diagram `Mᵒᵖ` is an essentially constant
> diagram.

```lean
def IsEssentiallyConstantInverseSystem (M : Iᵒᵖ ⥤ C) : Prop
```

## Tag 0G2V, a lemma

[Tag 0G2V](https://stacks.math.columbia.edu/tag/0G2V) in the Stacks Project.

**`CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantInd.hasColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean#L69).

> (ind, part 1) An essentially constant `M` has a colimit.

```lean
theorem hasColimit {M : I ⥤ C} (h : IsEssentiallyConstantInd M) : HasColimit M
```

**`CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantInd.exists_retraction_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean#L77).

> (ind, part 2) The colimit cocone realizes `IsEssentiallyConstantInd M` with value
> `colimit M`: some `i₀` admits a retraction `b` of `colimit.ι M i₀` through which every
> `colimit.ι M j` factors.

```lean
theorem exists_retraction_colimit {M : I ⥤ C} (h : IsEssentiallyConstantInd M) [HasColimit M] :
    ∃ (i₀ : I) (b : colimit M ⟶ M.obj i₀), IsEssentiallyConstantWith M (colimit.cocone M) i₀ b
```

**`CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantInd.hasLimit_of_op`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean#L83).

> (pro, part 1) If `M` is essentially constant as a pro-object, `M` has a limit.

```lean
theorem hasLimit_of_op {M : I ⥤ C} (h : IsEssentiallyConstantInd M.op) : HasLimit M
```

**`CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantInd.exists_retraction_op_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean#L91).

> (pro, part 2) The (opposite) limit cone realizes `IsEssentiallyConstantInd M.op` with value
> `op (limit M)`: some `i₀` admits a retraction `b` of `(limit.π M i₀.unop).op` through which every
> `(limit.π M j.unop).op` factors.

```lean
theorem exists_retraction_op_limit {M : I ⥤ C} (h : IsEssentiallyConstantInd M.op)
    [HasLimit M] :
    ∃ (i₀ : Iᵒᵖ) (b : op (limit M) ⟶ M.op.obj i₀),
      IsEssentiallyConstantWith M.op (limit.cone M).op i₀ b
```

## Tag 0G2X, a remark

[Tag 0G2X](https://stacks.math.columbia.edu/tag/0G2X) in the Stacks Project.

**`CategoryTheory.Pro.homEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/ProMorphisms.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/ProMorphisms.lean#L133).

> A morphism of pro-systems from `F` to `G` is the same thing as a transformation of functors
> `t : B ⟶ A`, where `A(X) = colim_i Mor(F i, X)` and `B(X) = colim_j Mor(G j, X)`. The bijection
> sends `t` to the family of images under `t` of the classes of the identities `id_{G j}`; see
> `component_homEquiv`.

```lean
noncomputable def homEquiv : (coyonedaColim G ⟶ coyonedaColim F) ≃ Hom F G
```

## Tag 05SH, a lemma

[Tag 05SH](https://stacks.math.columbia.edu/tag/05SH) in the Stacks Project.

**`CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantInd.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean#L54).

> (ind) Essential constancy is stable under postcomposition by any functor.

```lean
theorem comp {M : I ⥤ C} (h : IsEssentiallyConstantInd M) (F : C ⥤ D) :
    IsEssentiallyConstantInd (M ⋙ F)
```

**`CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantInd.op_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean#L61).

> (pro) Essential constancy as a pro-object is stable under postcomposition.

```lean
theorem op_comp {M : I ⥤ C} (h : IsEssentiallyConstantInd M.op) (F : C ⥤ D) :
    IsEssentiallyConstantInd (M ⋙ F).op
```

## Tag 05PY, a lemma

[Tag 05PY](https://stacks.math.columbia.edu/tag/05PY) in the Stacks Project.

**`CategoryTheory.EssentiallyConstantInd.isEssentiallyConstantWith_of_bijective_homComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/IndObject.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/IndObject.lean#L217).

> If `homComparison M t W` is bijective for every `W`, then `M` is essentially constant as an
> ind-object with value `t.pt`, with respect to the cocone `t`.

```lean
theorem isEssentiallyConstantWith_of_bijective_homComparison (M : I ⥤ C) [IsFiltered I]
    (t : Cocone M) (h : ∀ W : C, Function.Bijective (homComparison M t W)) :
    ∃ (i : I) (r : t.pt ⟶ M.obj i), IsEssentiallyConstantWith M t i r
```

**`CategoryTheory.EssentiallyConstantInd.isEssentiallyConstantWith_of_bijective_homComparisonInv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/IndObject.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/IndObject.lean#L238).

> If `homComparisonInv M r W` is bijective for every `W`, for a morphism `r : X ⟶ M i`, then
> `X` is the apex of a cocone with respect to which `M` is essentially constant, so `X` is a value of
> the essentially constant system.

```lean
theorem isEssentiallyConstantWith_of_bijective_homComparisonInv (M : I ⥤ C) [IsFiltered I]
    (X : C) (i : I) (r : X ⟶ M.obj i)
    (h : ∀ W : C, Function.Bijective (homComparisonInv M r W)) :
    ∃ (t : Cocone M), t.pt = X ∧
      ∃ (i' : I) (r' : t.pt ⟶ M.obj i'), IsEssentiallyConstantWith M t i' r'
```

**`CategoryTheory.EssentiallyConstantInd.essentiallyConstantInd_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/IndObject.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/IndObject.lean#L278). References: SGA 4 I (8.7.1.7), “partial”.

> For a filtered diagram `M : I ⥤ C` the four conditions (1) `M` is an essentially constant
> ind-object, (2) some cocone has bijective `homComparison` at every `W`, (3) some colimit cocone
> does, and (4) some `r : X ⟶ M i` has bijective `homComparisonInv` at every `W`, are equivalent.

```lean
theorem essentiallyConstantInd_tfae (M : I ⥤ C) [IsFiltered I] :
    [ IsEssentiallyConstantInd M,
      HasCoconeWithBijectiveHomComparison M,
      HasColimitWithBijectiveHomComparison M,
      HasCoreflectionWithBijectiveHomComparison M ].TFAE
```

## Tag 05PZ, a lemma

[Tag 05PZ](https://stacks.math.columbia.edu/tag/05PZ) in the Stacks Project.

**`CategoryTheory.EssentiallyConstantPro.isEssentiallyConstantWith_of_bijective_homComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/ProObject.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/ProObject.lean#L149).

> If the comparison map `colim_i Mor(M_i, W) → Mor(c.pt, W)` is bijective for every `W` at the
> cone `c`, then `M` is essentially constant as a pro-object with value `c.pt`, with respect to the
> cone `c`.

```lean
theorem isEssentiallyConstantWith_of_bijective_homComparison (M : I ⥤ C) [IsCofiltered I]
    (c : Cone M)
    (h : ∀ W : Cᵒᵖ, Function.Bijective
      (EssentiallyConstantInd.homComparison M.op c.op W)) :
    ∃ (i : I) (s : M.obj i ⟶ c.pt), IsEssentiallyConstantWith M c i s
```

**`CategoryTheory.EssentiallyConstantPro.isEssentiallyConstantWith_of_bijective_homComparisonInv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/ProObject.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/ProObject.lean#L162).

> If the reverse comparison map `Mor(X, W) → colim_j Mor(M_j, W)` is bijective for every `W`
> at `(X, i, s)`, then `X` is the apex of a cone with respect to which `M` is essentially constant,
> so `X` is a value of the essentially constant system.

```lean
theorem isEssentiallyConstantWith_of_bijective_homComparisonInv (M : I ⥤ C) [IsCofiltered I]
    (X : C) (i : I) (s : M.obj i ⟶ X)
    (h : ∀ W : Cᵒᵖ, Function.Bijective
      (EssentiallyConstantInd.homComparisonInv M.op s.op W)) :
    ∃ c : Cone M, c.pt = X ∧
      ∃ (i' : I) (s' : M.obj i' ⟶ c.pt), IsEssentiallyConstantWith M c i' s'
```

**`CategoryTheory.EssentiallyConstantPro.essentiallyConstantPro_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/ProObject.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/ProObject.lean#L179).

> For a cofiltered diagram `M : I ⥤ C` the four conditions (1) `M` is an essentially constant
> pro-object, (2) some cone has a bijective Hom-colimit comparison at every `W`, (3) some limit cone
> does, and (4) some `s : M i ⟶ X` has a bijective reverse comparison at every `W`, are
> equivalent.

```lean
theorem essentiallyConstantPro_tfae [IsCofiltered I] (M : I ⥤ C) :
    [ IsEssentiallyConstantPro M,
      HasConeWithBijectiveHomColimit M,
      HasLimitWithBijectiveHomColimit M,
      HasReflectionWithBijectiveHomColimit M ].TFAE
```

## Tag 0A1S, a lemma

[Tag 0A1S](https://stacks.math.columbia.edu/tag/0A1S) in the Stacks Project.

**`essentiallyConstant_iff_comp_final`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Cofinal.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/Cofinal.lean#L169).

> Stacks Tag 0A1S, Lemma 4.22.11. Let `H : I ⥤ J` be a cofinal (= `Final`)
> functor between filtered categories `I` and `J`, and `M : J ⥤ C` a diagram. Then
> `M` is essentially constant iff `M ∘ H` (written `H ⋙ M`) is essentially
> constant.

```lean
theorem essentiallyConstant_iff_comp_final
    {C : Type*} [Category C] {I : Type*} [Category I] {J : Type*} [Category J]
    [IsFiltered I] [IsFiltered J] (H : I ⥤ J) [H.Final] (M : J ⥤ C) :
    IsEssentiallyConstantInd M ↔ IsEssentiallyConstantInd (H ⋙ M)
```

## Tag 0A2C, a lemma

[Tag 0A2C](https://stacks.math.columbia.edu/tag/0A2C) in the Stacks Project.

**`isFiltered_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean#L128). References: SGA 4 I (8.5.4).

> The product of two filtered categories is filtered.

```lean
theorem isFiltered_prod [IsFiltered I] [IsFiltered J] : IsFiltered (I × J)
```

**`isEssentiallyConstantInd_iff_comp_prod_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/Operations.lean#L136).

> For filtered `I` and any `M : J ⥤ C`, essential constancy of `M` is equivalent to essential
> constancy of `M` precomposed with `Prod.snd I J`.

```lean
theorem isEssentiallyConstantInd_iff_comp_prod_snd [IsFiltered I] (M : J ⥤ C) :
    IsEssentiallyConstantInd M ↔ IsEssentiallyConstantInd (CategoryTheory.Prod.snd I J ⋙ M)
```

## Tag 0A1T, a lemma

[Tag 0A1T](https://stacks.math.columbia.edu/tag/0A1T) in the Stacks Project.

**`essentiallyConstant_iff_comp_initial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Initial.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/EssentiallyConstant/Initial.lean#L237).

> Stacks Tag 0A1T (Lemma 4.22.13). For cofiltered `I`, `J`, an initial functor
> `H : I ⥤ J`, and any diagram `M : J ⥤ C`, the diagram `M` is essentially constant iff its
> restriction `H ⋙ M` along `H` is essentially constant.
>
> Proved by combining the two directions: `essentiallyConstant_comp_initial_of` (→) and
> `essentiallyConstant_of_comp_initial` (←).

```lean
theorem essentiallyConstant_iff_comp_initial
    {C : Type*} [Category C]
    {I J : Type*} [Category I] [Category J]
    [IsCofiltered I] [IsCofiltered J]
    (H : I ⥤ J) [H.Initial] (M : J ⥤ C) :
    IsEssentiallyConstantPro M ↔ IsEssentiallyConstantPro (H ⋙ M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.22, Tag 05PT](https://stacks.math.columbia.edu/tag/05PT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
