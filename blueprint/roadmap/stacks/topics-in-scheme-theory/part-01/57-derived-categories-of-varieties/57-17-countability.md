---
declaration: section
origin: cited
lean: AlgebraicGeometry.countable_hom_of_finiteType, AlgebraicGeometry.countable_isomorphismClasses_of_finiteType, AlgebraicGeometry.boundedDerivedCategory_essentiallyCountable, AlgebraicGeometry.essentiallyCountable_perfect_and_boundedCoherent_of_finiteType, AlgebraicGeometry.exists_countable_finiteType_isomorphism_families_of_isAlgClosed, AlgebraicGeometry.exists_countable_relativeEquivalenceKernels
statement: formalized
proof: formalized
---

# 57.17 Countability

Section 57.17 of the Stacks Project, [Tag 0G0T](https://stacks.math.columbia.edu/tag/0G0T). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G0U, a lemma

[Tag 0G0U](https://stacks.math.columbia.edu/tag/0G0U) in the Stacks Project.

**`AlgebraicGeometry.countable_hom_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Countability/FiniteTypeSchemes.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Countability/FiniteTypeSchemes.lean#L143). The attribute's comment: “countable\_hom”.

> Over a countable Noetherian ring, the morphisms over the base between two schemes of finite
> type form a countable type.

```lean
public theorem countable_hom_of_finiteType
    {R : Type u} [CommRing R] [Countable R] [IsNoetherianRing R]
    (X Y : Over (Spec (.of R)))
    [LocallyOfFiniteType X.hom] [QuasiCompact X.hom]
    [LocallyOfFiniteType Y.hom] [QuasiCompact Y.hom] :
    Countable (X ⟶ Y)
```

**`AlgebraicGeometry.countable_isomorphismClasses_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Countability/IsomorphismClasses.lean, line 536](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Countability/IsomorphismClasses.lean#L536). The attribute's comment: “countable\_iso\_classes”.

> There are countably many isomorphism classes of schemes of finite type over a countable
> Noetherian ring.

```lean
public theorem countable_isomorphismClasses_of_finiteType
    (R : Type u) [CommRing R] [Countable R] [IsNoetherianRing R] :
    Countable
      (Quotient (isIsomorphicSetoid
        (ObjectProperty.FullSubcategory (fun X : Over (Spec (.of R)) =>
          LocallyOfFiniteType X.hom ∧ QuasiCompact X.hom))))
```

## Tag 0G0V, a lemma

[Tag 0G0V](https://stacks.math.columbia.edu/tag/0G0V) in the Stacks Project.

**`AlgebraicGeometry.boundedDerivedCategory_essentiallyCountable`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Countability/BoundedDerivedCategory.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Countability/BoundedDerivedCategory.lean#L453).

> The bounded derived category of an essentially countable abelian category is essentially
> countable.

```lean
public instance boundedDerivedCategory_essentiallyCountable
    (A : Type u) [Category.{v} A] [Abelian A] [EssentiallyCountableCategory A] :
    EssentiallyCountableCategory (DerivedCategory.Bounded A)
```

## Tag 0G0W, a lemma

[Tag 0G0W](https://stacks.math.columbia.edu/tag/0G0W) in the Stacks Project.

**`AlgebraicGeometry.essentiallyCountable_perfect_and_boundedCoherent_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Countability/PerfectDerivedCategory.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Countability/PerfectDerivedCategory.lean#L209). The attribute's comment: “D\_perf(O\_X) and D^b\_Coh(O\_X) are countable categories”.

> **Stacks Project, Tag 0G0W.** Let `X` be a scheme of finite type over a countable Noetherian
> ring `R`. Then the categories `D_perf(𝒪_X)` and `D^b_Coh(𝒪_X)` are countable: each has
> countably many morphisms between any two objects and countably many isomorphism classes of
> objects, which is `CategoryTheory.EssentiallyCountableCategory`, the notion of countability of
> [Stacks, Section 0G0T]. Both are read as full subcategories of `D(𝒪_X)`, at any model of the
> derived category.
>
> As in the source: `X` is Noetherian, `D_perf(𝒪_X)` is a full subcategory of `D^b_Coh(𝒪_X)`
> ([Stacks, Tag 0FXU]), `D^b_Coh(𝒪_X) = D^b(Coh(𝒪_X))` ([Stacks, Tag 0FDB]), and the bounded
> derived category of the countable abelian category `Coh(𝒪_X)`
> (`AlgebraicGeometry.essentiallyCountable_coherentModules_of_finiteType`) is countable
> ([Stacks, Tag 0G0V]).

```lean
public theorem essentiallyCountable_perfect_and_boundedCoherent_of_finiteType {R : Type u}
    [CommRing R] [Countable R] [IsNoetherianRing R] {X : Scheme.{u}} (f : X ⟶ Spec (.of R))
    [LocallyOfFiniteType f] [QuasiCompact f]
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace)] :
    EssentiallyCountableCategory
        (ObjectProperty.FullSubcategory
          (fun K : DerivedCategory (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace) =>
            RingedSpace.IsPerfect (X := X.toRingedSpace) K)) ∧
      EssentiallyCountableCategory
        (ObjectProperty.FullSubcategory
          (DerivedCategoryB.derivedCategoryBBounded
            (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent)))
```

## Tag 0G0X, a lemma

[Tag 0G0X](https://stacks.math.columbia.edu/tag/0G0X) in the Stacks Project.

**`AlgebraicGeometry.exists_countable_finiteType_isomorphism_families_of_isAlgClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/CountableIsomorphismFamilies.lean, line 592](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/CountableIsomorphismFamilies.lean#L592).

> For `S` of finite type over an algebraically closed field `K` and `X, Y` of finite type over
> `S`, there is a countable set `I`, for each `i` a finite-type morphism `S i ⟶ S` and an
> isomorphism `X ×_S S i ≅ Y ×_S S i` over `S i`, such that every closed point of `S` valued in `K`
> whose two fibres are isomorphic over `K` lies in the image of some `S i ⟶ S`.

```lean
public theorem exists_countable_finiteType_isomorphism_families_of_isAlgClosed
    {K : Type u} [Field K] [IsAlgClosed K]
    (S : Over (Spec (.of K))) [LocallyOfFiniteType S.hom] [QuasiCompact S.hom]
    (X Y : Over S.left)
    [LocallyOfFiniteType X.hom] [QuasiCompact X.hom]
    [LocallyOfFiniteType Y.hom] [QuasiCompact Y.hom] :
    ∃ (I : Type (u + 1)) (_ : Countable I) (T : I → Over S.left)
      (_ : ∀ i, LocallyOfFiniteType (T i).hom ∧ QuasiCompact (T i).hom)
      (_ : ∀ i, (Over.pullback (T i).hom).obj X ≅ (Over.pullback (T i).hom).obj Y),
      ∀ (s : Over.mk (𝟙 (Spec (.of K))) ⟶ S),
        Nonempty ((Over.pullback s.left).obj X ≅ (Over.pullback s.left).obj Y) →
          ∃ (i : I) (t : Spec (.of K) ⟶ (T i).left),
            t ≫ (T i).hom = s.left
```

## Tag 0G0Y, a lemma

[Tag 0G0Y](https://stacks.math.columbia.edu/tag/0G0Y) in the Stacks Project.

**`AlgebraicGeometry.exists_countable_relativeEquivalenceKernels`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Countability/RelativeEquivalenceKernels.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Countability/RelativeEquivalenceKernels.lean#L54).

> **Stacks Project, Tag 0G0Y.** Let `K` be an algebraically closed field. There is a countable
> set `I` and for each `i ∈ I` a system `(Sᵢ/K, Xᵢ ⟶ Sᵢ, Yᵢ ⟶ Sᵢ, Mᵢ)` with
> 1. `Sᵢ` of finite type over `K`,
> 2. `Xᵢ ⟶ Sᵢ` and `Yᵢ ⟶ Sᵢ` proper and smooth,
> 3. `Mᵢ ∈ D_perf(𝒪_{Xᵢ ×_{Sᵢ} Yᵢ})` the Fourier-Mukai kernel of a relative equivalence from `Xᵢ`
>    to `Yᵢ` over `Sᵢ`,
> 4. for all smooth proper `K`-schemes `X`, `Y` with a `K`-linear exact equivalence
>    `D_perf(𝒪_X) ⟶ D_perf(𝒪_Y)` there are `i ∈ I` and `s ∈ Sᵢ(K)` with `X ≅ (Xᵢ)ₛ` and
>    `Y ≅ (Yᵢ)ₛ`.

```lean
theorem exists_countable_relativeEquivalenceKernels (K : Type u) [Field K] [IsAlgClosed K] :
    ∃ (I : Type (u + 1)) (_ : Countable I)
      (S : I → Over (Spec (.of K)))
      (X Y : (i : I) → Over (S i).left)
      (M : (i : I) → DerivedCategory (pullback (X i).hom (Y i).hom).Modules)
      (_ : ∀ i, LocallyOfFiniteType (S i).hom ∧ QuasiCompact (S i).hom)
      (_ : ∀ i, Smooth (X i).hom ∧ IsProper (X i).hom)
      (_ : ∀ i, Smooth (Y i).hom ∧ IsProper (Y i).hom)
      (_ : ∀ i, IsRelativeEquivalenceKernel (X i).hom (Y i).hom (M i)),
      ∀ (A B : Over (Spec (.of K))),
        Smooth A.hom → IsProper A.hom → Smooth B.hom → IsProper B.hom →
          (letI : Linear K A.left.Modules := modulesLinear K A
           letI : Linear K B.left.Modules := modulesLinear K B
           ∃ e : PerfectDerivedCategory A.left ≌ PerfectDerivedCategory B.left,
             e.functor.Linear K ∧
               ∃ h : e.functor.CommShift ℤ,
                 letI := h
                 e.functor.IsTriangulated) →
            ∃ (i : I) (s : Over.mk (𝟙 (Spec (.of K))) ⟶ S i),
              Nonempty (A ≅ (Over.pullback s.left).obj (X i)) ∧
                Nonempty (B ≅ (Over.pullback s.left).obj (Y i))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.17, Tag 0G0T](https://stacks.math.columbia.edu/tag/0G0T)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
