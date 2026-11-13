---
declaration: section
origin: cited
lean: TopCat.Sheaf.existsUnique_hom_of_localHom, TopCat.Sheaf.GlueData.glued, TopCat.Sheaf.GlueData.sectionsEquiv, TopCat.Sheaf.GlueData.sectionsEquiv_map, TopCat.Sheaf.GlueData.trans_sectionsEquiv, TopCat.Sheaf.AddGlueData.gluedAddPresheaf_forget, TopCat.Sheaf.AddGlueData.gluedAddPresheaf_isSheaf, TopCat.Sheaf.ModuleGlueData.gluedModulePresheaf_forget
statement: formalized
proof: formalized
---

# 6.33 Glueing sheaves

Section 6.33 of the Stacks Project, [Tag 00AK](https://stacks.math.columbia.edu/tag/00AK). 4 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04TN, a lemma

[Tag 04TN](https://stacks.math.columbia.edu/tag/04TN) in the Stacks Project.

**`TopCat.Sheaf.existsUnique_hom_of_localHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/MapGluing.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/MapGluing.lean#L186).

> **Stacks 04TN.** Gluing maps of sheaves. Given an open covering `U : ι → Opens X` of a
> topological space `X`, sheaves of sets `F` and `G` on `X`, and local sheaf maps `φ i` on each `U i`
> agreeing on all overlaps, there is a unique morphism of sheaves `ψ : F ⟶ G` whose restriction to
> each `U i` is `φ i`.

```lean
theorem existsUnique_hom_of_localHom {ι : Type*} {X : TopCat.{u}}
    (U : ι → Opens X) (hU : ⨆ i, U i = ⊤)
    (F G : TopCat.Sheaf (Type u) X)
    (φ : (i : ι) → LocalSheafHom F G (U i))
    (hφ : ∀ i j (V : Opens X) (hVi : V ≤ U i) (hVj : V ≤ U j),
      (φ i).app V hVi = (φ j).app V hVj) :
    ∃! ψ : F ⟶ G, ∀ i (V : Opens X) (hV : V ≤ U i),
      ψ.1.app (op V) = (φ i).app V hV
```

## Tag 00AL, a lemma

[Tag 00AL](https://stacks.math.columbia.edu/tag/00AL) in the Stacks Project.

**`TopCat.Sheaf.GlueData.glued`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/Sheaf.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/Sheaf.lean#L278). References: EGA 0 (4.1.7), “partial”.

> The sheaf of sets on `X` glued from the glueing data `D`.

```lean
def glued (D : GlueData X U) : X.Sheaf (Type u)
```

**`TopCat.Sheaf.GlueData.sectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/Sheaf.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/Sheaf.lean#L284).

> The comparison isomorphism `φ i : F|_{U i} ≅ F_i` on sections over an open `V ≤ U i`.

```lean
def sectionsEquiv (D : GlueData X U) (i : ι) {V : Opens X} (hV : V ≤ U i) :
    D.Sections V ≃ (D.sheaf i).obj V hV
```

**`TopCat.Sheaf.GlueData.sectionsEquiv_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/Sheaf.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/Sheaf.lean#L309).

> The comparison isomorphism `φ i` commutes with the restriction maps, i.e. it is an
> isomorphism of sheaves on `U i`.

```lean
theorem sectionsEquiv_map (D : GlueData X U) (i : ι) {V W : Opens X} (hV : V ≤ U i) (hWV : W ≤ V)
    (s : D.Sections V) :
    D.sectionsEquiv i (hWV.trans hV) (D.sectionsMap hWV s)
      = (D.sheaf i).map hWV (D.sectionsEquiv i hV s)
```

**`TopCat.Sheaf.GlueData.trans_sectionsEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/Sheaf.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/Sheaf.lean#L318).

> The commuting diagram `φ i j ∘ φ i = φ j` over the overlaps.

```lean
theorem trans_sectionsEquiv (D : GlueData X U) (i j : ι) {V : Opens X} (hi : V ≤ U i)
    (hj : V ≤ U j) (s : D.Sections V) :
    D.trans i j hi hj (D.sectionsEquiv i hi s) = D.sectionsEquiv j hj s
```

## Tag 00AM, a lemma

[Tag 00AM](https://stacks.math.columbia.edu/tag/00AM) in the Stacks Project.

**`TopCat.Sheaf.AddGlueData.gluedAddPresheaf_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/AlgebraicStructure.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/AlgebraicStructure.lean#L216).

> **Stacks 00AM.** The underlying presheaf of sets of the glued presheaf of abelian groups is the
> presheaf of sets glued in Stacks 00AL: the additive subgroup cut out of `∏ i, F i (W ⊓ U i)` by the
> equalizer equations has, as its underlying set, exactly the set of compatible families.

```lean
theorem gluedAddPresheaf_forget :
    D.gluedAddPresheaf ⋙ CategoryTheory.forget AddCommGrpCat = D.toGlueData.gluedPresheaf
```

**`TopCat.Sheaf.AddGlueData.gluedAddPresheaf_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/AlgebraicStructure.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/AlgebraicStructure.lean#L223). References: EGA 0 (4.1.7), “partial”.

> **Stacks 00AM.** The presheaf of abelian groups glued from a glueing data of sheaves of abelian
> groups is a sheaf of abelian groups. Since its underlying presheaf of sets is the sheaf of Stacks
> 00AL, this is the sheaf condition of Stacks 00AL read through the forgetful functor.

```lean
theorem gluedAddPresheaf_isSheaf : D.gluedAddPresheaf.IsSheaf
```

**`TopCat.Sheaf.ModuleGlueData.gluedModulePresheaf_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/AlgebraicStructure.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/AlgebraicStructure.lean#L373).

> **Stacks 00AM.** The underlying presheaf of sets of the glued presheaf of `R`-modules is the
> presheaf of sets glued in Stacks 00AL: the submodule cut out of `∏ i, F i (W ⊓ U i)` by the
> equalizer equations has, as its underlying set, exactly the set of compatible families.

```lean
theorem gluedModulePresheaf_forget :
    D.gluedModulePresheaf ⋙ CategoryTheory.forget (ModuleCat R) = D.toGlueData.gluedPresheaf
```

**`TopCat.Sheaf.ModuleGlueData.gluedModulePresheaf_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/AlgebraicStructure.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/AlgebraicStructure.lean#L380).

> **Stacks 00AM.** The presheaf of `R`-modules glued from a glueing data of sheaves of
> `R`-modules is a sheaf of `R`-modules. Since its underlying presheaf of sets is the sheaf of Stacks
> 00AL, this is the sheaf condition of Stacks 00AL read through the forgetful functor.

```lean
theorem gluedModulePresheaf_isSheaf : D.gluedModulePresheaf.IsSheaf
```

**`TopCat.Sheaf.AlgGlueData.gluedPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/OfAlgebraicStructureType.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/OfAlgebraicStructureType.lean#L197). The attribute's comment: “sheaves of algebraic structures”.

> **Stacks 00AM.** The glued presheaf with values in `S.C`: its sections over `W` are the
> equalizer `D.sections W`, restricted componentwise.

```lean
noncomputable def gluedPresheaf : X.Presheaf S.C
```

**`TopCat.Sheaf.AlgGlueData.forgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/OfAlgebraicStructureType.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/OfAlgebraicStructureType.lean#L248). The attribute's comment: “sheaves of algebraic structures”.

> **Stacks 00AM.** The underlying presheaf of sets of the glued presheaf with values in `S.C` is
> the presheaf of sets glued in Stacks 00AL.

```lean
noncomputable def forgetIso : D.gluedPresheaf ⋙ S.F ≅ D.toGlueData.gluedPresheaf
```

**`TopCat.Sheaf.AlgGlueData.gluedPresheaf_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/OfAlgebraicStructureType.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/OfAlgebraicStructureType.lean#L262). The attribute's comment: “sheaves of algebraic structures”.

> **Stacks 00AM** (sheaves of algebraic structures). The presheaf with values in `S.C` glued
> from a glueing data of sheaves with values in `S.C` is a sheaf: its underlying presheaf of sets is
> the sheaf of Stacks 00AL, and `S.F` reflects the sheaf condition.

```lean
theorem gluedPresheaf_isSheaf : D.gluedPresheaf.IsSheaf
```

**`TopCat.Sheaf.AlgGlueData.glued`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/OfAlgebraicStructureType.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/OfAlgebraicStructureType.lean#L269). The attribute's comment: “sheaves of algebraic structures”.

> The sheaf with values in `S.C` on `X` glued from a glueing data of sheaves with values in
> `S.C`.

```lean
noncomputable def glued : X.Sheaf S.C
```

**`TopCat.Sheaf.AlgGlueData.sectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/OfAlgebraicStructureType.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/OfAlgebraicStructureType.lean#L297). The attribute's comment: “sheaves of algebraic structures”.

> **Stacks 00AM** (sheaves of algebraic structures). The comparison isomorphism
> `φ i : F|_{U i} ≅ F i` on sections over an open `V ≤ U i`, as an isomorphism in `S.C`.

```lean
noncomputable def sectionsIso (i : ι) {V : Opens X} (hV : V ≤ U i) :
    D.sections V ≅ (D.sheaf i).obj V hV
```

**`TopCat.Sheaf.AlgGlueData.sectionsIso_hom_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/OfAlgebraicStructureType.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/OfAlgebraicStructureType.lean#L313). The attribute's comment: “sheaves of algebraic structures”.

> **Stacks 00AM** (sheaves of algebraic structures). The commuting diagram `φ i j ∘ φ i = φ j`
> over the overlaps.

```lean
theorem sectionsIso_hom_trans (i j : ι) {V : Opens X} (hi : V ≤ U i) (hj : V ≤ U j) :
    (D.sectionsIso i hi).hom ≫ (D.trans i j hi hj).hom = (D.sectionsIso j hj).hom
```

**`TopCat.Sheaf.OModuleGlueData.gluedPresheafOfModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/OModule.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/OModule.lean#L264). The attribute's comment: “sheaves of O-modules”.

> **The glued presheaf of `𝒪`-modules.** Its underlying presheaf of abelian groups is
> `D.toAddGlueData.gluedAddPresheaf`, and its `𝒪(W)`-module of sections over `W` is
> `gluedModule`.

```lean
noncomputable def gluedPresheafOfModules : PresheafOfModules.{u} 𝒪
```

**`TopCat.Sheaf.OModuleGlueData.isSheaf_gluedPresheafOfModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/OModule.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/OModule.lean#L275). The attribute's comment: “sheaves of O-modules”.

> **The presheaf of `𝒪`-modules glued from a glueing datum of sheaves of `𝒪`-modules is a
> sheaf.**

```lean
theorem isSheaf_gluedPresheafOfModules :
    CategoryTheory.Presheaf.IsSheaf (Opens.grothendieckTopology X)
      D.gluedPresheafOfModules.presheaf
```

**`Stacks.SheafOfModules.OModuleGlueData.gluedPresheafOfModules_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean, line 377](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean#L377). The attribute's comment: “sheaves of O-modules, the underlying presheaf of sets”.

> The underlying presheaf of sets of the glued presheaf of `O`-modules is the presheaf of sets
> glued in Stacks 00AL.

```lean
theorem gluedPresheafOfModules_forget (D : OModuleGlueData O U) :
    D.gluedPresheafOfModules.presheaf ⋙ CategoryTheory.forget AddCommGrpCat
      = D.toGlueData.gluedPresheaf
```

**`Stacks.SheafOfModules.OModuleGlueData.gluedPresheafOfModules_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean, line 385](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean#L385). The attribute's comment: “sheaves of O-modules, the sheaf condition”.

> The presheaf of `O`-modules glued from a glueing datum of sheaves of `O`-modules is a sheaf.
> Since its underlying presheaf of sets is the sheaf of Stacks 00AL, this is the sheaf condition of
> Stacks 00AL read through the forgetful functor.

```lean
theorem gluedPresheafOfModules_isSheaf (D : OModuleGlueData O U) :
    Presheaf.IsSheaf (Opens.grothendieckTopology X) D.gluedPresheafOfModules.presheaf
```

**`Stacks.SheafOfModules.OModuleGlueData.glued`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean#L393). The attribute's comment: “sheaves of O-modules, the glued sheaf”.

> The sheaf of `O`-modules on `X` glued from a glueing datum of sheaves of `O`-modules.

```lean
noncomputable def glued (D : OModuleGlueData O U) : _root_.SheafOfModules.{u} O
```

**`Stacks.SheafOfModules.OModuleGlueData.chartLinearEquiv_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean#L423). The attribute's comment: “sheaves of O-modules, the comparison isomorphisms”.

> The comparison isomorphism `φ i` commutes with the restriction maps, i.e. it is an isomorphism
> of sheaves of modules on `U i`.

```lean
theorem chartLinearEquiv_restrict (D : OModuleGlueData O U) (i : ι) {V W : Opens X}
    (hV : V ≤ U i) (h : W ≤ V) (s : D.sectionsSubmodule V) :
    D.chartLinearEquiv i (h.trans hV) (D.sectionsMap h s)
      = (D.sheaf i).map h (D.chartLinearEquiv i hV s)
```

**`Stacks.SheafOfModules.OModuleGlueData.trans_chartLinearEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean, line 431](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean#L431). The attribute's comment: “sheaves of O-modules, compatibility of the comparisons”.

> The commuting triangle `φ i j ∘ φ i = φ j` over the overlaps.

```lean
theorem trans_chartLinearEquiv (D : OModuleGlueData O U) (i j : ι) {V : Opens X} (hi : V ≤ U i)
    (hj : V ≤ U j) (s : D.sectionsSubmodule V) :
    D.trans i j hi hj (D.chartLinearEquiv i hi s) = D.chartLinearEquiv j hj s
```

**`Stacks.SheafOfModules.ModulesGlueData.glued`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean, line 554](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean#L554). The attribute's comment: “sheaves of O-modules on a scheme, the glued module”.

> The sheaf of modules on `S` glued from `D`.

```lean
noncomputable abbrev glued (D : ModulesGlueData S f) : S.Modules
```

**`Stacks.SheafOfModules.ModulesGlueData.chartIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean, line 559](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean#L559). The attribute's comment: “sheaves of O-modules on a scheme, the comparison isomorphisms”.

> The glued module restricts along each chart to the sheaf of modules it was glued from.

```lean
noncomputable def chartIso (D : ModulesGlueData S f) (i : ι) :
    D.glued.restrict (f i) ≅ D.mod i
```

**`Stacks.SheafOfModules.ModulesGlueData.trans_chartSectionsIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean, line 594](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/Basic.lean#L594). The attribute's comment: “sheaves of O-modules on a scheme, the comparisons related by the transitions”.

> **The commuting triangle `φ i j ∘ φ i = φ j` on sections over an open contained in two
> charts.** Reading a section of the glued module on the `i`-th chart and comparing it with the
> `j`-th chart gives the same thing as reading it on the `j`-th chart directly. This is
> `Stacks.SheafOfModules.OModuleGlueData.trans_chartLinearEquiv` phrased with `chartSectionsIso`,
> so that it elaborates outside this file.

```lean
theorem trans_chartSectionsIso (D : ModulesGlueData S f) (i j : ι) {V : S.Opens}
    (hi : V ≤ (f i).opensRange) (hj : V ≤ (f j).opensRange)
    (x : ToType (D.glued.val.obj (op V))) :
    D.trans i j hi hj ((D.chartSectionsIso i hi).hom x) = (D.chartSectionsIso j hj).hom x
```

## Tag 00AN, a lemma

[Tag 00AN](https://stacks.math.columbia.edu/tag/00AN) in the Stacks Project.

**`TopCat.Sheaf.sheafEquivGlueData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/Equivalence.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/Equivalence.lean#L189). The attribute's comment: “sheaves of sets”. References: EGA 0 (3.3.1), “special case”.

> **Stacks 00AN, sheaves of sets.** For an open covering `X = ⋃ i, U i`, restriction to the
> members of the covering is an equivalence between the category of sheaves of sets on `X` and the
> category of glueing data with respect to the covering.

```lean
noncomputable def sheafEquivGlueData (hU : ⨆ i, U i = ⊤) : X.Sheaf (Type u) ≌ GlueData X U
```

**`TopCat.Sheaf.sheafOfModulesEquivGlueData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/OModuleEquivalence.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/OModuleEquivalence.lean#L210). The attribute's comment: “sheaves of O-modules”.

> **Stacks 00AN, sheaves of `𝒪`-modules.** Let `𝒪` be a sheaf of rings on a topological space
> `X` and let `X = ⋃ i, U i` be an open covering. Restriction to the members of the covering is an
> equivalence between the category of sheaves of `𝒪`-modules on `X` and the category of glueing
> data of sheaves of `𝒪`-modules with respect to the covering.

```lean
noncomputable def sheafOfModulesEquivGlueData (hU : ⨆ i, U i = ⊤) :
    SheafOfModules.{u} 𝒪 ≌ OModuleGlueData 𝒪.obj U
```

**`TopCat.Sheaf.addSheafEquivGlueData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/ValuedEquivalence.lean, line 626](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/ValuedEquivalence.lean#L626). The attribute's comment: “abelian sheaves”.

> **Stacks 00AN, abelian sheaves.** For an open covering `X = ⋃ i, U i`, restriction to the
> members of the covering is an equivalence between the category of abelian sheaves on `X` and the
> category of glueing data of abelian sheaves with respect to the covering.

```lean
noncomputable def addSheafEquivGlueData (hU : ⨆ i, U i = ⊤) :
    X.Sheaf AddCommGrpCat.{u} ≌ ValuedGlueData (CategoryTheory.forget AddCommGrpCat.{u}) U
```

**`TopCat.Sheaf.algebraicStructureSheafEquivGlueData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Glueing/ValuedEquivalence.lean, line 635](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Glueing/ValuedEquivalence.lean#L635). The attribute's comment: “sheaves of algebraic structures”.

> **Stacks 00AN, sheaves of algebraic structures.** Let `(C, F)` be a type of algebraic
> structure (Stacks 007M). For an open covering `X = ⋃ i, U i`, restriction to the members of the
> covering is an equivalence between the category of sheaves of algebraic structures of type
> `(C, F)` on `X` and the category of glueing data of such sheaves with respect to the covering.

```lean
noncomputable def algebraicStructureSheafEquivGlueData (S : AlgebraicStructureType.{u, w})
    (hU : ⨆ i, U i = ⊤) : X.Sheaf S.C ≌ ValuedGlueData S.F U
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.33, Tag 00AK](https://stacks.math.columbia.edu/tag/00AK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
