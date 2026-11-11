---
declaration: section
origin: cited
lean: CategoryTheory.Pretriangulated.isEssentiallyConstant_op_iff_exists_iso_const_biprod, CategoryTheory.Pretriangulated.isEssentiallyConstant_op_π₂_and_exists_limit_triangle, DerivedCategory.isEssentiallyConstant_op_and_exists_limit_cone_of_homology, CategoryTheory.Pretriangulated.exists_proInverse_mor₁_of_proZero_π₃, DerivedCategory.exists_proInverse_of_proInverse_homology
statement: formalized
proof: formalized
---

# 13.42 Essentially constant systems

Section 13.42 of the Stacks Project, [Tag 0G38](https://stacks.math.columbia.edu/tag/0G38). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G39, a lemma

[Tag 0G39](https://stacks.math.columbia.edu/tag/0G39) in the Stacks Project.

**`CategoryTheory.Pretriangulated.isEssentiallyConstant_op_iff_exists_iso_const_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/EssentiallyConstant.lean, line 745](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/EssentiallyConstant.lean#L745).

> **Stacks 0G39**. An inverse system `A : J ⥤ 𝒟` in a pre-triangulated category, indexed by a
> cofiltered category `J`, is essentially constant as a pro-object (Stacks 05PU for `A.op`) if and
> only if there are an index `i`, an object `X` and an inverse system `Z : Over i ⥤ 𝒟` on the
> indices `j ≥ i` such that
>
> * `A_j ≅ X ⊞ Z_j` naturally in `j ≥ i` — so the transition morphisms respect the decomposition
>   and are the identity on `X` — and
> * for every `j ≥ i` there are `j' ≥ j` and a transition morphism `Z_{j'} ⟶ Z_j` equal to zero.
>
> The value of the essentially constant system is then `X`.

```lean
public theorem isEssentiallyConstant_op_iff_exists_iso_const_biprod [IsCofiltered J] (A : J ⥤ D) :
    IsEssentiallyConstantInd A.op ↔
      ∃ (i : J) (X : D) (Z : Over i ⥤ D)
        (_ : Over.forget i ⋙ A ≅ (Functor.const (Over i)).obj X ⊞ Z),
        ∀ j : Over i, ∃ (j' : Over i) (u : j' ⟶ j), Z.map u = 0
```

## Tag 0G3A, a lemma

[Tag 0G3A](https://stacks.math.columbia.edu/tag/0G3A) in the Stacks Project.

**`CategoryTheory.Pretriangulated.isEssentiallyConstant_op_π₂_and_exists_limit_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/EssentiallyConstant.lean, line 983](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/EssentiallyConstant.lean#L983).

> **Stacks 0G3A**. Let `T : J ⥤ Triangle 𝒟` be an inverse system of distinguished triangles
> `A_j ⟶ B_j ⟶ C_j ⟶ A_j[1]` in a pre-triangulated category, indexed by a cofiltered category `J`.
> If `(A_j)` and `(C_j)` are essentially constant as pro-objects (Stacks 05PU for the opposite
> diagrams), then so is `(B_j)`, and there are an index `n`, a distinguished triangle
> `S = (A ⟶ B ⟶ C ⟶ A[1])` of the values and a morphism of triangles `φ : T_n ⟶ S` which induces
> an isomorphism `lim_{j ≥ n} A_j ⟶ A`, and similarly for `B` and `C`: for each of the three terms
> there is a limit cone on the system restricted to the indices `j ≥ n` (the objects of `Over n`)
> whose apex is that term of `S` and whose leg at `n` is split by the corresponding component of
> `φ`.

```lean
public theorem isEssentiallyConstant_op_π₂_and_exists_limit_triangle [IsCofiltered J]
    (T : J ⥤ Triangle D) (hT : ∀ j, T.obj j ∈ distTriang D)
    (h₁ : IsEssentiallyConstantInd (T ⋙ Triangle.π₁).op)
    (h₃ : IsEssentiallyConstantInd (T ⋙ Triangle.π₃).op) :
    IsEssentiallyConstantInd (T ⋙ Triangle.π₂).op ∧
      ∃ (n : J) (S : Triangle D) (_ : S ∈ distTriang D) (φ : T.obj n ⟶ S)
        (πA : (Functor.const (Over n)).obj S.obj₁ ⟶ Over.forget n ⋙ T ⋙ Triangle.π₁)
        (πB : (Functor.const (Over n)).obj S.obj₂ ⟶ Over.forget n ⋙ T ⋙ Triangle.π₂)
        (πC : (Functor.const (Over n)).obj S.obj₃ ⟶ Over.forget n ⋙ T ⋙ Triangle.π₃),
        (πA.app (Over.mk (𝟙 n)) ≫ φ.hom₁ = 𝟙 S.obj₁ ∧ Nonempty (IsLimit (Cone.mk _ πA))) ∧
        (πB.app (Over.mk (𝟙 n)) ≫ φ.hom₂ = 𝟙 S.obj₂ ∧ Nonempty (IsLimit (Cone.mk _ πB))) ∧
        (πC.app (Over.mk (𝟙 n)) ≫ φ.hom₃ = 𝟙 S.obj₃ ∧ Nonempty (IsLimit (Cone.mk _ πC)))
```

## Tag 0G3B, a lemma

[Tag 0G3B](https://stacks.math.columbia.edu/tag/0G3B) in the Stacks Project.

**`DerivedCategory.isEssentiallyConstant_op_and_exists_limit_cone_of_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/EssentiallyConstant.lean, line 1210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/EssentiallyConstant.lean#L1210).

> Let `A : J ⥤ D(𝒜)` be an inverse system in the derived category of an abelian category, indexed
> by a cofiltered category `J`. Assume `H^i(A_j) = 0` for every `j` and every `i` outside an interval
> `[a, b]`, and that each inverse system `(H^i(A_j))_j` of `𝒜` is essentially constant (Stacks 05PU
> for the opposite diagram). Then `(A_j)` is essentially constant: besides
> `IsEssentiallyConstantInd A.op`, there are an index `n`, an object `X`, a morphism `φ : A_n ⟶ X`
> and a limit cone with apex `X` on the system restricted to the indices `j ≥ n` (the objects of
> `Over n`) whose leg at `n` is split by `φ`; and for every `i` the image of that cone under `H^i` is
> again a limit cone, i.e. `H^i(X)` is the value of the essentially constant system `(H^i(A_j))_j`.

```lean
public theorem isEssentiallyConstant_op_and_exists_limit_cone_of_homology
    [IsCofiltered J] (A : J ⥤ DerivedCategory 𝒜) (a b : ℤ)
    (hA : ∀ (i : ℤ), i < a ∨ b < i → ∀ j : J, IsZero ((homologyFunctor 𝒜 i).obj (A.obj j)))
    (hH : ∀ i : ℤ, IsEssentiallyConstantInd (A ⋙ homologyFunctor 𝒜 i).op) :
    IsEssentiallyConstantInd A.op ∧
      ∃ (n : J) (X : DerivedCategory 𝒜) (φ : A.obj n ⟶ X)
        (π : (Functor.const (Over n)).obj X ⟶ Over.forget n ⋙ A),
        π.app (Over.mk (𝟙 n)) ≫ φ = 𝟙 X ∧ Nonempty (IsLimit (Cone.mk X π)) ∧
        ∀ i : ℤ, Nonempty (IsLimit ((homologyFunctor 𝒜 i).mapCone (Cone.mk X π)))
```

## Tag 0G3C, a lemma

[Tag 0G3C](https://stacks.math.columbia.edu/tag/0G3C) in the Stacks Project.

**`CategoryTheory.Pretriangulated.exists_proInverse_mor₁_of_proZero_π₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/EssentiallyConstant.lean, line 1060](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/EssentiallyConstant.lean#L1060).

> **Stacks 0G3C**. Let `T : J ⥤ Triangle 𝒟` be an inverse system of distinguished triangles
> `A_j ⟶ B_j ⟶ C_j ⟶ A_j[1]` in a pre-triangulated category, indexed by a cofiltered category `J`.
> If the inverse system `(C_j)` of third terms is pro-zero, i.e. every index admits an arrow along
> which the transition morphism of third terms vanishes, then the morphisms `A_j ⟶ B_j` determine
> an isomorphism of pro-objects between `(A_j)` and `(B_j)`: for every index `j` there are an arrow
> `f : k ⟶ j` and a morphism `s : B_k ⟶ A_j` such that `A_k ⟶ B_k ⟶ A_j` is the transition morphism
> `A_k ⟶ A_j` and `B_k ⟶ A_j ⟶ B_j` is the transition morphism `B_k ⟶ B_j`.

```lean
public theorem exists_proInverse_mor₁_of_proZero_π₃ [IsCofiltered J]
    (T : J ⥤ Triangle D) (hT : ∀ j, T.obj j ∈ distTriang D)
    (h₃ : ∀ j : J, ∃ (k : J) (f : k ⟶ j), (T.map f).hom₃ = 0) (j : J) :
    ∃ (k : J) (f : k ⟶ j) (s : (T.obj k).obj₂ ⟶ (T.obj j).obj₁),
      (T.obj k).mor₁ ≫ s = (T.map f).hom₁ ∧ s ≫ (T.obj j).mor₁ = (T.map f).hom₂
```

## Tag 0G3D, a lemma

[Tag 0G3D](https://stacks.math.columbia.edu/tag/0G3D) in the Stacks Project.

**`DerivedCategory.exists_proInverse_of_proInverse_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/EssentiallyConstant.lean, line 1452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/EssentiallyConstant.lean#L1452).

> **Stacks 0G3D**. Let `α : A ⟶ B` be an inverse system of maps `A_j ⟶ B_j` of the derived
> category of an abelian category, indexed by a cofiltered category `J`. Assume `H^i(A_j) = 0` and
> `H^i(B_j) = 0` for every `j` and every `i` outside an interval `[a, b]`, and that for every `i`
> the maps `H^i(A_j) ⟶ H^i(B_j)` are an isomorphism of pro-objects of `𝒜`, i.e. every index `j`
> admits an arrow `f : k ⟶ j` and a morphism `H^i(B_k) ⟶ H^i(A_j)` whose two round trips are the
> transition morphisms. Then the maps `A_j ⟶ B_j` determine an isomorphism of pro-objects between
> `(A_j)` and `(B_j)`: for every index `j` there are an arrow `f : k ⟶ j` and a morphism
> `s : B_k ⟶ A_j` such that `A_k ⟶ B_k ⟶ A_j` is the transition morphism `A_k ⟶ A_j` and
> `B_k ⟶ A_j ⟶ B_j` is the transition morphism `B_k ⟶ B_j`.

```lean
public theorem exists_proInverse_of_proInverse_homology [IsCofiltered J]
    {A B : J ⥤ DerivedCategory 𝒜} (α : A ⟶ B) (a b : ℤ)
    (hA : ∀ i : ℤ, i < a ∨ b < i → ∀ j : J, IsZero ((homologyFunctor 𝒜 i).obj (A.obj j)))
    (hB : ∀ i : ℤ, i < a ∨ b < i → ∀ j : J, IsZero ((homologyFunctor 𝒜 i).obj (B.obj j)))
    (hH : ∀ (i : ℤ) (j : J), ∃ (k : J) (f : k ⟶ j)
      (s : (homologyFunctor 𝒜 i).obj (B.obj k) ⟶ (homologyFunctor 𝒜 i).obj (A.obj j)),
      (homologyFunctor 𝒜 i).map (α.app k) ≫ s = (homologyFunctor 𝒜 i).map (A.map f) ∧
        s ≫ (homologyFunctor 𝒜 i).map (α.app j) = (homologyFunctor 𝒜 i).map (B.map f))
    (j : J) :
    ∃ (k : J) (f : k ⟶ j) (s : B.obj k ⟶ A.obj j),
      α.app k ≫ s = A.map f ∧ s ≫ α.app j = B.map f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.42, Tag 0G38](https://stacks.math.columbia.edu/tag/0G38)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
