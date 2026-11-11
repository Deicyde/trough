---
declaration: section
origin: cited
lean: PresheafOnBasis, PresheafOnBasis.Hom, SheafOnBasis, SheafOnBasisHom, main_theorem009K, Stacks.SheafOnBasis.sheaf_iff_cofinal_sheaf, Stacks.Topology.BasisPresheaf.germMap_bijection, Stacks.BasisExtension.sheaf_extension_exists
statement: formalized
proof: formalized
---

# 6.30 Bases and sheaves

Section 6.30 of the Stacks Project, [Tag 009H](https://stacks.math.columbia.edu/tag/009H). 17 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 009I, a definition

[Tag 009I](https://stacks.math.columbia.edu/tag/009I) in the Stacks Project.

**`PresheafOnBasis`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/Presheaf.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/Presheaf.lean#L63). The attribute's comment: “(1)”. References: EGA 0 (3.2.1), “set-valued definition”.

> A presheaf of sets on a basis `B` for the topology on `X`.

```lean
structure PresheafOnBasis (B : Set (Set X))
```

**`PresheafOnBasis.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/Presheaf.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/Presheaf.lean#L78). The attribute's comment: “(2)”. References: EGA 0 (3.2.3), “morphism definition”.

> A morphism of presheaves of sets on a basis `B`.

```lean
structure PresheafOnBasis.Hom {B : Set (Set X)} (F G : PresheafOnBasis B)
```

## Tag 009J, a definition

[Tag 009J](https://stacks.math.columbia.edu/tag/009J) in the Stacks Project.

**`SheafOnBasis`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/Sheaf.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/Sheaf.lean#L113). The attribute's comment: “(1)”. References: EGA 0 (3.2.2).

> A sheaf of sets on a basis `B` (Stacks 009J (1)): a presheaf on `B` satisfying the
> basis-sheaf condition.

```lean
structure SheafOnBasis {B : Set (Opens X)} (hB : Opens.IsBasis B)
```

**`SheafOnBasisHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/Sheaf.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/Sheaf.lean#L134). The attribute's comment: “(2)”. References: EGA 0 (3.2.3), “special case”.

> A morphism of sheaves on a basis `B` (Stacks 009J (2)): by definition a morphism of the
> underlying presheaves on `B`.

```lean
def SheafOnBasisHom {B : Set (Opens X)} {hB : Opens.IsBasis B}
    (F G : SheafOnBasis hB) : Type _
```

## Tag 009K, a lemma

[Tag 009K](https://stacks.math.columbia.edu/tag/009K) in the Stacks Project.

**`main_theorem009K`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/CofinalCoverings.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/CofinalCoverings.lean#L388).

> **Stacks Tag 009K (lemma-cofinal-systems-coverings).** A presheaf on a
> basis is a sheaf iff the sheaf condition holds on a cofinal system of
> coverings.

```lean
theorem main_theorem009K
    {B : Set (Opens X)} (hB : Opens.IsBasis B)
    (C : CofinalSystem B)
    (all : GivenIntersectionCoverings B)
    (F : BasisPresheaf B) :
    IsSheafOnBasisProp F all ↔ SheafConditionOnCofinalSystem F C all
```

## Tag 009L, a lemma

[Tag 009L](https://stacks.math.columbia.edu/tag/009L) in the Stacks Project.

**`Stacks.SheafOnBasis.sheaf_iff_cofinal_sheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/CofinalSheafCondition.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/CofinalSheafCondition.lean#L227).

> **Stacks 009L.** Let `B` be a family of subsets closed under intersection of pairs of its
> members lying in a common member, and for each `U ∈ B` let `C U` be a cofinal system of coverings
> of `U` by members of `B`. Then a presheaf of sets on `B` is a sheaf on `B` if and only if gluing
> holds for the coverings in `C U` with compatibility tested on the intersections `Uᵢ ∩ Uⱼ`.

```lean
theorem sheaf_iff_cofinal_sheaf {B : Set (Set X)} (hB_inter : ClosedUnderInter B)
    (C : ∀ U ∈ B, Set (Covering.{u, v} B U)) (hC : IsCofinalSystem B C) (F : Presheaf.{u, w} B) :
    Presheaf.IsSheaf.{u, v, w} F ↔ F.IsSheafOnCofinal hB_inter C
```

## Tag 009M, a lemma

[Tag 009M](https://stacks.math.columbia.edu/tag/009M) in the Stacks Project.

**`Stacks.Topology.BasisPresheaf.germMap_bijection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/Germs.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/Germs.lean#L339).

> **Stacks Project 009M (bijection form).** The germ map `Φ_U` induces
> a bijection between `F.obj U hU` and the set of `(*)`-families of germs
> over `U`.

```lean
theorem germMap_bijection {B : Set (Set X)} (hB : IsTopologicalBasis B)
    (F : PresheafOnBasisOpenSet B) (hF : F.IsSheaf) {U : Set X} (hU : U ∈ B) :
    Function.Bijective
      (fun s : F.obj U hU =>
        (⟨germMap F hU s, by
          rw [← germMap_range_eq_conditionStar hB F hF hU]; exact ⟨s, rfl⟩⟩ :
          {f : ∀ x : U, Stalk F x.1 // ConditionStar F f}))
```

## Tag 009N, a lemma

[Tag 009N](https://stacks.math.columbia.edu/tag/009N) in the Stacks Project.

**`Stacks.BasisExtension.sheaf_extension_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/SetExtension.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/SetExtension.lean#L332).

> **Stacks 009N.** *Existence.* Given a sheaf `F` of sets on a basis `B`, there exists a sheaf
> `Fext` of sets on `X` together with bijections `Fext(U) ≃ F(U)` for `U ∈ B`, compatible with the
> restriction maps.
>
> Uniqueness of the extension is `sheaf_extension_unique`.

```lean
theorem sheaf_extension_exists {B : Set (Opens X)} (hB : Opens.IsBasis B)
    (F : BasisPresheaf B) (hF : F.IsSheaf) :
    ∃ (Fext : OpensPresheaf X) (_ : Fext.IsSheaf),
      Nonempty (BasisPresheaf.Iso (Fext.restrictToBasis B) F)
```

**`Stacks.BasisExtension.sheaf_extension_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/SetExtension.lean, line 567](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/SetExtension.lean#L567).

> **Stacks 009N.** *Uniqueness.* Any two sheaves on `X` extending the same sheaf `F` on the
> basis `B` are isomorphic by a unique isomorphism intertwining the comparison bijections.
>
> Existence of an extension is `sheaf_extension_exists`.

```lean
theorem sheaf_extension_unique {B : Set (Opens X)} (hB : Opens.IsBasis B)
    (F : BasisPresheaf B)
    (Fext : OpensPresheaf X) (hFext : Fext.IsSheaf)
    (ι : BasisPresheaf.Iso (Fext.restrictToBasis B) F)
    (G : OpensPresheaf X) (hG : G.IsSheaf)
    (ι' : BasisPresheaf.Iso (G.restrictToBasis B) F) :
    ∃! Φ : OpensPresheaf.Iso Fext G,
      ∀ (U : B) (s : Fext.obj (U : Opens X)),
        ι'.toEquiv U (Φ.toEquiv (U : Opens X) s) = ι.toEquiv U s
```

## Tag 009O, a lemma

[Tag 009O](https://stacks.math.columbia.edu/tag/009O) in the Stacks Project.

**`Stacks.OpensBasis.restrictFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/OnBasis.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/OnBasis.lean#L257).

> **Stacks 009O.** The restriction-to-basis functor
> `r : Sh(X) ⥤ Sh(B)`, sending a sheaf on `X` to its restriction to the basis
> elements.

```lean
noncomputable def restrictFunctor (hB : Opens.IsBasis B) : TopCat.Sheaf (Type u) X ⥤ SheafOnBasis B
```

**`Stacks.OpensBasis.restrictFunctor_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/OnBasis.lean, line 687](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/OnBasis.lean#L687).

> **Stacks 009O.** Let `X` be a topological space and let `B` be a basis for
> the topology on `X`. The restriction-to-basis functor `r : Sh(X) ⥤ Sh(B)` is an
> equivalence of categories.

```lean
theorem restrictFunctor_isEquivalence (hB : Opens.IsBasis B) :
    (restrictFunctor (X := X) B hB).IsEquivalence
```

## Tag 009P, a definition

[Tag 009P](https://stacks.math.columbia.edu/tag/009P) in the Stacks Project.

**`SheafOnBasis.PresheafOnBasis`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/ValuedInCategory.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/ValuedInCategory.lean#L84). The attribute's comment: “(1)”. References: EGA 0 (3.2.1), “definition”.

> A presheaf with values in `C` on the basis `B` (Stacks 009P (1)): a functor on the members of
> `B` ordered by reverse inclusion.

```lean
abbrev PresheafOnBasis (B : Basis X) (C : Type u) [Category.{v} C] :
    Type max v u
```

**`SheafOnBasis.MorphismOnBasis`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/ValuedInCategory.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/ValuedInCategory.lean#L91). The attribute's comment: “(2)”. References: EGA 0 (3.2.3), “morphism definition”; SGA 3 I (2.1.1), “morphism of Ĉ-groups”.

> A morphism of presheaves with values in `C` on the basis `B` (Stacks 009P (2)): a natural
> transformation.

```lean
abbrev MorphismOnBasis {B : Basis X} {C : Type u} [Category.{v} C]
    (F G : PresheafOnBasis B C) : Type _
```

**`SheafOnBasis.underlyingPresheafOnBasis`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/ValuedInCategory.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/ValuedInCategory.lean#L97). The attribute's comment: “(3)”. References: SGA 4 II (6.3.0), “object assignment of ε^”.

> The underlying set-valued presheaf on the basis `B` of a presheaf with values in `C`
> (Stacks 009P (3)), obtained by post-composing with a forgetful functor `F₀ : C ⥤ Type v`.

```lean
def underlyingPresheafOnBasis {B : Basis X} {C : Type u} [Category.{v} C]
    (F₀ : C ⥤ Type v) (F : PresheafOnBasis B C) : PresheafOnBasis B (Type v)
```

**`SheafOnBasis.SheafOnBasisStruct`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/ValuedInCategory.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/ValuedInCategory.lean#L130). The attribute's comment: “(4)”.

> A sheaf with values in `C` on the basis `B` (Stacks 009P (4)): a presheaf with values in `C`
> on `B` together with the sheaf condition on its underlying sets.

```lean
structure SheafOnBasisStruct (B : Basis X) (C : Type u) [Category.{v} C]
    (F₀ : C ⥤ Type v)
```

## Tag 009Q, a lemma

[Tag 009Q](https://stacks.math.columbia.edu/tag/009Q) in the Stacks Project.

**`Stacks.BasisExtension.extension_of_sheaf_on_basis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/Extension.lean, line 728](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/Extension.lean#L728). References: EGA 0 (3.2.5), “1st para: F ≅ F₁'”.

> **Extension of a sheaf on a basis (Stacks 009Q / Lemma 6.30.9).**
>
> Let `(C, F)` be a type of algebraic structure, `B` a basis for `X`, and `F` a sheaf with
> values in `C` on `B`.  Then there is a sheaf `Fᵉˣᵗ` with values in `C` on `X`, unique up to
> unique isomorphism, whose restriction to `B` is isomorphic to `F`.
>
> * *Existence*: there is a sheaf `Fext` on `X` together with an isomorphism
>   `θ : Fext|_B ≅ F.presheaf`.
> * *Uniqueness*: any sheaf `G` on `X` equipped with an isomorphism `η : G|_B ≅ F.presheaf`
>   admits a unique isomorphism `Φ : G ≅ Fext` compatible with the identifications over `B`,
>   i.e. `(restrictIso Φ) ≪≫ θ = η`.

```lean
theorem extension_of_sheaf_on_basis
    (A : AlgebraicStructureType.{u, w}) (hB : Opens.IsBasis B)
    (F : CSheafOnBasis A hB) :
    ∃ (Fext : CSheaf A X)
      (θ : restrictToBasis A B Fext.presheaf ≅ F.presheaf),
      ∀ (G : CSheaf A X) (η : restrictToBasis A B G.presheaf ≅ F.presheaf),
        ∃! Φ : G.presheaf ≅ Fext.presheaf,
          restrictIso A B Φ ≪≫ θ = η
```

## Tag 009R, a lemma

[Tag 009R](https://stacks.math.columbia.edu/tag/009R) in the Stacks Project.

**`restrictBasisEquivalenceStructures`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/Equivalence.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/Equivalence.lean#L64). References: SGA 4 III (4.1), “special case”; SGA 4 V (8.1.12), “special case”.

> Let `X` be a topological space, let `B : ι → Opens X` be a family of opens whose inclusion
> into `Opens X` is cover-dense, and let `C` be a category with enough limits. Then restriction
> along the inclusion of `B` into `Opens X` is an equivalence from sheaves on `X` with values in
> `C` to sheaves with values in `C` on the site `B` with the topology induced from
> `Opens.grothendieckTopology X`.

```lean
noncomputable def restrictBasisEquivalenceStructures
    {X : TopCat.{w}} {ι : Type w} (B : ι → Opens X)
    [(inducedFunctor B).IsCoverDense (Opens.grothendieckTopology X)]
    (C : Type v) [Category.{u} C]
    [∀ Y, Limits.HasLimitsOfShape
        (CategoryTheory.StructuredArrow Y (inducedFunctor B).op) C] :
    Sheaf (Opens.grothendieckTopology X) C ≌
      Sheaf ((inducedFunctor B).inducedTopology
              (Opens.grothendieckTopology X)) C
```

## Tag 009S, a definition

[Tag 009S](https://stacks.math.columbia.edu/tag/009S) in the Stacks Project.

**`PresheafOfModulesOnBasis`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/Module.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/Module.lean#L115). The attribute's comment: “(1)”. References: SGA 3 I (3.1), “special case”.

> A presheaf of `O`-modules on a basis `B` (Stacks 009S).
>
> Given a presheaf of rings `O` on `B`, a presheaf of `O`-modules on `B` is
> a presheaf `F` of abelian groups on `B` together with an `O(U)`-module
> structure on `F(U)` for each `U ∈ B`, compatible with restriction in the
> sense that `res(r • m) = (res r) • (res m)`.

```lean
structure PresheafOfModulesOnBasis {B : Set (Set X)}
    (O : PresheafOfRingsOnBasis.{u, w₁} B)
```

**`PresheafOfModulesOnBasis.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/Module.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/Module.lean#L154). The attribute's comment: “(2)”.

> A morphism of presheaves of `O`-modules on `B`.
>
> A morphism `φ : F → G` is a family of `O(U)`-module homomorphisms
> `φ(U) : F(U) → G(U)` commuting with restriction.

```lean
structure PresheafOfModulesOnBasis.Hom {B : Set (Set X)}
    {O : PresheafOfRingsOnBasis.{u, w₁} B}
    (F G : PresheafOfModulesOnBasis.{u, w₁, w₂} O)
```

**`SheafOfModulesOnBasis`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/Module.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/Module.lean#L205). The attribute's comment: “(3)”. References: EGA 0 (3.2.2).

> A sheaf of `O`-modules on a basis `B` (Stacks 009S, part 3).
>
> A sheaf of `O`-modules on `B` is a presheaf of `O`-modules on `B` whose
> underlying presheaf of abelian groups satisfies the sheaf condition.

```lean
structure SheafOfModulesOnBasis {B : Set (Set X)}
    (O : PresheafOfRingsOnBasis.{u, w₁} B)
```

## Tag 009T, a lemma

[Tag 009T](https://stacks.math.columbia.edu/tag/009T) in the Stacks Project.

**`BasesSheaves.exists_moduleStructure_on_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/ModuleExtension.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/ModuleExtension.lean#L87). The attribute's comment: “the canonical module structure, agreeing with the given one over elements of B”. References: EGA 0 (3.2.5), “special case”.

> **Stacks 009T (Lemma 6.30.11), the module structure on the extension.**
>
> Let `X` be a topological space, `B` a basis for its topology, `𝒪` a sheaf of rings on `X`
> (playing the role of `O^ext`, the extension of a sheaf of rings `O` on `B`), and `N` a sheaf of
> `𝒪|_B`-modules on `B` (the sheaf `F`).
>
> Then there is a sheaf of `𝒪`-modules `M` on `X` — its scalar action `𝒪 × M → M` being the
> asserted map `O^ext × F^ext → F^ext` — together with an isomorphism
> `basis_iso : M|_B ≅ N` of sheaves of `𝒪|_B`-modules, i.e. the module structure agrees with the
> given one over elements of `B`. The map is canonical: for any other sheaf of `𝒪`-modules `M'`
> with an identification `M'|_B ≅ N` there is a *unique* isomorphism `M ≅ M'` inducing it.
>
> That the underlying abelian sheaf of `M` is `F^ext` is `restrictToSheaf_iso`.

```lean
theorem exists_moduleStructure_on_extension {B : Set (Opens X)} (hB : Opens.IsBasis B)
    (𝒪 : TopCat.Sheaf RingCat X) (N : ModuleSheafOnBasis hB 𝒪) :
    ∃ (M : SheafOfModules.{u} 𝒪) (basis_iso : (restrictModuleSheaf hB 𝒪).obj M ≅ N),
      ∀ (M' : SheafOfModules.{u} 𝒪) (θ : (restrictModuleSheaf hB 𝒪).obj M' ≅ N),
        ∃! Φ : M ≅ M', (restrictModuleSheaf hB 𝒪).mapIso Φ ≪≫ θ = basis_iso
```

**`BasesSheaves.restrictToSheaf_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/ModuleExtension.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/ModuleExtension.lean#L115). The attribute's comment: “the module structure is carried by the abelian extension F^ext of F”.

> **Stacks 009T (Lemma 6.30.11), the module structure lives on `F^ext`.**
>
> An isomorphism `M|_B ≅ N` of sheaves of `𝒪|_B`-modules induces an isomorphism of the underlying
> abelian sheaves on `B`. Hence the module structure produced by
> `exists_moduleStructure_on_extension` is carried by an abelian sheaf on `X` whose restriction to
> `B` is the underlying abelian sheaf of `N` — that is, by an extension of `F` off `B`, which by
> the uniqueness in Stacks 009Q is `F^ext`.

```lean
noncomputable def restrictToSheaf_iso {B : Set (Opens X)} (hB : Opens.IsBasis B)
    (𝒪 : TopCat.Sheaf RingCat X) (M : SheafOfModules.{u} 𝒪) (N : ModuleSheafOnBasis hB 𝒪)
    (basis_iso : (restrictModuleSheaf hB 𝒪).obj M ≅ N) :
    ((basisInclusion B).sheafPushforwardContinuous AddCommGrpCat
          (basisGrothendieckTopology hB) (Opens.grothendieckTopology X)).obj
        ((SheafOfModules.toSheaf 𝒪).obj M) ≅
      (SheafOfModules.toSheaf _).obj N
```

## Tag 009U, a lemma

[Tag 009U](https://stacks.math.columbia.edu/tag/009U) in the Stacks Project.

**`Stacks.BasisRestriction.restrictModuleSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/ModuleRestriction.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/ModuleRestriction.lean#L124).

> The restriction-to-`B` functor on sheaves of `𝒪`-modules.
>
> This is defined as the pushforward along the inclusion `B ↪ Opens X`, applied to
> sheaves of modules. The ring-level pushforward sends `𝒪` to its restriction
> `𝒪|_B`, so the module-level pushforward goes from `SheafOfModules 𝒪` to
> `SheafOfModules (𝒪|_B)`.

```lean
noncomputable def restrictModuleSheaf {B : Set (Opens X)} (hB : Opens.IsBasis B)
    (𝒪 : TopCat.Sheaf RingCat X) :
    SheafOfModules.{max u w} 𝒪 ⥤ ModuleSheafOnBasis hB 𝒪
```

**`Stacks.BasisRestriction.isEquivalence_restrictModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/ModuleRestriction.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/ModuleRestriction.lean#L583).

> **Stacks 009U.** The restriction-to-`B` functor
>
>   `r : SheafOfModules 𝒪 ⥤ SheafOfModules (𝒪|_B)`,
>   `F ↦ F|_B`,
>
> is an equivalence of categories, where `𝒪|_B` is the restriction of the sheaf of
> rings `𝒪` to the basis category `B`.

```lean
theorem isEquivalence_restrictModuleSheaf {B : Set (Opens X)} (hB : Opens.IsBasis B)
    (𝒪 : TopCat.Sheaf RingCat X) :
    (restrictModuleSheaf (X := X) hB 𝒪 : SheafOfModules.{max u w} 𝒪 ⥤ _).IsEquivalence
```

## Tag 009V, a lemma

[Tag 009V](https://stacks.math.columbia.edu/tag/009V) in the Stacks Project.

**`fMap_basis_unique_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/FMapUniqueness.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/FMapUniqueness.lean#L77). References: EGA 0 (3.2.5), “second paragraph”; EGA 0 (3.5.1), “special case”.

> **Stacks 009V.** Let `B : ι → Opens Y` be a family of opens whose range is a basis of `Y`.
> Then every compatible family of basis-level morphisms `φ i : G(B i) ⟶ (f_* F)(B i)` extends to a
> unique `f`-map `ψ : G ⟶ f_* F`, i.e. a unique sheaf morphism whose component at each `B i` is
> `φ i`.

```lean
theorem fMap_basis_unique_extension
    {C : Type u} [Category.{v} C]
    {FC : C → C → Type _} {CC : C → Type v}
    [∀ (X Y : C), FunLike (FC X Y) (CC X) (CC Y)]
    [ConcreteCategory C FC]
    [HasLimits C] [HasColimits C]
    [PreservesLimits (forget C)] [PreservesFilteredColimits (forget C)]
    [(forget C).ReflectsIsomorphisms]
    {X Y : TopCat} (f : X ⟶ Y)
    (F : TopCat.Sheaf C X) (G : TopCat.Sheaf C Y)
    {ι : Type w} (B : ι → Opens Y) (hB : Opens.IsBasis (Set.range B))
    (φ : BasisCompatibleFamily f G F B) :
    ∃! ψ : FMapParameterizedC f G F, ∀ i : ι, ψ.hom.app (op (B i)) = φ.app (op i)
```

## Tag 009W, a lemma

[Tag 009W](https://stacks.math.columbia.edu/tag/009W) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.existsUnique_fMap_of_basis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/ModuleFMap.lean, line 507](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/ModuleFMap.lean#L507). References: EGA 0 (3.2.5), “special case”.

> Unique $f$-map extension from basis-compatible module maps.
>
> Let $(f, f^\sharp) : (X, \mathcal{O}_X) \to (Y, \mathcal{O}_Y)$ be a morphism of ringed
> spaces. Let $\mathcal{F}$ be a sheaf of $\mathcal{O}_X$-modules, $\mathcal{G}$ a sheaf
> of $\mathcal{O}_Y$-modules, and $\mathcal{B}$ a basis for the topology on $Y$.
> For every basis-indexed compatible system of $\mathcal{O}_Y(V)$-module homomorphisms
> $\varphi_V : \mathcal{G}(V) \to \mathcal{F}(f^{-1}V)$ for $V \in \mathcal{B}$,
> there exists a unique $f$-map $\varphi : \mathcal{G} \to \mathcal{F}$ whose
> basis-restricted family equals $\{\varphi_V\}_{V \in \mathcal{B}}$.

```lean
theorem existsUnique_fMap_of_basis {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (G : ModuleSheaf Y) (F : ModuleSheaf X)
    (B : Set (Opens Y.carrier))
    (hB : Opens.IsBasis B)
    (φ : FMapOnBasis f G F B) :
    ∃! (Φ : FMapModuleSheaf f G F), Φ.restrictToBasis B = φ
```

## Tag 009X, a lemma

[Tag 009X](https://stacks.math.columbia.edu/tag/009X) in the Stacks Project.

**`main_theorem009X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/FMapExtension.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/FMapExtension.lean#L378). References: EGA 0 (3.2.5), “second paragraph”; EGA 0 (3.5.1), “special case”.

> **Stacks tag 009X (main theorem).** Given a compatible basis family, there is
> a unique `f`-map extending it.

```lean
theorem main_theorem009X (C : Type u) [Category.{v} C]
    {FC : C → C → Type*} {CC : C → Type w} [(X Y : C) → FunLike (FC X Y) (CC X) (CC Y)]
    [ConcreteCategory.{w} C FC]
    [HasLimits C]
    [PreservesLimits (CategoryTheory.forget C)]
    [(CategoryTheory.forget C).ReflectsIsomorphisms]
    {X Y : TopCat.{w}} (f : X ⟶ Y)
    (F : TopCat.Sheaf C X) (G : TopCat.Sheaf C Y)
    (BX : Set (Opens X)) (BY : Set (Opens Y))
    (hBX : Opens.IsBasis BX) (hBY : Opens.IsBasis BY)
    (Φ : CompatibleBasisFamily C f F G BX BY) :
    ∃! (φ : FMapValPresheaf C f F G),
      ∀ (V : Opens Y) (hV : V ∈ BY) (U : Opens X) (hU : U ∈ BX)
        (hfU : U ≤ (Opens.comap f.hom) V),
        Φ.φ V hV U hU hfU = φ.app (op V) ≫ F.obj.map (homOfLE hfU).op
```

## Tag 009Y, a lemma

[Tag 009Y](https://stacks.math.columbia.edu/tag/009Y) in the Stacks Project.

**`Stacks.RingedSpace.existsUnique_fMap_of_bases`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Basis/ModuleFMapOfBasisData.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Basis/ModuleFMapOfBasisData.lean#L563). References: EGA 0 (4.4.1), “basis data suffices”.

> **Stacks 009Y.** Let `f : X ⟶ Y` be a morphism of ringed spaces, `F` a sheaf of
> `𝒪_X`-modules, `G` a sheaf of `𝒪_Y`-modules, and `BX`, `BY` bases of the topologies of `X`
> and `Y`. Then a compatible system `φ` of maps `G(V) → F(U)`, indexed by the pairs of basis
> opens with `U ≤ f⁻¹ V`, extends to a unique `f`-map `ψ : G → F`, and each `φ_V^U` is
> recovered from `ψ` as the composite `G(V) → F(f⁻¹ V) → F(U)`.

```lean
theorem existsUnique_fMap_of_bases
    {X Y : RingedSpace.{v, u}} (f : X ⟶ Y)
    (F : SheafOfModulesOnRingedSpace X) (G : SheafOfModulesOnRingedSpace Y)
    (BY : Set (Opens Y.carrier)) (BX : Set (Opens X.carrier))
    (hBY : Opens.IsBasis BY) (hBX : Opens.IsBasis BX)
    (φ : BasisCompat f F G BX BY) :
    ∃! ψ : FMapAddGroupHom f F G,
      ∀ {V : Opens Y.carrier} (hV : V ∈ BY)
        {U : Opens X.carrier} (hU : U ∈ BX) (hUV : U ≤ (Opens.map f.hom.base).obj V)
        (g : G.sections V),
        φ.basisApp hV hU hUV g = F.restrict hUV (ψ.app V g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.30, Tag 009H](https://stacks.math.columbia.edu/tag/009H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
