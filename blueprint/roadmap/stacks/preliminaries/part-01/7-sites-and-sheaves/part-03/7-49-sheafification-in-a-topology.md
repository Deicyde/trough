---
declaration: section
origin: cited
lean: statement1_map_id, statement1_map_comp, statement2_ell_natural, statement3a_map_id, statement3a_map_comp, statement3b_ell_natural, statement4_preserves_mono, statement5_local_representability
statement: formalized
proof: formalized
---

# 7.49 Sheafification in a topology

Section 7.49 of the Stacks Project, [Tag 00ZG](https://stacks.math.columbia.edu/tag/00ZG). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 12 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00ZH, a lemma

[Tag 00ZH](https://stacks.math.columbia.edu/tag/00ZH) in the Stacks Project.

**`statement1_map_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean#L212). The attribute's comment: “(1)”. References: SGA 4 II (3.0.5), “LF presheaf: id law”.

> **Stacks 00ZH (1)**, identity law: restriction in `F⁺` along an identity arrow is the
> identity, one half of `F⁺` being a presheaf.

```lean
theorem statement1_map_id (F : Cᵒᵖ ⥤ Type u) (U : Cᵒᵖ) :
    (J.plusObj F).map (𝟙 U) = 𝟙 ((J.plusObj F).obj U)
```

**`statement1_map_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean#L219). The attribute's comment: “(1)”. References: SGA 4 II (3.0.5), “LF presheaf: comp law”.

> **Stacks 00ZH (1)**, composition law: restricting in `F⁺` along `f ≫ g` is restricting
> along `f` and then along `g`, the other half of `F⁺` being a presheaf.

```lean
theorem statement1_map_comp (F : Cᵒᵖ ⥤ Type u)
    {U V W : Cᵒᵖ} (f : U ⟶ V) (g : V ⟶ W) :
    (J.plusObj F).map (f ≫ g) = (J.plusObj F).map f ≫ (J.plusObj F).map g
```

**`statement2_ell_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean#L227). The attribute's comment: “(2)”. References: SGA 4 II (3.0.5), “ℓ(F):F→LF is natural”.

> **Stacks 00ZH (2)**: `ℓ : F ⟶ F⁺` is a morphism of presheaves, i.e. its components commute
> with restriction along any arrow `f`.

```lean
theorem statement2_ell_natural (F : Cᵒᵖ ⥤ Type u) {U V : Cᵒᵖ} (f : U ⟶ V) :
    F.map f ≫ (J.toPlus F).app V = (J.toPlus F).app U ≫ (J.plusObj F).map f
```

**`statement3a_map_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean#L234). The attribute's comment: “(3)”.

> **Stacks 00ZH (3)**, identity law for `F ↦ F⁺` as an operation on presheaves:
> `(𝟙 F)⁺ = 𝟙 F⁺`.

```lean
theorem statement3a_map_id (F : Cᵒᵖ ⥤ Type u) :
    (J.plusFunctor (Type u)).map (𝟙 F) = 𝟙 ((J.plusFunctor (Type u)).obj F)
```

**`statement3a_map_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean#L241). The attribute's comment: “(3)”.

> **Stacks 00ZH (3)**, composition law for `F ↦ F⁺` as an operation on presheaves:
> `(α ≫ β)⁺ = α⁺ ≫ β⁺`.

```lean
theorem statement3a_map_comp {F G H : Cᵒᵖ ⥤ Type u} (α : F ⟶ G) (β : G ⟶ H) :
    (J.plusFunctor (Type u)).map (α ≫ β) =
      (J.plusFunctor (Type u)).map α ≫ (J.plusFunctor (Type u)).map β
```

**`statement3b_ell_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean#L249). The attribute's comment: “(3)”.

> **Stacks 00ZH (3)**, naturality of `ℓ` in the presheaf variable: the square
> `α ≫ ℓ G = ℓ F ≫ α⁺` commutes, so `ℓ` is a natural transformation `𝟭 ⟶ plusFunctor`.

```lean
theorem statement3b_ell_natural {F G : Cᵒᵖ ⥤ Type u} (α : F ⟶ G) :
    α ≫ J.toPlus G = J.toPlus F ≫ J.plusMap α
```

**`statement4_preserves_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean#L257). The attribute's comment: “(4)”. References: SGA 3 IV (4.3.10.0).

> **Stacks 00ZH (4)**: if `α : F ⟶ G` is injective on sections over every object, then so is
> `α⁺`. The sections of `F⁺` over `U` form a filtered colimit of multiequalizers, and
> injectivity survives both `diagramNatTrans` and the filtered colimit.

```lean
theorem statement4_preserves_mono
    {F G : Cᵒᵖ ⥤ Type u} (α : F ⟶ G)
    (hα : ∀ U : Cᵒᵖ, Function.Injective (α.app U)) :
    ∀ U : Cᵒᵖ, Function.Injective ((J.plusMap α).app U)
```

**`statement5_local_representability`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/PlusProperties.lean#L270). The attribute's comment: “(5)”.

> **Stacks 00ZH (5)**: every section `s` of `F⁺` over `U` is locally in the image of `ℓ` —
> there is a covering sieve `S ∈ J U` and a `φ : S.functor ⟶ F` with `φ ≫ J.toPlus F` equal to the
> restriction of `s` to `S`, expressed via `S.functorInclusion` and `yonedaEquiv.symm s`.

```lean
theorem statement5_local_representability
    (F : Cᵒᵖ ⥤ Type u) (U : C) (s : (J.plusObj F).obj (op U)) :
    ∃ (S : Sieve U) (_ : S ∈ J U) (φ : S.functor ⟶ F),
      φ ≫ J.toPlus F =
        S.functorInclusion ≫ (CategoryTheory.yonedaEquiv.symm s)
```

## Tag 00ZI, a definition

[Tag 00ZI](https://stacks.math.columbia.edu/tag/00ZI) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Presieve.IsSeparated`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Presieve.IsSeparated#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/PlusIsSheaf.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/PlusIsSheaf.lean#L21) (StacksFrontier): “a presheaf of sets is separated for `J` when the canonical map `F U ⟶ Mor_{PSh(C)}(S, F)` is injective for every covering sieve `S` on every `U`”. References: SGA 3 IV (4.3.18); SGA 3 XXII (4.1.11); SGA 4 II (2.7); SGA 4 II (3.2); SGA 3 IV (4.3.1), “separated presheaf”; SGA 4 II (2.1), “separated clause”.

## Tag 00ZJ, a theorem

[Tag 00ZJ](https://stacks.math.columbia.edu/tag/00ZJ) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.Plus.sep`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.Plus.sep#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Plus.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Plus.lean#L60) (StacksCore): “(1) The presheaf `LF` is separated: two sections of `LF` over `X` whose restrictions along every arrow of a covering of `X` agree are equal.”. References: SGA 3 IV (4.3.11), “(i), LP separated”; SGA 4 II (3.2), “2)”.
- [`CategoryTheory.GrothendieckTopology.Plus.isSheaf_of_sep`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.Plus.isSheaf_of_sep#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Plus.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Plus.lean#L66) (StacksCore): “(2) If `F` is separated then `LF` is a sheaf.”. References: SGA 4 II (3.2), “part of 3)”; SGA 3 IV (4.3.11), “(iv), LP a sheaf”.
- [`CategoryTheory.GrothendieckTopology.Plus.inj_of_sep`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.Plus.inj_of_sep#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Plus.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Plus.lean#L71) (StacksCore): “(2) If `F` is separated then the map of presheaves `F → LF` is injective on the sections over every object.”. References: SGA 3 IV (4.3.11), “(iv), mono part”; SGA 4 II (3.2), “3) sep ⇒ ℓ(F) mono”.
- [`CategoryTheory.GrothendieckTopology.isIso_toPlus_of_isSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.isIso_toPlus_of_isSheaf#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Plus.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Plus.lean#L77) (StacksCore): “(3) If `F` is a sheaf then `F → LF` is an isomorphism.”. References: SGA 4 II (3.2), “4) (ii) ⇒ (i)”; SGA 3 IV (4.3.11), “more general”.
- [`CategoryTheory.GrothendieckTopology.Plus.isSheaf_plus_plus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.Plus.isSheaf_plus_plus#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Plus.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Plus.lean#L81) (StacksCore): “(4) The presheaf `LLF` is always a sheaf.”. References: SGA 3 IV (4.3.11), “(iv), special case”; SGA 4 II (3.2), “clause 3, special case”.

## Tag 00ZL, a definition

[Tag 00ZL](https://stacks.math.columbia.edu/tag/00ZL) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.sheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.sheafify#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/AssociatedSheaf.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/AssociatedSheaf.lean#L26) (StacksFrontier): “the sheaf F^# = L L F”. References: SGA 3 IV (4.3.14); SGA 3 IV (4.3.15); SGA 3 VIB (8.1); SGA 4 II (3.5), “the sheaf F^# = LLF”.
- [`CategoryTheory.GrothendieckTopology.toSheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.toSheafify#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/AssociatedSheaf.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/AssociatedSheaf.lean#L32) (StacksFrontier): “the canonical map F → F^#”. References: SGA 4 II (3.5), “canonical map F → aF”.
- [`CategoryTheory.GrothendieckTopology.sheafify_isSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.sheafify_isSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/AssociatedSheaf.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/AssociatedSheaf.lean#L35) (StacksFrontier): “F^# is a sheaf”. References: SGA 3 IV (4.3.14), “more general”; SGA 4 II (3.5), “aF is a sheaf”.
- [`CategoryTheory.GrothendieckTopology.toPlus_naturality`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.toPlus_naturality#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/AssociatedSheaf.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/AssociatedSheaf.lean#L42) (StacksFrontier): “the canonical map F → F^# is the composite of the two units ℓ_F and ℓ_{L F} of the plus construction: naturality of `toPlus` at `toPlus F` turns Mathlib's `toPlus F ≫ plusMap (toPlus F)` into `toPlus F ≫ toPlus (plusObj F)`”.

## Tag 00ZM, a proposition

[Tag 00ZM](https://stacks.math.columbia.edu/tag/00ZM) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.toSheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.toSheafify#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/SheafificationUniversal.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/SheafificationUniversal.lean#L23) (StacksFrontier): “the canonical map `F ⟶ F^#` to the sheafification, the unit of the adjunction”.
- [`CategoryTheory.sheafificationAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.sheafificationAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/SheafificationUniversal.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topology/SheafificationUniversal.lean#L25) (StacksFrontier): “composing with the canonical map is a bijection `Mor_{Sh(C)}(F^#, G) ≃ Mor_{PSh(C)}(F, G)`, i.e. every map from `F` into a sheaf factors uniquely through `F ⟶ F^#`”. References: EGA 0 (3.5.6), “more general”; SGA 4 IV (10.4.1).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.49, Tag 00ZG](https://stacks.math.columbia.edu/tag/00ZG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
