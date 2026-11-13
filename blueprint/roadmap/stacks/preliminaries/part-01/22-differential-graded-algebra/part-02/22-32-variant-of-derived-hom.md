---
declaration: section
origin: cited
lean: CochainComplex.homComplexesFunctorCommShift, DifferentialGradedModule.derivedForgetData, CochainComplex.homHomotopyFunctor_isTriangulated, CochainComplex.homToDerivedCategory_isTriangulated, CochainComplex.derivedHomReflectorFunctor, CochainComplex.homHomotopyFunctorCommShift, CochainComplex.homToDerivedCategoryCommShift, CochainComplex.derivedHomReflectorFunctorIso
statement: formalized
proof: formalized
---

# 22.32 Variant of derived Hom

Section 22.32 of the Stacks Project, [Tag 09LJ](https://stacks.math.columbia.edu/tag/09LJ). 1 tag here is carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09LK, a lemma

[Tag 09LK](https://stacks.math.columbia.edu/tag/09LK) in the Stacks Project.

**`CochainComplex.homComplexesFunctorCommShift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomCommShift.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomCommShift.lean#L88). The attribute's comment: “the functor Hom(K, -) being derived commutes with the translation: the shift comparisons Hom(K, X[n]) = Hom(K, X)[n] are natural in X and compatible with shiftFunctorZero and shiftFunctorAdd, which is the coherence Functor.mapTriangle is formed with”.

> **`Hom(K, -)` commutes with the translation.** The shift comparisons
> `Hom(K, X[n]) ≅ Hom(K, X)[n]` of Tag 09LE are natural in `X` and compatible with
> `CategoryTheory.shiftFunctorZero` and `CategoryTheory.shiftFunctorAdd`, so they make
> `Hom(K, -) : CochainComplex B ℤ ⥤ Mod_{(E, d)}` a functor commuting with the shift by `ℤ`.

```lean
noncomputable instance homComplexesFunctorCommShift :
    (homComplexesFunctor B K).CommShift ℤ
```

**`DifferentialGradedModule.derivedForgetData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomData.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomData.lean#L136). The attribute's comment: “the forgetful functor D(E, d) ⥤ D(Ab) of the conclusion, together with the identification of its value on an ordinary differential graded module with the underlying complex of that module, which is the phrase `on taking associated complexes`”.

> **The forgetful functor datum of Tag 09LK exists**, with no hypothesis beyond a differential
> graded algebra over a commutative ring and a chosen derived category of complexes of modules
> over that ring.
>
> The functor is `DifferentialGradedModule.derivedForget`, the underlying-complex functor descended
> through the quotient by homotopy and then through the localization at the quasi-isomorphisms, and
> the identification is the composite of those two descents,
> `DifferentialGradedModule.derivedForgetFactorization` and
> `DifferentialGradedModule.forgetHomotopyToDerivedCategoryIso`.

```lean
def derivedForgetData : DerivedForgetData A
```

**`CochainComplex.homHomotopyFunctor_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomExactness.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomExactness.lean#L219). The attribute's comment: “the differential graded Hom functor Hom(K, -) : K(B) ⥤ K(E, d) is exact as a functor of triangulated categories -- it commutes with the translation and carries distinguished triangles to distinguished triangles, which is the exactness of the functor being derived read on the homotopy categories”.

> **Stacks 09LK, the exactness of `Hom(K, -)` on the homotopy categories.** The differential
> graded Hom functor `Hom(K, -) : K(B) ⥤ K(E, d)` of Tag 09LE is exact as a functor of triangulated
> categories: it commutes with the translation, which is
> `CochainComplex.homHomotopyFunctorCommShift`, and it carries distinguished triangles to
> distinguished triangles.
>
> This is the exactness asserted by Tag 09LK of the functor being derived, read on the homotopy
> categories. It is obtained from the exactness of the descent of `Hom(K, -)` along the quotient by
> homotopy, transported along `CochainComplex.homHomotopyFunctorLiftIso`.

```lean
noncomputable instance homHomotopyFunctor_isTriangulated :
    (homHomotopyFunctor B K).IsTriangulated
```

**`CochainComplex.homToDerivedCategory_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomExactness.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomExactness.lean#L231). The attribute's comment: “the functor Hom(K, -) : K(B) ⥤ D(E, d) being right derived is exact as a functor of triangulated categories”.

> **Stacks 09LK, the exactness of the functor being right derived.** The functor
> `Hom(K, -) : K(B) ⥤ D(E, d)` of Tag 09LK — the differential graded Hom functor followed by the
> localization of the differential graded `E`-modules at the quasi-isomorphisms — is exact as a
> functor of triangulated categories, the localization functor being exact.

```lean
noncomputable instance homToDerivedCategory_isTriangulated :
    (homToDerivedCategory B K).IsTriangulated
```

**`CochainComplex.derivedHomReflectorFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomFunctorAssembly.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomFunctorAssembly.lean#L243). The attribute's comment: “the functor itself: R Hom(K, -) : D(A) ⥤ D(E, d), for E the endomorphism differential graded category of K”.

> **The functor `R Hom(K, -) : D(A) ⥤ D(E, d)` of [Stacks, Tag 09LK]**, for
> `E = C(K, K)` the endomorphism differential graded category of `K` in `Comp^dg(A)`: the
> reflector-and-descend functor `DGCategory.phiReflector` of steps 1 and 2, taken at the chosen
> witnesses `CochainComplex.derivedHomReflectorL` and `CochainComplex.derivedHomReflector_isZero`.
>
> Deliberately an `abbrev`: the exactness and shift compatibility of `DGCategory.phiReflector`
> (`DGCategory.phiReflectorCommShift`, `DGCategory.phiReflector_isTriangulated`) and the
> identification `(*)` and step 3 at an arbitrary reflector all apply to it after reduction, so
> nothing has to be re-registered or restated at the chosen witnesses — and in particular no second
> `CommShift` term competes with the canonical one.

```lean
abbrev derivedHomReflectorFunctor : DerivedCategory A ⥤
    DGCategory.RightModule.derivedCategory
      (DGCategory.endDGCategory (CochainComplex.dgCategory A) K)
```

**`CochainComplex.homHomotopyFunctorCommShift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomHomotopyCommShift.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomHomotopyCommShift.lean#L195). The attribute's comment: “the differential graded Hom functor Hom(K, -) : K(B) ⥤ K(E, d) commutes with the translation, the shift comparisons of 09LE descending along the quotient by homotopy”.

> **`Hom(K, -) : K(B) ⥤ K(E, d)` commutes with the translation.**

```lean
noncomputable instance homHomotopyFunctorCommShift :
    (homHomotopyFunctor B K).CommShift ℤ
```

**`CochainComplex.homToDerivedCategoryCommShift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomHomotopyCommShift.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomHomotopyCommShift.lean#L202). The attribute's comment: “the functor Hom(K, -) : K(B) ⥤ D(E, d) being right derived commutes with the translation”.

> **The functor being right derived in Tag 09LK commutes with the translation.**

```lean
noncomputable instance homToDerivedCategoryCommShift :
    (homToDerivedCategory B K).CommShift ℤ
```

**`CochainComplex.derivedHomReflectorFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomReflectorCanonical.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomReflectorCanonical.lean#L188). The attribute's comment: “canonicity of R Hom(K, -) : D(A) ⥤ D(E, d): the functor is independent of the reflector used to construct it, up to the isomorphism induced by the unique isomorphism of reflectors compatible with the units”.

> **The functor `R Hom(K, -) : D(A) ⥤ D(E, d)` of [Stacks, Tag 09LK] is canonical.** Let `L'`
> be any exact reflector on `K(Mod^dg(Comp^dg A))` with a unit `η'` satisfying the clauses of
> steps 1 and 2: every `L' X` is local, the cone of every `η'.app X` lies in `N`, and `L'` kills
> the preimage of `N`. Then the functor `DGCategory.phiReflector` built from `L'` is isomorphic to
> `CochainComplex.derivedHomReflectorFunctor`, through the isomorphism of reflectors
> `CategoryTheory.ObjectProperty.reflectorIsoOfUnits`, which is the unique one compatible with the
> units (`CategoryTheory.ObjectProperty.eq_reflectorIsoOfUnits`).

```lean
def derivedHomReflectorFunctorIso
    (L' : derivedHomModuleK A ⥤ derivedHomModuleK A)
    [L'.CommShift ℤ] [L'.IsTriangulated] (η' : 𝟭 _ ⟶ L')
    (hL' : ∀ X, (DGCategory.RightModule.yonedaLocalizing (CochainComplex.dgCategory A)
      (DGCategory.phiGen A)).rightOrthogonal (L'.obj X))
    (hη' : ∀ (X Z : derivedHomModuleK A) (f : Z ⟶ X)
      (g : L'.obj X ⟶ Z⟦(1 : ℤ)⟧),
      Triangle.mk f (η'.app X) g ∈ distTriang (derivedHomModuleK A) →
        DGCategory.RightModule.yonedaLocalizing (CochainComplex.dgCategory A)
          (DGCategory.phiGen A) Z)
    (hΦ' : ∀ X, DGCategory.RightModule.yonedaInverseImage (CochainComplex.dgCategory A)
      (DGCategory.phiGen A) X →
      IsZero ((((DGCategory.yonedaDGFunctor (CochainComplex.dgCategory A)).onK) ⋙ L').obj X)) :
    derivedHomReflectorFunctor A K ≅ DGCategory.phiReflector A K L' hΦ'
```

**`CochainComplex.isDistinguishedTriangle_homComplexesFunctor_triangleOfDegreewiseSplit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomTriangles.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomTriangles.lean#L213). The attribute's comment: “the functor Hom(K, -) carries the triangle of a degreewise split short exact sequence of complexes to a distinguished triangle of K(E, d) -- preservation of distinguished triangles for the functor being derived”.

> **`Hom(K, -)` carries the triangle of a degreewise split short exact sequence of complexes to
> a distinguished triangle of `K(E, d)`.** This is the triangle half of the exactness clause of Tag
> 09LK for the functor being derived.

```lean
theorem isDistinguishedTriangle_homComplexesFunctor_triangleOfDegreewiseSplit :
    IsDistinguishedTriangle (DGCategory.endAlgebra (dgCategory B) K)
      (Pretriangulated.Triangle.mk
        ((toHomotopyCategory _).map ((homComplexesFunctor B K).map S.f))
        ((toHomotopyCategory _).map ((homComplexesFunctor B K).map S.g))
        ((toHomotopyCategory _).map (homComplexesConnecting B K S σ) ≫
          eqToHom (CategoryTheory.Quotient.functor_obj_shift
            (homotopyRel (DGCategory.endAlgebra (dgCategory B) K)) ℤ
            (DGCategory.representableModule (dgCategory B) K S.X₁) 1).symm))
```

**`CochainComplex.exists_isDistinguishedTriangle_homComplexesFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomTriangles.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomTriangles.lean#L242). The attribute's comment: “the functor Hom(K, -) being derived preserves distinguished triangles: every distinguished triangle of K(B) is the triangle of a degreewise split short exact sequence of complexes, and its image, with the third arrow read through the shift comparison Hom(K, X[1]) = Hom(K, X)[1], is a distinguished triangle of K(E, d)”. References: SGA 4½ Etat 0 (1.2.4).

> **`Hom(K, -)` preserves distinguished triangles.** Every distinguished triangle of `K(B)` is
> isomorphic to the triangle of a degreewise split short exact sequence of complexes, and the
> image of that triangle under `Hom(K, -)` — with its third arrow corrected by the shift
> comparison `Hom(K, X[1]) ≅ Hom(K, X)[1]` — is a distinguished triangle of `K(E, d)`.
>
> This is the preservation of distinguished triangles asserted by Tag 09LK of the functor being
> derived. It is stated for a presentation of the triangle by a degreewise split sequence rather
> than as `CategoryTheory.Functor.IsTriangulated`; the `CategoryTheory.Functor.CommShift ℤ` that
> the latter also requires is `CochainComplex.homComplexesFunctorCommShift`, whose degree-one
> component is the comparison appearing here.

```lean
theorem exists_isDistinguishedTriangle_homComplexesFunctor [HasZeroObject B]
    [HasBinaryBiproducts B]
    (T : Pretriangulated.Triangle (HomotopyCategory B (ComplexShape.up ℤ)))
    (hT : T ∈ Pretriangulated.distinguishedTriangles
      (C := HomotopyCategory B (ComplexShape.up ℤ))) :
    ∃ (S : ShortComplex (CochainComplex B ℤ))
      (σ : ∀ n, (S.map (eval B (ComplexShape.up ℤ) n)).Splitting),
      Nonempty (T ≅ trianglehOfDegreewiseSplit S σ) ∧
        IsDistinguishedTriangle (DGCategory.endAlgebra (dgCategory B) K)
          (Pretriangulated.Triangle.mk
            ((toHomotopyCategory _).map ((homComplexesFunctor B K).map S.f))
            ((toHomotopyCategory _).map ((homComplexesFunctor B K).map S.g))
            ((toHomotopyCategory _).map (homComplexesConnecting B K S σ) ≫
              eqToHom (CategoryTheory.Quotient.functor_obj_shift
                (homotopyRel (DGCategory.endAlgebra (dgCategory B) K)) ℤ
                (DGCategory.representableModule (dgCategory B) K S.X₁) 1).symm))
```

**`DGCategory.derivedHomForgetPhiReflectorBetaIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomUnitAppIdCore.lean, line 600](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomUnitAppIdCore.lean#L600). The attribute's comment: “the reduction clause: the functor REDUCES TO THE USUAL R Hom(K, -) on taking associated complexes of abelian groups, under the source's own hypothesis h and the reflector data of steps 1 and 2”.

> **`R Hom(K, -) ≅ R̃ ⋙ U`, with nothing owed.**

```lean
def derivedHomForgetPhiReflectorBetaIso :
    CochainComplex.derivedHomForgetFunctor A K h ≅ phiReflectorForget A K L hΦ
```

**`DGCategory.phiReflectorCommShift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/RightModule/DerivedHomPhiReflectorExact.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/DifferentialGraded/RightModule/DerivedHomPhiReflectorExact.lean#L98). The attribute's comment: “half of exactness as a functor of TRIANGULATED categories: the translation compatibility of R Hom(K, -) : D(A) ⥤ D(E, d), relative to which the exactness below is stated”.

> **`R̃ : D(A) ⥤ D(E)` commutes with the translations.** The comparison isomorphisms are
> those of the composite `J ⋙ ev_K`: on the first factor they come from
> `CategoryTheory.Functor.commShiftOfLocalization` at the localization
> `DGCategory.phiComparisonLocalization`, on the second from the derived evaluation functor.
>
> This names the term global instance search already produces for this goal; it is deliberately
> not itself registered as an instance, since `CategoryTheory.Functor.CommShift` is data and a
> second registration would be a diamond.

```lean
def phiReflectorCommShift : (phiReflector A K L hΦ).CommShift ℤ
```

**`DGCategory.phiReflector_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/RightModule/DerivedHomPhiReflectorExact.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/DifferentialGraded/RightModule/DerivedHomPhiReflectorExact.lean#L106). The attribute's comment: “the other half: R Hom(K, -) : D(A) ⥤ D(E, d) is EXACT -- it carries distinguished triangles to distinguished triangles, for the translation compatibility above”.

> **`R̃ : D(A) ⥤ D(E)` is exact.** It is the composite of the descent `J` of step 1 through
> the localization `q` of `K(Comp^dg(A))` at the complexes `Φ⁻¹ N`, which is exact by
> `DGCategory.isTriangulated_derivedReflectorDescent`, with evaluation at `K` on the derived
> categories; both factors are exact, hence so is `R̃`.

```lean
instance phiReflector_isTriangulated : (phiReflector A K L hΦ).IsTriangulated
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.32, Tag 09LJ](https://stacks.math.columbia.edu/tag/09LJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
