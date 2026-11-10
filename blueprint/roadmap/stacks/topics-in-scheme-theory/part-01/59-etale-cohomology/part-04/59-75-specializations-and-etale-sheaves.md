---
declaration: section
origin: cited
lean: AlgebraicGeometry.etaleStalkToSectionsAb_eq_smallEtaleSpecializationStalkAb, AlgebraicGeometry.smallEtaleSpecializationStalkAb_eq_sectionsRestrictionAb, AlgebraicGeometry.etaleStalkToSectionsAb_id_comp_sectionsRestrictionAb, AlgebraicGeometry.existsUnique_specializationMorphism_and_specialization_eq_pullback, AlgebraicGeometry.existsUnique_specializationMorphism, AlgebraicGeometry.specializationMorphism, AlgebraicGeometry.specializationMapOnSections, AlgebraicGeometry.abelianSpecializationMapOnSections
statement: formalized
proof: formalized
---

# 59.75 Specializations and étale sheaves

Section 59.75 of the Stacks Project, [Tag 0GJ2](https://stacks.math.columbia.edu/tag/0GJ2). 8 tags here are carried by 21 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GJ3, a remark

[Tag 0GJ3](https://stacks.math.columbia.edu/tag/0GJ3) in the Stacks Project.

**`AlgebraicGeometry.etaleStalkToSectionsAb_eq_smallEtaleSpecializationStalkAb`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationStalk.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationStalk.lean#L253). The attribute's comment: “the specialization map is pullback by the geometric point of the strict henselization, after the identification of the stalk at the specialized point with sections on that point. The factorization of the left-hand side through sections over the strict henselization itself is not proved here; see the module docstring.”.

> **The specialization map is pullback by `t`.** Composed with the comparison
> `F_{t ≫ p} ⟶ Γ(t, (t ≫ p)⁻¹F)` of Stacks 03Q1, the specialization map on stalks is the canonical
> map `F_s ⟶ Γ(t, (t ≫ p)⁻¹F)` of Stacks 0GJN, which restricts the germ at `s` of a section over an
> étale neighbourhood `W` along the composite `t ⟶ Spec(𝒪^{sh}_{S,s}) ⟶ W`.

```lean
theorem etaleStalkToSectionsAb_eq_smallEtaleSpecializationStalkAb :
    etaleStalkToSectionsAb B S hS s t.hom =
      smallEtaleSpecializationStalkAb B S hS s t ≫
        geometricStalkToPullbackSectionsAb (t.hom ≫ strictHenselizationToBase B S hS s)
```

**`AlgebraicGeometry.smallEtaleSpecializationStalkAb_eq_sectionsRestrictionAb`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SpecializationStalkIdentifications.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SpecializationStalkIdentifications.lean#L354). The attribute's comment: “the specialization map is pullback of sections along `t`, read through the two identifications F_s = Γ(Spec 𝒪^sh_{S,s}, p⁻¹F) (03Q9 at the identity) and F_{t ≫ p} = Γ(t, t⁻¹p⁻¹F) (03Q1), both isomorphisms”.

> Let `S` be a scheme, `s` a geometric point of `S`, `p : Spec(𝒪^{sh}_{S,s}) ⟶ S` the
> structure morphism of the strict henselization at `s`, and `t` a geometric point of
> `Spec(𝒪^{sh}_{S,s})`, so that the image of `t ≫ p` is a specialization of the image of `s`. Use
> the two identifications
>
> `F_s = Γ(Spec(𝒪^{sh}_{S,s}), p⁻¹F)`  and  `F_{t ≫ p} = Γ(t, t⁻¹p⁻¹F)`,
>
> the first of which is Theorem 03Q9 applied to `id_S : S ⟶ S` and the second Lemma 03Q1. Then the
> specialization map `sp : F_s ⟶ F_{t ≫ p}` of Stacks 0GJ2 *is* the map induced between them by
> pullback of sections along `t`, that is, it is the composite of the first identification, the
> restriction of sections along `t`, and the inverse of the second.
>
> Here the first identification is `AlgebraicGeometry.etaleStalkSectionsAbIso`, the second is
> `AlgebraicGeometry.geometricStalkPullbackSectionsAbIso`, and restriction of sections along `t` is
> `Stacks.EtaleCohomology.smallEtaleSectionsRestrictionAb`.

```lean
theorem smallEtaleSpecializationStalkAb_eq_sectionsRestrictionAb :
    smallEtaleSpecializationStalkAb B S hS s t =
      (etaleStalkSectionsAbIso B S hS s).hom ≫
        smallEtaleSectionsRestrictionAb
            (𝟙 (strictHenselization B S hS s) ≫ strictHenselizationToBase B S hS s) t.hom
            (t.hom ≫ strictHenselizationToBase B S hS s)
            ((Category.assoc t.hom (𝟙 (strictHenselization B S hS s))
                (strictHenselizationToBase B S hS s)).symm.trans
              (congrArg (fun y : t.source ⟶ strictHenselization B S hS s =>
                y ≫ strictHenselizationToBase B S hS s) (Category.comp_id t.hom))) ≫
          (geometricStalkPullbackSectionsAbIso
            (t.hom ≫ strictHenselizationToBase B S hS s)).inv
```

**`AlgebraicGeometry.etaleStalkToSectionsAb_id_comp_sectionsRestrictionAb`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkSectionsTransitivity.lean, line 506](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkSectionsTransitivity.lean#L506). The attribute's comment: “the displayed composite: the identification of the stalk at `s` with sections over the strict henselization, followed by pullback by `t`, is the specialization map followed by the identification of the stalk at the specialized point with sections on that point. The two identifications are the canonical maps; this statement compares them and does not assert that either is invertible. Invertibility is Stacks 03Q1 and Stacks 03Q9. Of these the library carries 03Q1 for `Type`-valued sheaves, as `AlgebraicGeometry.smallEtalePullbackStalkIso`, and 03Q9 only conditionally on the base being the spectrum of a strictly henselian local ring; neither is in the abelian form and at the generality used here, so neither is applied.”.

> **Stacks 0GJ3, the displayed composite.** Let `S` be a scheme, `s` a geometric point of `S`,
> `p : Spec(𝒪^{sh}_{S,s}) ⟶ S` the structure morphism of the strict henselization at `s`, and `t` a
> geometric point of `Spec(𝒪^{sh}_{S,s})`. Then the identification
> `F_s = Γ(Spec(𝒪^{sh}_{S,s}), p⁻¹F)` of Stacks 03Q9, followed by pullback of sections by `t`, is
> the specialization map `sp : F_s ⟶ F_{t ≫ p}` followed by the identification
> `F_{t ≫ p} = Γ(t, (t ≫ p)⁻¹F)` of Stacks 03Q1.
>
> This is the source's displayed description of `sp` as pullback by `t`. The two identifications
> are `AlgebraicGeometry.etaleStalkToSectionsAb` at the identity of the strict henselization and
> `AlgebraicGeometry.geometricStalkToPullbackSectionsAb`; they are the canonical maps, which Stacks
> 03Q9 and 03Q1 assert are isomorphisms.

```lean
theorem etaleStalkToSectionsAb_id_comp_sectionsRestrictionAb :
    etaleStalkToSectionsAb B S hS s (𝟙 (strictHenselization B S hS s)) ≫
        smallEtaleSectionsRestrictionAb
          (𝟙 (strictHenselization B S hS s) ≫ strictHenselizationToBase B S hS s) t.hom
          (t.hom ≫ strictHenselizationToBase B S hS s)
          ((Category.assoc t.hom (𝟙 (strictHenselization B S hS s))
              (strictHenselizationToBase B S hS s)).symm.trans
            (congrArg (fun y : t.source ⟶ strictHenselization B S hS s =>
              y ≫ strictHenselizationToBase B S hS s) (Category.comp_id t.hom))) =
      smallEtaleSpecializationStalkAb B S hS s t ≫
        geometricStalkToPullbackSectionsAb (t.hom ≫ strictHenselizationToBase B S hS s)
```

## Tag 0GJ4, a remark

[Tag 0GJ4](https://stacks.math.columbia.edu/tag/0GJ4) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_specializationMorphism_and_specialization_eq_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationIsPullbackByMorphism.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationIsPullbackByMorphism.lean#L408). The attribute's comment: “the whole remark: (1) the unique existence of `c`; (2) global sections over the two strictly henselian schemes are exact and are stalks at their closed geometric points; (3) on abelian sheaves, the identifications of the stalks at `s` and at `t ≫ p` with the sections over the two strict henselizations are isomorphisms, and `sp` is pullback by `c`; (4) the same on the unbounded derived category, with `RΓ`. The big etale site `B` with `hS` is a size device, not a source hypothesis.”.

> **Stacks 0GJ4.** Let `S` be a scheme, `s` a geometric point of `S`, and `t` a geometric
> point of the strict henselization `Spec(𝒪^{sh}_{S,s})`, with structure morphism
> `p : Spec(𝒪^{sh}_{S,s}) ⟶ S`.
>
> 1. There is exactly one morphism `c : Spec(𝒪^{sh}_{S,t ≫ p}) ⟶ Spec(𝒪^{sh}_{S,s})` over `S`
>    compatible with the given morphism `t` to `Spec(𝒪^{sh}_{S,s})` and the canonical geometric
>    point of `Spec(𝒪^{sh}_{S,t ≫ p})`.
> 2. Taking global sections of abelian sheaves over the strictly henselian schemes
>    `Spec(𝒪^{sh}_{S,s})` and `Spec(𝒪^{sh}_{S,t ≫ p})` is exact, and is the same as taking stalks
>    at their canonical geometric points (lying over `s` and over `t ≫ p`). This is the source's
>    reason that the equality signs below are valid.
> 3. For abelian sheaves `F` on the small étale site of `S`, the identifications
>    `F_s = Γ(Spec(𝒪^{sh}_{S,s}), p⁻¹F)` and `F_{t ≫ p} = Γ(Spec(𝒪^{sh}_{S,t ≫ p}), p⁻¹F)` are
>    isomorphisms, and the specialization map `sp : F_s ⟶ F_{t ≫ p}` is pullback by `c`: the
>    first identification followed by restriction of sections along `c` is `sp` followed by the
>    second identification.
> 4. The same holds for objects `K` of the unbounded derived category `D(S_étale)`, with `RΓ` in
>    place of `Γ` and the specialization map on derived stalks in place of `sp`: both
>    identifications `K_s = RΓ(Spec(𝒪^{sh}_{S,s}), K)` and
>    `K_{t ≫ p} = RΓ(Spec(𝒪^{sh}_{S,t ≫ p}), K)` are isomorphisms, and `sp` is pullback by `c`.
>
> Part (1) is `AlgebraicGeometry.existsUnique_specializationMorphism`; part (2) is
> `AlgebraicGeometry.preservesFiniteColimits_smallEtaleGlobalSections_strictHenselization` and
> `AlgebraicGeometry.isIso_strictHenselizationSectionsToStalkAb`; the invertibility in (3) and
> (4) is `AlgebraicGeometry.isIso_etaleStalkToSectionsAb_id` and
> `AlgebraicGeometry.isIso_vanishingCyclesMap_id`, the source's reason that global sections over a
> strictly henselian scheme are exact and are the stalk at the closed point; the equations are
> `AlgebraicGeometry.etaleStalkToSectionsAb_id_comp_sectionsRestrictionAb_specializationMorphism`
> and
> `AlgebraicGeometry.vanishingCyclesMap_id_comp_derivedSectionsRestriction_specializationMorphism`.
> The derivability instances that unbounded derived global sections on the two strict
> henselizations are formed with are bound inside part (4); they hold for every scheme
> (`Stacks.EtaleCohomology.smallEtaleGlobalSectionsAb_hasRightDerivedFunctor`), and part (4) is
> proved for every choice of them.

```lean
public theorem existsUnique_specializationMorphism_and_specialization_eq_pullback
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) (s : GeometricPoint S)
    (t : GeometricPoint (strictHenselization B S hS s)) :
    (∃! c : strictHenselization B S hS (t.map (strictHenselizationToBase B S hS s)) ⟶
        strictHenselization B S hS s,
        c ≫ strictHenselizationToBase B S hS s =
            strictHenselizationToBase B S hS
              (t.map (strictHenselizationToBase B S hS s)) ∧
          geometricPointToStrictHenselization B S hS
              (t.map (strictHenselizationToBase B S hS s)) ≫ c = t.hom) ∧
      (PreservesFiniteColimits
          (Sheaf.Γ (smallEtaleTopology (strictHenselization B S hS s)) Ab.{u + 1}) ∧
        PreservesFiniteColimits (Sheaf.Γ (smallEtaleTopology (strictHenselization B S hS
          (t.map (strictHenselizationToBase B S hS s)))) Ab.{u + 1}) ∧
        IsIso (strictHenselizationSectionsToStalkAb B S hS s) ∧
        IsIso (strictHenselizationSectionsToStalkAb B S hS
          (t.map (strictHenselizationToBase B S hS s)))) ∧
      (IsIso (etaleStalkToSectionsAb B S hS s (𝟙 (strictHenselization B S hS s))) ∧
        IsIso (etaleStalkToSectionsAb B S hS (t.map (strictHenselizationToBase B S hS s))
          (𝟙 (strictHenselization B S hS (t.map (strictHenselizationToBase B S hS s))))) ∧
        etaleStalkToSectionsAb B S hS s (𝟙 (strictHenselization B S hS s)) ≫
            smallEtaleSectionsRestrictionAb
              (𝟙 (strictHenselization B S hS s) ≫ strictHenselizationToBase B S hS s)
              (specializationMorphism B S hS s t)
              (𝟙 (strictHenselization B S hS
                  (t.map (strictHenselizationToBase B S hS s))) ≫
                strictHenselizationToBase B S hS
                  (t.map (strictHenselizationToBase B S hS s)))
              (specializationMorphism_id_comp B S hS s t) =
          smallEtaleSpecializationStalkAb B S hS s t ≫
            etaleStalkToSectionsAb B S hS (t.map (strictHenselizationToBase B S hS s))
              (𝟙 (strictHenselization B S hS
                (t.map (strictHenselizationToBase B S hS s))))) ∧
        ∀ [((Sheaf.Γ (smallEtaleTopology (strictHenselization B S hS s))
                Ab.{u + 1}).mapHomotopyCategory (.up ℤ) ⋙
              DerivedCategory.Qh).HasRightDerivedFunctor
              (HomotopyCategory.quasiIso
                (Sheaf (smallEtaleTopology (strictHenselization B S hS s))
                  Ab.{u + 1}) (.up ℤ))]
            [((Sheaf.Γ (smallEtaleTopology (strictHenselization B S hS
                    (t.map (strictHenselizationToBase B S hS s))))
                  Ab.{u + 1}).mapHomotopyCategory (.up ℤ) ⋙
                DerivedCategory.Qh).HasRightDerivedFunctor
                (HomotopyCategory.quasiIso
                  (Sheaf (smallEtaleTopology (strictHenselization B S hS
                    (t.map (strictHenselizationToBase B S hS s)))) Ab.{u + 1}) (.up ℤ))],
          IsIso (vanishingCyclesMap B S hS s (𝟙 (strictHenselization B S hS s))) ∧
          IsIso (vanishingCyclesMap B S hS (t.map (strictHenselizationToBase B S hS s))
            (𝟙 (strictHenselization B S hS (t.map (strictHenselizationToBase B S hS s))))) ∧
          vanishingCyclesMap B S hS s (𝟙 (strictHenselization B S hS s)) ≫
              Functor.whiskerLeft
                  (smallEtaleDerivedPullbackAb
                    (𝟙 (strictHenselization B S hS s) ≫
                      strictHenselizationToBase B S hS s))
                  (smallEtaleDerivedGlobalSectionsRestriction
                    (specializationMorphism B S hS s t)) ≫
                (Functor.associator
                    (smallEtaleDerivedPullbackAb
                      (𝟙 (strictHenselization B S hS s) ≫
                        strictHenselizationToBase B S hS s))
                    (smallEtaleDerivedPullbackAb (specializationMorphism B S hS s t))
                    (smallEtaleDerivedGlobalSections (strictHenselization B S hS
                      (t.map (strictHenselizationToBase B S hS s))))).inv ≫
                  Functor.whiskerRight (Functor.mapDerivedCategoryCompIsoOfCompIso
                      (smallEtalePullbackAbCompIso (specializationMorphism B S hS s t)
                          (𝟙 (strictHenselization B S hS s) ≫
                            strictHenselizationToBase B S hS s) ≪≫
                        eqToIso (congrArg
                          (fun m : strictHenselization B S hS
                              (t.map (strictHenselizationToBase B S hS s)) ⟶ S =>
                            smallEtalePullbackAb m)
                          (specializationMorphism_id_comp B S hS s t)))).hom
                    (smallEtaleDerivedGlobalSections (strictHenselization B S hS
                      (t.map (strictHenselizationToBase B S hS s)))) =
            smallEtaleDerivedSpecializationStalkAb B S hS s t ≫
              vanishingCyclesMap B S hS (t.map (strictHenselizationToBase B S hS s))
                (𝟙 (strictHenselization B S hS
                  (t.map (strictHenselizationToBase B S hS s))))
```

**`AlgebraicGeometry.existsUnique_specializationMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationMorphism.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationMorphism.lean#L195). The attribute's comment: “specialization_morphism_of_strict_henselizations”.

> The specialization morphism of strict henselizations exists and is unique: a geometric point
> `t` of the strict henselization at `s` determines exactly one morphism from the strict
> henselization at the image of `t` in `S` to the strict henselization at `s` which lies over `S`
> and carries the canonical geometric point of its source to `t`.

```lean
public theorem existsUnique_specializationMorphism (s : GeometricPoint S)
    (t : GeometricPoint (strictHenselization B S hS s)) :
    let T := strictHenselization B S hS s
    let p := strictHenselizationToBase B S hS s
    let tS := t.map p
    ∃! c : strictHenselization B S hS tS ⟶ T,
      (c ≫ p = strictHenselizationToBase B S hS tS) ∧
      (geometricPointToStrictHenselization B S hS tS ≫ c = t.hom)
```

**`AlgebraicGeometry.specializationMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationMorphism.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationMorphism.lean#L398). The attribute's comment: “specialization_morphism_of_strict_henselizations”.

> The specialization morphism of strict henselizations attached to a geometric point of the
> strict henselization at `s`: the unique morphism over `S` from the strict henselization at the
> image of that point in `S` to the strict henselization at `s` which carries the canonical
> geometric point of its source to the given one.

```lean
public def specializationMorphism (s : GeometricPoint S)
    (t : GeometricPoint (strictHenselization B S hS s)) :
    strictHenselization B S hS (t.map (strictHenselizationToBase B S hS s)) ⟶
      strictHenselization B S hS s
```

**`AlgebraicGeometry.specializationMapOnSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationOnSections.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationOnSections.lean#L161). The attribute's comment: “specialization_map_on_sections”.

> Specialization of a section along the canonical morphism of strict henselizations
> determined by a geometric point `t` of the strict henselization at `s`: the pullback of global
> sections along the specialization morphism.

```lean
public def specializationMapOnSections
    (t : GeometricPoint (strictHenselization B S hS s))
    (hT : B.Contains (strictHenselization B S hS s))
    (hU : B.Contains (strictHenselization B S hS
      (t.map (strictHenselizationToBase B S hS s))))
    (F : Sheaf (SmallEtale.topology B S hS) (Type (u + 1))) :
    let p : (⟨strictHenselization B S hS s, hT⟩ : B.Scheme) ⟶ (⟨S, hS⟩ : B.Scheme) :=
      ⟨strictHenselizationToBase B S hS s⟩
    haveI := smallEtaleBaseChange_isContinuous B p
    let c : (⟨strictHenselization B S hS
      (t.map (strictHenselizationToBase B S hS s)), hU⟩ : B.Scheme) ⟶
      (⟨strictHenselization B S hS s, hT⟩ : B.Scheme) :=
      ⟨specializationMorphism B S hS s t⟩
    haveI := smallEtaleBaseChange_isContinuous B c
    let G := ((smallEtaleBaseChange B p).sheafPullback (Type (u + 1))
      (SmallEtale.topology B S hS)
      (SmallEtale.topology B _ hT)).obj F
    (Sheaf.Γ (SmallEtale.topology B _ hT) (Type (u + 1))).obj G ⟶
      (Sheaf.Γ (SmallEtale.topology B _ hU) (Type (u + 1))).obj
        (((smallEtaleBaseChange B c).sheafPullback (Type (u + 1))
          (SmallEtale.topology B _ hT)
          (SmallEtale.topology B _ hU)).obj G)
```

**`AlgebraicGeometry.abelianSpecializationMapOnSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationOnSections.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationOnSections.lean#L199). The attribute's comment: “specialization_map_on_sections”.

> Specialization along the canonical morphism of strict henselizations, as a natural
> transformation of functors on abelian sheaves.

```lean
public def abelianSpecializationMapOnSections
    (t : GeometricPoint (strictHenselization B S hS s))
    (hT : B.Contains (strictHenselization B S hS s))
    (hU : B.Contains (strictHenselization B S hS
      (t.map (strictHenselizationToBase B S hS s)))) :
    let p : (⟨strictHenselization B S hS s, hT⟩ : B.Scheme) ⟶ (⟨S, hS⟩ : B.Scheme) :=
      ⟨strictHenselizationToBase B S hS s⟩
    haveI := smallEtaleBaseChange_isContinuous B p
    let c : (⟨strictHenselization B S hS
      (t.map (strictHenselizationToBase B S hS s)), hU⟩ : B.Scheme) ⟶
      (⟨strictHenselization B S hS s, hT⟩ : B.Scheme) :=
      ⟨specializationMorphism B S hS s t⟩
    haveI := smallEtaleBaseChange_isContinuous B c
    ((smallEtaleBaseChange B p).sheafPullback Ab.{u + 1}
      (SmallEtale.topology B S hS) (SmallEtale.topology B _ hT) ⋙
      Sheaf.Γ (SmallEtale.topology B _ hT) Ab.{u + 1}) ⟶
    ((smallEtaleBaseChange B p).sheafPullback Ab.{u + 1}
      (SmallEtale.topology B S hS) (SmallEtale.topology B _ hT) ⋙
      ((smallEtaleBaseChange B c).sheafPullback Ab.{u + 1}
        (SmallEtale.topology B _ hT) (SmallEtale.topology B _ hU) ⋙
        Sheaf.Γ (SmallEtale.topology B _ hU) Ab.{u + 1}))
```

**`AlgebraicGeometry.specializationMapOnSections_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationOnSections.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationOnSections.lean#L236). The attribute's comment: “specialization_map_on_sections”.

> The geometric germ of a specialized global section is the pullback of its germ on the first
> strict henselization.

```lean
public theorem specializationMapOnSections_germ
    (t : GeometricPoint (strictHenselization B S hS s))
    (hT : B.Contains (strictHenselization B S hS s))
    (hU : B.Contains (strictHenselization B S hS
      (t.map (strictHenselizationToBase B S hS s))))
    (x : GeometricPoint (strictHenselization B S hS
      (t.map (strictHenselizationToBase B S hS s))))
    (F : Sheaf (SmallEtale.topology B S hS) (Type (u + 1))) :
    let p : (⟨strictHenselization B S hS s, hT⟩ : B.Scheme) ⟶ (⟨S, hS⟩ : B.Scheme) :=
      ⟨strictHenselizationToBase B S hS s⟩
    haveI := smallEtaleBaseChange_isContinuous B p
    let c : (⟨strictHenselization B S hS
      (t.map (strictHenselizationToBase B S hS s)), hU⟩ : B.Scheme) ⟶
      (⟨strictHenselization B S hS s, hT⟩ : B.Scheme) :=
      ⟨specializationMorphism B S hS s t⟩
    haveI := smallEtaleBaseChange_isContinuous B c
    let G := ((smallEtaleBaseChange B p).sheafPullback (Type (u + 1))
      (SmallEtale.topology B S hS)
      (SmallEtale.topology B _ hT)).obj F
    let H := ((smallEtaleBaseChange B c).sheafPullback (Type (u + 1))
      (SmallEtale.topology B _ hT)
      (SmallEtale.topology B _ hU)).obj G
    ∀ σ : (Sheaf.Γ (SmallEtale.topology B _ hT) (Type (u + 1))).obj G,
      ((smallEtalePullbackStalkIso B c x).hom.app G)
        ((globalSectionsToEtaleStalk B
          ↥(etaleLocalRing B S hS (t.map (strictHenselizationToBase B S hS s))) hU x H)
          (specializationMapOnSections B S hS s t hT hU F σ)) =
      (globalSectionsToEtaleStalk B ↥(etaleLocalRing B S hS s) hT
          (x.map (B.inclusion.map c)) G) σ
```

## Tag 0GJ5, a remark

[Tag 0GJ5](https://stacks.math.columbia.edu/tag/0GJ5) in the Stacks Project.

**`AlgebraicGeometry.isSeparable_residueField_strictHenselizationToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationLifting.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationLifting.lean#L101). The attribute's comment: “the residue-field extension”.

> The residue field at a point of the strict henselization at a geometric point is separable
> over the residue field at the image of that point in the scheme.

```lean
public theorem isSeparable_residueField_strictHenselizationToBase (sbar : GeometricPoint S)
    (x : strictHenselization B S hS sbar) :
    let f := strictHenselizationToBase B S hS sbar
    letI := (f.residueFieldMap x).hom.toAlgebra
    Algebra.IsSeparable (S.residueField (f x))
      ((strictHenselization B S hS sbar).residueField x)
```

**`AlgebraicGeometry.exists_lift_toStrictHenselization_of_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationLifting.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationLifting.lean#L149). The attribute's comment: “lifting the generic geometric point”.

> A geometric point over a generization lifts to the strict henselization at a geometric point
> over the specialization, and the lifted point specializes to the canonical point of the strict
> henselization.

```lean
public theorem exists_lift_toStrictHenselization_of_specializes
    (t s : S) (hts : t ⤳ s) (tbar sbar : GeometricPoint S)
    (ht : tbar.LiesOver t) (hs : sbar.LiesOver s) :
    ∃ lift : tbar.source ⟶ strictHenselization B S hS sbar,
      (lift ≫ strictHenselizationToBase B S hS sbar = tbar.hom) ∧
      (lift default ⤳ (geometricPointToStrictHenselization B S hS sbar) default)
```

Declarations registered for the tag:

- [`geometricPointToStrictHenselization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=geometricPointToStrictHenselization#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationLifting.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationLifting.lean#L233) (StacksFrontier): “the special geometric point”.
- [`geometricPointToStrictHenselization_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=geometricPointToStrictHenselization_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationLifting.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HenselianRings/SpecializationLifting.lean#L235) (StacksFrontier): “compatibility of the special geometric point”.

## Tag 0GJ6, a lemma

[Tag 0GJ6](https://stacks.math.columbia.edu/tag/0GJ6) in the Stacks Project.

**`AlgebraicGeometry.specializationMapOnStalks_smallEtalePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/Specialization.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/Specialization.lean#L303).

> **Stacks Project, Tag 0GJ6.** Let `g : S' ⟶ S` be a morphism of schemes, let `s'` be a
> geometric point of `S'` and let `σ` be a geometric specialization of `s'`, and let `h` be the
> canonical morphism of strict henselizations, characterized by lying over `g` and carrying the
> canonical geometric point of its source to the canonical geometric point of its target. For a
> sheaf `F` on the small étale site of `S` the specialization map of the inverse image `g⁻¹F`
> from `s'` to `σ` is the specialization map of `F` from the image of `s'` to the image of `σ`,
> under the identification of the stalks of an inverse image with the stalks of `F`.

```lean
public theorem specializationMapOnStalks_smallEtalePullback (B : BigEtaleSite.{u})
    (S S' : B.Scheme) (g : S' ⟶ S) (s' : GeometricPoint S'.1)
    (σ : GeometricSpecialization B S'.1 S'.property s')
    (h : strictHenselization B S'.1 S'.property s' ⟶
      strictHenselization B S.1 S.property (s'.map (B.inclusion.map g)))
    (hbase : h ≫ strictHenselizationToBase B S.1 S.property (s'.map (B.inclusion.map g)) =
      strictHenselizationToBase B S'.1 S'.property s' ≫ B.inclusion.map g)
    (hpoint : geometricPointToStrictHenselization B S'.1 S'.property s' ≫ h =
      geometricPointToStrictHenselization B S.1 S.property (s'.map (B.inclusion.map g)))
    (F : Sheaf (SmallEtale.topology B S.1 S.property) (Type (u + 1))) :
    specializationMapOnStalks σ
          (((smallEtaleBaseChange B g).sheafPullback (Type (u + 1))
            (SmallEtale.topology B S.1 S.property)
            (SmallEtale.topology B S'.1 S'.property)).obj F).obj ≫
        (smallEtalePullbackStalkIso B g σ.target).hom.app F =
      (smallEtalePullbackStalkIso B g s').hom.app F ≫
        specializationMapOnStalks (σ.map g h hbase) F.obj
```

## Tag 0GJ7, a lemma

[Tag 0GJ7](https://stacks.math.columbia.edu/tag/0GJ7) in the Stacks Project.

**`AlgebraicGeometry.isFiniteLocallyConstant_iff_finite_etaleStalk_and_bijective_specializationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SpecializationFiniteLocallyConstant.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SpecializationFiniteLocallyConstant.lean#L236). References: SGA 4 IX (2.13), “(i), special case”.

> Let `S` be a scheme every quasi-compact open of which has finitely many irreducible components
> and let `F` be a sheaf of sets on the small étale site of `S`. Then `F` is finite locally constant
> if and only if all its stalks at geometric points are finite and all specialization maps between
> those stalks are bijective.

```lean
public theorem isFiniteLocallyConstant_iff_finite_etaleStalk_and_bijective_specializationMap
    (hScomp : ∀ V : S.Opens, IsCompact (V : Set S) → (irreducibleComponents V).Finite)
    (F : Sheaf (SmallEtale.topology B S hS) (Type (u + 1))) :
    Stacks.ConstantSheaf.IsFiniteLocallyConstant (SmallEtale.topology B S hS) F ↔
      (∀ s : GeometricPoint S, Finite (etaleStalk B S hS s F.obj)) ∧
        ∀ (s : GeometricPoint S) (σ : GeometricSpecialization B S hS s),
          Function.Bijective (specializationMapOnStalks σ F.obj)
```

## Tag 0GKC, a lemma

[Tag 0GKC](https://stacks.math.columbia.edu/tag/0GKC) in the Stacks Project.

**`AlgebraicGeometry.isFG_etaleStalk_of_isFiniteTypeLocallyConstantModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SpecializationFiniteTypeLocallyConstantModule.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SpecializationFiniteTypeLocallyConstantModule.lean#L263). The attribute's comment: “(1) ⟹ (2), the stalks are finite modules”.

> **Stacks Project, Tag 0GKC, the implication (1) ⟹ (2), first half.** The stalk at a
> geometric point of a finite type locally constant sheaf of `Λ`-modules on the small étale site
> of a scheme is a finitely generated `Λ`-module.

```lean
public theorem isFG_etaleStalk_of_isFiniteTypeLocallyConstantModuleSheaf
    (F : Sheaf (SmallEtale.topology B S hS) (ModuleCat.{max (u + 1) r} Λ))
    (hF : IsFiniteTypeLocallyConstantModuleSheaf.{u, u + 1, r}
      (SmallEtale.topology B S hS) Λ F)
    (s : GeometricPoint S) :
    ModuleCat.isFG Λ (etaleStalk B S hS s F.obj)
```

**`AlgebraicGeometry.bijective_specializationMapOnStalks_of_isFiniteTypeLocallyConstantModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SpecializationFiniteTypeLocallyConstantModule.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SpecializationFiniteTypeLocallyConstantModule.lean#L278). The attribute's comment: “(1) ⟹ (2), the specialization maps are bijective”. References: SGA 4 IX (2.13), “(i)”.

> **Stacks Project, Tag 0GKC, the implication (1) ⟹ (2), second half.** Every specialization
> map between stalks of a finite type locally constant sheaf of `Λ`-modules on the small étale
> site of a scheme is bijective.

```lean
public theorem bijective_specializationMapOnStalks_of_isFiniteTypeLocallyConstantModuleSheaf
    (F : Sheaf (SmallEtale.topology B S hS) (ModuleCat.{max (u + 1) r} Λ))
    (hF : IsFiniteTypeLocallyConstantModuleSheaf.{u, u + 1, r}
      (SmallEtale.topology B S hS) Λ F)
    (s : GeometricPoint S) (σ : GeometricSpecialization B S hS s) :
    Function.Bijective (specializationMapOnStalks σ F.obj)
```

**`AlgebraicGeometry.isFiniteTypeLocallyConstantModuleSheaf_iff_stalks_and_specialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SpecializationFiniteTypeLocallyConstantModule.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SpecializationFiniteTypeLocallyConstantModule.lean#L302). The attribute's comment: “the equivalence, with (2) ⟹ (1) carried as the hypothesis `hconverse`”.

> **Stacks Project, Tag 0GKC.** Let `S` be a scheme such that every quasi-compact open of `S`
> has a finite number of irreducible components, let `Λ` be a Noetherian ring and let `F` be a
> sheaf of `Λ`-modules on the small étale site of `S`. Then `F` is a finite type locally constant
> sheaf of `Λ`-modules if and only if all its stalks at geometric points are finite, i.e.
> finitely generated, `Λ`-modules and all specialization maps between stalks are bijective.
>
> The implication (1) ⟹ (2) is proved here, using neither `hqc` nor the Noetherian hypothesis
> on `Λ`. The converse implication (2) ⟹ (1) is **not** proved: it is carried as the
> explicit hypothesis `hconverse`, which is the only use made of `hqc` and of
> `IsNoetherianRing Λ`. See the implementation notes of this file for what its proof needs.

```lean
public theorem isFiniteTypeLocallyConstantModuleSheaf_iff_stalks_and_specialization
    [IsNoetherianRing Λ]
    (hqc : ∀ V : S.Opens, IsCompact (V : Set S) → (irreducibleComponents V).Finite)
    (F : Sheaf (SmallEtale.topology B S hS) (ModuleCat.{max (u + 1) r} Λ))
    (hconverse : (∀ V : S.Opens, IsCompact (V : Set S) → (irreducibleComponents V).Finite) →
      (∀ s : GeometricPoint S, ModuleCat.isFG Λ (etaleStalk B S hS s F.obj)) →
      (∀ (s : GeometricPoint S) (σ : GeometricSpecialization B S hS s),
        Function.Bijective (specializationMapOnStalks σ F.obj)) →
      IsFiniteTypeLocallyConstantModuleSheaf.{u, u + 1, r}
        (SmallEtale.topology B S hS) Λ F) :
    IsFiniteTypeLocallyConstantModuleSheaf.{u, u + 1, r} (SmallEtale.topology B S hS) Λ F ↔
      (∀ s : GeometricPoint S, ModuleCat.isFG Λ (etaleStalk B S hS s F.obj)) ∧
        ∀ (s : GeometricPoint S) (σ : GeometricSpecialization B S hS s),
          Function.Bijective (specializationMapOnStalks σ F.obj)
```

**`AlgebraicGeometry.isFiniteTypeLocallyConstantModuleSheaf_iff_isFG_etaleStalk_and_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SpecializationFiniteTypeLocallyConstantModuleConverse.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SpecializationFiniteTypeLocallyConstantModuleConverse.lean#L217). References: SGA 4 IX (2.13), “(i), special case”.

> **Stacks Project, Tag 0GKC.** Let `S` be a scheme such that every quasi-compact open of `S`
> has a finite number of irreducible components, let `Λ` be a Noetherian ring and let `F` be a
> sheaf of `Λ`-modules on the small étale site of `S`. Then `F` is a finite type locally constant
> sheaf of `Λ`-modules if and only if all its stalks at geometric points are finite, i.e.
> finitely generated, `Λ`-modules and all specialization maps between stalks are bijective.

```lean
public theorem isFiniteTypeLocallyConstantModuleSheaf_iff_isFG_etaleStalk_and_bijective
    [IsNoetherianRing Λ]
    (hqc : ∀ V : S.Opens, IsCompact (V : Set S) → (irreducibleComponents V).Finite)
    (F : Sheaf (SmallEtale.topology B S hS) (ModuleCat.{max (u + 1) r} Λ)) :
    IsFiniteTypeLocallyConstantModuleSheaf.{u, u + 1, r} (SmallEtale.topology B S hS) Λ F ↔
      (∀ s : GeometricPoint S, ModuleCat.isFG Λ (etaleStalk B S hS s F.obj)) ∧
        ∀ (s : GeometricPoint S) (σ : GeometricSpecialization B S hS s),
          Function.Bijective (specializationMapOnStalks σ F.obj)
```

## Tag 0GJ8, a lemma

[Tag 0GJ8](https://stacks.math.columbia.edu/tag/0GJ8) in the Stacks Project.

**`AlgebraicGeometry.pushforwardStalkToStrictHenselizationSectionsAb_comp_sectionsRestrictionAb`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedPushforwardStalkSpecialization.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedPushforwardStalkSpecialization.lean#L589). The attribute's comment: “the square for an abelian sheaf `F`, in place of an object `K` of `D⁺(X_étale)`: the vertical identifications are those of Stacks 0GIX rather than their derived counterparts”.

> **The square on abelian sheaves.** The map `(f_*F)_s ⟶ Γ(X ×_S Spec(𝒪^{sh}_{S,s}), p⁻¹F)`
> of Stacks 0GIX at `s`, followed by restriction of sections along `id_X × c`, is the
> specialization map `sp : (f_*F)_s ⟶ (f_*F)_{t ≫ p}` followed by the same map at `t ≫ p`.
>
> Both sides are maps out of the stalk at `s` of the direct image, so it suffices to compare them
> on the germ of a section over an étale neighbourhood `(V, w)` of `s`; there both are restriction
> along `X ×_S Spec(𝒪^{sh}_{S,t ≫ p}) ⟶ X ×_S V` of the corresponding section of `F` over
> `X ×_S V`, the two morphisms agreeing because `c` carries the canonical morphism from the strict
> henselization into `V` to the one for the specialized neighbourhood.

```lean
theorem pushforwardStalkToStrictHenselizationSectionsAb_comp_sectionsRestrictionAb :
    pushforwardStalkToStrictHenselizationSectionsAb B hS f s ≫
        smallEtaleSectionsRestrictionAb (strictHenselizationBaseChangeToSource B hS f s)
          (strictHenselizationBaseChangeSpecializationMap B hS f s t)
          (strictHenselizationBaseChangeToSource B hS f
            (t.map (strictHenselizationToBase B S hS s)))
          (strictHenselizationBaseChangeSpecializationMap_comp_toSource B hS f s t) =
      Functor.whiskerLeft (smallEtalePushforwardAb f)
          (smallEtaleSpecializationStalkAb B S hS s t) ≫
        pushforwardStalkToStrictHenselizationSectionsAb B hS f
          (t.map (strictHenselizationToBase B S hS s))
```

**`AlgebraicGeometry.specializationStalk_comp_derivedPushforwardStalkToStrictHenselizationSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SpecializationMapAndFibres.lean, line 939](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SpecializationMapAndFibres.lean#L939). The attribute's comment: “the square, with `sp` on top and the maps of Stacks 0GIX as its verticals, proved for an arbitrary morphism of schemes and an arbitrary object of `D(X_etale)`”.

> For `K` in `D(X_etale)`, the square whose top arrow is the specialization map `sp` on the
> stalk of `Rf_*K` and whose verticals are the maps of Stacks 0GIX from those stalks to the global
> sections over the base changes to the strict henselizations commutes, its bottom arrow being
> pullback along `id_X × c`.  The verticals are the identifications of Theorem 03Q9 when `f` is
> quasi-compact and quasi-separated and `K` is bounded below; the square commutes for an arbitrary
> morphism of schemes and an arbitrary object of `D(X_etale)`.  It is the square of
> `derivedPushforwardStalkToStrictHenselizationSections_comp_sectionsSpecialization` read with
> `sp` on top.

```lean
theorem specializationStalk_comp_derivedPushforwardStalkToStrictHenselizationSections :
    Functor.whiskerLeft (smallEtaleDerivedPushforwardAb f)
          (smallEtaleDerivedSpecializationStalkAbAt B S hS s t) ≫
        derivedPushforwardStalkToStrictHenselizationSections B hS f
          (specializedGeometricPoint B S hS s t) =
      derivedPushforwardStalkToStrictHenselizationSections B hS f s ≫
        strictHenselizationSectionsSpecializationAt B hS f s t
```

## Tag 0GJ9, a remark

[Tag 0GJ9](https://stacks.math.columbia.edu/tag/0GJ9) in the Stacks Project.

**`AlgebraicGeometry.derivedPushforwardStalkToStrictHenselizationSections_comp_sectionsSpecialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SpecializationMapAndFibres.lean, line 896](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SpecializationMapAndFibres.lean#L896). The attribute's comment: “the left square, whose verticals are the specialization map `sp` and pullback along `id_X × c`; the source states that in general no vertical map exists between the cohomologies of `K` on the two fibres, so the right-hand column carries no square”.

> **Stacks 0GJ9.** For `K` in `D(X_etale)` the specialization map on the stalk of `Rf_*K` at a
> geometric point `s` of `S`, and pullback along `id_X × c` on global sections over the base change
> to the strict henselization, form a commutative square with the two maps of Stacks 0GIX from
> those stalks.
>
> Read with `sp` vertical this is the left square of the diagram of Stacks 0GJ9; read with `sp`
> horizontal it is the square of Stacks 0GJ8, which is
> `AlgebraicGeometry.specializationStalk_comp_derivedPushforwardStalkToStrictHenselizationSections`.
> It is proved here for an arbitrary morphism of schemes and an arbitrary object of `D(X_etale)`,
> which is the generality Stacks 0GJ9 asserts it in.

```lean
theorem derivedPushforwardStalkToStrictHenselizationSections_comp_sectionsSpecialization :
    derivedPushforwardStalkToStrictHenselizationSections B hS f s ≫
        strictHenselizationSectionsSpecializationAt B hS f s t =
      Functor.whiskerLeft (smallEtaleDerivedPushforwardAb f)
          (smallEtaleDerivedSpecializationStalkAbAt B S hS s t) ≫
        derivedPushforwardStalkToStrictHenselizationSections B hS f
          (specializedGeometricPoint B S hS s t)
```

**`AlgebraicGeometry.derivedPushforwardStalkToStrictHenselizationSections_comp_sectionsSpecialization_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SpecializationMapAndFibresUnconditional.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SpecializationMapAndFibresUnconditional.lean#L64). The attribute's comment: “the left square for an arbitrary morphism of schemes and an arbitrary object of the unbounded `D(X_etale)`: its verticals are `sp` and pullback along `id_X × c`, its horizontals the maps of Stacks 0GIX, and the unbounded `Rf_*` and `RΓ` are built from K-injective resolutions; the source states that no vertical map exists in general between the cohomologies of `K` on the two fibres, so the right-hand column carries no square”.

> Let `f : X ⟶ S` be a morphism of schemes, `s` a geometric point of `S` and `t` a geometric
> point of the strict henselization of `S` at `s`. For `K` in the unbounded derived category
> `D(X_étale)`, the maps of Stacks 0GIX from the stalks of `Rf_*K` at `s` and at the specialized
> point `t ≫ p` to the derived global sections over the base changes of `X` to the two strict
> henselizations form a commutative square with the specialization map `sp` on the left and pullback
> along `id_X × c` on the right.

```lean
theorem derivedPushforwardStalkToStrictHenselizationSections_comp_sectionsSpecialization_unconditional
    (B : BigEtaleSite.{u}) {X S : Scheme.{u}} (hS : B.Contains S) (f : X ⟶ S)
    (s : GeometricPoint S) (t : GeometricPoint (strictHenselization B S hS s)) :
    derivedPushforwardStalkToStrictHenselizationSections B hS f s ≫
        strictHenselizationSectionsSpecializationAt B hS f s t =
      Functor.whiskerLeft (smallEtaleDerivedPushforwardAb f)
          (smallEtaleDerivedSpecializationStalkAbAt B S hS s t) ≫
        derivedPushforwardStalkToStrictHenselizationSections B hS f
          (specializedGeometricPoint B S hS s t)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.75, Tag 0GJ2](https://stacks.math.columbia.edu/tag/0GJ2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
