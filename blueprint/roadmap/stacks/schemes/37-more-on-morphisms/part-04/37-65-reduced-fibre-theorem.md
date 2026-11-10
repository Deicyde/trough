---
declaration: section
origin: cited
lean: AlgebraicGeometry.normalizedBaseChange, AlgebraicGeometry.normalizedBaseChangeOverIntegralClosure, AlgebraicGeometry.exists_finiteExtension_smoothAt_genericPoints_fiber_normalization_pullback, AlgebraicGeometry.exists_finiteExtension_smoothAt_genericPoints_fiber_normalization_of_isRegular, AlgebraicGeometry.exists_finiteSeparableExtension_smoothAt_genericPoints_fiber_normalization_pullback, AlgebraicGeometry.exists_finiteSeparableExtension_smoothAt_genericPoints_fiber_normalization_of_isRegular
statement: formalized
proof: formalized
---

# 37.65 Reduced fibre theorem

Section 37.65 of the Stacks Project, [Tag 09IJ](https://stacks.math.columbia.edu/tag/09IJ). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09IK, an equation

[Tag 09IK](https://stacks.math.columbia.edu/tag/09IK) in the Stacks Project.

**`AlgebraicGeometry.normalizedBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/NormalizedBaseChange.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/NormalizedBaseChange.lean#L49). The attribute's comment: “the normalization morphism to the base change”.

> The normalized pullback of a finite-type scheme over a Dedekind domain along the
> integral closure in a finite fraction-field extension, as a scheme over the pullback.

```lean
noncomputable def normalizedBaseChange
    (A K L B : Type u)
    [CommRing A] [IsDedekindDomain A]
    [Field K] [Algebra A K] [IsFractionRing A K]
    [Field L] [Algebra K L] [FiniteDimensional K L]
    [Algebra A L] [IsScalarTower A K L]
    [CommRing B] [Algebra A B] [Algebra B L]
    [IsScalarTower A B L] [IsIntegralClosure B A L]
    (X : Scheme.{u}) (p : X ⟶ Spec (.of A))
    [Flat p] [LocallyOfFiniteType p] [QuasiCompact p] :
    let g : Spec (.of B) ⟶ Spec (.of A) :=
      Spec.map (CommRingCat.ofHom (algebraMap A B))
    Over (pullback p g)
```

**`AlgebraicGeometry.normalizedBaseChangeOverIntegralClosure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/NormalizedBaseChange.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/NormalizedBaseChange.lean#L79). The attribute's comment: “the morphism to the integral closure”.

> The structure morphism to the integral closure in the normalized base-change diagram.

```lean
noncomputable def normalizedBaseChangeOverIntegralClosure
    (A K L B : Type u)
    [CommRing A] [IsDedekindDomain A]
    [Field K] [Algebra A K] [IsFractionRing A K]
    [Field L] [Algebra K L] [FiniteDimensional K L]
    [Algebra A L] [IsScalarTower A K L]
    [CommRing B] [Algebra A B] [Algebra B L]
    [IsScalarTower A B L] [IsIntegralClosure B A L]
    (X : Scheme.{u}) (p : X ⟶ Spec (.of A))
    [Flat p] [LocallyOfFiniteType p] [QuasiCompact p] :
    Over (Spec (.of B))
```

## Tag 09IL, a theorem

[Tag 09IL](https://stacks.math.columbia.edu/tag/09IL) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteExtension_smoothAt_genericPoints_fiber_normalization_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibreTheorem.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibreTheorem.lean#L379).

> **Stacks Project, Tag 09IL (the reduced fibre theorem).**  Let `A` be a Nagata Dedekind
> domain with fraction field `K` and let `f : X ⟶ Spec A` be flat, quasi-compact and locally of
> finite type.  Then there is a finite extension `L / K` such that, with `B` the integral closure
> of `A` in `L`, the normalization `Y` of `X ×_{Spec A} Spec B` is smooth over `Spec B` at every
> generic point of every one of the fibres of `Y ⟶ Spec B`.
>
> `X` is assumed neither reduced nor normal nor affine, and `A` is not assumed excellent; the
> smoothness is at *all* generic points of *all* fibres.
>
> The fraction field is allowed its own universe: the statement is the one in the scheme's universe
> transported along the `A`-algebra isomorphism `K ≃ₐ[A] FractionRing A`, which carries the
> `K`-algebra structure of the extension and its finite dimensionality while leaving the extension,
> the integral closure and the whole conclusion where they are.

```lean
theorem exists_finiteExtension_smoothAt_genericPoints_fiber_normalization_pullback
    {A : Type u} [CommRing A] [IsDedekindDomain A] (K : Type v) [Field K]
    [Algebra A K] [IsFractionRing A K] (hA : IsNagataRing A) {X : Scheme.{u}}
    (f : X ⟶ Spec (.of A)) [Flat f] [LocallyOfFiniteType f] [QuasiCompact f] :
    ∃ (L : Type u) (_ : Field L) (_ : Algebra K L) (_ : FiniteDimensional K L)
      (_ : Algebra A L) (_ : IsScalarTower A K L),
      ∃ hW : ∀ U : (pullback f (Spec.map (CommRingCat.ofHom
          (algebraMap A ↥(integralClosure A L)))) : Scheme.{u}).Opens,
        IsCompact (U : Set (pullback f (Spec.map (CommRingCat.ofHom
          (algebraMap A ↥(integralClosure A L)))) : Scheme.{u})) →
        (irreducibleComponents U).Finite,
      ∀ b : Spec (.of ↥(integralClosure A L)),
      ∀ y : (Scheme.normalization _ hW ≫ pullback.snd f (Spec.map (CommRingCat.ofHom
        (algebraMap A ↥(integralClosure A L))))).fiber b,
      y ∈ genericPoints ↥((Scheme.normalization _ hW ≫ pullback.snd f (Spec.map
        (CommRingCat.ofHom (algebraMap A ↥(integralClosure A L))))).fiber b) →
      InfinitesimalLifting.SmoothAt (Scheme.normalization _ hW ≫ pullback.snd f
          (Spec.map (CommRingCat.ofHom (algebraMap A ↥(integralClosure A L)))))
        ((Scheme.normalization _ hW ≫ pullback.snd f (Spec.map (CommRingCat.ofHom
          (algebraMap A ↥(integralClosure A L))))).fiberι b y)
```

## Tag 0BRQ, a lemma

[Tag 0BRQ](https://stacks.math.columbia.edu/tag/0BRQ) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteExtension_smoothAt_genericPoints_fiber_normalization_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibreCurve.lean, line 835](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibreCurve.lean#L835). The attribute's comment: “corrected statement: the source omits quasi-compactness and is false without it (`not_forall_exists_finiteExtension_smoothAt_genericPoints_fiber_normalization`); stated here with `X` quasi-compact, which is implied by `S` quasi-compact (see the `_of_compactSpace` corollary)”.

> **Stacks Project, Tag 0BRQ (variant of the reduced fibre theorem over curves), corrected:
> the source omits quasi-compactness, and the statement is false without it.**  Let `f : X ⟶ S` be
> flat and of finite type with `X` quasi-compact.  Assume `S` is Nagata, integral with function
> field `K`, and regular of dimension `1`.  Then there is a finite extension `L / K` such that, with
> `T` the normalization of `S` in `Spec L` (`(S.genericExtensionHom L).normalization`, Tag 035H) and
> `ν : Y ⟶ X ×_S T` the normalization, the morphism `g = ν ≫ pr₂ : Y ⟶ T` is smooth at every
> generic point of every fibre.
>
> The finiteness witness `hW` is the one the normalization of a scheme takes as an argument; it is a
> theorem here (`X ×_S T` is locally Noetherian), not a hypothesis.
>
> **Correction.**  The source states the lemma for arbitrary `S`, and its proof begins "choose a
> finite affine open covering of `S`".  Without quasi-compactness the statement is false: this is
> `AlgebraicGeometry.not_forall_exists_finiteExtension_smoothAt_genericPoints_fiber_normalization`,
> the negation of the statement exactly as the source writes it, in the vocabulary of this theorem.
> There `S` is the affine line over a field `k` with infinitely many origins (countably many copies
> of `Spec k[t]` glued along `Spec k[t, t⁻¹]`), integral, regular of dimension one and Nagata but not
> quasi-compact, and `X` is glued from countably many copies of the plane `Spec k[x, y]` along the
> torus `Spec k[x, t, (xt)⁻¹]`, the `n`-th copy lying over the `n`-th copy of the line by
> `t = x ^ (n + 1) y`; `f` is flat, affine and of finite type.  Over the `n`-th origin the fibre
> contains the line `x = 0` with multiplicity `n + 1`, and smoothness of `g` at the generic points
> of the fibres over the points of `T` above it forces `n + 1 ≤ [L : K]`; no `L` serves every `n`.
> Quasi-compactness of `S` repairs the statement, and it is enough that `X` be quasi-compact, since
> then only the finitely many affine opens of `S` covering the image of `X` matter; with `S`
> quasi-compact this is
> `AlgebraicGeometry.exists_finiteExtension_smoothAt_genericPoints_normalization_of_compactSpace`.
>
> The proof is the source's: cover the image of `X` by finitely many affine opens `Spec A_i` with
> `A_i` a Nagata Dedekind domain with fraction field `K`, apply Tag 09IL
> (`AlgebraicGeometry.exists_finiteExtension_smoothAt_genericPoints_fiber_normalization_pullback`)
> over each, and take `L` dominating the resulting extensions; this is
> `AlgebraicGeometry.exists_finiteExtension_smoothAt_normalization_of_forall_affine`
> with the trivial property.

```lean
theorem exists_finiteExtension_smoothAt_genericPoints_fiber_normalization_of_isRegular
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFiniteType f] [QuasiCompact f]
    [CompactSpace X] [IsIntegral S] (hN : IsNagataScheme S) (hR : IsRegular S)
    (hdim : topologicalKrullDim S = 1) :
    ∃ (L : Type u) (_ : Field L) (_ : Algebra S.functionField L)
      (_ : FiniteDimensional S.functionField L),
      ∃ hW : ∀ V : (pullback f (S.genericExtensionHom L).fromNormalization : Scheme.{u}).Opens,
        IsCompact (V : Set (pullback f (S.genericExtensionHom L).fromNormalization :
          Scheme.{u})) → (irreducibleComponents V).Finite,
      ∀ b : (S.genericExtensionHom L).normalization,
      ∀ y : (Scheme.normalization _ hW ≫
        pullback.snd f (S.genericExtensionHom L).fromNormalization).fiber b,
      y ∈ genericPoints ↥((Scheme.normalization _ hW ≫
        pullback.snd f (S.genericExtensionHom L).fromNormalization).fiber b) →
      InfinitesimalLifting.SmoothAt (Scheme.normalization _ hW ≫
          pullback.snd f (S.genericExtensionHom L).fromNormalization)
        ((Scheme.normalization _ hW ≫
          pullback.snd f (S.genericExtensionHom L).fromNormalization).fiberι b y)
```

## Tag 0BRR, a lemma

[Tag 0BRR](https://stacks.math.columbia.edu/tag/0BRR) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteSeparableExtension_smoothAt_genericPoints_fiber_normalization_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibreSeparableTheorem.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibreSeparableTheorem.lean#L411).

> **Stacks Project, Tag 0BRR (the reduced fibre theorem with a separable extension).**  Let `A`
> be a Dedekind domain with fraction field `K` and let `f : X ⟶ Spec A` be flat, quasi-compact and
> locally of finite type.  Assume `A` is a Nagata ring and that for every generic point `η` of an
> irreducible component of `X` the residue field `κ(η)` is a separable extension of `K`.  Then there
> is a finite separable extension `L / K` such that, with `B` the integral closure of `A` in `L`,
> the normalization `Y` of `X ×_{Spec A} Spec B` is smooth over `Spec B` at every generic point of
> every one of the fibres of `Y ⟶ Spec B`.
>
> The separability hypothesis is stated over the residue field of `Spec A` at `f η`, through the
> residue field map of `f`: since `f` is flat, `f η` is the generic point of `Spec A`, whose residue
> field is the fraction field `K`, so this is the separability of `κ(η) / K` of the source, for the
> notion of separability of Tag 030O which does not require `κ(η) / K` to be algebraic.
>
> The fraction field is allowed its own universe: the statement is the one in the scheme's universe
> transported along the `A`-algebra isomorphism `K ≃ₐ[A] FractionRing A`, as for Tag 09IL.

```lean
theorem exists_finiteSeparableExtension_smoothAt_genericPoints_fiber_normalization_pullback
    {A : Type u} [CommRing A] [IsDedekindDomain A] (K : Type v) [Field K]
    [Algebra A K] [IsFractionRing A K] (hA : IsNagataRing A) {X : Scheme.{u}}
    (f : X ⟶ Spec (.of A)) [Flat f] [LocallyOfFiniteType f] [QuasiCompact f]
    (hsep : ∀ x : X, x ∈ genericPoints X →
      letI : Algebra ((Spec (.of A)).residueField (f x)) (X.residueField x) :=
        (f.residueFieldMap x).hom.toAlgebra
      Algebra.IsSeparableExtension ((Spec (.of A)).residueField (f x)) (X.residueField x)) :
    ∃ (L : Type u) (_ : Field L) (_ : Algebra K L) (_ : FiniteDimensional K L)
      (_ : Algebra.IsSeparable K L) (_ : Algebra A L) (_ : IsScalarTower A K L),
      ∃ hW : ∀ U : (pullback f (Spec.map (CommRingCat.ofHom
          (algebraMap A ↥(integralClosure A L)))) : Scheme.{u}).Opens,
        IsCompact (U : Set (pullback f (Spec.map (CommRingCat.ofHom
          (algebraMap A ↥(integralClosure A L)))) : Scheme.{u})) →
        (irreducibleComponents U).Finite,
      ∀ b : Spec (.of ↥(integralClosure A L)),
      ∀ y : (Scheme.normalization _ hW ≫ pullback.snd f (Spec.map (CommRingCat.ofHom
        (algebraMap A ↥(integralClosure A L))))).fiber b,
      y ∈ genericPoints ↥((Scheme.normalization _ hW ≫ pullback.snd f (Spec.map
        (CommRingCat.ofHom (algebraMap A ↥(integralClosure A L))))).fiber b) →
      InfinitesimalLifting.SmoothAt (Scheme.normalization _ hW ≫ pullback.snd f
          (Spec.map (CommRingCat.ofHom (algebraMap A ↥(integralClosure A L)))))
        ((Scheme.normalization _ hW ≫ pullback.snd f (Spec.map (CommRingCat.ofHom
          (algebraMap A ↥(integralClosure A L))))).fiberι b y)
```

## Tag 0BRS, a lemma

[Tag 0BRS](https://stacks.math.columbia.edu/tag/0BRS) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteSeparableExtension_smoothAt_genericPoints_fiber_normalization_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibreCurveSeparable.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibreCurveSeparable.lean#L143). The attribute's comment: “corrected statement: the source omits quasi-compactness and is false without it (`not_forall_exists_finiteSeparableExtension_smoothAt_genericPoints_fiber_normalization`); stated here with `X` quasi-compact, which is implied by `S` quasi-compact (see the `_of_compactSpace` corollary)”.

> **Stacks Project, Tag 0BRS (variant with separable extensions over curves), corrected: the
> source omits quasi-compactness, and the statement is false without it.**  Let `f : X ⟶ S` be
> flat and of finite type with `X` quasi-compact.  Assume `S` is Nagata, integral with function
> field `K`, and regular of dimension `1`, and that the field extension `κ(η) / K` is separable for
> every generic point `η` of an irreducible component of `X`.  Then there is a finite separable
> extension `L / K` such that, with `T` the normalization of `S` in `Spec L`
> (`(S.genericExtensionHom L).normalization`) and `ν : Y ⟶ X ×_S T` the normalization, the
> morphism `g = ν ≫ pr₂ : Y ⟶ T` is smooth at every generic point of every fibre.
>
> The separability hypothesis is that of `κ(η)` over `κ(f η)`; flatness puts `f η` at the generic
> point of `S`, whose residue field is `K`.  The finiteness witness `hW` is the argument the
> normalization of a scheme takes; it is a theorem (`X ×_S T` is locally Noetherian), not a
> hypothesis.
>
> **Correction.**  The source's proof is that of Tag 0BRQ, which begins with a finite affine open
> covering of `S`; without quasi-compactness the statement is false: this is
> `not_forall_exists_finiteSeparableExtension_smoothAt_genericPoints_fiber_normalization`, the
> negation of the statement exactly as the source writes it, in the vocabulary of this theorem.
> The counterexample is that of Tag 0BRQ
> (`AlgebraicGeometry.not_forall_exists_finiteExtension_smoothAt_genericPoints_fiber_normalization`)
> over `ℚ`, where the separability hypothesis holds because every extension of a field of
> characteristic zero is separable, and the conclusion of Tag 0BRS contains that of Tag 0BRQ.
> Quasi-compactness of `X` repairs the statement (only the finitely many affine opens covering the
> image of `X` matter), and it is implied by that of `S`
> (`AlgebraicGeometry.exists\_finiteSeparableExtension\_smoothAt\_genericPoints\_normalization\_of\_\
> compactSpace`).

```lean
theorem exists_finiteSeparableExtension_smoothAt_genericPoints_fiber_normalization_of_isRegular
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFiniteType f] [QuasiCompact f]
    [CompactSpace X] [IsIntegral S] (hN : IsNagataScheme S) (hR : IsRegular S)
    (hdim : topologicalKrullDim S = 1)
    (hsep : ∀ x : X, x ∈ genericPoints X →
      letI : Algebra (S.residueField (f.base x)) (X.residueField x) :=
        (f.residueFieldMap x).hom.toAlgebra
      Algebra.IsSeparableExtension (S.residueField (f.base x)) (X.residueField x)) :
    ∃ (L : Type u) (_ : Field L) (_ : Algebra S.functionField L)
      (_ : FiniteDimensional S.functionField L) (_ : Algebra.IsSeparable S.functionField L),
      ∃ hW : ∀ V : (pullback f (S.genericExtensionHom L).fromNormalization : Scheme.{u}).Opens,
        IsCompact (V : Set (pullback f (S.genericExtensionHom L).fromNormalization :
          Scheme.{u})) → (irreducibleComponents V).Finite,
      ∀ b : (S.genericExtensionHom L).normalization,
      ∀ y : (Scheme.normalization _ hW ≫
        pullback.snd f (S.genericExtensionHom L).fromNormalization).fiber b,
      y ∈ genericPoints ↥((Scheme.normalization _ hW ≫
        pullback.snd f (S.genericExtensionHom L).fromNormalization).fiber b) →
      InfinitesimalLifting.SmoothAt (Scheme.normalization _ hW ≫
          pullback.snd f (S.genericExtensionHom L).fromNormalization)
        ((Scheme.normalization _ hW ≫
          pullback.snd f (S.genericExtensionHom L).fromNormalization).fiberι b y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.65, Tag 09IJ](https://stacks.math.columbia.edu/tag/09IJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
