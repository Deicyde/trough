---
declaration: section
origin: cited
lean: Deformation.Examples.ProjectiveGradedAlgebra, Deformation.Examples.ProjectiveGradedAlgebra.Hom, Deformation.Examples.ProjectiveGradedAlgebra.instCategory, Deformation.Examples.ProjectiveGradedAlgebra.projection, Deformation.Examples.ProjectiveGradedAlgebra.specialFiber, Deformation.Examples.ProjectiveGradedAlgebra.deformationCategory, Deformation.Examples.ProjectiveGradedAlgebra.projection_isCofiberedInGroupoids, Deformation.Examples.ProjectiveGradedAlgebra.satisfiesRS_projection
statement: formalized
proof: formalized
---

# 93.7 Graded algebras

Section 93.7 of the Stacks Project, [Tag 0DVX](https://stacks.math.columbia.edu/tag/0DVX). 4 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D3L, an example

[Tag 0D3L](https://stacks.math.columbia.edu/tag/0D3L) in the Stacks Project.

**`Deformation.Examples.ProjectiveGradedAlgebra`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean#L52). The attribute's comment: “graded\_algebra\_deformation\_category: objects”.

> A commutative graded algebra, finite projective in every degree, over an object of the
> category `𝒞_Λ` of Artinian local `Λ`-algebras with residue field `k`.

```lean
public structure ProjectiveGradedAlgebra (Λ : Type u) (k : Type w)
    [CommRing Λ] [Field k] [Algebra Λ k]
```

**`Deformation.Examples.ProjectiveGradedAlgebra.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean#L74). The attribute's comment: “graded\_algebra\_deformation\_category: morphisms”.

> A base-change morphism between graded algebras over varying base algebras: a graded ring
> map, semilinear over a morphism of base algebras, exhibiting the target as an extension of
> scalars of the source.

```lean
public structure Hom {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (X Y : ProjectiveGradedAlgebra.{u, v, w, m} Λ k)
```

**`Deformation.Examples.ProjectiveGradedAlgebra.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean#L95). The attribute's comment: “graded\_algebra\_deformation\_category: category structure”.

> The category structure on graded algebras over the algebras of `𝒞_Λ`.

```lean
public instance instCategory {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k] :
    Category (ProjectiveGradedAlgebra.{u, v, w, m} Λ k)
```

**`Deformation.Examples.ProjectiveGradedAlgebra.projection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean#L142). The attribute's comment: “graded\_algebra\_deformation\_category: projection”.

> The base-algebra projection.

```lean
public def projection {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k] :
    ProjectiveGradedAlgebra.{u, v, w, m} Λ k ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k
```

**`Deformation.Examples.ProjectiveGradedAlgebra.specialFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean#L151). The attribute's comment: “graded\_algebra\_deformation\_category: special fiber”.

> A graded algebra over `k` viewed as the distinguished special-fibre object.

```lean
public noncomputable def specialFiber {Λ : Type u} {k : Type w}
    [CommRing Λ] [Field k] [Algebra Λ k]
    (P : Type m) [CommRing P] [Algebra k P]
    (grading : ℕ → Submodule k P) [GradedAlgebra grading]
    [∀ d, Module.Finite k (grading d)] : ProjectiveGradedAlgebra.{u, w, w, m} Λ k
```

**`Deformation.Examples.ProjectiveGradedAlgebra.deformationCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean#L163). The attribute's comment: “graded\_algebra\_deformation\_category”.

> Deformations of a fixed graded `k`-algebra.

```lean
public abbrev deformationCategory {Λ : Type u} {k : Type w}
    [CommRing Λ] [Field k] [Algebra Λ k]
    (P : Type m) [CommRing P] [Algebra k P]
    (grading : ℕ → Submodule k P) [GradedAlgebra grading]
    [∀ d, Module.Finite k (grading d)]
```

**`Deformation.Examples.ProjectiveGradedAlgebra.deformationCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebras.lean#L163). The attribute's comment: “graded\_algebra\_deformation\_category: deformation category”.

> Deformations of a fixed graded `k`-algebra.

```lean
public abbrev deformationCategory {Λ : Type u} {k : Type w}
    [CommRing Λ] [Field k] [Algebra Λ k]
    (P : Type m) [CommRing P] [Algebra k P]
    (grading : ℕ → Submodule k P) [GradedAlgebra grading]
    [∀ d, Module.Finite k (grading d)]
```

**`Deformation.Examples.ProjectiveGradedAlgebra.projection_isCofiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebrasCofibered.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebrasCofibered.lean#L496).

> The base-algebra projection of the category of graded algebras, finite projective in each
> degree, is cofibered in groupoids.

```lean
public theorem projection_isCofiberedInGroupoids :
    IsCofiberedInGroupoids
      (ProjectiveGradedAlgebra.projection.{u, v, w, max v m} (Λ := Λ) (k := k))
```

## Tag 0DVY, a lemma

[Tag 0DVY](https://stacks.math.columbia.edu/tag/0DVY) in the Stacks Project.

**`Deformation.Examples.ProjectiveGradedAlgebra.satisfiesRS_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebrasRimSchlessinger.lean, line 881](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebrasRimSchlessinger.lean#L881). The attribute's comment: “Rim-Schlessinger condition”.

> The category of graded algebras finite projective in each degree satisfies the
> Rim–Schlessinger condition.

```lean
public theorem satisfiesRS_projection
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k] :
    SatisfiesRS
      (ProjectiveGradedAlgebra.projection.{u, v, w, max v m} (Λ := Λ) (k := k))
```

**`Deformation.Examples.ProjectiveGradedAlgebra.isDeformationCategory_deformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebrasRimSchlessinger.lean, line 932](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebrasRimSchlessinger.lean#L932). The attribute's comment: “deformation category”.

> The deformations of a fixed graded `k`-algebra, finite-dimensional in each degree, form a
> deformation category.

```lean
public theorem isDeformationCategory_deformationCategory
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (P : Type (max w m)) [CommRing P] [Algebra k P]
    (grading : ℕ → Submodule k P) [GradedAlgebra grading]
    [∀ d, Module.Finite k (grading d)] :
    IsDeformationCategory
      (objectsOverFunctor
        (ProjectiveGradedAlgebra.projection.{u, w, w, max w m} (Λ := Λ) (k := k))
        (specialFiber (Λ := Λ) P grading))
```

## Tag 0DVZ, a lemma

[Tag 0DVZ](https://stacks.math.columbia.edu/tag/0DVZ) in the Stacks Project.

**`Deformation.Examples.ProjectiveGradedAlgebra.infinitesimalAutomorphismGroupEquivDegreeZeroDerivations`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebraDerivations.lean, line 837](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebraDerivations.lean#L837). The attribute's comment: “graded\_inf\_derivations”.

> The infinitesimal automorphism group of the deformation category of a graded algebra is the
> additive group of degree-preserving derivations.

```lean
public noncomputable def infinitesimalAutomorphismGroupEquivDegreeZeroDerivations
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (P : Type (max w m)) [CommRing P] [Algebra k P]
    (grading : ℕ → Submodule k P) [GradedAlgebra grading]
    [∀ d, Module.Finite k (grading d)]
    {Aε : ArtinianLocalAlgCat.{u, w, w} Λ k}
    {x₀ : (objectsOverFunctor
      (ProjectiveGradedAlgebra.projection.{u, w, w, max w m} (Λ := Λ) (k := k))
      (specialFiber (Λ := Λ) P grading)).Fiber
        (residueFieldObject.{u, w, w} Λ k)}
    {xε : (objectsOverFunctor
      (ProjectiveGradedAlgebra.projection.{u, w, w, max w m} (Λ := Λ) (k := k))
      (specialFiber (Λ := Λ) P grading)).Fiber Aε}
    (g : residueFieldObject.{u, w, w} Λ k ⟶ Aε)
    (e : Aε ⟶ residueFieldObject.{u, w, w} Λ k)
    (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1)
    (hi : (objectsOverFunctor
      (ProjectiveGradedAlgebra.projection.{u, w, w, max w m} (Λ := Λ) (k := k))
      (specialFiber (Λ := Λ) P grading)).IsHomLift g i) :
    infinitesimalAutomorphismGroup
      (isDeformationCategory_deformationCategory P grading).predeformation
      g e hpair i hi ≃*
      Multiplicative (degreeZeroDerivations grading)
```

**`Deformation.Examples.ProjectiveGradedAlgebra.gradedAlgebra_infinitesimalAutomorphisms_finiteDimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebraDerivationsFiniteDimensional.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebraDerivationsFiniteDimensional.lean#L114). The attribute's comment: “graded\_inf\_finite”.

> **Stacks 0DVZ.** The infinitesimal automorphisms of the deformation category of a graded
> algebra of finite type over a field, with finite-dimensional graded pieces, form a
> finite-dimensional vector space whose addition is composition of automorphisms.

```lean
public theorem gradedAlgebra_infinitesimalAutomorphisms_finiteDimensional
    {Λ : Type u} {k : Type w} [CommRing Λ] [IsNoetherianRing Λ]
    [Field k] [Algebra Λ k] [Module.Finite Λ k]
    (P : Type (max w m)) [CommRing P] [Algebra k P]
    (grading : ℕ → Submodule k P) [GradedAlgebra grading]
    [∀ d, Module.Finite k (grading d)] [Algebra.FiniteType k P] :
    let p := objectsOverFunctor
      (ProjectiveGradedAlgebra.projection.{u, w, w, max w m} (Λ := Λ) (k := k))
      (specialFiber (Λ := Λ) P grading)
    let hp := (isDeformationCategory_deformationCategory (Λ := Λ) P grading).predeformation
    ∀ {Aε : ArtinianLocalAlgCat.{u, w, w} Λ k}
      {x₀ : p.Fiber (residueFieldObject.{u, w, w} Λ k)}
      {xε : p.Fiber Aε}
      (g : residueFieldObject.{u, w, w} Λ k ⟶ Aε)
      (e : Aε ⟶ residueFieldObject.{u, w, w} Λ k)
      (hpair : IsCanonicalDualNumberPair g e)
      (i : x₀.1 ⟶ xε.1) (hi : p.IsHomLift g i),
      let G := infinitesimalAutomorphismGroup hp g e hpair i hi
      ∃ hA : AddCommGroup G,
        letI := hA
        ∃ hM : Module k G,
          letI := hM
          (∀ a b : G, a + b = a * b) ∧ FiniteDimensional k G
```

**`Deformation.Examples.ProjectiveGradedAlgebra.finiteDimensional_tangentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebraTangentRecord.lean, line 706](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebraTangentRecord.lean#L706). The attribute's comment: “graded\_tangent\_finite”.

> **The tangent-space half of Stacks 0DVZ.** The tangent space of the deformation category of
> a graded `k`-algebra which is finite-dimensional in each degree and of finite type over `k` is
> finite-dimensional.
>
> The proof is Stacks' own: choose a weighted graded presentation of `P`
> (`GradedAlgebra.exists_weightedGradedPresentation`), attach to a lift of `P` over `k[V]` the
> class in `W ⊗[k] V` of the vector of obstructions of the lifted relations, where `W` is the
> cokernel of the graded Jacobian of the presentation
> (`Deformation.Examples.ProjectiveGradedAlgebra.tangentRecord`), and feed that map, its
> naturality and its injectivity to
> `Deformation.finiteDimensional_artinianTangentSpace_of_natural_injection` through
> `finiteDimensional_tangentSpace_of_gradedJacobian_natural_injection`. `W` is
> finite-dimensional because each graded piece of `P` is.

```lean
theorem finiteDimensional_tangentSpace :
    letI p := objectsOverFunctor
      (ProjectiveGradedAlgebra.projection.{u, w, w, max w m} (Λ := Λ) (k := k))
      (specialFiber (Λ := Λ) P grading)
    letI 𝓕 := BasedCategory.ofFunctor p
    letI hD := isDeformationCategory_deformationCategory (Λ := Λ) P grading
    letI hS2 := Artin.schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory 𝓕 hD
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨hD.predeformation⟩
    letI : Fact (SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses 𝓕 hD.predeformation.cofibered))) := ⟨hS2⟩
    letI T := artinianTangentSpace Λ k (isomorphismClasses 𝓕 hD.predeformation.cofibered)
    letI : AddCommGroup T := associatedTangentSpaceAddCommGroupUnlifted 𝓕
    letI : Module k T := associatedTangentSpaceModuleUnlifted 𝓕
    FiniteDimensional k T
```

## Tag 0ET3, a lemma

[Tag 0ET3](https://stacks.math.columbia.edu/tag/0ET3) in the Stacks Project.

**`Deformation.Examples.ProjectiveGradedAlgebra.exists_hull_isomorphismClasses_gradedAlgebra_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/GradedAlgebraHull.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/GradedAlgebraHull.lean#L219). The attribute's comment: “Def\_P of 0D3L: finite-dimensional graded pieces define it, not an extra hypothesis”.

> **Stacks 0ET3.** In Example 0D3L, assume `P` is a finitely generated graded `k`-algebra
> and `Λ → k` is the classical case (`Λ` a Noetherian complete local ring with residue field `k`).
> Then the functor `A ↦ Ob(Def_P(A))/≅` of isomorphism classes has a hull: a versal formal object
> with bijective differential.
>
> The section variable `[∀ d, Module.Finite k (grading d)]` is Example 0D3L's standing condition
> defining `Def_P`. The source requires `dim_k(P_d) < ∞` for all `d ≥ 0` before it forms
> `x_0 = (k, P)` and sets `Def_P = F_{x_0}`, and `specialFiber` requires the same condition to
> build `x_0`. It is not a hypothesis added to 0ET3. The only hypotheses that 0ET3 adds to
> Example 0D3L are finite generation, which is `[Algebra.FiniteType k P]`, and the classical case,
> which is `hΛ`.
>
> The proof applies `exists_hull_isomorphismClasses_gradedAlgebra`. Its hypothesis on the tangent
> space comes from `finiteDimensional_tangentSpace`, the tangent-space clause of Stacks 0DVZ,
> through the comparison of the two tangent-space models.

```lean
public theorem exists_hull_isomorphismClasses_gradedAlgebra_of_finiteType
    [Algebra.FiniteType k P] (hΛ : IsClassical Λ k) :
    ∃ ξ : FormalObject (CategoryOfElements.π (Deformation.isomorphismClasses
        (BasedCategory.ofFunctor (deformationProjection (Λ := Λ) P grading))
        (isPredeformationCategory_deformationProjection (Λ := Λ) P grading).cofibered)),
      IsVersal (categoryOfElements_projection_isCofibered (Deformation.isomorphismClasses
          (BasedCategory.ofFunctor (deformationProjection (Λ := Λ) P grading))
          (isPredeformationCategory_deformationProjection (Λ := Λ) P grading).cofibered)) ξ ∧
        HasBijectiveDifferential
          (categoryOfElements_projection_isCofibered (Deformation.isomorphismClasses
            (BasedCategory.ofFunctor (deformationProjection (Λ := Λ) P grading))
            (isPredeformationCategory_deformationProjection (Λ := Λ) P grading).cofibered))
          ξ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.7, Tag 0DVX](https://stacks.math.columbia.edu/tag/0DVX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
