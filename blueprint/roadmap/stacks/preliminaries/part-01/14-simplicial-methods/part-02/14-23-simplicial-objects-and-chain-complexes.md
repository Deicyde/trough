---
declaration: section
origin: cited
lean: AlgebraicTopology.alternatingFaceMapComplex_preservesHomology, AlgebraicTopology.acyclic_alternatingFaceMapComplex_emEobj, AlgebraicTopology.homology_alternatingFaceMapComplex_eilenbergMacLane, AlgebraicTopology.inclusionOfMooreComplexMap, AlgebraicTopology.inclusionOfMooreComplexMap_f, AlgebraicTopology.isIsomorphic_normalizedMooreComplex_eilenbergMacLane_single, AlgebraicTopology.exists_degenerateComplex, AlgebraicTopology.exists_degenerateComplex_eq_sup_imageSubobject_σ
statement: formalized
proof: formalized
---

# 14.23 Simplicial objects and chain complexes

Section 14.23 of the Stacks Project, [Tag 0194](https://stacks.math.columbia.edu/tag/0194). 9 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0195, a lemma

[Tag 0195](https://stacks.math.columbia.edu/tag/0195) in the Stacks Project.

**`AlgebraicTopology.alternatingFaceMapComplex_preservesHomology`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplex.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/MooreComplex.lean#L373).

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

**`AlgebraicTopology.acyclic_alternatingFaceMapComplex_emEobj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplex.lean, line 700](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/MooreComplex.lean#L700).

> **Stacks 0196**.
> Let `𝒜` be an abelian category, let `A` be an object of `𝒜` and let `k ≥ 0` be an integer. The
> Moore complex `s(E)` of the simplicial object `E = emEobj A k` of [Stacks, Tag 0192], whose
> `n`-simplices are `⨁ A` over the monotone maps `α : [n] → [k + 1]` with image `[k]` or `[k + 1]`,
> is acyclic. Following Stacks, the maps `h_n : E_n ⟶ E_{n + 1}` sending the summand of `α` to the
> summand of its extension `α'` by `α'(n + 1) = k + 1` satisfy `d h_n - h_{n - 1} d = (-1)^(n + 1)`,
> so `(-1)^(n + 1) h_n` is a null-homotopy of the identity of `s(E)`.

```lean
public theorem acyclic_alternatingFaceMapComplex_emEobj :
    ((alternatingFaceMapComplex 𝒜).obj (emEobj A k)).Acyclic
```

## Tag 0197, a lemma

[Tag 0197](https://stacks.math.columbia.edu/tag/0197) in the Stacks Project.

**`AlgebraicTopology.homology_alternatingFaceMapComplex_eilenbergMacLane`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplexEilenbergMacLane.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/MooreComplexEilenbergMacLane.lean#L57).

> **Stacks 0197**.
> Let `C` be an abelian category, let `A` be an object of `C` and let `k ≥ 0` be an integer. The
> Moore complex `s(K(A, k))` of the Eilenberg-MacLane object `K(A, k) = i_{k!}U` has homology
> `H_k(s(K(A, k))) ≅ A` and `H_i(s(K(A, k))) = 0` for every `i ≠ k`.

```lean
public theorem homology_alternatingFaceMapComplex_eilenbergMacLane (A : C) (k : ℕ) :
    IsIsomorphic (((alternatingFaceMapComplex C).obj
        (SimplicialObject.eilenbergMacLane A k)).homology k) A ∧
      ∀ i ≠ k, IsZero (((alternatingFaceMapComplex C).obj
        (SimplicialObject.eilenbergMacLane A k)).homology i)
```

## Tag 0198, a lemma

[Tag 0198](https://stacks.math.columbia.edu/tag/0198) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicTopology.inclusionOfMooreComplexMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicTopology.inclusionOfMooreComplexMap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L77) (StacksFrontier): “the morphism of complexes N(U) -> s(U)”.
- [`AlgebraicTopology.inclusionOfMooreComplexMap_f`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicTopology.inclusionOfMooreComplexMap_f#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L79) (StacksFrontier): “its components are the inclusions N(U\_n) -> U\_n”.

## Tag 0199, a lemma

[Tag 0199](https://stacks.math.columbia.edu/tag/0199) in the Stacks Project.

**`AlgebraicTopology.isIsomorphic_normalizedMooreComplex_eilenbergMacLane_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplex.lean, line 778](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/MooreComplex.lean#L778).

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

**`AlgebraicTopology.exists_degenerateComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplex.lean, line 828](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/MooreComplex.lean#L828).

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

**`AlgebraicTopology.exists_degenerateComplex_eq_sup_imageSubobject_σ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplex.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/MooreComplex.lean#L252).

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

**`AlgebraicTopology.exactFunctor_normalizedMooreComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplex.lean, line 913](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/MooreComplex.lean#L913).

> **Stacks 019B**.
> The normalized complex functor `N : Simp(C) ⥤ Ch_{≥0}(C)` of an abelian category `C` is exact, i.e.
> it preserves finite limits and finite colimits.

```lean
public theorem exactFunctor_normalizedMooreComplex :
    exactFunctor (SimplicialObject C) (ChainComplex C ℕ) (normalizedMooreComplex C)
```

## Tag 019C, a lemma

[Tag 019C](https://stacks.math.columbia.edu/tag/019C) in the Stacks Project.

**`AlgebraicTopology.quasiIso_inclusionOfMooreComplexMap_and_acyclic_degenerateComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/MooreComplexQuasiIso.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/MooreComplexQuasiIso.lean#L70).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
