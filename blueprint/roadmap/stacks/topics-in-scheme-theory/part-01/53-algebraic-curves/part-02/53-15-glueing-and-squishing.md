---
declaration: section
origin: cited
lean: Algebra.algEquiv_prod_or_dualNumber_of_natCard_subalgebra_eq_two, Algebra.algEquiv_prod_or_dualNumber_of_no_intermediateSubalgebra, AlgebraicGeometry.IsGlueingTwoPoints, Stacks.GlueSquishUnits.isShortExact_units_of_isGlueingTwoPoints, Stacks.SquishSheafSequence.shortExact_units_of_isSquishingTangentVector, AlgebraicGeometry.IsSquishingTangentVector, Stacks.SquishSheafSequence.shortExact_of_isSquishingTangentVector, Stacks.GlueSquishFactor.algEquiv_prod_or_dualNumber_of_minimal
statement: formalized
proof: formalized
---

# 53.15 Glueing and squishing

Section 53.15 of the Stacks Project, [Tag 0C1H](https://stacks.math.columbia.edu/tag/0C1H). 6 tags here are carried by 34 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C1I, a lemma

[Tag 0C1I](https://stacks.math.columbia.edu/tag/0C1I) in the Stacks Project.

**`Algebra.algEquiv_prod_or_dualNumber_of_natCard_subalgebra_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SubalgebraClassification.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SubalgebraClassification.lean#L270).

> **Stacks Project, Tag 0C1I.** An algebra over an algebraically closed field with exactly
> two subalgebras is isomorphic, as an algebra, either to the product algebra or to the dual
> numbers.

```lean
theorem algEquiv_prod_or_dualNumber_of_natCard_subalgebra_eq_two
    (k : Type u) (A : Type v) [Field k] [IsAlgClosed k] [CommRing A] [Algebra k A]
    (h : Nat.card (Subalgebra k A) = 2) :
    Nonempty (A ≃ₐ[k] k × k) ∨ Nonempty (A ≃ₐ[k] DualNumber k)
```

**`Algebra.algEquiv_prod_or_dualNumber_of_no_intermediateSubalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SubalgebraClassification.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SubalgebraClassification.lean#L285).

> **Stacks Project, Tag 0C1I.** An algebra over an algebraically closed field with no proper
> intermediate subalgebra is either the product algebra or the algebra of dual numbers.

```lean
theorem algEquiv_prod_or_dualNumber_of_no_intermediateSubalgebra
    (k : Type u) (A : Type v) [Field k] [IsAlgClosed k] [CommRing A] [Algebra k A]
    (h_ne : (⊥ : Subalgebra k A) ≠ ⊤)
    (h : ∀ B : Subalgebra k A, B = ⊥ ∨ B = ⊤) :
    Nonempty (A ≃ₐ[k] k × k) ∨ Nonempty (A ≃ₐ[k] DualNumber k)
```

## Tag 0C1J, an example

[Tag 0C1J](https://stacks.math.columbia.edu/tag/0C1J) in the Stacks Project.

**`AlgebraicGeometry.IsGlueingTwoPoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingTwoPoints.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingTwoPoints.lean#L142). The attribute's comment: “glueing\_two\_points”.

> A morphism of algebraic `k`-schemes glues the distinct rational points `a` and `b` if
> they have the same image, the morphism is finite and is an isomorphism off that image, and
> the additive difference of evaluation at `a` and `b` gives the skyscraper quotient of its
> pushforward structure sheaf.

```lean
def IsGlueingTwoPoints {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (a b : Spec (.of k) ⟶ X') : Prop
```

**`Stacks.GlueSquishUnits.isShortExact_units_of_isGlueingTwoPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingUnitsSequence.lean, line 839](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingUnitsSequence.lean#L839). The attribute's comment: “the units short exact sequence”.

> **The short exact sequence of sheaves of units of a glueing of two rational points.**
> If `f : X' ⟶ X` glues the distinct rational points `a` and `b` of `X'` to the point
> `x = f(a) = f(b)` of `X`, then
>
> `1 ⟶ 𝒪_X^* ⟶ f_*𝒪_{X'}^* ⟶ (k^*)_x ⟶ 1`
>
> is a short exact sequence of sheaves of abelian groups on `X`, the first map being pullback of
> units along `f` and the second the ratio `h ↦ h(a) h(b)⁻¹` of the two values of a unit. Both
> maps are pinned down on sections, so the sequence is the one of [Stacks, Tag 0C1J] and not
> merely some exact sequence with those terms.
>
> This is the input from which [Stacks, Tag 0C1M] obtains the exact sequence
> `k^* ⟶ Pic(X) ⟶ Pic(X') ⟶ 0`: the five-term low-degree cohomology sequence over `U = ⊤`,
> `Stacks.Cohomology.AbelianColimit.H'longExactSequence_exact`, gives
> `H⁰(X, f_*𝒪_{X'}^*) ⟶ k^* ⟶ H¹(X, 𝒪_X^*) ⟶ H¹(X, f_*𝒪_{X'}^*)`, and
> `Stacks.Cohomology.Generators.h1UnitsAddEquivPicardGroup` identifies the first cohomology of a
> units sheaf with the Picard group.

```lean
theorem isShortExact_units_of_isGlueingTwoPoints {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (a b : Spec (.of k) ⟶ X')
    (h : IsGlueingTwoPoints f a b) (hab : a ≫ f = b ≫ f) :
    ∃ (φ : unitsSheaf X.toLocallyRingedSpace.toRingedSpace ⟶
        (TopCat.Sheaf.pushforward AddCommGrpCat.{u} f.base).obj
          (unitsSheaf X'.toLocallyRingedSpace.toRingedSpace))
      (ψ : (TopCat.Sheaf.pushforward AddCommGrpCat.{u} f.base).obj
          (unitsSheaf X'.toLocallyRingedSpace.toRingedSpace) ⟶
        skyscraperUnitsSheaf (k := k) X (gluedPoint f a))
      (hzero : φ ≫ ψ = 0),
      (ShortComplex.mk φ ψ hzero).ShortExact ∧
      (∀ (U : X.Opens) (s : Γ(X, U)ˣ),
        φ.hom.app (op U) (Additive.ofMul s) =
          Additive.ofMul (Units.map (f.app U).hom.toMonoidHom s)) ∧
      (∀ (U : X.Opens) (hz : gluedPoint f a ∈ U)
        (ha : a.base (IsLocalRing.closedPoint k) ∈ f ⁻¹ᵁ U)
        (hb : b.base (IsLocalRing.closedPoint k) ∈ f ⁻¹ᵁ U) (s : Γ(X', f ⁻¹ᵁ U)ˣ),
        skyscraperUnitsEval X (gluedPoint f a) hz
            (ψ.hom.app (op U) (Additive.ofMul s)) =
          Additive.ofMul (unitRatioAt a b (f ⁻¹ᵁ U) ha hb s))
```

## Tag 0C1K, an example

[Tag 0C1K](https://stacks.math.columbia.edu/tag/0C1K) in the Stacks Project.

**`Stacks.SquishSheafSequence.shortExact_units_of_isSquishingTangentVector`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicardSequence.lean, line 671](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicardSequence.lean#L671). The attribute's comment: “the units short exact sequence”.

> **The short exact sequence of sheaves of units of the squishing of a tangent vector.**
> If `f : X' ⟶ X` squishes the tangent vector `ϑ` of `X'` to the rational point `x` of `X`, then
>
> `1 ⟶ 𝒪_X^* ⟶ f_*𝒪_{X'}^* ⟶ (k, +)_x ⟶ 1`
>
> is a short exact sequence of sheaves of abelian groups on `X`, the first map being pullback of
> units along `f` and the second the logarithmic `ε`-derivative along `ϑ`. Both maps are pinned
> down on sections — by `Stacks.GlueSquishUnits.unitsPushforwardMap_app` and
> `Stacks.SquishSheafSequence.epsilonLogDerivSheafHom_app` — so the sequence is the one of
> [Stacks, Tag 0C1N] and not merely some exact sequence with those terms.
>
> Injectivity of the first map and exactness in the middle hold already on sections over every
> open. Surjectivity of the second is local at the contracted point, where it is the surjectivity
> of the logarithmic `ε`-derivative on the units of the stalk of `f_*𝒪_{X'}`; away from the
> contracted point the skyscraper has no sections.

```lean
theorem shortExact_units_of_isSquishingTangentVector {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (θ : Spec (.of (DualNumber k)) ⟶ X')
    (h : AlgebraicGeometry.IsSquishingTangentVector f θ) :
    (ShortComplex.mk (unitsPushforwardMap f) (epsilonLogDerivSheafHom f θ)
      (unitsPushforwardMap_comp_epsilonLogDerivSheafHom f θ h)).ShortExact
```

**`AlgebraicGeometry.IsSquishingTangentVector`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingTangentVector.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingTangentVector.lean#L77). The attribute's comment: “squishing\_tangent\_vector”.

> A morphism of algebraic `k`-schemes squishes a tangent vector if that vector is a closed
> immersion which is contracted to a rational point, the morphism is finite and an isomorphism
> off that point, and taking the coefficient of `ε` gives the skyscraper quotient of the
> pushforward structure sheaf.

```lean
def IsSquishingTangentVector {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (θ : Spec (.of (DualNumber k)) ⟶ X') : Prop
```

**`Stacks.SquishSheafSequence.shortExact_of_isSquishingTangentVector`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingUnitsSequence.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingUnitsSequence.lean#L185). The attribute's comment: “the short exact sequence of sheaves”.

> **The short exact sequence of sheaves attached to the squishing of a tangent vector.**
>
> If `f : X' ⟶ X` squishes the tangent vector `ϑ` of `X'` to the rational point `x` of `X`, then
> there is a map of additive sheaves `ψ : f_*𝒪_{X'} ⟶ (k, +)_x` to the additive skyscraper at `x`
> for which
>
> `0 → 𝒪_X → f_*𝒪_{X'} → (k, +)_x → 0`
>
> is short exact, and `ψ` is given on every neighbourhood `U` of `x` by the coefficient of `ε` of
> the restriction along `ϑ` of a section of `𝒪_{X'}` over `f⁻¹U`. This is the clause of
> [Stacks, Tag 0C1K] that the exactness statements of Tags 0C1M and 0C1N consume.

```lean
theorem shortExact_of_isSquishingTangentVector {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (θ : Spec (.of (DualNumber k)) ⟶ X')
    (h : AlgebraicGeometry.IsSquishingTangentVector f θ) :
    ∃ (ψ : pushforwardAddSheaf f ⟶ skyscraperAddSheaf (k := k) X
        ((θ ≫ f).base (IsLocalRing.closedPoint (DualNumber k))))
      (hzero : structureToPushforwardAddSheaf f ≫ ψ = 0),
      (ShortComplex.mk (structureToPushforwardAddSheaf f) ψ hzero).ShortExact ∧
        ∀ (U : X.Opens)
          (hx : (θ ≫ f).base (IsLocalRing.closedPoint (DualNumber k)) ∈ U)
          (s : Γ(X', f ⁻¹ᵁ U)),
          ψ.hom.app (op U) s =
            skyscraperAddSheafMk X ((θ ≫ f).base (IsLocalRing.closedPoint (DualNumber k))) hx
              (epsilonCoefficientAt θ (f ⁻¹ᵁ U) (by exact hx) s)
```

## Tag 0C1L, a lemma

[Tag 0C1L](https://stacks.math.columbia.edu/tag/0C1L) in the Stacks Project.

**`Stacks.GlueSquishFactor.algEquiv_prod_or_dualNumber_of_minimal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/ElementaryFactorization.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/ElementaryFactorization.lean#L351). The attribute's comment: “the local algebra of a minimal step”.

> **The local algebra of a minimal step of [Stacks, Tag 0C1L].** Let `k` be an algebraically
> closed field, let `A` be a local `k`-algebra whose residue field is `k` (hypothesis `hres`: every
> element of `A` is a scalar modulo the maximal ideal), and let `B` be a module-finite `A`-algebra
> which is not generated by `A` (hypothesis `hne`) and admits no `A`-subalgebra strictly between
> `A` and `B` (hypothesis `hmin`). Then the fibre `B ⧸ m_A B` is, as a `k`-algebra, either the
> product `k × k` or the dual numbers `k[ε]`.
>
> In the source this is the whole of the case `n = 1`: with `A = 𝒪_{X, x}` and
> `B = (f_*𝒪_{X'})_x`, the absence of a proper intermediate subalgebra forces `B = A + m_A B`
> (Nakayama) and then forces the fibre `C = B / m_A B` to have exactly two `k`-subalgebras, so
> [Stacks, Tag 0C1I] applies. The two outcomes are what make the step a glueing of two points
> respectively a squishing of a tangent vector.
>
> This is the mathematical heart of [Stacks, Tag 0C1L], but not the whole lemma: see the
> implementation notes of this file for the geometric statements that remain.

```lean
theorem algEquiv_prod_or_dualNumber_of_minimal (k : Type u) (A B : Type v) [Field k]
    [IsAlgClosed k] [CommRing A] [Algebra k A] [IsLocalRing A] [CommRing B] [Algebra k B]
    [Algebra A B] [IsScalarTower k A B] [Module.Finite A B]
    (hres : ∀ a : A, ∃ c : k, a - algebraMap k A c ∈ IsLocalRing.maximalIdeal A)
    (hne : (⊥ : Subalgebra A B) ≠ ⊤) (hmin : ∀ E : Subalgebra A B, E = ⊥ ∨ E = ⊤) :
    Nonempty ((B ⧸ (IsLocalRing.maximalIdeal A).map (algebraMap A B)) ≃ₐ[k] k × k) ∨
      Nonempty ((B ⧸ (IsLocalRing.maximalIdeal A).map (algebraMap A B)) ≃ₐ[k] DualNumber k)
```

**`Stacks.GlueSquishFactor.IsElementaryStep`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/ElementaryFactorization.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/ElementaryFactorization.lean#L550). The attribute's comment: “the elementary modifications”.

> **One step of the factorization of [Stacks, Tag 0C1L]**: a morphism of algebraic
> `k`-schemes which either glues two rational points ([Stacks, Tag 0C1J]) or squishes a tangent
> vector ([Stacks, Tag 0C1K]).

```lean
def IsElementaryStep {k : Type u} [Field k] [IsAlgClosed k] {Y' Y : Over (Spec (.of k))}
    (f : Y' ⟶ Y) : Prop
```

**`Stacks.GlueSquishFactor.IsElementaryChain`**, an inductive in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/ElementaryFactorization.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/ElementaryFactorization.lean#L570). The attribute's comment: “the factorization, as an inductive predicate”.

> **The conclusion of [Stacks, Tag 0C1L], as a predicate on one morphism.** `f` is a composite
> of finitely many elementary modifications and isomorphisms, which is the content of the source's
> chain `X' = X_n ⟶ ⋯ ⟶ X_0 = X` together with its endpoint identifications. The recursor is the
> induction on the length that the source's proof performs.

```lean
inductive IsElementaryChain (k : Type u) [Field k] [IsAlgClosed k] :
    {Y' Y : Over (Spec (.of k))} → (Y' ⟶ Y) → Prop
```

**`Stacks.GlueSquishFactor.toIntermediateOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/IntermediateFactorization.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/IntermediateFactorization.lean#L136). The attribute's comment: “the intermediate factorization attached to a subalgebra”.

> **The morphism `X' ⟶ Spec_X(A)` over `X` attached to a morphism `ψ : A ⟶ f_* 𝒪_{X'}` of
> `𝒪_X`-algebras.** It is the morphism corresponding to `ψ` under the universal property of the
> relative spectrum, read through the identification `(Spec_X(A) ⟶ X)_* 𝒪 ≅ A`.

```lean
def toIntermediateOver : Over.mk f ⟶ Over.mk (relativeSpecToBase A)
```

**`Stacks.GlueSquishFactor.toIntermediate_comp_relativeSpecToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/IntermediateFactorization.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/IntermediateFactorization.lean#L155). The attribute's comment: “the intermediate factorization attached to a subalgebra”.

> **The factorization of `f` attached to a morphism `ψ : A ⟶ f_* 𝒪_{X'}`.** The morphism
> `X' ⟶ Spec_X(A)` of `Stacks.GlueSquishFactor.toIntermediate`, followed by the structure morphism
> of the relative spectrum, is `f`.

```lean
theorem toIntermediate_comp_relativeSpecToBase :
    toIntermediate f A ψ ≫ relativeSpecToBase A = f
```

**`Stacks.GlueSquishFactor.isoRelativeSpecOfAffine`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/IntermediateFactorization.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/IntermediateFactorization.lean#L226). The attribute's comment: “every affine intermediate factorization comes from a subalgebra”.

> **A scheme affine over `X` is the relative spectrum of its algebra of functions over `X`.**
> For `g : Y ⟶ X` affine, the comparison morphism `Y ⟶ Spec_X(g_* 𝒪_Y)` is an isomorphism of
> schemes over `X`. This is [Stacks, Tag 01SA] in the form used by [Stacks, Tag 0C1L]: an
> intermediate factorization with affine second half is a relative spectrum.

```lean
def isoRelativeSpecOfAffine :
    Over.mk g ≅ Over.mk (relativeSpecToBase (pushforwardAlgebra g))
```

**`Stacks.GlueSquishFactor.toIntermediateOver_factorizationAlgebraHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/IntermediateFactorization.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/IntermediateFactorization.lean#L245). The attribute's comment: “every affine intermediate factorization comes from a subalgebra”.

> **Every intermediate factorization with affine second half comes from an algebra.** For a
> factorization `f = u ≫ g` with `g` affine, the comparison isomorphism
> `Y ≅ Spec_X(g_* 𝒪_Y)` carries `u` to the morphism attached by
> `Stacks.GlueSquishFactor.toIntermediateOver` to the algebra map `g_* 𝒪_Y ⟶ f_* 𝒪_{X'}` of the
> factorization.

```lean
theorem toIntermediateOver_factorizationAlgebraHom :
    toIntermediateOver f (pushforwardAlgebra g) (factorizationAlgebraHom f u g hu) =
      (Over.homMk u hu : Over.mk f ⟶ Over.mk g) ≫ toRelativeSpecOfAffine g
```

**`Stacks.GlueSquishFactor.exists_split_of_algebraHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SplittingStep.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SplittingStep.lean#L315). The attribute's comment: “the splitting attached to a finite intermediate subalgebra”.

> **The splitting step of [Stacks, Tag 0C1L].** Let `f : X' ⟶ X` be a finite morphism of
> schemes over a base `S` with `𝒪_X ⊂ f_*𝒪_{X'}` which is an isomorphism over an open `U` of `X`,
> and let `𝒜` be a finite quasi-coherent sheaf of `𝒪_X`-algebras with an injection
> `ψ : 𝒜 ⟶ f_*𝒪_{X'}` of `𝒪_X`-algebras. Then `f` factors over `S` as `p ≫ q` with
>
> * `q : Spec_X(𝒜) ⟶ X` finite, with `𝒪_X ⊂ q_*𝒪`, and an isomorphism over `U`;
> * `p : X' ⟶ Spec_X(𝒜)` finite, with `𝒪_{Spec_X(𝒜)} ⊂ p_*𝒪_{X'}`, and an isomorphism over
>   `q⁻¹U`.
>
> Finiteness of `q` is the finiteness of `𝒜`; finiteness of `p` is finiteness of `f` cancelled
> against it; `𝒪_X ⊂ q_*𝒪` is the chain `𝒪_X ⊂ 𝒜 ⊂ f_*𝒪_{X'}`;
> `𝒪_{Spec_X(𝒜)} ⊂ p_*𝒪_{X'}` is `ψ` propagated from the preimages of the affine opens of `X`
> to every open of `Spec_X(𝒜)` by
> `Stacks.GlueSquishFactor.mono_hom_pushforwardAlgebra_toIntermediate`; and the two statements
> over `U` are the squeeze
> `Stacks.GlueSquishFactor.isIso_morphismRestrict_relativeSpecToBase` together with cancellation
> of `q ∣_ U` out of `f ∣_ U`.
>
> The last clause is the *capture* clause: over every open `V` of `X` the sections of `𝒜` are
> sections of the intermediate scheme, by
> `Stacks.GlueSquishFactor.mem_range_appLE_toIntermediate`. It is what makes the splitting
> nontrivial — without it a splitting is produced even by `𝒜 = 𝒪_X`, for which `q` is an
> isomorphism and nothing has happened.

```lean
theorem exists_split_of_algebraHom {S : Scheme.{u}} {W' W : Over S} (f : W' ⟶ W)
    [IsFinite f.left] [Mono (pushforwardAlgebra f.left).hom] (A : AlgebraSheaf W.left)
    [AlgebraSheaf.IsQuasicoherent A] (hAfin : AlgebraSheaf.IsFinite A)
    (ψ : A ⟶ pushforwardAlgebra f.left)
    (hψ : ∀ V : W.left.Opens, Function.Injective (ψ.right.hom.app (op V)).hom)
    {U : W.left.Opens} (hU : IsIso (f.left ∣_ U)) :
    ∃ (Z : Over S) (p : W' ⟶ Z) (q : Z ⟶ W), p ≫ q = f ∧ IsFinite q.left ∧
      Mono (pushforwardAlgebra q.left).hom ∧ IsIso (q.left ∣_ U) ∧ IsFinite p.left ∧
      Mono (pushforwardAlgebra p.left).hom ∧ IsIso (p.left ∣_ (q.left ⁻¹ᵁ U)) ∧
      ∀ (V : W.left.Opens) (hle : f.left ⁻¹ᵁ V ≤ p.left ⁻¹ᵁ (q.left ⁻¹ᵁ V))
        (s : Γ(W'.left, f.left ⁻¹ᵁ V)), s ∈ Set.range (ψ.right.hom.app (op V)).hom →
          s ∈ Set.range (p.left.appLE (q.left ⁻¹ᵁ V) (f.left ⁻¹ᵁ V) hle).hom
```

**`Stacks.GlueSquishFactor.exists_split_isAlmostIso_of_algebraHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SplittingStep.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SplittingStep.lean#L364). The attribute's comment: “the splitting, read against the hypotheses of the lemma”.

> **The splitting step of [Stacks, Tag 0C1L], read against the hypotheses of the lemma.** An
> almost isomorphism of algebraic `k`-schemes and a finite quasi-coherent `𝒪_X`-subalgebra `𝒜` of
> `f_*𝒪_{X'}` give a factorization `f = p ≫ q` over `Spec k` in which *both* halves are again
> almost isomorphisms, so both satisfy every hypothesis of the source.
>
> Together with a measure which drops along this factorization, this is the hypothesis `hsplit`
> of `Stacks.GlueSquishFactor.isElementaryChain_of_isAlmostIso`. No measure is constructed
> here. The last clause records that the splitting *captures* the sections of `𝒜`, which is what
> distinguishes it from the trivial splitting by `𝒜 = 𝒪_X`.

```lean
theorem exists_split_isAlmostIso_of_algebraHom {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Over (Spec (.of k))} (f : X' ⟶ X) (hf : IsAlmostIso f) (A : AlgebraSheaf X.left)
    [AlgebraSheaf.IsQuasicoherent A] (hAfin : AlgebraSheaf.IsFinite A)
    (ψ : A ⟶ pushforwardAlgebra f.left)
    (hψ : ∀ V : X.left.Opens, Function.Injective (ψ.right.hom.app (op V)).hom) :
    ∃ (Z : Over (Spec (.of k))) (p : X' ⟶ Z) (q : Z ⟶ X),
      p ≫ q = f ∧ IsAlmostIso q ∧ IsAlmostIso p ∧
      ∀ (V : X.left.Opens) (hle : f.left ⁻¹ᵁ V ≤ p.left ⁻¹ᵁ (q.left ⁻¹ᵁ V))
        (s : Γ(X'.left, f.left ⁻¹ᵁ V)), s ∈ Set.range (ψ.right.hom.app (op V)).hom →
          s ∈ Set.range (p.left.appLE (q.left ⁻¹ᵁ V) (f.left ⁻¹ᵁ V) hle).hom
```

**`Stacks.GlueSquishFactor.IsAlmostIso.isElementaryChain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingProducer.lean, line 615](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingProducer.lean#L615).

> **[Stacks, Tag 0C1L].** A finite morphism of algebraic `k`-schemes which is injective on
> structure sheaves and an isomorphism away from a finite set of points is a composite of glueings
> of two rational points and squishings of tangent vectors.

```lean
theorem IsAlmostIso.isElementaryChain {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Over (Spec (.of k))} (f : X' ⟶ X) (hf : IsAlmostIso f) : IsElementaryChain k f
```

## Tag 0C1M, a lemma

[Tag 0C1M](https://stacks.math.columbia.edu/tag/0C1M) in the Stacks Project.

**`Stacks.GluePicard.surjective_schemePullbackClassHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicard.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicard.lean#L99). The attribute's comment: “surjectivity”.

> **Pullback of invertible modules along the glueing of two rational points is surjective on
> Picard groups.** The glueing is finite and is an isomorphism away from a single point, so
> [Stacks, Tag 0C0T] descends a representative of any class on `X'` to `X`.

```lean
theorem surjective_schemePullbackClassHom {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (a b : Spec (.of k) ⟶ X')
    (h : AlgebraicGeometry.IsGlueingTwoPoints f a b) :
    Function.Surjective (Stacks.Picard.schemePullbackClassHom f)
```

**`Stacks.GluePicard.exists_globalUnit_sectionAt_eq_of_ne_connectedComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicard.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicard.lean#L224). The attribute's comment: “the lifting criterion for vanishing at points on different components”.

> **The first map of the sequence of Stacks Tag 0C1M is zero when the two glued points lie
> on different connected components of `X'`**, in the form that the connecting homomorphism
> consumes: every scalar `c` is the ratio of the values at `a` and at `b` of a unit on all of
> `X'`, so the invertible module obtained by glueing the fibres at `a` and `b` with ratio `c` is
> trivial.

```lean
theorem exists_globalUnit_sectionAt_eq_of_ne_connectedComponents
    {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (a b : Spec (.of k) ⟶ X')
    (h : AlgebraicGeometry.IsGlueingTwoPoints f a b)
    (hab : ConnectedComponents.mk (a.base (IsLocalRing.closedPoint k)) ≠
      ConnectedComponents.mk (b.base (IsLocalRing.closedPoint k))) (c : kˣ) :
    ∃ s : Γ(X', ⊤)ˣ,
      AlgebraicGeometry.sectionAt a ⊤ (Opens.mem_top _) (s : Γ(X', ⊤)) = (c : k) ∧
        AlgebraicGeometry.sectionAt b ⊤ (Opens.mem_top _) (s : Γ(X', ⊤)) = 1
```

**`Stacks.GluePicard.schemePullbackClassHom_eq_zero_iff_exists_picardGluingHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicardExactness.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicardExactness.lean#L154). The attribute's comment: “exactness at Pic(X): the kernel of pullback is the image of k^*”.

> **Exactness at `Pic(X)` of the sequence of [Stacks, Tag 0C1M].** For `k` algebraically
> closed and `f : X' ⟶ X` the glueing of the two rational points `a` and `b` of `X'`, a Picard
> class of `X` pulls back to zero on `X'` exactly when it is the value of the gluing homomorphism
> `Stacks.GluePicard.picardGluingHom` at a scalar; that is, the kernel of `Pic(X) ⟶ Pic(X')` is
> the image of `k^* ⟶ Pic(X)`.

```lean
theorem schemePullbackClassHom_eq_zero_iff_exists_picardGluingHom {k : Type u} [Field k]
    [IsAlgClosed k] {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (a b : Spec (.of k) ⟶ X')
    (h : AlgebraicGeometry.IsGlueingTwoPoints f a b) (L : Stacks.Picard.ofScheme X) :
    Stacks.Picard.schemePullbackClassHom f L = 0 ↔
      ∃ c : Additive kˣ, picardGluingHom f a b h c = L
```

**`Stacks.GluePicard.exact_picardGluingHom_schemePullbackClassHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicardExactness.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicardExactness.lean#L179). The attribute's comment: “exactness at Pic(X): the kernel of pullback is the image of k^*”.

> **Exactness at `Pic(X)` of the sequence of [Stacks, Tag 0C1M]**, in the `Function.Exact`
> spelling: the kernel of pullback of Picard classes is the range of the gluing homomorphism.

```lean
theorem exact_picardGluingHom_schemePullbackClassHom {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (a b : Spec (.of k) ⟶ X')
    (h : AlgebraicGeometry.IsGlueingTwoPoints f a b) :
    Function.Exact (picardGluingHom f a b h) (Stacks.Picard.schemePullbackClassHom f)
```

**`Stacks.GluePicard.picardGluingHom_eq_zero_of_ne_connectedComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicardExactness.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicardExactness.lean#L253). The attribute's comment: “the first map is zero if a and b are on different connected components of X'”.

> **The first map of the sequence of [Stacks, Tag 0C1M] is zero when the two glued points lie
> on different connected components of `X'`.**

```lean
theorem picardGluingHom_eq_zero_of_ne_connectedComponents {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (a b : Spec (.of k) ⟶ X')
    (h : AlgebraicGeometry.IsGlueingTwoPoints f a b)
    (hab : ConnectedComponents.mk (a.base (IsLocalRing.closedPoint k)) ≠
      ConnectedComponents.mk (b.base (IsLocalRing.closedPoint k))) :
    picardGluingHom f a b h = 0
```

**`Stacks.GluePicard.picardGluingHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicardSequence.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicardSequence.lean#L343). The attribute's comment: “the gluing homomorphism”.

> **Stacks Project, Tag 0C1M.** The gluing homomorphism `k^* ⟶ Pic(X)`.

```lean
def picardGluingHom {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (a b : Spec (.of k) ⟶ X')
    (h : AlgebraicGeometry.IsGlueingTwoPoints f a b) :
    Additive kˣ →+ Stacks.Picard.ofScheme X
```

**`Stacks.GluePicard.injective_picardGluingHom_of_connectedComponents_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicardSequence.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/GlueingPicardSequence.lean#L559). The attribute's comment: “injectivity if X' is proper and the two points lie on the same connected component”.

> **Stacks Project, Tag 0C1M.** The gluing homomorphism is injective when `X'` is proper and
> the two glued points lie on the same connected component of `X'`: a scalar in its kernel is the
> ratio of the two values of a unit on `X'`, and on a connected component of a proper scheme over
> an algebraically closed field the two values of any function agree.

```lean
theorem injective_picardGluingHom_of_connectedComponents_eq
    {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (a b : Spec (.of k) ⟶ X')
    (h : AlgebraicGeometry.IsGlueingTwoPoints f a b) [IsProper (X' ↘ Spec (.of k))]
    (hab : ConnectedComponents.mk (a.base (IsLocalRing.closedPoint k)) =
      ConnectedComponents.mk (b.base (IsLocalRing.closedPoint k))) :
    Function.Injective (picardGluingHom f a b h)
```

## Tag 0C1N, a lemma

[Tag 0C1N](https://stacks.math.columbia.edu/tag/0C1N) in the Stacks Project.

**`Stacks.SquishPicard.picardPullback_zero_and_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicard.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicard.lean#L97). The attribute's comment: “the Picard pullback homomorphism”.

> Pullback of Picard classes is a homomorphism of abelian groups.

```lean
theorem picardPullback_zero_and_add {X' X : Scheme.{u}} (f : X' ⟶ X) :
    Stacks.Picard.schemePullbackClassHom f 0 = 0 ∧
      ∀ x y : Stacks.Picard.ofScheme X,
        Stacks.Picard.schemePullbackClassHom f (x + y) =
          Stacks.Picard.schemePullbackClassHom f x +
            Stacks.Picard.schemePullbackClassHom f y
```

**`Stacks.SquishPicard.surjective_schemePullbackClassHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicard.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicard.lean#L107). The attribute's comment: “surjectivity”.

> Pullback along the squishing of a tangent vector is surjective on Picard groups.

```lean
theorem surjective_schemePullbackClassHom {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (θ : Spec (.of (DualNumber k)) ⟶ X')
    (h : AlgebraicGeometry.IsSquishingTangentVector f θ) :
    Function.Surjective (Stacks.Picard.schemePullbackClassHom f)
```

**`Stacks.SquishPicard.epsilonCoefficientAt_eq_zero_of_isProper_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicard.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicard.lean#L240). The attribute's comment: “the lifting criterion for injectivity on a proper reduced scheme”.

> **The first map of the sequence of Stacks Tag 0C1N is injective when `X'` is proper and
> reduced**, in the form that the connecting homomorphism consumes: the `ε`-coefficient along the
> squished tangent vector of every global section of `𝒪_{X'}` vanishes.
>
> The global functions of a scheme proper over `k` are integral over `k`, and those of a reduced
> scheme are a reduced ring, so the minimal polynomial over `k` of a global section is squarefree.
> Its image in `k[ε]` therefore cannot be a double root of a linear polynomial, which is what a
> nonzero `ε`-coefficient would make it.

```lean
theorem epsilonCoefficientAt_eq_zero_of_isProper_of_isReduced
    {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (θ : Spec (.of (DualNumber k)) ⟶ X')
    (h : AlgebraicGeometry.IsSquishingTangentVector f θ)
    [IsProper (X' ↘ Spec (.of k))] [IsReduced X'] (s : Γ(X', ⊤)) :
    AlgebraicGeometry.epsilonCoefficientAt θ ⊤ trivial s = 0
```

**`Stacks.SquishPicard.epsilonCoefficientAt_unit_eq_zero_of_isProper_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicard.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicard.lean#L258). The attribute's comment: “the lifting criterion for injectivity on a proper reduced scheme”.

> The criterion of `Stacks.SquishPicard.epsilonCoefficientAt_eq_zero_of_isProper_of_isReduced`
> for a global unit: the logarithmic `ε`-derivative of a unit on a proper reduced `X'` vanishes, so
> no nonzero scalar is hit by the units sequence and the first map of Tag 0C1N is injective.

```lean
theorem epsilonCoefficientAt_unit_eq_zero_of_isProper_of_isReduced
    {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (θ : Spec (.of (DualNumber k)) ⟶ X')
    (h : AlgebraicGeometry.IsSquishingTangentVector f θ)
    [IsProper (X' ↘ Spec (.of k))] [IsReduced X'] (s : Γ(X', ⊤)ˣ) :
    AlgebraicGeometry.epsilonCoefficientAt θ ⊤ trivial (s : Γ(X', ⊤)) = 0
```

**`Stacks.SquishSheafSequence.schemePullbackClassHom_eq_zero_iff_exists_picardTangentHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicardExactness.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicardExactness.lean#L222). The attribute's comment: “exactness”.

> **Exactness at `Pic(X)` of the sequence of [Stacks, Tag 0C1N].**  For `k` algebraically
> closed and `f : X' ⟶ X` the squishing of the tangent vector `θ` of `X'`, a Picard class of `X`
> pulls back to zero on `X'` exactly when it is the value of the tangent homomorphism
> `Stacks.SquishSheafSequence.picardTangentHom` at a scalar; that is, the kernel of
> `Pic(X) ⟶ Pic(X')` is the image of `(k, +) ⟶ Pic(X)`.

```lean
theorem schemePullbackClassHom_eq_zero_iff_exists_picardTangentHom (f : X' ⟶ X)
    (θ : Spec (.of (DualNumber k)) ⟶ X')
    (h : AlgebraicGeometry.IsSquishingTangentVector f θ) (L : Stacks.Picard.ofScheme X) :
    Stacks.Picard.schemePullbackClassHom f L = 0 ↔
      ∃ a : k, picardTangentHom f θ h a = L
```

**`Stacks.SquishSheafSequence.exact_picardTangentHom_schemePullbackClassHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicardExactness.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicardExactness.lean#L246). The attribute's comment: “exactness”.

> **Exactness at `Pic(X)` of the sequence of [Stacks, Tag 0C1N]**, in the `Function.Exact`
> spelling: the kernel of pullback of Picard classes is the range of the tangent homomorphism.

```lean
theorem exact_picardTangentHom_schemePullbackClassHom (f : X' ⟶ X)
    (θ : Spec (.of (DualNumber k)) ⟶ X')
    (h : AlgebraicGeometry.IsSquishingTangentVector f θ) :
    Function.Exact (picardTangentHom f θ h) (Stacks.Picard.schemePullbackClassHom f)
```

**`Stacks.SquishSheafSequence.picardTangentHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicardSequence.lean, line 901](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicardSequence.lean#L901). The attribute's comment: “the tangent homomorphism”.

> **The tangent homomorphism `(k, +) ⟶ Pic(X)` of [Stacks, Tag 0C1N].** It is the connecting
> homomorphism of the short exact sequence of sheaves of units of a squishing, read through the
> five-term low-degree cohomology sequence over the whole space and through the identification of
> `H¹(X, 𝒪_X^*)` with the Picard group of [Stacks, Tag 09NU].

```lean
def picardTangentHom {k : Type u} [Field k] [IsAlgClosed k] {X' X : Scheme.{u}}
    [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))] (f : X' ⟶ X)
    (θ : Spec (.of (DualNumber k)) ⟶ X')
    (h : AlgebraicGeometry.IsSquishingTangentVector f θ) : k →+ Stacks.Picard.ofScheme X
```

**`Stacks.SquishSheafSequence.injective_picardTangentHom_of_isProper_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicardSequence.lean, line 975](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingPicardSequence.lean#L975). The attribute's comment: “injectivity on a proper reduced scheme”.

> **The tangent homomorphism is injective when `X'` is proper and reduced.** A scalar in its
> kernel is the logarithmic `ε`-derivative of a unit on `X'`, and on a proper reduced `X'` the
> logarithmic `ε`-derivative of a global unit vanishes by
> `Stacks.SquishSheafSequence.epsilonLogDeriv_eq_zero_of_isProper_of_isReduced`.

```lean
theorem injective_picardTangentHom_of_isProper_of_isReduced {k : Type u} [Field k]
    [IsAlgClosed k] {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (θ : Spec (.of (DualNumber k)) ⟶ X')
    (h : AlgebraicGeometry.IsSquishingTangentVector f θ)
    [IsProper (X' ↘ Spec (.of k))] [IsReduced X'] :
    Function.Injective (picardTangentHom f θ h)
```

**`Stacks.SquishSheafSequence.epsilonLogDerivSheafHom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingUnitsSequence.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingUnitsSequence.lean#L435). The attribute's comment: “the quotient map of the sequence of sheaves of units”.

> **The quotient map of the units sequence is the logarithmic `ε`-derivative** on the units of
> the sections over every neighbourhood of the contracted point.

```lean
theorem epsilonLogDerivSheafHom_app {k : Type u} [Field k] {X' X : Scheme.{u}} (f : X' ⟶ X)
    (θ : Spec (.of (DualNumber k)) ⟶ X') (U : X.Opens)
    (hx : (θ ≫ f).base (IsLocalRing.closedPoint (DualNumber k)) ∈ U)
    (s : Γ(X', f ⁻¹ᵁ U)ˣ) :
    (epsilonLogDerivSheafHom f θ).hom.app (op U) (Additive.ofMul s) =
      skyscraperAddSheafMk X ((θ ≫ f).base (IsLocalRing.closedPoint (DualNumber k))) hx
        (epsilonLogDeriv θ (f ⁻¹ᵁ U) hx s)
```

**`Stacks.SquishSheafSequence.epsilonLogDeriv_eq_zero_of_isProper_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingUnitsSequence.lean, line 451](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GlueingSquishing/SquishingUnitsSequence.lean#L451). The attribute's comment: “vanishing of the logarithmic derivative on a proper reduced scheme”.

> **On a proper reduced `X'` the logarithmic `ε`-derivative of a global unit vanishes**, so the
> arrow to `(k, +)` of the units sequence of [Stacks, Tag 0C1N] kills the global units and the
> connecting homomorphism `(k, +) → Pic(X)` is injective. The `ε`-coefficient of every global
> section already vanishes, by
> `Stacks.SquishPicard.epsilonCoefficientAt_eq_zero_of_isProper_of_isReduced`.

```lean
theorem epsilonLogDeriv_eq_zero_of_isProper_of_isReduced
    {k : Type u} [Field k] [IsAlgClosed k]
    {X' X : Scheme.{u}} [X'.Over (Spec (.of k))] [X.Over (Spec (.of k))]
    (f : X' ⟶ X) (θ : Spec (.of (DualNumber k)) ⟶ X')
    (h : AlgebraicGeometry.IsSquishingTangentVector f θ)
    [IsProper (X' ↘ Spec (.of k))] [IsReduced X'] (u : Γ(X', ⊤)ˣ) :
    epsilonLogDeriv θ ⊤ (Opens.mem_top _) u = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.15, Tag 0C1H](https://stacks.math.columbia.edu/tag/0C1H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
