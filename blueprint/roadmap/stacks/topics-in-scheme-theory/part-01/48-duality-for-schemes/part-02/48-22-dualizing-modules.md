---
declaration: section
origin: cited
lean: Stacks.Duality.IsDualizingModuleOf.shift, Stacks.Duality.IsDualizingModuleOf.exists_isInvertibleModule_iso_sheafTensor, Stacks.Duality.isDualizingModuleOf_iff, Stacks.Duality.isGreatest_neg_of_isDualizingModuleOf, Stacks.Duality.IsDualizingModuleOf.restrict, Stacks.Duality.IsDualizingModuleOf.restrict_of_associatedShiftFunction_genericPoints, Stacks.Duality.isDualizingModuleOf_relativeDualizingModule, Stacks.Duality.normalizedDualizingModule
statement: formalized
proof: formalized
---

# 48.22 Dualizing modules

Section 48.22 of the Stacks Project, [Tag 0AWH](https://stacks.math.columbia.edu/tag/0AWH). 6 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AWH, the section

[Tag 0AWH](https://stacks.math.columbia.edu/tag/0AWH) in the Stacks Project.

**`Stacks.Duality.IsDualizingModuleOf.shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleInvertibleTwist.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleInvertibleTwist.lean#L231). The attribute's comment: “the first half of the section's second warning: the dualizing complex is not unique. A shift of a dualizing complex is a dualizing complex, not isomorphic to it for a nonzero shift, with the same dualizing module in the shifted degree”.

> **Stacks Project, Tag 0AWH.** The dualizing complex is not unique. If `ω` is a dualizing
> module of the dualizing complex `K`, realized in degree `n`, then for every integer `k` the
> shifted complex `K⟦k⟧` is again a dualizing complex, its dualizing module is realized in degree
> `n - k` and is isomorphic to `ω`, and for `k ≠ 0` the complex `K⟦k⟧` is not isomorphic to `K`.

```lean
theorem IsDualizingModuleOf.shift [HasDerivedCategory.{w} X.Modules] {ω : X.Modules}
    {K : DerivedCategory X.Modules} {n : ℤ} (h : IsDualizingModuleOf ω K n) (k : ℤ) :
    IsDualizingModuleOf ((DerivedCategory.homologyFunctor X.Modules (n - k)).obj (K⟦k⟧))
        (K⟦k⟧) (n - k) ∧
      Nonempty ((DerivedCategory.homologyFunctor X.Modules (n - k)).obj (K⟦k⟧) ≅ ω) ∧
      (k ≠ 0 → IsEmpty (K⟦k⟧ ≅ K))
```

**`Stacks.Duality.IsDualizingModuleOf.exists_isInvertibleModule_iso_sheafTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleInvertibleTwist.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleInvertibleTwist.lean#L270). The attribute's comment: “the second half of the section's second warning: the dualizing module is unique up to tensoring by an invertible module. Stated for a connected locally Noetherian scheme: on a disconnected one two dualizing complexes can shift by different amounts on different components and their dualizing modules then need not differ by a twist (counterexample Spec k disjoint union Spec k in the module documentation). The relation between the two complexes is proved, from Tag 0ATP and Tag 0FPG, not assumed”.

> **Stacks Project, Tag 0AWH.** On a connected locally Noetherian scheme the dualizing module
> is unique up to tensoring by an invertible module: if `ω` is a dualizing module of the dualizing
> complex `K` and `ω'` one of the dualizing complex `K'`, there is an invertible `𝒪_X`-module `ℒ`
> with `ω' ≅ ω ⊗_{𝒪_X} ℒ`.

```lean
theorem IsDualizingModuleOf.exists_isInvertibleModule_iso_sheafTensor [ConnectedSpace X]
    [HasDerivedCategory.{w} X.Modules] {ω ω' : X.Modules} {K K' : DerivedCategory X.Modules}
    {n n' : ℤ} (h : IsDualizingModuleOf ω K n) (h' : IsDualizingModuleOf ω' K' n') :
    ∃ ℒ : X.Modules, Stacks.SheafOfModules.Tensor.IsInvertibleModule X.sheaf ℒ ∧
      Nonempty (ω' ≅ ((Stacks.SheafOfModules.Tensor.sheafTensor X.sheaf).obj ω).obj ℒ)
```

**`Stacks.Duality.isDualizingModuleOf_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleMaximalDimension.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleMaximalDimension.lean#L191). The attribute's comment: “the definition the section states: omega\_X = H^n(omega\_X^bullet) with n the smallest integer such that H^n(omega\_X^bullet) is nonzero, for a dualizing complex on a (locally) Noetherian scheme; IsDualizingModuleOf omega K n holds exactly when K is a dualizing complex, n is the least element of the set of degrees with nonzero cohomology, and omega is the cohomology sheaf in degree n”.

> **Stacks Project, Tag 0AWH, the definition.** Let `X` be a locally Noetherian scheme and `K`
> a dualizing complex on `X`. Let `n` be the smallest integer such that `H^n(K)` is nonzero; then
> `H^n(K)` is the dualizing module `ω_X`. This is what `Stacks.Duality.IsDualizingModuleOf ω K n`
> says: it holds exactly when `K` is a dualizing complex, `n` is the least degree with nonzero
> cohomology, and `ω = H^n(K)`.

```lean
theorem isDualizingModuleOf_iff {X : Scheme.{u}} [IsLocallyNoetherian X]
    [HasDerivedCategory.{w} X.Modules] (ω : X.Modules) (K : DerivedCategory X.Modules) (n : ℤ) :
    IsDualizingModuleOf ω K n ↔ IsDualizingComplex K ∧
      IsLeast {i : ℤ | ¬ IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj K)} n ∧
      ω = (DerivedCategory.homologyFunctor X.Modules n).obj K
```

**`Stacks.Duality.isGreatest_neg_of_isDualizingModuleOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleMaximalDimension.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleMaximalDimension.lean#L212). The attribute's comment: “the section's identification of the degree: -n is the maximal value of the dimension function attached to omega\_X^bullet (Tag 0AWF), where n is the least degree in which the dualizing complex has nonvanishing cohomology. The dimension function is associatedShiftFunction K, which Tag 0AWF (isUniversallyCatenary\_and\_isDimensionFunction\_associatedShiftFunction) shows is the normalizing shift of the derived stalks and a dimension function. Stated for a locally Noetherian scheme, which contains the source's Noetherian case”.

> **Stacks Project, Tag 0AWH.** Let `X` be a locally Noetherian scheme and let `ω` be a
> dualizing module of the dualizing complex `K`, realized in degree `n`, the least degree in which
> `K` has nonvanishing cohomology. Then `-n` is the maximal value of the dimension function attached
> to `K` by [Stacks, Tag 0AWF], the function `δ = associatedShiftFunction K` with
> `ω^•_{X,x}⟦-δ(x)⟧` a normalized dualizing complex over `𝒪_{X,x}`.

```lean
theorem isGreatest_neg_of_isDualizingModuleOf {X : Scheme.{u}} [IsLocallyNoetherian X]
    [HasDerivedCategory.{w} X.Modules] {ω : X.Modules} {K : DerivedCategory X.Modules} {n : ℤ}
    (hω : IsDualizingModuleOf ω K n) :
    IsGreatest (Set.range (associatedShiftFunction K)) (-n)
```

**`Stacks.Duality.IsDualizingModuleOf.restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleRestriction.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleRestriction.lean#L64). The attribute's comment: “the section's first warning: the integer n may change on passing to an open U, and then the restriction of omega\_X to U is not omega\_U. The degree can only go up, the two modules agree when it does not change, and when it changes the restriction is zero while omega\_U is not”.

> **Stacks Project, Tag 0AWH, the first warning.** Let `ω` be a dualizing module of the
> dualizing complex `K` on `X`, realized in degree `n`, let `U ⊆ X` be open and let `ω_U` be a
> dualizing module of the restriction `K|_U`, realized in degree `n_U`. Then `n ≤ n_U`; if
> `n = n_U` then `ω|_U ≅ ω_U`; and if the degree changes, `n < n_U`, then `ω|_U` is zero while `ω_U`
> is not, so `ω|_U` is not isomorphic to `ω_U`.

```lean
theorem IsDualizingModuleOf.restrict {ω : X.Modules} {K : DerivedCategory X.Modules} {n : ℤ}
    (h : IsDualizingModuleOf ω K n) (U : X.Opens) [HasDerivedCategory.{w'} U.toScheme.Modules]
    {ωU : U.toScheme.Modules} {nU : ℤ}
    (hU : IsDualizingModuleOf ωU
      ((Scheme.Modules.restrictFunctor U.ι).mapDerivedCategory.obj K) nU) :
    n ≤ nU ∧ (n = nU → Nonempty ((Scheme.Modules.restrictFunctor U.ι).obj ω ≅ ωU)) ∧
      (n < nU → IsZero ((Scheme.Modules.restrictFunctor U.ι).obj ω) ∧ ¬ IsZero ωU ∧
        IsEmpty ((Scheme.Modules.restrictFunctor U.ι).obj ω ≅ ωU))
```

**`Stacks.Duality.IsDualizingModuleOf.restrict_of_associatedShiftFunction_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleRestriction.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleRestriction.lean#L150). The attribute's comment: “the section's closing remark on the first warning: if the dimension function attached to omega\_X^bullet (Tag 0AWF) maps every generic point of X to the same integer, the degree does not change on a nonempty open U and omega\_X restricted to U is omega\_U”.

> **Stacks Project, Tag 0AWH, the closing remark on the first warning.** If the dimension
> function attached to `K` ([Stacks, Tag 0AWF]) takes the same value at every generic point of `X`,
> then the degree of the dualizing module does not change on passing to a nonempty open `U ⊆ X`,
> and the restriction of the dualizing module of `K` is the dualizing module of `K|_U`.

```lean
theorem IsDualizingModuleOf.restrict_of_associatedShiftFunction_genericPoints
    {ω : X.Modules} {K : DerivedCategory X.Modules} {n : ℤ}
    (h : IsDualizingModuleOf ω K n)
    (hgen : ∃ c : ℤ, ∀ ξ ∈ genericPoints X, associatedShiftFunction K ξ = c)
    (U : X.Opens) (hne : (U : Set X).Nonempty) [HasDerivedCategory.{w'} U.toScheme.Modules]
    {ωU : U.toScheme.Modules} {nU : ℤ}
    (hU : IsDualizingModuleOf ωU
      ((Scheme.Modules.restrictFunctor U.ι).mapDerivedCategory.obj K) nU) :
    nU = n ∧ Nonempty ((Scheme.Modules.restrictFunctor U.ι).obj ω ≅ ωU)
```

## Tag 0AWI, an example

[Tag 0AWI](https://stacks.math.columbia.edu/tag/0AWI) in the Stacks Project.

**`Stacks.Duality.isDualizingModuleOf_relativeDualizingModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingModuleProperCharts.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingModuleProperCharts.lean#L96). The attribute's comment: “the whole example”.

> **Stacks Project, Tag 0AWI (Example 48.22.1).** Let `S` be affine with
> `A = Γ(S, ⊤)` a Noetherian local ring, `ω_S^•` modelled on `S` by a normalized dualizing complex
> `ω_A^•`, `f : X ⟶ S` proper and `ω_X^• = f^!ω_S^• = a(ω_S^•)`. Then `ω_X = H^{-dim X}(ω_X^•)` is a
> coherent sheaf, and, `X` being nonempty, a dualizing module: `ω_X^•` is a dualizing complex and
> `-dim X` is the least degree in which it has nonzero cohomology.

```lean
theorem isDualizingModuleOf_relativeDualizingModule
    (f : X ⟶ S) [IsProper f] (ωS : quasiCoherentDerivedCategory S)
    (ω : DerivedCategory (ModuleCat.{u} Γ(S, ⊤)))
    (hω : Dualizing.IsNormalizedDualizingComplex.{u, u} ω)
    (hmodel : IsTildeModelOnAnyModel ωS.obj ⊤ (isAffineOpen_top S) ω) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    (relativeDualizingModule f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        ωS).IsCoherent ∧
      (Nonempty X → IsDualizingModuleOf
        (relativeDualizingModule f (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ωS)
        (relativeDualizingComplex f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          ωS).obj (-(natDim X : ℤ)))
```

## Tag 0AWJ, an example

[Tag 0AWJ](https://stacks.math.columbia.edu/tag/0AWJ) in the Stacks Project.

**`Stacks.Duality.normalizedDualizingModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleOverField.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleOverField.lean#L117). The attribute's comment: “the definition: omega\_X = H^\{-dim X}(omega\_X^bullet) for the complex normalized relative to k[0]”.

> **The dualizing module `ω_X = H^{-dim(X)}(ω_X^•)`** of [Stacks, Tag 0AWJ]: the cohomology
> sheaf in degree minus the dimension of `X` of a complex normalized relative to a chosen complex
> on the base. Over a field, with `ω_S^• = k[0]`, this is the customary dualizing module of an
> equidimensional scheme of finite type over `k`.

```lean
def normalizedDualizingModule (𝒩 : Normalized A hp ωS 𝒰) : X.Modules
```

**`Stacks.Duality.normalizedUpperShriekOverField`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleOverField.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleOverField.lean#L224). The attribute's comment: “the second assertion: for X separated over k the normalized complex is f^! O\_\{Spec k}. RESTRICTED: the upper-shriek formalism of Stacks 0A9Y/0ATX/0ATY is the parameter UpperShriek, pending its landing”.

> **[Stacks, Tag 0AWJ]** For `X` separated and of finite type over a field `k` with structure
> morphism `f : X ⟶ Spec(k)`, the complex `f^!𝒪_{Spec(k)}` is normalized relative to `k[0]`: this
> is the identification `ω_X^• = f^!𝒪_{Spec(k)}` the example records, by [Stacks, Tag 0AUE].

```lean
def normalizedUpperShriekOverField {ι : Type w} (𝒰 : SeparatedCovering p ι) :
    Normalized A (isFiniteTypeOverNoetherian_of_field p)
      (DerivedPushforward.derivedStructureSheaf (Spec (.of k))).obj 𝒰
```

**`Stacks.Duality.isDualizingComplex_normalizedDualizingComplex_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/DualizingModuleOverFieldNagata.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/DualizingModuleOverFieldNagata.lean#L62). The attribute's comment: “omega\_X^bullet, the dualizing complex normalized relative to k[0]”.

> **[Stacks, Tag 0AWJ], the complex `ω_X^•`.** For `X` of finite type over a field `k`, the
> dualizing complex `ω_X^•` normalized relative to `k[0]` (`k[0]` being a dualizing complex on
> `Spec(k)`) is a dualizing complex, and it is unique up to unique isomorphism: any complex
> normalized relative to `k[0]` is isomorphic to it by exactly one isomorphism compatible with
> the normalizations.

```lean
theorem isDualizingComplex_normalizedDualizingComplex_of_field :
    haveI := (isFiniteTypeOverNoetherian_of_field p).source_noetherian
    IsDualizingComplex (normalizedDualizingComplex (isFiniteTypeOverNoetherian_of_field p)
        (derivedStructureSheafPlus (Spec (.of k)))
        (isDualizingComplex_derivedStructureSheafPlus_of_field k)).complex.obj.obj ∧
    ∀ 𝒦 : NormalizedOnOpens UpperShriek.nagata (isFiniteTypeOverNoetherian_of_field p)
        (derivedStructureSheafPlus (Spec (.of k))),
      ∃! e : (normalizedDualizingComplex (isFiniteTypeOverNoetherian_of_field p)
          (derivedStructureSheafPlus (Spec (.of k)))
          (isDualizingComplex_derivedStructureSheafPlus_of_field k)).complex ≅ 𝒦.complex,
        ∀ (W : X.Opens) (hW : IsShriekable (W.ι ≫ p)),
          (UpperShriek.nagata.shriek W.ι
              ((isFiniteTypeOverNoetherian_of_field p).isShriekable_ι W)).mapIso e ≪≫
            𝒦.localIso W hW =
          (normalizedDualizingComplex (isFiniteTypeOverNoetherian_of_field p)
            (derivedStructureSheafPlus (Spec (.of k)))
            (isDualizingComplex_derivedStructureSheafPlus_of_field k)).localIso W hW
```

**`Stacks.Duality.dualizingModuleOfCompactifications_nagata_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/DualizingModuleOverFieldNagata.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/DualizingModuleOverFieldNagata.lean#L88). The attribute's comment: “omega\_X = H^\{-dim X}(omega\_X^bullet)”.

> **[Stacks, Tag 0AWJ], the module `ω_X`.** For `X` of finite type over a field `k`, the
> dualizing module `ω_X` is `H^{-dim(X)}(ω_X^•)`, the cohomology sheaf in degree minus the dimension
> of `X` of the dualizing complex normalized relative to `k[0]`.

```lean
theorem dualizingModuleOfCompactifications_nagata_eq :
    dualizingModuleOfCompactifications nagataCompactification p =
      (DerivedCategory.homologyFunctor X.Modules
        (-(ENat.toNat ((topologicalKrullDim X).getD 0) : ℤ))).obj
        (normalizedDualizingComplex (isFiniteTypeOverNoetherian_of_field p)
          (derivedStructureSheafPlus (Spec (.of k)))
          (isDualizingComplex_derivedStructureSheafPlus_of_field k)).complex.obj.obj
```

**`Stacks.Duality.existsUnique_iso_upperShriekPlus_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/DualizingModuleOverFieldNagata.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/DualizingModuleOverFieldNagata.lean#L104). The attribute's comment: “for X separated over k, omega\_X^bullet = f^! O\_\{Spec k}”.

> **[Stacks, Tag 0AWJ], the separated case.** If `X` is separated and of finite type over a
> field `k`, then `ω_X^• = f^! 𝒪_{Spec(k)}`, `f : X ⟶ Spec(k)` being the structure morphism and
> `f^!` the upper shriek functor of [Stacks, Tag 0A9Y] at any compactification `j` of `f`: there is
> exactly one isomorphism `ω_X^• ≅ f^!_j 𝒪_{Spec(k)}` which, followed by the comparison with the
> Nagata compactification, carries the normalization of `ω_X^•` on each open `W` separated over `k`
> to the canonical `(f^! 𝒪_{Spec(k)})|_W ≅ (W → Spec(k))^! 𝒪_{Spec(k)}`.

```lean
theorem existsUnique_iso_upperShriekPlus_of_field [IsSeparated p]
    (j : CompactificationOf (Over.mk p)) :
    haveI := isNoetherian_spec_of_field k
    ∃! e : (normalizedDualizingComplex (isFiniteTypeOverNoetherian_of_field p)
        (derivedStructureSheafPlus (Spec (.of k)))
        (isDualizingComplex_derivedStructureSheafPlus_of_field k)).complex ≅
      (upperShriekPlus (ftsHomOf p (isShriekable_of_field p).separatedFiniteType
        (isSeparatedFiniteType_id _) (Category.comp_id p)) j).obj
        (derivedStructureSheafPlus (Spec (.of k))),
      ∀ (W : X.Opens) (hW : IsShriekable (W.ι ≫ p)),
        (UpperShriek.nagata.shriek W.ι
            ((isFiniteTypeOverNoetherian_of_field p).isShriekable_ι W)).mapIso
            (e ≪≫ (DominatingCompactification.upperShriekPlusIso (ftsHomOf p
              (isShriekable_of_field p).separatedFiniteType (isSeparatedFiniteType_id _)
              (Category.comp_id p)) j
              (nagataCompactification p (isShriekable_of_field p))).app
              (derivedStructureSheafPlus (Spec (.of k)))) ≪≫
          upperShriekLocalIso UpperShriek.nagata (isFiniteTypeOverNoetherian_of_field p)
            (isShriekable_of_field p) (derivedStructureSheafPlus (Spec (.of k))) hW =
        (normalizedDualizingComplex (isFiniteTypeOverNoetherian_of_field p)
          (derivedStructureSheafPlus (Spec (.of k)))
          (isDualizingComplex_derivedStructureSheafPlus_of_field k)).localIso W hW
```

**`Stacks.Duality.normalizedDualizingComplexIsoRelativeDualizingComplexOfField`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/DualizingModuleOverFieldNagata.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/DualizingModuleOverFieldNagata.lean#L134). The attribute's comment: “for X proper over k, omega\_X^bullet = a(O\_\{Spec k}), the complex of Example 0AWI”.

> **[Stacks, Tag 0AWJ], the proper case: `ω_X^• = a(𝒪_{Spec(k)})`.** If `X` is proper over a
> field `k`, the dualizing complex normalized relative to `k[0]` is the twisted inverse image
> `a(𝒪_{Spec(k)})` of [Stacks, Tag 0A9E], that is, the relative dualizing complex `f^! ω_S^•` of
> [Stacks, Tag 0AWI] for `S = Spec(k)` and `ω_S^• = k[0]`.

```lean
def normalizedDualizingComplexIsoRelativeDualizingComplexOfField [IsProper p] :
    haveI := isNoetherian_spec_of_field k
    haveI := (isFiniteTypeOverNoetherian_of_field p).source_noetherian
    (normalizedDualizingComplex (isFiniteTypeOverNoetherian_of_field p)
        (derivedStructureSheafPlus (Spec (.of k)))
        (isDualizingComplex_derivedStructureSheafPlus_of_field k)).complex.obj ≅
      relativeDualizingComplex p (isQuasicoherent_homology_derivedPushforward_of_qcqs p)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))
```

**`Stacks.Duality.dualizingModuleOfCompactifications_nagata_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/DualizingModuleOverFieldNagata.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/DualizingModuleOverFieldNagata.lean#L159). The attribute's comment: “for X proper over k, this is a special case of Example 0AWI”.

> **[Stacks, Tag 0AWJ], the proper case is a special case of [Stacks, Tag 0AWI].** If `X` is
> proper over a field `k`, then `ω_X` is the relative dualizing module of [Stacks, Tag 0AWI] for
> `S = Spec(k)` and `ω_S^• = k[0]` (a normalized dualizing complex over the local ring `k`); hence
> `ω_X` is coherent and, `X` being nonempty, a dualizing module: `ω_X^•` is a dualizing complex and
> `-dim(X)` is the least degree in which it has nonzero cohomology.

```lean
theorem dualizingModuleOfCompactifications_nagata_of_isProper [IsProper p] :
    haveI := isNoetherian_spec_of_field k
    haveI := (isFiniteTypeOverNoetherian_of_field p).source_noetherian
    Nonempty (dualizingModuleOfCompactifications nagataCompactification p ≅
        relativeDualizingModule p (isQuasicoherent_homology_derivedPushforward_of_qcqs p)
          (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))) ∧
      (dualizingModuleOfCompactifications nagataCompactification p).IsCoherent ∧
      (Nonempty X → IsDualizingModuleOf
        (dualizingModuleOfCompactifications nagataCompactification p)
        (normalizedDualizingComplex (isFiniteTypeOverNoetherian_of_field p)
          (derivedStructureSheafPlus (Spec (.of k)))
          (isDualizingComplex_derivedStructureSheafPlus_of_field k)).complex.obj.obj
        (-(natDim X : ℤ)))
```

## Tag 0AWK, a lemma

[Tag 0AWK](https://stacks.math.columbia.edu/tag/0AWK) in the Stacks Project.

**`Stacks.Duality.IsDualizingModuleOf.sheafHasPropertySk_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleSupportSerre.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleSupportSerre.lean#L52). The attribute's comment: “the (S₂) clause”.

> **Stacks Project, Tag 0AWK**, the `(S₂)` clause. The dualizing module of a dualizing complex
> on a connected Noetherian scheme satisfies Serre's condition `(S₂)`.

```lean
public theorem IsDualizingModuleOf.sheafHasPropertySk_two {X : Scheme.{u}} [IsNoetherian X]
    [ConnectedSpace X] [HasDerivedCategory.{w} X.Modules] {ω : X.Modules}
    {K : DerivedCategory X.Modules} {n : ℤ} (h : IsDualizingModuleOf ω K n) :
    SheafHasPropertySk X ω 2
```

**`Stacks.Duality.IsDualizingModuleOf.supp_eq_and_isCoherent_and_sheafHasPropertySk_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleSupportSerreFull.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleSupportSerreFull.lean#L218).

> **Stacks Project, Tag 0AWK.** Let `X` be a connected Noetherian scheme and let `ω` be a
> dualizing module on `X`, the cohomology sheaf of a dualizing complex `K` in the leftmost degree
> `n` in which `K` has nonvanishing cohomology. Then the support of `ω` is the union of the
> irreducible components of maximal dimension with respect to any dimension function `δ`, and `ω`
> is a coherent `𝒪_X`-module having property `(S₂)`.

```lean
theorem IsDualizingModuleOf.supp_eq_and_isCoherent_and_sheafHasPropertySk_two
    [ConnectedSpace X] (h : IsDualizingModuleOf ω K n) :
    (∀ δ : DimensionFunction X,
      (⟨ω.val, ω.isSheaf⟩ : RingedSpace.ModuleSheaf.{u} X.toRingedSpace).supp =
        {x : X | ∃ ξ ∈ genericPoints X, x ∈ closure {ξ} ∧
          ∀ η ∈ genericPoints X, δ η ≤ δ ξ}) ∧
      _root_.SheafOfModules.IsCoherent ω ∧ SheafHasPropertySk X ω 2
```

## Tag 0AWN, a lemma

[Tag 0AWN](https://stacks.math.columbia.edu/tag/0AWN) in the Stacks Project.

**`Stacks.Duality.vanishing_and_support_relativeDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ProperOverLocalBaseCharts.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/ProperOverLocalBaseCharts.lean#L92).

> **Stacks Project, Tag 0AWN (Lemma 48.22.4).** Let `S` be affine with `A = Γ(S, ⊤)` a
> Noetherian local ring, `ω_S^•` the complex associated to a normalized dualizing complex `ω_A^•`,
> `f : X ⟶ S` proper, `ω_X^• = f^!ω_S^• = a(ω_S^•)` and `ω_X = H^{-dim X}(ω_X^•)`
> ([Stacks, Tag 0AWI]). Then
> 1. `H^i(ω_X^•) ≠ 0` implies `i ∈ {-dim X, …, 0}`;
> 2. the support of `H^i(ω_X^•)` has dimension at most `-i`;
> 3. `Supp(ω_X)` is the union of the irreducible components of dimension `dim X`;
> 4. `ω_X` (which is coherent) has property `(S₂)`.

```lean
theorem vanishing_and_support_relativeDualizingComplex
    (f : X ⟶ S) [IsProper f] (ωS : quasiCoherentDerivedCategory S)
    (ω : DerivedCategory (ModuleCat.{u} Γ(S, ⊤)))
    (hω : Dualizing.IsNormalizedDualizingComplex.{u, u} ω)
    (hmodel : IsTildeModelOnAnyModel ωS.obj ⊤ (isAffineOpen_top S) ω) :
    let L := (relativeDualizingComplex f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      ωS).obj
    (∀ i : ℤ, ¬ Limits.IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj L) →
      i ≤ 0 ∧ (((-i).toNat : ℕ) : WithBot ℕ∞) ≤ topologicalKrullDim X) ∧
    (∀ i : ℤ, topologicalKrullDim (_root_.SheafOfModules.supp
        ((DerivedCategory.homologyFunctor X.Modules i).obj L)) ≤
      if i ≤ 0 then (((-i).toNat : ℕ) : WithBot ℕ∞) else ⊥) ∧
    (relativeDualizingModule f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        ωS).IsCoherent ∧
    SheafHasPropertySk X (relativeDualizingModule f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ωS) 2 ∧
    _root_.SheafOfModules.supp (relativeDualizingModule f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ωS) =
      ⋃₀ {C ∈ irreducibleComponents X | topologicalKrullDim C = topologicalKrullDim X}
```

**`Stacks.Duality.supp_relativeDualizingModule_eq_topDimensionalComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/VanishingAndSupport.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/VanishingAndSupport.lean#L291). The attribute's comment: “part (3): Supp(omega\_X) is the union of the components of dimension dim(X). RESTRICTED: two explicit hypotheses. hloc is the local description of omega\_X^bullet, a Stacks.Duality.HasNormalizedStalks; see part (1) for what it records and why. hcomp is a statement about a catenary Noetherian scheme with no dualizing complex in it -- that a point satisfies dim(closure \{x}) + dim(O\_\{X,x}) = dim(X) exactly when it lies on an irreducible component of dimension dim(X); its analogue over a Noetherian local ring is the catenary step inside Dualizing.support\_canonicalModule of Tag 0AWE, but the scheme-level statement is not proved here. The dualizing content is proved and is unconditional given hloc: supp\_relativeDualizingModule\_eq\_setOf identifies Supp(omega\_X) with the locus where that equality holds, by the lower degree bound of Tag 0A7U and the nonvanishing of the canonical module of Tag 0A7V on the stalk”.

> **Stacks Project, Tag 0AWN, part (3).** Let `X/A` with `ω_X^•` and `ω_X` be as in
> [Stacks, Tag 0AWI]. Then `Supp(ω_X)` is the union of the irreducible components of `X` of
> dimension `dim(X)`, given the hypothesis `hcomp` that a point `x` satisfies
> `dim(closure {x}) + dim(𝒪_{X,x}) = dim(X)` exactly when it lies on an irreducible component of `X`
> of dimension `dim(X)`.

```lean
theorem supp_relativeDualizingModule_eq_topDimensionalComponents
    (hloc : HasNormalizedStalks (relativeDualizingComplex f hpush ωY).obj n)
    (hcomp : ∀ x : X, topologicalKrullDim (closure ({x} : Set X)) +
          ringKrullDim (X.presheaf.stalk x) = (n : WithBot ℕ∞) ↔
        x ∈ ⋃₀ {C ∈ irreducibleComponents X | topologicalKrullDim C = (n : WithBot ℕ∞)}) :
    _root_.SheafOfModules.supp (relativeDualizingModule f hpush ωY) =
      ⋃₀ {C ∈ irreducibleComponents X | topologicalKrullDim C = (n : WithBot ℕ∞)}
```

## Tag 0AWP, a lemma

[Tag 0AWP](https://stacks.math.columbia.edu/tag/0AWP) in the Stacks Project.

**`Stacks.Duality.dualizingModuleRepresentableBy`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingModuleRepresentabilityLocalBase.lean, line 994](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingModuleRepresentabilityLocalBase.lean#L994). The attribute's comment: “the whole lemma, in the setting of Example 0AWI with omega\_X^bullet the twisted inverse image of omega\_S^bullet (the relative dualizing complex of the 0AWI definition) and omega\_A = H^\{-dim A}(omega\_A^bullet); the functor is represented on all quasi-coherent modules, which contain the coherent ones, and d may be any upper bound for dim(X\_s) with dim(X) = d + dim(A)”.

> **[Stacks, Tag 0AWP].** Let `(A, 𝔪, κ)` be a Noetherian local ring and let `ω_S^•` be an
> object of `D_QCoh(𝒪_{Spec A})` corresponding to a normalized dualizing complex `ω_A^•`. Let
> `f : X ⟶ Spec A` be proper, `ω_X^• = f^×ω_S^•` and `ω_X = H^{-dim(X)}(ω_X^•)`, as in
> Example [Stacks, Tag 0AWI]. Let `d` bound the dimension of the closed fibre `X_s` and suppose
> `dim(X) = d + dim(A)`. Then `ω_X` represents the functor
>
>   `ℱ ↦ Hom_A(H^d(X, ℱ), ω_A)`,   `ω_A = H^{-dim(A)}(ω_A^•)`,
>
> on the quasi-coherent `𝒪_X`-modules — so in particular on the coherent ones.
>
> The represented functor is `ℱ ↦ Hom_A(H^d(X, ℱ), ω_A)` with `H^d(X, ℱ)` the classical sheaf
> cohomology with its `A`-module structure, and the representation is
> `Stacks.Duality.dualizingModuleHomAddEquiv`, natural by
> `Stacks.Duality.dualizingModuleHomAddEquiv_naturality`. Nothing is carried: part (1) of
> [Stacks, Tag 0AWN], the vanishing of `H^i(ω_X^•)` below `-dim(X)` that the source's first
> equality needs, is `Stacks.Duality.isGE_relativeDualizingComplex_of_closedFibre_dim_le`.

```lean
def dualizingModuleRepresentableBy :
    (((SheafOfModules.isQuasicoherent X.ringCatSheaf).ι ⋙
        Stacks.LocalCohomology.cohomologyOverBaseFunctor.{u, u} A f d).op ⋙
      yoneda.obj ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-(e : ℤ))).obj
        ((derivedGlobalSectionsQuasicoherent (CommRingCat.of A)).obj ωS))).RepresentableBy
      (⟨relativeDualizingModule f (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ωS,
        isQuasicoherent_relativeDualizingModule f
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ωS⟩ :
        (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.22, Tag 0AWH](https://stacks.math.columbia.edu/tag/0AWH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
