---
declaration: section
origin: cited
lean: CochainComplex.exists_sequence_quasiIso_truncLE, CategoryTheory.Functor.hasPointwiseLeftDerivedFunctor_of_acyclic_mapHomologicalComplex, CochainComplex.exists_sequence_quasiIso_truncGE
statement: formalized
proof: formalized
---

# 13.29 Unbounded complexes

Section 13.29 of the Stacks Project, [Tag 06XW](https://stacks.math.columbia.edu/tag/06XW). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06XX, a lemma

[Tag 06XX](https://stacks.math.columbia.edu/tag/06XX) in the Stacks Project.

**`CochainComplex.exists_sequence_quasiIso_truncLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/UnboundedComplexes/TruncLEResolutions.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/UnboundedComplexes/TruncLEResolutions.lean#L443).

> **Stacks 06XX.** Let `A` be an abelian category and let `P` be a class of objects of `A`
> which contains a zero object, is closed under finite direct sums, and is such that every object
> of `A` is a quotient of an object satisfying `P`. Let `K` be a cochain complex. Then there are
> complexes `Q n`, quasi-isomorphisms `f n : Q n ⟶ τ_{≤ n} K` and morphisms
> `g n : Q n ⟶ Q (n + 1)` forming a commutative ladder over the canonical truncations of `K`,
> such that (1) each `f n` is degreewise epimorphic, (2) each `Q n` is bounded above with all
> terms satisfying `P`, and (3) each `g n` is degreewise a split injection whose cokernel
> satisfies `P`.

```lean
public theorem exists_sequence_quasiIso_truncLE (P : ObjectProperty A) [P.ContainsZero]
    (hsum : ∀ X Y : A, P X → P Y → P (X ⊞ Y))
    (hP : ∀ X : A, ∃ (Y : A) (_ : P Y) (p : Y ⟶ X), Epi p) (K : CochainComplex A ℤ) :
    ∃ (Q : ℕ → CochainComplex A ℤ) (f : ∀ n : ℕ, Q n ⟶ K.truncLE n)
      (g : ∀ n : ℕ, Q n ⟶ Q (n + 1)),
      (∀ n, QuasiIso (f n)) ∧ (∀ (n : ℕ) (i : ℤ), Epi ((f n).f i)) ∧
        (∀ n : ℕ, (Q n).IsStrictlyLE n) ∧ (∀ (n : ℕ) (i : ℤ), P ((Q n).X i)) ∧
        (∀ (n : ℕ) (i : ℤ), ∃ (C : A) (_ : P C) (e : (Q (n + 1)).X i ≅ (Q n).X i ⊞ C),
          (g n).f i ≫ e.hom = biprod.inl) ∧
        (∀ n : ℕ, g n ≫ f (n + 1) ≫ K.ιTruncLE ((n + 1 : ℕ) : ℤ)
          = f n ≫ K.ιTruncLE ((n : ℕ) : ℤ))
```

## Tag 0794, a proposition

[Tag 0794](https://stacks.math.columbia.edu/tag/0794) in the Stacks Project.

**`CategoryTheory.Functor.hasPointwiseLeftDerivedFunctor_of_acyclic_mapHomologicalComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/UnboundedComplexes/LeftDerivedFunctor.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/UnboundedComplexes/LeftDerivedFunctor.lean#L417).

> **Stacks 0794.** Let `F : 𝒜 ⥤ ℬ` be a right exact functor of abelian categories and let `P`
> be a class of objects of `𝒜` which contains a zero object, is closed under finite direct sums,
> and is such that every object of `𝒜` is a quotient of an object satisfying `P`. Assume that
>
> 1. `F` turns every bounded above acyclic complex with all terms satisfying `P` into an acyclic
>    complex,
> 2. `𝒜` and `ℬ` have colimits of systems indexed by `ℕ`,
> 3. those colimits are exact in both `𝒜` and `ℬ`, and
> 4. `F` commutes with them.
>
> Then the left derived functor `LF` of `K(𝒜) ⥤ D(ℬ)`, `K ↦ F(K)`, along the localization
> `Qh : K(𝒜) ⥤ D(𝒜)` at quasi-isomorphisms is defined at every object, i.e. `LF` is defined on
> all of `D(𝒜)`.

```lean
public theorem hasPointwiseLeftDerivedFunctor_of_acyclic_mapHomologicalComplex
    (F : A ⥤ B) [F.Additive] [PreservesFiniteColimits F]
    (P : ObjectProperty A) [P.ContainsZero]
    (hsum : ∀ X Y : A, P X → P Y → P (X ⊞ Y))
    (hP : ∀ X : A, ∃ (Y : A) (_ : P Y) (p : Y ⟶ X), Epi p)
    (hFP : ∀ (a : ℤ) (L : CochainComplex A ℤ), L.IsStrictlyLE a → (∀ n, P (L.X n)) →
      L.Acyclic → ((F.mapHomologicalComplex (ComplexShape.up ℤ)).obj L).Acyclic)
    [HasColimitsOfShape ℕ A] [HasColimitsOfShape ℕ B]
    [HasExactColimitsOfShape ℕ A] [HasExactColimitsOfShape ℕ B]
    [PreservesColimitsOfShape ℕ F] :
    (F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).HasPointwiseLeftDerivedFunctor
      (HomotopyCategory.quasiIso A (ComplexShape.up ℤ))
```

## Tag 070F, a lemma

[Tag 070F](https://stacks.math.columbia.edu/tag/070F) in the Stacks Project.

**`CochainComplex.exists_sequence_quasiIso_truncGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/UnboundedComplexes/TruncGEResolutions.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/UnboundedComplexes/TruncGEResolutions.lean#L468).

> **Stacks 070F.** Let `A` be an abelian category and let `P` be a class of objects of `A`
> which contains a zero object, is closed under finite products, and is such that every object of
> `A` is a subobject of an object satisfying `P`. Let `K` be a cochain complex. Then there are
> complexes `I n`, quasi-isomorphisms `f n : τ_{≥ -n} K ⟶ I n` and morphisms
> `g n : I (n + 1) ⟶ I n` forming a commutative ladder under the canonical truncations of `K`,
> such that (1) each `f n` is degreewise monomorphic, (2) each `I n` is bounded below with all
> terms satisfying `P`, and (3) each `g n` is degreewise a split surjection whose kernel satisfies
> `P`. This is the dual of Stacks 06XX.

```lean
public theorem exists_sequence_quasiIso_truncGE (P : ObjectProperty A) [P.ContainsZero]
    (hprod : ∀ X Y : A, P X → P Y → P (X ⊞ Y))
    (hP : ∀ X : A, ∃ (Y : A) (_ : P Y) (i : X ⟶ Y), Mono i) (K : CochainComplex A ℤ) :
    ∃ (I : ℕ → CochainComplex A ℤ) (f : ∀ n : ℕ, K.truncGE (-(n : ℤ)) ⟶ I n)
      (g : ∀ n : ℕ, I (n + 1) ⟶ I n),
      (∀ n, QuasiIso (f n)) ∧ (∀ (n : ℕ) (i : ℤ), Mono ((f n).f i)) ∧
        (∀ n : ℕ, (I n).IsStrictlyGE (-(n : ℤ))) ∧ (∀ (n : ℕ) (i : ℤ), P ((I n).X i)) ∧
        (∀ (n : ℕ) (i : ℤ), ∃ (C : A) (_ : P C) (e : (I (n + 1)).X i ≅ (I n).X i ⊞ C),
          e.inv ≫ (g n).f i = biprod.fst) ∧
        (∀ n : ℕ, K.πTruncGE (-((n + 1 : ℕ) : ℤ)) ≫ f (n + 1) ≫ g n
          = K.πTruncGE (-(n : ℤ)) ≫ f n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.29, Tag 06XW](https://stacks.math.columbia.edu/tag/06XW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
