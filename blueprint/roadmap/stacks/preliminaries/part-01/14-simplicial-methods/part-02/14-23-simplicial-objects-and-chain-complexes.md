---
declaration: section
origin: cited
lean: AlgebraicTopology.alternatingFaceMapComplex_preservesHomology, AlgebraicTopology.DoldKan.acyclic_alternatingFaceMapComplex_Γ₀_double, AlgebraicTopology.DoldKan.homology_alternatingFaceMapComplex_Γ₀_single, AlgebraicTopology.inclusionOfMooreComplexMap, AlgebraicTopology.inclusionOfMooreComplexMap_f, AlgebraicTopology.isIsomorphic_normalizedMooreComplex_eilenbergMacLane_single, AlgebraicTopology.exists_degenerateComplex, AlgebraicTopology.exists_degenerateComplex_eq_sup_imageSubobject_σ
statement: formalized
proof: formalized
---

# 14.23 Simplicial objects and chain complexes

Section 14.23 of the Stacks Project, [Tag 0194](https://stacks.math.columbia.edu/tag/0194). 9 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0195, a lemma

[Tag 0195](https://stacks.math.columbia.edu/tag/0195) in the Stacks Project.

**`AlgebraicTopology.alternatingFaceMapComplex_preservesHomology`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplex.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/MooreComplex.lean#L370).

> **Stacks 0195**.
> The Moore complex functor `s : Simp(C) ⥤ Ch_{≥0}(C)`, sending a simplicial object `U` of a
> preadditive category `C` to the chain complex `U₀ ← U₁ ← U₂ ← …` with differentials the alternating
> sums of the face maps, is exact: it preserves kernels and cokernels.

```lean
public instance alternatingFaceMapComplex_preservesHomology :
    (alternatingFaceMapComplex C).PreservesHomology
```

## Tag 0196, a lemma

[Tag 0196](https://stacks.math.columbia.edu/tag/0196) in the Stacks Project.

**`AlgebraicTopology.DoldKan.acyclic_alternatingFaceMapComplex_Γ₀_double`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplex.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/MooreComplex.lean#L468).

> **Stacks 0196**.
> The Moore complex of the simplicial object `E` of [Stacks, Tag 0192], the termwise split extension
> of `K(A, k + 1)` by `K(A, k)`, that is `Γ₀` of the two-term complex `A --𝟙--> A` in degrees `k + 1`
> and `k`, is acyclic.

```lean
public theorem acyclic_alternatingFaceMapComplex_Γ₀_double (A : C) (k : ℕ) :
    K[Γ₀.obj (HomologicalComplex.double (𝟙 A)
      (show (ComplexShape.down ℕ).Rel (k + 1) k by simp))].Acyclic
```

## Tag 0197, a lemma

[Tag 0197](https://stacks.math.columbia.edu/tag/0197) in the Stacks Project.

**`AlgebraicTopology.DoldKan.homology_alternatingFaceMapComplex_Γ₀_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplex.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/MooreComplex.lean#L478).

> **Stacks 0197**.
> The Moore complex of the Eilenberg-MacLane object `K(A, k)` of an object `A` of an additive
> category with homology has homology `A` in degree `k` and zero homology in every other degree. Here
> `K(A, k)` is `Γ₀.obj L` for `L` the chain complex `A` concentrated in degree `k`.

```lean
public theorem homology_alternatingFaceMapComplex_Γ₀_single (A : C) (k : ℕ) :
    IsIsomorphic
        (K[Γ₀.obj ((HomologicalComplex.single C (ComplexShape.down ℕ) k).obj A)].homology k) A ∧
      ∀ i ≠ k, IsZero
        (K[Γ₀.obj ((HomologicalComplex.single C (ComplexShape.down ℕ) k).obj A)].homology i)
```

## Tag 0198, a lemma

[Tag 0198](https://stacks.math.columbia.edu/tag/0198) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicTopology.inclusionOfMooreComplexMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicTopology.inclusionOfMooreComplexMap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch14.lean#L76) (StacksFrontier): “the morphism of complexes N(U) -> s(U)”.
- [`AlgebraicTopology.inclusionOfMooreComplexMap_f`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicTopology.inclusionOfMooreComplexMap_f#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch14.lean#L78) (StacksFrontier): “its components are the inclusions N(U\_n) -> U\_n”.

## Tag 0199, a lemma

[Tag 0199](https://stacks.math.columbia.edu/tag/0199) in the Stacks Project.

**`AlgebraicTopology.isIsomorphic_normalizedMooreComplex_eilenbergMacLane_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplex.lean, line 561](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/MooreComplex.lean#L561).

> **Stacks 0199**.
> The normalized complex `N(K(A, k))` of the Eilenberg-MacLane object `K(A, k) = i_{k!}U` of an
> object `A` of an abelian category is isomorphic to the chain complex `A` concentrated in degree
> `k`; in particular `N(K(A, k))ᵢ` is `A` for `i = k` and `0` otherwise.

```lean
public theorem isIsomorphic_normalizedMooreComplex_eilenbergMacLane_single (A : C) (k : ℕ) :
    IsIsomorphic ((normalizedMooreComplex C).obj (SimplicialObject.eilenbergMacLane A k))
      ((HomologicalComplex.single C (ComplexShape.down ℕ) k).obj A)
```

## Tag 019A, a lemma

[Tag 019A](https://stacks.math.columbia.edu/tag/019A) in the Stacks Project.

**`AlgebraicTopology.exists_degenerateComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplex.lean, line 611](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/MooreComplex.lean#L611).

> **Stacks 019A**.
> Let `A` be an abelian category. The canonical morphism of chain complexes `N(U) ⟶ s(U)` from the
> normalized complex of a simplicial object `U` of `A` to its Moore complex is split, functorially in
> `U`: there are a functor `D` from simplicial objects of `A` to chain complexes, the degenerate
> part, and a natural isomorphism `N ⊞ D ≅ s` which on the first summand is the canonical inclusion.
> In other words `s(U) = N(U) ⊕ D(U)`, naturally in `U`.

```lean
public theorem exists_degenerateComplex :
    ∃ (D : SimplicialObject A ⥤ ChainComplex A ℕ)
      (e : normalizedMooreComplex A ⊞ D ≅ alternatingFaceMapComplex A),
      biprod.inl ≫ e.hom = inclusionOfMooreComplex A
```

## Tag 0FKI, a remark

[Tag 0FKI](https://stacks.math.columbia.edu/tag/0FKI) in the Stacks Project.

**`AlgebraicTopology.exists_degenerateComplex_eq_sup_imageSubobject_σ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplex.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/MooreComplex.lean#L252).

> **Stacks 0FKI**.
> Let `A` be an abelian category. The functorial splitting `s(U) = N(U) ⊕ D(U)` of the Moore complex
> of a simplicial object `U` of `A` along its normalized subcomplex ([Stacks, Tag 019A]) can be
> chosen so that the degenerate part is described degreewise as the subobject of `U_n` generated by
> the degenerate simplices: `D(U)_0 = 0` and `D(U)_{n + 1}` is the supremum of the images of the
> degeneracy operators `σ_i : U_n ⟶ U_{n + 1}`, `i = 0, …, n`. For a simplicial abelian group this
> says that the elements of `D(U)_n` are exactly the sums of degenerate `n`-simplices.

```lean
public theorem exists_degenerateComplex_eq_sup_imageSubobject_σ :
    ∃ (D : SimplicialObject A ⥤ ChainComplex A ℕ)
      (e : normalizedMooreComplex A ⊞ D ≅ alternatingFaceMapComplex A),
      biprod.inl ≫ e.hom = inclusionOfMooreComplex A ∧
        ∀ U : SimplicialObject A,
          IsZero ((D.obj U).X 0) ∧
            ∀ n : ℕ, imageSubobject (((biprod.inr ≫ e.hom).app U).f (n + 1)) =
              Finset.univ.sup fun i : Fin (n + 1) => imageSubobject (U.σ i)
```

## Tag 019B, a lemma

[Tag 019B](https://stacks.math.columbia.edu/tag/019B) in the Stacks Project.

**`AlgebraicTopology.exactFunctor_normalizedMooreComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplex.lean, line 696](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/MooreComplex.lean#L696).

> **Stacks 019B**.
> The normalized complex functor `N : Simp(C) ⥤ Ch_{≥0}(C)` of an abelian category `C` is exact, i.e.
> it preserves finite limits and finite colimits.

```lean
public theorem exactFunctor_normalizedMooreComplex :
    exactFunctor (SimplicialObject C) (ChainComplex C ℕ) (normalizedMooreComplex C)
```

## Tag 019C, a lemma

[Tag 019C](https://stacks.math.columbia.edu/tag/019C) in the Stacks Project.

**`AlgebraicTopology.quasiIso_inclusionOfMooreComplexMap_and_acyclic_degenerateComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplexQuasiIso.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/MooreComplexQuasiIso.lean#L70).

> Let `A` be an abelian category and let `V` be a simplicial object of `A`. The canonical
> morphism of chain complexes `N(V) ⟶ s(V)` is a quasi-isomorphism, and for every functorial
> splitting `e : N ⊞ D ≅ s` which on the first summand is the canonical inclusion, the complex `D(V)`
> is acyclic.

```lean
public theorem quasiIso_inclusionOfMooreComplexMap_and_acyclic_degenerateComplex
    (V : SimplicialObject A) :
    QuasiIso (inclusionOfMooreComplexMap V) ∧
      ∀ (D : SimplicialObject A ⥤ ChainComplex A ℕ)
        (e : normalizedMooreComplex A ⊞ D ≅ alternatingFaceMapComplex A),
        biprod.inl ≫ e.hom = inclusionOfMooreComplex A → (D.obj V).Acyclic
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.23, Tag 0194](https://stacks.math.columbia.edu/tag/0194)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
