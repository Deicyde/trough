---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Modules.isPseudoCoherentFrom_some_iff_forall_fin, AlgebraicGeometry.Scheme.Hom.IsPseudoCoherentFrom, AlgebraicGeometry.Scheme.Hom.IsPseudoCoherent, AlgebraicGeometry.Scheme.Hom.IsModulePseudoCoherentFrom, AlgebraicGeometry.Scheme.Hom.IsModulePseudoCoherent, AlgebraicGeometry.Scheme.Hom.isQuasicoherent_homology_of_isPseudoCoherentFrom, AlgebraicGeometry.Scheme.Hom.isQuasicoherentDerived_of_isPseudoCoherent, AlgebraicGeometry.Scheme.Modules.isPseudoCoherentFromAfterPushforward_restrict
statement: formalized
proof: formalized
---

# 37.59 Relative pseudo-coherence

Section 37.59 of the Stacks Project, [Tag 09UH](https://stacks.math.columbia.edu/tag/09UH). 18 tags here are carried by 33 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09VC, a lemma

[Tag 09VC](https://stacks.math.columbia.edu/tag/09VC) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.isPseudoCoherentFrom_some_iff_forall_fin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/SideCondition.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/SideCondition.lean#L338).

> **Stacks 09VC.** Let `f : X ⟶ S` be a morphism of affine schemes locally of finite type, let
> `E` be an object of `D(𝒪_X)` and let `m` be an integer. Then `m`-pseudo-coherence of the derived
> pushforward of `E` along *some* closed immersion of `X` into a finite-dimensional affine space
> over `S` factoring `f` is equivalent to `m`-pseudo-coherence of the derived pushforward along
> *every* such closed immersion.
>
> This is
> `AlgebraicGeometry.Scheme.Modules.isPseudoCoherentFrom_some_iff_forall_of_transport_fin`, whose
> transport hypothesis is supplied by the two halves of Stacks 09VA —
> `AlgebraicGeometry.Scheme.Modules.isPseudoCoherentFrom_pushforward_mapDerivedCategory` and
> `AlgebraicGeometry.Scheme.Modules.isPseudoCoherentFrom_of_pushforward_mapDerivedCategory` — and
> whose side condition is
> `AlgebraicGeometry.Scheme.Modules.isPseudoCoherent_singleFunctor_pushforward_unit_affineSpace`.
> Nothing is assumed.

```lean
public theorem isPseudoCoherentFrom_some_iff_forall_fin {X S : Scheme.{u}} [IsAffine X]
    [IsAffine S] (f : X ⟶ S) [LocallyOfFiniteType f] (E : DerivedCategory X.Modules) (m : ℤ) :
    (∃ (n : ℕ) (i : X ⟶ AffineSpace (ULift.{u} (Fin n)) S),
      IsClosedImmersion i ∧
        i ≫ (AffineSpace.over (ULift.{u} (Fin n)) S).hom = f ∧
          IsPseudoCoherentFromAfterPushforward i E m) ↔
      (∀ (n : ℕ) (i : X ⟶ AffineSpace (ULift.{u} (Fin n)) S),
        IsClosedImmersion i →
          i ≫ (AffineSpace.over (ULift.{u} (Fin n)) S).hom = f →
            IsPseudoCoherentFromAfterPushforward i E m)
```

## Tag 09UI, a definition

[Tag 09UI](https://stacks.math.columbia.edu/tag/09UI) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.IsPseudoCoherentFrom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/Relative.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/Relative.lean#L75). The attribute's comment: “part (1)”.

> An object `E` of the derived category of `𝒪_X`-modules is relatively `m`-pseudo-coherent for
> `f : X ⟶ S` locally of finite type if there are an affine open cover `V` of `S` and, for each
> `V i`, an affine open cover `U` of `f⁻¹(V i)` such that the restriction of `E` to each `U j`
> becomes `m`-pseudo-coherent after derived pushforward along some closed immersion
> `U j ⟶ 𝔸ⁿ_{V i}` over `V i` through which `f` restricted to `U j` factors.

```lean
public abbrev IsPseudoCoherentFrom {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (E : DerivedCategory X.Modules) (m : ℤ) : Prop
```

**`AlgebraicGeometry.Scheme.Hom.IsPseudoCoherent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/Relative.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/Relative.lean#L93). The attribute's comment: “part (2)”.

> An object of the derived category of `𝒪_X`-modules is relatively pseudo-coherent for `f` if it
> is relatively `m`-pseudo-coherent for every integer `m`.

```lean
public abbrev IsPseudoCoherent {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (E : DerivedCategory X.Modules) : Prop
```

**`AlgebraicGeometry.Scheme.Hom.IsModulePseudoCoherentFrom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/Relative.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/Relative.lean#L100). The attribute's comment: “part (3)”.

> A sheaf of `𝒪_X`-modules is relatively `m`-pseudo-coherent for `f` if it is so as an object of
> the derived category concentrated in degree zero.

```lean
public abbrev IsModulePseudoCoherentFrom {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F : X.Modules) (m : ℤ) : Prop
```

**`AlgebraicGeometry.Scheme.Hom.IsModulePseudoCoherent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/Relative.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/Relative.lean#L107). The attribute's comment: “part (4)”.

> A sheaf of `𝒪_X`-modules is relatively pseudo-coherent for `f` if it is so as an object of the
> derived category concentrated in degree zero.

```lean
public abbrev IsModulePseudoCoherent {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F : X.Modules) : Prop
```

## Tag 0CSU, a lemma

[Tag 0CSU](https://stacks.math.columbia.edu/tag/0CSU) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isQuasicoherent_homology_of_isPseudoCoherentFrom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeQuasicoherentCohomology.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeQuasicoherentCohomology.lean#L98). The attribute's comment: “quasi-coherence of the cohomology sheaves above the bound”.

> Let `f : X ⟶ S` be a morphism of schemes locally of finite type and let `E` be an object of
> `D(𝒪_X)` which is `m`-pseudo-coherent relative to `S`. Then the cohomology sheaf `H^i(E)` is a
> quasi-coherent `𝒪_X`-module for every `i > m`.

```lean
public theorem isQuasicoherent_homology_of_isPseudoCoherentFrom {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (E : DerivedCategory X.Modules) (m i : ℤ)
    (hE : f.IsPseudoCoherentFrom E m) (hi : m < i) :
    ((DerivedCategory.homologyFunctor X.Modules i).obj E).IsQuasicoherent
```

**`AlgebraicGeometry.Scheme.Hom.isQuasicoherentDerived_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeQuasicoherentCohomology.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeQuasicoherentCohomology.lean#L123). The attribute's comment: “membership in the quasi-coherent derived category”.

> Let `f : X ⟶ S` be a morphism of schemes locally of finite type and let `E` be an object of
> `D(𝒪_X)` which is pseudo-coherent relative to `S`. Then `E` is an object of `D_QCoh(𝒪_X)`, that
> is, `H^i(E)` is quasi-coherent for every `i`.

```lean
public theorem isQuasicoherentDerived_of_isPseudoCoherent {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (E : DerivedCategory X.Modules) (hE : f.IsPseudoCoherent E) :
    DerivedCategoryB.derivedCategoryB
      (_root_.SheafOfModules.isQuasicoherent X.ringCatSheaf) E
```

## Tag 09VD, a lemma

[Tag 09VD](https://stacks.math.columbia.edu/tag/09VD) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.isPseudoCoherentFromAfterPushforward_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/StandardOpenSideCondition.lean, line 701](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/StandardOpenSideCondition.lean#L701).

> **Stacks 09VD.** Let `S` be affine, let `V` be a standard open of `S`, let `X` be affine and
> `f : X ⟶ V` locally of finite type, let `E` be an object of `D(𝒪_X)` and let `U` be an affine open
> of `X`. If the equivalent conditions of Stacks 09VC hold for the pair `(X ⟶ V, E)`, then they hold
> for the pair `(U ⟶ S, E|_U)`.
>
> This is
> `AlgebraicGeometry.Scheme.Modules.exists_isPseudoCoherentFromAfterPushforward_affineOpen'` with
> its three hypotheses discharged:
> `AlgebraicGeometry.Scheme.Modules.pushforwardStructureSheafPseudoCoherentOver_basicOpen` at the
> base `S` and at the base `V`, and
> `AlgebraicGeometry.Scheme.Modules.pushforwardStructureSheafPseudoCoherentOver_affineSpace` for the
> affine spaces over `V` mapping to the affine spaces over `S`. The last of the three is what needs
> `V` to be a *standard* open.

```lean
public theorem isPseudoCoherentFromAfterPushforward_restrict {S X : Scheme.{u}}
    [IsAffine S] [IsAffine X] (V : S.affineOpens) (hV : ∃ a : Γ(S, ⊤), V.1 = S.basicOpen a)
    (f : X ⟶ (V.1 : Scheme.{u})) [LocallyOfFiniteType f] [QuasiCompact f]
    (U : X.affineOpens) (E : DerivedCategory X.Modules) (m : ℤ) :
    (∃ (n : ℕ) (i : X ⟶ AffineSpace (ULift.{u} (Fin n)) (V.1 : Scheme.{u})),
      IsClosedImmersion i ∧
        i ≫ (AffineSpace.over (ULift.{u} (Fin n)) (V.1 : Scheme.{u})).hom = f ∧
          IsPseudoCoherentFromAfterPushforward i E m) →
      (∃ (n : ℕ) (i : (U.1 : Scheme.{u}) ⟶ AffineSpace (ULift.{u} (Fin n)) S),
        IsClosedImmersion i ∧
          i ≫ (AffineSpace.over (ULift.{u} (Fin n)) S).hom = U.1.ι ≫ f ≫ V.1.ι ∧
            IsPseudoCoherentFromAfterPushforward i
              ((restrictFunctor U.1.ι).mapDerivedCategory.obj E) m)
```

## Tag 09VE, a lemma

[Tag 09VE](https://stacks.math.columbia.edu/tag/09VE) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.isPseudoCoherentFrom_some_iff_forall_standardCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/StandardOpenSideCondition.lean, line 668](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/StandardOpenSideCondition.lean#L668).

> **Stacks 09VE.** Let `f : X ⟶ S` be a morphism of affine schemes locally of finite type, let
> `E` be an object of `D(𝒪_X)` and let the basic opens of `g : Fin n → Γ(X, ⊤)` be a standard affine
> open cover of `X`. Then the equivalent conditions of Stacks 09VC hold for every pair
> `(X_{gⱼ} ⟶ S, E|_{X_{gⱼ}})` if and only if they hold for the pair `(X ⟶ S, E)`.
>
> This is
> `AlgebraicGeometry.Scheme.Modules.isPseudoCoherentFrom_some_iff_forall_basicOpen'` with its
> hypothesis `hOb` discharged by
> `AlgebraicGeometry.Scheme.Modules.pushforwardStructureSheafPseudoCoherentOver_basicOpen`.

```lean
public theorem isPseudoCoherentFrom_some_iff_forall_standardCover {X S : Scheme.{u}}
    [IsAffine X] [IsAffine S] (f : X ⟶ S) [LocallyOfFiniteType f] [QuasiCompact f]
    (E : DerivedCategory X.Modules) (m : ℤ) {n : ℕ} (g : Fin n → Γ(X, ⊤))
    (hg : PrimeSpectrum.IsStandardOpenCoverOfSpectrum g) :
    (∀ j : Fin n, ∃ (k : ℕ) (i : (X.basicOpen (g j)).toScheme ⟶
        AffineSpace (ULift.{u} (Fin k)) S),
      IsClosedImmersion i ∧
        i ≫ (AffineSpace.over (ULift.{u} (Fin k)) S).hom = (X.basicOpen (g j)).ι ≫ f ∧
          IsPseudoCoherentFromAfterPushforward i
            ((restrictFunctor (X.basicOpen (g j)).ι).mapDerivedCategory.obj E) m) ↔
      (∃ (k : ℕ) (i : X ⟶ AffineSpace (ULift.{u} (Fin k)) S),
        IsClosedImmersion i ∧
          i ≫ (AffineSpace.over (ULift.{u} (Fin k)) S).hom = f ∧
            IsPseudoCoherentFromAfterPushforward i E m)
```

## Tag 09UJ, a lemma

[Tag 09UJ](https://stacks.math.columbia.edu/tag/09UJ) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_forall_affinePair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/AffinePairLocality.lean, line 501](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/AffinePairLocality.lean#L501). The attribute's comment: “affine-open characterization”.

> **Stacks 09UJ.** For `f : X ⟶ S` locally of finite type, `E` an object of the derived
> category of `𝒪_X`-modules and `m` an integer, `E` is relatively `m`-pseudo-coherent if and only
> if the local condition of Stacks 09UI holds at every compatible pair of affine opens
> `U ⊆ f ⁻¹ᵁ V`.
>
> The two implications are
> `AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_of_forall_affinePair` and
> `AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFromOnAffinePair_of_isPseudoCoherentFrom`.

```lean
public theorem isPseudoCoherentFrom_iff_forall_affinePair [LocallyOfFiniteType f]
    (E : DerivedCategory X.Modules) (m : ℤ) : AffinePairComparison f E m
```

**`AlgebraicGeometry.Scheme.Hom.IsPseudoCoherentFrom.resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/AffinePairLocality.lean, line 536](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/AffinePairLocality.lean#L536). The attribute's comment: “restriction to open subschemes”. References: SGA 6 III (1.1), “(i)”.

> **Stacks 09UJ, the final assertion.** If `E` is `m`-pseudo-coherent relative to `S`, then for
> every pair of open subschemes `U ⊆ X` and `V ⊆ S` with `f(U) ⊆ V` the restriction `E|_U` is
> `m`-pseudo-coherent relative to `V`.
>
> By `AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_forall_affinePair` it is enough to
> check the local condition at a compatible pair of affine opens `A ⊆ U`, `B ⊆ V`; their images in
> `X` and `S` are a compatible pair of affine opens there, the same lemma supplies the condition at
> that pair, and the two canonical isomorphisms `A ≅ ι_U(A)` and `B ≅ ι_V(B)` are absorbed by
> `AlgebraicGeometry.exists_isPseudoCoherentFromAfterPushforward_openSource` and
> `AlgebraicGeometry.exists_isPseudoCoherentFromAfterPushforward_shrinkBase`.

```lean
public theorem IsPseudoCoherentFrom.resLE [LocallyOfFiniteType f]
    (E : DerivedCategory X.Modules) (m : ℤ) (U : X.Opens) (V : S.Opens) (hUV : U ≤ f ⁻¹ᵁ V)
    (hE : IsPseudoCoherentFrom f E m) :
    IsPseudoCoherentFrom (f.resLE V U hUV)
      ((Scheme.Modules.restrictFunctor U.ι).mapDerivedCategory.obj E) m
```

## Tag 09VF, a lemma

[Tag 09VF](https://stacks.math.columbia.edu/tag/09VF) in the Stacks Project.

**`AlgebraicGeometry.derivedSectionsPseudoCoherentComparison'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/AffineSectionsComparison.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/AffineSectionsComparison.lean#L439).

> **Stacks 09VF.** Let `f : X ⟶ S` be locally of finite type, let `E` be an object of the derived
> category of `𝒪_X`-modules all of whose cohomology sheaves are quasi-coherent, and let `m` be an
> integer. Then the following are equivalent:
>
> 1. `E` is `m`-pseudo-coherent relative to `S`;
> 2. there are affine open coverings `S = ⋃ Vⱼ` and `f ⁻¹ᵁ Vⱼ = ⋃ Uⱼᵢ` such that each complex
>    `RΓ(Uⱼᵢ, E)` is `m`-pseudo-coherent relative to `Γ(S, Vⱼ)`;
> 3. for every affine open `V ⊆ S` and every affine open `U ⊆ f ⁻¹ᵁ V`, the complex `RΓ(U, E)` is
>    `m`-pseudo-coherent relative to `Γ(S, V)`.
>
> This is `AlgebraicGeometry.derivedSectionsPseudoCoherentComparison'_of_derivedSectionsSpec` with
> its hypothesis discharged by
> `AlgebraicGeometry.IsAffineOpen.nonempty_iso_derivedSectionsSpec`.

```lean
public theorem derivedSectionsPseudoCoherentComparison' (f : X ⟶ S) [LocallyOfFiniteType f]
    (E : DerivedCategory X.Modules)
    (hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj E).IsQuasicoherent) (m : ℤ) :
    DerivedSectionsPseudoCoherentComparison' f E hE m
```

## Tag 09VG, a lemma

[Tag 09VG](https://stacks.math.columbia.edu/tag/09VG) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_derivedPushforward_of_reductionImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/ReductionClosedPushforward.lean, line 953](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/ReductionClosedPushforward.lean#L953). The attribute's comment: “corrected statement — Stacks erratum. The source's topological hypothesis, that i induce a homeomorphism of X with a closed subset of Y, makes the lemma false (AlgebraicGeometry.Scheme.Hom.not\_forall\_isPseudoCoherentFrom\_iff\_derivedPushforward, over the nodal curve A = \{h ∈ k[s] | h(0) = h(1)} with B = k[s, 1/s]); it is replaced here by the hypothesis the source's proof actually uses, that i be a closed immersion on reductions, i.e. that A/rad(A) → B/rad(B) be surjective. Both directions, E and m arbitrary”.

> Let `f : X ⟶ S` and `g : Y ⟶ S` be morphisms of schemes locally of finite type and let
> `i : X ⟶ Y` be a morphism over `S` which induces a closed immersion on reductions: there is a
> closed immersion `j` of the reduction of `X` into the reduction of `Y` making the square with the
> canonical immersions of the reductions commute. Let `E` be an object of `D(𝒪_X)` and `m` an
> integer. Then `E` is `m`-pseudo-coherent relative to `S` if and only if `Ri_*E` is
> `m`-pseudo-coherent relative to `S`.
>
> With the hypothesis on `i` weakened to a homeomorphism of `X` with a closed subset of `Y` the
> equivalence fails, by
> `AlgebraicGeometry.Scheme.Hom.not_forall_isPseudoCoherentFrom_iff_derivedPushforward`.

```lean
public theorem Scheme.Hom.isPseudoCoherentFrom_iff_derivedPushforward_of_reductionImmersion
    {X Y S : Scheme.{u}}
    (f : X ⟶ S) (g : Y ⟶ S) [LocallyOfFiniteType f] [LocallyOfFiniteType g] (i : X ⟶ Y)
    (hi : i ≫ g = f)
    (hred : ∃ j : X.nilradical.subscheme ⟶ Y.nilradical.subscheme,
      IsClosedImmersion j ∧
        j ≫ Y.nilradical.subschemeι = X.nilradical.subschemeι ≫ i)
    (E : DerivedCategory X.Modules) (m : ℤ) :
    Scheme.Hom.IsPseudoCoherentFrom f E m ↔
      Scheme.Hom.IsPseudoCoherentFrom g
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward
          i.toLRSHom.toShHom).obj E) m
```

## Tag 09UK, a lemma

[Tag 09UK](https://stacks.math.columbia.edu/tag/09UK) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFinitePushforward.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFinitePushforward.lean#L237). References: SGA 6 III (2.1), “finite morphism, QCoh”; SGA 6 III (2.2), “special case”; SGA 6 IV (3.3.2), “3.3.2.3”.

> **Stacks 09UK.** Let `π : X ⟶ Y` be a finite morphism of schemes locally of finite type over
> a base `S`, and let `E` be an object of the derived category of `𝒪_X`-modules with quasi-coherent
> cohomology. Then `E` is `m`-pseudo-coherent relative to `S` if and only if `Rπ_* E` is.
>
> The proof is the translation the source asks for. In one direction Stacks 09VF, which is
> `AlgebraicGeometry.derivedSectionsPseudoCoherentComparison'`, turns relative `m`-pseudo-coherence
> of `E` into its per-pair condition at *every* compatible pair of affine opens, and
> `AlgebraicGeometry.derivedSectionsPseudoCoherentOn'_preimage_iff` carries the condition at
> `(π ⁻¹ᵁ U, V)` to the condition at `(U, V)` for `Rπ_* E`, at every pair of the target. In the
> other direction the covers the source provides for `Rπ_* E` cannot be used directly — an affine
> open of `X` need not be an inverse image — so the "exists an affine cover" form of Stacks 09VF is
> used instead and its covers are pulled back along `π`, which is where the morphism being over `S`
> enters. That `Rπ_* E` again has quasi-coherent cohomology, so that Stacks 09VF applies to it, is
> clause (1) of Stacks 08D5 by way of
> `AlgebraicGeometry.preservesQuasicoherentOnAffineTarget`.

```lean
public theorem Scheme.Hom.isPseudoCoherentFrom_iff_derivedPushforward
    {X Y S : Scheme.{u}} (π : X ⟶ Y) (f : X ⟶ S) (g : Y ⟶ S)
    (hπ : π ≫ g = f) [IsFinite π] [LocallyOfFiniteType f] [LocallyOfFiniteType g]
    (E : DerivedCategory X.Modules)
    (hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj E).IsQuasicoherent)
    (m : ℤ) :
    Scheme.Hom.IsPseudoCoherentFrom f E m ↔
      Scheme.Hom.IsPseudoCoherentFrom g
        ((RingedSpace.derivedPushforward π.toLRSHom.toShHom).obj E) m
```

## Tag 09UL, a lemma

[Tag 09UL](https://stacks.math.columbia.edu/tag/09UL) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_obj₃_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeTriangle.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeTriangle.lean#L96). The attribute's comment: “part (1)”. References: SGA 6 I (2.6), “row 1 (n+1, n, n)”; SGA 6 III (1.4), “1st line (G underlined)”.

> **Stacks 09UL, part (1).** If the first term of a distinguished triangle of `D(𝒪_X)` is
> `(m + 1)`-pseudo-coherent relative to `S` and the second is `m`-pseudo-coherent relative to `S`,
> then the third is `m`-pseudo-coherent relative to `S`.

```lean
public theorem isPseudoCoherentFrom_obj₃_of_distinguished [LocallyOfFiniteType f] (m : ℤ)
    (T : Triangle (DerivedCategory X.Modules)) (hT : T ∈ distinguishedTriangles)
    (hE : IsPseudoCoherentFrom f T.obj₁ (m + 1)) (hE' : IsPseudoCoherentFrom f T.obj₂ m) :
    IsPseudoCoherentFrom f T.obj₃ m
```

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_obj₂_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeTriangle.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeTriangle.lean#L119). The attribute's comment: “part (2)”. References: SGA 6 I (2.6), “row 2 (n, n, n)”; SGA 6 III (1.4), “2nd line (F underlined)”.

> **Stacks 09UL, part (2).** If the first and third terms of a distinguished triangle of
> `D(𝒪_X)` are `m`-pseudo-coherent relative to `S`, then so is the second.

```lean
public theorem isPseudoCoherentFrom_obj₂_of_distinguished [LocallyOfFiniteType f] (m : ℤ)
    (T : Triangle (DerivedCategory X.Modules)) (hT : T ∈ distinguishedTriangles)
    (hE : IsPseudoCoherentFrom f T.obj₁ m) (hE'' : IsPseudoCoherentFrom f T.obj₃ m) :
    IsPseudoCoherentFrom f T.obj₂ m
```

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_obj₁_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeTriangle.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeTriangle.lean#L144). The attribute's comment: “part (3)”. References: SGA 6 I (2.6), “row 3 (n, n, n-1)”; SGA 6 III (1.4), “3rd line (E underlined)”.

> **Stacks 09UL, part (3).** If the second term of a distinguished triangle of `D(𝒪_X)` is
> `(m + 1)`-pseudo-coherent relative to `S` and the third is `m`-pseudo-coherent relative to `S`,
> then the first is `(m + 1)`-pseudo-coherent relative to `S`.

```lean
public theorem isPseudoCoherentFrom_obj₁_of_distinguished [LocallyOfFiniteType f] (m : ℤ)
    (T : Triangle (DerivedCategory X.Modules)) (hT : T ∈ distinguishedTriangles)
    (hE' : IsPseudoCoherentFrom f T.obj₂ (m + 1)) (hE'' : IsPseudoCoherentFrom f T.obj₃ m) :
    IsPseudoCoherentFrom f T.obj₁ (m + 1)
```

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherent_obj₃_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeTriangle.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeTriangle.lean#L166). The attribute's comment: “moreover, third term”.

> **Stacks 09UL, the "moreover" clause for the third term.** If the first two terms of a
> distinguished triangle of `D(𝒪_X)` are pseudo-coherent relative to `S`, so is the third.

```lean
public theorem isPseudoCoherent_obj₃_of_distinguished [LocallyOfFiniteType f]
    (T : Triangle (DerivedCategory X.Modules)) (hT : T ∈ distinguishedTriangles)
    (hE : IsPseudoCoherent f T.obj₁) (hE' : IsPseudoCoherent f T.obj₂) :
    IsPseudoCoherent f T.obj₃
```

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherent_obj₂_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeTriangle.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeTriangle.lean#L175). The attribute's comment: “moreover, second term”.

> **Stacks 09UL, the "moreover" clause for the second term.** If the first and third terms of a
> distinguished triangle of `D(𝒪_X)` are pseudo-coherent relative to `S`, so is the second.

```lean
public theorem isPseudoCoherent_obj₂_of_distinguished [LocallyOfFiniteType f]
    (T : Triangle (DerivedCategory X.Modules)) (hT : T ∈ distinguishedTriangles)
    (hE : IsPseudoCoherent f T.obj₁) (hE'' : IsPseudoCoherent f T.obj₃) :
    IsPseudoCoherent f T.obj₂
```

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherent_obj₁_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeTriangle.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeTriangle.lean#L184). The attribute's comment: “moreover, first term”.

> **Stacks 09UL, the "moreover" clause for the first term.** If the last two terms of a
> distinguished triangle of `D(𝒪_X)` are pseudo-coherent relative to `S`, so is the first.

```lean
public theorem isPseudoCoherent_obj₁_of_distinguished [LocallyOfFiniteType f]
    (T : Triangle (DerivedCategory X.Modules)) (hT : T ∈ distinguishedTriangles)
    (hE' : IsPseudoCoherent f T.obj₂) (hE'' : IsPseudoCoherent f T.obj₃) :
    IsPseudoCoherent f T.obj₁
```

## Tag 09UM, a lemma

[Tag 09UM](https://stacks.math.columbia.edu/tag/09UM) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isModulePseudoCoherentFrom_neg_one_iff_isFinitelyPresentedRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFinitePresentationDegree.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFinitePresentationDegree.lean#L152). The attribute's comment: “degree\_minus\_one”. References: SGA 6 III (1.2.1).

> **Stacks 09UM, the degree-minus-one clause.** For a morphism of schemes locally of finite
> type, a sheaf of `𝒪_X`-modules is `(-1)`-pseudo-coherent relative to the base if and only if it
> is quasi-coherent and finitely presented relative to the base.
>
> Stacks 09UJ turns relative `(-1)`-pseudo-coherence into the local condition of Stacks 09UI at
> every compatible pair of affine opens `U ⊆ f ⁻¹ᵁ V`, where by Stacks 09V9(2) it says that the
> direct image of `ℱ|_U` along a closed immersion `i : U ⟶ 𝔸ⁿ_V` over `V` is of finite
> presentation. Finite presentation of `i_*(ℱ|_U)` gives quasi-coherence of `ℱ|_U`, and
> quasi-coherence is local on `X`; it also gives relative finite presentation of `ℱ|_U` over `V`
> by Stacks 09T8 and 09T9, which is the affine-pair criterion of Stacks 09T7. Conversely Stacks
> 09T7 restricts relative finite presentation to the pair, and Stacks 09T9 and 09T8 turn it back
> into finite presentation of `i_*(ℱ|_U)` at a closed immersion of our own choosing.

```lean
public theorem isModulePseudoCoherentFrom_neg_one_iff_isFinitelyPresentedRelative
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] (F : X.Modules) :
    IsModulePseudoCoherentFrom f F (-1) ↔
      (F.IsQuasicoherent ∧ IsFinitelyPresentedRelative f F)
```

**`AlgebraicGeometry.Scheme.Hom.isModulePseudoCoherentFrom_zero_iff_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeModuleDegrees.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeModuleDegrees.lean#L65). The attribute's comment: “degree\_zero”.

> **Stacks 09UM, the degree-zero clause.** For a morphism of schemes locally of finite type, a
> sheaf of `𝒪_X`-modules is `0`-pseudo-coherent relative to the base if and only if it is of finite
> type.
>
> Stacks 09UJ turns relative `0`-pseudo-coherence into the local condition of Stacks 09UI at every
> compatible pair of affine opens, where it is finiteness of type of the restriction of `ℱ` to the
> source open; finiteness of type is inherited by restriction and is local on `X`, which gives the
> two implications.

```lean
public theorem isModulePseudoCoherentFrom_zero_iff_isFiniteType {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F : X.Modules) :
    IsModulePseudoCoherentFrom f F 0 ↔ F.IsFiniteType
```

**`AlgebraicGeometry.Scheme.Hom.isModulePseudoCoherentFrom_of_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/TrivialRange.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/TrivialRange.lean#L168). The attribute's comment: “positive\_degrees”.

> **Stacks 09UM, the positive degrees.** For a morphism of schemes locally of finite type,
> every sheaf of `𝒪_X`-modules is relatively `m`-pseudo-coherent whenever `0 < m`.
>
> The affine open covering of the base is the family of all affine opens, and over each member the
> covering of its inverse image is the family of all affine opens of `X` contained in it; the
> closed immersions into affine space are the ones produced by
> `AlgebraicGeometry.exists_isClosedImmersion_affineSpace_resLE`, and the local condition at each
> of them holds because the restriction of a sheaf of modules is still concentrated in degree
> zero.

```lean
public theorem isModulePseudoCoherentFrom_of_pos {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F : X.Modules) {m : ℤ} (hm : 0 < m) :
    IsModulePseudoCoherentFrom f F m
```

## Tag 09UN, a lemma

[Tag 09UN](https://stacks.math.columbia.edu/tag/09UN) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.IsPseudoCoherentFrom.of_biprod_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeSummand.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeSummand.lean#L107). The attribute's comment: “first summand”.

> **Stacks 09UN, first summand.** If `E ⊕ K` is `m`-pseudo-coherent relative to `S` then so is
> `E`.

```lean
public theorem IsPseudoCoherentFrom.of_biprod_left {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (E K : DerivedCategory X.Modules) (m : ℤ)
    (h : IsPseudoCoherentFrom f (E ⊞ K) m) : IsPseudoCoherentFrom f E m
```

**`AlgebraicGeometry.Scheme.Hom.IsPseudoCoherentFrom.of_biprod_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeSummand.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeSummand.lean#L115). The attribute's comment: “second summand”.

> **Stacks 09UN, second summand.** If `E ⊕ K` is `m`-pseudo-coherent relative to `S` then so is
> `K`.

```lean
public theorem IsPseudoCoherentFrom.of_biprod_right {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (E K : DerivedCategory X.Modules) (m : ℤ)
    (h : IsPseudoCoherentFrom f (E ⊞ K) m) : IsPseudoCoherentFrom f K m
```

## Tag 09UP, a lemma

[Tag 09UP](https://stacks.math.columbia.edu/tag/09UP) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_Q_of_locally_boundedAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeBoundedComplex.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeBoundedComplex.lean#L144).

> **Stacks 09UP.** Let `f : X ⟶ S` be a morphism of schemes locally of finite type, let `m` be
> an integer and let `𝓕` be a complex of `𝒪_X`-modules which is bounded above on a neighbourhood of
> every point. If `𝓕ⁱ` is `(m - i)`-pseudo-coherent relative to `S` for every `i`, then `𝓕` is
> `m`-pseudo-coherent relative to `S`.
>
> By Stacks 09UJ it is enough to check the local condition of Stacks 09UI at a compatible pair of
> affine opens `U ⊆ f ⁻¹ᵁ V`, and by Stacks 09VC it may be checked at any one closed immersion
> `i : U ⟶ 𝔸ⁿ_V` over `V`. There it says that the complex `i_*(𝓕|_U)` on `𝔸ⁿ_V` represents an
> `m`-pseudo-coherent object, which is the globally bounded above case of Stacks 09V7: the terms
> are `m`-pseudo-coherent in their degrees because each `𝓕ⁱ` is relatively `(m - i)`-pseudo-coherent
> at the same pair and the same closed immersion, and the complex is bounded above on all of the
> quasi-compact `U`.

```lean
public theorem isPseudoCoherentFrom_Q_of_locally_boundedAbove [LocallyOfFiniteType f] (m : ℤ)
    (F : CochainComplex X.Modules ℤ)
    (hbdd : ∀ x : X, ∃ U : X.Opens, x ∈ U ∧ ∃ b : ℤ, ∀ i : ℤ, b < i →
      IsZero ((Scheme.Modules.restrictFunctor U.ι).obj (F.X i)))
    (hterms : ∀ i : ℤ, IsModulePseudoCoherentFrom f (F.X i) (m - i)) :
    IsPseudoCoherentFrom f (DerivedCategory.Q.obj F) m
```

## Tag 09UQ, a lemma

[Tag 09UQ](https://stacks.math.columbia.edu/tag/09UQ) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_of_homology_of_locally_boundedAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeBoundedAboveCohomology.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeBoundedAboveCohomology.lean#L55).

> Let `f : X ⟶ S` be a morphism of schemes locally of finite type, let `m` be an integer and let
> `E` be an object of `D(𝒪_X)` whose cohomology sheaves vanish in high degrees on a neighbourhood of
> every point. If `H^i(E)` is `(m - i)`-pseudo-coherent relative to `S` for every `i`, then `E` is
> `m`-pseudo-coherent relative to `S`.

```lean
public theorem isPseudoCoherentFrom_of_homology_of_locally_boundedAbove [LocallyOfFiniteType f]
    (m : ℤ) (E : DerivedCategory X.Modules)
    (hbdd : ∀ x : X, ∃ U : X.Opens, x ∈ U ∧ ∃ b : ℤ, ∀ i : ℤ, b < i →
      IsZero ((Scheme.Modules.restrictFunctor U.ι).obj
        ((DerivedCategory.homologyFunctor X.Modules i).obj E)))
    (hcoh : ∀ i : ℤ, IsModulePseudoCoherentFrom f
      ((DerivedCategory.homologyFunctor X.Modules i).obj E) (m - i)) :
    IsPseudoCoherentFrom f E m
```

## Tag 09UR, a lemma

[Tag 09UR](https://stacks.math.columbia.edu/tag/09UR) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_derivedPullback_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/ChartTorIndependence.lean, line 462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/ChartTorIndependence.lean#L462). References: SGA 6 III (1.10); SGA 6 III (1.8), “special case”.

> **Stacks 09UR.** Let `f : X ⟶ S` be locally of finite type, let `E` be an object of `D(𝒪_X)`
> which is `m`-pseudo-coherent relative to `S`, and let `g : S' ⟶ S` be a morphism of schemes. If
> `S'` and `X` are Tor independent over `S`, then the derived pullback of `E` to `X ×_S S'` is
> `m`-pseudo-coherent relative to `S'`.
>
> This is `AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_derivedPullback_of_torIndependentCharts`
> with its chart hypothesis discharged by
> `AlgebraicGeometry.Scheme.Hom.chartTorIndependence_of_torIndependent`, so the Tor independence
> assumed here is the one the source assumes.
>
> No hypothesis beyond the source's is assumed. Stacks 0E23, the base change isomorphism stated
> as `AlgebraicGeometry.DerivedBaseChangeIsoOfTorIndependent`, is proved —
> `AlgebraicGeometry.derivedBaseChangeIsoOfTorIndependent`, from
> `Stacks.Cohomology.ClosedImmersionBaseChange.isIso_derivedBaseChangeMap_of_torIndependent` — so
> it is not needed as a hypothesis here. The tag for Stacks 09UR sits here rather than on
> `AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_derivedPullback_of_torIndependentCharts`,
> because the source's hypothesis is Tor independence of `X` and `S'` over `S`, which is what this
> statement assumes; the chart form that one assumes is strictly stronger-looking and is derived
> here by `AlgebraicGeometry.Scheme.Hom.chartTorIndependence_of_torIndependent`.

```lean
public theorem Scheme.Hom.isPseudoCoherentFrom_derivedPullback_of_torIndependent
    {X S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) [LocallyOfFiniteType f]
    (E : DerivedCategory X.Modules) (m : ℤ)
    (htor : TorIndependent f g) (hE : f.IsPseudoCoherentFrom E m) :
    (pullback.snd f g).IsPseudoCoherentFrom
      ((derivedPullback (pullback.fst f g).toLRSHom.toShHom).obj E) m
```

## Tag 09US, a lemma

[Tag 09US](https://stacks.math.columbia.edu/tag/09US) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_comp_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/DerivedPullback09US.lean, line 1205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/DerivedPullback09US.lean#L1205).

> **Stacks 09US.** Let `f : X ⟶ Y` be a pseudo-coherent morphism of schemes, let `g : Y ⟶ S` be
> locally of finite type and let `E` be an object of `D(𝒪_Y)` which is `m`-pseudo-coherent relative
> to `S`. Then the derived pullback `Lf^*E` is `m`-pseudo-coherent relative to `S`.
>
> The hypothesis on `f` is `AlgebraicGeometry.PseudoCoherent`, which by Stacks 067Y is the
> conjunction of the two hypotheses of the source: `f` is locally of finite type and `𝒪_X` is
> pseudo-coherent relative to `Y`.
>
> No hypothesis beyond those of the source is needed. The appeal the source makes to Stacks 0E23,
> through Stacks 09UR, is at a square whose horizontal morphism is flat — it is
> `AlgebraicGeometry.AffineSpace.map` of a restriction of the flat projection `𝔸ᵈ_W ⟶ W` — and that
> case of 0E23 is `AlgebraicGeometry.nonempty_derivedPullbackPushforwardIso`, proved in this file.

```lean
public theorem Scheme.Hom.isPseudoCoherentFrom_comp_derivedPullback {X Y S : Scheme.{u}} (f : X ⟶ Y)
    (g : Y ⟶ S) [PseudoCoherent f] [LocallyOfFiniteType g] (E : DerivedCategory Y.Modules)
    (m : ℤ) (hE : g.IsPseudoCoherentFrom E m) :
    (f ≫ g).IsPseudoCoherentFrom ((derivedPullback f.toLRSHom.toShHom).obj E) m
```

## Tag 09UT, a lemma

[Tag 09UT](https://stacks.math.columbia.edu/tag/09UT) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeComp09UT.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeComp09UT.lean#L269). The attribute's comment: “the equivalence, with pseudo-coherence of g as a class”. References: SGA 6 III (1.12); SGA 6 I (2.14), “(ii)”; SGA 6 III (1.11), “b), g pseudo-coherent”.

> **Stacks 09UT.** Let `f : X ⟶ Y` be locally of finite type, let `g : Y ⟶ S` be
> pseudo-coherent, let `E` be an object of `D(𝒪_X)` and let `m` be an integer. Then `E` is
> `m`-pseudo-coherent relative to `Y` if and only if it is `m`-pseudo-coherent relative to `S`.
>
> The two implications are
> `AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_comp` and
> `AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_of_comp`.

```lean
public theorem isPseudoCoherentFrom_iff_comp (E : DerivedCategory X.Modules) (m : ℤ) :
    f.IsPseudoCoherentFrom E m ↔ (f ≫ g).IsPseudoCoherentFrom E m
```

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_comp_of_isModulePseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeComp09UT.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeComp09UT.lean#L286). The attribute's comment: “the equivalence, with the hypothesis in the shape of condition (3) of 067Y”. References: SGA 6 III (1.12); SGA 6 I (2.14), “(ii)”; SGA 6 III (1.11), “b), g pseudo-coherent”.

> **Stacks 09UT with pseudo-coherence of `g` in the shape of condition (3) of Stacks 067Y.**
> Let `f : X ⟶ Y` be locally of finite type and let `g : Y ⟶ S` be locally of finite type with
> `𝒪_Y` pseudo-coherent relative to `S`. Then an object `E` of `D(𝒪_X)` is `m`-pseudo-coherent
> relative to `Y` if and only if it is `m`-pseudo-coherent relative to `S`.
>
> The hypothesis is condition (3) of Stacks 067Y rather than
> `AlgebraicGeometry.PseudoCoherent`; the two are interchangeable by the unconditional
> `AlgebraicGeometry.pseudoCoherent_iff_isModulePseudoCoherent`, so this is
> `AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_comp`.

```lean
public theorem isPseudoCoherentFrom_iff_comp_of_isModulePseudoCoherent {X Y S : Scheme.{u}}
    (f : X ⟶ Y) (g : Y ⟶ S) [LocallyOfFiniteType f]
    (hg : ∃ hft : LocallyOfFiniteType g,
      letI := hft
      Scheme.Hom.IsModulePseudoCoherent g (SheafOfModules.unit Y.ringCatSheaf))
    (E : DerivedCategory X.Modules) (m : ℤ) :
    letI : LocallyOfFiniteType g := hg.choose
    letI : LocallyOfFiniteType (f ≫ g) := locallyOfFiniteType_comp f g
    f.IsPseudoCoherentFrom E m ↔ (f ≫ g).IsPseudoCoherentFrom E m
```

## Tag 09UU, a lemma

[Tag 09UU](https://stacks.math.columbia.edu/tag/09UU) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_derivedPushforwardRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/DerivedRelative09UU.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/DerivedRelative09UU.lean#L294). The attribute's comment: “the equivalence of clauses (1) and (2), at a closed immersion”. References: SGA 6 III (2.1), “special case”.

> **Stacks 09UU, the equivalence of clauses (1) and (2).** Let `i : X ⟶ P` be a closed immersion
> of schemes and let `p : P ⟶ S` be locally of finite type. For an object `E` of `D(𝒪_X)` and an
> integer `m`, `E` is relatively `m`-pseudo-coherent for `i ≫ p` if and only if the unbounded
> derived pushforward `Ri_*E` is relatively `m`-pseudo-coherent for `p`.
>
> This is
> `AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_pushforwardMapDerivedCategory` transported
> along `Stacks.ClosedImmersion.derivedPushforwardIsoMapDerivedCategoryOfSchemes`, which identifies
> the chosen total right derived functor
>   `Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward` with the functor the
> exact `i_*` induces on derived categories; relative `m`-pseudo-coherence depends only on the
> isomorphism class of its argument.

```lean
public theorem Scheme.Hom.isPseudoCoherentFrom_iff_derivedPushforwardRelative {X P S : Scheme.{u}}
    (i : X ⟶ P) (p : P ⟶ S) [IsClosedImmersion i] [LocallyOfFiniteType p]
    (E : DerivedCategory X.Modules) (m : ℤ) :
    (i ≫ p).IsPseudoCoherentFrom E m ↔
      p.IsPseudoCoherentFrom
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward
          i.toLRSHom.toShHom).obj E) m
```

**`AlgebraicGeometry.Scheme.Hom.derivedPushforwardRelative_iff_pseudoCoherentFrom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeAbsolute.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeAbsolute.lean#L213). The attribute's comment: “the equivalence of clauses (2) and (3)”.

> **Stacks 09UU, the equivalence of clauses (2) and (3).** Let `i : X ⟶ P` be a morphism of
> schemes and let `p : P ⟶ S` be flat and locally of finite presentation. For an object `E` of
> `D(𝒪_X)` and an integer `m`, the unbounded derived pushforward `Ri_*E` is relatively
> `m`-pseudo-coherent for `p` if and only if it is `m`-pseudo-coherent on `P`.
>
> This is `AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_of_pseudoCoherent` at the object
> `Ri_*E`, together with
> `AlgebraicGeometry.pseudoCoherent_of_flat_of_locallyOfFinitePresentation`. Nothing about `Ri_*E`
> beyond its being an object of `D(𝒪_P)` is used, and in particular no hypothesis on `i` is
> needed.

```lean
public theorem derivedPushforwardRelative_iff_pseudoCoherentFrom {X P S : Scheme.{u}} (i : X ⟶ P)
    (p : P ⟶ S) [Flat p] [LocallyOfFinitePresentation p] (E : DerivedCategory X.Modules)
    (m : ℤ) :
    p.IsPseudoCoherentFrom
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward
          i.toLRSHom.toShHom).obj E) m ↔
      RingedSpace.IsPseudoCoherentFrom (X := P.toRingedSpace)
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward
          i.toLRSHom.toShHom).obj E) m
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.59, Tag 09UH](https://stacks.math.columbia.edu/tag/09UH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
