---
declaration: section
origin: cited
lean: Stacks.Chow.IsEquidimensional, Stacks.Chow.equidimensionalRelativeCycles, Stacks.Chow.NotEquidimensional.exampleFamily, Stacks.Chow.NotEquidimensional.exampleFamily_of_eq_zero, Stacks.Chow.NotEquidimensional.exampleFamily_of_ne_zero, Stacks.Chow.NotEquidimensional.mem_closure_supportOfFamily_exampleFamily, Stacks.Chow.NotEquidimensional.not_isEquidimensional_exampleFamily, Stacks.Chow.NotEquidimensional.isRelativeCycle_exampleFamily
statement: formalized
proof: formalized
---

# 62.7 Equidimensional relative cycles

Section 62.7 of the Stacks Project, [Tag 0H5H](https://stacks.math.columbia.edu/tag/0H5H). 6 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H5I, a definition

[Tag 0H5I](https://stacks.math.columbia.edu/tag/0H5I) in the Stacks Project.

**`Stacks.Chow.IsEquidimensional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalCycles.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalCycles.lean#L89). The attribute's comment: “the equidimensionality condition”.

> A family of `r`-cycles on the fibres of `f` is *equidimensional* when its support is
> contained in a closed subset of `X` whose relative dimension over `S` is at most `r`.

```lean
def IsEquidimensional {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    [IsLocallyNoetherian S] (r : ℕ) (α : FamilyOfCycles f r) : Prop
```

**`Stacks.Chow.equidimensionalRelativeCycles`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalCycles.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalCycles.lean#L461). The attribute's comment: “the group z_equi(X/S, r) of equidimensional relative r-cycles”.

> The group `z_equi(X/S, r)` of equidimensional relative `r`-cycles on `X/S`: the subgroup of
> the group of families of `r`-cycles on the fibres of `X/S` whose members are the relative
> `r`-cycles whose support is contained in a closed subset of `X` of relative dimension at most `r`
> over `S`.

```lean
def equidimensionalRelativeCycles {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    [IsLocallyNoetherian S] (r : ℕ) : AddSubgroup (FamilyOfCycles f r)
```

## Tag 0H5J, an example

[Tag 0H5J](https://stacks.math.columbia.edu/tag/0H5J) in the Stacks Project.

**`Stacks.Chow.NotEquidimensional.exampleFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean#L430). The attribute's comment: “the family of 0-cycles of the example”.

> **Stacks Project, Tag 0H5J.** The family of `0`-cycles on the fibres of
> `Spec k[x, y, t] ⟶ Spec k[x, y]` of Suslin--Voevodsky's example.

```lean
def exampleFamily (k : Type u) [Field k] : FamilyOfCycles (projection k) 0
```

**`Stacks.Chow.NotEquidimensional.exampleFamily_of_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean#L436). The attribute's comment: “the first clause: the member of the family is zero when b = 0”.

> **Stacks Project, Tag 0H5J, first clause.** The example family vanishes on the fibre over
> a point where the image of `y` is zero.

```lean
theorem exampleFamily_of_eq_zero (k : Type u) [Field k] (s : baseScheme k)
    (hb : yImage k s = 0) : exampleFamily k s = 0
```

**`Stacks.Chow.NotEquidimensional.exampleFamily_of_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean#L445). The attribute's comment: “the second clause: the member of the family is [p] - [q] when b is nonzero”.

> **Stacks Project, Tag 0H5J, second clause.** On a fibre where the image `b` of `y` is
> nonzero the member of the example family is the difference `[p] - [q]` of the `κ(s)`-rational
> points at `t = a/b` and at `t = (a + b²)/b`.

```lean
theorem exampleFamily_of_ne_zero (k : Type u) [Field k] (s : baseScheme k)
    (hb : yImage k s ≠ 0) :
    (exampleFamily k s : AlgebraicCycle ((projection k).fiber s) ℤ) =
      twoPointCycle (firstPoint k s) (secondPoint k s)
```

**`Stacks.Chow.NotEquidimensional.mem_closure_supportOfFamily_exampleFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean#L523). The attribute's comment: “the closure of the support contains the whole fibre over the origin”.

> **Stacks Project, Tag 0H5J.** The closure of the support of the example family contains the
> whole fibre over the origin, which is a line: the surface `y·t = x` lies in that closure and
> contains the fibre over the origin.

```lean
theorem mem_closure_supportOfFamily_exampleFamily (k : Type u) [Field k] (z : totalScheme k)
    (hz : projection k z = origin k) :
    z ∈ closure (supportOfFamily (projection k) (exampleFamily k))
```

**`Stacks.Chow.NotEquidimensional.not_isEquidimensional_exampleFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean, line 639](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean#L639). The attribute's comment: “the example family is not equidimensional”.

> **Stacks Project, Tag 0H5J.** The example family of `0`-cycles on the fibres of
> `Spec k[x, y, t] ⟶ Spec k[x, y]` is not equidimensional: a closed subset of `X` containing its
> support contains the whole fibre over the origin, which is a line, so that closed subset
> cannot have relative dimension `0` over the base.

```lean
theorem not_isEquidimensional_exampleFamily (k : Type u) [Field k] :
    ¬ IsEquidimensional (projection k) 0 (exampleFamily k)
```

**`Stacks.Chow.NotEquidimensional.isRelativeCycle_exampleFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean, line 1320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean#L1320). The attribute's comment: “the example family is a relative 0-cycle, compatible with specializations”.

> **Stacks Project, Tag 0H5J.** The family `α` of Suslin--Voevodsky's example is a relative
> `0`-cycle: it is compatible with specializations. Over a discrete valuation ring `R` with a
> morphism `g : Spec R ⟶ S` there are three cases. If `b = 0` in the residue field of the generic
> point of `Spec R` then it also vanishes at the closed point, so both members of the base change
> are zero. If `b ≠ 0` at the generic point but `b = 0` at the closed point, then the translation
> `t ↦ t + y` of the affine line is the identity on the special fibre and carries the first of the
> two rational points to the second, so their fundamental cycles have the same specialization and
> the difference specializes to zero, which is the vanishing member at the closed point. If
> `b ≠ 0` at the closed point then `y` is a unit of `R`, the value `a/b` lies in `R` and the two
> points of the generic fibre extend to closed sections of `X ×_S Spec R` over `Spec R`, whose
> values at the closed point are the two rational points of the special fibre; the specialization
> of the fundamental cycle of a section is the prime cycle of its closed value.

```lean
theorem isRelativeCycle_exampleFamily (k : Type u) [Field k] :
    IsRelativeCycle (projection k) 0 (exampleFamily k)
```

**`Stacks.Chow.NotEquidimensional.exists_isRelativeCycle_not_isEquidimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean, line 1458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NotEquidimensional.lean#L1458). The attribute's comment: “there exist relative r-cycles which are not equidimensional”.

> **Stacks Project, Tag 0H5J.** There exist relative `0`-cycles which are not
> equidimensional: Suslin--Voevodsky's family on `Spec k[x, y, t] ⟶ Spec k[x, y]` is one.

```lean
theorem exists_isRelativeCycle_not_isEquidimensional (k : Type u) [Field k] :
    ∃ α : FamilyOfCycles (projection k) 0,
      IsRelativeCycle (projection k) 0 α ∧ ¬ IsEquidimensional (projection k) 0 α
```

## Tag 0H5K, a lemma

[Tag 0H5K](https://stacks.math.columbia.edu/tag/0H5K) in the Stacks Project.

**`Stacks.Chow.isEquidimensional_restrictedFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalCycles.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalCycles.lean#L115). The attribute's comment: “restriction”.

> Restriction to compatible open subschemes of the source and the base preserves
> equidimensionality of a family of cycles on the fibres.

```lean
theorem isEquidimensional_restrictedFamily {X S U V : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (fU : U ⟶ V) (j : U ⟶ X) [IsOpenImmersion j]
    (i : V ⟶ S) [IsOpenImmersion i] (h : j ≫ f = fU ≫ i) (r : ℕ) (α : FamilyOfCycles f r)
    (hα : IsEquidimensional f r α) :
    letI : IsLocallyNoetherian V := isLocallyNoetherian_of_isOpenImmersion i
    letI : LocallyOfFiniteType fU := by
      let : LocallyOfFiniteType (fU ≫ i) := h ▸ inferInstance
      exact locallyOfFiniteType_of_comp fU i
    IsEquidimensional fU r (restrictedFamily f fU j i h r α).1
```

**`Stacks.Chow.isEquidimensional_baseChangeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalDescent.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalDescent.lean#L542). The attribute's comment: “base change”.

> **Stacks Project, Tag 0H5K, the base-change clause.** The base change of an equidimensional
> family of `r`-cycles along an arbitrary morphism `g : S' ⟶ S` of the base is equidimensional:
> its support is the inverse image of the support of the original family, and the base change of
> a bounding closed subscheme bounds it and has the same relative dimension over `S'`.

```lean
theorem isEquidimensional_baseChangeFamily {X S S' : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (g : S' ⟶ S) [IsLocallyNoetherian S']
    (r : ℕ) (α : FamilyOfCycles f r) (hα : IsEquidimensional f r α) :
    IsEquidimensional (pullback.snd f g) r (baseChangeFamily f g r α)
```

**`Stacks.Chow.isEquidimensional_flatPullbackFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalDescent.lean, line 590](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalDescent.lean#L590). The attribute's comment: “flat pullback”.

> **Stacks Project, Tag 0H5K, the flat-pullback clause.** The flat pullback of an
> equidimensional family of `r`-cycles along a morphism `j : U ⟶ X` of schemes over `S` which is
> flat, locally of finite type and of relative dimension `e` is an equidimensional family of
> `(r + e)`-cycles: the inverse image of a closed subscheme bounding the support of the original
> family bounds the support of the pullback, and its relative dimension over `S` is at most
> `r + e` because it maps to the bounding subscheme by a morphism of relative dimension `e`.

```lean
theorem isEquidimensional_flatPullbackFamily {X S U : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (fU : U ⟶ S) [LocallyOfFiniteType fU]
    (j : U ⟶ X) [LocallyOfFiniteType j] [Flat j] (h : j ≫ f = fU) (e : ℕ)
    (he : RelativeDimension j e) (r : ℕ) (α : FamilyOfCycles f r)
    (hα : IsEquidimensional f r α) :
    IsEquidimensional fU (r + e) (flatPullbackFamily f fU j h e he r α)
```

## Tag 0H5L, a lemma

[Tag 0H5L](https://stacks.math.columbia.edu/tag/0H5L) in the Stacks Project.

**`Stacks.Chow.isEquidimensional_iff_forall_restrictedFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalCycles.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalCycles.lean#L293).

> Equidimensionality of a family of cycles may be checked Zariski locally on `X` and on `S`:
> given open subschemes `U t ⊆ X` lying over open subschemes `V t ⊆ S` whose members cover `X`,
> the family is equidimensional exactly when each of its restrictions is.

```lean
theorem isEquidimensional_iff_forall_restrictedFamily {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (r : ℕ) (α : FamilyOfCycles f r)
    {ι : Type*} (U V : ι → Scheme.{u})
    (fU : ∀ t, U t ⟶ V t) (j : ∀ t, U t ⟶ X) (hj : ∀ t, IsOpenImmersion (j t))
    (i : ∀ t, V t ⟶ S) (hi : ∀ t, IsOpenImmersion (i t))
    (h : ∀ t, j t ≫ f = fU t ≫ i t)
    (hcover : ∀ x : X, ∃ (t : ι) (y : U t), j t y = x) :
    IsEquidimensional f r α ↔
      ∀ t : ι,
        letI : IsOpenImmersion (j t) := hj t
        letI : IsOpenImmersion (i t) := hi t
        letI : IsLocallyNoetherian (V t) := isLocallyNoetherian_of_isOpenImmersion (i t)
        letI : LocallyOfFiniteType (fU t) := by
          let : LocallyOfFiniteType (fU t ≫ i t) := h t ▸ inferInstance
          exact locallyOfFiniteType_of_comp (fU t) (i t)
        IsEquidimensional (fU t) r (restrictedFamily f (fU t) (j t) (i t) (h t) r α).1
```

## Tag 0H5M, a lemma

[Tag 0H5M](https://stacks.math.columbia.edu/tag/0H5M) in the Stacks Project.

**`Stacks.Chow.isEquidimensional_iff_forall_of_fppfCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalDescent.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalDescent.lean#L367). The attribute's comment: “generalized: the families over the covering are an argument and enter only through their supports, so no relative-cycle condition is needed; `isEquidimensional_iff_forall_baseChangeFamily` instantiates them at the base changes themselves”.

> The support form of Tag 0H5M: for an fppf covering `{g i : T i ⟶ S}` of the base, a family
> of `r`-cycles on the fibres of `f : X ⟶ S` is equidimensional exactly when each family on the
> fibres of `X ×_S T i ⟶ T i` whose support is the preimage of its support is equidimensional.
> The base changes of the family have that property, by the base-change clause of Tag 0H4V.

```lean
theorem isEquidimensional_iff_forall_of_fppfCovering {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (r : ℕ) (α : FamilyOfCycles f r)
    {I : Type v} {T : I → Scheme.{u}} (g : ∀ i, T i ⟶ S)
    (hg : Presieve.ofArrows T g ∈ Scheme.fppfPrecoverage S)
    (β : ∀ i, FamilyOfCycles (pullback.snd f (g i)) r)
    (hβ : ∀ i, supportOfFamily (pullback.snd f (g i)) (β i) =
      pullback.fst f (g i) ⁻¹' supportOfFamily f α) :
    letI (i : I) : IsLocallyNoetherian (T i) :=
      isLocallyNoetherian_of_mem_fppfPrecoverage g hg i
    (IsEquidimensional f r α ↔
      ∀ i, IsEquidimensional (pullback.snd f (g i)) r (β i))
```

**`Stacks.Chow.isEquidimensional_iff_forall_baseChangeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalDescent.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalDescent.lean#L395).

> **Stacks Project, Tag 0H5M.** Equidimensionality of a family of `r`-cycles on the fibres of
> `f : X ⟶ S` is local for an fppf covering `{g i : T i ⟶ S}` of the base: the family is
> equidimensional exactly when every base change `g i ^* α` is.

```lean
theorem isEquidimensional_iff_forall_baseChangeFamily {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (r : ℕ) (α : FamilyOfCycles f r)
    {I : Type v} {T : I → Scheme.{u}} (g : ∀ i, T i ⟶ S)
    (hg : Presieve.ofArrows T g ∈ Scheme.fppfPrecoverage S) :
    letI (i : I) : IsLocallyNoetherian (T i) :=
      isLocallyNoetherian_of_mem_fppfPrecoverage g hg i
    (IsEquidimensional f r α ↔
      ∀ i, IsEquidimensional (pullback.snd f (g i)) r (baseChangeFamily f (g i) r α))
```

## Tag 0H5N, a lemma

[Tag 0H5N](https://stacks.math.columbia.edu/tag/0H5N) in the Stacks Project.

**`Stacks.Chow.isEquidimensional_iff_forall_flatPullbackFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalDescent.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EquidimensionalDescent.lean#L522).

> **Stacks Project, Tag 0H5N.** Equidimensionality of a family of `r`-cycles on the fibres of
> `f : X ⟶ S` can be checked after a jointly surjective family `{fi i : Xi i ⟶ X}` of flat
> morphisms locally of finite type of relative dimension `e`: the family is equidimensional
> exactly when every flat pullback `fi i ^* α`, a family of `(r + e)`-cycles on the fibres of
> `Xi i ⟶ S`, is.

```lean
theorem isEquidimensional_iff_forall_flatPullbackFamily {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (r e : ℕ) (α : FamilyOfCycles f r)
    {I : Type v} {Xi : I → Scheme.{u}} (fi : ∀ i, Xi i ⟶ X)
    [∀ i, LocallyOfFiniteType (fi i)] [∀ i, Flat (fi i)]
    (hdim : ∀ i, RelativeDimension (fi i) e)
    (hsurj : ∀ x : X, ∃ i, x ∈ Set.range (fi i)) :
    IsEquidimensional f r α ↔
      ∀ i, IsEquidimensional (fi i ≫ f) (r + e)
        (flatPullbackFamily f (fi i ≫ f) (fi i) rfl e (hdim i) r α)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 62.7, Tag 0H5H](https://stacks.math.columbia.edu/tag/0H5H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
