---
declaration: section
origin: cited
lean: DifferentialGraded.Bimodule.derivedExtensionEquivalence_functor_isTriangulated, DifferentialGraded.Bimodule.derivedExtensionEquivalence_inverse_isTriangulated, DifferentialGraded.Bimodule.isEquivalence_derivedTensorFunctor_regular, DifferentialGraded.Bimodule.derivedExtensionEquivalence, DifferentialGraded.Bimodule.derivedExtensionEquivalence_functor, DifferentialGraded.Bimodule.derivedExtensionEquivalence_inverse, DifferentialGraded.Bimodule.derivedExtensionEquivalence_linear, DifferentialGraded.Bimodule.isEquivalence_derivedTensorFunctor
statement: formalized
proof: formalized
---

# 22.37 Equivalences of derived categories

Section 22.37 of the Stacks Project, [Tag 09S5](https://stacks.math.columbia.edu/tag/09S5). 8 tags here are carried by 30 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09S6, a lemma

[Tag 09S6](https://stacks.math.columbia.edu/tag/09S6) in the Stacks Project.

**`DifferentialGraded.Bimodule.derivedExtensionEquivalence_functor_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceCompactGeneratorConverse.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceCompactGeneratorConverse.lean#L138). The attribute's comment: “the equivalence is one of TRIANGULATED categories: exactness of the functor - ⊗\_A^𝐋 B : D(A, d) ⥤ D(B, d), under the source's hypothesis that φ is an isomorphism on cohomology and no other”.

> For a homomorphism `φ : A ⟶ B` of differential graded `R`-algebras inducing an isomorphism
> on cohomology, the functor `- ⊗_A^𝐋 B : D(A, d) ⥤ D(B, d)` of `derivedExtensionEquivalence φ hφ`
> is a triangulated functor.

```lean
instance derivedExtensionEquivalence_functor_isTriangulated (φ : A.Hom B)
    (hφ : ∀ k : ℤ, Function.Bijective (φ.cohomologyMap k)) :
    (derivedExtensionEquivalence φ hφ).functor.IsTriangulated
```

**`DifferentialGraded.Bimodule.derivedExtensionEquivalence_inverse_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceCompactGeneratorConverse.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceCompactGeneratorConverse.lean#L161). The attribute's comment: “the equivalence is one of TRIANGULATED categories: exactness of the quasi-inverse, the restriction functor N ↦ N\_A, under the source's hypothesis that φ is an isomorphism on cohomology and no other”.

> For a homomorphism `φ : A ⟶ B` of differential graded `R`-algebras inducing an isomorphism
> on cohomology, the quasi-inverse `N ↦ N_A` of `derivedExtensionEquivalence φ hφ` is a triangulated
> functor.

```lean
instance derivedExtensionEquivalence_inverse_isTriangulated (φ : A.Hom B)
    (hφ : ∀ k : ℤ, Function.Bijective (φ.cohomologyMap k)) :
    (derivedExtensionEquivalence φ hφ).inverse.IsTriangulated
```

**`DifferentialGraded.Bimodule.isEquivalence_derivedTensorFunctor_regular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceQuasiIso.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceQuasiIso.lean#L301). The attribute's comment: “the equivalence of triangulated categories”.

> **Stacks 09S6**, in the form "`- ⊗_A^𝐋 B` is an equivalence". Let `φ : (A, d) → (B, d)` be a
> homomorphism of differential graded algebras over a commutative ring `R` which induces an
> isomorphism on cohomology algebras — that is, `H^k(φ) : H^k(A) → H^k(B)` is bijective for every
> `k : ℤ`. Then extension of scalars `- ⊗_A^𝐋 B : D(A, d) ⥤ D(B, d)`, the derived tensor product
> with the regular differential graded `(A, B)`-bimodule of Tag 0BYX, is an equivalence of
> categories.
>
> The functor is exact and `R`-linear before any hypothesis (Tags 09LR, 09LS and 09S7, all
> instances), so this is the source's `R`-linear equivalence of triangulated categories; the
> `R`-linearity is recorded separately at
> `DifferentialGraded.Bimodule.derivedExtensionEquivalence_linear`.
>
> This is Tag 09S7 for `N = B`. Its hypothesis (1) is
> `DifferentialGraded.Bimodule.isCompactObject_q_regular`, its hypothesis (2) is
> `DifferentialGradedModule.isWeakTriangulatedGenerator_q_regularModule` verbatim, and its
> hypothesis (3) is the hypothesis on `φ` through
> `DifferentialGraded.Bimodule.bijective_cohomologyEndomorphismComparison_regular_iff`.

```lean
theorem isEquivalence_derivedTensorFunctor_regular (φ : A.Hom B)
    (hφ : ∀ k : ℤ, Function.Bijective (φ.cohomologyMap k)) :
    (derivedTensorFunctor (Bimodule.regular φ)).IsEquivalence
```

**`DifferentialGraded.Bimodule.derivedExtensionEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceQuasiIso.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceQuasiIso.lean#L329). The attribute's comment: “the equivalence of triangulated categories with restriction of scalars as quasi-inverse”.

> **Stacks 09S6.** Let `φ : (A, d) → (B, d)` be a homomorphism of differential graded algebras
> over a commutative ring `R` inducing an isomorphism on cohomology algebras. Then extension of
> scalars `- ⊗_A^𝐋 B` is one half of an equivalence `D(A, d) ≌ D(B, d)` whose other half is
> derived restriction of scalars `N ↦ N_A`.
>
> The equivalence is `DifferentialGraded.Bimodule.derivedTensorEquivalence` (Tag 09S7) for the
> regular bimodule, whose quasi-inverse is derived Hom `RHom(B, -)`, transported along the
> identification of `RHom(B, -)` with derived restriction of scalars
> (`DifferentialGradedModule.DerivedHomData.functorIsoDerivedRestriction`, Example 22.33.2 of
> Tag 0BYX). `CategoryTheory.Equivalence.changeInverse` leaves the functor untouched and replaces
> the inverse by the isomorphic one, so both halves are what the source names:
> `DifferentialGraded.Bimodule.derivedExtensionEquivalence_functor` and
> `DifferentialGraded.Bimodule.derivedExtensionEquivalence_inverse` are both true by
> `rfl`.
>
> Both functors are exact: extension of scalars by Tags 09LR and 09LS, restriction of scalars as
> the right adjoint of an exact functor (Tag 0A8D). Both are `R`-linear by
> `DifferentialGraded.Bimodule.derivedExtensionEquivalence_linear`, so this is the source's
> `R`-linear equivalence of triangulated categories.

```lean
def derivedExtensionEquivalence (φ : A.Hom B)
    (hφ : ∀ k : ℤ, Function.Bijective (φ.cohomologyMap k)) :
    derivedCategory' A ≌ derivedCategory' B
```

**`DifferentialGraded.Bimodule.derivedExtensionEquivalence_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceQuasiIso.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceQuasiIso.lean#L342). The attribute's comment: “the functor of the equivalence is extension of scalars”.

> **The equivalence of Tag 09S6 goes by extension of scalars.**

```lean
theorem derivedExtensionEquivalence_functor (φ : A.Hom B)
    (hφ : ∀ k : ℤ, Function.Bijective (φ.cohomologyMap k)) :
    (derivedExtensionEquivalence φ hφ).functor = derivedTensorFunctor (Bimodule.regular φ)
```

**`DifferentialGraded.Bimodule.derivedExtensionEquivalence_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceQuasiIso.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceQuasiIso.lean#L350). The attribute's comment: “the quasi-inverse of the equivalence is restriction of scalars”.

> **The quasi-inverse of Tag 09S6 is restriction of scalars.** This is the half of the
> conclusion of Tag 09S6 that names the quasi-inverse: `N ↦ N_A`.

```lean
theorem derivedExtensionEquivalence_inverse (φ : A.Hom B)
    (hφ : ∀ k : ℤ, Function.Bijective (φ.cohomologyMap k)) :
    (derivedExtensionEquivalence φ hφ).inverse = derivedRestriction φ
```

**`DifferentialGraded.Bimodule.derivedExtensionEquivalence_linear`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceQuasiIso.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceQuasiIso.lean#L364). The attribute's comment: “the R-linearity of the equivalence and of its quasi-inverse”.

> **The equivalence of Tag 09S6 is `R`-linear.** This is the remaining half of the source's
> conclusion that `- ⊗_A^𝐋 B : D(A, d) → D(B, d)` is an *`R`-linear* equivalence of triangulated
> categories: both the functor and its quasi-inverse are `R`-linear.
>
> The functor is `- ⊗_A^𝐋 B` by `DifferentialGraded.Bimodule.derivedExtensionEquivalence_functor`,
> and `DifferentialGraded.Bimodule.derivedTensorFunctor_linear` (Tag 09S7) gives the `R`-linearity
> of the derived tensor product with any bimodule, with no hypotheses; the quasi-inverse of an
> `R`-linear equivalence is `R`-linear by `CategoryTheory.Equivalence.inverseLinear`.

```lean
theorem derivedExtensionEquivalence_linear (φ : A.Hom B)
    (hφ : ∀ k : ℤ, Function.Bijective (φ.cohomologyMap k)) :
    (derivedExtensionEquivalence φ hφ).functor.Linear R ∧
      (derivedExtensionEquivalence φ hφ).inverse.Linear R
```

## Tag 09S7, a lemma

[Tag 09S7](https://stacks.math.columbia.edu/tag/09S7) in the Stacks Project.

**`DifferentialGraded.Bimodule.isEquivalence_derivedTensorFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceBimodule.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceBimodule.lean#L244). The attribute's comment: “the equivalence of triangulated categories, not the R-linearity of the functor”.

> **Stacks 09S7.** Let `(A, d)` and `(B, d)` be differential graded algebras over a commutative
> ring `R` and let `N` be a differential graded `(A, B)`-bimodule. Assume
>
> 1. the class of `N` in `D(B, d)` is a compact object,
> 2. an object `X` of `D(B, d)` with `Hom_{D(B,d)}(N, X[n]) = 0` for every `n : ℤ` is zero, and
> 3. the canonical map `H^k(A) → Hom_{D(B,d)}(N, N[k])` of
>    `DifferentialGraded.Bimodule.cohomologyEndomorphismComparison` is bijective for every `k : ℤ`.
>
> Then `- ⊗_A^𝐋 N : D(A, d) ⥤ D(B, d)` is an equivalence of categories.
>
> The functor is exact with no hypothesis at all — it commutes with the translation by
> `DifferentialGraded.Bimodule.derivedTensorFunctor_commShift` and preserves distinguished
> triangles by `DifferentialGraded.Bimodule.derivedTensorFunctor_isTriangulated`, Tags 09LR and
> 09LS — so this is the source's equivalence of triangulated categories. What the clause string
> excludes is the source's `R`-linearity of the functor, which is not proved here.
>
> This is
> `DifferentialGraded.Bimodule.isEquivalence_derivedTensorFunctor_of_isWeakTriangulatedGenerator`,
> hypothesis (2) being weak generation of `D(B, d)` by the class of `N` ([Stacks, Tag 09SJ\](3)).

```lean
theorem isEquivalence_derivedTensorFunctor (N : Bimodule A B)
    [IsCompactObject.{u} ((toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj N.rightModule)]
    (h2 : ∀ X : derivedCategory' B,
      (∀ (n : ℤ) (f : (toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj N.rightModule ⟶
        X⟦n⟧), f = 0) → IsZero X)
    (h3 : ∀ k : ℤ, Function.Bijective (N.cohomologyEndomorphismComparison k)) :
    (derivedTensorFunctor N).IsEquivalence
```

**`DifferentialGraded.Bimodule.derivedTensorEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceBimodule.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceBimodule.lean#L267). The attribute's comment: “the equivalence, with RHom(N, -) as quasi-inverse; not the R-linearity”.

> **Stacks 09S7, as an equivalence with its quasi-inverse named.** Under the hypotheses of
> `DifferentialGraded.Bimodule.isEquivalence_derivedTensorFunctor`, the derived tensor product
> `- ⊗_A^𝐋 N` is one half of an equivalence `D(A, d) ≌ D(B, d)` whose other half is the derived
> Hom functor `RHom(N, -) : D(B, d) ⥤ D(A, d)` of Tag 09LI, with the unit and counit of the
> adjunction of Tag 09LT as the two structural isomorphisms.
>
> The source asserts only that `- ⊗_A^𝐋 N` *is* an equivalence and leaves the quasi-inverse
> unnamed; this records which functor it is. The unit is invertible by
> `DifferentialGraded.Bimodule.isIso_unit_derivedTensorFunctor_adj_derivedHomFunctor` (the heart of
> Tag 09R9), and the counit is invertible at every object because the functor is fully faithful and
> essentially surjective, so every object of `D(B, d)` lies in its essential image. Again only the
> equivalence is claimed, not its `R`-linearity.

```lean
def derivedTensorEquivalence (N : Bimodule A B)
    [IsCompactObject.{u} ((toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj N.rightModule)]
    (h2 : ∀ X : derivedCategory' B,
      (∀ (n : ℤ) (f : (toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj N.rightModule ⟶
        X⟦n⟧), f = 0) → IsZero X)
    (h3 : ∀ k : ℤ, Function.Bijective (N.cohomologyEndomorphismComparison k)) :
    derivedCategory' A ≌ derivedCategory' B
```

**`DifferentialGraded.Bimodule.derivedTensorFunctor_linear`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorLinear.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorLinear.lean#L164). The attribute's comment: “the R-linearity of the functor - ⊗\_A^𝐋 N”.

> **Stacks 09S7.** The derived tensor product `- ⊗_A^𝐋 N : D(A, d) ⥤ D(B, d)` is `R`-linear.
>
> This holds for every differential graded `(A, B)`-bimodule `N`, with none of the hypotheses of
> the tag: it is a property of the functor of Tag 09LS, not of the equivalence. Together with the
> exactness recorded by `DifferentialGraded.Bimodule.derivedTensorFunctor_commShift` and
> `DifferentialGraded.Bimodule.derivedTensorFunctor_isTriangulated` (Tags 09LR and 09LS) it is
> what makes the conclusion of Tag 09S7 an equivalence of `R`-linear triangulated categories.
>
> Every object of `D(A, d)` is isomorphic to the image of an object of `K(A, d)` orthogonal on the
> left to the acyclic modules, so `CategoryTheory.Functor.linear_iff` reduces the statement to
> `DifferentialGraded.Bimodule.derivedTensorFunctor_map_smul_id_q`.

```lean
instance derivedTensorFunctor_linear (N : Bimodule A B) :
    (derivedTensorFunctor N).Linear R
```

**`DifferentialGraded.Bimodule.derivedTensorEquivalence_linear`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorLinear.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorLinear.lean#L183). The attribute's comment: “the R-linearity of the equivalence and of its quasi-inverse”.

> **Stacks 09S7.** Under the three hypotheses of that tag, the equivalence
> `D(A, d) ≌ D(B, d)` of `DifferentialGraded.Bimodule.derivedTensorEquivalence` is `R`-linear in
> both directions: its functor is `- ⊗_A^𝐋 N`, which is `R`-linear, and the quasi-inverse of an
> `R`-linear equivalence is `R`-linear.

```lean
theorem derivedTensorEquivalence_linear (N : Bimodule A B)
    [IsCompactObject.{u} ((toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj N.rightModule)]
    (h2 : ∀ X : derivedCategory' B,
      (∀ (n : ℤ) (f : (toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj N.rightModule ⟶
        X⟦n⟧), f = 0) → IsZero X)
    (h3 : ∀ k : ℤ, Function.Bijective (N.cohomologyEndomorphismComparison k)) :
    (derivedTensorEquivalence N h2 h3).functor.Linear R ∧
      (derivedTensorEquivalence N h2 h3).inverse.Linear R
```

## Tag 09SS, a remark

[Tag 09SS](https://stacks.math.columbia.edu/tag/09SS) in the Stacks Project.

**`DifferentialGraded.Bimodule.isEquivalence_derivedTensorFunctor_of_triangEnvelope_eq_isCompactObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceClassicalGenerator.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceClassicalGenerator.lean#L253). The attribute's comment: “replacing condition (2) of 09S7 by classical generation of D\_compact(B, d)”.

> **Stacks 09SS, first assertion.** Let `(A, d)` and `(B, d)` be differential graded algebras
> over a commutative ring `R` and let `N` be a differential graded `(A, B)`-bimodule. Assume
>
> 1. the class of `N` in `D(B, d)` is a compact object,
> 2. `N` is a classical generator for `D_{compact}(B, d)`, that is, the triangulated envelope of the
>    class of `N` is exactly the subcategory of compact objects of `D(B, d)`, and
> 3. the canonical map `H^k(A) → Hom_{D(B,d)}(N, N[k])` of
>    `DifferentialGraded.Bimodule.cohomologyEndomorphismComparison` is bijective for every `k : ℤ`.
>
> Then `- ⊗_A^𝐋 N : D(A, d) ⥤ D(B, d)` is an equivalence of categories.
>
> This is [Stacks, Tag 09S7] with its hypothesis (2) replaced as Tag 09SS says it may be. Hypothesis
> (2) above gives that the class of the regular module `B`, being a compact object of `D(B, d)`,
> lies in the triangulated envelope of the class of `N`; since that class is a weak generator of
> `D(B, d)`, so is the class of `N`, by
> `CategoryTheory.ObjectProperty.isWeakTriangulatedGenerator_singleton_of_prop_triangEnvelope`. That
> is hypothesis (2) of Tag 09S7.
>
> As for Tag 09S7, the functor is exact and `R`-linear before any hypothesis (Tags 09LR, 09LS and
> 09S7), so this is the source's `R`-linear equivalence of triangulated categories, the
> `R`-linearity being recorded at
> `DifferentialGraded.Bimodule.linear_derivedTensorFunctor_of_isEquivalence`. The second
> assertion of the remark — that a weak generator of `D_{compact}(B, d)` suffices once `RHom(N, B)`
> is a compact object of `D(A, d)` — is the statement below,
> `isEquivalence_derivedTensorFunctor_of_isWeakTriangulatedGenerator_isCompactObject`.

```lean
theorem isEquivalence_derivedTensorFunctor_of_triangEnvelope_eq_isCompactObject (N : Bimodule A B)
    [IsCompactObject.{u} ((toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj N.rightModule)]
    (h2 : (ObjectProperty.singleton ((toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj
        N.rightModule)).triangEnvelope =
      IsCompactObject.{u, _, _} (C := derivedCategory' B))
    (h3 : ∀ k : ℤ, Function.Bijective (N.cohomologyEndomorphismComparison k)) :
    (derivedTensorFunctor N).IsEquivalence
```

## Tag 09S8, a lemma

[Tag 09S8](https://stacks.math.columbia.edu/tag/09S8) in the Stacks Project.

**`DifferentialGradedModule.exists_isCompactObject_and_isWeakGenerator_of_derivedEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceCompactGenerator.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceCompactGenerator.lean#L324). The attribute's comment: “(1) ⇒ (2), including the degree-zero clause as an R-algebra isomorphism A ≃ₐ[R] End P, with P the image of the regular module under the given equivalence; NOT (2) ⇒ (1) and NOT the source's final clause about the equivalence constructed from (2) — those are exists\_derivedEquivalence\_of\_isCompactObject\_and\_isWeakGenerator and the iff derivedEquivalence\_iff\_exists\_isCompactObject\_and\_isWeakGenerator, in the Converse file”.

> Let `(A, d)` and `(B, d)` be differential graded algebras over a commutative ring `R`, and
> assume `A = H^0(A)`, i.e. that every homogeneous component of `A` outside degree zero vanishes. Let
> `E : D(A, d) ≌ D(B, d)` be an `R`-linear, additive, shift-commuting equivalence. Then there is an
> object `P` of `D(B, d)` such that
>
> * `P` is a compact object of `D(B, d)`;
> * an object `N` of `D(B, d)` with `Hom_{D(B,d)}(P, N[i]) = 0` for every `i : ℤ` is zero;
> * `Hom_{D(B,d)}(P, P[i]) = 0` for `i ≠ 0`, and the endomorphism `R`-algebra of `P` is `A`;
>
> and `E` sends the regular module `A` to `P`. Indeed `P` is the image of the regular module.
>
> The degree-zero half of the third clause is an isomorphism of `R`-algebras `A ≃ₐ[R] End P`, which
> is what the source's "equal to `A`" says: `End P` is `Hom_{D(B,d)}(P, P[0])` with the shift by
> zero undone, and its ring structure is composition.
>
> The source's condition (1) is an equivalence of `R`-linear triangulated categories. What is
> assumed here is less: `Functor.IsTriangulated` is not used, only `Functor.Additive`, which it
> implies, together with `Functor.CommShift ℤ` and the `R`-linearity that "`R`-linear" provides.
> The final clause is the statement that the witness `P` may be taken to be `E(A)`, not the source's
> final clause about the equivalence constructed from (2).

```lean
theorem exists_isCompactObject_and_isWeakGenerator_of_derivedEquivalence
    (A B : DifferentialGradedAlgebra R) (hA : ∀ i : ℤ, i ≠ 0 → A.grading i = ⊥)
    (E : derivedCategory' A ≌ derivedCategory' B) [E.functor.Additive]
    [E.functor.Linear R] [E.functor.CommShift ℤ] :
    ∃ P : derivedCategory' B,
      IsCompactObject.{u} P ∧
      (∀ N : derivedCategory' B, (∀ (i : ℤ) (f : P ⟶ N⟦i⟧), f = 0) → IsZero N) ∧
      (∀ i : ℤ, i ≠ 0 → ∀ f : P ⟶ P⟦i⟧, f = 0) ∧
      Nonempty (A.A ≃ₐ[R] End P) ∧
      Nonempty (E.functor.obj
        ((toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj (regularModule A)) ≅ P)
```

**`DifferentialGraded.Bimodule.exists_derivedEquivalence_of_isCompactObject_and_isWeakGenerator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceCompactGeneratorConverse.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceCompactGeneratorConverse.lean#L298). The attribute's comment: “(2) ⇒ (1), by an additive R-linear shift-commuting triangulated equivalence, together with the source's final clause that the equivalence constructed in (2) sends A to P”.

> **Stacks 09S8, the implication (2) ⇒ (1), with the source's final clause.** Let `(A, d)` and
> `(B, d)` be differential graded `R`-algebras with `A = H^0(A)`, i.e. with every homogeneous
> component of `A` outside degree zero vanishing. Let `P` be an object of `D(B, d)` such that
>
> * `P` is a compact object of `D(B, d)`,
> * an object `N` of `D(B, d)` with `Hom_{D(B,d)}(P, N[i]) = 0` for every `i : ℤ` is zero,
> * `Hom_{D(B,d)}(P, P[i]) = 0` for `i ≠ 0`, and
> * the endomorphism `R`-algebra of `P` is `A`.
>
> Then `D(A, d)` and `D(B, d)` are equivalent by an additive, `R`-linear, shift-commuting and
> triangulated equivalence, **and that equivalence sends the regular module `A` to `P`** — the
> source's final clause.
>
> The proof replaces `P` by a property-(P) model `Q`, whose endomorphism differential graded algebra
> `E = End(Q)` makes `Q` an `(E, B)`-bimodule satisfying the hypotheses of [Stacks, Tag 09S7], and
> composes the equivalence that bimodule defines with the two equivalences of [Stacks, Tag 09S6]
> attached to the quasi-isomorphisms `(A, d) ← (E', d) → (E, d)` out of the degree-`≤ 0` truncation
> `E'` of `E`; see
> `DifferentialGradedModule.exists_hom_nonpositiveEndomorphismDGA_to_concentrated` and
> `DifferentialGraded.Bimodule.exists_derivedEquivalence_of_quasiIso_pair`.

```lean
theorem exists_derivedEquivalence_of_isCompactObject_and_isWeakGenerator
    (A B : DifferentialGradedAlgebra.{u, u} R)
    (hA : ∀ i : ℤ, i ≠ 0 → A.grading i = ⊥)
    (P : derivedCategory' B) (hcompact : IsCompactObject.{u} P)
    (hgen : ∀ N : derivedCategory' B, (∀ (i : ℤ) (f : P ⟶ N⟦i⟧), f = 0) → IsZero N)
    (hvan : ∀ i : ℤ, i ≠ 0 → ∀ f : P ⟶ P⟦i⟧, f = 0)
    (hend : Nonempty (A.A ≃ₐ[R] End P)) :
    ∃ G : derivedCategory' A ≌ derivedCategory' B,
      G.functor.Additive ∧ G.functor.Linear R ∧
        (∃ hs : G.functor.CommShift ℤ, letI := hs; G.functor.IsTriangulated) ∧
          Nonempty (G.functor.obj ((toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj
            (regularModule A)) ≅ P)
```

**`DifferentialGraded.Bimodule.derivedEquivalence_iff_exists_isCompactObject_and_isWeakGenerator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceCompactGeneratorConverse.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceCompactGeneratorConverse.lean#L354). The attribute's comment: “the equivalence of (1) and (2), with (1) as an additive R-linear shift-commuting triangulated equivalence and the degree-zero clause of (2) as an isomorphism of R-algebras A ≃ₐ[R] End P”.

> **Stacks 09S8.** Let `(A, d)` and `(B, d)` be differential graded algebras over a commutative
> ring `R` and assume `A = H^0(A)`. The following are equivalent.
>
> 1. `D(A, d)` and `D(B, d)` are equivalent as `R`-linear triangulated categories.
> 2. There is an object `P` of `D(B, d)` such that `P` is compact, an object `N` with
>    `Hom_{D(B,d)}(P, N[i]) = 0` for all `i : ℤ` is zero, `Hom_{D(B,d)}(P, P[i]) = 0` for `i ≠ 0`,
>    and the endomorphism `R`-algebra of `P` is `A`.
>
> Condition (1) is spelled as the existence of an equivalence of categories whose functor is
> additive, `R`-linear, commutes with the translation and is triangulated; the degree-zero clause of
> (2) is an isomorphism of `R`-algebras `A ≃ₐ[R] End P`, which is what the source's "equal to `A`"
> says, the ring structure on the right-hand side being composition.
>
> The implication (1) ⇒ (2) is
> `DifferentialGradedModule.exists_isCompactObject_and_isWeakGenerator_of_derivedEquivalence`, which
> needs only additivity, `R`-linearity and commutation with the translation; the converse is
> `DifferentialGraded.Bimodule`
> `.exists_derivedEquivalence_of_isCompactObject_and_isWeakGenerator`, which also proves the
> source's final clause that the equivalence it constructs sends `A` to `P`.

```lean
theorem derivedEquivalence_iff_exists_isCompactObject_and_isWeakGenerator
    (A B : DifferentialGradedAlgebra.{u, u} R)
    (hA : ∀ i : ℤ, i ≠ 0 → A.grading i = ⊥) :
    (∃ G : derivedCategory' A ≌ derivedCategory' B,
        G.functor.Additive ∧ G.functor.Linear R ∧
          ∃ hs : G.functor.CommShift ℤ, letI := hs; G.functor.IsTriangulated) ↔
      ∃ P : derivedCategory' B,
        IsCompactObject.{u} P ∧
          (∀ N : derivedCategory' B, (∀ (i : ℤ) (f : P ⟶ N⟦i⟧), f = 0) → IsZero N) ∧
            (∀ i : ℤ, i ≠ 0 → ∀ f : P ⟶ P⟦i⟧, f = 0) ∧ Nonempty (A.A ≃ₐ[R] End P)
```

## Tag 09S9, a remark

[Tag 09S9](https://stacks.math.columbia.edu/tag/09S9) in the Stacks Project.

**`DifferentialGradedModule.exists_dgModule_iso_obj_q_regularModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceRegularImage.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceRegularImage.lean#L90). The attribute's comment: “N = F(A) is represented by a differential graded B-module”.

> **Stacks 09S9.** The image `N = F(A)` of the regular module under a functor
> `F : D(A, d) ⥤ D(B, d)` is represented by a differential graded `B`-module.

```lean
theorem exists_dgModule_iso_obj_q_regularModule :
    ∃ N : DifferentialGradedModule B,
      Nonempty (F.obj ((toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj (regularModule A)) ≅
        (toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj N)
```

**`DifferentialGradedModule.isCompactObject_obj_q_regularModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceRegularImage.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceRegularImage.lean#L101). The attribute's comment: “N = F(A) is a compact object of D(B, d)”.

> **Stacks 09S9.** The image `N = F(A)` of the regular module under an additive equivalence
> `F : D(A, d) ⥤ D(B, d)` is a compact object of `D(B, d)`: the regular module is compact
> (`DifferentialGradedModule.isCompactObject_q_regularModule`) and compactness is invariant under
> an additive equivalence.

```lean
theorem isCompactObject_obj_q_regularModule [F.IsEquivalence] [F.Additive] :
    IsCompactObject.{u}
      (F.obj ((toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj (regularModule A)))
```

**`DifferentialGradedModule.isWeakTriangulatedGenerator_singleton_obj_q_regularModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceRegularImage.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceRegularImage.lean#L116). The attribute's comment: “N = F(A) generates D(B, d)”.

> **Stacks 09S9.** The image `N = F(A)` of the regular module under an additive equivalence
> `F : D(A, d) ⥤ D(B, d)` commuting with the translation generates `D(B, d)`: an object receiving
> only zero morphisms from the shifts of `N` is zero.
>
> The regular module generates `D(A, d)` (`DifferentialGradedModule`
> `.isWeakTriangulatedGenerator_q_regularModule`), so it suffices to carry a vanishing hypothesis
> on `K` back along `F`: a morphism `A ⟶ (F⁻¹K)[n]` becomes, under `F` and the commutation with
> the translation, a morphism `N ⟶ K[n]`, hence vanishes, hence vanishes itself because `F` is
> faithful. Then `F⁻¹K` is zero and so is `K`.

```lean
theorem isWeakTriangulatedGenerator_singleton_obj_q_regularModule
    [F.IsEquivalence] [F.Additive] [F.CommShift ℤ] :
    ObjectProperty.IsWeakTriangulatedGenerator (ObjectProperty.singleton
      (F.obj ((toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj (regularModule A))))
```

**`DifferentialGradedModule.cohomologyEquivDerivedHomObjRegular`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceRegularImage.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceRegularImage.lean#L143). The attribute's comment: “H^k(A) = Hom\_\{D(B,d)}(N, N[k])”.

> **Stacks 09S9.** For a fully faithful `F : D(A, d) ⥤ D(B, d)` commuting with the translation
> and `N = F(A)` the image of the regular module, `H^k(A) = Hom_{D(B, d)}(N, N[k])` for every
> `k ∈ ℤ`.
>
> This transports the bijection `H^k(A) ≃ Hom_{D(A, d)}(A, A[k])` of
> `DifferentialGradedModule.cohomologyEquivDerivedHom` along `F`, using the shift comparison
> `DifferentialGradedModule.regularShiftCompare` at the source and the commutation of `F` with the
> translation at the target.

```lean
def cohomologyEquivDerivedHomObjRegular [F.Full] [F.Faithful] [F.CommShift ℤ] (k : ℤ) :
    A.Cohomology k ≃
      (F.obj ((toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj (regularModule A)) ⟶
        (F.obj
          ((toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj (regularModule A)))⟦k⟧)
```

## Tag 09SA, a proposition

[Tag 09SA](https://stacks.math.columbia.edu/tag/09SA) in the Stacks Project.

**`DifferentialGraded.Bimodule.exists_bimodule_of_derivedEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceBimoduleExistence.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceBimoduleExistence.lean#L226). The attribute's comment: “the (A, B)-bimodule N as in Lemma 09S7, together with the equivalence it defines and the identification of its class in D(B, d) with F(A); the equivalence F is taken to be additive, R-linear and shift-commuting, Functor.IsTriangulated not being used”.

> **Stacks 09SA.** Let `R` be a commutative ring, let `(A, d)` and `(B, d)` be differential
> graded `R`-algebras and let `F : D(A, d) ≌ D(B, d)` be an additive, `R`-linear,
> shift-commuting equivalence. Assume
>
> 1. `A = H^0(A)`, i.e. every homogeneous component of `A` outside degree zero vanishes, and
> 2. `B` is K-flat as a complex of `R`-modules.
>
> Then there is a differential graded `(A, B)`-bimodule `N` as in [Stacks, Tag 09S7]: the class of
> `N` in `D(B, d)` is a compact object, it weakly generates `D(B, d)`, and the canonical map
> `H^k(A) → Hom_{D(B,d)}(N, N[k])` of
> `DifferentialGraded.Bimodule.cohomologyEndomorphismComparison` is bijective for every `k`.
> Consequently `- ⊗_A^𝐋 N : D(A, d) ⥤ D(B, d)` is an equivalence, and the class of `N` is `F(A)`.
>
> Hypothesis (1) enters through
> `DifferentialGradedModule.exists_hom_nonpositiveEndomorphismDGA_to_concentrated`, which needs the
> vanishing of `Hom_{D(B,d)}(Q, Q[k])` for `k ≠ 0` and the identification of `A` with the
> endomorphism algebra of the class of `Q`; hypothesis (2) enters only through Tag 09S4
> (`DifferentialGraded.Bimodule.derivedTensorFunctorCompIsoOfKFlatAlgebra`), which composes the
> three derived tensor functors of the proof into one.

```lean
theorem exists_bimodule_of_derivedEquivalence (A B : DifferentialGradedAlgebra.{u, u} R)
    (hA : ∀ i : ℤ, i ≠ 0 → A.grading i = ⊥)
    (hB : CochainComplex.KFlat.{u, u} (regularModule B).toCochainComplex)
    (F : derivedCategory' A ≌ derivedCategory' B) [F.functor.Additive]
    [F.functor.Linear R] [F.functor.CommShift ℤ] :
    ∃ N : Bimodule A B,
      IsCompactObject.{u}
          ((toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj N.rightModule) ∧
        (∀ X : derivedCategory' B,
            (∀ (n : ℤ) (f : (toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj N.rightModule ⟶
              X⟦n⟧), f = 0) → IsZero X) ∧
          (∀ k : ℤ, Function.Bijective (N.cohomologyEndomorphismComparison k)) ∧
            (derivedTensorFunctor N).IsEquivalence ∧
              Nonempty ((toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj N.rightModule ≅
                F.functor.obj ((toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj
                  (regularModule A)))
```

## Tag 09SC, a lemma

[Tag 09SC](https://stacks.math.columbia.edu/tag/09SC) in the Stacks Project.

**`DifferentialGradedModule.exists_isPerfect_and_detectsZero_of_derivedEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroRickard.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroRickard.lean#L159). The attribute's comment: “(1) ⇒ (2), with D(A) read as the derived category of right A-modules, clause (2)(a) as StacksDraft.Perfect.IsPerfect, Ext vanishing as Subsingleton of the shifted Hom group and the degree-zero clause of (2)(c) as an isomorphism of R-algebras A ≃ₐ[R] End P; NOT (2) ⇒ (1), which needs CategoryTheory.Functor.IsTriangulated for DifferentialGradedModule.degreeZeroDerivedEquivalence, and NOT part (3)”.

> **Stacks 09SC, the implication (1) ⇒ (2).** Let `R` be a commutative ring and let `A` and `B`
> be `R`-algebras, not assumed commutative. Let
>
> `E : D(Mod-A) ≌ D(Mod-B)`
>
> be an additive, `R`-linear, shift-commuting equivalence of the derived categories of right
> modules. Then there is an object `P` of `D(Mod-B)` such that
>
> * `P` can be represented by a finite complex of finite projective right `B`-modules, that is, `P`
>   is perfect;
> * an object `K` of `D(Mod-B)` with `Ext^i_B(P, K) = 0` for every `i : ℤ` is zero;
> * `Ext^i_B(P, P) = 0` for `i ≠ 0`, and the endomorphism `R`-algebra of `P` is `A`.
>
> The object `P` is produced by Tag 09S8 inside the differential graded world and carried across
> the degree-zero comparison `DifferentialGradedModule.degreeZeroDerivedEquivalence`; perfectness
> is compactness by Tag 07LT.
>
> The source's condition (1) is an equivalence of `R`-linear triangulated categories; what is
> assumed here is less, namely additivity, `R`-linearity and commutation with the translation,
> `CategoryTheory.Functor.IsTriangulated` not being used. The converse implication is not proved
> here: see the implementation notes of this file.

```lean
theorem exists_isPerfect_and_detectsZero_of_derivedEquivalence
    (E : DerivedCategory (ModuleCat.{u} Aᵐᵒᵖ) ≌ DerivedCategory (ModuleCat.{u} Bᵐᵒᵖ))
    [E.functor.Additive] [E.functor.Linear R] [E.functor.CommShift ℤ] :
    ∃ P : DerivedCategory (ModuleCat.{u} Bᵐᵒᵖ),
      StacksDraft.Perfect.IsPerfect P ∧
      (∀ K : DerivedCategory (ModuleCat.{u} Bᵐᵒᵖ),
        (∀ i : ℤ, Subsingleton (P ⟶ K⟦i⟧)) → IsZero K) ∧
      (∀ i : ℤ, i ≠ 0 → Subsingleton (P ⟶ P⟦i⟧)) ∧
      Nonempty (A ≃ₐ[R] End P)
```

**`DifferentialGradedModule.exists_bimodule_derivedTensorEquivalence_of_derivedEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroRickardBimodule.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroRickardBimodule.lean#L176). The attribute's comment: “(1) ⇒ (3) under B flat over R, with N a DIFFERENTIAL GRADED (A,B)-bimodule -- the chapter's own unqualified sense in 09SA/09S7, which 09SC(3) cites, and the ONLY reading under which (3) is true. The literal ordinary-bimodule reading is not merely unproved but FALSE: such an N would be a one-sided tilting module with End\_B(N) = A, hence projective and a progenerator over a finite-dimensional self-injective B, forcing A Morita equivalent to B -- so (3) would say derived equivalent self-injective algebras are Morita equivalent, refuted by Brauer tree algebras (Rickard). D(A) is the derived category of right A-modules. NOT (3) ⇒ (1)”.

> **Stacks 09SC, the implication (1) ⇒ (3).** Let `R` be a commutative ring, let `A` and `B`
> be `R`-algebras, not assumed commutative, and assume `B` is flat as an `R`-module. Let
>
> `E : D(Mod-A) ≌ D(Mod-B)`
>
> be an additive, `R`-linear, shift-commuting equivalence of the derived categories of right
> modules. Then there is a differential graded `(A, B)`-bimodule `N` over the degree-zero algebras
> `degreeZero R A` and `degreeZero R B` such that
>
> * `- ⊗_A^𝐋 N : D(degreeZero R A, d) ⥤ D(degreeZero R B, d)` is an equivalence, and
> * so is the functor `D(Mod-A) ⥤ D(Mod-B)` it induces along the degree-zero comparisons, which is
>   what the source's `- ⊗_A^𝐋 N : D(A) → D(B)` names.
>
> The bimodule is the one of [Stacks, Tag 09SA], applied to the equivalence `E` conjugated into the
> differential graded derived categories; its hypothesis `A = H^0(A)` holds because the degree-zero
> grading vanishes away from degree zero, and its K-flatness hypothesis is supplied from flatness
> of `B` over `R` by `DifferentialGradedModule.kFlat_regularModule_degreeZero_of_flat`.
>
> The source writes "`(A, B)`-bimodule" with no differential graded qualifier. What is proved here
> is the differential graded reading, which is what the proof the source cites — Tag 09SA, via
> Tag 09S7 — actually yields; the literal ordinary-bimodule reading is strictly stronger, is not
> established by anything the source cites, and is in fact false, by the self-injective
> counterexample in the implementation notes of this file.

```lean
theorem exists_bimodule_derivedTensorEquivalence_of_derivedEquivalence [Module.Flat R B]
    (E : DerivedCategory (ModuleCat.{u} Aᵐᵒᵖ) ≌ DerivedCategory (ModuleCat.{u} Bᵐᵒᵖ))
    [E.functor.Additive] [E.functor.Linear R] [E.functor.CommShift ℤ] :
    ∃ N : DifferentialGraded.Bimodule (degreeZero R A) (degreeZero R B),
      (derivedTensorFunctor N).IsEquivalence ∧
        ((degreeZeroDerivedEquivalence (R := R) (S := A) (A := Aᵐᵒᵖ)).inverse ⋙
          derivedTensorFunctor N ⋙
            (degreeZeroDerivedEquivalence (R := R) (S := B)
              (A := Bᵐᵒᵖ)).functor).IsEquivalence
```

**`DifferentialGradedModule.exists_derivedEquivalence_of_isPerfect_and_detectsZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroRickardConverse.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroRickardConverse.lean#L162). The attribute's comment: “(2) ⇒ (1), the converse of DegreeZeroRickard's (1) ⇒ (2), with the same spellings: clause (2)(a) as StacksDraft.Perfect.IsPerfect, Ext vanishing as Subsingleton of the shifted Hom group, the degree-zero clause of (2)(c) as A ≃ₐ[R] End P, and clause (1) delivered as an additive R-linear equivalence triangulated for SOME commutation with the translation, as in 09S8's own clause (1). D(A) is the derived category of right A-modules”.

> **Stacks 09SC, the implication (2) ⇒ (1).** Let `R` be a commutative ring and let `A` and `B`
> be `R`-algebras, not assumed commutative. Let `P` be an object of `D(Mod-B)` such that
>
> * `P` can be represented by a finite complex of finite projective right `B`-modules, that is, `P`
>   is perfect;
> * an object `K` of `D(Mod-B)` with `Ext^i_B(P, K) = 0` for every `i : ℤ` is zero;
> * `Ext^i_B(P, P) = 0` for `i ≠ 0`, and the endomorphism `R`-algebra of `P` is `A`.
>
> Then `D(Mod-A)` and `D(Mod-B)` are equivalent by an additive, `R`-linear equivalence which, for
> some commutation with the translation, is triangulated.
>
> The object `P` is carried back along the degree-zero comparison
> `DifferentialGradedModule.degreeZeroDerivedEquivalence` into `D(degreeZero R B, d)`, where
> [Stacks, Tag 09S8] produces an equivalence with `D(degreeZero R A, d)`; conjugating that
> equivalence by the two comparisons gives the conclusion, the comparisons being exact by
> `DifferentialGradedModule.degreeZeroDerivedEquivalence_functor_exact`. Compactness of `P` is its
> perfectness, by Tag 07LT.

```lean
theorem exists_derivedEquivalence_of_isPerfect_and_detectsZero
    (P : DerivedCategory (ModuleCat.{u} Bᵐᵒᵖ))
    (hperf : StacksDraft.Perfect.IsPerfect P)
    (hgen : ∀ K : DerivedCategory (ModuleCat.{u} Bᵐᵒᵖ),
      (∀ i : ℤ, Subsingleton (P ⟶ K⟦i⟧)) → IsZero K)
    (hvan : ∀ i : ℤ, i ≠ 0 → Subsingleton (P ⟶ P⟦i⟧))
    (hend : Nonempty (A ≃ₐ[R] End P)) :
    ∃ E : DerivedCategory (ModuleCat.{u} Aᵐᵒᵖ) ≌ DerivedCategory (ModuleCat.{u} Bᵐᵒᵖ),
      E.functor.Additive ∧ E.functor.Linear R ∧
        ∃ hs : E.functor.CommShift ℤ, letI := hs; E.functor.IsTriangulated
```

**`DifferentialGradedModule.derivedEquivalence_iff_exists_isPerfect_and_detectsZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroRickardConverse.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroRickardConverse.lean#L220). The attribute's comment: “the equivalence of (1) and (2), with clause (1) as an additive R-linear equivalence of the derived categories of right modules which is triangulated for SOME commutation with the translation, clause (2)(a) as StacksDraft.Perfect.IsPerfect, Ext vanishing as Subsingleton of the shifted Hom group and the degree-zero clause of (2)(c) as an isomorphism of R-algebras A ≃ₐ[R] End P”.

> **Stacks 09SC, the equivalence of (1) and (2).** Let `R` be a commutative ring and let `A`
> and `B` be `R`-algebras, not assumed commutative. The following are equivalent.
>
> 1. `D(Mod-A)` and `D(Mod-B)` are equivalent by an additive, `R`-linear equivalence which, for some
>    commutation with the translation, is triangulated.
> 2. There is an object `P` of `D(Mod-B)` which is perfect, for which an object `K` with
>    `Ext^i_B(P, K) = 0` for all `i : ℤ` is zero, with `Ext^i_B(P, P) = 0` for `i ≠ 0` and with
>    endomorphism `R`-algebra `A`.
>
> The implication `(1) ⇒ (2)` is
> `DifferentialGradedModule.exists_isPerfect_and_detectsZero_of_derivedEquivalence`, which needs
> only additivity, `R`-linearity and commutation with the translation; the converse is
> `DifferentialGradedModule.exists_derivedEquivalence_of_isPerfect_and_detectsZero`.

```lean
theorem derivedEquivalence_iff_exists_isPerfect_and_detectsZero :
    (∃ E : DerivedCategory (ModuleCat.{u} Aᵐᵒᵖ) ≌ DerivedCategory (ModuleCat.{u} Bᵐᵒᵖ),
        E.functor.Additive ∧ E.functor.Linear R ∧
          ∃ hs : E.functor.CommShift ℤ, letI := hs; E.functor.IsTriangulated) ↔
      ∃ P : DerivedCategory (ModuleCat.{u} Bᵐᵒᵖ),
        StacksDraft.Perfect.IsPerfect P ∧
        (∀ K : DerivedCategory (ModuleCat.{u} Bᵐᵒᵖ),
          (∀ i : ℤ, Subsingleton (P ⟶ K⟦i⟧)) → IsZero K) ∧
        (∀ i : ℤ, i ≠ 0 → Subsingleton (P ⟶ P⟦i⟧)) ∧
        Nonempty (A ≃ₐ[R] End P)
```

**`DifferentialGradedModule.exists_derivedEquivalence_of_bimodule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroRickardConverse.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroRickardConverse.lean#L257). The attribute's comment: “(3) ⇒ (1), the converse of DegreeZeroRickardBimodule's (1) ⇒ (3), with N a differential graded (A,B)-bimodule over the degree-zero algebras and the hypothesis that its differential graded derived tensor functor is an equivalence; no flatness of B over R is needed for this direction. Clause (1) is delivered as an additive R-linear equivalence of the derived categories of right modules which is triangulated for SOME commutation with the translation”.

> **Stacks 09SC, the implication (3) ⇒ (1).** Let `R` be a commutative ring, let `A` and `B` be
> `R`-algebras, not assumed commutative, and let `N` be a differential graded `(A, B)`-bimodule over
> the degree-zero algebras for which the derived tensor functor
>
> `- ⊗_A^𝐋 N : D(degreeZero R A, d) ⥤ D(degreeZero R B, d)`
>
> is an equivalence. Then `D(Mod-A)` and `D(Mod-B)` are equivalent by an additive, `R`-linear
> equivalence which, for some commutation with the translation, is triangulated.
>
> The derived tensor functor is additive, `R`-linear (Tag 09S7) and exact (Tags 09LR and 09LS), so
> conjugating it by the two degree-zero comparisons — exact by
> `DifferentialGradedModule.degreeZeroDerivedEquivalence_functor_exact` — gives the conclusion. No
> flatness hypothesis is needed for this direction.

```lean
theorem exists_derivedEquivalence_of_bimodule
    (N : DifferentialGraded.Bimodule (degreeZero R A) (degreeZero R B))
    (hN : (DifferentialGraded.Bimodule.derivedTensorFunctor N).IsEquivalence) :
    ∃ E : DerivedCategory (ModuleCat.{u} Aᵐᵒᵖ) ≌ DerivedCategory (ModuleCat.{u} Bᵐᵒᵖ),
      E.functor.Additive ∧ E.functor.Linear R ∧
        ∃ hs : E.functor.CommShift ℤ, letI := hs; E.functor.IsTriangulated
```

**`DifferentialGradedModule.derivedEquivalence_iff_exists_bimodule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroRickardConverse.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroRickardConverse.lean#L285). The attribute's comment: “the equivalence of (1) and (3) for B flat over R, with clause (1) as an additive R-linear equivalence of the derived categories of right modules which is triangulated for SOME commutation with the translation, and N a differential graded (A,B)-bimodule over the degree-zero algebras per 09SA/09S7 rather than an ordinary bimodule”.

> **Stacks 09SC, the equivalence of (1) and (3).** Let `R` be a commutative ring, let `A` and
> `B` be `R`-algebras, not assumed commutative, and assume `B` is flat as an `R`-module. The
> following are equivalent.
>
> 1. `D(Mod-A)` and `D(Mod-B)` are equivalent by an additive, `R`-linear equivalence which, for some
>    commutation with the translation, is triangulated.
> 3. There is a differential graded `(A, B)`-bimodule `N` over the degree-zero algebras for which
>    `- ⊗_A^𝐋 N : D(degreeZero R A, d) ⥤ D(degreeZero R B, d)` is an equivalence.
>
> The implication `(1) ⇒ (3)` is
> `DifferentialGradedModule.exists_bimodule_derivedTensorEquivalence_of_derivedEquivalence`, which
> is where flatness is used; the converse is
> `DifferentialGradedModule.exists_derivedEquivalence_of_bimodule`, which needs no flatness. The
> reading of "`(A, B)`-bimodule" is the differential graded one of
> `StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroRickardBimodule.lean`.

```lean
theorem derivedEquivalence_iff_exists_bimodule [Module.Flat R B] :
    (∃ E : DerivedCategory (ModuleCat.{u} Aᵐᵒᵖ) ≌ DerivedCategory (ModuleCat.{u} Bᵐᵒᵖ),
        E.functor.Additive ∧ E.functor.Linear R ∧
          ∃ hs : E.functor.CommShift ℤ, letI := hs; E.functor.IsTriangulated) ↔
      ∃ N : DifferentialGraded.Bimodule (degreeZero R A) (degreeZero R B),
        (DifferentialGraded.Bimodule.derivedTensorFunctor N).IsEquivalence
```

**`DifferentialGradedModule.degreeZeroHomotopyFunctor_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroTriangulated.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroTriangulated.lean#L214). The attribute's comment: “exactness of the degree-zero comparison on homotopy categories”.

> **The degree-zero comparison is exact on homotopy categories.** The functor
> `K(degreeZero R S, d) ⥤ K(A)` carries distinguished triangles to distinguished triangles: a
> distinguished triangle of `K(degreeZero R S, d)` is isomorphic to the triangle of an admissible
> short exact sequence, whose image is a degreewise split short exact sequence of cochain
> complexes.

```lean
theorem degreeZeroHomotopyFunctor_isTriangulated :
    (degreeZeroHomotopyFunctor R A (S := S)).IsTriangulated
```

**`DifferentialGradedModule.degreeZeroDerivedEquivalence_functor_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroTriangulated.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DegreeZeroTriangulated.lean#L296). The attribute's comment: “exactness of the degree-zero comparison equivalence of derived categories”.

> **The comparison equivalence of derived categories is exact.** For the commutation with the
> shift that the localization of the homotopy category induces on it, the equivalence
> `D(degreeZero R S, d) ≌ D(A)` carries distinguished triangles to distinguished triangles: it
> lifts the exact functor `K(degreeZero R S, d) ⥤ D(A)` of
> `DifferentialGradedModule.degreeZeroHomotopyFunctor_isTriangulated` along a localization of
> pretriangulated categories, and such a lift is exact.

```lean
theorem degreeZeroDerivedEquivalence_functor_exact :
    ∃ h : (degreeZeroDerivedEquivalence (R := R) (A := A)).functor.CommShift ℤ, letI := h;
      (degreeZeroDerivedEquivalence (R := R) (A := A)).functor.IsTriangulated
```

## Tag 09SD, a remark

[Tag 09SD](https://stacks.math.columbia.edu/tag/09SD) in the Stacks Project.

**`DerivedEquivalence.centerAlgEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DerivedEquivalenceCenter.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DerivedEquivalenceCenter.lean#L132). The attribute's comment: “Z(A) to Z(B) by transporting the shift-compatible centre along the equivalence”.

> **Derived equivalent algebras have isomorphic centres.** Let `A` and `B` be algebras over a
> commutative ring `R` whose derived categories are equivalent through an additive, `R`-linear,
> shift-commuting equivalence `E`. If the canonical maps from `Z(A)` and from `Z(B)` to the
> shift-compatible centres of `D(A)` and of `D(B)` are surjective — the step the Stacks project
> defers to Rickard, assumed here and not proved — then `Z(A)` and `Z(B)` are isomorphic as
> `R`-algebras, by transporting the shift-compatible centre along `E`.
>
> The `@[stacks 09SD]` part string below says "the centre of `DerivedCategory (ModuleCat A)`". Read
> that as the SHIFT-COMPATIBLE centre `CatCenter.shiftSubalgebra`, which is the correct object: the
> full `CatCenter` of the derived category is too big, being `∏_{n : ℤ} k` over a field `k`, so the
> hypothesis as originally stated here was unsatisfiable and has been replaced by surjectivity of
> `ModuleCat.centerToShiftCenterDerived`. See the note on Tag 09SD at the top of this file.

```lean
noncomputable def centerAlgEquiv
    (hA : Function.Surjective (ModuleCat.centerToShiftCenterDerived R A))
    (hB : Function.Surjective (ModuleCat.centerToShiftCenterDerived R B))
    (E : DerivedCategory (ModuleCat.{u} A) ≌ DerivedCategory (ModuleCat.{v} B))
    [E.functor.Additive] [E.functor.Linear R] [E.functor.CommShift ℤ] :
    (Subalgebra.center R A) ≃ₐ[R] (Subalgebra.center R B)
```

**`DerivedEquivalence.algEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DerivedEquivalenceCenter.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DerivedEquivalenceCenter.lean#L159). The attribute's comment: “the commutative case: A to B, a commutative algebra being its own centre”.

> **Derived equivalent commutative algebras are isomorphic.** A commutative algebra is its own
> centre, so the isomorphism of centres of `DerivedEquivalence.centerAlgEquiv` is an isomorphism
> `A ≃ₐ[R] B` when `A` and `B` are commutative. The same surjectivity of
> `ModuleCat.centerToShiftCenterDerived` is assumed and not proved.
>
> As for `centerAlgEquiv`, read "the centre of `DerivedCategory (ModuleCat A)`" in the part string
> below as the SHIFT-COMPATIBLE centre; the full `CatCenter` there is too big and the hypothesis as
> originally stated was unsatisfiable.

```lean
noncomputable def algEquiv
    (hA : Function.Surjective (ModuleCat.centerToShiftCenterDerived R A))
    (hB : Function.Surjective (ModuleCat.centerToShiftCenterDerived R B))
    (E : DerivedCategory (ModuleCat.{u} A) ≌ DerivedCategory (ModuleCat.{v} B))
    [E.functor.Additive] [E.functor.Linear R] [E.functor.CommShift ℤ] :
    A ≃ₐ[R] B
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.37, Tag 09S5](https://stacks.math.columbia.edu/tag/09S5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
