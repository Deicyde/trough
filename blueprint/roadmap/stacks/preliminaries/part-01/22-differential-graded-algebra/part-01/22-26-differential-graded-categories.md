---
declaration: section
origin: cited
lean: DGCategory, DGCategory.DGFunctor, DGCategory.Cocycle, DGCategory.Comp, DGCategory.instCategoryComp, DGCategory.K, DGCategory.HomotopyClass, DGCategory.instCategoryK
statement: formalized
proof: formalized
---

# 22.26 Differential graded categories

Section 22.26 of the Stacks Project, [Tag 09L4](https://stacks.math.columbia.edu/tag/09L4). 10 tags here are carried by 37 declarations of the repository (all in StacksFrontier) and 27 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09L5, a definition

[Tag 09L5](https://stacks.math.columbia.edu/tag/09L5) in the Stacks Project.

**`DGCategory`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/DGCategory.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/DGCategory.lean#L43).

> **Definition 1 (Tag 09L5).**  A *differential graded category over a
> commutative ring `R`*.  For each pair of objects `x, y` the family
> `Hom x y n` (degree-`n` morphisms) is a graded `R`-module; the differential `d`
> raises the degree by one and squares to zero; composition `comp` is graded and
> `R`-bilinear, obeys the Leibniz rule, is associative and unital, and the
> identities are closed of degree `0`.
>
> To avoid casting along the (non-definitional) arithmetic identities of the
> grading group `ℤ`, the graded operations carry an explicit equality of degrees
> (e.g. composition of a degree-`m` and a degree-`n` morphism lands in any
> prescribed degree `k` together with a proof `m + n = k`).

```lean
structure DGCategory (R : Type*) [CommRing R]
```

## Tag 09L6, a definition

[Tag 09L6](https://stacks.math.columbia.edu/tag/09L6) in the Stacks Project.

**`DGCategory.DGFunctor`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/DGCategory.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/DGCategory.lean#L384).

> **Definition 2 (Tag 09L6).**  A *functor of differential graded categories
> over `R`*: a map on objects together with degree-preserving `R`-linear maps on
> Hom-modules that commute with the differential and preserve composition and
> identities.

```lean
structure DGFunctor {R : Type*} [CommRing R] (A B : DGCategory R)
```

## Tag 09L7, a definition

[Tag 09L7](https://stacks.math.columbia.edu/tag/09L7) in the Stacks Project.

Declarations registered for the tag:

- [`DGCategory.Cocycle`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/DGCategory.lean#L218), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean#L39) (StacksFrontier): “category_of_complexes”.
- [`DGCategory.Comp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/DGCategory.lean#L252), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean#L40) (StacksFrontier): “category_of_complexes”.
- [`DGCategory.instCategoryComp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/DGCategory.lean#L257), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean#L41) (StacksFrontier): “category_of_complexes”.
- [`DGCategory.K`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/DGCategory.lean#L345), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean#L43) (StacksFrontier): “homotopy_category”.
- [`DGCategory.HomotopyClass`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/DGCategory.lean#L349), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean#L44) (StacksFrontier): “homotopy_category”.
- [`DGCategory.instCategoryK`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/DGCategory.lean#L364), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean#L45) (StacksFrontier): “homotopy_category”.

## Tag 09P4, a definition

[Tag 09P4](https://stacks.math.columbia.edu/tag/09P4) in the Stacks Project.

**`DGCategory.BinaryBiproductData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Biproduct.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Biproduct.lean#L40).

> A direct sum of `X` and `Y` in a differential graded category, with all inclusions and
> projections closed and homogeneous of degree zero.

```lean
public structure BinaryBiproductData {R : Type w} [CommRing R] (A : DGCategory.{v, u} R)
    (X Y : A.Obj)
```

## Tag 09L8, a lemma

[Tag 09L8](https://stacks.math.columbia.edu/tag/09L8) in the Stacks Project.

**`DGCategory.dgFunctor_induces_functors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/DGCategory.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/DGCategory.lean#L499).

> **Tag 09L8.**  A DG-functor `F : A → B` induces ordinary functors
> `Comp F : Comp A ⥤ Comp B` (here `F.onComp`) and `K F : K A ⥤ K B` (here
> `F.onK`), characterised by:
>
> 1. (objects) both agree with `F` on objects;
> 2. (morphisms of `Comp`) `Comp F` sends a closed degree-`0` morphism `f` to the
>    (again closed) morphism `F.map f`;
> 3. (morphisms of `K`) `K F` sends the homotopy class `[f]` to `[F.map f]`;
> 4. (compatibility) the canonical functors `Comp → K` intertwine `Comp F` and
>    `K F`, i.e. `compToK A ⋙ K F = Comp F ⋙ compToK B`.
>
> These are the genuine functoriality content of the lemma; `F.onComp` and
> `F.onK` are honest `CategoryTheory.Functor`s, so identity- and
> composition-preservation (part (4) of the informal statement) is built into
> their types.

```lean
theorem dgFunctor_induces_functors (F : DGFunctor A B) :
    (∀ x : A.Comp, F.onComp.obj x = F.obj x) ∧
      (∀ {x y : A.Comp} (f : x ⟶ y), (F.onComp.map f).1 = F.map f.1) ∧
      (∀ x : A.K, F.onK.obj x = F.obj x) ∧
      (∀ {x y : A.Obj} (f : A.Cocycle x y),
        F.onK.map (Quotient.mk _ f : A.HomotopyClass x y)
          = Quotient.mk _ (F.mapCocycle f)) ∧
      (compToK A ⋙ F.onK = F.onComp ⋙ compToK B)
```

## Tag 09L9, an example

[Tag 09L9](https://stacks.math.columbia.edu/tag/09L9) in the Stacks Project.

**`CochainComplex.homotopicToZero_iff_eq_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean#L60). The attribute's comment: “boundaries_homotopies”.

> A closed homogeneous morphism is a boundary if and only if the associated morphism to the
> shifted target is homotopic to zero.

```lean
public theorem homotopicToZero_iff_eq_d {A C : CochainComplex B ℤ} {n : ℤ}
    (f : Cocycle A C n) :
    Nonempty (Homotopy (Cocycle.equivHomShift.symm f) 0) ↔
      ∃ (m : ℤ) (hm : m + 1 = n) (g : (dgCategory B).Hom A C m),
        hm ▸ (dgCategory B).d g = f.1
```

**`CochainComplex.complexesCategoryEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean#L115). The attribute's comment: “complexes_category”.

> The canonical equivalence from the category of complexes of `CochainComplex.dgCategory B`
> to the ordinary category of cochain complexes in `B`. It fixes objects and acts on morphisms by
> taking the component of a cochain in each degree.

```lean
public noncomputable def complexesCategoryEquivalence :
    { E : (dgCategory B).Comp ≌ CochainComplex B ℤ //
      (∀ X : (dgCategory B).Comp, E.functor.obj X = X) ∧
      (∀ (X Y : (dgCategory B).Comp) (f : X ⟶ Y) (i : ℤ),
        HEq ((E.functor.map f).f i) (f.1.v i i (add_zero i))) }
```

**`CochainComplex.homotopyCategoryHomologyAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean#L135). The attribute's comment: “homotopy_category”. References: SGA 2 V (1.1), “more general”; SGA 4½ Etat 0 (1.3.3), “H⁰(Hom•(A”.

> The canonical identification of homotopy classes of maps of complexes with
> degree-zero cohomology of the differential graded Hom.

```lean
public noncomputable def homotopyCategoryHomologyAddEquiv
    (A C : CochainComplex B ℤ) :
    (((HomotopyCategory.quotient B (.up ℤ)).obj A) ⟶
      ((HomotopyCategory.quotient B (.up ℤ)).obj C)) ≃+
      (CochainComplex.HomComplex A C).homology 0
```

**`CochainComplex.homotopyCategoryHomologyAddEquiv_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean#L150). The attribute's comment: “homotopy_category”.

> The canonical comparison carries a chain map to the cohomology class of its
> degree-zero cochain.

```lean
public theorem homotopyCategoryHomologyAddEquiv_map
    {A C : CochainComplex B ℤ} (f : A ⟶ C) :
    homotopyCategoryHomologyAddEquiv B A C
        ((HomotopyCategory.quotient B (.up ℤ)).map f) =
      (homologyAddEquiv A C 0).symm (CohomologyClass.mk (Cocycle.ofHom f))
```

**`CochainComplex.homotopyCategoryEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean#L184). The attribute's comment: “homotopy_category”.

> The homotopy category of the differential graded category of complexes is
> equivalent to the usual homotopy category of complexes.

```lean
public noncomputable def homotopyCategoryEquivalence :
    HomotopyCategory B (.up ℤ) ≌ (dgCategory B).K
```

**`CochainComplex.homotopyCategoryEquivalence_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean#L249). The attribute's comment: “homotopy_category”.

> The comparison equivalence is the identity on complexes.

```lean
public theorem homotopyCategoryEquivalence_obj (A : CochainComplex B ℤ) :
    (homotopyCategoryEquivalence B).functor.obj
      ((HomotopyCategory.quotient B (.up ℤ)).obj A) = A
```

**`CochainComplex.homotopyCategoryEquivalence_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparison.lean#L258). The attribute's comment: “homotopy_category”.

> On morphisms, the comparison sends the homotopy class of a chain map to
> the corresponding degree-zero cocycle modulo boundaries.

```lean
public theorem homotopyCategoryEquivalence_map {A C : CochainComplex B ℤ}
    (f : A ⟶ C) :
    HEq ((homotopyCategoryEquivalence B).functor.map
      ((HomotopyCategory.quotient B (.up ℤ)).map f))
      (Quotient.mk _
        (show (dgCategory B).Cocycle A C from
          ⟨Cochain.ofHom f, by
            change δ 0 1 (Cochain.ofHom f) = 0
            simp⟩) :
        (dgCategory B).HomotopyClass A C)
```

**`CochainComplex.homotopyCategoryEquivalence_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparisonTriangulated.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexComparisonTriangulated.lean#L191). The attribute's comment: “the comparison of the homotopy category of the differential graded category of complexes with the ordinary homotopy category is an equivalence of TRIANGULATED categories”.

> **The comparison of the two homotopy categories is an equivalence of triangulated
> categories.** This is [Stacks, Tag 09L9] read as a statement about triangulated categories: the
> two pretriangulated structures, Mathlib's on `K(B)` and
> `CochainComplex.dgCategoryKPretriangulated` on `K(Comp^dg(B))`, correspond under it.

```lean
instance homotopyCategoryEquivalence_isTriangulated :
    (homotopyCategoryEquivalence B).IsTriangulated
```

**`CochainComplex.dgCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexDGCategory.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexDGCategory.lean#L58). The attribute's comment: “differential_graded_category_of_complexes”. References: SGA 2 V (1.1), “Hom^•(F,G) complex”; SGA 4 XVII (1.1.10), “(ii)”.

> The differential graded category of cochain complexes in a preadditive category `B`. Its
> degree-`n` morphisms `A ⟶ C` are the families `A.X i ⟶ C.X (i + n)`, the differential is
> `(d f) i = f i ≫ d - (-1)^n • (d ≫ f (i + 1))`, and composition and identities are the
> componentwise ones.

```lean
public def dgCategory : DGCategory ℤ
```

Declarations registered for the tag:

- [`DGCategory.d_d`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.d_d#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Basic.lean#L47) (StacksFrontier): “hom_differential”.
- [`CochainComplex.HomComplex.Cocycle.equivHomShift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.HomComplex.Cocycle.equivHomShift#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexDGCategory.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexDGCategory.lean#L238) (StacksFrontier): “closed_shift”.
- [`CochainComplex.HomComplex.Cocycle.equivHomShift_symm_apply`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.HomComplex.Cocycle.equivHomShift_symm_apply#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexDGCategory.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexDGCategory.lean#L239) (StacksFrontier): “closed_shift”.
- [`CochainComplex.HomComplex.Cocycle.cochain_ofHom_homOf_eq_coe`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.HomComplex.Cocycle.cochain_ofHom_homOf_eq_coe#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexDGCategory.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexDGCategory.lean#L240) (StacksFrontier): “closed_shift”.
- [`CochainComplex.HomComplex.Cocycle.rightShift_coe`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.HomComplex.Cocycle.rightShift_coe#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexDGCategory.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexDGCategory.lean#L241) (StacksFrontier): “closed_shift”.
- [`DGCategory.leibniz`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.leibniz#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexLeibniz.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexLeibniz.lean#L30) (StacksFrontier): “composition_leibniz”.

## Tag 09LB, a lemma

[Tag 09LB](https://stacks.math.columbia.edu/tag/09LB) in the Stacks Project.

**`CochainComplex.additiveFunctorDG`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexAdditiveFunctor.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexAdditiveFunctor.lean#L59). The attribute's comment: “the differential graded functor”. References: SGA 4 XVII (1.1.6), “one covariant variable”.

> Applying an additive functor to each component of a cochain defines a differential graded
> functor on complexes.

```lean
noncomputable def additiveFunctorDG (F : B ⥤ B') [F.Additive] :
    DGFunctor (dgCategory B) (dgCategory B')
```

**`CochainComplex.additiveFunctorDG_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexAdditiveFunctor.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexAdditiveFunctor.lean#L93). The attribute's comment: “action on objects”.

> The differential graded functor applies `F` degreewise to objects.

```lean
theorem additiveFunctorDG_obj (A : CochainComplex B ℤ) :
    (additiveFunctorDG F).obj A = (F.mapHomologicalComplex (.up ℤ)).obj A
```

**`CochainComplex.additiveFunctorDG_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexAdditiveFunctor.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexAdditiveFunctor.lean#L99). The attribute's comment: “action on homogeneous morphisms”.

> The differential graded functor applies `F` to every component of a homogeneous map.

```lean
theorem additiveFunctorDG_map {A C : CochainComplex B ℤ} {n : ℤ}
    (f : Cochain A C n) :
    HEq ((additiveFunctorDG F).map f) (f.map F)
```

**`CochainComplex.additiveFunctorDG_onComp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexAdditiveFunctor.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexAdditiveFunctor.lean#L117). The attribute's comment: “induced functor on complexes”.

> On closed degree-zero maps, the differential graded functor is the usual functor on
> cochain complexes, through the canonical comparisons.

```lean
theorem additiveFunctorDG_onComp :
    (additiveFunctorDG F).onComp ⋙ (complexesCategoryEquivalence B').1.functor =
      (complexesCategoryEquivalence B).1.functor ⋙ F.mapHomologicalComplex (.up ℤ)
```

**`CochainComplex.additiveFunctorDG_onK`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexAdditiveFunctor.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexAdditiveFunctor.lean#L161). The attribute's comment: “induced functor on homotopy categories”.

> On homotopy classes, the differential graded functor is the usual functor on homotopy
> categories, through the canonical comparisons.

```lean
theorem additiveFunctorDG_onK :
    letI : Category (dgCategory B).K :=
      (dgCategory B).instCategoryK
    letI : Category (dgCategory B').K :=
      (dgCategory B').instCategoryK
    F.mapHomotopyCategory (.up ℤ) ⋙ (homotopyCategoryEquivalence B').functor =
      (homotopyCategoryEquivalence B).functor ⋙ (additiveFunctorDG F).onK
```

## Tag 09LC, an example

[Tag 09LC](https://stacks.math.columbia.edu/tag/09LC) in the Stacks Project.

**`CochainComplex.homologyCoyonedaNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomCohomologyIso.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomCohomologyIso.lean#L426). The attribute's comment: “the cohomology of the differential graded Hom module Hom(K, -) of 09LE, in every degree, as the functor corepresented by K composed with the translation”. References: SGA 4½ Etat 0 (1.3.3), “The final clause of 3.3”.

> **`H^n(Hom^•(K, -)) ≅ Hom_{K(B)}(K, (-)[n])` as functors.** The degree-`n` cohomology of the
> `D(Ab)`-valued differential graded Hom functor `Hom(K, -)` that Tag 09LK right derives, read as a
> functor to sets, is the functor corepresented by the homotopy class of `K` composed with the
> `n`-th translation of the homotopy category of complexes in `B`.

```lean
def homologyCoyonedaNatIso (n : ℤ) :
    homToDerivedCategoryForget B K ⋙ DerivedCategory.homologyFunctor (ModuleCat.{0} ℤ) n ⋙
        forget (ModuleCat.{0} ℤ) ≅
      CategoryTheory.shiftFunctor (HomotopyCategory B (ComplexShape.up ℤ)) n ⋙
        coyoneda.obj (Opposite.op ((HomotopyCategory.quotient B (ComplexShape.up ℤ)).obj K))
```

**`DifferentialGradedModule.homogeneousMapSubmodule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategory.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategory.lean#L67). The attribute's comment: “differential_graded_category_of_differential_graded_modules”.

> A homogeneous right `A`-linear map of degree `n` between differential graded modules.

```lean
public def homogeneousMapSubmodule (L M : DifferentialGradedModule.{u, v, w} A)
    (n : ℤ) : Submodule R (L.M →ₗ[R] M.M)
```

**`DifferentialGradedModule.dgCategoryData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategory.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategory.lean#L262). The attribute's comment: “differential_graded_category_of_differential_graded_modules”.

> The differential graded category of right differential graded modules over `A`.

```lean
public noncomputable def dgCategoryData :
    DGCategoryData A
```

**`DifferentialGradedModule.homogeneousMapDifferential_eq_zero_iff_exists_hom_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryClosedMaps.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryClosedMaps.lean#L81). The attribute's comment: “closed_maps”.

> A homogeneous map is closed for the Hom differential if and only if it is a homomorphism
> into the shifted target, with the same underlying linear map.

```lean
theorem homogeneousMapDifferential_eq_zero_iff_exists_hom_shift
    (L M : DifferentialGradedModule A) (n : ℤ) (f : HomogeneousMap A L M n) :
    homogeneousMapDifferential A f = 0 ↔
      ∃ g : Hom L (shift M n), g.toFun = f.1
```

**`DifferentialGradedModule.homotopic_zero_iff_exists_homogeneousMapDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryClosedMaps.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryClosedMaps.lean#L111). The attribute's comment: “boundaries_homotopies”.

> A closed homogeneous map is a boundary exactly when the corresponding homomorphism into the
> shifted target is homotopic to zero.

```lean
theorem homotopic_zero_iff_exists_homogeneousMapDifferential
    {L M : DifferentialGradedModule A} {n : ℤ}
    (f : HomogeneousMap A L M n) (F : Hom L (shift M n)) (hF : F.toFun = f.1) :
    Homotopic F 0 ↔
      ∃ g : HomogeneousMap A L M (n - 1), (homogeneousMapDifferential A g).1 = f.1
```

**`DifferentialGradedModule.dgCategoryCompEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComp.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComp.lean#L122). The attribute's comment: “category_of_complexes”.

> The category of complexes of the differential graded category of differential graded modules
> is canonically equivalent to the category of differential graded modules: the equivalence is the
> identity on objects and does not change the underlying linear map of a morphism.

```lean
noncomputable def dgCategoryCompEquivalence :
    { E : (dgCategoryData A).category.Comp ≌ DifferentialGradedModule A //
      (∀ M : (dgCategoryData A).category.Comp, E.functor.obj M = M) ∧
      (∀ (L M : (dgCategoryData A).category.Comp) (f : L ⟶ M),
        HEq (E.functor.map f).toFun f.1.1) }
```

**`DifferentialGradedModule.homotopyCategoryHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryHomotopyCategory.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryHomotopyCategory.lean#L109). The attribute's comment: “homotopy_category”.

> Homotopy classes of homomorphisms of differential graded modules are canonically the
> degree-zero cohomology classes of their differential graded Hom module.

```lean
noncomputable def homotopyCategoryHomEquiv (L M : DifferentialGradedModule A) :
    ((((toHomotopyCategory A).obj L) ⟶ ((toHomotopyCategory A).obj M)) ≃
      (dgCategory A).HomotopyClass L M)
```

**`DifferentialGradedModule.homotopyCategoryHomEquiv_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryHomotopyCategory.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryHomotopyCategory.lean#L126). The attribute's comment: “homotopy_category”.

> The canonical bijection sends a homomorphism to the cohomology class of the closed
> homogeneous map with the same underlying linear map.

```lean
theorem homotopyCategoryHomEquiv_map (L M : DifferentialGradedModule A) (f : Hom L M) :
    ∃ c : (dgCategory A).Cocycle L M, c.1.1 = f.toFun ∧
      homotopyCategoryHomEquiv A L M ((toHomotopyCategory A).map f) = Quotient.mk _ c
```

**`DifferentialGradedModule.homotopyCategoryEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryHomotopyCategory.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryHomotopyCategory.lean#L134). The attribute's comment: “homotopy_category”.

> The homotopy category of the differential graded category of differential graded modules is
> canonically equivalent to the homotopy category of differential graded modules.

```lean
noncomputable def homotopyCategoryEquivalence :
    HomotopyCategory A ≌ (dgCategory A).K
```

**`DifferentialGradedModule.homotopyCategoryEquivalence_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryHomotopyCategory.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryHomotopyCategory.lean#L159). The attribute's comment: “homotopy_category”.

> The canonical equivalence of homotopy categories is the identity on differential graded
> modules.

```lean
theorem homotopyCategoryEquivalence_obj (L : DifferentialGradedModule A) :
    (homotopyCategoryEquivalence A).functor.obj ((toHomotopyCategory A).obj L) = L
```

**`DifferentialGradedModule.homotopyCategoryEquivalence_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryHomotopyCategory.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryHomotopyCategory.lean#L166). The attribute's comment: “homotopy_category”.

> The functor of the canonical equivalence acts on every morphism by the canonical
> identification with degree-zero Hom cohomology.

```lean
theorem homotopyCategoryEquivalence_map (L M : DifferentialGradedModule A)
    (f : ((toHomotopyCategory A).obj L) ⟶ ((toHomotopyCategory A).obj M)) :
    HEq ((homotopyCategoryEquivalence A).functor.map f) (homotopyCategoryHomEquiv A L M f)
```

**`DifferentialGradedModule.homologyAddEquiv_homologyMap_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DGFunctorHomComplexCohomology.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGFunctorHomComplexCohomology.lean#L224). The attribute's comment: “naturality of the cohomology of the Hom complex under a differential graded functor, on cohomology classes”.

> **Tag 09LC is natural under a differential graded functor**, on cohomology classes. The
> degree-`n` cohomology of the map of Hom complexes induced by `F` sends the class of a closed
> degree-`n` homogeneous morphism `f : M ⟶ N` to the class of the cocycle `F f`.

```lean
theorem homologyAddEquiv_homologyMap_mk
    (f : ↥(AddCommGrpCat.Hom.hom (General.homSc A M N n).g).ker) :
    CochainComplex.HomComplex.homologyAddEquiv ((dgFunctorToComplexes F).obj M)
        ((dgFunctorToComplexes F).obj N) n
        (HomologicalComplex.homologyMap (dgFunctorHomComplexMap F M N) n
          ((General.homScHomologyEquiv A M N n).symm (QuotientAddGroup.mk f))) =
      CochainComplex.HomComplex.CohomologyClass.mk
        (dgFunctorCocycle F (General.scX₂ A M N n f.1)
          ((General.homSc_g_eq_zero_iff A M N n f.1).mp f.2))
```

**`DifferentialGradedModule.homAddEquiv_homologyAddEquiv_homologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DGFunctorHomComplexCohomology.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGFunctorHomComplexCohomology.lean#L277). The attribute's comment: “naturality of the cohomology of the Hom complex under a differential graded functor”.

> **Tag 09LC is natural under a differential graded functor**, read on homotopy classes. The
> degree-`n` cohomology class of the Hom complex `Hom^•_{(A, d)}(M, N)` attached to a closed
> degree-`n` homogeneous morphism `f` is the homotopy class of `f : M ⟶ N[n]`
> (`DifferentialGradedModule.General.closedToHomotopy`); its image under the degree-`n` cohomology
> of the map of Hom complexes induced by `F` is the homotopy class attached to the cocycle `F f`,
> and that class is the image of `f : M ⟶ N[n]` under the functor `F` induces on homotopy
> categories, followed by the comparison `F(N[n]) ≅ F(N)[n]` of
> `DifferentialGradedModule.dgFunctorToComplexesShiftIso`.

```lean
theorem homAddEquiv_homologyAddEquiv_homologyMap
    (f : ↥(AddCommGrpCat.Hom.hom (General.homSc A M N n).g).ker) :
    CochainComplex.HomComplex.CohomologyClass.homAddEquiv
        (CochainComplex.HomComplex.homologyAddEquiv ((dgFunctorToComplexes F).obj M)
          ((dgFunctorToComplexes F).obj N) n
          (HomologicalComplex.homologyMap (dgFunctorHomComplexMap F M N) n
            ((General.homScHomologyEquiv A M N n).symm (QuotientAddGroup.mk f)))) =
      (dgFunctorToHomotopyCategory F).map (General.closedToHomotopy A M N n f) ≫
        (HomotopyCategory.quotient B (ComplexShape.up ℤ)).map
          (dgFunctorToComplexesShiftIso F N n).hom
```

**`DifferentialGradedModule.General.homComplexHomologyEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/HomComplexExtGeneral.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/HomComplexExtGeneral.lean#L369). The attribute's comment: “the cohomology of the Hom complex in every degree, at independent universes”. References: SGA 4 XVII (2.2.8), “partial”.

> **Tag 09LC in every degree, at independent universes.** The degree-`n` cohomology of the
> differential graded Hom complex `Hom^•_{(A, d)}(L, M)` is the group of morphisms `L ⟶ M[n]` of the
> homotopy category of right differential graded `A`-modules.
>
> A degree-`n` cohomology class is a closed degree-`n` homogeneous map modulo coboundaries, a closed
> degree-`n` homogeneous map is a homomorphism `L ⟶ M[n]`, and a coboundary is a null-homotopic
> one.

```lean
def homComplexHomologyEquiv (n : ℤ) :
    ↥((homComplex A L M).homology n) ≃+
      ((toHomotopyCategory A).obj L ⟶ ((toHomotopyCategory A).obj M)⟦n⟧)
```

**`DifferentialGradedModule.homCohomologyZeroNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomCohomology.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomCohomology.lean#L192). The attribute's comment: “degree-zero cohomology of the internal hom, functorially”.

> **`H^0(Hom^•_B(N, -)) ≅ Hom_{K(B,d)}(N, -)` on the homotopy category.** Degree-zero
> cohomology of the internal hom out of a differential graded `(A, B)`-bimodule, as a functor on
> `K(B, d)`, is the module of morphisms out of `N` in `K(B, d)`.
>
> This is Tag 09LC read functorially: the left-hand side is the internal hom functor of Tag 0FQQ
> followed by the degree-zero cohomology functor of Tag 09KW.

```lean
def homCohomologyZeroNatIso :
    homHomotopyCategoryFunctor A B N L ⋙ degreeZeroCohomologyOnHomotopy' A ≅
      (linearCoyoneda R (HomotopyCategory B)).obj
        (Opposite.op ((toHomotopyCategory B).obj N))
```

Declarations registered for the tag:

- [`DifferentialGradedModule.dgCategory`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategory.lean#L175), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean#L38) (StacksFrontier): “composition”.
- [`DifferentialGradedModule.homogeneousMapComp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategory.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean#L39) (StacksFrontier): “composition”.
- [`DGCategory.comp_add_left`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.comp_add_left#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean#L40) (StacksFrontier): “composition”.
- [`DGCategory.comp_add_right`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.comp_add_right#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean#L41) (StacksFrontier): “composition”.
- [`DGCategory.comp_smul_left`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.comp_smul_left#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean#L42) (StacksFrontier): “composition”.
- [`DGCategory.comp_smul_right`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.comp_smul_right#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean#L43) (StacksFrontier): “composition”.
- [`DGCategory.leibniz`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.leibniz#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean#L44) (StacksFrontier): “composition”.
- [`DGCategory.assoc`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.assoc#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean#L45) (StacksFrontier): “composition”.
- [`DGCategory.id_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.id_comp#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean#L46) (StacksFrontier): “composition”.
- [`DGCategory.comp_id`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.comp_id#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean#L47) (StacksFrontier): “composition”.
- [`DGCategory.d_id`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.d_id#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryComposition.lean#L48) (StacksFrontier): “composition”.
- [`DifferentialGradedModule.homogeneousMapDifferential`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategory.lean#L113), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryDifferential.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryDifferential.lean#L36) (StacksFrontier): “hom_differential”.
- [`DGCategory.d_add`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.d_add#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryDifferential.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryDifferential.lean#L37) (StacksFrontier): “hom_differential”.
- [`DGCategory.d_smul`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.d_smul#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryDifferential.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryDifferential.lean#L38) (StacksFrontier): “hom_differential”.
- [`DGCategory.d_d`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DGCategory.d_d#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryDifferential.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DGCategoryDifferential.lean#L39) (StacksFrontier): “hom_differential”.

## Tag 09LD, a lemma

[Tag 09LD](https://stacks.math.columbia.edu/tag/09LD) in the Stacks Project.

**`DifferentialGradedModule.restrictScalarsDGFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/RestrictionDGFunctor.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/RestrictionDGFunctor.lean#L43).

> Restriction along a homomorphism of differential graded algebras, as a differential graded
> functor between the differential graded categories of right modules.

```lean
noncomputable def restrictScalarsDGFunctor (φ : A.Hom B) :
    { F : DGCategory.DGFunctor (dgCategory B) (dgCategory A) //
      (∀ N : DifferentialGradedModule B, F.obj N = restrictScalars φ N) ∧
      (∀ (L M : DifferentialGradedModule B) (n : ℤ) (f : (dgCategory B).Hom L M n),
        HEq (F.map f).1 f.1) }
```

## Tag 09LE, a lemma

[Tag 09LE](https://stacks.math.columbia.edu/tag/09LE) in the Stacks Project.

**`DifferentialGradedModule.endomorphismRepresentation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/EndomorphismDGA.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/EndomorphismDGA.lean#L82). The attribute's comment: “the endomorphism algebra of a differential graded module”.

> The data of Tag 09LE for the object `Q` of the differential graded category of right
> differential graded `B`-modules: its endomorphism differential graded algebra, the representable
> functor `Hom(Q, -)`, and the identifications that pin them down.

```lean
abbrev endomorphismRepresentation :
    DGCategory.HomRepresentation (dgCategory.{u, v, w} B) Q
```

**`CochainComplex.homShiftIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexShiftComparison.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexShiftComparison.lean#L135). The attribute's comment: “the shift comparison for the representable differential graded module”.

> **The shift comparison for `Hom(K, -)`.** For a cochain complex `K` in a preadditive
> category, the identification of a degree `k + n` cochain `K ⟶ X` with a degree `k` cochain
> `K ⟶ X[n]` is an isomorphism `Hom(K, X[n]) ≅ Hom(K, X)[n]` of differential graded modules over
> the endomorphism algebra `End(K)`.

```lean
noncomputable def homShiftIso (K : CochainComplex B ℤ) (n : ℤ) (X : CochainComplex B ℤ) :
    DGCategory.representableModule (dgCategory B) K (X⟦n⟧ : CochainComplex B ℤ) ≅
      (DGCategory.representableModule (dgCategory B) K X).shift n
```

**`DGCategory.homRepresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/HomRepresentation.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/HomRepresentation.lean#L106).

> The endomorphism differential graded algebra and representable differential graded functor
> `Hom(x, -)` of an object `x` of a differential graded category, with the induced functors on the
> category of complexes and on the homotopy category.

```lean
noncomputable def homRepresentation : HomRepresentation A x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.26, Tag 09L4](https://stacks.math.columbia.edu/tag/09L4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
