---
declaration: section
origin: cited
lean: AlgebraicGeometry.smallEtaleTopos, AlgebraicGeometry.bigEtaleTopos, AlgebraicGeometry.smallZariskiTopos, AlgebraicGeometry.bigZariskiTopos, AlgebraicGeometry.bigSmoothTopos, AlgebraicGeometry.bigSyntomicTopos, AlgebraicGeometry.bigFppfTopos, AlgebraicGeometry.smallEtaleToposEquiv
statement: formalized
proof: formalized
---

# 59.21 The étale topos

Section 59.21 of the Stacks Project, [Tag 04HP](https://stacks.math.columbia.edu/tag/04HP). 2 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04HQ, a definition

[Tag 04HQ](https://stacks.math.columbia.edu/tag/04HQ) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleTopos`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleTopos.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleTopos.lean#L45). The attribute's comment: “part (1): the small étale topos”.

> **Stacks 04HQ, part (1).** The small étale topos of `S` is the category of set-valued
> sheaves on the small étale site of `S`.

```lean
public abbrev smallEtaleTopos
```

**`AlgebraicGeometry.bigEtaleTopos`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleTopos.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleTopos.lean#L50). The attribute's comment: “part (3): the big étale topos”.

> **Stacks 04HQ, part (3), the étale case.** The big étale topos of `S` is the category of
> set-valued sheaves on the big étale site over `S`.

```lean
public abbrev bigEtaleTopos
```

**`AlgebraicGeometry.smallZariskiTopos`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Topoi.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Topoi.lean#L55). The attribute's comment: “part (2): the small Zariski topos”.

> **Stacks 04HQ, part (2).** The small Zariski topos of `S` is the category of set-valued
> sheaves on the small Zariski site of `S`.

```lean
public abbrev smallZariskiTopos (B : BigZariskiSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S)
```

**`AlgebraicGeometry.bigZariskiTopos`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Topoi.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Topoi.lean#L61). The attribute's comment: “part (3): the big Zariski topos”.

> **Stacks 04HQ, part (3), the Zariski case.** The big Zariski topos of `S` is the
> category of set-valued sheaves on the big Zariski site over `S`.

```lean
public abbrev bigZariskiTopos (B : BigZariskiSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S)
```

**`AlgebraicGeometry.bigSmoothTopos`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Topoi.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Topoi.lean#L67). The attribute's comment: “part (3): the big smooth topos”.

> **Stacks 04HQ, part (3), the smooth case.** The big smooth topos of `S` is the category
> of set-valued sheaves on the big smooth site over `S`.

```lean
public abbrev bigSmoothTopos (B : BigSmoothSite.{u}) (S : Scheme.{u})
    (hS : S.size < B.cutoff)
```

**`AlgebraicGeometry.bigSyntomicTopos`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Topoi.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Topoi.lean#L73). The attribute's comment: “part (3): the big syntomic topos”.

> **Stacks 04HQ, part (3), the syntomic case.** The big syntomic topos of `S` is the
> category of set-valued sheaves on the big syntomic site over `S`.

```lean
public abbrev bigSyntomicTopos (B : BigSyntomicSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S)
```

**`AlgebraicGeometry.bigFppfTopos`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Topoi.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Topoi.lean#L79). The attribute's comment: “part (3): the big fppf topos”.

> **Stacks 04HQ, part (3), the fppf case.** The big fppf topos of `S` is the category of
> set-valued sheaves on the big fppf site over `S`.

```lean
public abbrev bigFppfTopos (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S)
```

## Tag 0958, a lemma

[Tag 0958](https://stacks.math.columbia.edu/tag/0958) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleToposEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleToposIndependence.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleToposIndependence.lean#L390). The attribute's comment: “equivalence of small étale topoi”.

> The canonical equivalence between the small étale topoi obtained from two
> big étale sites containing the same scheme.

```lean
public noncomputable def smallEtaleToposEquiv
    (B₁ B₂ : BigEtaleSite.{u}) (S : Scheme.{u})
    (h₁ : B₁.Contains S) (h₂ : B₂.Contains S) :
    smallEtaleTopos.{u, max (u + 1) v} B₁ S h₁ ≌
      smallEtaleTopos.{u, max (u + 1) v} B₂ S h₂
```

**`AlgebraicGeometry.smallEtaleToposEquiv_sections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleToposIndependence.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleToposIndependence.lean#L402). The attribute's comment: “comparison on common affine étale objects”.

> On affine étale objects represented in both small sites, the comparison
> equivalence agrees with restriction along their identification over `S`. This
> is a natural isomorphism of evaluation functors, hence is natural in the sheaf.

```lean
public noncomputable def smallEtaleToposEquiv_sections
    (B₁ B₂ : BigEtaleSite.{u}) (S : Scheme.{u})
    (h₁ : B₁.Contains S) (h₂ : B₂.Contains S)
    (X₁ : SmallAffineEtale B₁ S h₁)
    (X₂ : SmallAffineEtale B₂ S h₂)
    (e : (Over.post B₁.inclusion).obj X₁.obj.obj ≅
      (Over.post B₂.inclusion).obj X₂.obj.obj) :
    (smallEtaleToposEquiv.{u, v} B₁ B₂ S h₁ h₂).functor ⋙
        (sheafSections (SmallEtale.topology B₂ S h₂)
          (Type (max (u + 1) v))).obj
          (Opposite.op X₂.obj) ≅
      (sheafSections (SmallEtale.topology B₁ S h₁)
        (Type (max (u + 1) v))).obj
        (Opposite.op X₁.obj)
```

**`AlgebraicGeometry.smallEtaleToposEquiv_sections_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleToposIndependence.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleToposIndependence.lean#L429). The attribute's comment: “naturality on common affine étale objects”.

> The section comparison commutes with restrictions along a morphism of
> common affine étale objects.

```lean
public theorem smallEtaleToposEquiv_sections_natural
    (B₁ B₂ : BigEtaleSite.{u}) (S : Scheme.{u})
    (h₁ : B₁.Contains S) (h₂ : B₂.Contains S)
    (X₁ Y₁ : SmallAffineEtale B₁ S h₁)
    (X₂ Y₂ : SmallAffineEtale B₂ S h₂)
    (eX : (Over.post B₁.inclusion).obj X₁.obj.obj ≅
      (Over.post B₂.inclusion).obj X₂.obj.obj)
    (eY : (Over.post B₁.inclusion).obj Y₁.obj.obj ≅
      (Over.post B₂.inclusion).obj Y₂.obj.obj)
    (f₁ : X₁ ⟶ Y₁) (f₂ : X₂ ⟶ Y₂)
    (hf : (Over.post B₁.inclusion).map
        ((SmallEtale.inclusion B₁ S h₁).map
          ((SmallAffineEtale.inclusion B₁ S h₁).map f₁)) ≫ eY.hom =
      eX.hom ≫ (Over.post B₂.inclusion).map
        ((SmallEtale.inclusion B₂ S h₂).map
          ((SmallAffineEtale.inclusion B₂ S h₂).map f₂)))
    (F : smallEtaleTopos.{u, max (u + 1) v} B₁ S h₁) :
    (smallEtaleToposEquiv_sections.{u, v} B₁ B₂ S h₁ h₂ Y₁ Y₂ eY).hom.app F ≫
        ((sheafSections (SmallEtale.topology B₁ S h₁)
          (Type (max (u + 1) v))).map
          (Opposite.op ((SmallAffineEtale.inclusion B₁ S h₁).map f₁))).app F =
      ((sheafSections (SmallEtale.topology B₂ S h₂)
        (Type (max (u + 1) v))).map
          (Opposite.op ((SmallAffineEtale.inclusion B₂ S h₂).map f₂))).app
            ((smallEtaleToposEquiv.{u, v} B₁ B₂ S h₁ h₂).functor.obj F) ≫
        (smallEtaleToposEquiv_sections.{u, v} B₁ B₂ S h₁ h₂ X₁ X₂ eX).hom.app F
```

**`AlgebraicGeometry.smallEtaleToposEquiv_refl`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleToposIndependence.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleToposIndependence.lean#L483). The attribute's comment: “identity comparison”.

> Comparing a small étale topos with itself is naturally isomorphic to the
> identity functor.

```lean
public noncomputable def smallEtaleToposEquiv_refl
    (B : BigEtaleSite.{u}) (S : Scheme.{u})
    (h : B.Contains S) :
    (smallEtaleToposEquiv.{u, v} B B S h h).functor ≅
      𝟭 (smallEtaleTopos.{u, max (u + 1) v} B S h)
```

**`AlgebraicGeometry.smallEtaleToposEquiv_trans`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleToposIndependence.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleToposIndependence.lean#L493). The attribute's comment: “composition of comparisons”.

> The equivalence for two successive changes of big étale site agrees,
> naturally in sheaves, with the equivalence for the direct change.

```lean
public noncomputable def smallEtaleToposEquiv_trans
    (B₁ B₂ B₃ : BigEtaleSite.{u}) (S : Scheme.{u})
    (h₁ : B₁.Contains S) (h₂ : B₂.Contains S) (h₃ : B₃.Contains S) :
    (smallEtaleToposEquiv.{u, v} B₁ B₂ S h₁ h₂).functor ⋙
      (smallEtaleToposEquiv.{u, v} B₂ B₃ S h₂ h₃).functor ≅
        (smallEtaleToposEquiv.{u, v} B₁ B₃ S h₁ h₃).functor
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.21, Tag 04HP](https://stacks.math.columbia.edu/tag/04HP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
