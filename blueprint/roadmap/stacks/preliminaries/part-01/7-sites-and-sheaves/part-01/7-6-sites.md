---
declaration: section
origin: cited
lean: IsSite, Opens.pretopology, Opens.grothendieckTopology, Opens.pretopology_toGrothendieck, TopCat.Presheaf.IsSheaf, TopCat.Presheaf.isSheaf_iff_isSheafUniqueGluing_types, CategoryTheory.Precoverage.chaotic, CategoryTheory.Precoverage.toGrothendieck_chaotic
statement: formalized
proof: formalized
---

# 7.6 Sites

Section 7.6 of the Stacks Project, [Tag 00VG](https://stacks.math.columbia.edu/tag/00VG). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00VH, a definition

[Tag 00VH](https://stacks.math.columbia.edu/tag/00VH) in the Stacks Project.

**`IsSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/SmallSubsite.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/SmallSubsite.lean#L185). The attribute's comment: “Stacks' definition of a site: no fibre products beyond those of axiom (3).”. References: SGA 4 II (1.3); SGA 3 IV (4.2.5).

> A class of coverings is a *site* if it satisfies the isomorphism, composition and base
> change axioms: these are axioms (1), (2) and (3) of Stacks 00VH, as `IsoCond`, `CompositionCond`
> and `BaseChangeCond`. The set `Cov(𝒞)` is the predicate `IsCov`. The coverings are families of
> morphisms with fixed target, indexed by a type (Stacks 0396), not presieves, so a family may
> repeat a morphism. Following the clarification after 00VH, axiom (3) asks for the fibre products
> `Uᵢ ×_U V` of the members of a covering only, and for the covering property of *some* choice of
> them; no other fibre products are assumed to exist.
>
> Mathlib's `CategoryTheory.Pretopology`, which also carries Stacks 00VH, is the special case of a
> category with all pullbacks, with coverings recorded as presieves and base change taken along
> the chosen pullbacks; `IsSite.pretopologyBigFppfPretopology` produces it from a site when `C` has
> pullbacks. Conversely `CategoryTheory.Precoverage.isSite_presieve₀_mem` produces a site from a
> Mathlib precoverage with `HasIsos`, `IsStableUnderComposition`, `IsStableUnderBaseChange` and
> `HasPullbacks`.

```lean
def IsSite (IsCov : Covering.{u, v, w} C → Prop) : Prop
```

## Tag 00VJ, an example

[Tag 00VJ](https://stacks.math.columbia.edu/tag/00VJ) in the Stacks Project.

Declarations registered for the tag:

- [`Opens.pretopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Opens.pretopology#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch07.lean#L25) (StacksFrontier): “the site X\_Zar: coverings of U are the families of opens with union U”. References: SGA 4 III (1.9.1); SGA 4½ Arcata (1.6.4), “partial”.
- [`Opens.grothendieckTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Opens.grothendieckTopology#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch07.lean#L27) (StacksFrontier): “the Grothendieck topology on the opens of X”. References: SGA 4 III (1.9.1); SGA 4 VII (4.2.2); SGA 4½ Arcata (1.1); SGA 4½ Arcata (1.6.4).
- [`Opens.pretopology_toGrothendieck`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Opens.pretopology_toGrothendieck#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch07.lean#L28) (StacksFrontier): “the covering families generate the Grothendieck topology of X\_Zar”.
- [`TopCat.Presheaf.IsSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.IsSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch07.lean#L30) (StacksFrontier): “sheaves on a space are by definition sheaves on the site X\_Zar”. References: EGA 0 (3.1.2); EGA 0 (3.1.4); SGA 3 IV (4.3.1), “special case”; SGA 4 IV (2.1), “partial”; SGA 4½ Arcata (1.2.3), “more general”; SGA 4½ Arcata (1.6.3), “special case”.
- [`TopCat.Presheaf.isSheaf_iff_isSheafUniqueGluing_types`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.isSheaf_iff_isSheafUniqueGluing_types#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch07.lean#L32) (StacksFrontier): “sheaves of sets on X\_Zar agree with the usual unique-gluing sheaves on X”. References: EGA 0 (3.1.2), “C = Set”; SGA 3 IV (4.3.5), “special case”; SGA 4½ Arcata (1.6.3), “topological site”.

## Tag 07GE, an example

[Tag 07GE](https://stacks.math.columbia.edu/tag/07GE) in the Stacks Project.

**`CategoryTheory.Precoverage.chaotic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/ChaoticSite.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/ChaoticSite.lean#L50). The attribute's comment: “the iso-singleton coverings, for an arbitrary category (Mathlib's `Pretopology.trivial` needs `HasPullbacks C`)”.

> The chaotic (indiscrete) precoverage on an arbitrary category `C`: the covering presieves
> of `U` are the singletons `{φ}` with `φ : V ⟶ U` an isomorphism.

```lean
def chaotic : Precoverage C
```

**`CategoryTheory.Precoverage.toGrothendieck_chaotic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/ChaoticSite.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/ChaoticSite.lean#L104). The attribute's comment: “the iso-singleton coverings of an arbitrary category generate the bottom topology”.

> The Grothendieck topology generated by the chaotic precoverage is `⊥`, the topology in which
> only the maximal sieve covers.

```lean
theorem toGrothendieck_chaotic : (chaotic C).toGrothendieck = ⊥
```

**`CategoryTheory.Precoverage.sheafChaoticEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/ChaoticSite.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/ChaoticSite.lean#L120). The attribute's comment: “sheaves on the chaotic site of an arbitrary category are the presheaves”.

> Sheaves on the chaotic site of an arbitrary category `C`, with values in a category `A`,
> are the presheaves on `C`: the forgetful functor is an equivalence of categories.

```lean
def sheafChaoticEquivalence (A : Type*) [Category* A] :
    Sheaf (chaotic C).toGrothendieck A ≌ Cᵒᵖ ⥤ A
```

Declarations registered for the tag:

- [`CategoryTheory.Pretopology.toGrothendieck_bot`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pretopology.toGrothendieck_bot#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Pretopology.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Sites/Pretopology.lean#L28) (StacksCore): “the chaotic pretopology generates the bottom topology, in which only the maximal sieve covers”.
- [`CategoryTheory.sheafBotEquivalence`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.sheafBotEquivalence#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Pretopology.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Sites/Pretopology.lean#L30) (StacksCore): “sheaves on the chaotic site are the presheaves: the forgetful functor from sheaves for the bottom topology to presheaves is an equivalence of categories”. References: SGA 3 IV (4.4.2), “final observation”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.6, Tag 00VG](https://stacks.math.columbia.edu/tag/00VG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
