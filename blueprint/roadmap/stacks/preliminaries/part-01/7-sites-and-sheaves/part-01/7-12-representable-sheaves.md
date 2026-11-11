---
declaration: section
origin: cited
lean: StacksEffectiveEpi.IsEffectiveEpiFamily, StacksEffectiveEpi.IsUniversalEffectiveEpiFamily, CategoryTheory.GrothendieckTopology.Subcanonical, IsRepresentableSheaf, CategoryTheory.GrothendieckTopology.yonedaFullyFaithful, CategoryTheory.sheafificationAdjunction, CategoryTheory.yonedaEquiv, isLocallySurjective_coprodYonedaDesc
statement: formalized
proof: formalized
---

# 7.12 Representable sheaves

Section 7.12 of the Stacks Project, [Tag 00WO](https://stacks.math.columbia.edu/tag/00WO). 7 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00WP, a definition

[Tag 00WP](https://stacks.math.columbia.edu/tag/00WP) in the Stacks Project.

**`StacksEffectiveEpi.IsEffectiveEpiFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Representable/EffectiveEpiFamily.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Representable/EffectiveEpiFamily.lean#L73). References: SGA 3 IV (1.3), “effective epimorphism”; SGA 3 IV (1.13), “effective epi family”; SGA 4 I (10.3), “effective epi family”.

> **Stacks 00WP.** A family `{X i ⟶ B}` in a category `C` is an *effective epimorphic
> family* if it is representable and if for every object `Y` the diagram
> `Mor(B, Y) → ∏ᵢ Mor(X i, Y) ⇉ ∏₍ᵢ,ⱼ₎ Mor(X i ×_B X j, Y)` is an equalizer.
>
> The equalizer condition is spelled out as: a family `g i : X i ⟶ Y` whose two restrictions
> to any fibre product `X i ×_B X j` agree extends uniquely to `B`.  Both halves of the
> equalizer property are contained in the `∃!`: uniqueness says that
> `Mor(B, Y) → ∏ᵢ Mor(X i, Y)` is injective, existence says that its image is the set of
> compatible families.  Fibre products are referred to through `IsPullback`, so that the
> condition does not depend on a choice of pullbacks; representability guarantees that at
> least one such square exists for every pair `(i, j)`.

```lean
def IsEffectiveEpiFamily : Prop
```

**`StacksEffectiveEpi.IsUniversalEffectiveEpiFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Representable/EffectiveEpiFamily.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Representable/EffectiveEpiFamily.lean#L91). References: SGA 3 IV (1.3), “universal eff. epi”; SGA 3 IV (1.13), “universal variant”; SGA 4 I (10.3), “univ. eff. epi family”; SGA 4 II (2.5), “univ. effective epi fam”; SGA 3 IV (3.3.3.1), “Singleton case”; SGA 3 IV (3.4.2); SGA 3 IX (5.4).

> **Stacks 00WP.** A family `{X i ⟶ B}` is a *universal effective epimorphic family* if it
> is representable and if for every morphism `h : V ⟶ B` the base-changed family
> `{X i ×_B V ⟶ V}` is an effective epimorphic family.

```lean
def IsUniversalEffectiveEpiFamily : Prop
```

## Tag 00WQ, a definition

[Tag 00WQ](https://stacks.math.columbia.edu/tag/00WQ) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.Subcanonical`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.Subcanonical#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Representable/RepresentableIsSheaf.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Representable/RepresentableIsSheaf.lean#L22) (StacksCore): “a topology is subcanonical when every representable presheaf is a sheaf for it”. References: SGA 3 IV (4.5); SGA 3 IV (4.5.5); SGA 3 IV (4.6); SGA 3 IV (4.7); SGA 3 VIB (10.15); SGA 4 II (2.5.1); SGA 4 II (4.6.3); SGA 4 IV (0.1); SGA 4 VII (2.1); SGA 7 VII (1.3.8).

## Tag 00WR, a definition

[Tag 00WR](https://stacks.math.columbia.edu/tag/00WR) in the Stacks Project.

**`IsRepresentableSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Representable/RepresentableSheafDefs.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Representable/RepresentableSheafDefs.lean#L28). References: SGA 4 I (1.4.1), “special case”.

> A sheaf `F` on a site whose topology `J` is subcanonical is *representable* if it is
> isomorphic to the sheaf `h_U = J.yoneda.obj U` for some object `U`. This is
> `(GrothendieckTopology.yoneda J).essImage` with the witnessing isomorphism written the other way
> round.

```lean
def IsRepresentableSheaf {C : Type u} [Category.{v, u} C]
    (J : GrothendieckTopology C) [J.Subcanonical]
    (F : Sheaf J (Type v)) : Prop
```

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.yonedaFullyFaithful`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.yonedaFullyFaithful#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Representable/RepresentableSheafDefs.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Representable/RepresentableSheafDefs.lean#L33) (StacksFrontier): “full subcategory of sheaves”. References: EGA 0 (8.1.7), “more general”; SGA 3 I (1.1), “special case”; SGA 3 IV (4.5.1); SGA 4 II (4.4.0), “full faithfulness”; SGA 4 V (2.4.1); SGA 4 VI (2.17), “more general”; SGA 4 VI (3.11), “b)”; SGA 4 VII (2.1), “more general”.

## Tag 090I, an equation

[Tag 090I](https://stacks.math.columbia.edu/tag/090I) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.sheafificationAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.sheafificationAdjunction#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Representable/MapsFromRepresentable.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Representable/MapsFromRepresentable.lean#L25) (StacksCore): “(1) morphisms from the sheafification of a representable presheaf to a sheaf `F` correspond to morphisms of presheaves `h_U ⟶ F`, by the hom-equivalence of the sheafification adjunction”. References: EGA 0 (3.5.6), “more general”; SGA 4 IV (10.4.1).
- [`CategoryTheory.yonedaEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.yonedaEquiv#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Representable/MapsFromRepresentable.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Representable/MapsFromRepresentable.lean#L28) (StacksCore): “(2) morphisms of presheaves `h_U ⟶ F` correspond to elements of `F(U)`, by the Yoneda lemma”. References: EGA 0 (8.1.3); EGA 0 (8.1.4); EGA 0 (8.1.6), “more general”; EGA 0 (8.1.8), “partial, special case”; SGA 3 I (1.1); SGA 3 I (1.1.1), “more general”; SGA 3 I (1.6.1), “Hom(h\_S, F) ≃ F(S)”; SGA 3 I (1.7.0), “partial”; SGA 3 IV (4.3.1), “partial”; SGA 4 I (1.4), “bijection Hom(h(X)”; SGA 4 I (8.3.2), “partial”.

## Tag 00WT, a lemma

[Tag 00WT](https://stacks.math.columbia.edu/tag/00WT) in the Stacks Project.

**`isLocallySurjective_coprodYonedaDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Representable/CoproductYonedaDesc.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Representable/CoproductYonedaDesc.lean#L36).

> **Stacks 00WT.** Let `(C, J)` be a site. If `{f_i : U_i ⟶ U}_{i ∈ I}` is a covering of `U`,
> then the canonical map `∐_i h_{U_i} ⟶ h_U` of presheaves of sets is locally surjective for
> `J`; equivalently, it becomes an epimorphism after sheafification.

```lean
theorem isLocallySurjective_coprodYonedaDesc
    {C : Type u} [Category.{v} C] (J : GrothendieckTopology C)
    {I : Type v} (U : I → C) (X : C) (f : ∀ i, U i ⟶ X)
    (hf : Sieve.generate (Presieve.ofArrows U f) ∈ J X) :
    Presheaf.IsLocallySurjective J (coprodYonedaDesc U X f)
```

## Tag 00WS, a lemma

[Tag 00WS](https://stacks.math.columbia.edu/tag/00WS) in the Stacks Project.

**`Stacks.Sites.CoveredByRepresentables.isLocallySurjective_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Representable/CoveredByRepresentables.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Representable/CoveredByRepresentables.lean#L176).

> **Stacks 00WS** (narrowed to the substantive first step of the Stacks
> proof). Let `J` be a Grothendieck topology on `C`, let `E ⊆ Ob(C)` be a
> covering subset of the site (Definition `IsCoveringSubset`), and let `F00WS` be a
> sheaf of sets on `C`.
>
> Then the canonical map
> `π : F00WS₀ := a(∐_{(U, s) : E × F00WS(U)} y(U)) ⟶ F00WS`
> into `F00WS` is an *epimorphism* in `Sheaf J (Type max v u)`, where `a` denotes
> sheafification. Equivalently, `π` is locally surjective.
>
> The full Stacks 00WS statement — that `F00WS` is a coequalizer
> `F00WS₁ ⇉ F00WS₀ → F00WS` of two such coproducts — follows by combining this lemma with
> Stacks 086K applied to `π` (existence of `F00WS₁`) and to the analogous epimorphism
> onto the kernel pair `F00WS₀ ×_F F00WS₀` (faithfulness of the coequalizer cofork).

```lean
theorem isLocallySurjective_π {E : Set C} (hE : IsCoveringSubset J E)
    (F00WS : Sheaf J (Type max v u)) :
    Sheaf.IsLocallySurjective (π J E F00WS)
```

## Tag 0GLW, a lemma

[Tag 0GLW](https://stacks.math.columbia.edu/tag/0GLW) in the Stacks Project.

**`CategoryTheory.Sheaf.colimitOfRepresentable`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Density.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Density.lean#L171). The attribute's comment: “(main statement) Every sheaf of sets on a site is the colimit of the sheafified representables over its category of elements. The final clause, that the diagram may be taken to land in a given family of objects covering every object, is not covered.”. References: SGA 4 IV (6.3), “for each sheaf F”.

> A sheaf `F` of sets on a site `C` is the colimit of the sheafified representables
> `h_{U_i}^#` along the diagram `indexingDiagram J F`.

```lean
noncomputable def colimitOfRepresentable : IsColimit (coconeOfRepresentable J F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.12, Tag 00WO](https://stacks.math.columbia.edu/tag/00WO)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
