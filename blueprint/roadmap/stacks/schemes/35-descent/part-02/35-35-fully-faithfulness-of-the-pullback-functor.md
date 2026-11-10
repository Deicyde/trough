---
declaration: section
origin: cited
lean: AlgebraicGeometry.Flat.faithful_overPullback_of_surjective, AlgebraicGeometry.pullbackFunctor_faithful, AlgebraicGeometry.pullbackFunctor_fullyFaithful_of_fpqc, AlgebraicGeometry.DescentData.selfPullbackFunctorIso, AlgebraicGeometry.pullbackFunctor_isEquivalence_of_exists_reverse, AlgebraicGeometry.pullbackFunctor_faithful_of_source_surjective_flat, AlgebraicGeometry.pullbackFunctor_fullyFaithful_of_source_fpqc, AlgebraicGeometry.pullbackFunctor_fullyFaithful_of_fpqcRefinement
statement: formalized
proof: formalized
---

# 35.35 Fully faithfulness of the pullback functors

Section 35.35 of the Stacks Project, [Tag 02VV](https://stacks.math.columbia.edu/tag/02VV). 12 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02VX, a lemma

[Tag 02VX](https://stacks.math.columbia.edu/tag/02VX) in the Stacks Project.

**`AlgebraicGeometry.Flat.faithful_overPullback_of_surjective`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/BaseChangeFaithful.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/BaseChangeFaithful.lean#L49).

> **Stacks Project, Tag 02VX.** Base change along a surjective flat morphism of schemes is a
> faithful functor on the category of schemes over the base.

```lean
instance Flat.faithful_overPullback_of_surjective {S' S : Scheme.{u}} (h : S' ⟶ S)
    [Flat h] [Surjective h] : (Over.pullback h).Faithful
```

## Tag 0240, a lemma

[Tag 0240](https://stacks.math.columbia.edu/tag/0240) in the Stacks Project.

**`AlgebraicGeometry.pullbackFunctor_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/PullbackFaithful.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germs/PullbackFaithful.lean#L42).

> **Stacks Project, Tag 0240.** Pullback of descent data along a surjective flat morphism
> is faithful.

```lean
theorem pullbackFunctor_faithful
    {S S' X X' : Scheme.{u}} {a : X ⟶ S} {a' : X' ⟶ S'} {h : S' ⟶ S}
    {f : X' ⟶ X} {comm : f ≫ a = a' ≫ h}
    (P : DescentData.PullbackFunctor a a' h f comm) [Surjective f] [Flat f] :
    P.functor.Faithful
```

## Tag 0241, a lemma

[Tag 0241](https://stacks.math.columbia.edu/tag/0241) in the Stacks Project.

**`AlgebraicGeometry.pullbackFunctor_fullyFaithful_of_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/PullbackFullyFaithful.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germs/PullbackFullyFaithful.lean#L504).

> **Stacks Project, Tag 0241.** Pullback along an fpqc covering over a fixed
> base scheme is fully faithful on descent data.

```lean
public theorem pullbackFunctor_fullyFaithful_of_fpqc
    {S X X' : Scheme.{u}} {a : X ⟶ S} {a' : X' ⟶ S} {f : X' ⟶ X}
    {comm : f ≫ a = a' ≫ (𝟙 S)}
    (P : DescentData.PullbackFunctor a a' (𝟙 S) f comm)
    (hcover : Presieve.singleton f ∈ Scheme.fpqcPrecoverage X) :
    Nonempty P.functor.FullyFaithful
```

## Tag 0242, a lemma

[Tag 0242](https://stacks.math.columbia.edu/tag/0242) in the Stacks Project.

**`AlgebraicGeometry.DescentData.selfPullbackFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/Equivalence.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/Equivalence.lean#L47).

> Pullback of descent data along a selfmap `f : X ⟶ X` over `S` is isomorphic to the identity
> functor on the category of descent data relative to `X ⟶ S`.

```lean
def selfPullbackFunctorIso {S X : Scheme.{u}} (a : X ⟶ S) (f : X ⟶ X) (hf : f ≫ a = a) :
    (pullbackFunctor a a (𝟙 S) f (by simpa using hf)).functor ≅ 𝟭 _
```

## Tag 0243, a lemma

[Tag 0243](https://stacks.math.columbia.edu/tag/0243) in the Stacks Project.

**`AlgebraicGeometry.pullbackFunctor_isEquivalence_of_exists_reverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/Equivalence.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/Equivalence.lean#L68).

> Pullback of descent data along `f : X' ⟶ X` is an equivalence if there is a morphism
> `X ⟶ X'` over the same base scheme.

```lean
theorem pullbackFunctor_isEquivalence_of_exists_reverse
    {S X X' : Scheme.{u}} (a : X ⟶ S) (a' : X' ⟶ S) (f : X' ⟶ X)
    (comm : f ≫ a = a') (h : ∃ g : X ⟶ X', g ≫ a' = a) :
    (DescentData.pullbackFunctor a a' (𝟙 S) f (by simpa using comm)).functor.IsEquivalence
```

## Tag 040J, a lemma

[Tag 040J](https://stacks.math.columbia.edu/tag/040J) in the Stacks Project.

**`AlgebraicGeometry.pullbackFunctor_faithful_of_source_surjective_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/SourceFaithful.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/SourceFaithful.lean#L70).

> **Stacks Project, Tag 040J.** Pullback of descent data along a morphism whose source is
> surjective and flat over the base is faithful.

```lean
theorem pullbackFunctor_faithful_of_source_surjective_flat
    {S X X' : Scheme.{u}} (a : X ⟶ S) (a' : X' ⟶ S) (f : X ⟶ X') (comm : f ≫ a' = a)
    [Surjective a] [Flat a] :
    (DescentData.pullbackFunctor a' a (𝟙 S) f (by simpa using comm)).functor.Faithful
```

## Tag 040K, a lemma

[Tag 040K](https://stacks.math.columbia.edu/tag/040K) in the Stacks Project.

**`AlgebraicGeometry.pullbackFunctor_fullyFaithful_of_source_fpqc`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/SourceFullyFaithful.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/SourceFullyFaithful.lean#L59). References: SGA 1 VIII (5.2).

> Pullback along a morphism `X ⟶ X'` over `S` is fully
> faithful on descent data if `X ⟶ S` is an fpqc covering.

```lean
lemma pullbackFunctor_fullyFaithful_of_source_fpqc
    {S X X' : Scheme.{u}} (a : X ⟶ S) (a' : X' ⟶ S) (f : X ⟶ X') (comm : f ≫ a' = a)
    (hcover : Presieve.singleton a ∈ Scheme.fpqcPrecoverage S) :
    Nonempty
      (DescentData.pullbackFunctor a' a (𝟙 S) f
        (by simpa using comm)).functor.FullyFaithful
```

## Tag 02VZ, a lemma

[Tag 02VZ](https://stacks.math.columbia.edu/tag/02VZ) in the Stacks Project.

**`AlgebraicGeometry.pullbackFunctor_fullyFaithful_of_fpqcRefinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/PullbackFpqcRefinement.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germs/PullbackFpqcRefinement.lean#L91).

> An fpqc refinement of each member of a family induces a fully faithful
> pullback functor on descent data.

```lean
public theorem pullbackFunctor_fullyFaithful_of_fpqcRefinement
    {S : Scheme.{u}} (U V : PreZeroHypercover.{u} S)
    (α : U.HomOver V (𝟙 S))
    (hfpqc : ∀ j : V.I₀,
      Presieve.ofArrows
        (fun i : {i : U.I₀ // α.s₀ i = j} ↦ U.X i)
        (fun i ↦ α.h₀ i.val ≫ eqToHom (congrArg V.X i.property)) ∈
          Scheme.fpqcPrecoverage (V.X j)) :
    Nonempty ((MorphismOfSchemeFamilies.pullbackFunctor
      { sourceBase := S, targetBase := S,
        sourceFamily := U, targetFamily := V,
        baseHom := 𝟙 S, familyHom := α }).functor.FullyFaithful)
```

## Tag 02VY, a lemma

[Tag 02VY](https://stacks.math.columbia.edu/tag/02VY) in the Stacks Project.

**`AlgebraicGeometry.pullbackFunctor_isEquivalence_of_zariskiRefinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/ZariskiRefinementEquivalence.lean, line 1158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Scheme/ZariskiRefinementEquivalence.lean#L1158).

> A fibrewise Zariski refinement induces an equivalence on descent data.

```lean
public theorem pullbackFunctor_isEquivalence_of_zariskiRefinement
    {S : Scheme.{u}} (U V : PreZeroHypercover.{u} S)
    (α : U.HomOver V (𝟙 S))
    (hZar : ∀ j : V.I₀,
      Presieve.ofArrows
        (fun i : {i : U.I₀ // α.s₀ i = j} ↦ U.X i)
        (fun i ↦ α.h₀ i.val ≫ eqToHom (congrArg V.X i.property)) ∈
          Scheme.zariskiPrecoverage (V.X j)) :
    Nonempty ((MorphismOfSchemeFamilies.pullbackFunctor
      { sourceBase := S, targetBase := S,
        sourceFamily := U, targetFamily := V,
        baseHom := 𝟙 S, familyHom := α }).functor.IsEquivalence)
```

**`AlgebraicGeometry.descentData_equivalence_of_zariskiCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/ZariskiRefinementEquivalence.lean, line 1204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Scheme/ZariskiRefinementEquivalence.lean#L1204).

> Schemes over a base are equivalent to descent data for any Zariski cover.

```lean
public theorem descentData_equivalence_of_zariskiCovering
    {S : Scheme.{u}} (U : PreZeroHypercover.{u} S)
    (hZar : Presieve.ofArrows U.X U.f ∈ Scheme.zariskiPrecoverage S) :
    Nonempty (Over S ≌ DescentData U.f)
```

## Tag 02W0, a lemma

[Tag 02W0](https://stacks.math.columbia.edu/tag/02W0) in the Stacks Project.

**`AlgebraicGeometry.DescentData.canonicalFunctor_fullyFaithful_of_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/CanonicalFullyFaithful.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germs/CanonicalFullyFaithful.lean#L66). The attribute's comment: “in particular, for a covering by a single morphism”. References: SGA 1 VIII (5.2), “more general”.

> If the single morphism `f : X ⟶ S` is an fpqc covering of `S`, then the canonical descent
> datum functor `Over S ⥤ DescentDatum f` is fully faithful, so schemes over `S` form a full
> subcategory of the descent data relative to `f`.

```lean
theorem canonicalFunctor_fullyFaithful_of_fpqc (f : X ⟶ S)
    (hcover : Presieve.singleton f ∈ Scheme.fpqcPrecoverage.coverings S) :
    Nonempty (canonicalFunctor f).FullyFaithful
```

**`AlgebraicGeometry.pullbackFunctor_fullyFaithful_of_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/Refinement.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/Refinement.lean#L76).

> **Stacks 02W0.** Let `U` and `V` be families of schemes over `S` and let `α` exhibit `U` as
> a refinement of `V` over the identity of `S`. If `U` is an fpqc covering of `S`, then the
> pullback functor from descent data relative to `V` to descent data relative to `U` is fully
> faithful.

```lean
theorem pullbackFunctor_fullyFaithful_of_refinement
    {S : Scheme.{u}} (U V : PreZeroHypercover.{u} S)
    (α : U.HomOver V (𝟙 S))
    (hU : Presieve.ofArrows U.X U.f ∈ Scheme.fpqcPrecoverage S) :
    Nonempty ((MorphismOfSchemeFamilies.pullbackFunctor
      { sourceBase := S, targetBase := S,
        sourceFamily := U, targetFamily := V,
        baseHom := 𝟙 S, familyHom := α }).functor.FullyFaithful)
```

**`AlgebraicGeometry.fullyFaithful_canonicalFunctor_comp_familyCoproduct_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/Refinement.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/PullbackFullyFaithful/Refinement.lean#L108). The attribute's comment: “the schemes over the base as a full subcategory of the descent data”. References: SGA 1 VIII (5.2), “more general”.

> **Stacks 02W0**, final sentence: the schemes over `S` form a full subcategory of the
> category of descent data relative to an fpqc covering `U` of `S`. The embedding is the
> canonical descent datum of the coproduct morphism of `U`, read as a descent datum for the
> family through the family–coproduct equivalence.

```lean
theorem fullyFaithful_canonicalFunctor_comp_familyCoproduct_inverse
    {S : Scheme.{u}} (U : PreZeroHypercover.{u} S)
    (hU : Presieve.ofArrows U.X U.f ∈ Scheme.fpqcPrecoverage S) :
    Nonempty ((DescentData.canonicalFunctor (Sigma.desc U.f) ⋙
      (DescentData.familyCoproductEquivalence U.f).equivalence.inverse).FullyFaithful)
```

## Tag 040L, a remark

[Tag 040L](https://stacks.math.columbia.edu/tag/040L) in the Stacks Project.

**`AlgebraicGeometry.isSheaf_relativeHom_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/MorphismDescent.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germs/MorphismDescent.lean#L103). The attribute's comment: “the functor `T ↦ Mor_T(X_T, Y_T)` on the schemes over `S` satisfies the sheaf condition for the fpqc topology”. References: SGA 1 VIII (5.2); SGA 3 IV (4.5.13), “Hom_S(X, special case”; SGA 3 VIII (1.7.1), “more general”.

> Let `X` and `Y` be schemes over `S`. The relative morphism functor
> `Mor_S(X, Y) : (Sch/S)ᵒᵖ ⥤ Set`, which sends an `S`-scheme `T` to the set of morphisms
> `X_T ⟶ Y_T` over `T`, satisfies the sheaf condition for the fpqc topology on the schemes over
> `S`.

```lean
theorem isSheaf_relativeHom_fpqc (X Y : Over S) :
    Presheaf.IsSheaf (Scheme.fpqcTopology.{u}.over S) (relativeHom X Y)
```

## Tag 0AP4, a lemma

[Tag 0AP4](https://stacks.math.columbia.edu/tag/0AP4) in the Stacks Project.

**`AlgebraicGeometry.DescentDatum.isEffective_of_forall_exists_restrictOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/DescendedScheme.lean, line 1186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Scheme/DescendedScheme.lean#L1186). References: SGA 1 VIII (7.2), “local eff ⇒ effective”.

> **Effectivity of a descent datum is local on the scheme it is carried by.** Let
> `f : X ⟶ S` be a surjective, quasi-compact, flat morphism of schemes and let `(V, φ)` be a
> descent datum relative to `X/S`. If every point of `V` has an invariant open neighbourhood
> `W ⊆ V` such that the restricted datum `(W, φ|_{W ×_S X})` is effective, then `(V, φ)` is
> effective.

```lean
theorem isEffective_of_forall_exists_restrictOpen {S X : Scheme.{u}} {f : X ⟶ S}
    [Surjective f] [Flat f] [QuasiCompact f] (D : DescentDatum f)
    (h : ∀ v : D.over.left, ∃ (W : D.over.left.Opens) (hW : D.IsTransitionInvariant W),
      v ∈ W ∧ DescentData.IsEffective (D.restrictOpen W hW)) :
    DescentData.IsEffective D
```

**`AlgebraicGeometry.DescentDatum.isEffective_of_forall_exists_restrictOpen_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/LocalEffectivity.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Scheme/LocalEffectivity.lean#L59).

> **Effectivity of a descent datum is local on the scheme it is carried by.** Let
> `f : X ⟶ S` be a surjective, quasi-compact, flat morphism of schemes and let `(V, φ)` be a
> descent datum relative to `X/S`. Suppose that for every `v ∈ V` there is an open subscheme
> `v ∈ W ⊆ V` with `φ(W ×_S X) ⊆ X ×_S W` and such that the descent datum
> `(W, φ|_{W ×_S X})` is effective. Then `(V, φ)` is effective.
>
> Only the inclusion `φ(W ×_S X) ⊆ X ×_S W` is asked for. The reverse inclusion, which makes
> `φ|_{W ×_S X}` an isomorphism onto `X ×_S W` and so the gluing isomorphism of the restricted
> datum, follows from the cocycle condition by
> `AlgebraicGeometry.DescentDatum.isTransitionInvariant_of_le`.

```lean
theorem isEffective_of_forall_exists_restrictOpen_le {S X : Scheme.{u}} {f : X ⟶ S}
    [Surjective f] [Flat f] [QuasiCompact f] (D : DescentDatum f)
    (h : ∀ v : D.over.left, ∃ (W : D.over.left.Opens)
      (hW : D.transitionPullbackIso.hom ''ᵁ (pullback.fst (D.over.hom ≫ f) f ⁻¹ᵁ W) ≤
        pullback.snd f (D.over.hom ≫ f) ⁻¹ᵁ W),
      v ∈ W ∧
        DescentData.IsEffective (D.restrictOpen W (D.isTransitionInvariant_of_le W hW))) :
    DescentData.IsEffective D
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.35, Tag 02VV](https://stacks.math.columbia.edu/tag/02VV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
