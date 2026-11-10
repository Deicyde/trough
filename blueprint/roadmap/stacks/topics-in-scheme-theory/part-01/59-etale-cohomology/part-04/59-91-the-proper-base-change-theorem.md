---
declaration: section
origin: cited
lean: AlgebraicGeometry.bijective_globalSectionsRestriction_closedFibre_of_henselianPair_of_isProper, Stacks.EtaleCohomology.isIso_globalSectionsComparison_closedFibre_of_henselianPair_of_isProper, Stacks.EtaleCohomology.bijective_globalSectionsComparison_app_closedFibre_of_henselianPair_of_isProper, Stacks.EtaleCohomology.isIso_globalSectionsComparison_closedFibre_of_isProper, Stacks.EtaleCohomology.bijective_globalSectionsComparison_app_closedFibre_of_isProper, Stacks.EtaleCohomology.pushforwardSheafFiberClosedPointIsoGeometricFibreGamma, Stacks.EtaleCohomology.isIso_properGeometricFibreComparison_of_isProper, Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_isProper
statement: formalized
proof: formalized
---

# 59.91 The proper base change theorem

Section 59.91 of the Stacks Project, [Tag 095S](https://stacks.math.columbia.edu/tag/095S). 15 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A0B, a lemma

[Tag 0A0B](https://stacks.math.columbia.edu/tag/0A0B) in the Stacks Project.

**`AlgebraicGeometry.bijective_globalSectionsRestriction_closedFibre_of_henselianPair_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ClosedFibreGlobalSections.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ClosedFibreGlobalSections.lean#L223).

> For `(A, I)` a henselian pair and `f : X ⟶ Spec A` proper, restriction to the closed fibre
> `X ×_{Spec A} Spec (A ⧸ I)` is bijective on global sections of every sheaf of sets on the space
> of `X`.

```lean
theorem bijective_globalSectionsRestriction_closedFibre_of_henselianPair_of_isProper
    (A : Type u) [CommRing A] (I : Ideal A) (hI : HenselianPair A I) {X : Scheme.{u}}
    (f : X ⟶ Spec (.of A)) [IsProper f]
    (F : TopCat.Sheaf (Type u) (TopCat.of X)) :
    Function.Bijective (Stacks.globalSectionsRestriction
      (Set.range (pullback.fst f (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))))) F)
```

## Tag 0A0C, a lemma

[Tag 0A0C](https://stacks.math.columbia.edu/tag/0A0C) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_globalSectionsComparison_closedFibre_of_henselianPair_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ClosedFibreEtaleSectionsProper.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ClosedFibreEtaleSectionsProper.lean#L119). References: SGA 4 XII (6.13), “partial, special case”.

> **[Stacks, Tag 0A0C].** Let `(A, I)` be a henselian pair and let `f : X ⟶ Spec A` be proper.
> For every sheaf of sets `ℱ` on the small étale site of `X`, restriction of global sections to the
> closed fibre `Z = X ×_{Spec A} Spec (A ⧸ I)` is bijective: the canonical comparison
> `Γ(X, ℱ) ⟶ Γ(Z, i_{small}^{-1}ℱ)`, natural in `ℱ`, is an isomorphism.
>
> This is [Stacks, Tag 09ZF] for the closed immersion `i : Z ⟶ X`, whose two hypotheses are
> [Stacks, Tag 0A0B] for `f` and for `Y ⟶ X ⟶ Spec A`, `Y ⟶ X` finite.

```lean
public theorem isIso_globalSectionsComparison_closedFibre_of_henselianPair_of_isProper :
    IsIso (globalSectionsSmallEtaleInverseImageComparison.{u, v}
      (pullback.fst f (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))))).val
```

**`Stacks.EtaleCohomology.bijective_globalSectionsComparison_app_closedFibre_of_henselianPair_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ClosedFibreEtaleSectionsProper.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ClosedFibreEtaleSectionsProper.lean#L137). References: SGA 4 XII (6.13), “partial, special case”.

> **[Stacks, Tag 0A0C], sheaf by sheaf.** Let `(A, I)` be a henselian pair and let
> `f : X ⟶ Spec A` be proper. For every sheaf of sets `ℱ` on the small étale site of `X`, the
> restriction map `Γ(X, ℱ) ⟶ Γ(Z, i_{small}^{-1}ℱ)` to the closed fibre
> `Z = X ×_{Spec A} Spec (A ⧸ I)` is bijective. This is the component at `ℱ` of
> `isIso_globalSectionsComparison_closedFibre_of_henselianPair_of_isProper`.

