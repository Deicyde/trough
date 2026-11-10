---
declaration: section
origin: cited
lean: AlgebraicGeometry.CoherentReflexive.isIso_dualTensorHullToSheafHom, AlgebraicGeometry.CoherentReflexive.rankOneSkeletonMul_toSkeleton, AlgebraicGeometry.CoherentReflexive.rankOneSkeletonCommMonoid, AlgebraicGeometry.CoherentReflexive.rankOneSkeletonCommGroup, AlgebraicGeometry.nonempty_iso_of_weilDivisorClassOfInvertibleSheaf_restrict_eq, AlgebraicGeometry.CoherentReflexive.rankOneSkeletonMulEquivWeilDivisorClass, AlgebraicGeometry.CoherentReflexive.isOpen_sectionIsomorphismLocus_and_nonempty_isColimit, Stacks.AlgebraicGeometry.ReflexivePowers.reflexivePower
statement: formalized
proof: formalized
---

# 31.30 Weil divisors on normal schemes

Section 31.30 of the Stacks Project, [Tag 0EBK](https://stacks.math.columbia.edu/tag/0EBK). 6 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EBL, a lemma

[Tag 0EBL](https://stacks.math.columbia.edu/tag/0EBL) in the Stacks Project.

**`AlgebraicGeometry.CoherentReflexive.isIso_dualTensorHullToSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/DualTensorInternalHom.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/DualTensorInternalHom.lean#L438). The attribute's comment: “the comparison (ℋom(ℱ, 𝒪_X) ⊗ 𝒢)^∨∨ → ℋom(ℱ, 𝒢) is an isomorphism”.

> Let `X` be an integral locally Noetherian normal scheme and let `ℱ` and `𝒢` be coherent
> reflexive `𝒪_X`-modules. Then the canonical map
>
> `(ℋom_{𝒪_X}(ℱ, 𝒪_X) ⊗_{𝒪_X} 𝒢)^∨∨ ⟶ ℋom_{𝒪_X}(ℱ, 𝒢)`
>
> is an isomorphism.

```lean
theorem isIso_dualTensorHullToSheafHom (E F : X.Modules) [E.IsCoherent] [F.IsCoherent]
    (hE : IsReflexive E) (hF : IsReflexive F) :
    IsIso (dualTensorHullToSheafHom E F hF)
```

**`AlgebraicGeometry.CoherentReflexive.rankOneSkeletonMul_toSkeleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RankOneTensorMonoid.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RankOneTensorMonoid.lean#L307). The attribute's comment: “the monoid law is the double dual of the tensor product”.

> **Stacks Project, Tag 0EBL.**  The product of two isomorphism classes of rank one coherent
> reflexive modules is the class of `(ℱ ⊗_{𝒪_X} 𝒢)^∨∨`.  This identifies the monoid law of
> `rankOneSkeletonCommMonoid` with the rule the tag states, so the two together assert that that
> rule is a commutative monoid law.

```lean
theorem rankOneSkeletonMul_toSkeleton (F G : RankOneReflexiveModules X) :
    rankOneSkeletonMul (toSkeleton F) (toSkeleton G) = toSkeleton (rankOneTensorObj F G)
```

**`AlgebraicGeometry.CoherentReflexive.rankOneSkeletonCommMonoid`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RankOneTensorMonoid.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RankOneTensorMonoid.lean#L357). The attribute's comment: “commutative monoid law on rank 1 coherent reflexive classes”.

> **Stacks Project, Tag 0EBL, the monoid part of the group law.**  On an integral locally
> Noetherian scheme the rule `ℱ, 𝒢 ↦ (ℱ ⊗_{𝒪_X} 𝒢)^∨∨` is a commutative monoid law on the set of
> isomorphism classes of rank one coherent reflexive `𝒪_X`-modules, with the class of the
> structure sheaf as its unit.  Inverses are not provided; see the implementation notes.

```lean
noncomputable def rankOneSkeletonCommMonoid (X : Scheme.{u}) [IsIntegral X]
    [IsLocallyNoetherian X] : CommMonoid (Skeleton (RankOneReflexiveModules X))
```

**`AlgebraicGeometry.CoherentReflexive.rankOneSkeletonCommGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RankOneWeilClassSurjective.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RankOneWeilClassSurjective.lean#L104). The attribute's comment: “the abelian group law on isomorphism classes of rank 1 coherent reflexive modules”.

> On an integral locally Noetherian normal scheme the rule `ℱ, 𝒢 ↦ (ℱ ⊗_{𝒪_X} 𝒢)^∨∨` is an
> **abelian group law** on the set of isomorphism classes of rank one coherent reflexive
> `𝒪_X`-modules.
>
> Multiplication and unit are those of
> `AlgebraicGeometry.CoherentReflexive.rankOneSkeletonCommMonoid`, and the inverse of `[ℱ]` is the
> class whose Weil divisor class is `-[ℱ]`.

```lean
noncomputable def rankOneSkeletonCommGroup (X : Scheme.{u}) [IsIntegral X]
    [IsLocallyNoetherian X] [IsNormal X] :
    CommGroup (Skeleton (RankOneReflexiveModules X))
```

## Tag 0EBM, a lemma

[Tag 0EBM](https://stacks.math.columbia.edu/tag/0EBM) in the Stacks Project.

**`AlgebraicGeometry.nonempty_iso_of_weilDivisorClassOfInvertibleSheaf_restrict_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/DivisorClassFaithful.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/DivisorClassFaithful.lean#L166). The attribute's comment: “the injectivity clause, with the two modules compared directly”.

> **Stacks Project, Tag 0EBM, the injectivity clause.**  Let `X` be an integral locally
> Noetherian normal scheme and `U ⊆ X` an open subscheme whose complement has codimension at least
> two at every point.  Two coherent reflexive `𝒪_X`-modules whose restrictions to `U` are invertible
> with the same Weil divisor class in `Cl(U)` are isomorphic.
>
> This is the injectivity clause of the source's proof of Tag 0EBM, stated without the map that
> clause is about: the first Chern class of `U` is injective by [Stacks, Tag 0BE8], so the two
> restrictions are isomorphic, and restriction to `U` is an equivalence on coherent reflexive modules
> by [Stacks, Tag 0EBJ], so the two modules are isomorphic on `X`.  The isomorphism that Tag 0EBM
> itself asserts — between `Cl(X)` and the group of isomorphism classes of rank one coherent
> reflexive `𝒪_X`-modules — is **not** proved here and no declaration claims it; see the
> implementation notes for what is missing.

```lean
theorem nonempty_iso_of_weilDivisorClassOfInvertibleSheaf_restrict_eq {X : Scheme.{u}}
    [IsIntegral X] [IsLocallyNoetherian X] [IsNormal X] (U : X.Opens)
    (hU : ∀ x : X, x ∉ U → (2 : ℕ∞) ≤ codimension (IrreducibleCloseds.closureSingleton x))
    (M N : X.Modules) (hM : _root_.SheafOfModules.IsCoherent M) (hMr : IsReflexive M)
    (hN : _root_.SheafOfModules.IsCoherent N) (hNr : IsReflexive N)
    [hMU : SheafOfModules.IsInvertible U.toScheme.sheaf.obj U.toScheme.ringCatSheaf.property
      (M.restrict U.ι)]
    [hNU : SheafOfModules.IsInvertible U.toScheme.sheaf.obj U.toScheme.ringCatSheaf.property
      (N.restrict U.ι)]
    (hc : haveI : IsIntegral U.toScheme := isIntegral_of_two_le_codimension_compl U hU
      haveI : IsLocallyNoetherian U.toScheme := isLocallyNoetherian_of_isOpenImmersion U.ι
      weilDivisorClassOfInvertibleSheaf U.toScheme (M.restrict U.ι) =
        weilDivisorClassOfInvertibleSheaf U.toScheme (N.restrict U.ι)) :
    Nonempty (M ≅ N)
```

**`AlgebraicGeometry.CoherentReflexive.rankOneSkeletonMulEquivWeilDivisorClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RankOneWeilClassSurjective.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RankOneWeilClassSurjective.lean#L75).

> On an integral locally Noetherian normal scheme the isomorphism classes of rank one coherent
> reflexive `𝒪_X`-modules, under the monoid law `ℱ, 𝒢 ↦ (ℱ ⊗_{𝒪_X} 𝒢)^∨∨` of [Stacks, Tag 0EBL],
> are isomorphic to the Weil divisor class group `Cl(X)`, written multiplicatively.
>
> The isomorphism is `AlgebraicGeometry.CoherentReflexive.rankOneSkeletonToWeilClass`, which sends
> a module to the class of its restriction to an open subscheme whose complement has codimension at
> least two and on which it is invertible.

```lean
def rankOneSkeletonMulEquivWeilDivisorClass :
    Skeleton (RankOneReflexiveModules X) ≃* Multiplicative (weilDivisorClassGroup X)
```

## Tag 0EBN, a lemma

[Tag 0EBN](https://stacks.math.columbia.edu/tag/0EBN) in the Stacks Project.

**`AlgebraicGeometry.CoherentReflexive.isOpen_sectionIsomorphismLocus_and_nonempty_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ReflexivePowerColimit.lean, line 690](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ReflexivePowerColimit.lean#L690).

> Let `X` be an integral locally Noetherian normal scheme, `ℱ` a rank one coherent reflexive
> `𝒪_X`-module and `s ∈ Γ(X, ℱ)`.  The set `U = {x ∈ X | s : 𝒪_{X, x} → ℱ_x is an isomorphism}`
> is open, so that `j : U → X` is an open subscheme, and
>
> `j_*𝒪_U = colim (𝒪_X →ˢ ℱ →ˢ ℱ^{[2]} →ˢ ℱ^{[3]} →ˢ ⋯)`,
>
> where `ℱ^{[1]} = ℱ` and `ℱ^{[n + 1]} = (ℱ ⊗_{𝒪_X} ℱ^{[n]})^{**}`: the cocone
> `AlgebraicGeometry.CoherentReflexive.sectionIsomorphismOpenCocone` on the directed system
> `AlgebraicGeometry.CoherentReflexive.reflexivePowerModules` of reflexive powers under
> multiplication by `s`, with vertex `j_*𝒪_U`, is a colimit cocone.

```lean
theorem isOpen_sectionIsomorphismLocus_and_nonempty_isColimit (F : RankOneReflexiveModules X)
    (s : F.module.sections) :
    IsOpen (sectionIsomorphismLocus F.module s) ∧
      Nonempty (IsColimit (sectionIsomorphismOpenCocone F.obj s))
```

**`Stacks.AlgebraicGeometry.ReflexivePowers.reflexivePower`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ReflexivePowers.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ReflexivePowers.lean#L81). The attribute's comment: “the reflexive powers ℱ^[1] = ℱ, ℱ^[n+1] = (ℱ ⊗ ℱ^[n])^{**}”.

> The reflexive powers of `ℱ`: `ℱ^{[1]} = ℱ` and `ℱ^{[n + 1]} = (ℱ ⊗_{𝒪_X} ℱ^{[n]})^{**}`; the
> value at `0` is `𝒪_X`, the first term of the system `𝒪_X → ℱ → ℱ^{[2]} → ⋯`.

```lean
noncomputable def reflexivePower (F : X.Modules) : ℕ → X.Modules
```

## Tag 0EBP, a lemma

[Tag 0EBP](https://stacks.math.columbia.edu/tag/0EBP) in the Stacks Project.

**`AlgebraicGeometry.exists_ringKrullDim_stalk_eq_one_of_maximal_irreducible_compl_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/SectionLocusCodimension.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/SectionLocusCodimension.lean#L246).

> Assumptions and notation as in [Stacks, Tag 0EBN]: `X` is an integral locally Noetherian normal
> scheme, `ℱ` is a coherent reflexive `𝒪_X`-module of rank one, `s` is a global section of `ℱ`, and
> `U = sectionIsomorphismLocus F s` is the open locus where `s` induces an isomorphism
> `𝒪_{X, x} ⟶ ℱ_x`. If `s` is nonzero then every irreducible component `Z` of `X \ U` has codimension
> one in `X`: `Z` is the closure of a point `ξ`, its generic point, and the local ring `𝒪_{X, ξ}` has
> Krull dimension one, which is the codimension of `Z` in `X` by [Stacks, Tag 02IZ].

```lean
theorem exists_ringKrullDim_stalk_eq_one_of_maximal_irreducible_compl_locus [IsIntegral X]
    [IsLocallyNoetherian X] [IsNormal X] (F : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] (hF : IsReflexive F)
    (hrank : Scheme.Modules.fiberRank F (genericPoint X) = 1)
    (s : F.sections) (hs : s.eval (Opposite.op (⊤ : X.Opens)) ≠ 0) {Z : Set X}
    (hZ : Maximal (fun Z : Set X =>
      IsIrreducible Z ∧ Z ⊆ (sectionIsomorphismLocus F s)ᶜ) Z) :
    ∃ ξ : X, closure {ξ} = Z ∧ ringKrullDim (X.presheaf.stalk ξ) = 1
```

**`AlgebraicGeometry.codimension_eq_one_of_maximal_irreducible_compl_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/SectionLocusCodimension.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/SectionLocusCodimension.lean#L271). The attribute's comment: “every irreducible component of the complement of the isomorphism locus has codimension one in X”.

> Let `X` be an integral locally Noetherian normal scheme, `ℱ` a coherent reflexive `𝒪_X`-module
> of rank one, `s` a nonzero global section, and `U = sectionIsomorphismLocus ℱ s` the open locus of
> [Stacks, Tag 0EBN] where `s` induces an isomorphism `𝒪_{X, x} ⟶ ℱ_x`. Then every irreducible
> component `Z` of `X \ U` has codimension one in `X`, in the sense of [Stacks, Tag 02I3].

```lean
theorem codimension_eq_one_of_maximal_irreducible_compl_locus [IsIntegral X]
    [IsLocallyNoetherian X] [IsNormal X] (F : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] (hF : IsReflexive F)
    (hrank : Scheme.Modules.fiberRank F (genericPoint X) = 1)
    (s : F.sections) (hs : s.eval (Opposite.op (⊤ : X.Opens)) ≠ 0)
    (Z : IrreducibleCloseds X)
    (hZ : Maximal (fun W : Set X =>
      IsIrreducible W ∧ W ⊆ (sectionIsomorphismLocus F s)ᶜ) (Z : Set X)) :
    codimension Z = 1
```

## Tag 0EBQ, a remark

[Tag 0EBQ](https://stacks.math.columbia.edu/tag/0EBQ) in the Stacks Project.

**`AlgebraicGeometry.objective_0EBQ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ReflexiveColimitSections.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ReflexiveColimitSections.lean#L125).

> For `A` a Noetherian normal domain, `M` a finite reflexive `A`-module of rank one and `s ∈ M`
> nonzero, the open `U` of [Stacks, Tag 0EBN] is the complement of `V(𝔭₁) ∪ ⋯ ∪ V(𝔭_r)` for the
> height one primes `𝔭ᵢ` of `A` in the support of `M ⧸ A·s`, and `Γ(U, 𝒪_U)` is the colimit of the
> reflexive powers `M^{[n]}`.

```lean
theorem objective_0EBQ (hrank : Module.rank R M = 1) {s : M} (hs : s ≠ 0) :
    ((AlgebraicGeometry.sectionIsomorphismOpen (Spec R) (tilde M)
          (tildeGlobalSection M s) : Set (Spec R)) =
        (heightOneSupportZeroLocus R s)ᶜ) ∧
      Nonempty (IsColimit (moduleColimitCocone R M hrank hs))
```

**`Stacks.AlgebraicGeometry.ReflexiveHeightOnePrimes.sectionIsomorphismPrimes_eq_compl_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ReflexiveHeightOnePrimes.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ReflexiveHeightOnePrimes.lean#L176). The attribute's comment: “the open U of Lemma 31.30.3, on Spec(A), identified with the complement of the support of M/As; the identification of that support with V(p_1) ∪ … ∪ V(p_r) is Lemma 31.30.4 (Tag 0EBP)”.

> For `A` a Noetherian normal domain, `M` a finite reflexive `A`-module and `s ∈ M` nonzero, the
> set of primes at which `s : A_𝔭 → M_𝔭` is an isomorphism is the complement of the support of
> `M ⧸ A·s`.

```lean
theorem sectionIsomorphismPrimes_eq_compl_support [IsDomain A] [IsNoetherianRing A]
    [IsIntegrallyClosed A] [Module.Finite A M] [Module.IsReflexive A M] {s : M} (hs : s ≠ 0) :
    sectionIsomorphismPrimes A s = (Module.support A (M ⧸ (A ∙ s)))ᶜ
```

**`Stacks.AlgebraicGeometry.ReflexiveHeightOnePrimes.sectionIsomorphismPrimes_eq_compl_heightOneSupportZeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ReflexiveHeightOnePrimes.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ReflexiveHeightOnePrimes.lean#L231). The attribute's comment: “the first display, U = Spec(A) \ (V(p_1) ∪ … ∪ V(p_r)), unconditionally; the colimit Γ(U, O_U) = colim M^[n] is AlgebraicGeometry.objective_0EBQ of Divisors/Reflexive/ReflexiveColimitSections.lean”.

> For `A` a Noetherian normal domain, `M` a finite reflexive `A`-module of rank one and `s ∈ M`
> nonzero, `U = Spec(A) \ (V(𝔭₁) ∪ ⋯ ∪ V(𝔭_r))`, where `U` is the set of primes at which
> `s : A_𝔭 → M_𝔭` is an isomorphism and `𝔭₁, …, 𝔭_r` are the height one primes of `A` in the support
> of `M ⧸ A·s`.

```lean
theorem sectionIsomorphismPrimes_eq_compl_heightOneSupportZeroLocus [IsDomain A]
    [IsNoetherianRing A] [IsIntegrallyClosed A] [Module.Finite A M] [Module.IsReflexive A M]
    (hrank : Module.rank A M = 1) {s : M} (hs : s ≠ 0) :
    sectionIsomorphismPrimes A s = (heightOneSupportZeroLocus A s)ᶜ
```

## Tag 0EBR, a lemma

[Tag 0EBR](https://stacks.math.columbia.edu/tag/0EBR) in the Stacks Project.

**`Stacks.AlgebraicGeometry.SectionLocusAffine.exists_pos_sectionPowStalk_mem_smul_maximalIdeal_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/SectionLocusAffineTag.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/SectionLocusAffineTag.lean#L172). The attribute's comment: “(1) ⇒ (2)”.

> **[Stacks, Tag 0EBR], (1) ⇒ (2).** With `X`, `ℱ`, `s` and `U` as in [Stacks, Tag 0EBN]:
> if the inclusion `j : U → X` is affine, then for every `x ∈ X \ U` there is an `n > 0` with
> `sⁿ ∈ 𝔪_x ℱ^{[n]}_x`.
>
> The hypotheses are the source's: `X` integral, locally Noetherian and normal, `ℱ` coherent,
> reflexive (`hF`) and of rank one (`hrank`, the fibre rank at the generic point), and `s` a global
> section.  The reflexive powers, the multiplication by `s` and the power `sⁿ` are the constructed
> ones of `ReflexivePowers.lean`.
>
> If `s = 0` then `s¹ = 0` lies in every submodule and there is nothing to prove.  Otherwise `U`
> contains the generic point, so the colimit clause of [Stacks, Tag 0EBN] is available at `x`; the
> inverse image `U_x` of `U` under `f_x : Spec 𝒪_{X, x} ⟶ X` is affine because affineness of a
> morphism is stable under base change, and it misses the closed point because `f_x` carries the
> closed point to `x ∉ U`; so `𝔪_x Γ(U_x, 𝒪_{U_x})` is the unit ideal, and the colimit argument
> `exists_pos_powElt_mem_smul` extracts the positive power.

```lean
theorem exists_pos_sectionPowStalk_mem_smul_maximalIdeal_of_isAffineHom
    (X : Scheme.{u}) [IsIntegral X] [IsLocallyNoetherian X] [IsNormal X]
    (F : X.Modules) [F.IsCoherent] (hF : ReflexiveModules.IsReflexive F)
    (hrank : Scheme.Modules.fiberRank F (genericPoint X) = 1) (s : F.sections)
    (hj : IsAffineHom (AlgebraicGeometry.sectionIsomorphismOpen X F s).ι)
    (x : X) (hx : x ∉ AlgebraicGeometry.sectionIsomorphismOpen X F s) :
    ∃ n, 0 < n ∧ sectionPowStalk X F s x n ∈ IsLocalRing.maximalIdeal ↑(X.presheaf.stalk x) •
      (⊤ : Submodule ↑(X.presheaf.stalk x) (reflexivePowerStalk F x n))
```

**`Stacks.AlgebraicGeometry.SectionLocusAffine.isAffineHom_of_forall_exists_pos_sectionPowStalk_mem_smul_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/SectionLocusAffineTag.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/SectionLocusAffineTag.lean#L216). The attribute's comment: “(2) ⇒ (1)”.

> **[Stacks, Tag 0EBR], (2) ⇒ (1).** With `X`, `ℱ`, `s` and `U` as in [Stacks, Tag 0EBN]:
> if for every `x ∈ X \ U` there is an `n > 0` with `sⁿ ∈ 𝔪_x ℱ^{[n]}_x`, then the inclusion
> `j : U → X` is affine.
>
> If `s = 0` then `U` is empty (`isEmpty_sectionIsomorphismLocus_of_eval_eq_zero`) and the
> inclusion of an empty open subscheme is affine.  Otherwise `U` contains the generic point, the
> colimit clause of [Stacks, Tag 0EBN] identifies `(j_*𝒪_U)_x` with `colim ℱ^{[n]}_x`, and
> `mem_smul_of_powElt_mem_smul` carries clause (2) over to `1 ∈ 𝔪_x (j_*𝒪_U)_x`, which is
> `𝔪_x (j_*𝒪_U)_x = (j_*𝒪_U)_x`, at every point off `U`.  That is exactly the hypothesis of
> `AlgebraicGeometry.isAffineHom_of_forall_map_maximalIdeal_eq_top`, the relative-spectrum form of
> the second half of the source's proof.

```lean
theorem isAffineHom_of_forall_exists_pos_sectionPowStalk_mem_smul_maximalIdeal
    (X : Scheme.{u}) [IsIntegral X] [IsLocallyNoetherian X] [IsNormal X]
    (F : X.Modules) [F.IsCoherent] (hF : ReflexiveModules.IsReflexive F)
    (hrank : Scheme.Modules.fiberRank F (genericPoint X) = 1) (s : F.sections)
    (h₂ : ∀ x : X, x ∉ AlgebraicGeometry.sectionIsomorphismOpen X F s →
      ∃ n, 0 < n ∧ sectionPowStalk X F s x n ∈
        IsLocalRing.maximalIdeal ↑(X.presheaf.stalk x) •
          (⊤ : Submodule ↑(X.presheaf.stalk x) (reflexivePowerStalk F x n))) :
    IsAffineHom (AlgebraicGeometry.sectionIsomorphismOpen X F s).ι
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.30, Tag 0EBK](https://stacks.math.columbia.edu/tag/0EBK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
