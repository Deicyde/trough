---
declaration: section
origin: cited
lean: AlgebraicGeometry.PrePureSituation, AlgebraicGeometry.ImpurityDiagram, AlgebraicGeometry.IsImpurity, AlgebraicGeometry.exists_impurity_locallyOfFinitePresentation_closedPoint, AlgebraicGeometry.exists_isImpurity_mapBase_of_isLimit, AlgebraicGeometry.exists_isImpurity_elementaryEtaleNeighborhood_of_quasiFiniteAt, AlgebraicGeometry.exists_isImpurity_quasiFiniteAt, AlgebraicGeometry.exists_isImpurity_elementaryEtaleNeighborhood_of_henselization
statement: formalized
proof: formalized
---

# 38.15 Impurities

Section 38.15 of the Stacks Project, [Tag 05IW](https://stacks.math.columbia.edu/tag/05IW). 9 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05FW, a situation

[Tag 05FW](https://stacks.math.columbia.edu/tag/05FW) in the Stacks Project.

**`AlgebraicGeometry.PrePureSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Impurities.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Impurities.lean#L60).

> **Stacks Project, Tag 05FW.** The standing pre-pure situation: a finite type morphism
> `X ⟶ S`, a finite type quasi-coherent module on `X`, and a point of `S`.

```lean
structure PrePureSituation
```

## Tag 05IX, an equation

[Tag 05IX](https://stacks.math.columbia.edu/tag/05IX) in the Stacks Project.

**`AlgebraicGeometry.ImpurityDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Impurities.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Impurities.lean#L85).

> **Stacks Project, Tag 05IX.** A base-change diagram together with a specialization over the
> chosen point of a pre-pure situation and a point above its generalization.

```lean
structure ImpurityDiagram (P : PrePureSituation.{u})
```

## Tag 05IY, a definition

[Tag 05IY](https://stacks.math.columbia.edu/tag/05IY) in the Stacks Project.

**`AlgebraicGeometry.IsImpurity`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Impurities.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Impurities.lean#L118).

> **Stacks Project, Tag 05IY.** An impurity diagram defines an impurity when its chosen point
> belongs to the relative assassin of the pulled-back module and its closure is disjoint from the
> fibre over the specialized point.

```lean
abbrev IsImpurity (P : PrePureSituation.{u}) (D : ImpurityDiagram P) : Prop
```

## Tag 05FX, a lemma

[Tag 05FX](https://stacks.math.columbia.edu/tag/05FX) in the Stacks Project.

**`AlgebraicGeometry.exists_impurity_locallyOfFinitePresentation_closedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Impurity/FinitePresentationBase.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Impurity/FinitePresentationBase.lean#L300).

> An impurity can be witnessed over a test family which is
> locally of finite presentation over the base, with its specialized point closed in the fibre over
> the distinguished point.

```lean
theorem exists_impurity_locallyOfFinitePresentation_closedPoint (P : PrePureSituation.{u})
    (h : ∃ D : ImpurityDiagram P, IsImpurity P D) :
    ∃ D : ImpurityDiagram P, IsImpurity P D ∧ LocallyOfFinitePresentation D.g ∧
      ∃ t_fib : D.g.fiber P.s,
        D.g.fiberι P.s t_fib = D.t ∧ t_fib ∈ closedPoints (D.g.fiber P.s)
```

## Tag 05IZ, a lemma

[Tag 05IZ](https://stacks.math.columbia.edu/tag/05IZ) in the Stacks Project.

**`AlgebraicGeometry.exists_isImpurity_mapBase_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Impurity/LimitDescent.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Impurity/LimitDescent.lean#L399).

> An impurity on a cofiltered limit of affine schemes over the base is the pullback of an
> impurity at some stage.

```lean
public theorem exists_isImpurity_mapBase_of_isLimit
    {P : AlgebraicGeometry.PrePureSituation.{u}}
    {I : Type v} [Category.{w} I] [IsCofiltered I]
    (F : I ⥤ Over P.S) (c : Cone F) (hc : IsLimit c)
    (D : AlgebraicGeometry.ImpurityDiagram P) (e : Over.mk D.g ≅ c.pt)
    (hF : ∀ i, IsAffine (F.obj i).left) (hD : AlgebraicGeometry.IsImpurity P D) :
    ∃ i, AlgebraicGeometry.IsImpurity P
      (mapBase D (F.obj i).hom (e.hom ≫ c.π.app i).left (e.hom ≫ c.π.app i).w)
```

## Tag 05J0, a lemma

[Tag 05J0](https://stacks.math.columbia.edu/tag/05J0) in the Stacks Project.

**`AlgebraicGeometry.exists_isImpurity_elementaryEtaleNeighborhood_of_quasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Impurity/QuasiFiniteNeighborhood.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Impurity/QuasiFiniteNeighborhood.lean#L235).

> **Stacks Project, Tag 05J0.** If a pre-pure situation admits an impurity whose test family
> is quasi-finite over the base at the distinguished point, then it admits one whose test family,
> pointed at the distinguished point, is an elementary étale neighbourhood of the chosen point of
> the base.

```lean
theorem exists_isImpurity_elementaryEtaleNeighborhood_of_quasiFiniteAt
    (P : PrePureSituation.{u})
    (h : ∃ D : ImpurityDiagram P, IsImpurity P D ∧ quasiFiniteAt D.g D.t) :
    ∃ (D : ImpurityDiagram P) (hD : Etale D.g), IsImpurity P D ∧
      EtaleNeighborhood.IsElementary
        ({ scheme := D.T
           point := D.t
           toBase := D.g
           etale_toBase := hD
           map_point := D.mapsToChosenPoint } : EtaleNeighborhood P.S P.s)
```

## Tag 05J1, a lemma

[Tag 05J1](https://stacks.math.columbia.edu/tag/05J1) in the Stacks Project.

**`AlgebraicGeometry.exists_isImpurity_quasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Impurity/QuasiFiniteTestFamily.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Impurity/QuasiFiniteTestFamily.lean#L337).

> **Stacks Project, Tag 05J1.** Over a locally Noetherian base, an impurity of the module of a
> pre-pure situation above the chosen point of the base can be witnessed by an impurity whose test
> family is quasi-finite over the base at its specialized point.

```lean
theorem exists_isImpurity_quasiFiniteAt (P : PrePureSituation.{u}) [IsLocallyNoetherian P.S]
    (h : ∃ D : ImpurityDiagram P, IsImpurity P D) :
    ∃ D : ImpurityDiagram P, IsImpurity P D ∧ quasiFiniteAt D.g D.t
```

## Tag 05J2, a lemma

[Tag 05J2](https://stacks.math.columbia.edu/tag/05J2) in the Stacks Project.

**`AlgebraicGeometry.exists_isImpurity_elementaryEtaleNeighborhood_of_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Impurity/HenselizationDescent.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Impurity/HenselizationDescent.lean#L173).

> An impurity whose test family is the spectrum of a henselization of the local ring of the base
> at the distinguished point already occurs over an elementary étale neighbourhood of that point.

```lean
theorem exists_isImpurity_elementaryEtaleNeighborhood_of_henselization
    (P : PrePureSituation.{u}) (Rh : Type u) [CommRing Rh] [IsLocalRing Rh]
    [Algebra (P.S.presheaf.stalk P.s) Rh]
    [IsLocalRing.IsHenselization (P.S.presheaf.stalk P.s)
      (IsLocalRing.ResidueField (P.S.presheaf.stalk P.s)) Rh]
    (h : ∃ (D : ImpurityDiagram P) (e : D.T ≅ Spec (CommRingCat.of Rh)),
      D.g = e.hom ≫ specHenselizationToBase P.s Rh ∧ IsImpurity P D) :
    ∃ (D : ImpurityDiagram P) (hD : Etale D.g), IsImpurity P D ∧
      EtaleNeighborhood.IsElementary
        ({ scheme := D.T
           point := D.t
           toBase := D.g
           etale_toBase := hD
           map_point := D.mapsToChosenPoint } : EtaleNeighborhood P.S P.s)
```

## Tag 05J3, a lemma

[Tag 05J3](https://stacks.math.columbia.edu/tag/05J3) in the Stacks Project.

**`AlgebraicGeometry.exists_isImpurity_henselization_iff_elementaryEtaleNeighborhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Impurity/HenselizationAscent.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Impurity/HenselizationAscent.lean#L104). The attribute's comment: “parts (1) and (2)”.

> In a pre-pure situation, an impurity over the henselization of the base at the distinguished
> point exists if and only if one exists over an elementary étale neighbourhood of that point.

```lean
theorem exists_isImpurity_henselization_iff_elementaryEtaleNeighborhood
    (P : PrePureSituation.{u}) :
    (∃ (D : ImpurityDiagram P) (e : D.T ≅ henselization P.S P.s),
      D.g = e.hom ≫ henselizationToBase P.S P.s ∧ IsImpurity P D) ↔
    (∃ (D : ImpurityDiagram P) (hD : Etale D.g), IsImpurity P D ∧
      EtaleNeighborhood.IsElementary
        ({ scheme := D.T
           point := D.t
           toBase := D.g
           etale_toBase := hD
           map_point := D.mapsToChosenPoint } : EtaleNeighborhood P.S P.s))
```

**`AlgebraicGeometry.exists_isImpurity_elementaryEtaleNeighborhood_iff_quasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/QuasiFiniteImpurityData.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/QuasiFiniteImpurityData.lean#L248). The attribute's comment: “parts (2) and (3)”.

> **Stacks Project, Tag 05J3, parts (2) and (3).** A pre-pure situation admits an impurity
> whose test family, pointed at the distinguished point, is an elementary étale neighbourhood of
> the chosen point of the base if and only if it admits one whose test family is quasi-finite over
> the base at the distinguished point.

```lean
theorem exists_isImpurity_elementaryEtaleNeighborhood_iff_quasiFiniteAt
    (P : PrePureSituation.{u}) :
    (∃ (D : ImpurityDiagram P) (hD : Etale D.g), IsImpurity P D ∧
      EtaleNeighborhood.IsElementary
        ({ scheme := D.T
           point := D.t
           toBase := D.g
           etale_toBase := hD
           map_point := D.mapsToChosenPoint } : EtaleNeighborhood P.S P.s)) ↔
    (∃ D : ImpurityDiagram P, IsImpurity P D ∧ quasiFiniteAt D.g D.t)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.15, Tag 05IW](https://stacks.math.columbia.edu/tag/05IW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