```lean
public theorem bijective_globalSectionsComparison_app_closedFibre_of_henselianPair_of_isProper
    (F : Sheaf (Scheme.smallEtaleTopology X) (Type (max (u + 1) v))) :
    Function.Bijective ((globalSectionsSmallEtaleInverseImageComparison.{u, v}
      (pullback.fst f (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))))).val.app F)
```

## Tag 0A3S, a lemma

[Tag 0A3S](https://stacks.math.columbia.edu/tag/0A3S) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_globalSectionsComparison_closedFibre_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ClosedFibreEtaleSectionsProper.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ClosedFibreEtaleSectionsProper.lean#L152). References: SGA 4 XII (6.13), “special case”.

> **[Stacks, Tag 0A3S].** Let `A` be a henselian local ring, let `f : X ⟶ Spec A` be proper
> and let `X₀ = X ×_{Spec A} Spec κ(A)` be the fibre of `f` over the closed point. For every sheaf of
> sets `ℱ` on the small étale site of `X`, `Γ(X, ℱ) = Γ(X₀, ℱ|_{X₀})`: the canonical comparison of
> global sections along the inclusion of `X₀`, natural in `ℱ`, is an isomorphism.
>
> This is [Stacks, Tag 0A0C] for the henselian pair `(A, 𝔪)`.

```lean
public theorem isIso_globalSectionsComparison_closedFibre_of_isProper [HenselianLocalRing A] :
    IsIso (globalSectionsSmallEtaleInverseImageComparison.{u, v}
      (closedFibreInclusion A f)).val
```

**`Stacks.EtaleCohomology.bijective_globalSectionsComparison_app_closedFibre_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ClosedFibreEtaleSectionsProper.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ClosedFibreEtaleSectionsProper.lean#L165).

> **[Stacks, Tag 0A3S], sheaf by sheaf.** Let `A` be a henselian local ring, let
> `f : X ⟶ Spec A` be proper and let `X₀ = X ×_{Spec A} Spec κ(A)` be the fibre over the closed
> point. For every sheaf of sets `ℱ` on the small étale site of `X`, restriction of global sections
> `Γ(X, ℱ) ⟶ Γ(X₀, ℱ|_{X₀})` is bijective. This is the component at `ℱ` of
> `isIso_globalSectionsComparison_closedFibre_of_isProper`.

```lean
public theorem bijective_globalSectionsComparison_app_closedFibre_of_isProper
    [HenselianLocalRing A] (F : Sheaf (Scheme.smallEtaleTopology X) (Type (max (u + 1) v))) :
    Function.Bijective ((globalSectionsSmallEtaleInverseImageComparison.{u, v}
      (closedFibreInclusion A f)).val.app F)
```

## Tag 0A3T, a lemma

[Tag 0A3T](https://stacks.math.columbia.edu/tag/0A3T) in the Stacks Project.

**`Stacks.EtaleCohomology.pushforwardSheafFiberClosedPointIsoGeometricFibreGamma`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/GeometricFibreSections.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/GeometricFibreSections.lean#L494). The attribute's comment: “conditional on the base being `Spec R` for a strictly henselian local ring `R`, the reduction of a general base to the strict henselization being Tag 03Q9 for sheaves of sets, which is absent; and carrying `hcompat`, the hypothesis of the library's Tag 0A3S”.

> **The stalk of a direct image along a proper morphism over a strictly henselian local base is
> the set of global sections over the geometric fibre**, granted compatible presenting families.
> For `R` strictly henselian local with residue field `κ(R)`, `f : X ⟶ Spec R` proper, `Ω` an
> extension of `κ(R)` and `x` a geometric point of `Spec R` above the closed point,
> `(f_*F)_x = Γ(X_Ω, F|_{X_Ω})` with `X_Ω = (X ×_{Spec R} Spec κ(R)) ×_{Spec κ(R)} Spec Ω`,
> naturally in the sheaf of sets `F`.
>
> This is the whole of the proof of [Stacks, Tag 0A3T] except for the reduction of a general base
> to the strict henselization, which is Tag 03Q9 and is absent: Tag 03Q9 over the already strictly
> henselian base is `pushforwardSheafFiberClosedPointIsoGamma`, Tag 0A3S is the hypothesis
> `hcompat`, and the extension of the separably closed residue field to `Ω` is [Stacks, Tag 0A3I].
> That the right-hand side is the geometric fibre of `f` at `x` is
> `closedFibreBaseChange_fst_comp_closedFibreInclusion`, for `x` the composite point.

```lean
def pushforwardSheafFiberClosedPointIsoGeometricFibreGamma [IsProper f]
    (hcompat : ∀ (F : Sheaf (Scheme.smallEtaleTopology X) (Type (max (u + 1) v)))
      (t : ((smallEtaleInverseImage.{u, v} (closedFibreInclusion R f)).obj F).obj.obj
        (op (terminal (closedFibre R f).Etale))),
      ∃ (α : Type (u + 1)) (W : α → X.Etale) (s : ∀ j, F.obj.obj (op (W j))),
        (⨆ j, smallEtaleImage (W j)) = ⊤ ∧ SmallEtaleCompatible F W s ∧
          ∀ j, ((smallEtaleInverseImage.{u, v} (closedFibreInclusion R f)).obj F).obj.map
                (terminal.from ((smallEtaleBaseChange
                  (closedFibreInclusion R f)).obj (W j))).op t
              = smallEtaleSectionPullback.{u, v} (closedFibreInclusion R f) F (W j) (s j)) :
    (smallEtaleBaseChange f).sheafPushforwardContinuous (Type (max (u + 1) v))
          (smallEtaleTopology (Spec (.of R))) (smallEtaleTopology X) ⋙
        (pointSmallEtale x).sheafFiber ≅
      smallEtaleInverseImage.{u, v}
          (pullback.fst (closedFibreProjection R f)
            (Spec.map (CommRingCat.ofHom
              (algebraMap (IsLocalRing.ResidueField R) Ω))) ≫ closedFibreInclusion R f) ⋙
        Sheaf.Γ (smallEtaleTopology (pullback (closedFibreProjection R f)
          (Spec.map (CommRingCat.ofHom (algebraMap (IsLocalRing.ResidueField R) Ω)))))
          (Type (max (u + 1) v))
```

Declarations registered for the tag:

- [`Stacks.EtaleCohomology.isIso_properGeometricFibreComparison_of_isProper`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperPushforwardBaseChangeUnconditional.lean#L63), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperBaseChangeStacksTags.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperBaseChangeStacksTags.lean#L47) (StacksFrontier).

## Tag 0A3U, a lemma

[Tag 0A3U](https://stacks.math.columbia.edu/tag/0A3U) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_isProper`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperPushforwardBaseChangeUnconditional.lean#L42), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperBaseChangeStacksTags.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperBaseChangeStacksTags.lean#L49) (StacksFrontier).

## Tag 0A2A, an equation

[Tag 0A2A](https://stacks.math.columbia.edu/tag/0A2A) in the Stacks Project.

**`Stacks.EtaleCohomology.etaleAbelianDerivedBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/BaseChangeMap.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/BaseChangeMap.lean#L158).

> The canonical base change map `g^{-1} Rf_* ⟶ Rf'_* (g')^{-1}` on the
> unbounded derived categories of abelian sheaves for the small étale topology, attached to a
> commutative square `g' ≫ f = f' ≫ g` of schemes.

```lean
public def etaleAbelianDerivedBaseChange :
    etaleAbelianDerivedDirectImage.{u, v} f ⋙ etaleAbelianDerivedInverseImage.{u, v} g ⟶
      etaleAbelianDerivedInverseImage.{u, v} g' ⋙ etaleAbelianDerivedDirectImage.{u, v} f'
```

**`Stacks.EtaleCohomology.etaleAbelianDerivedBaseChange_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/BaseChangeMap.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/BaseChangeMap.lean#L241). The attribute's comment: “canonical comparison on unbounded complexes”.

> For every complex `K` of abelian sheaves on `X_étale`, the base change map at the object it
> represents, precomposed with the exactness comparison for `g^{-1}` and with the derived-functor
> unit of `Rf_*`, is the degreewise base change comparison followed by the derived-functor unit
> of `Rf'_*`.

```lean
public theorem etaleAbelianDerivedBaseChange_fac :
    (etaleAbelianInverseImage.{u, v} g).mapDerivedCategoryFactorsh.inv.app
        (((etaleAbelianDirectImage.{u, v} f).mapHomotopyCategory
          (ComplexShape.up ℤ)).obj K) ≫
      (etaleAbelianDerivedInverseImage.{u, v} g).map
        ((etaleAbelianDerivedDirectImageUnit.{u, v} f).app K) ≫
      (etaleAbelianDerivedBaseChange.{u, v} f g g' f' h).app (DerivedCategory.Qh.obj K) =
    DerivedCategory.Qh.map ((etaleAbelianHomotopyBaseChange.{u, v} f g g' f' h).app K) ≫
      (etaleAbelianDerivedDirectImageUnit.{u, v} f').app
        (((etaleAbelianInverseImage.{u, v} g').mapHomotopyCategory
          (ComplexShape.up ℤ)).obj K) ≫
      (etaleAbelianDerivedDirectImage.{u, v} f').map
        ((etaleAbelianInverseImage.{u, v} g').mapDerivedCategoryFactorsh.inv.app K)
```

## Tag 0A4A, an equation

[Tag 0A4A](https://stacks.math.columbia.edu/tag/0A4A) in the Stacks Project.

**`Stacks.EtaleCohomology.etaleAbelianSheafDerivedBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/BaseChangeMap.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/BaseChangeMap.lean#L277).

> The base change map for a single abelian sheaf `F` on `X_étale`, placed in
> degree zero: the canonical morphism `g^{-1} Rf_* F ⟶ Rf'_* (g')^{-1} F` in the derived category
> of `Y'_étale`, attached to a commutative square `g' ≫ f = f' ≫ g` of schemes. It is the
> component of `Stacks.EtaleCohomology.etaleAbelianDerivedBaseChange` at `F[0]`.

```lean
public def etaleAbelianSheafDerivedBaseChange
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) :
    (etaleAbelianDerivedInverseImage.{u, v} g).obj
        ((etaleAbelianDerivedDirectImage.{u, v} f).obj
          ((DerivedCategory.singleFunctor
            (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) 0).obj F)) ⟶
      (etaleAbelianDerivedDirectImage.{u, v} f').obj
        ((etaleAbelianDerivedInverseImage.{u, v} g').obj
          ((DerivedCategory.singleFunctor
            (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) 0).obj F))
```

## Tag 0A4B, a lemma

[Tag 0A4B](https://stacks.math.columbia.edu/tag/0A4B) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.EtaleCohomology.cohomologyCommutesWithBaseChange_iff_higherDirectImagesVanishOnInjectives`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperPushforwardBaseChangeUnconditional.lean#L74), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperPushforwardBaseChangeRegistration.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperPushforwardBaseChangeRegistration.lean#L15) (StacksFrontier): “(1) cohomology commutes with base change for f iff (2) higher direct images of pulled-back injective Z/lZ-sheaves vanish”.

## Tag 0A4C, a lemma

[Tag 0A4C](https://stacks.math.columbia.edu/tag/0A4C) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_etaleAbelianBaseChange_of_mono_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/SurjectiveCancellation.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/SurjectiveCancellation.lean#L297). The attribute's comment: “RESTRICTED: degree zero only — each `cohomology commutes with base change` is invertibility of the underived comparison of Tag 0A2A at every abelian sheaf, not of the derived comparison at every torsion sheaf, the bridge between the two being Tag 0A4B, absent here; hypothesis (3) is carried as monomorphy of the unit `A ⟶ f_*f⁻¹A`, which `mono_etaleAbelianUnit_of_surjective` supplies from `Surjective f`; properness is unused”.

> **Stacks 0A4C in degree zero: cancelling a surjection from a composite.**  Let `f : X ⟶ Y`
> and `g : Y ⟶ Z` be morphisms of schemes with named composite `gf : X ⟶ Z`, let `c : Z' ⟶ Z`, and
> consider commutative squares
> ```
> X' --e--> X      Y' --d--> Y
> |f'       |f     |g'       |g
> v         v      v         v
> Y' --d--> Y      Z' --c--> Z
> ```
> with `q : X' ⟶ Z'` the named composite of `f'` and `g'`.  Assume
>
> 1. the comparison `d^{-1} f_* ⟶ f'_* e^{-1}` of the upper square is invertible at every abelian
>    sheaf on `X_étale`;
> 2. the comparison `c^{-1} (gf)_* ⟶ q_* e^{-1}` of the rectangle is invertible at every abelian
>    sheaf on `X_étale`;
> 3. the unit `A ⟶ f_* f^{-1} A` is a monomorphism for every abelian sheaf `A` on `Y_étale`.
>
> Then the comparison `c^{-1} g_* ⟶ g'_* d^{-1}` of the lower square is invertible at every
> abelian sheaf on `Y_étale`.
>
> Hypothesis 3 is what surjectivity of `f` provides:
> `Stacks.EtaleCohomology.mono_etaleAbelianUnit_of_surjective` proves it from `Surjective f` at
> the coefficients `Ab.{u + 1}`.  Properness of `f` and `g` is not used.

```lean
public theorem isIso_etaleAbelianBaseChange_of_mono_unit
    (f : X ⟶ Y) (g : Y ⟶ Z) (gf : X ⟶ Z) (hgf : gf = f ≫ g)
    (c : Z' ⟶ Z) (d : Y' ⟶ Y) (g' : Y' ⟶ Z') (e : X' ⟶ X) (f' : X' ⟶ Y')
    (q : X' ⟶ Z') (hq : q = f' ≫ g')
    (sq₁ : d ≫ g = g' ≫ c) (sq₂ : e ≫ f = f' ≫ d) (hyp : e ≫ gf = q ≫ c)
    (hunit : ∀ A : Sheaf Y.smallEtaleTopology AddCommGrpCat.{max (u + 1) v},
      Mono ((etaleAbelianInverseImageDirectImageAdj.{u, v} f).unit.app A))
    (h₁ : ∀ F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v},
      IsIso ((etaleAbelianBaseChange.{u, v} f d e f' sq₂).app F))
    (h₂ : ∀ F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v},
      IsIso ((etaleAbelianBaseChange.{u, v} gf c e q hyp).app F))
    (A : Sheaf Y.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) :
    IsIso ((etaleAbelianBaseChange.{u, v} g c d g' sq₁).app A)
```

**`Stacks.EtaleCohomology.CohomologyCommutesWithBaseChange.of_comp_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/SurjectiveCancellationUnconditional.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/SurjectiveCancellationUnconditional.lean#L233).

> **[Stacks, Tag 0A4C]: cancelling a surjection from a composite.** Let `f : X ⟶ Y` and
> `g : Y ⟶ Z` be morphisms of schemes. Assume
>
> 1. cohomology commutes with base change for `f`,
> 2. cohomology commutes with base change for `g ∘ f`, and
> 3. `f` is surjective.
>
> Then cohomology commutes with base change for `g`.
>
> The source assumes `f` and `g` proper; only surjectivity of `f` and quasi-compactness and
> quasi-separatedness of `g` are used, so the statement is proved under those weaker hypotheses (a
> proper morphism is quasi-compact and quasi-separated). Cohomology commuting with base change is
> `Stacks.EtaleCohomology.CohomologyCommutesWithBaseChange`: the derived base change map
> `c⁻¹ Rg_* F ⟶ Rg'_* d⁻¹ F` is an isomorphism for every cartesian square and every torsion abelian
> sheaf `F`, in all degrees at once.

```lean
public theorem CohomologyCommutesWithBaseChange.of_comp_of_surjective (f : X ⟶ Y) (g : Y ⟶ Z)
    [Surjective f] [QuasiCompact g] [QuasiSeparated g]
    (hf : CohomologyCommutesWithBaseChange.{u, v} f)
    (hgf : CohomologyCommutesWithBaseChange.{u, v} (f ≫ g)) :
    CohomologyCommutesWithBaseChange.{u, v} g
```

## Tag 0A4D, a lemma

[Tag 0A4D](https://stacks.math.columbia.edu/tag/0A4D) in the Stacks Project.

**`Stacks.EtaleCohomology.etaleAbelianDerivedBaseChange_isIso_of_compDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/CompositeMorphismBaseChange.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/CompositeMorphismBaseChange.lean#L328). The attribute's comment: “the derived half: for K in D(X\_étale), if c⁻¹Rg\_*(Rf\_*K) → Rg'\_*d⁻¹(Rf\_*K) and d⁻¹Rf\_*K → Rf'\_*e⁻¹K are isomorphisms then c⁻¹R(g∘f)\_*K → R(g'∘f')\_*e⁻¹K is an isomorphism; the R^q statement of the same tag, and the reduction to injective Z/l-modules of 0A4B that the source proof uses to obtain it, are not covered here”.

> **Stacks 0A4D, the derived half.**  Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of schemes
> with named composite `gf : X ⟶ Z`, let `c : Z' ⟶ Z`, and consider commutative squares
> ```
> X' --e--> X      Y' --d--> Y
> |f'       |f     |g'       |g
> v         v      v         v
> Y' --d--> Y      Z' --c--> Z
> ```
> with `q : X' ⟶ Z'` the named composite of `f'` and `g'`.  Let `K` be an object of
> `D(X_étale)`.  If the base change map `c⁻¹ Rg_* ⟶ Rg'_* d⁻¹` of the lower square is an
> isomorphism at `Rf_* K`, and the base change map `d⁻¹ Rf_* ⟶ Rf'_* e⁻¹` of the upper square is
> an isomorphism at `K`, then the base change map `c⁻¹ R(gf)_* K ⟶ Rq_* e⁻¹ K` of the outer
> rectangle is an isomorphism.
>
> This is the composition statement of the source in the derived formulation of
> `Stacks.EtaleCohomology.etaleAbelianDerivedBaseChange`: both hypotheses and conclusion say that
> a base change map of unbounded derived categories is invertible, so no torsion condition is
> imposed on the coefficients.  It is formal, by
> `Stacks.EtaleCohomology.etaleAbelianDerivedBaseChange_compDirectImage_app`, which exhibits the
> map of the rectangle as the composite of the two given maps with two isomorphisms; neither
> square need be cartesian and neither morphism need be proper.

```lean
public theorem etaleAbelianDerivedBaseChange_isIso_of_compDirectImage
    (f : X ⟶ Y) (g : Y ⟶ Z) (gf : X ⟶ Z) (hgf : gf = f ≫ g)
    (c : Z' ⟶ Z) (d : Y' ⟶ Y) (g' : Y' ⟶ Z') (e : X' ⟶ X) (f' : X' ⟶ Y')
    (q : X' ⟶ Z') (hq : q = f' ≫ g')
    (sq₁ : d ≫ g = g' ≫ c) (sq₂ : e ≫ f = f' ≫ d) (hyp : e ≫ gf = q ≫ c)
    (K : DerivedCategory (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}))
    (h₁ : IsIso ((etaleAbelianDerivedBaseChange.{u, v} g c d g' sq₁).app
      ((etaleAbelianDerivedDirectImage.{u, v} f).obj K)))
    (h₂ : IsIso ((etaleAbelianDerivedBaseChange.{u, v} f d e f' sq₂).app K)) :
    IsIso ((etaleAbelianDerivedBaseChange.{u, v} gf c e q hyp).app K)
```

**`Stacks.EtaleCohomology.CohomologyCommutesWithBaseChange.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/CompositeMorphismBaseChangeUnconditional.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/CompositeMorphismBaseChangeUnconditional.lean#L270).

> **[Stacks, Tag 0A4D]: cohomology commutes with base change for a composite.**  Let
> `f : X ⟶ Y` and `g : Y ⟶ Z` be proper morphisms of schemes.  Assume
>
> 1. cohomology commutes with base change for `f`, and
> 2. cohomology commutes with base change for `g`.
>
> Then cohomology commutes with base change for `g ∘ f`.
>
> Cohomology commuting with base change is
> `Stacks.EtaleCohomology.CohomologyCommutesWithBaseChange`: the derived base change map
> `c⁻¹ R(gf)_* F ⟶ Rq_* e⁻¹ F` is an isomorphism for every cartesian square over `g ∘ f` and every
> torsion abelian sheaf `F` on `X_étale`, in all degrees at once.  The proof follows the source: at
> an injective sheaf of `ℤ/nℤ`-modules the composition formula for base change maps reduces the
> statement to the conditions for `f` and `g`
> (`isIso_etaleAbelianSheafDerivedBaseChange_comp_toSheaf_injective`); dimension shifting carries
> it to every sheaf killed by `n`, which is how the source uses Tag 0A4B; and a torsion sheaf is
> the filtered colimit of its subsheaves killed by an integer, with which both sides commute as
> `g ∘ f` is quasi-compact and quasi-separated (Tag 09Z1).

```lean
public theorem CohomologyCommutesWithBaseChange.comp {f : X ⟶ Y} {g : Y ⟶ Z}
    [IsProper f] [IsProper g]
    (hf : CohomologyCommutesWithBaseChange.{u, v} f)
    (hg : CohomologyCommutesWithBaseChange.{u, v} g) :
    CohomologyCommutesWithBaseChange.{u, v} (f ≫ g)
```

## Tag 0A4E, a lemma

[Tag 0A4E](https://stacks.math.columbia.edu/tag/0A4E) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_etaleAbelianSheafDerivedBaseChange_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/AbelianCoefficientTransfer.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/AbelianCoefficientTransfer.lean#L618). The attribute's comment: “RESTRICTED: the cartesian square is carried as four objects and four morphisms of the underlying category of a given big étale site `B`, the conclusion being about their images under `B.inclusion`; that containment is the only hypothesis beyond the square being cartesian with `f` finite, and coefficients are the abelian groups of `AddCommGrpCat.{u+1}`, which is `Ab.{u+1}`. No torsion condition and no invertibility is assumed.”. References: SGA 4 XII (5.1), “(iii)”.

> **Stacks 0A4E: cohomology commutes with base change for a finite morphism.** For a cartesian
> square
>
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
>
> of the underlying category of a big étale site with `f` finite, and every abelian sheaf `F` on
> the small étale site of `X`, the base change map `g^{-1} Rf_* F ⟶ Rf'_* (g')^{-1} F` on
> unbounded derived categories is an isomorphism.
>
> No torsion condition on `F` is imposed — the source states the lemma for torsion sheaves, and
> this is the stronger statement — and finiteness of `f'` is not assumed but obtained from the
> square. The two inputs are
> `Stacks.EtaleCohomology.isIso_etaleAbelianSheafDerivedBaseChange_of_isFinite_of_isIso`, which
> reduces the derived statement to the underived comparison using the vanishing of the positive
> higher direct images of a finite morphism, and
> `Stacks.EtaleCohomology.isIso_etaleAbelianBaseChange_of_isFinite`, which is Stacks 0959 at
> abelian coefficients.

```lean
public theorem isIso_etaleAbelianSheafDerivedBaseChange_of_isFinite
    (sq : IsPullback (B.inclusion.map g') (B.inclusion.map f') (B.inclusion.map f)
      (B.inclusion.map g)) [IsFinite (B.inclusion.map f)]
    (F : Sheaf (Scheme.smallEtaleTopology (B.inclusion.obj X)) AddCommGrpCat.{u + 1}) :
    IsIso (etaleAbelianSheafDerivedBaseChange.{u, 0} (B.inclusion.map f) (B.inclusion.map g)
      (B.inclusion.map g') (B.inclusion.map f') sq.w F)
```

**`Stacks.EtaleCohomology.cohomologyCommutesWithBaseChange_of_isFinite_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/FiniteBaseChangeUniverse.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/FiniteBaseChangeUniverse.lean#L187). References: SGA 4 XII (5.2), “(iii), special case”; SGA 4½ Th finitude (5.1.3), “1.3.1, special case”.

> **Proper base change for finite morphisms.** Cohomology commutes with base change for a finite
> morphism of schemes `f : X ⟶ Y`: for every cartesian square with
> `X' = Y' ×_Y X` and every torsion abelian sheaf `F` on `X_étale`, with values in
> `AddCommGrpCat.{max (u + 1) v}`, the base change map `g⁻¹ Rf_* F ⟶ Rf'_* (g')⁻¹ F` is an
> isomorphism. The torsion hypothesis is not used:
> `isIso_etaleAbelianSheafDerivedBaseChange_of_isFinite_univ` holds at every abelian
> sheaf.

```lean
theorem cohomologyCommutesWithBaseChange_of_isFinite_univ {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsFinite f] :
    CohomologyCommutesWithBaseChange.{u, v} f
```

## Tag 0A4F, a lemma

[Tag 0A4F](https://stacks.math.columbia.edu/tag/0A4F) in the Stacks Project.

**`Stacks.EtaleCohomology.cohomologyCommutesWithBaseChange_of_projectiveLine_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProjectiveLineReductionGeneral.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProjectiveLineReductionGeneral.lean#L197).

> **[Stacks, Tag 0A4F].** To prove that cohomology commutes with base change for every proper
> morphism of schemes it suffices to prove it for the morphism `ℙ¹_S ⟶ S` for every scheme `S`:
> if cohomology commutes with base change for every `ℙ¹_S ⟶ S`, then it does for every proper
> `f`.

```lean
public theorem cohomologyCommutesWithBaseChange_of_projectiveLine_unconditional
    (hline : ∀ S : Scheme.{u},
      CohomologyCommutesWithBaseChange.{u, v} (ProjectiveSpace 1 S ↘ S))
    {X Y : Scheme.{u}} (f : X ⟶ Y) (hf : IsProper f) :
    CohomologyCommutesWithBaseChange.{u, v} f
```

## Tag 095T, a theorem

[Tag 095T](https://stacks.math.columbia.edu/tag/095T) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.EtaleCohomology.isIso_etaleAbelianSheafDerivedBaseChange_of_isProper`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperBaseChangeTheoremUnconditional.lean#L164), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperBaseChangeStacksTags.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperBaseChangeStacksTags.lean#L53) (StacksFrontier).

## Tag 0DDE, a lemma

[Tag 0DDE](https://stacks.math.columbia.edu/tag/0DDE) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_etaleAbelianDerivedBaseChange_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/DerivedProperBaseChange.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/DerivedProperBaseChange.lean#L45). References: SGA 4 XVII (4.3.2), “special case”; SGA 4 XVII (5.2.7), “(ii), special case”.

> **Stacks Project, Tag 0DDE.** Let `f : X ⟶ Y` be a proper morphism of schemes, `g : Y' ⟶ Y`
> a morphism of schemes, and `X' = Y' ×_Y X`, given as a cartesian square `sq` with projections
> `f' : X' ⟶ Y'` and `g' : X' ⟶ X`. Let `E` be an object of the derived category of abelian sheaves
> on `X_étale` which is bounded below and has torsion cohomology sheaves. Then the base change map
> `g^{-1} Rf_* E ⟶ Rf'_* (g')^{-1} E` of Tag 0A2A is an isomorphism.

```lean
theorem isIso_etaleAbelianDerivedBaseChange_of_isProper {X Y X' Y' : Scheme.{u}} (f : X ⟶ Y)
    [IsProper f] {g : Y' ⟶ Y} {g' : X' ⟶ X} {f' : X' ⟶ Y'} (sq : IsPullback g' f' f g)
    (E : DerivedCategory (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})) (n : ℤ)
    (hE : E.IsGE n)
    (hT : Stacks.Torsion.torsionCohomologyProperty.{u + 1} X.smallEtaleTopology E) :
    IsIso ((etaleAbelianDerivedBaseChange.{u, 0} f g g' f' sq.w).app E)
```

## Tag 0DDF, a lemma

[Tag 0DDF](https://stacks.math.columbia.edu/tag/0DDF) in the Stacks Project.

**`Stacks.EtaleCohomology.etaleAbelianSheafFiberRightDerivedDirectImageIsoOfIsProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperGeometricFibreStalk.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperGeometricFibreStalk.lean#L48). The attribute's comment: “part (1)”.

> **Stacks 0DDF (1).** For a proper morphism `f : X ⟶ Y`, a geometric point `ȳ : Spec Ω ⟶ Y`
> and a torsion abelian sheaf `F` on `X_étale`, the stalk of `Rⁿf_* F` at `ȳ` is the étale
> cohomology `Hⁿ(X_ȳ, F_ȳ)` of the restriction of `F` to the geometric fibre `X_ȳ = X ×_Y Spec Ω`.

```lean
def etaleAbelianSheafFiberRightDerivedDirectImageIsoOfIsProper
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty X.smallEtaleTopology F) (n : ℕ) :
    letI := hasExt_sheaf_smallEtale_succ (pullback f y)
    (((pointSmallEtale y).ulift.{u + 1}).sheafFiber (A := AddCommGrpCat.{u + 1})).obj
      (((etaleAbelianDirectImage.{u, 0} f).rightDerived n).obj F) ≅
    AddCommGrpCat.of
      (Sheaf.H.{u + 1} ((etaleAbelianInverseImage.{u, 0} (pullback.fst f y)).obj F) n)
```

**`Stacks.EtaleCohomology.etaleAbelianSheafFiberHomologyDerivedDirectImageIsoOfIsProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperGeometricFibreStalk.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperGeometricFibreStalk.lean#L65). The attribute's comment: “part (2)”.

> **Stacks 0DDF (2).** For a proper morphism `f : X ⟶ Y`, a geometric point `ȳ : Spec Ω ⟶ Y`
> and an object `E` of `D⁺(X_étale)` with torsion cohomology sheaves, the stalk at `ȳ` of the
> `n`-th cohomology sheaf of `Rf_* E` is the `n`-th hypercohomology of the restriction of `E` to
> the geometric fibre `X_ȳ = X ×_Y Spec Ω`.

```lean
def etaleAbelianSheafFiberHomologyDerivedDirectImageIsoOfIsProper
    (E : DerivedCategory (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})) (m : ℤ)
    (hE : E.IsGE m)
    (hT : Stacks.Torsion.torsionCohomologyProperty.{u + 1} X.smallEtaleTopology E) (n : ℤ) :
    letI := isGrothendieckAbelian_sheaf_smallEtale_objectUniverse (pullback f y)
    (((pointSmallEtale y).ulift.{u + 1}).sheafFiber (A := AddCommGrpCat.{u + 1})).obj
      ((DerivedCategory.homologyFunctor (Sheaf Y.smallEtaleTopology AddCommGrpCat.{u + 1})
        n).obj ((etaleAbelianDerivedDirectImage.{u, 0} f).obj E)) ≅
    (DerivedCategory.homologyFunctor AddCommGrpCat.{u + 1} n).obj
      ((Stacks.DerivedFunctor.totalRightDerived
        (Sheaf.Γ (pullback f y).smallEtaleTopology AddCommGrpCat.{u + 1})).obj
        ((etaleAbelianDerivedInverseImage.{u, 0} (pullback.fst f y)).obj E))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.91, Tag 095S](https://stacks.math.columbia.edu/tag/095S)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
