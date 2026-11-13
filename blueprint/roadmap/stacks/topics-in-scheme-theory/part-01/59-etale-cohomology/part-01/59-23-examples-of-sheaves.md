---
declaration: section
origin: cited
lean: AlgebraicGeometry.BigSyntomicOver.additiveGroupSheaf, AlgebraicGeometry.BigSmoothOver.additiveGroupSheaf, AlgebraicGeometry.SmallEtale.additiveGroupSheaf, AlgebraicGeometry.SmallZariski.additiveGroupSheaf, Stacks.Sites.constantSheafZMod, Stacks.Sites.multiplicativeGroupSheaf, AlgebraicGeometry.BigFppfOver.multiplicativeGroupSheaf, AlgebraicGeometry.BigSyntomicOver.multiplicativeGroupSheaf
statement: formalized
proof: formalized
---

# 59.23 Examples of sheaves

Section 59.23 of the Stacks Project, [Tag 03YZ](https://stacks.math.columbia.edu/tag/03YZ). 4 tags here are carried by 70 declarations of the repository (all in StacksFrontier) and 13 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03P4, a definition

[Tag 03P4](https://stacks.math.columbia.edu/tag/03P4) in the Stacks Project.

**`AlgebraicGeometry.BigSyntomicOver.additiveGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean#L71). The attribute's comment: “part (1), Gₐ on the big syntomic site”.

> **Stacks 03P4, part (1), the big syntomic site.**  `Gₐ` as an abelian sheaf on
> `(Sch/S)_{syntomic}`.

```lean
noncomputable def additiveGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.BigSmoothOver.additiveGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean#L86). The attribute's comment: “part (1), Gₐ on the big smooth site”.

> **Stacks 03P4, part (1), the big smooth site.**  `Gₐ` as an abelian sheaf on
> `(Sch/S)_{smooth}`.

```lean
noncomputable def additiveGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.SmallEtale.additiveGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean#L101). The attribute's comment: “part (1), Gₐ on the small étale site”.

> **Stacks 03P4, part (1), the small étale site.**  `Gₐ` as an abelian sheaf on
> `S_{étale}`.

```lean
noncomputable def additiveGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.SmallZariski.additiveGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean#L116). The attribute's comment: “part (1), Gₐ on the small Zariski site”.

> **Stacks 03P4, part (1), the small Zariski site.**  `Gₐ` as an abelian sheaf on
> `S_{Zar}`.

```lean
noncomputable def additiveGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

**`Stacks.Sites.constantSheafZMod`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/Basic.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/Basic.lean#L60). The attribute's comment: “part (3), the constant sheaf ℤ/nℤ”.

> **Stacks 03P4, part (3).** The constant sheaf `ℤ/nℤ` on a site: the sheafification of the
> constant presheaf `U ↦ ℤ/nℤ`, formed in abelian groups.

```lean
noncomputable abbrev constantSheafZMod {C : Type u} [Category.{v} C]
    (J : GrothendieckTopology C) [HasWeakSheafify J AddCommGrpCat.{w}] (n : ℕ) :
    Sheaf J AddCommGrpCat.{w}
```

**`Stacks.Sites.multiplicativeGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean#L96). The attribute's comment: “part (2), 𝐆\_m on a site of schemes over S”.

> **Stacks 03P4, part (2).**  `𝐆_m = 𝒪_S^*` as an abelian sheaf on a site of schemes over `S`
> on which the invertible global functions are a sheaf of types.

```lean
def multiplicativeGroupSheaf (J : GrothendieckTopology C)
    (h : Presheaf.IsSheaf J (toOver.op ⋙ globalUnitsOver S)) :
    Sheaf J AddCommGrpCat.{u}
```

**`AlgebraicGeometry.BigFppfOver.multiplicativeGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean#L130). The attribute's comment: “part (2), 𝐆\_m on the big fppf site”.

> **Stacks 03P4, part (2), the big fppf site.**  `𝐆_m` as an abelian sheaf on
> `(Sch/S)_{fppf}`.

```lean
def multiplicativeGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.BigSyntomicOver.multiplicativeGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean#L149). The attribute's comment: “part (2), 𝐆\_m on the big syntomic site”.

> **Stacks 03P4, part (2), the big syntomic site.**  `𝐆_m` as an abelian sheaf on
> `(Sch/S)_{syntomic}`.

```lean
def multiplicativeGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.BigSmoothOver.multiplicativeGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean#L169). The attribute's comment: “part (2), 𝐆\_m on the big smooth site”.

> **Stacks 03P4, part (2), the big smooth site.**  `𝐆_m` as an abelian sheaf on
> `(Sch/S)_{smooth}`.

```lean
def multiplicativeGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.BigEtaleOver.multiplicativeGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean#L190). The attribute's comment: “part (2), 𝐆\_m on the big étale site”.

> **Stacks 03P4, part (2), the big étale site.**  `𝐆_m` as an abelian sheaf on
> `(Sch/S)_{étale}`.

```lean
def multiplicativeGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.BigZariskiOver.multiplicativeGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean#L210). The attribute's comment: “part (2), 𝐆\_m on the big Zariski site”.

> **Stacks 03P4, part (2), the big Zariski site.**  `𝐆_m` as an abelian sheaf on
> `(Sch/S)_{Zar}`.

```lean
def multiplicativeGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.SmallEtale.multiplicativeGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean#L234). The attribute's comment: “part (2), 𝐆\_m on the small étale site”.

> **Stacks 03P4, part (2), the small étale site.**  `𝐆_m` as an abelian sheaf on
> `S_{étale}`.

```lean
def multiplicativeGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.SmallZariski.multiplicativeGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/MultiplicativeGroupSheaf.lean#L255). The attribute's comment: “part (2), 𝐆\_m on the small Zariski site”.

> **Stacks 03P4, part (2), the small Zariski site.**  `𝐆_m` as an abelian sheaf on
> `S_{Zar}`.

```lean
def multiplicativeGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

Declarations registered for the tag:

- [`Stacks.Sites.additiveGroupSheaf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L152), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean#L52) (StacksFrontier): “part (1), Gₐ on a site of schemes over S”.
- [`AlgebraicGeometry.BigFppfOver.additiveGroupSheaf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L207), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean#L53) (StacksFrontier): “part (1), Gₐ on the big fppf site”.
- [`AlgebraicGeometry.BigEtaleOver.additiveGroupSheaf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L240), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean#L55) (StacksFrontier): “part (1), Gₐ on the big étale site”.
- [`AlgebraicGeometry.BigZariskiOver.additiveGroupSheaf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L274), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafSites.lean#L57) (StacksFrontier): “part (1), Gₐ on the big Zariski site”.
- [`CategoryTheory.constantSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.constantSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/Basic.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/Basic.lean#L40) (StacksFrontier): “constant\_sheaf”. References: EGA 0 (15.2.1), “partial”; EGA 0 (3.6.1); SGA 4 IV (11.1.5); SGA 4 IV (2.7.5); SGA 4 IV (4.3.4); SGA 4 IX (2.0); SGA 4 VII (2.1), “partial”; SGA 4½ Arcata (2.2.1); SGA 4½ Arcata (4.3.2).

## Tag 03P5, a remark

[Tag 03P5](https://stacks.math.columbia.edu/tag/03P5) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleConstantSheafIsoLocallyConstantMapsAb`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/ConstantSheafSections.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/ConstantSheafSections.lean#L231). The attribute's comment: “Scheme.smallEtaleTopology with AddCommGrpCat coefficients”. References: SGA 4 XII (5.6), “special case”.

> The constant sheaf of abelian groups with value `A` on the small étale site of a scheme `X`
> has as its sections over an étale `X`-scheme `V` the group of locally constant `A`-valued maps
> on `V`.

```lean
public def smallEtaleConstantSheafIsoLocallyConstantMapsAb (X : Scheme.{u})
    (A : Type (max (u + 1) v)) [AddCommGroup A] :
    ((constantSheaf (Scheme.smallEtaleTopology X)
        AddCommGrpCat.{max (u + 1) v}).obj (AddCommGrpCat.of A)).obj ≅
      smallEtaleLocallyConstantMapsAb.{u, max (u + 1) v} X A
```

**`AlgebraicGeometry.smallEtaleConstantSheafIsoLocallyConstantMapsAb_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/ConstantSheafSections.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/ConstantSheafSections.lean#L263). The attribute's comment: “constant sections on Scheme.smallEtaleTopology, AddCommGrpCat coefficients”.

> The identification of the constant abelian sheaf on the small étale site with the locally
> constant maps sends the sheafification-unit image of `a : A` to the constant map with value
> `a`.

```lean
public theorem smallEtaleConstantSheafIsoLocallyConstantMapsAb_unit (X : Scheme.{u})
    (A : Type (max (u + 1) v)) [AddCommGroup A] (T : (X.Etale)ᵒᵖ) (a : A) :
    ((smallEtaleConstantSheafIsoLocallyConstantMapsAb.{u, v} X A).hom.app T)
      ((toSheafify (Scheme.smallEtaleTopology X)
        ((Functor.const (X.Etale)ᵒᵖ).obj (AddCommGrpCat.of A))).app T a) =
      LocallyConstant.const T.unop.left a
```

**`AlgebraicGeometry.constantGroupSheafRepresentedByConstantGroupScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ConstantGroupSheaf.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ConstantGroupSheaf.lean#L233). The attribute's comment: “group-valued representation on the big over-site”.

> The constant sheaf of groups on the schemes over `S` is represented by the constant group
> scheme `G_S`, compatibly with the constant-presheaf unit, for every topology between the
> Zariski and the fpqc topology.

```lean
public def constantGroupSheafRepresentedByConstantGroupScheme (S : Scheme.{u})
    (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] (J : GrothendieckTopology (Over S))
    (hZ : Scheme.zariskiTopology.over S ≤ J) (hF : J ≤ Scheme.fpqcTopology.over S) :
    GroupSheafRepresentation S (𝟭 (Over S)) J G
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ConstantSheaf.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ConstantSheaf.lean#L363).

> The sheafification of the constant presheaf on the schemes over `S` has the locally
> constant `G`-valued maps as its sections, for every topology between the Zariski and the fpqc
> topology.

```lean
public def constantSheafIsoLocallyConstantMaps (S : Scheme.{u}) (G : Type (max (u + 1) v))
    [Small.{u} G] [Group G] (J : GrothendieckTopology (Over S))
    (hZ : Scheme.zariskiTopology.over S ≤ J) (hF : J ≤ Scheme.fpqcTopology.over S) :
    ((constantSheaf J (Type (max (u + 1) v))).obj G).obj ≅
      (locallyConstantMapsOver G S ⋙ forget GrpCat)
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ConstantSheaf.lean, line 374](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ConstantSheaf.lean#L374). The attribute's comment: “compatibility with constant sections”.

> The identification of the constant sheaf with locally constant maps sends the
> sheafification-unit image of `g` to the constant map with value `g`.

```lean
public theorem constantSheafIsoLocallyConstantMaps_unit (S : Scheme.{u})
    (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] (J : GrothendieckTopology (Over S))
    (hZ : Scheme.zariskiTopology.over S ≤ J) (hF : J ≤ Scheme.fpqcTopology.over S)
    (T : (Over S)ᵒᵖ) (g : G) :
    ((constantSheafIsoLocallyConstantMaps S G J hZ hF).hom.app T)
      ((toSheafify J ((Functor.const (Over S)ᵒᵖ).obj G)).app T g) =
      LocallyConstant.const T.unop.left g
```

**`AlgebraicGeometry.constantSheafComparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ConstantSheaf.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ConstantSheaf.lean#L391). The attribute's comment: “canonical Zariski-to-tau sheafification comparison”.

> On the schemes over `S`, the canonical comparison from the Zariski sheafification of the
> constant presheaf to its `J`-sheafification is invertible.

```lean
public theorem constantSheafComparison_isIso (S : Scheme.{u}) (G : Type (max (u + 1) v))
    [Small.{u} G] [Group G] (J : GrothendieckTopology (Over S))
    (hZ : Scheme.zariskiTopology.over S ≤ J) (hF : J ≤ Scheme.fpqcTopology.over S)
    [HasWeakSheafify (Scheme.zariskiTopology.over S) (Type (max (u + 1) v))]
    [HasWeakSheafify J (Type (max (u + 1) v))] :
    let P : (Over S)ᵒᵖ ⥤ Type (max (u + 1) v) := (Functor.const (Over S)ᵒᵖ).obj G
    IsIso (zariskiSheafToTauSheaf (Scheme.zariskiTopology.over S) J hZ P)
```

**`AlgebraicGeometry.constantSheafIsoConstantGroupSchemePoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ConstantSheaf.lean, line 432](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ConstantSheaf.lean#L432). The attribute's comment: “representation of the constant sheaf by the group scheme”.

> The constant sheaf of sets is naturally the underlying functor of points of the constant
> group scheme. The isomorphism is the composite through the group-valued functor of locally
> constant maps.

```lean
public def constantSheafIsoConstantGroupSchemePoints (S : Scheme.{u})
    (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] (J : GrothendieckTopology (Over S))
    (hZ : Scheme.zariskiTopology.over S ≤ J) (hF : J ≤ Scheme.fpqcTopology.over S) :
    ((constantSheaf J (Type (max (u + 1) v))).obj G).obj ≅
      ((yonedaGrp.obj (constantGroupScheme G S) ⋙
        GrpCat.uliftFunctor.{max (u + 1) v}) ⋙ forget GrpCat)
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_bigEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean#L386). The attribute's comment: “big étale site”.

> Constant sheaves on the chosen big étale site have locally constant sections.

```lean
public def constantSheafIsoLocallyConstantMaps_bigEtale (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ((constantSheaf (BigEtaleOver.topology B S hS) (Type (max (u + 1) v))).obj G).obj ≅
    ((BigEtaleOver.toScheme B S hS).op ⋙
      locallyConstantMaps.{u, max (u + 1) v} G ⋙ forget GrpCat)
```

**`AlgebraicGeometry.zariskiConstantSheafIsoLocallyConstantMaps_bigEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean#L399). The attribute's comment: “Zariski sheafification on the big étale site”.

> The Zariski sheafification on a chosen big étale site has locally constant sections.

```lean
public def zariskiConstantSheafIsoLocallyConstantMaps_bigEtale (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ((constantSheaf
      ((BigEtaleOver.toScheme B S hS).restrictedTopology Scheme.zariskiTopology)
      (Type (max (u + 1) v))).obj G).obj ≅
    ((BigEtaleOver.toScheme B S hS).op ⋙
      locallyConstantMaps.{u, max (u + 1) v} G ⋙ forget GrpCat)
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_smallEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean#L416). The attribute's comment: “small étale site”.

> Constant sheaves on the chosen small étale site have locally constant sections.

```lean
public def constantSheafIsoLocallyConstantMaps_smallEtale (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ((constantSheaf (SmallEtale.topology B S hS) (Type (max (u + 1) v))).obj G).obj ≅
    ((SmallEtale.toScheme B S hS).op ⋙
      locallyConstantMaps.{u, max (u + 1) v} G ⋙ forget GrpCat)
```

**`AlgebraicGeometry.zariskiConstantSheafIsoLocallyConstantMaps_smallEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean, line 429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean#L429). The attribute's comment: “Zariski sheafification on the small étale site”.

> The Zariski sheafification on a chosen small étale site has locally constant sections.

```lean
public def zariskiConstantSheafIsoLocallyConstantMaps_smallEtale (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ((constantSheaf
      ((SmallEtale.toScheme B S hS).restrictedTopology Scheme.zariskiTopology)
      (Type (max (u + 1) v))).obj G).obj ≅
    ((SmallEtale.toScheme B S hS).op ⋙
      locallyConstantMaps.{u, max (u + 1) v} G ⋙ forget GrpCat)
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_bigEtale_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean#L448). The attribute's comment: “tau unit on the big etale site”.

> The specified-topology identification on the big etale site preserves constant sections.

```lean
public theorem constantSheafIsoLocallyConstantMaps_bigEtale_unit (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ConstantSheafIso.UnitCompatible (BigEtaleOver.toScheme B S hS)
      (BigEtaleOver.topology B S hS) G
      (constantSheafIsoLocallyConstantMaps_bigEtale B S hS G)
```

**`AlgebraicGeometry.zariskiConstantSheafIsoLocallyConstantMaps_bigEtale_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean#L461). The attribute's comment: “Zariski unit on the big etale site”.

> The Zariski-topology identification on the big etale site preserves constant sections.

```lean
public theorem zariskiConstantSheafIsoLocallyConstantMaps_bigEtale_unit
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ConstantSheafIso.UnitCompatible (BigEtaleOver.toScheme B S hS)
      ((BigEtaleOver.toScheme B S hS).restrictedTopology Scheme.zariskiTopology) G
      (zariskiConstantSheafIsoLocallyConstantMaps_bigEtale B S hS G)
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_smallEtale_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean#L478). The attribute's comment: “tau unit on the small etale site”.

> The specified-topology identification on the small etale site preserves constant
> sections.

```lean
public theorem constantSheafIsoLocallyConstantMaps_smallEtale_unit (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ConstantSheafIso.UnitCompatible (SmallEtale.toScheme B S hS)
      (SmallEtale.topology B S hS) G
      (constantSheafIsoLocallyConstantMaps_smallEtale B S hS G)
```

**`AlgebraicGeometry.zariskiConstantSheafIsoLocallyConstantMaps_smallEtale_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean, line 492](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean#L492). The attribute's comment: “Zariski unit on the small etale site”.

> The Zariski-topology identification on the small etale site preserves constant
> sections.

```lean
public theorem zariskiConstantSheafIsoLocallyConstantMaps_smallEtale_unit
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ConstantSheafIso.UnitCompatible (SmallEtale.toScheme B S hS)
      ((SmallEtale.toScheme B S hS).restrictedTopology Scheme.zariskiTopology) G
      (zariskiConstantSheafIsoLocallyConstantMaps_smallEtale B S hS G)
```

**`AlgebraicGeometry.constantGroupSheafRepresentedByConstantGroupScheme_bigEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean, line 510](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean#L510). The attribute's comment: “group-valued representation on the big étale site”.

> Representation of the constant group sheaf on the chosen big étale site.

```lean
public def constantGroupSheafRepresentedByConstantGroupScheme_bigEtale (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    GroupSheafRepresentation S (Over.post (X := B.obj S hS) B.inclusion)
      (BigEtaleOver.topology B S hS) G
```

**`AlgebraicGeometry.constantGroupSheafRepresentedByConstantGroupScheme_smallEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean, line 529](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean#L529). The attribute's comment: “group-valued representation on the small étale site”.

> Representation of the constant group sheaf on the chosen small étale site.

```lean
public def constantGroupSheafRepresentedByConstantGroupScheme_smallEtale
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    GroupSheafRepresentation S
      (SmallEtale.inclusion B S hS ⋙ Over.post (X := B.obj S hS) B.inclusion)
      (SmallEtale.topology B S hS) G
```

**`AlgebraicGeometry.zariskiGroupSheafRepresented_bigEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean, line 550](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean#L550). The attribute's comment: “Zariski group sheaf on the big étale site”.

> The Zariski constant group sheaf on the chosen big étale site is represented by `G_S`.

```lean
public def zariskiGroupSheafRepresented_bigEtale (B : BigEtaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    GroupSheafRepresentation S (Over.post (X := B.obj S hS) B.inclusion)
      ((BigEtaleOver.toScheme B S hS).restrictedTopology Scheme.zariskiTopology) G
```

**`AlgebraicGeometry.zariskiGroupSheafRepresented_smallEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean, line 570](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/ConstantSheaf.lean#L570). The attribute's comment: “Zariski group sheaf on the small étale site”.

> The Zariski constant group sheaf on the chosen small étale site is represented by `G_S`.

```lean
public def zariskiGroupSheafRepresented_smallEtale (B : BigEtaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    GroupSheafRepresentation S
      (SmallEtale.inclusion B S hS ⋙ Over.post (X := B.obj S hS) B.inclusion)
      ((SmallEtale.toScheme B S hS).restrictedTopology Scheme.zariskiTopology) G
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_bigFppf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ConstantSheaf.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ConstantSheaf.lean#L148). The attribute's comment: “big fppf site”.

> Constant sheaves on the chosen big fppf site have locally constant sections.

```lean
public def constantSheafIsoLocallyConstantMaps_bigFppf (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ((constantSheaf (BigFppfOver.topology B S hS) (Type (max (u + 1) v))).obj G).obj ≅
    ((BigFppfOver.toScheme B S hS).op ⋙
      locallyConstantMaps.{u, max (u + 1) v} G ⋙ forget GrpCat)
```

**`AlgebraicGeometry.zariskiConstantSheafIsoLocallyConstantMaps_bigFppf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ConstantSheaf.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ConstantSheaf.lean#L161). The attribute's comment: “Zariski sheafification on the big fppf site”.

> The Zariski sheafification on a chosen big fppf site has locally constant sections.

```lean
public def zariskiConstantSheafIsoLocallyConstantMaps_bigFppf (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ((constantSheaf
      ((BigFppfOver.toScheme B S hS).restrictedTopology Scheme.zariskiTopology)
      (Type (max (u + 1) v))).obj G).obj ≅
    ((BigFppfOver.toScheme B S hS).op ⋙
      locallyConstantMaps.{u, max (u + 1) v} G ⋙ forget GrpCat)
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_bigFppf_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ConstantSheaf.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ConstantSheaf.lean#L178). The attribute's comment: “tau unit on the big fppf site”.

> The specified-topology identification on the big fppf site preserves constant sections.

```lean
public theorem constantSheafIsoLocallyConstantMaps_bigFppf_unit (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ConstantSheafIso.UnitCompatible (BigFppfOver.toScheme B S hS)
      (BigFppfOver.topology B S hS) G
      (constantSheafIsoLocallyConstantMaps_bigFppf B S hS G)
```

**`AlgebraicGeometry.zariskiConstantSheafIsoLocallyConstantMaps_bigFppf_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ConstantSheaf.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ConstantSheaf.lean#L191). The attribute's comment: “Zariski unit on the big fppf site”.

> The Zariski-topology identification on the big fppf site preserves constant sections.

```lean
public theorem zariskiConstantSheafIsoLocallyConstantMaps_bigFppf_unit (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ConstantSheafIso.UnitCompatible (BigFppfOver.toScheme B S hS)
      ((BigFppfOver.toScheme B S hS).restrictedTopology Scheme.zariskiTopology) G
      (zariskiConstantSheafIsoLocallyConstantMaps_bigFppf B S hS G)
```

**`AlgebraicGeometry.constantGroupSheafRepresentedByConstantGroupScheme_bigFppf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ConstantSheaf.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ConstantSheaf.lean#L207). The attribute's comment: “group-valued representation on the big fppf site”.

> On the chosen big fppf site, the constant group sheaf itself is the restriction of the
> group-valued functor of points of the constant group scheme.

```lean
public def constantGroupSheafRepresentedByConstantGroupScheme_bigFppf (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    GroupSheafRepresentation S (Over.post (X := B.obj hS) B.inclusion)
      (BigFppfOver.topology B S hS) G
```

**`AlgebraicGeometry.zariskiGroupSheafRepresented_bigFppf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ConstantSheaf.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/ConstantSheaf.lean#L224). The attribute's comment: “Zariski group sheaf on the big fppf site”.

> The Zariski constant group sheaf on the chosen big fppf site is represented by `G_S`.

```lean
public def zariskiGroupSheafRepresented_bigFppf (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    GroupSheafRepresentation S (Over.post (X := B.obj hS) B.inclusion)
      ((BigFppfOver.toScheme B S hS).restrictedTopology Scheme.zariskiTopology) G
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_bigSmooth`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/ConstantSheaf.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/ConstantSheaf.lean#L143). The attribute's comment: “big smooth site”.

> Constant sheaves on the chosen big smooth site have locally constant sections.

```lean
public def constantSheafIsoLocallyConstantMaps_bigSmooth (B : BigSmoothSite.{u})
    (S : Scheme.{u}) (hS : S.size < B.cutoff) (G : Type (max (u + 1) v)) [Small.{u} G]
    [Group G] :
    ((constantSheaf (BigSmoothOver.topology B S hS) (Type (max (u + 1) v))).obj G).obj ≅
    ((BigSmoothOver.toScheme B S hS).op ⋙
      locallyConstantMaps.{u, max (u + 1) v} G ⋙ forget GrpCat)
```

**`AlgebraicGeometry.zariskiConstantSheafIsoLocallyConstantMaps_bigSmooth`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/ConstantSheaf.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/ConstantSheaf.lean#L157). The attribute's comment: “Zariski sheafification on the big smooth site”.

> The Zariski sheafification on a chosen big smooth site has locally constant sections.

```lean
public def zariskiConstantSheafIsoLocallyConstantMaps_bigSmooth (B : BigSmoothSite.{u})
    (S : Scheme.{u}) (hS : S.size < B.cutoff) (G : Type (max (u + 1) v)) [Small.{u} G]
    [Group G] :
    ((constantSheaf
      ((BigSmoothOver.toScheme B S hS).restrictedTopology Scheme.zariskiTopology)
      (Type (max (u + 1) v))).obj G).obj ≅
    ((BigSmoothOver.toScheme B S hS).op ⋙
      locallyConstantMaps.{u, max (u + 1) v} G ⋙ forget GrpCat)
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_bigSmooth_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/ConstantSheaf.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/ConstantSheaf.lean#L176). The attribute's comment: “tau unit on the big smooth site”.

> The specified-topology identification on the big smooth site preserves constant
> sections.

```lean
public theorem constantSheafIsoLocallyConstantMaps_bigSmooth_unit (B : BigSmoothSite.{u})
    (S : Scheme.{u}) (hS : S.size < B.cutoff) (G : Type (max (u + 1) v)) [Small.{u} G]
    [Group G] :
    ConstantSheafIso.UnitCompatible (BigSmoothOver.toScheme B S hS)
      (BigSmoothOver.topology B S hS) G
      (constantSheafIsoLocallyConstantMaps_bigSmooth B S hS G)
```

**`AlgebraicGeometry.zariskiConstantSheafIsoLocallyConstantMaps_bigSmooth_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/ConstantSheaf.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/ConstantSheaf.lean#L190). The attribute's comment: “Zariski unit on the big smooth site”.

> The Zariski-topology identification on the big smooth site preserves constant sections.

```lean
public theorem zariskiConstantSheafIsoLocallyConstantMaps_bigSmooth_unit
    (B : BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff)
    (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ConstantSheafIso.UnitCompatible (BigSmoothOver.toScheme B S hS)
      ((BigSmoothOver.toScheme B S hS).restrictedTopology Scheme.zariskiTopology) G
      (zariskiConstantSheafIsoLocallyConstantMaps_bigSmooth B S hS G)
```

**`AlgebraicGeometry.constantGroupSheafRepresentedByConstantGroupScheme_bigSmooth`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/ConstantSheaf.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/ConstantSheaf.lean#L206). The attribute's comment: “group-valued representation on the big smooth site”.

> Representation of the constant group sheaf on the chosen big smooth site.

```lean
public def constantGroupSheafRepresentedByConstantGroupScheme_bigSmooth
    (B : BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff)
    (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    GroupSheafRepresentation S
      (Over.post (X := (⟨S, hS⟩ : B.category)) (ObjectProperty.ι _))
      (BigSmoothOver.topology B S hS) G
```

**`AlgebraicGeometry.zariskiGroupSheafRepresented_bigSmooth`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/ConstantSheaf.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/ConstantSheaf.lean#L225). The attribute's comment: “Zariski group sheaf on the big smooth site”.

> The Zariski constant group sheaf on the chosen big smooth site is represented by `G_S`.

```lean
public def zariskiGroupSheafRepresented_bigSmooth (B : BigSmoothSite.{u}) (S : Scheme.{u})
    (hS : S.size < B.cutoff) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    GroupSheafRepresentation S
      (Over.post (X := (⟨S, hS⟩ : B.category)) (ObjectProperty.ι _))
      ((BigSmoothOver.toScheme B S hS).restrictedTopology Scheme.zariskiTopology) G
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_bigSyntomic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean#L170). The attribute's comment: “big syntomic site”.

> Constant sheaves on the chosen big syntomic site have locally constant sections.

```lean
public def constantSheafIsoLocallyConstantMaps_bigSyntomic (B : BigSyntomicSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ((constantSheaf (BigSyntomicOver.topology B S hS) (Type (max (u + 1) v))).obj G).obj ≅
    ((BigSyntomicOver.toScheme B S hS).op ⋙
      locallyConstantMaps.{u, max (u + 1) v} G ⋙ forget GrpCat)
```

**`AlgebraicGeometry.zariskiConstantSheafIsoLocallyConstantMaps_bigSyntomic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean#L183). The attribute's comment: “Zariski sheafification on the big syntomic site”.

> The Zariski sheafification on a chosen big syntomic site has locally constant sections.

```lean
public def zariskiConstantSheafIsoLocallyConstantMaps_bigSyntomic (B : BigSyntomicSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ((constantSheaf
      ((BigSyntomicOver.toScheme B S hS).restrictedTopology Scheme.zariskiTopology)
      (Type (max (u + 1) v))).obj G).obj ≅
    ((BigSyntomicOver.toScheme B S hS).op ⋙
      locallyConstantMaps.{u, max (u + 1) v} G ⋙ forget GrpCat)
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_bigSyntomic_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean#L201). The attribute's comment: “tau unit on the big syntomic site”.

> The specified-topology identification on the big syntomic site preserves constant
> sections.

```lean
public theorem constantSheafIsoLocallyConstantMaps_bigSyntomic_unit (B : BigSyntomicSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ConstantSheafIso.UnitCompatible (BigSyntomicOver.toScheme B S hS)
      (BigSyntomicOver.topology B S hS) G
      (constantSheafIsoLocallyConstantMaps_bigSyntomic B S hS G)
```

**`AlgebraicGeometry.zariskiConstantSheafIsoLocallyConstantMaps_bigSyntomic_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean#L215). The attribute's comment: “Zariski unit on the big syntomic site”.

> The Zariski-topology identification on the big syntomic site preserves constant
> sections.

```lean
public theorem zariskiConstantSheafIsoLocallyConstantMaps_bigSyntomic_unit
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ConstantSheafIso.UnitCompatible (BigSyntomicOver.toScheme B S hS)
      ((BigSyntomicOver.toScheme B S hS).restrictedTopology Scheme.zariskiTopology) G
      (zariskiConstantSheafIsoLocallyConstantMaps_bigSyntomic B S hS G)
```

**`AlgebraicGeometry.constantGroupSheafRepresentedByConstantGroupScheme_bigSyntomic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean#L231). The attribute's comment: “group-valued representation on the big syntomic site”.

> Representation of the constant group sheaf on the chosen big syntomic site.

```lean
public def constantGroupSheafRepresentedByConstantGroupScheme_bigSyntomic
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    GroupSheafRepresentation S (Over.post (X := B.obj S hS) B.inclusion)
      (BigSyntomicOver.topology B S hS) G
```

**`AlgebraicGeometry.zariskiGroupSheafRepresented_bigSyntomic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean#L251). The attribute's comment: “Zariski group sheaf on the big syntomic site”.

> The Zariski constant group sheaf on the chosen big syntomic site is represented by
> `G_S`.

```lean
public def zariskiGroupSheafRepresented_bigSyntomic (B : BigSyntomicSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    GroupSheafRepresentation S (Over.post (X := B.obj S hS) B.inclusion)
      ((BigSyntomicOver.toScheme B S hS).restrictedTopology Scheme.zariskiTopology) G
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_bigZariski`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Zariski/ConstantSheaf.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Zariski/ConstantSheaf.lean#L240). The attribute's comment: “big Zariski site”.

> Constant sheaves on the chosen big Zariski site have locally constant sections.

```lean
public def constantSheafIsoLocallyConstantMaps_bigZariski (B : BigZariskiSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ((constantSheaf (BigZariskiOver.topology B S hS)
      (Type (max (u + 1) v))).obj G).obj ≅
    ((BigZariskiOver.toScheme B S hS).op ⋙
      locallyConstantMaps.{u, max (u + 1) v} G ⋙ forget GrpCat)
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_smallZariski`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Zariski/ConstantSheaf.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Zariski/ConstantSheaf.lean#L252). The attribute's comment: “small Zariski site”.

> Constant sheaves on the chosen small Zariski site have locally constant sections.

```lean
public def constantSheafIsoLocallyConstantMaps_smallZariski (B : BigZariskiSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ((constantSheaf (SmallZariski.topology B S hS) (Type (max (u + 1) v))).obj G).obj ≅
    ((SmallZariski.toScheme B S hS).op ⋙
      locallyConstantMaps.{u, max (u + 1) v} G ⋙ forget GrpCat)
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_bigZariski_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Zariski/ConstantSheaf.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Zariski/ConstantSheaf.lean#L265). The attribute's comment: “unit on the big Zariski site”.

> The big Zariski identification preserves constant sections.

```lean
public theorem constantSheafIsoLocallyConstantMaps_bigZariski_unit (B : BigZariskiSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ConstantSheafIso.UnitCompatible (BigZariskiOver.toScheme B S hS)
      (BigZariskiOver.topology B S hS) G
      (constantSheafIsoLocallyConstantMaps_bigZariski B S hS G)
```

**`AlgebraicGeometry.constantSheafIsoLocallyConstantMaps_smallZariski_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Zariski/ConstantSheaf.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Zariski/ConstantSheaf.lean#L276). The attribute's comment: “unit on the small Zariski site”.

> The small Zariski identification preserves constant sections.

```lean
public theorem constantSheafIsoLocallyConstantMaps_smallZariski_unit (B : BigZariskiSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    ConstantSheafIso.UnitCompatible (SmallZariski.toScheme B S hS)
      (SmallZariski.topology B S hS) G
      (constantSheafIsoLocallyConstantMaps_smallZariski B S hS G)
```

**`AlgebraicGeometry.constantGroupSheafRepresentedByConstantGroupScheme_bigZariski`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Zariski/ConstantSheaf.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Zariski/ConstantSheaf.lean#L289). The attribute's comment: “group-valued representation on the big Zariski site”.

> Representation of the constant group sheaf on the chosen big Zariski site.

```lean
public def constantGroupSheafRepresentedByConstantGroupScheme_bigZariski
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    GroupSheafRepresentation S (Over.post (X := (⟨S, hS⟩ : B.Schemes)) B.inclusion)
      (BigZariskiOver.topology B S hS) G
```

**`AlgebraicGeometry.constantGroupSheafRepresentedByConstantGroupScheme_smallZariski`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Zariski/ConstantSheaf.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Zariski/ConstantSheaf.lean#L308). The attribute's comment: “group-valued representation on the small Zariski site”.

> Representation of the constant group sheaf on the chosen small Zariski site.

```lean
public def constantGroupSheafRepresentedByConstantGroupScheme_smallZariski
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : Type (max (u + 1) v)) [Small.{u} G] [Group G] :
    GroupSheafRepresentation S
      (SmallZariski.inclusion B S hS ⋙
        Over.post (X := (⟨S, hS⟩ : B.Schemes)) B.inclusion)
      (SmallZariski.topology B S hS) G
```

Declarations registered for the tag:

- [`AlgebraicGeometry.constantGroupSchemePointsIsoLocallyConstantMaps`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean#L819), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/ConstantGroupSheaf.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ConstantGroupSheaf.lean#L51) (StacksFrontier): “representation by the constant group scheme”.

## Tag 04HS, a definition

[Tag 04HS](https://stacks.math.columbia.edu/tag/04HS) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.BigEtaleOver.structureSheaf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigEtaleStructureSheaf.lean#L60), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BigEtaleStructureSheaf.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigEtaleStructureSheaf.lean#L72) (StacksFrontier): “big étale structure sheaf”. References: SGA 4½ Arcata (2.2), “structure sheaf O\_S”.
- [`AlgebraicGeometry.BigFppfOver.structureSheaf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigFppfStructureSheaf.lean#L120), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BigFppfStructureSheaf.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigFppfStructureSheaf.lean#L134) (StacksFrontier): “big fppf structure sheaf”.
- [`AlgebraicGeometry.BigSmoothOver.structureSheaf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSmoothStructureSheaf.lean#L60), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BigSmoothStructureSheaf.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSmoothStructureSheaf.lean#L74) (StacksFrontier): “big smooth structure sheaf”.
- [`AlgebraicGeometry.BigSyntomicOver.structureSheaf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSyntomicStructureSheaf.lean#L62), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BigSyntomicStructureSheaf.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSyntomicStructureSheaf.lean#L74) (StacksFrontier): “big syntomic structure sheaf”.
- [`AlgebraicGeometry.BigZariskiOver.structureSheaf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigZariskiStructureSheaf.lean#L66), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BigZariskiStructureSheaf.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigZariskiStructureSheaf.lean#L81) (StacksFrontier): “big Zariski structure sheaf”.
- [`AlgebraicGeometry.SmallEtale.structureSheaf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SmallEtaleStructureSheaf.lean#L106), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/SmallEtaleStructureSheaf.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SmallEtaleStructureSheaf.lean#L120) (StacksFrontier): “small étale structure sheaf”.
- [`AlgebraicGeometry.SmallZariski.structureSheaf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiStructureSheaf.lean#L85), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/SmallZariskiStructureSheaf.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SmallZariskiStructureSheaf.lean#L34) (StacksFrontier): “small Zariski structure sheaf”.

## Tag 03P6, a remark

[Tag 03P6](https://stacks.math.columbia.edu/tag/03P6) in the Stacks Project.

**`Stacks.Sites.additiveGroupPresheafIsoPoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L132). The attribute's comment: “Gₐ is the functor of points of the additive group scheme”. References: SGA 3 I (4.3.1), “more general”.

> **Stacks 03P6, the identification of `Gₐ`.**  The additive group sheaf of a site of
> schemes over `S` is the functor of points of the additive group scheme `Gₐ,S` of
> [Stacks, Tag 022V], restricted to the site along `toOver`.
>
> The comparison is stated after the forgetful retyping of `AddCommGrpCat` into `GrpCat`, which
> is the shape in which `AlgebraicGeometry.additiveGroupBaseChangePointsIsoGlobalSections`
> records that the group law on sections is addition of functions.  It is a whiskering of that
> natural isomorphism and assumes nothing about the topology.

```lean
noncomputable def additiveGroupPresheafIsoPoints :
    toOver.op ⋙ yonedaGrpObj (Scheme.asOver (additiveGroupBaseChange S) S) ≅
      additiveGroupPresheaf S toOver ⋙ forget₂ AddCommGrpCat AddGrpCat ⋙ AddGrpCat.toGrp
```

**`Stacks.Sites.additiveGroupSheaf_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L163). The attribute's comment: “Gₐ is the structure sheaf of Stacks 04HS read additively”.

> **Stacks 03P6, the notation `H^p_τ(X, 𝒪_X)`.**  The underlying presheaf of `Gₐ` is the
> structure presheaf of the site read additively.  So the cohomology of `Gₐ` on a site of
> schemes over `S` and the cohomology of the structure sheaf `𝒪_S` of [Stacks, Tag 04HS] on that
> site are cohomology of one and the same abelian sheaf, which is what lets the two notations of
> the remark be used interchangeably.

```lean
theorem additiveGroupSheaf_obj (J : GrothendieckTopology C)
    (h : Presheaf.IsSheaf J (toOver.op ⋙ globalSectionsOver S)) :
    (additiveGroupSheaf S toOver J h).obj =
      structurePresheaf S toOver ⋙ forget₂ RingCat AddCommGrpCat
```

**`Stacks.Sites.sheafHZeroAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L183). The attribute's comment: “degree zero: H⁰ of Gₐ is the additive group of global functions”.

> **Stacks 03P6 in degree zero.**  On a site of schemes over `S` with a terminal object `X₀`,
> the degree-zero cohomology of `Gₐ` is the additive group of global functions on the scheme over
> `S` that `X₀` names.  This is the degree-zero case of the remark's chain of equalities, and it
> holds for every topology at once with no input from [Stacks, Tag 03P2]: degree-zero sheaf
> cohomology is sections over a terminal object, and the sections of `Gₐ` are the global
> functions.

```lean
noncomputable def sheafHZeroAddEquiv (J : GrothendieckTopology C)
    (h : Presheaf.IsSheaf J (toOver.op ⋙ globalSectionsOver S))
    [HasSheafify J AddCommGrpCat.{u}] [HasExt.{w} (Sheaf J AddCommGrpCat.{u})]
    {X₀ : C} (hX₀ : IsTerminal X₀) :
    Sheaf.H (additiveGroupSheaf S toOver J h) 0 ≃+
      (additiveGroupPresheaf S toOver).obj (op X₀)
```

**`AlgebraicGeometry.BigFppfOver.additiveGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L207). The attribute's comment: “Gₐ on the big fppf site”.

> **Stacks 03P6, the big fppf site.**  `Gₐ` as an abelian sheaf on `(Sch/S)_{fppf}`.  Its
> underlying presheaf is the structure sheaf of [Stacks, Tag 04HS] of that site read additively,
> so its cohomology is the group the remark also writes `H^p_{fppf}(X, 𝒪_X)`.

```lean
noncomputable def additiveGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.BigFppfOver.sheafHZeroAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L225). The attribute's comment: “degree zero on the big fppf site”.

> **Stacks 03P6 in degree zero, fppf.**  `H^0_{fppf}(S, Gₐ) = Γ(S, 𝒪_S)`: the big fppf site
> over `S` has `S` itself for a terminal object, and degree-zero sheaf cohomology is sections
> over a terminal object.

```lean
noncomputable def sheafHZeroAddEquiv [HasSheafify (topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (topology B S hS) AddCommGrpCat.{u})] :
    Sheaf.H (additiveGroupSheaf S B hS) 0 ≃+ Stacks.Sites.globalSectionsAddCommGrp S
```

**`AlgebraicGeometry.BigEtaleOver.additiveGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L240). The attribute's comment: “Gₐ on the big étale site”.

> **Stacks 03P6, the big étale site.**  `Gₐ` as an abelian sheaf on `(Sch/S)_{étale}`.  Its
> underlying presheaf is the structure sheaf of [Stacks, Tag 04HS] of that site read additively,
> so its cohomology is the group the remark also writes `H^p_{étale}(X, 𝒪_X)`.

```lean
noncomputable def additiveGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.BigEtaleOver.sheafHZeroAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L259). The attribute's comment: “degree zero on the big étale site”.

> **Stacks 03P6 in degree zero, étale.**  `H^0_{étale}(S, Gₐ) = Γ(S, 𝒪_S)`: the big étale
> site over `S` has `S` itself for a terminal object, and degree-zero sheaf cohomology is
> sections over a terminal object.

```lean
noncomputable def sheafHZeroAddEquiv [HasSheafify (topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (topology B S hS) AddCommGrpCat.{u})] :
    Sheaf.H (additiveGroupSheaf S B hS) 0 ≃+ Stacks.Sites.globalSectionsAddCommGrp S
```

**`AlgebraicGeometry.BigZariskiOver.additiveGroupSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L274). The attribute's comment: “Gₐ on the big Zariski site”.

> **Stacks 03P6, the big Zariski site.**  `Gₐ` as an abelian sheaf on `(Sch/S)_{Zar}`.  Its
> underlying presheaf is the structure sheaf of [Stacks, Tag 04HS] of that site read additively,
> so its cohomology is the group the remark also writes `H^p_{Zar}(X, 𝒪_X)`.

```lean
noncomputable def additiveGroupSheaf : Sheaf (topology B S hS) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.BigZariskiOver.sheafHZeroAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L294). The attribute's comment: “degree zero on the big Zariski site”.

> **Stacks 03P6 in degree zero, Zariski.**  `H^0_{Zar}(S, Gₐ) = Γ(S, 𝒪_S)`: the big Zariski
> site over `S` has `S` itself for a terminal object, and degree-zero sheaf cohomology is
> sections over a terminal object.

```lean
noncomputable def sheafHZeroAddEquiv [HasSheafify (topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (topology B S hS) AddCommGrpCat.{u})] :
    Sheaf.H (additiveGroupSheaf S B hS) 0 ≃+ Stacks.Sites.globalSectionsAddCommGrp S
```

**`AlgebraicGeometry.additiveGroupSheafHZeroFppfEtaleAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L320). The attribute's comment: “degree zero: fppf against étale”.

> **Stacks 03P6 in degree zero, fppf against étale.**  `H^0\_\{fppf}(S, Gₐ) =
> H^0\_\{étale}(S, Gₐ)`: both are the additive group `Γ(S, 𝒪\_S)` of global functions.  This is one
> leg of the remark's chain of equalities, in the degree in which it needs nothing from
> [Stacks, Tag 03P2].

```lean
noncomputable def additiveGroupSheafHZeroFppfEtaleAddEquiv :
    Sheaf.H (BigFppfOver.additiveGroupSheaf S Bf hSf) 0 ≃+
      Sheaf.H (BigEtaleOver.additiveGroupSheaf S Be hSe) 0
```

**`AlgebraicGeometry.additiveGroupSheafHZeroFppfZariskiAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheaf.lean#L331). The attribute's comment: “degree zero: fppf against Zariski”.

> **Stacks 03P6 in degree zero, fppf against Zariski.**  `H^0\_\{fppf}(S, Gₐ) =
> H^0\_\{Zar}(S, Gₐ)`: both are the additive group `Γ(S, 𝒪\_S)` of global functions.  Together with
> `AlgebraicGeometry.additiveGroupSheafHZeroFppfEtaleAddEquiv` this is the remark's whole chain
> of equalities in degree zero, the rightmost term `H^0(S, 𝒪_S)` being `Γ(S, 𝒪_S)` as well.

```lean
noncomputable def additiveGroupSheafHZeroFppfZariskiAddEquiv :
    Sheaf.H (BigFppfOver.additiveGroupSheaf S Bf hSf) 0 ≃+
      Sheaf.H (BigZariskiOver.additiveGroupSheaf S Bz hSz) 0
```

**`AlgebraicGeometry.additiveGroupSheafCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafCohomology.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafCohomology.lean#L233). The attribute's comment: “all degrees p ≥ 0: H^p\_τ(X, Gₐ) = H^p(X, 𝒪\_X), the specialization of Theorem 03P2 to ℱ = 𝒪\_S. τ is a bound variable, so this one declaration is the comparison for all five big sites at once, in particular for the fppf, étale and Zariski sites the remark names. The left-hand side is cohomology of the structure sheaf on the site of opens of the underlying topological space of S, which is this repository's spelling of H^p(X, 𝒪\_X), so the rightmost equality of the chain needs no further comparison. The missing ingredient supplied here on top of 03P2 is Gₐ = (𝒪\_S)ᵃ, namely overAdditiveGroupSheafIsoAssociatedSheaf”. References: SGA 1 XI (5.3), “G\_a clause”; SGA 4 VII (4.2.1), “special case”.

> For a scheme `S` below the cutoff of a big `τ`-site and every `p`,
> `H^p(X, 𝒪_X) ≅ H^p_τ(X, Gₐ)`: the left-hand side is the cohomology of the structure sheaf on the
> underlying topological space of `S`, the right-hand side the `τ`-cohomology of `Gₐ` over the
> final object `(opensBelowToOver hS).obj ⊤` of the localized big site.

```lean
public def additiveGroupSheafCohomologyIso (p : ℕ) :
    Sheaf.H' ((SheafOfModules.toSheaf S.ringCatSheaf).obj (Scheme.unitModule S)) p ⊤ ≅
      Sheaf.H' (overAdditiveGroupSheaf S τ B hS) p
        ((opensBelowToOver (κ := cutoff τ B) hS).obj ⊤)
```

**`AlgebraicGeometry.additiveGroupSheafCohomologyFppfEtaleIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafCohomology.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafCohomology.lean#L252). The attribute's comment: “all degrees p ≥ 0: H^p\_fppf(X, Gₐ) = H^p\_étale(X, Gₐ), the first leg of the chain, obtained by composing additiveGroupSheafCohomologyIso at τ = fppf with its inverse at τ = étale. The sheaves are BigFppfOver.additiveGroupSheaf and BigEtaleOver.additiveGroupSheaf themselves, by overAdditiveGroupSheaf\_fppf and overAdditiveGroupSheaf\_etale. The degree-zero case is additiveGroupSheafHZeroFppfEtaleAddEquiv”.

> `H^p_{fppf}(X, Gₐ) ≅ H^p_{étale}(X, Gₐ)` for every `p`, both being `H^p(X, 𝒪_X)`.

```lean
public def additiveGroupSheafCohomologyFppfEtaleIso (p : ℕ) :
    Sheaf.H' (BigFppfOver.additiveGroupSheaf S Bf hSf) p
        ((opensBelowToOver (κ := cutoff .fppf Bf) hSf).obj ⊤) ≅
      Sheaf.H' (BigEtaleOver.additiveGroupSheaf S Be hSe) p
        ((opensBelowToOver (κ := cutoff .etale Be) hSe).obj ⊤)
```

**`AlgebraicGeometry.additiveGroupSheafCohomologyFppfZariskiIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafCohomology.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExamplesSheaves/AdditiveGroupSheafCohomology.lean#L267). The attribute's comment: “all degrees p ≥ 0: H^p\_fppf(X, Gₐ) = H^p\_Zar(X, Gₐ), the second leg of the chain. With additiveGroupSheafCohomologyFppfEtaleIso and additiveGroupSheafCohomologyIso this completes the chain H^p\_fppf = H^p\_étale = H^p\_Zar = H^p(X, 𝒪\_X) for all p ≥ 0. The sheaves are BigFppfOver.additiveGroupSheaf and BigZariskiOver.additiveGroupSheaf themselves, by overAdditiveGroupSheaf\_fppf and overAdditiveGroupSheaf\_zariski. The degree-zero case is additiveGroupSheafHZeroFppfZariskiAddEquiv”.

> `H^p_{fppf}(X, Gₐ) ≅ H^p_{Zar}(X, Gₐ)` for every `p`, both being `H^p(X, 𝒪_X)`.

```lean
public def additiveGroupSheafCohomologyFppfZariskiIso (p : ℕ) :
    Sheaf.H' (BigFppfOver.additiveGroupSheaf S Bf hSf) p
        ((opensBelowToOver (κ := cutoff .fppf Bf) hSf).obj ⊤) ≅
      Sheaf.H' (BigZariskiOver.additiveGroupSheaf S Bz hSz) p
        ((opensBelowToOver (κ := cutoff .zariski Bz) hSz).obj ⊤)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.23, Tag 03YZ](https://stacks.math.columbia.edu/tag/03YZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
