---
declaration: section
origin: cited
lean: StacksDraft.DerivedHom.homInternalHomEquiv, homComplex_of_isKInjective_represents_RHom, StacksDraft.DerivedHom.derivedHomCurrying, StacksDraft.DerivedHom.projectiveHomComparison, StacksDraft.DerivedHom.projectiveHomComparisonULift, cohomologyClassRHomAddEquiv, homComplexHomologyRHomAddEquiv, homComplex_represents_RHom
statement: formalized
proof: formalized
---

# 15.75 Derived hom

Section 15.75 of the Stacks Project, [Tag 0A5W](https://stacks.math.columbia.edu/tag/0A5W). 8 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A63, an equation

[Tag 0A63](https://stacks.math.columbia.edu/tag/0A63) in the Stacks Project.

**`StacksDraft.DerivedHom.homInternalHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/DerivedAdjunction.lean, line 2909](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/DerivedAdjunction.lean#L2909).

> **Stacks 0A63.** The canonical characterization equation in `D(R)`:
> `Hom(K, RHom(L, M)) ≃+ Hom(K ⊗ᴸ L, M)`. The bifunctors and the equivalence are
> transported from the fixed K-flat/K-injective construction, with compatibility given by
> `derivedTensorULiftIso` and `derivedHomULiftIso`. No adjunction or scalar equivalence is
> supplied as a parameter. The ring, module enlargement, and derived-morphism universes are
> independent.

```lean
public noncomputable def homInternalHomEquiv {R : Type u} [CommRing R]
    [HasDerivedCategory.{w} (ModuleCat.{max u v} R)]
    (K L M : DerivedCategory (ModuleCat.{max u v} R)) :
    (K ⟶ (derivedHomAdjunctionOverRing R).hom.obj (Opposite.op L, M)) ≃+
      ((derivedHomAdjunctionOverRing R).tensor.obj (K, L) ⟶ M)
```

## Tag 0A64, an equation

[Tag 0A64](https://stacks.math.columbia.edu/tag/0A64) in the Stacks Project.

**`homComplex_of_isKInjective_represents_RHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/RHom.lean#L272).

> **Stacks 0A64**.
> If `I` is K-injective, then the degree-`n` cohomology of the Hom complex `Hom^•(L, I)` is
> canonically identified with the morphisms `L ⟶ I⟦n⟧` in the derived category; equivalently, when
> `I` represents `M`, this is `Hⁿ(RHom(L, M)) = Hom(L, M⟦n⟧)`.

```lean
theorem homComplex_of_isKInjective_represents_RHom (L I : CochainComplex C ℤ) [I.IsKInjective]
    (n : ℤ) :
    Function.Bijective
      (fun (c : CochainComplex.HomComplex.CohomologyClass L I n) ↦
        DerivedCategory.Qh.map
          (CochainComplex.HomComplex.CohomologyClass.homAddEquiv c))
```

## Tag 0A65, a lemma

[Tag 0A65](https://stacks.math.columbia.edu/tag/0A65) in the Stacks Project.

**`StacksDraft.DerivedHom.derivedHomCurrying`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/DerivedAdjunction.lean, line 3927](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/DerivedAdjunction.lean#L3927). References: SGA 6 I (7.4), “affine case, 1st iso”; SGA 7 VIII (1.1), “(1.1.2) in D(R)”.

> **Stacks 0A65.** Derived Hom satisfies the canonical currying isomorphism
> `RHom(K, RHom(L, M)) ≅ RHom(K ⊗ᴸ L, M)`, functorially in `K`, `L`, and `M`.
> On K-flat/K-injective representatives this is the Hom-complex currying map of Stacks 0A5Y.
> On degree-zero cohomology this is the derived tensor--Hom equivalence of Stacks 0A63.

```lean
public noncomputable def derivedHomCurrying {R : Type u} [CommRing R]
    [HasDerivedCategory.{v} (ModuleCat.{u} R)] :
    DerivedHomCurrying (derivedHomAdjunction (R := R))
```

## Tag 0A66, a lemma

[Tag 0A66](https://stacks.math.columbia.edu/tag/0A66) in the Stacks Project.

**`StacksDraft.DerivedHom.projectiveHomComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/ProjectiveRHom.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/ProjectiveRHom.lean#L387).

> **Stacks 0A66.** A bounded-above complex of projective modules computes the derived
> internal Hom against every target complex. The comparison is natural in both variables,
> recovers the defining K-injective model, and hence is the comparison induced by a
> K-injective resolution in the proof of the source lemma.

```lean
def projectiveHomComparison {R : Type u} [CommRing R]
    [HasDerivedCategory.{w} (ModuleCat.{u} R)] : ProjectiveHomComparison R
```

**`StacksDraft.DerivedHom.projectiveHomComparisonULift`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/ProjectiveRHom.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/ProjectiveRHom.lean#L403).

> The comparison of Stacks 0A66 in an independently chosen module universe. The lifted
> ring is canonically isomorphic to `R`, and retains all naturality and model comparisons.

```lean
abbrev projectiveHomComparisonULift {R : Type u} [CommRing R]
    [HasDerivedCategory.{w} (ModuleCat.{max u v} (ULift.{v} R))] :
    ProjectiveHomComparison (ULift.{v} R)
```

**`cohomologyClassRHomAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/RHom.lean#L293).

> **Stacks 0A66**.
> Let `P` be a bounded above complex of projective `R`-modules and `L` a complex of `R`-modules.
> The degree-`n` cohomology classes of `Hom^•(P, L)` are canonically *isomorphic as abelian groups*
> to `Hom_{D(R)}(P, L⟦n⟧)`, the isomorphism sending a class to the image under
> `DerivedCategory.Qh` of the corresponding morphism `P ⟶ L⟦n⟧` in the homotopy category. This is
> the assertion that `Hom^•(P, L)` represents `RHom_R(P, L)`.

```lean
noncomputable def cohomologyClassRHomAddEquiv (P L : CochainComplex (ModuleCat R) ℤ) (d n : ℤ)
    [P.IsStrictlyLE d] [∀ i, CategoryTheory.Projective (P.X i)] :
    CochainComplex.HomComplex.CohomologyClass P L n ≃+
      (DerivedCategory.Qh.obj
          ((HomotopyCategory.quotient (ModuleCat R) (ComplexShape.up ℤ)).obj P) ⟶
        DerivedCategory.Qh.obj
          ((HomotopyCategory.quotient (ModuleCat R) (ComplexShape.up ℤ)).obj (L⟦n⟧)))
```

**`homComplexHomologyRHomAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/RHom.lean#L319).

> **Stacks 0A66**.
> The comparison isomorphism of [stacks 0A66] read on the homology of the Hom complex: for `P` a
> bounded above complex of projective `R`-modules,
> `Hⁿ(Hom^•(P, L)) ≃+ Hom_{D(R)}(P, L⟦n⟧)`, so `Hom^•(P, L)` represents `RHom_R(P, L)`.

```lean
noncomputable def homComplexHomologyRHomAddEquiv (P L : CochainComplex (ModuleCat R) ℤ)
    (d n : ℤ) [P.IsStrictlyLE d] [∀ i, CategoryTheory.Projective (P.X i)] :
    (P.HomComplex L).homology n ≃+
      (DerivedCategory.Qh.obj
          ((HomotopyCategory.quotient (ModuleCat R) (ComplexShape.up ℤ)).obj P) ⟶
        DerivedCategory.Qh.obj
          ((HomotopyCategory.quotient (ModuleCat R) (ComplexShape.up ℤ)).obj (L⟦n⟧)))
```

**`homComplex_represents_RHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/RHom.lean#L353). References: SGA 4 XVII (5.5.6.3), “more general”; SGA 4½ Rapport (4.3), “more general”; SGA 5 IIIB (5.7), “partial”; SGA 6 I (7.1.1), “partial”.

> **Stacks 0A66**.
> Let `P` be a bounded above complex of projective `R`-modules and `L` a complex of `R`-modules.
> For every `n : ℤ`, the map from degree-`n` cohomology classes of `Hom^•(P, L)` to
> `Hom_{D(R)}(P, L⟦n⟧)`, sending a class to the image under `DerivedCategory.Qh` of the corresponding
> morphism `P ⟶ L⟦n⟧` in the homotopy category, is bijective; that is, `Hom^•(P, L)` represents
> `RHom_R(P, L)`.
>
> This is the pointwise shadow of `cohomologyClassRHomAddEquiv`, from which it is derived.

```lean
theorem homComplex_represents_RHom (P L : CochainComplex (ModuleCat R) ℤ) (d n : ℤ)
    [P.IsStrictlyLE d] [∀ i, CategoryTheory.Projective (P.X i)] :
    Function.Bijective
      (fun (c : CochainComplex.HomComplex.CohomologyClass P L n) =>
        DerivedCategory.Qh.map (CochainComplex.HomComplex.CohomologyClass.homAddEquiv c))
```

**`cohomologyClassRHomAddEquiv_naturality_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/RHom.lean#L366).

> **Stacks 0A66**.
> Naturality of the comparison isomorphism in the first variable: for `f : P' ⟶ P` a morphism of
> bounded above complexes of projectives, the square formed by `cohomologyClassRHomAddEquiv` at `P`
> and at `P'`, precomposition by `f` on cohomology classes, and precomposition by the image of `f`
> in `D(R)` commutes. Thus `Hom^•(-, L)` represents `RHom_R(-, L)` contravariantly.

```lean
theorem cohomologyClassRHomAddEquiv_naturality_left (P P' L : CochainComplex (ModuleCat R) ℤ)
    (f : P' ⟶ P) (d d' n : ℤ) [P.IsStrictlyLE d] [∀ i, CategoryTheory.Projective (P.X i)]
    [P'.IsStrictlyLE d'] [∀ i, CategoryTheory.Projective (P'.X i)]
    (c : CochainComplex.HomComplex.CohomologyClass P L n) :
    cohomologyClassRHomAddEquiv P' L d' n (cohomologyClassPrecomp f L n c) =
      DerivedCategory.Qh.map
          ((HomotopyCategory.quotient (ModuleCat R) (ComplexShape.up ℤ)).map f) ≫
        cohomologyClassRHomAddEquiv P L d n c
```

**`cohomologyClassRHomAddEquiv_naturality_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/RHom.lean#L384).

> **Stacks 0A66**.
> Naturality of the comparison isomorphism in the second variable: for `g : L ⟶ L'` the square
> formed by `cohomologyClassRHomAddEquiv` at `L` and at `L'`, postcomposition by `g` on cohomology
> classes, and postcomposition by the image of `g⟦n⟧'` in `D(R)` commutes. Thus `Hom^•(P, -)`
> represents `RHom_R(P, -)` covariantly.

```lean
theorem cohomologyClassRHomAddEquiv_naturality_right (P L L' : CochainComplex (ModuleCat R) ℤ)
    (g : L ⟶ L') (d n : ℤ) [P.IsStrictlyLE d] [∀ i, CategoryTheory.Projective (P.X i)]
    (c : CochainComplex.HomComplex.CohomologyClass P L n) :
    cohomologyClassRHomAddEquiv P L' d n (cohomologyClassPostcomp P g n c) =
      cohomologyClassRHomAddEquiv P L d n c ≫
        DerivedCategory.Qh.map
          ((HomotopyCategory.quotient (ModuleCat R) (ComplexShape.up ℤ)).map (g⟦n⟧'))
```

**`homComplexRHom_isKInjective_model_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/RHom.lean#L402).

> **Stacks 0A66**.
> Compatibility of the two routes to `RHom`: for `g : L ⟶ I` with `I` K-injective, the square whose
> left edge is the comparison of [stacks 0A66] for `(P, L)`, whose right edge is the comparison of
> [stacks 0A64] for `(P, I)`, whose top edge is the map on cohomology classes induced by `g`, and
> whose bottom edge is postcomposition with the image of `g⟦n⟧'` in `D(R)`, commutes. No
> quasi-isomorphism hypothesis is needed for commutativity.

```lean
theorem homComplexRHom_isKInjective_model_comm (P L I : CochainComplex (ModuleCat R) ℤ)
    (g : L ⟶ I) [I.IsKInjective] (d n : ℤ) [P.IsStrictlyLE d]
    [∀ i, CategoryTheory.Projective (P.X i)]
    (c : CochainComplex.HomComplex.CohomologyClass P L n) :
    cohomologyClassRHomAddEquivOfIsKInjective P I n (cohomologyClassPostcomp P g n c) =
      cohomologyClassRHomAddEquiv P L d n c ≫
        DerivedCategory.Qh.map
          ((HomotopyCategory.quotient (ModuleCat R) (ComplexShape.up ℤ)).map (g⟦n⟧'))
```

**`homComplexRHom_eq_isKInjective_model_route`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/RHom.lean#L419).

> **Stacks 0A66**.
> The comparison of [stacks 0A66] is *computed by* the comparison of [stacks 0A64] through a
> K-injective model: if `g : L ⟶ I` is a quasi-isomorphism with `I` K-injective, then the bottom
> edge of the square of `homComplexRHom_isKInjective_model_comm` is invertible, and the
> [stacks 0A66] comparison for `(P, L)` is the [stacks 0A64] comparison for `(P, I)` applied to the
> transported class, followed by that inverse. So the two representability statements agree.

```lean
theorem homComplexRHom_eq_isKInjective_model_route (P L I : CochainComplex (ModuleCat R) ℤ)
    (g : L ⟶ I) [I.IsKInjective] [QuasiIso g] (d n : ℤ) [P.IsStrictlyLE d]
    [∀ i, CategoryTheory.Projective (P.X i)]
    (c : CochainComplex.HomComplex.CohomologyClass P L n) :
    cohomologyClassRHomAddEquiv P L d n c =
      cohomologyClassRHomAddEquivOfIsKInjective P I n (cohomologyClassPostcomp P g n c) ≫
        CategoryTheory.inv (DerivedCategory.Qh.map
          ((HomotopyCategory.quotient (ModuleCat R) (ComplexShape.up ℤ)).map (g⟦n⟧')))
```

**`Dualizing.homComplexRHomologyLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/RelativeBaseChangeAssemblyLinear.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/RelativeBaseChangeAssemblyLinear.lean#L99).

> **[stacks 0A66] read on the derived category, `S`-linearly.**  For `P` a bounded above complex
> of projective `S`-modules and `L` any complex, the degree-`n` cohomology of the `S`-linear Hom
> complex `Hom^•_S(P, L)` is the module of morphisms `P ⟶ L⟦n⟧` in `D(S)`, as `S`-modules.
>
> This is `Dualizing.homComplexRHomologyAddEquiv` with the `S`-action checked.  The comparison runs
> through the cohomology classes of the Hom complex of the underlying abelian groups, where no
> `S`-action is available, so the equivariance is read on representatives: a class in
> `H^n(Hom^•_S(P, L))` is the class of a cocycle
> (`Dualizing.LocalDuality.homComplexRHomologyAddEquiv_cyclesMk`), the `S`-action on `H^n` is the
> action on cocycles, and the passage from a cocycle to a morphism in the homotopy category is
> `S`-linear because `CochainComplex.HomComplex.Cocycle.equivHomShift` is and because
> `HomotopyCategory.quotient` and `DerivedCategory.Qh` are `S`-linear functors.

```lean
def homComplexRHomologyLinearEquiv (P L : CochainComplex (ModuleCat.{u} S) ℤ) (d n : ℤ)
    [P.IsStrictlyLE d] [∀ i, Projective (P.X i)] :
    ((CochainComplex.HomComplexR S P L).homology n : Type u) ≃ₗ[S]
      (DerivedCategory.Q.obj P ⟶
        (CategoryTheory.shiftFunctor (DerivedCategory (ModuleCat.{u} S)) n).obj
          (DerivedCategory.Q.obj L))
```

## Tag 0A67, a lemma

[Tag 0A67](https://stacks.math.columbia.edu/tag/0A67) in the Stacks Project.

**`StacksDraft.DerivedHom.exists_evaluationToIteratedDerivedHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/DerivedAdjunction.lean, line 4019](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/DerivedAdjunction.lean#L4019).

> **Stacks 0A67.** There is a canonical morphism
> `RHom_R(L, M) ⊗ᴸ_R K ⟶ RHom_R(RHom_R(K, L), M)` for arbitrary objects of `D(R)`,
> natural in all three objects. On K-flat and K-injective representatives it is induced by the
> chain-level evaluation map of Stacks Tag 0A60 through the standard comparison isomorphisms.

```lean
public theorem exists_evaluationToIteratedDerivedHom :
    let D := derivedHomAdjunction (R := R)
    let e₀ := ChainEvaluation.chainEvaluation
    ∃ e : ∀ (K L M : DerivedCategory (ModuleCat R)),
        D.tensor.obj (D.hom.obj (Opposite.op L, M), K) ⟶
          D.hom.obj (Opposite.op (D.hom.obj (Opposite.op K, L)), M),
      (∀ {K K' L M : DerivedCategory (ModuleCat R)} (f : K ⟶ K'),
        D.tensor.map (𝟙 (D.hom.obj (Opposite.op L, M)), f) ≫ e K' L M =
          e K L M ≫ D.hom.map
            ((D.hom.map (f.op, 𝟙 L)).op, 𝟙 M)) ∧
      (∀ {K L L' M : DerivedCategory (ModuleCat R)} (f : L ⟶ L'),
        D.tensor.map (D.hom.map (f.op, 𝟙 M), 𝟙 K) ≫ e K L M =
          e K L' M ≫ D.hom.map
            ((D.hom.map (𝟙 (Opposite.op K), f)).op, 𝟙 M)) ∧
      (∀ {K L M M' : DerivedCategory (ModuleCat R)} (f : M ⟶ M'),
        D.tensor.map (D.hom.map (𝟙 (Opposite.op L), f), 𝟙 K) ≫ e K L M' =
          e K L M ≫ D.hom.map
            (𝟙 (Opposite.op (D.hom.obj (Opposite.op K, L))), f)) ∧
      (∀ (K L M : CochainComplex (ModuleCat R) ℤ) (hK : K.KFlat)
          [L.IsKInjective] [M.IsKInjective],
        D.tensor.map ((D.homIso L M).hom, 𝟙 (DerivedCategory.Q.obj K)) ≫
              (D.tensorIso (HomComplexR R L M) K hK).hom ≫
              DerivedCategory.Q.map (e₀ K L M) ≫
              (D.homIso (HomComplexR R K L) M).inv ≫
              D.hom.map ((D.homIso K L).hom.op, 𝟙 (DerivedCategory.Q.obj M)) =
            e (DerivedCategory.Q.obj K) (DerivedCategory.Q.obj L)
              (DerivedCategory.Q.obj M))
```

## Tag 0A8J, a lemma

[Tag 0A8J](https://stacks.math.columbia.edu/tag/0A8J) in the Stacks Project.

**`StacksDraft.DerivedHom.derivedInternalHomComposition_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/DerivedComposition.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/DerivedComposition.lean#L48).

> **Stacks 0A8J.** The canonical composition morphisms
> `RHom(L, M) ⊗ᴸ RHom(K, L) ⟶ RHom(K, M)` in `D(R)` are contravariantly natural in
> `K`, dinatural in `L`, and covariantly natural in `M`.

```lean
theorem derivedInternalHomComposition_natural
    (R : Type u) [CommRing R] [HasDerivedCategory (ModuleCat R)] :
    (∀ {K K' L M : DerivedCategory (ModuleCat R)} (f : K' ⟶ K),
      (DerivedInternalHom.Model.tensor R).map
            (𝟙 ((DerivedInternalHom.Model.hom R).obj (Opposite.op L, M)),
              (DerivedInternalHom.Model.hom R).map (f.op, 𝟙 L)) ≫
          DerivedInternalHom.Model.composition K' L M =
        DerivedInternalHom.Model.composition K L M ≫
          (DerivedInternalHom.Model.hom R).map (f.op, 𝟙 M)) ∧
    (∀ {K L L' M : DerivedCategory (ModuleCat R)} (f : L' ⟶ L),
      (DerivedInternalHom.Model.tensor R).map
            ((DerivedInternalHom.Model.hom R).map (f.op, 𝟙 M),
              𝟙 ((DerivedInternalHom.Model.hom R).obj (Opposite.op K, L'))) ≫
          DerivedInternalHom.Model.composition K L' M =
        (DerivedInternalHom.Model.tensor R).map
            ((𝟙 ((DerivedInternalHom.Model.hom R).obj (Opposite.op L, M)),
              ((DerivedInternalHom.Model.hom R).map (𝟙 (Opposite.op K), f) :
                (DerivedInternalHom.Model.hom R).obj (Opposite.op K, L') ⟶
                  (DerivedInternalHom.Model.hom R).obj (Opposite.op K, L))) :
              ((DerivedInternalHom.Model.hom R).obj (Opposite.op L, M),
                (DerivedInternalHom.Model.hom R).obj (Opposite.op K, L')) ⟶
              ((DerivedInternalHom.Model.hom R).obj (Opposite.op L, M),
                (DerivedInternalHom.Model.hom R).obj (Opposite.op K, L))) ≫
          DerivedInternalHom.Model.composition K L M) ∧
    (∀ {K L M M' : DerivedCategory (ModuleCat R)} (f : M ⟶ M'),
      (DerivedInternalHom.Model.tensor R).map
            ((DerivedInternalHom.Model.hom R).map (𝟙 (Opposite.op L), f),
              𝟙 ((DerivedInternalHom.Model.hom R).obj (Opposite.op K, L))) ≫
          DerivedInternalHom.Model.composition K L M' =
        DerivedInternalHom.Model.composition K L M ≫
          (DerivedInternalHom.Model.hom R).map (𝟙 (Opposite.op K), f))
```

## Tag 0BYN, a lemma

[Tag 0BYN](https://stacks.math.columbia.edu/tag/0BYN) in the Stacks Project.

**`StacksDraft.DerivedHom.derivedTensorHomDiagonal`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/DerivedTensorHom.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/DerivedTensorHom.lean#L66).

> **Stacks 0BYN.** The canonical morphism
> `K ⊗ᴸ RHom(M, L) ⟶ RHom(M, K ⊗ᴸ L)` in the derived category.

```lean
alias derivedTensorHomDiagonal
```

**`StacksDraft.DerivedHom.derivedTensorHomDiagonal_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/DerivedTensorHom.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/DerivedTensorHom.lean#L71).

> **Stacks 0BYN.** The derived tensor--Hom diagonal is covariantly natural in `K` and `L`
> and contravariantly natural in `M`.

```lean
theorem derivedTensorHomDiagonal_natural :
    (∀ {K K' L M : DerivedCategory (ModuleCat R)} (f : K ⟶ K'),
      (DerivedInternalHom.Model.tensor R).map
          (f, 𝟙 ((DerivedInternalHom.Model.hom R).obj (Opposite.op M, L))) ≫
          derivedTensorHomDiagonal K' L M =
        derivedTensorHomDiagonal K L M ≫
          (DerivedInternalHom.Model.hom R).map
            (𝟙 (Opposite.op M), (DerivedInternalHom.Model.tensor R).map (f, 𝟙 L))) ∧
    (∀ {K L L' M : DerivedCategory (ModuleCat R)} (f : L ⟶ L'),
      (DerivedInternalHom.Model.tensor R).map
          (𝟙 K, (DerivedInternalHom.Model.hom R).map (𝟙 (Opposite.op M), f)) ≫
          derivedTensorHomDiagonal K L' M =
        derivedTensorHomDiagonal K L M ≫
          (DerivedInternalHom.Model.hom R).map
            (𝟙 (Opposite.op M), (DerivedInternalHom.Model.tensor R).map (𝟙 K, f))) ∧
    (∀ {K L M M' : DerivedCategory (ModuleCat R)} (f : M' ⟶ M),
      (DerivedInternalHom.Model.tensor R).map
          (𝟙 K, (DerivedInternalHom.Model.hom R).map (f.op, 𝟙 L)) ≫
          derivedTensorHomDiagonal K L M' =
        derivedTensorHomDiagonal K L M ≫
          (DerivedInternalHom.Model.hom R).map
            (f.op, 𝟙 ((DerivedInternalHom.Model.tensor R).obj (K, L))))
```

## Tag 0A6B, a lemma

[Tag 0A6B](https://stacks.math.columbia.edu/tag/0A6B) in the Stacks Project.

**`StacksDraft.DerivedHom.derivedTensorHomCoevaluation_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/DerivedTensorHom.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/HomComplex/DerivedTensorHom.lean#L100).

> **Stacks 0A6B.** The canonical morphism `K ⟶ RHom(L, K ⊗ᴸ L)` is the transpose
> of the identity on `K ⊗ᴸ L`; it is covariantly natural in `K` and dinatural in `L`.

```lean
theorem derivedTensorHomCoevaluation_natural :
    (∀ (K L : DerivedCategory (ModuleCat R)),
      DerivedInternalHom.Model.homEquiv K L ((DerivedInternalHom.Model.tensor R).obj (K, L))
          (DerivedInternalHom.Model.coevaluation K L) =
        𝟙 ((DerivedInternalHom.Model.tensor R).obj (K, L))) ∧
    (∀ {K K' L : DerivedCategory (ModuleCat R)} (f : K ⟶ K'),
      f ≫ DerivedInternalHom.Model.coevaluation K' L =
        DerivedInternalHom.Model.coevaluation K L ≫
          (DerivedInternalHom.Model.hom R).map
            (𝟙 (Opposite.op L), (DerivedInternalHom.Model.tensor R).map (f, 𝟙 L))) ∧
    (∀ {K L L' : DerivedCategory (ModuleCat R)} (g : L ⟶ L'),
      DerivedInternalHom.Model.coevaluation K L' ≫
          (DerivedInternalHom.Model.hom R).map
            ((g.op, 𝟙 ((DerivedInternalHom.Model.tensor R).obj (K, L'))) :
              (Opposite.op L', (DerivedInternalHom.Model.tensor R).obj (K, L')) ⟶
                (Opposite.op L, (DerivedInternalHom.Model.tensor R).obj (K, L'))) =
        DerivedInternalHom.Model.coevaluation K L ≫
          (DerivedInternalHom.Model.hom R).map
            ((𝟙 (Opposite.op L), (DerivedInternalHom.Model.tensor R).map (𝟙 K, g)) :
              (Opposite.op L, (DerivedInternalHom.Model.tensor R).obj (K, L)) ⟶
                (Opposite.op L, (DerivedInternalHom.Model.tensor R).obj (K, L'))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.75, Tag 0A5W](https://stacks.math.columbia.edu/tag/0A5W)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
