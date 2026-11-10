---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.proetalePrecoverage, AlgebraicGeometry.mem_proetalePrecoverage_iff_weaklyEtale_and_mem_fpqcPrecoverage, AlgebraicGeometry.mem_proetalePrecoverage_iff_affine_finite_support, AlgebraicGeometry.mem_proetalePrecoverage_iff_exists_affine_open_cover, AlgebraicGeometry.mem_proetalePrecoverage_iff_pointwise_compact_open_neighborhood, AlgebraicGeometry.Scheme.etalePrecoverage_le_proetalePrecoverage, AlgebraicGeometry.Scheme.zariskiPrecoverage_le_propQCPrecoverage, AlgebraicGeometry.Scheme.instHasIsosProetalePrecoverage
statement: formalized
proof: formalized
---

# 61.12 The pro-étale site

Section 61.12 of the Stacks Project, [Tag 0988](https://stacks.math.columbia.edu/tag/0988). 23 tags here are carried by 71 declarations of the repository (all in StacksFrontier) and 26 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0989, a definition

[Tag 0989](https://stacks.math.columbia.edu/tag/0989) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.proetalePrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.proetalePrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch61.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch61.lean#L14) (StacksFrontier).

## Tag 098A, a lemma

[Tag 098A](https://stacks.math.columbia.edu/tag/098A) in the Stacks Project.

**`AlgebraicGeometry.mem_proetalePrecoverage_iff_weaklyEtale_and_mem_fpqcPrecoverage`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/CoveringCharacterization.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/CoveringCharacterization.lean#L77). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 098A, conditions (1) and (2).** A family is a pro-étale covering if and only if
> every member is weakly étale and the family is an fpqc covering.

```lean
public lemma mem_proetalePrecoverage_iff_weaklyEtale_and_mem_fpqcPrecoverage :
    Presieve.ofArrows X f ∈ Scheme.proetalePrecoverage T ↔
      ((∀ i, WeaklyEtale (f i)) ∧ Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage T)
```

**`AlgebraicGeometry.mem_proetalePrecoverage_iff_affine_finite_support`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/CoveringCharacterization.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/CoveringCharacterization.lean#L89). The attribute's comment: “conditions (1) and (3)”.

> **Stacks 098A, conditions (1) and (3).** A family is a pro-étale covering if and only if
> every member is weakly étale and every affine open of the target is the union of the images of
> quasi-compact opens in the sources, all but finitely many of which are empty.

```lean
public lemma mem_proetalePrecoverage_iff_affine_finite_support :
    Presieve.ofArrows X f ∈ Scheme.proetalePrecoverage T ↔
      ((∀ i, WeaklyEtale (f i)) ∧
        (∀ U : T.Opens, IsAffineOpen U →
            ∃ V : ∀ i, (X i).Opens,
              ((∀ i, IsCompact (V i : Set (X i))) ∧
                ({i | V i ≠ ⊥} : Set I).Finite ∧
                ⋃ i, f i '' (V i : Set (X i)) = (U : Set T))))
```

**`AlgebraicGeometry.mem_proetalePrecoverage_iff_exists_affine_open_cover`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/CoveringCharacterization.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/CoveringCharacterization.lean#L105). The attribute's comment: “conditions (1) and (4)”.

> **Stacks 098A, conditions (1) and (4).** A family is a pro-étale covering if and only if
> its members are weakly étale and some affine open covering of the target is, member by member,
> the union of images of finitely many quasi-compact opens in the sources.

```lean
public lemma mem_proetalePrecoverage_iff_exists_affine_open_cover :
    Presieve.ofArrows X f ∈ Scheme.proetalePrecoverage T ↔
      ((∀ i, WeaklyEtale (f i)) ∧
        ∃ (A : Type u) (U : A → T.Opens),
          ((∀ a, IsAffineOpen (U a)) ∧
            (⋃ a, (U a : Set T)) = Set.univ ∧
            ∀ a, ∃ (n : ℕ) (i : Fin n → I) (V : ∀ j, (X (i j)).Opens),
              ((∀ j, IsCompact (V j : Set (X (i j)))) ∧
                ⋃ j, f (i j) '' (V j : Set (X (i j))) = (U a : Set T))))
```

**`AlgebraicGeometry.mem_proetalePrecoverage_iff_pointwise_compact_open_neighborhood`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/CoveringCharacterization.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/CoveringCharacterization.lean#L123). The attribute's comment: “conditions (1) and (5)”.

> **Stacks 098A, conditions (1) and (5).** If the target is quasi-separated, a family is a
> pro-étale covering if and only if its members are weakly étale and every point has a
> neighbourhood which is the union of the images of finitely many quasi-compact opens in the
> sources. The neighbourhood itself is not required to be open.

```lean
public lemma mem_proetalePrecoverage_iff_pointwise_compact_open_neighborhood
    [QuasiSeparatedSpace T] :
    Presieve.ofArrows X f ∈ Scheme.proetalePrecoverage T ↔
      ((∀ i, WeaklyEtale (f i)) ∧
        ∀ t : T, ∃ (n : ℕ) (i : Fin n → I) (V : ∀ j, (X (i j)).Opens),
          ((∀ j, IsCompact (V j : Set (X (i j)))) ∧
            (⋃ j, f (i j) '' (V j : Set (X (i j)))) ∈ nhds t))
```

## Tag 098B, a lemma

[Tag 098B](https://stacks.math.columbia.edu/tag/098B) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.etalePrecoverage_le_proetalePrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.etalePrecoverage_le_proetalePrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch61.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch61.lean#L15) (StacksFrontier): “étale coverings”.
- [`AlgebraicGeometry.Scheme.zariskiPrecoverage_le_propQCPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.zariskiPrecoverage_le_propQCPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch61.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch61.lean#L17) (StacksFrontier): “Zariski coverings (the case P = weakly étale)”.

## Tag 098C, a lemma

[Tag 098C](https://stacks.math.columbia.edu/tag/098C) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.instHasIsosProetalePrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.instHasIsosProetalePrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch61.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch61.lean#L19) (StacksFrontier): “(1)”.
- [`AlgebraicGeometry.Scheme.instIsStableUnderCompositionProetalePrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.instIsStableUnderCompositionProetalePrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch61.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch61.lean#L20) (StacksFrontier): “(2)”.
- [`AlgebraicGeometry.Scheme.instIsStableUnderBaseChangeProetalePrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.instIsStableUnderBaseChangeProetalePrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch61.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch61.lean#L21) (StacksFrontier): “(3)”.

## Tag 098D, a lemma

[Tag 098D](https://stacks.math.columbia.edu/tag/098D) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.QuasiCompactCover.exists_hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompactCover.exists_hom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch61.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch61.lean#L22) (StacksFrontier): “finite affine refinement by open immersions into the members”.
- [`AlgebraicGeometry.QuasiCompactCover.instCoverOfIsAffineOfFiniteI₀`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompactCover.instCoverOfIsAffineOfFiniteI₀#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch61.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch61.lean#L24) (StacksFrontier): “the refinement is quasi-compact, hence a pro-étale covering”.

## Tag 098E, a definition

[Tag 098E](https://stacks.math.columbia.edu/tag/098E) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IsStandardProEtaleCovering`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/StandardCovering.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/StandardCovering.lean#L40).

> A family of morphisms `f i : X i ⟶ T` is a *standard pro-étale covering* of `T` if `T` is
> affine, the family is finite, each `X i` is affine, each `f i` is weakly étale, and the images of
> the `f i` cover `T`.

```lean
structure IsStandardProEtaleCovering {T : Scheme.{u}} {ι : Type v} {X : ι → Scheme.{u}}
    (f : ∀ i, X i ⟶ T) : Prop
```

## Tag 098G, a definition

[Tag 098G](https://stacks.math.columbia.edu/tag/098G) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.BigProetaleSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Big.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Big.lean#L100).

> A big pro-étale site, including the initial set-sized choices, the
> size-bounded full category of schemes, and a set-sized choice of pro-étale coverings satisfying
> the site axioms and representing every pro-étale covering.

```lean
structure BigProetaleSite
```

## Tag 098K, a definition

[Tag 098K](https://stacks.math.columbia.edu/tag/098K) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.BigProetaleOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean#L56). The attribute's comment: “part (1), category”.

> The big pro-étale category over `S` in the chosen big site.

```lean
abbrev BigProetaleOver
```

**`AlgebraicGeometry.ProEtale.BigProetaleOver.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean#L68). The attribute's comment: “part (1), coverings”.

> A covering in the slice is a covering of the chosen big site.

```lean
abbrev IsCovering (E : Covering (BigProetaleOver B S hS)) : Prop
```

**`AlgebraicGeometry.ProEtale.SmallProetale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean#L83). The attribute's comment: “part (2), category in a chosen big site”.

> The small pro-étale category in the chosen big site.

```lean
abbrev SmallProetale
```

**`AlgebraicGeometry.ProEtale.SmallProetale.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean#L101). The attribute's comment: “part (2), coverings in a chosen big site”.

> Small-site coverings are those induced from the chosen big site.

```lean
abbrev IsCovering (E : Covering (SmallProetale B S hS)) : Prop
```

**`AlgebraicGeometry.ProEtale.BigAffineProetale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean#L127). The attribute's comment: “part (3), category”.

> The big affine pro-étale category over `S`.

```lean
abbrev BigAffineProetale
```

**`AlgebraicGeometry.ProEtale.BigAffineProetale.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean#L145). The attribute's comment: “part (3), coverings”.

> Standard affine pro-étale coverings are finite chosen big coverings.

```lean
abbrev IsCovering (E : Covering (BigAffineProetale B S hS)) : Prop
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.ProEt.precoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.ProEt.precoverage#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Slices.lean#L50) (StacksFrontier): “small-site coverings”.

## Tag 098L, a lemma

[Tag 098L](https://stacks.math.columbia.edu/tag/098L) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.SmallProetale.isSite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/SiteAxioms.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/SiteAxioms.lean#L55). The attribute's comment: “small pro-étale site”.

> The covering families on the small pro-étale category of `S` form a site.

```lean
lemma isSite (B : BigProetaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) : IsSite (SmallProetale.IsCovering B S hS)
```

**`AlgebraicGeometry.ProEtale.BigAffineProetale.isSite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/SiteAxioms.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/SiteAxioms.lean#L100). The attribute's comment: “affine pro-étale site”.

> The standard covering families on affine pro-étale objects over `S` form a site.

```lean
lemma isSite (B : BigProetaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) : IsSite (BigAffineProetale.IsCovering B S hS)
```

## Tag 098M, a lemma

[Tag 098M](https://stacks.math.columbia.edu/tag/098M) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.specZ_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L150). The attribute's comment: “part (4), containment of Spec ℤ”.

> `Spec ℤ` belongs to every big pro-étale site.

```lean
theorem specZ_mem : B.Contains (Spec (.of (ULift.{u} ℤ)))
```

**`AlgebraicGeometry.ProEtale.specZObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L157). The attribute's comment: “part (4), final object”.

> The scheme `Spec ℤ`, regarded as an object of the big pro-étale category.

```lean
noncomputable def specZObject : B.Scheme
```

**`AlgebraicGeometry.ProEtale.specZObject_isTerminal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L162). The attribute's comment: “part (4), finality and agreement with schemes”.

> `Spec ℤ` is final in the big pro-étale category.

```lean
noncomputable def specZObject_isTerminal :
    IsTerminal (specZObject B)
```

**`AlgebraicGeometry.ProEtale.smallIdentity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L170). The attribute's comment: “part (3), small final object”.

> The identity of `S`, as an object of the small pro-étale category.

```lean
def smallIdentity : SmallProetale B S hS
```

**`AlgebraicGeometry.ProEtale.smallIdentity_isTerminal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L177). The attribute's comment: “part (3), small finality”.

> The identity of `S` is final in the small pro-étale category.

```lean
noncomputable def smallIdentity_isTerminal :
    IsTerminal (smallIdentity B S hS)
```

**`AlgebraicGeometry.ProEtale.smallProetale_hasPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L186). The attribute's comment: “part (1), small category: fibre products exist”.

> The small pro-étale category has fibre products computed in schemes.

```lean
instance smallProetale_hasPullbacks :
    HasPullbacks (SmallProetale B S hS)
```

**`AlgebraicGeometry.ProEtale.smallProetale_createsPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L195). The attribute's comment: “part (1), small category: agreement with schemes”.

> The inclusion of the small pro-étale category creates fibre products.

```lean
noncomputable instance smallProetale_createsPullbacks :
    CreatesLimitsOfShape WalkingCospan
      (SmallProetale.toScheme B S hS)
```

**`AlgebraicGeometry.ProEtale.bigAffineProetale_hasPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L213). The attribute's comment: “part (1), affine category: fibre products exist”.

> The affine pro-étale category has fibre products computed in schemes.

```lean
instance bigAffineProetale_hasPullbacks :
    HasPullbacks (BigAffineProetale B S hS)
```

**`AlgebraicGeometry.ProEtale.bigAffineProetale_createsPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L224). The attribute's comment: “part (1), affine category: agreement with schemes”.

> The inclusion of the affine pro-étale category creates fibre products.

```lean
noncomputable instance bigAffineProetale_createsPullbacks :
    CreatesLimitsOfShape WalkingCospan
      (BigAffineProetale.toScheme B S hS)
```

**`AlgebraicGeometry.ProEtale.bigProetale_hasEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L241). The attribute's comment: “part (2), big category: equalizers exist”.

> The big pro-étale category has equalizers.

```lean
instance bigProetale_hasEqualizers : HasEqualizers B.Scheme
```

**`AlgebraicGeometry.ProEtale.bigProetale_createsEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L248). The attribute's comment: “part (2), big category: agreement with schemes”.

> The inclusion of the big pro-étale category creates equalizers.

```lean
noncomputable instance bigProetale_createsEqualizers :
    CreatesLimitsOfShape WalkingParallelPair B.inclusion
```

**`AlgebraicGeometry.ProEtale.smallProetale_hasEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L268). The attribute's comment: “part (2), small category: equalizers exist”.

> The small pro-étale category has equalizers.

```lean
instance smallProetale_hasEqualizers :
    HasEqualizers (SmallProetale B S hS)
```

**`AlgebraicGeometry.ProEtale.smallProetale_createsEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L279). The attribute's comment: “part (2), small category: agreement with schemes”.

> The inclusion of the small pro-étale category creates equalizers.

```lean
noncomputable instance smallProetale_createsEqualizers :
    CreatesLimitsOfShape WalkingParallelPair
      (SmallProetale.toScheme B S hS)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.ProEtale.BigProetaleSite.hasPullbacks`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Big.lean#L173), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L62) (StacksFrontier): “part (1), big category: fibre products exist”.
- [`AlgebraicGeometry.ProEtale.BigProetaleSite.createsPullbacks`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Big.lean#L177), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L64) (StacksFrontier): “part (1), big category: fibre products agree with schemes”.
- [`CategoryTheory.Over.createsLimitsOfShapeForgetOfIsConnected`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.createsLimitsOfShapeForgetOfIsConnected#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L66) (StacksFrontier): “parts (1) and (2), slices: limits agree with the underlying category”.
- [`CategoryTheory.Over.hasLimitsOfShape_of_isConnected`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.hasLimitsOfShape_of_isConnected#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L68) (StacksFrontier): “parts (1) and (2), slices: connected limits exist”.
- [`CategoryTheory.Over.mkIdTerminal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mkIdTerminal#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Limits.lean#L70) (StacksFrontier): “part (3), final object of a slice”. References: EGA 0 (8.1.10), “more general”; SGA 3 I (1.3); SGA 4 IV (5.11.1), “terminal object (X”.

## Tag 098N, a lemma

[Tag 098N](https://stacks.math.columbia.edu/tag/098N) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.inclusion_isSpecialCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AffineDense.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AffineDense.lean#L432).

> **Stacks 098N.** The inclusion of the big affine pro-étale site over a
> scheme into its big pro-étale site is special cocontinuous, and induces the
> canonical equivalence of their topoi of sheaves.

```lean
theorem inclusion_isSpecialCocontinuous
    (B : BigProetaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    IsSpecialCocontinuous
      (BigAffineProetale.topology B S hS)
      (BigProetaleOver.topology B S hS)
      (BigAffineProetale.inclusion B S hS)
```

## Tag 098P, a lemma

[Tag 098P](https://stacks.math.columbia.edu/tag/098P) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.smallProetaleToBigProetaleFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean#L86). The attribute's comment: “the functor”.

> Send a weakly étale object `U / T` to the composite `U / S`.

```lean
public abbrev smallProetaleToBigProetaleFunctor :
    SmallProetale B T.obj T.property ⥤ BigProetaleOver B S.obj S.property
```

**`AlgebraicGeometry.ProEtale.smallProetaleToBigProetaleFunctor_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean#L373). The attribute's comment: “cocontinuity”.

> Composition from the small pro-étale site of `T` to the big pro-étale
> site over `S` is cocontinuous.

```lean
public instance smallProetaleToBigProetaleFunctor_isCocontinuous :
    (smallProetaleToBigProetaleFunctor B T S f).IsCocontinuous
      (SmallProetale.topology B T.obj T.property)
      (BigProetaleOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.ProEtale.smallProetaleToBigProetaleFunctor_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean#L392). The attribute's comment: “continuity”.

> Composition also preserves coverings and fibre products, hence is continuous.

```lean
public instance smallProetaleToBigProetaleFunctor_isContinuous :
    (smallProetaleToBigProetaleFunctor B T S f).IsContinuous
      (SmallProetale.topology B T.obj T.property)
      (BigProetaleOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.ProEtale.smallProetaleToBigProetaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean#L439). The attribute's comment: “the morphism of topoi”.

> The morphism `i_f : Sh(T_proetale) ⟶ Sh((Sch/S)_proetale)` of topoi.

```lean
public noncomputable def smallProetaleToBigProetaleMorphism :
    MorphismOfTopoi
      (Sheaf (SmallProetale.topology B T.obj T.property) (Type (u + 1)))
      (Sheaf (BigProetaleOver.topology B S.obj S.property) (Type (u + 1)))
```

**`AlgebraicGeometry.ProEtale.smallProetaleToBigProetaleLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean#L464). The attribute's comment: “existence of lower shriek”.

> The lower shriek is left adjoint to inverse image.

```lean
public noncomputable def smallProetaleToBigProetaleLowerShriekAdjunction :
    smallProetaleToBigProetaleLowerShriek B T S f ⊣
      (smallProetaleToBigProetaleMorphism B T S f).inverseImage
```

**`AlgebraicGeometry.ProEtale.smallProetaleToBigProetaleLowerShriek_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean#L481). The attribute's comment: “lower shriek preserves fibre products”.

> The lower shriek preserves fibre products.

```lean
public instance smallProetaleToBigProetaleLowerShriek_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan
      (smallProetaleToBigProetaleLowerShriek B T S f)
```

**`AlgebraicGeometry.ProEtale.smallProetaleToBigProetaleLowerShriek_preservesEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean#L494). The attribute's comment: “lower shriek preserves equalizers”.

> The lower shriek preserves equalizers.

```lean
public instance smallProetaleToBigProetaleLowerShriek_preservesEqualizers :
    PreservesLimitsOfShape WalkingParallelPair
      (smallProetaleToBigProetaleLowerShriek B T S f)
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.sheafPullbackCocontinuousIsoSheafPushforwardContinuous`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean#L64) (StacksFrontier): “the inverse-image formula”.

## Tag 098Q, a lemma

[Tag 098Q](https://stacks.math.columbia.edu/tag/098Q) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.smallProetaleInclusion_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SiteFunctorLimits.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SiteFunctorLimits.lean#L55). The attribute's comment: “preservation of fibre products”.

> Fibre products in the small pro-étale site remain fibre products in the
> big pro-étale slice.

```lean
public instance smallProetaleInclusion_preservesPullbacks
    (B : BigProetaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    PreservesLimitsOfShape WalkingCospan (SmallProetale.inclusion B S hS)
```

**`AlgebraicGeometry.ProEtale.smallProetaleInclusion_preservesTerminal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean#L85). The attribute's comment: “preservation of the final object”.

> The inclusion carries the final object of the small pro-étale site to the
> final object of the big pro-étale slice.

```lean
public instance smallProetaleInclusion_preservesTerminal :
    PreservesLimit (Functor.empty.{0} (SmallProetale B S hS))
      (SmallProetale.inclusion B S hS)
```

**`AlgebraicGeometry.ProEtale.smallProetaleInclusion_isMorphismOfSites`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean#L100). The attribute's comment: “the morphism of sites”.

> The full inclusion defines a morphism of sites from the big pro-étale
> slice to the small pro-étale site.

```lean
public instance smallProetaleInclusion_isMorphismOfSites :
    _root_.IsMorphismOfSites.{u + 1} (SmallProetale.inclusion B S hS)
      (SmallProetale.topology B S hS) (BigProetaleOver.topology B S hS)
```

**`AlgebraicGeometry.ProEtale.bigProetaleToSmallProetaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean#L156). The attribute's comment: “the projection of topoi”.

> The geometric morphism `π_S` associated to the inclusion of the small
> pro-étale site into the big pro-étale slice.

```lean
public noncomputable def bigProetaleToSmallProetaleMorphism :
    MorphismOfTopoi
      (Sheaf (BigProetaleOver.topology B S hS) (Type (u + 1)))
      (Sheaf (SmallProetale.topology B S hS) (Type (u + 1)))
```

**`AlgebraicGeometry.ProEtale.projectionCompInclusionPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean#L177). The attribute's comment: “the section property”.

> The composite `π_S ∘ i_S` is naturally the identity of the small
> pro-étale topos, with `i_S = i_{\mathrm{id}_S}`.

```lean
public noncomputable def projectionCompInclusionPushforwardIso :
    (smallProetaleToBigProetaleMorphism B
        (⟨S, hS⟩ : B.Scheme) (⟨S, hS⟩ : B.Scheme)
        (𝟙 (⟨S, hS⟩ : B.Scheme))).pushforward ⋙
      (bigProetaleToSmallProetaleMorphism B S hS).pushforward ≅
        𝟭 (Sheaf (SmallProetale.topology B S hS) (Type (u + 1)))
```

**`AlgebraicGeometry.ProEtale.inclusionInverseImageIsoProjectionPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean#L228). The attribute's comment: “inverse image is restriction”.

> Inverse image along `i_S` is naturally restriction to the small
> pro-étale site, equivalently direct image along `π_S`.

```lean
public noncomputable def inclusionInverseImageIsoProjectionPushforward :
    (smallProetaleToBigProetaleMorphism B
        (⟨S, hS⟩ : B.Scheme) (⟨S, hS⟩ : B.Scheme)
        (𝟙 (⟨S, hS⟩ : B.Scheme))).inverseImage ≅
      (bigProetaleToSmallProetaleMorphism B S hS).pushforward
```

Declarations registered for the tag:

- [`AlgebraicGeometry.ProEtale.smallProetaleToBigProetaleMorphism`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallToBigTopos.lean#L439), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean#L171) (StacksFrontier): “the inclusion i_S is i_id from 098P”.

## Tag 098R, a definition

[Tag 098R](https://stacks.math.columbia.edu/tag/098R) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.bigProetaleToSmallProetaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallProjection.lean#L156). The attribute's comment: “restriction to the small pro-étale site is the pushforward along this projection”.

> The geometric morphism `π_S` associated to the inclusion of the small
> pro-étale site into the big pro-étale slice.

```lean
public noncomputable def bigProetaleToSmallProetaleMorphism :
    MorphismOfTopoi
      (Sheaf (BigProetaleOver.topology B S hS) (Type (u + 1)))
      (Sheaf (SmallProetale.topology B S hS) (Type (u + 1)))
```

## Tag 098S, a lemma

[Tag 098S](https://stacks.math.columbia.edu/tag/098S) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.bigProetaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean#L85). The attribute's comment: “the morphism of topoi”.

> The geometric morphism of big pro-étale topoi induced by `f`.

```lean
public noncomputable def bigProetaleMorphism :
    MorphismOfTopoi
      (Sheaf (BigProetaleOver.topology B T.obj T.property) (Type (u + 1)))
      (Sheaf (BigProetaleOver.topology B S.obj S.property) (Type (u + 1)))
```

**`AlgebraicGeometry.ProEtale.bigProetaleLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean#L102). The attribute's comment: “existence of lower shriek”.

> Lower shriek is left adjoint to inverse image.

```lean
public noncomputable def bigProetaleLowerShriekAdjunction :
    (Over.map f).sheafPullback (Type (u + 1))
      (BigProetaleOver.topology B T.obj T.property)
      (BigProetaleOver.topology B S.obj S.property) ⊣
        (bigProetaleMorphism B T S f).inverseImage
```

**`AlgebraicGeometry.ProEtale.bigProetaleLowerShriek_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean#L119). The attribute's comment: “lower shriek preserves fibre products”.

> Lower shriek preserves fibre products.

```lean
public instance bigProetaleLowerShriek_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan
      ((Over.map f).sheafPullback (Type (u + 1))
        (BigProetaleOver.topology B T.obj T.property)
        (BigProetaleOver.topology B S.obj S.property))
```

**`AlgebraicGeometry.ProEtale.bigProetaleLowerShriek_preservesEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean#L130). The attribute's comment: “lower shriek preserves equalizers”.

> Lower shriek preserves equalizers.

```lean
public instance bigProetaleLowerShriek_preservesEqualizers :
    PreservesLimitsOfShape WalkingParallelPair
      ((Over.map f).sheafPullback (Type (u + 1))
        (BigProetaleOver.topology B T.obj T.property)
        (BigProetaleOver.topology B S.obj S.property))
```

Declarations registered for the tag:

- [`CategoryTheory.Over.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.map#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean#L59) (StacksFrontier): “the composition functor”. References: EGA I (2.5.3); EGA I (2.5.4), “more general”; SGA 3 I (1.6); SGA 4 IV (5.5).
- [`CategoryTheory.Over.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean#L64) (StacksFrontier): “the base-change functor”. References: EGA I (3.3.7), “more general”; EGA IV (8.2.6); SGA 3 I (1.6); SGA 4 III (5.5); SGA 4 IV (5.2), “more general”; SGA 4 IV (5.5).
- [`CategoryTheory.Over.mapPullbackAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mapPullbackAdj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean#L71) (StacksFrontier): “the adjunction”.
- [`CategoryTheory.GrothendieckTopology.instIsCocontinuousOverMapOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.instIsCocontinuousOverMapOver#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean#L72) (StacksFrontier): “cocontinuity of composition”.
- [`CategoryTheory.GrothendieckTopology.instIsContinuousOverMapOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.instIsContinuousOverMapOver#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean#L74) (StacksFrontier): “continuity of composition”.
- [`CategoryTheory.GrothendieckTopology.instIsContinuousOverPullbackOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.instIsContinuousOverPullbackOver#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean#L76) (StacksFrontier): “continuity of base change”.
- [`CategoryTheory.Functor.sheafPullbackCocontinuousIsoSheafPushforwardContinuous`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean#L78) (StacksFrontier): “inverse-image formula”.
- [`CategoryTheory.Adjunction.sheafPushforwardCocontinuousIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean#L70), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigProetaleMorphism.lean#L80) (StacksFrontier): “direct-image formula and agreement of the two site functors”.

## Tag 098T, a lemma

[Tag 098T](https://stacks.math.columbia.edu/tag/098T) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.smallProetaleBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean#L80). The attribute's comment: “part (2), base-change functor”.

> Base change of a weakly étale object over `S` along `f`, regarded as an
> object of the small pro-étale site over `T`.

```lean
public noncomputable def smallProetaleBaseChange :
    SmallProetale B S.obj S.property ⥤ SmallProetale B T.obj T.property
```

**`AlgebraicGeometry.ProEtale.smallProetaleBaseChange_comp_inclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean#L92). The attribute's comment: “part (3), site square”.

> Small-site base change followed by inclusion is big-slice base change
> following inclusion, including its action on morphisms.

```lean
public theorem smallProetaleBaseChange_comp_inclusion :
    smallProetaleBaseChange B T S f ⋙ SmallProetale.inclusion B T.obj T.property =
      SmallProetale.inclusion B S.obj S.property ⋙ Over.pullback f
```

**`AlgebraicGeometry.ProEtale.smallProetaleBaseChange_isMorphismOfSites`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean#L175). The attribute's comment: “part (2), morphism of sites”.

> Base change on small pro-étale sites is continuous and defines a morphism
> of sites.

```lean
public instance smallProetaleBaseChange_isMorphismOfSites :
    _root_.IsMorphismOfSites.{u + 1} (smallProetaleBaseChange B T S f)
      (SmallProetale.topology B S.obj S.property)
      (SmallProetale.topology B T.obj T.property)
```

**`AlgebraicGeometry.ProEtale.smallProetaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean#L232). The attribute's comment: “part (2), morphism of topoi”.

> The geometric morphism induced by small pro-étale base change.

```lean
public noncomputable def smallProetaleMorphism :
    MorphismOfTopoi
      (Sheaf (SmallProetale.topology B T.obj T.property) (Type (u + 1)))
      (Sheaf (SmallProetale.topology B S.obj S.property) (Type (u + 1)))
```

**`AlgebraicGeometry.ProEtale.smallProetalePushforward_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean#L249). The attribute's comment: “part (2), direct-image formula”.

> The direct image evaluates a sheaf on the base change of the test object.

```lean
public theorem smallProetalePushforward_obj
    (F : Sheaf (SmallProetale.topology B T.obj T.property) (Type (u + 1)))
    (U : SmallProetale B S.obj S.property) :
    ((smallProetaleMorphism B T S f).pushforward.obj F).obj.obj (Opposite.op U) =
      F.obj.obj (Opposite.op ((smallProetaleBaseChange B T S f).obj U))
```

**`AlgebraicGeometry.ProEtale.inclusionBigBaseChangePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean#L261). The attribute's comment: “part (1)”.

> The inclusion `i_f` agrees with `f_big ∘ i_T`, naturally on sheaves.

```lean
public noncomputable def inclusionBigBaseChangePushforwardIso :
    (smallProetaleToBigProetaleMorphism B T S f).pushforward ≅
      (smallProetaleToBigProetaleMorphism B T T (𝟙 T)).pushforward ⋙
        (bigProetaleMorphism B T S f).pushforward
```

**`AlgebraicGeometry.ProEtale.bigSmallProetalePushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean#L299). The attribute's comment: “part (3), topos square”.

> The square of small- and big-site morphisms commutes on direct images.

```lean
public noncomputable def bigSmallProetalePushforwardCommIso :
    (bigProetaleToSmallProetaleMorphism B T.obj T.property).pushforward ⋙
        (smallProetaleMorphism B T S f).pushforward ≅
      (bigProetaleMorphism B T S f).pushforward ⋙
        (bigProetaleToSmallProetaleMorphism B S.obj S.property).pushforward
```

**`AlgebraicGeometry.ProEtale.smallProetaleMorphismFactorizationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean#L333). The attribute's comment: “part (4), factorization through big base change”.

> The small morphism factors through `i_T`, big base change, and `π_S`.

```lean
public noncomputable def smallProetaleMorphismFactorizationIso :
    (smallProetaleMorphism B T S f).pushforward ≅
      (smallProetaleToBigProetaleMorphism B T T (𝟙 T)).pushforward ⋙
        (bigProetaleMorphism B T S f).pushforward ⋙
          (bigProetaleToSmallProetaleMorphism B S.obj S.property).pushforward
```

**`AlgebraicGeometry.ProEtale.smallProetaleMorphismInclusionFactorizationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean#L352). The attribute's comment: “part (4), factorization through i_f”.

> Equivalently, the small morphism is `π_S ∘ i_f`.

```lean
public noncomputable def smallProetaleMorphismInclusionFactorizationIso :
    (smallProetaleMorphism B T S f).pushforward ≅
      (smallProetaleToBigProetaleMorphism B T S f).pushforward ⋙
        (bigProetaleToSmallProetaleMorphism B S.obj S.property).pushforward
```

## Tag 0F60, an equation

[Tag 0F60](https://stacks.math.columbia.edu/tag/0F60) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.bigSmallProetalePushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChange.lean#L299). The attribute's comment: “(f_big)_* F restricted to S_proet is (f_small)_* of F restricted to T_proet”.

> The square of small- and big-site morphisms commutes on direct images.

```lean
public noncomputable def bigSmallProetalePushforwardCommIso :
    (bigProetaleToSmallProetaleMorphism B T.obj T.property).pushforward ⋙
        (smallProetaleMorphism B T S f).pushforward ≅
      (bigProetaleMorphism B T S f).pushforward ⋙
        (bigProetaleToSmallProetaleMorphism B S.obj S.property).pushforward
```

## Tag 098U, a lemma

[Tag 098U](https://stacks.math.columbia.edu/tag/098U) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.proetaleMorphismCompPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/MorphismComposition.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/MorphismComposition.lean#L108).

> **Stacks 098U.** For composable morphisms `f : X ⟶ Y` and `g : Y ⟶ Z` of a chosen big
> pro-étale site we have `g_big ∘ f_big = (g ∘ f)_big` and `g_small ∘ f_small = (g ∘ f)_small`,
> as canonical isomorphisms of the direct-image functors.

```lean
public noncomputable def proetaleMorphismCompPushforwardIso :
    (((bigProetaleMorphism B Y Z g).comp (bigProetaleMorphism B X Y f)).pushforward ≅
        (bigProetaleMorphism B X Z (f ≫ g)).pushforward) ×
      (((smallProetaleMorphism B Y Z g).comp (smallProetaleMorphism B X Y f)).pushforward ≅
        (smallProetaleMorphism B X Z (f ≫ g)).pushforward)
```

## Tag 0F61, a lemma

[Tag 0F61](https://stacks.math.columbia.edu/tag/0F61) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.smallProetaleBaseChangePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BaseChangeSquare.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BaseChangeSquare.lean#L76). The attribute's comment: “small-site base change”.

> Restriction of a big pro-étale direct image to the small site of `S'`
> agrees naturally with small direct image after restriction to `T'`.

```lean
public noncomputable def smallProetaleBaseChangePushforwardIso
    (h : IsPullback g' f' f g) :
    (bigProetaleMorphism B T S f).pushforward ⋙
      (smallProetaleToBigProetaleMorphism B S' S g).inverseImage ≅
    (smallProetaleToBigProetaleMorphism B T' T g').inverseImage ⋙
      (smallProetaleMorphism B T' S' f').pushforward
```

**`AlgebraicGeometry.ProEtale.bigProetaleBaseChangePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BaseChangeSquare.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BaseChangeSquare.lean#L165). The attribute's comment: “big-site base change”.

> Big pro-étale direct image commutes naturally with inverse image along
> the horizontal arrows of a cartesian square.

```lean
public noncomputable def bigProetaleBaseChangePushforwardIso
    (h : IsPullback g' f' f g) :
    (bigProetaleMorphism B T S f).pushforward ⋙
      (bigProetaleMorphism B S' S g).inverseImage ≅
    (bigProetaleMorphism B T' T g').inverseImage ⋙
      (bigProetaleMorphism B T' S' f').pushforward
```

## Tag 098V, a lemma

[Tag 098V](https://stacks.math.columbia.edu/tag/098V) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.BigProetaleSheafData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigSheafCompatibleData.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigSheafCompatibleData.lean#L130). The attribute's comment: “the compatible data”.

> The data of a sheaf on the big pro-étale site over `S`, presented on the small sites: a
> sheaf on the small pro-étale site of every `T / S`, transition maps between their inverse
> images, subject to the cocycle condition and to invertibility along weakly étale maps.
> See [Stacks Project, Tag 098V](https://stacks.math.columbia.edu/tag/098V).

```lean
public structure BigProetaleSheafData
```

**`AlgebraicGeometry.ProEtale.characterizeSheafBigProetale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigSheafCompatibleData.lean, line 1207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/BigSheafCompatibleData.lean#L1207). The attribute's comment: “equivalence with big pro-étale sheaves”.

> **Stacks 098V.** Sheaves on the big pro-étale site over `S` are the same thing as
> compatible families of small pro-étale sheaves: there is an equivalence of categories whose
> component at every object over `S` is restriction to its small pro-étale site, and which
> carries the transition map of a sheaf to restriction along the projection out of the fibre
> product.

```lean
public theorem characterizeSheafBigProetale :
    ∃ (e : Sheaf (BigProetaleOver.topology B S hS) (Type (max (u + 1) v)) ≌
        BigProetaleSheafData.{u, v} B S hS)
      (ι : ∀ T : BigProetaleOver B S hS,
        e.functor ⋙ BigProetaleSheafData.eval B S hS T ≅
          smallRestriction B S hS T),
      ∀ (F : Sheaf (BigProetaleOver.topology B S hS) (Type (max (u + 1) v)))
        {T T' : BigProetaleOver B S hS} (f : T' ⟶ T)
        (U : SmallProetale B T.left.obj T.left.property),
        (((smallProetalePullbackAdjunction B f.left).homEquiv _ _
          ((e.functor.obj F).pullback f)).hom.app (op U)) ≫
            ((ι T').hom.app F).hom.app
              (op ((smallProetaleBaseChange B T'.left T.left f.left).obj U)) =
          ((ι T).hom.app F).hom.app (op U) ≫
            F.obj.map (smallProetaleBaseChangeProjection B S hS f U).op
```

## Tag 098W, a lemma

[Tag 098W](https://stacks.math.columbia.edu/tag/098W) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.affineInclusion_isDenseSubsite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineDenseSubsite.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineDenseSubsite.lean#L290).

> The affine objects of the small pro-étale site, with the topology of standard finite pro-étale
> coverings, form a dense subsite of it; restriction of sheaves along the inclusion is therefore an
> equivalence of topoi.

```lean
public theorem affineInclusion_isDenseSubsite :
    (AffineProetale.inclusion S).IsDenseSubsite
      (AffineProetale.topology S) (Scheme.ProEt.topology S)
```

## Tag 098X, a lemma

[Tag 098X](https://stacks.math.columbia.edu/tag/098X) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.AppProetale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/AppProetaleSite.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/AppProetaleSite.lean#L98). The attribute's comment: “the category”.

> The category `S_app`: the full subcategory of the small pro-étale site of `S` on the affine
> objects whose coordinate ring extension is ind-étale.

```lean
public abbrev AppProetale
```

**`AlgebraicGeometry.ProEtale.AppProetale.precoverage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/AppProetaleSite.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/AppProetaleSite.lean#L112). The attribute's comment: “the coverings”.

> Precoverage of the affine ind-étale site by finite standard pro-étale covering families.

```lean
public def precoverage : Precoverage (AppProetale S)
```

**`AlgebraicGeometry.ProEtale.AffineIndEtaleProetale.isEquivalence_restriction_addCommGrp`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/WeaklyContractibleAbelian.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/WeaklyContractibleAbelian.lean#L81). The attribute's comment: “restriction is an equivalence of topoi, for abelian sheaves”.

> **Stacks 098X for abelian sheaves.** Restriction from the small pro-étale site to the affine
> ind-étale subsite is an equivalence of categories of abelian sheaves.

```lean
instance isEquivalence_restriction_addCommGrp [IsAffine S.obj] :
    ((inclusion B S).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
      (topology B S) (SmallProetale.topology B S.obj S.property)).IsEquivalence
```

**`AlgebraicGeometry.ProEtale.AffineIndEtaleProetale.inclusion_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AffineIndEtaleDense.lean, line 555](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AffineIndEtaleDense.lean#L555). The attribute's comment: “restriction preserves sheaves”.

> **Stacks 098X.** Restriction along the inclusion takes pro-étale sheaves to sheaves on the
> affine ind-étale site.

```lean
instance inclusion_isContinuous [IsAffine S.obj] :
    (inclusion B S).IsContinuous (topology B S)
      (SmallProetale.topology B S.obj S.property)
```

**`AlgebraicGeometry.ProEtale.AffineIndEtaleProetale.isEquivalence_restriction`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AffineIndEtaleDense.lean, line 566](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AffineIndEtaleDense.lean#L566). The attribute's comment: “restriction is an equivalence of topoi”.

> **Stacks 098X.** Restriction from the small pro-étale site to the affine ind-étale subsite
> is an equivalence of categories of sheaves of sets.

```lean
instance isEquivalence_restriction [IsAffine S.obj] :
    ((inclusion B S).sheafPushforwardContinuous (Type (max u v))
      (topology B S) (SmallProetale.topology B S.obj S.property)).IsEquivalence
```

## Tag 098Z, a lemma

[Tag 098Z](https://stacks.math.columbia.edu/tag/098Z) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.bigProetale_subcanonical`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/Subcanonical.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/Subcanonical.lean#L64). The attribute's comment: “big pro-étale site”.

> The topology of a chosen big pro-étale site is subcanonical.

```lean
public instance bigProetale_subcanonical (B : BigProetaleSite.{u}) :
    B.topology.Subcanonical
```

**`AlgebraicGeometry.ProEtale.smallProetale_subcanonical`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/Subcanonical.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/Subcanonical.lean#L145). The attribute's comment: “small pro-étale site in a chosen big site”.

> The small pro-étale site inside a chosen big site is subcanonical.

```lean
public instance smallProetale_subcanonical (B : BigProetaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) :
    (SmallProetale.topology B S hS).Subcanonical
```

**`AlgebraicGeometry.ProEtale.smallAffineProetale_subcanonical`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/Subcanonical.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/Subcanonical.lean#L161). The attribute's comment: “affine small pro-étale site”.

> The affine small pro-étale site is subcanonical.

```lean
public instance smallAffineProetale_subcanonical (S : Scheme.{u}) :
    (AffineProetale.topology S).Subcanonical
```

**`AlgebraicGeometry.ProEtale.bigAffineProetale_subcanonical`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/Subcanonical.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/Subcanonical.lean#L172). The attribute's comment: “affine big pro-étale site over a scheme”.

> The affine objects of a chosen big pro-étale site over a scheme form a
> subcanonical site.

```lean
public instance bigAffineProetale_subcanonical (B : BigProetaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) :
    (BigAffineProetale.topology B S hS).Subcanonical
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.ProEt.instSubcanonicalTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.ProEt.instSubcanonicalTopology#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/Subcanonical.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/Subcanonical.lean#L56) (StacksFrontier): “small pro-étale site”.
- [`CategoryTheory.GrothendieckTopology.subcanonical_over`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.subcanonical_over#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/Subcanonical.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/Subcanonical.lean#L58) (StacksFrontier): “big pro-étale site over a scheme”. References: SGA 3 IV (4.5.3).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.12, Tag 0988](https://stacks.math.columbia.edu/tag/0988)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
