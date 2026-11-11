---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.existsUnique_tensorExtension_coherent, AlgebraicGeometry.Stack.exists_ringHom_tensorFunctor_comp_quasicoherentPushforward, AlgebraicGeometry.Stack.universallyInjective_affineTensorAlgebra, Algebra.faithfullyFlat_of_flat_selfTensor_of_universallyInjective, AlgebraicGeometry.Stack.AlgebraicStacks.isIso_tensorPushforwardMap, AlgebraicGeometry.Stack.AlgebraicStacks.nonempty_iso_tensorPushforward, AlgebraicGeometry.Stack.AlgebraicStacks.not_forall_nonempty_tensorPushforwardUnits_iso, AlgebraicGeometry.Stack.quasicoherentTensorPushforwardMap
statement: formalized
proof: formalized
---

# 106.16 Tensor functors

Section 106.16 of the Stacks Project, [Tag 0GRI](https://stacks.math.columbia.edu/tag/0GRI). 8 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GRJ, a lemma

[Tag 0GRJ](https://stacks.math.columbia.edu/tag/0GRJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.existsUnique_tensorExtension_coherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/TensorFunctorExtensionNoetherian.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/TensorFunctorExtensionNoetherian.lean#L57).

> **Stacks 0GRJ.** Let `𝒳` and `𝒴` be Noetherian algebraic stacks.  Any right exact tensor
> functor `F' : Coh(𝒪_𝒳) ⟶ Coh(𝒪_𝒴)` — additive, preserving finite colimits, and a functor of
> monoidal categories (Stacks 0FFL) — extends to a right exact tensor functor
> `F : QCoh(𝒪_𝒳) ⟶ QCoh(𝒪_𝒴)` commuting with all (small) colimits, in particular with direct
> sums: there is an identification `e` of the restriction of `F` to `Coh(𝒪_𝒳)` with `F'`
> (followed by the inclusion of `Coh(𝒪_𝒴)`), compatible with the tensor structures.  The extension
> is unique up to unique isomorphism: for any other functor `G` commuting with filtered colimits and
> identification `e'`, there is a unique isomorphism `F ≅ G` restricting to `e' ⁻¹ ∘ e` on coherent
> modules, and it is compatible with any tensor structure on `G` for which `e'` is.
>
> The input "every quasi-coherent module is a filtered colimit of coherent ones" is Stacks 0GRF
> (`AlgebraicGeometry.Stack.AlgebraicStacks.isFiltered_coherentSubobject_and_isColimit`), in the form
> `AlgebraicGeometry.Stack.ind_coherentQuasicoherent`.

```lean
theorem existsUnique_tensorExtension_coherent
    (𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS) (h𝒳 : IsNoetherianStack.{u, w, w'} B S hS 𝒳)
    (h𝒴 : IsNoetherianStack.{u, w, w'} B S hS 𝒴) :
    haveI := coherentQuasicoherent_isMonoidal B S hS 𝒳 h𝒳.2.2
    haveI := coherentQuasicoherent_isMonoidal B S hS 𝒴 h𝒴.2.2
    ∀ (F' : (coherentQuasicoherent B S hS 𝒳).FullSubcategory ⥤
        (coherentQuasicoherent B S hS 𝒴).FullSubcategory) [F'.Additive]
      [PreservesFiniteColimits F'] (hF' : F'.TensorStructure),
      ∃ (F : FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p
          𝒳.val.isFiberedInGroupoids ⥤
          FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒴.val.val.p
            𝒴.val.isFiberedInGroupoids)
        (e : (coherentQuasicoherent B S hS 𝒳).ι ⋙ F ≅ F' ⋙ (coherentQuasicoherent B S hS 𝒴).ι)
        (hF : F.TensorStructure),
        (F.Additive ∧ PreservesFiniteColimits F ∧ PreservesColimitsOfSize.{u, u} F ∧
          (hF.restrict (coherentQuasicoherent B S hS 𝒳)).IsCompatible
            (hF'.compι (coherentQuasicoherent B S hS 𝒴)) e) ∧
        ∀ (G : FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p
            𝒳.val.isFiberedInGroupoids ⥤
            FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒴.val.val.p
              𝒴.val.isFiberedInGroupoids),
          PreservesFilteredColimitsOfSize.{u, u} G →
            ∀ (e' : (coherentQuasicoherent B S hS 𝒳).ι ⋙ G ≅
                F' ⋙ (coherentQuasicoherent B S hS 𝒴).ι),
              ∃! φ : F ≅ G, Functor.whiskerLeft (coherentQuasicoherent B S hS 𝒳).ι φ.hom =
                  (e ≪≫ e'.symm).hom ∧
                ∀ hG : G.TensorStructure,
                  (hG.restrict (coherentQuasicoherent B S hS 𝒳)).IsCompatible
                    (hF'.compι (coherentQuasicoherent B S hS 𝒴)) e' →
                    hF.IsCompatible hG φ
```

## Tag 0GRK, a lemma

[Tag 0GRK](https://stacks.math.columbia.edu/tag/0GRK) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_ringHom_tensorFunctor_comp_quasicoherentPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/TensorFunctors/TensorFunctorAffineDiagonal.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/TensorFunctors/TensorFunctorAffineDiagonal.lean#L146).

> **Stacks 0GRK.**  Let `𝒳` be an algebraic stack with affine diagonal, `R` a ring and
> `F : QCoh(𝒪_𝒳) ⥤ Mod_R` a right exact tensor functor (additive, preserving finite colimits, lax
> symmetric monoidal) which commutes with direct sums.  Let `g : U ⟶ 𝒳` be a morphism with `U` an
> affine scheme, with ring of global functions `A`.  Then `g` is affine, and
>
> 1. `C = F(g_{QCoh,*}𝒪_U)` is a commutative `R`-algebra
>    (`AlgebraicGeometry.Stack.affineTensorAlgebra` with its `CommRing` and `Algebra R`
>    instances), and
> 2. there is a ring map `φ : A → C`
>
> such that `F ∘ g_{QCoh,*}` sends `M` to `M ⊗_A C` seen as an `R`-module: both as a functor
> `Mod_A ⥤ Mod_R` through `M ↦ M~`, and as a functor `QCoh(𝒪_U) ⥤ Mod_R` through
> `N ↦ Γ(U, N)`, which is how `QCoh(𝒪_U)` is `Mod_A`
> (`AlgebraicGeometry.Stack.tildeCounitIso`).
>
> "Affine diagonal" is absolute, as in the source (Morphisms of Stacks, Definition 050D): it is the
> diagonal of the view of `𝒳` over the terminal scheme `Spec ℤ`
> (`AlgebraicGeometry.Stack.AlgebraicStacks.viewOverIntegers`), which lies in every big fppf site
> (`AlgebraicGeometry.Stack.contains_terminalScheme`).  That `g` is affine is
> `AlgebraicGeometry.Stack.AlgebraicStacks.isAffineHom_of_isAffineHom_diagonal_viewOverIntegers`
> (Stacks 0GQE over `Spec ℤ`).

```lean
theorem exists_ringHom_tensorFunctor_comp_quasicoherentPushforward
    (hΔ : Stack.IsAffineHom B (⊤_ Scheme.{u}) (contains_terminalScheme B)
      (diagonal.{u, u, u + 1} B (⊤_ Scheme.{u}) (contains_terminalScheme B)
        (AlgebraicStacks.viewOverIntegers B S hS (contains_terminalScheme B) 𝒳).val))
    (hUaff : IsAffineOver B S hS U) (g : schemeStack.{u, w} B S hS U ⟶ 𝒳) :
    ∃ hg : AlgebraicStacks.IsAffineHom B S hS g,
      ∃ φ : schemeGlobalRing U →+* affineTensorAlgebra g hg F,
        Nonempty (tildeQuasicoherent.{u, w} U ⋙ affineQuasicoherentPushforward g hg ⋙ F ≅
          ModuleCat.extendScalars φ ⋙
            ModuleCat.restrictScalars (algebraMap R (affineTensorAlgebra g hg F))) ∧
        Nonempty (affineQuasicoherentPushforward g hg ⋙ F ≅
          quasicoherentGlobalSections.{u, w} U ⋙ ModuleCat.extendScalars φ ⋙
            ModuleCat.restrictScalars (algebraMap R (affineTensorAlgebra g hg F)))
```

## Tag 0GRL, a lemma

[Tag 0GRL](https://stacks.math.columbia.edu/tag/0GRL) in the Stacks Project.

**`AlgebraicGeometry.Stack.universallyInjective_affineTensorAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/TensorFunctors/AffineTensorAlgebraUniversallyInjective.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/TensorFunctors/AffineTensorAlgebraUniversallyInjective.lean#L60).

> **Stacks 0GRL.**  Let `𝒳` be a Noetherian algebraic stack with affine diagonal, `R` a ring and
> `F : QCoh(𝒪_𝒳) ⥤ Mod_R` a right exact tensor functor (additive, preserving finite colimits,
> symmetric monoidal) which commutes with direct sums.  Let `g : U ⟶ 𝒳` be a flat and surjective
> morphism from an affine scheme `U`.  Then `g` is affine, and the structure map `R ⟶ C` of the
> commutative `R`-algebra `C = F(g_{QCoh,*}𝒪_U)` of Stacks 0GRK
> (`AlgebraicGeometry.Stack.affineTensorAlgebra`) is universally injective.
>
> "Affine diagonal" is absolute, as in Stacks 0GRK: the diagonal of the view of `𝒳` over the
> terminal scheme `Spec ℤ` (`AlgebraicGeometry.Stack.AlgebraicStacks.viewOverIntegers`).  The proof
> is `AlgebraicGeometry.Stack.universallyInjective_affineTensorAlgebra_of_coherentGeneration` with
> Stacks 0GRF (`AlgebraicGeometry.Stack.AlgebraicStacks.isFiltered_coherentSubobject_and_isColimit`,
> in the form `AlgebraicGeometry.Stack.ind_coherentQuasicoherent`) as its input.

```lean
theorem universallyInjective_affineTensorAlgebra
    (hΔ : Stack.IsAffineHom B (⊤_ Scheme.{u}) (contains_terminalScheme B)
      (diagonal.{u, u, u + 1} B (⊤_ Scheme.{u}) (contains_terminalScheme B)
        (AlgebraicStacks.viewOverIntegers B S hS (contains_terminalScheme B) 𝒳).val))
    (h𝒳 : IsNoetherianStack.{u, w, w'} B S hS 𝒳) (hUaff : IsAffineOver B S hS U)
    {R : Type u} [CommRing R]
    (F : AlgebraicStacks.quasicoherentModules B S hS 𝒳 ⥤ ModuleCat.{u} R) [F.Braided]
    [F.Additive] [PreservesFiniteColimits F] [∀ J : Type u, PreservesColimitsOfShape (Discrete J) F]
    (g : schemeStack.{u, w} B S hS U ⟶ 𝒳) (hflat : AlgebraicStacks.IsFlat B S hS g)
    (hsurj : IsSurjective B S hS g) :
    ∃ hg : AlgebraicStacks.IsAffineHom B S hS g,
      Algebra.UniversallyInjective R (affineTensorAlgebra g hg F)
```

## Tag 0GRM, a lemma

[Tag 0GRM](https://stacks.math.columbia.edu/tag/0GRM) in the Stacks Project.

**`Algebra.faithfullyFlat_of_flat_selfTensor_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Exercises/NonExercises/FaithfullyFlatSelfBaseChange.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/NonExercises/FaithfullyFlatSelfBaseChange.lean#L41).

> A universally injective ring map whose two self-base-change coprojections are flat is
> faithfully flat.

```lean
theorem faithfullyFlat_of_flat_selfTensor_of_universallyInjective
    {B : Type u} [CommRing B] {C : Type u} [CommRing C] [Algebra B C]
    (hleft : ((Algebra.TensorProduct.includeLeft : C →ₐ[B] C ⊗[B] C).toRingHom).Flat)
    (_hright : ((Algebra.TensorProduct.includeRight : C →ₐ[B] C ⊗[B] C).toRingHom).Flat)
    (hBC : Algebra.UniversallyInjective B C) :
    (algebraMap B C).FaithfullyFlat
```

## Tag 0GRN, a lemma

[Tag 0GRN](https://stacks.math.columbia.edu/tag/0GRN) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isIso_tensorPushforwardMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/TensorPushforwardAffineLeg.lean, line 1037](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/TensorPushforwardAffineLeg.lean#L1037). The attribute's comment: “corrected (one leg affine): for a : 𝒴 ⟶ 𝒳 affine, quasi-compact, quasi-separated and flat and b : 𝒵 ⟶ 𝒳 representable, quasi-compact and quasi-separated, the canonical map a\_\{QCoh,*}O\_𝒴 ⊗ b\_\{QCoh,*}O\_𝒵 ⟶ f\_\{QCoh,*}O\_\{𝒴 ×\_𝒳 𝒵} is an isomorphism. Added relative to the source: a affine (as printed the tag is false, not\_forall\_nonempty\_tensorPushforwardUnits\_iso: two disjoint punctured planes, where H¹(V,O) ≠ 0 and Γ(V,O) is not flat over the base, so H⁰ of the derived tensor product is not the tensor product). Affineness makes a\_*O be Γ(V,O) with V affine and flat over the base, so the last step is flat base change of H⁰. Dropped: flatness of b (not needed)”. References: SGA 3 VIB (11.1), “more general”.

> **Stacks 0GRN, corrected: one leg affine.** Let `a : 𝒴 ⟶ 𝒳` be an affine (Stacks 0CHQ),
> quasi-compact, quasi-separated and flat 1-morphism of algebraic stacks and `b : 𝒵 ⟶ 𝒳` one which
> is representable (by schemes), quasi-compact and quasi-separated. For the projection
> `f = pr₁ ≫ a : 𝒴 ×_𝒳 𝒵 ⟶ 𝒳` of the canonical 2-fibre product, the canonical map
> `μ : a_{QCoh,*}𝒪_𝒴 ⊗_{𝒪_𝒳} b_{QCoh,*}𝒪_𝒵 ⟶ f_{QCoh,*}𝒪_{𝒴 ×_𝒳 𝒵}`
> (`AlgebraicGeometry.Stack.AlgebraicStacks.tensorPushforwardMap`, `s ⊗ t ↦ pr₁^*s · pr₂^*t`) is an
> isomorphism in `QCoh(𝒪_𝒳)`; here `g_{QCoh,*} = quasicoherentDirectImage g`, `⊗` is the tensor
> product sheaf of Stacks 0GQM and `𝒪 = 𝟙_`.
>
> Relative to the source: `a` is in addition affine. Without it the statement is false
> (`AlgebraicGeometry.Stack.AlgebraicStacks.not_forall_nonempty_tensorPushforwardUnits_iso`: for the
> two disjoint punctured planes `V`, `W` of `Spec k[x,y,z,w]/(xz,xw,yz,yw)` the right hand side is
> `0` and the left hand side has global sections `Γ(V, 𝒪) ⊗ Γ(W, 𝒪) = k`); the source's proof
> breaks at reading off `H⁰` of the derived tensor product, which needs `H¹(V, 𝒪) = 0` and
> flatness of `Γ(V, 𝒪)` over the base. With `a` affine, `a_*𝒪` is computed by `Γ(V, 𝒪)` with `V`
> affine and flat over the base, and the last step is flat base change of `H⁰`. Flatness of `b`,
> and representability of `a` beyond what affineness gives, are not needed and are dropped.

```lean
theorem isIso_tensorPushforwardMap (ha : AlgebraicStacks.IsAffineHom B S hS a)
    (haqc : IsQuasiCompactMorphism B S hS a) (haqs : AlgebraicStacks.IsQuasiSeparated B S hS a)
    (haf : AlgebraicStacks.IsFlat B S hS a)
    (hbr : Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒵.val.val.p 𝒳.val.val.p
      (CatFiberedInGroupoids.homFunctor b.hom))
    (hbqc : IsQuasiCompactMorphism B S hS b) (hbqs : AlgebraicStacks.IsQuasiSeparated B S hS b) :
    IsIso (tensorPushforwardMap a b)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.nonempty_iso_tensorPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/TensorPushforwardAffineLeg.lean, line 1100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/TensorPushforwardAffineLeg.lean#L1100). The attribute's comment: “corrected (one leg affine), the asserted isomorphism a\_\{QCoh,*}O\_𝒴 ⊗ b\_\{QCoh,*}O\_𝒵 ≅ f\_\{QCoh,*}O\_\{𝒴 ×\_𝒳 𝒵}, for a affine, quasi-compact, quasi-separated and flat and b representable, quasi-compact and quasi-separated; see isIso\_tensorPushforwardMap for the added hypothesis (a affine) and why it is needed”.

> **Stacks 0GRN, corrected (one leg affine), the asserted isomorphism**
> `a_{QCoh,*}𝒪_𝒴 ⊗ b_{QCoh,*}𝒪_𝒵 ≅ f_{QCoh,*}𝒪_{𝒴 ×_𝒳 𝒵}`, under the hypotheses of
> `AlgebraicGeometry.Stack.AlgebraicStacks.isIso_tensorPushforwardMap`.

```lean
theorem nonempty_iso_tensorPushforward (ha : AlgebraicStacks.IsAffineHom B S hS a)
    (haqc : IsQuasiCompactMorphism B S hS a) (haqs : AlgebraicStacks.IsQuasiSeparated B S hS a)
    (haf : AlgebraicStacks.IsFlat B S hS a)
    (hbr : Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒵.val.val.p 𝒳.val.val.p
      (CatFiberedInGroupoids.homFunctor b.hom))
    (hbqc : IsQuasiCompactMorphism B S hS b) (hbqs : AlgebraicStacks.IsQuasiSeparated B S hS b) :
    Nonempty ((quasicoherentDirectImage B S hS a).obj (𝟙_ _) ⊗
        (quasicoherentDirectImage B S hS b).obj (𝟙_ _) ≅
      (quasicoherentDirectImage B S hS
        ((twoFibreProductSquareAlgebraicStacks B S hS a b).fst ≫ a)).obj (𝟙_ _))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.not_forall_nonempty_tensorPushforwardUnits_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/TensorPushforwardStackCounterexample.lean, line 604](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/TensorPushforwardStackCounterexample.lean#L604). The attribute's comment: “as printed it is false: a counterexample at X = Spec A, A = k[x,y,z,w]/(xz,xw,yz,yw), with a, b the open immersions of the two punctured planes D(z) ∪ D(w) and D(x) ∪ D(y); the 2-fibre product is empty so f\_\{QCoh,*}O = 0, while a\_\{QCoh,*}O ⊗ b\_\{QCoh,*}O ≠ 0 since Γ(V,O) ⊗\_A Γ(W,O) = k (H¹(V,O) ≠ 0 and Γ(V,O) is not A-flat)”.

> **Stacks 0GRN, as printed, is false.** It is not true that for all 1-morphisms
> `a : 𝒴 ⟶ 𝒳`, `b : 𝒵 ⟶ 𝒳` of algebraic stacks which are representable (by schemes),
> quasi-compact, quasi-separated and flat,
> `a_{QCoh,*}𝒪_𝒴 ⊗_{𝒪_𝒳} b_{QCoh,*}𝒪_𝒵 ≅ f_{QCoh,*}𝒪_{𝒴 ×_𝒳 𝒵}` for the projection
> `f : 𝒴 ×_𝒳 𝒵 ⟶ 𝒳` of the 2-fibre product; not even an abstract isomorphism exists in general.
>
> The counterexample: `X = Spec A`, `A = k[x, y, z, w] / (xz, xw, yz, yw)` the union of two planes
> meeting at the origin, viewed as an algebraic stack over itself, and `a`, `b` the open immersions
> of the punctured planes `V = D(z) ∪ D(w)` and `W = D(x) ∪ D(y)`. They are disjoint, so the right
> hand side is `0`, while on global sections the left hand side is
> `Γ(V, 𝒪) ⊗_A Γ(W, 𝒪) = k[z, w] ⊗_A k[x, y] = k`. Here `quasicoherentDirectImage` is
> `f_{QCoh,*}` of Stacks 077A, `⊗` the tensor product of `QCoh(𝒪_𝒳)` of Stacks 0GQM (the local
> instance `fppfModulesMonoidal`, the tensor product sheaf) and `𝟙_` the structure sheaf. The
> source's proof breaks at its last step: the
> Künneth formula (**Lemma 0FLQ**) computes `Rf_*𝒪 = Ra_*𝒪 ⊗^𝐋 Rb_*𝒪`, and reading off `H⁰` of the
> right hand side as `a_*𝒪 ⊗ b_*𝒪` needs `H¹(V, 𝒪) = 0` or flatness; here `H¹(V, 𝒪) ≠ 0` (a punctured
> plane) and `Γ(V, 𝒪) = A / (x, y)` is not flat over `A`. The same failure occurs with `a = b` the
> open immersion `D(x) ∪ D(z) → Spec k[x, y, z, w] / (xy - zw)`
> (`AlgebraicGeometry.TensorPushforwardCounterexample.not_injective_lmul'_coneSections`). The
> statement holds when one leg is affine
> (`AlgebraicGeometry.Stack.AlgebraicStacks.isIso_tensorPushforwardMap`).

```lean
theorem not_forall_nonempty_tensorPushforwardUnits_iso :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
      (𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS) (a : 𝒴 ⟶ 𝒳) (b : 𝒵 ⟶ 𝒳),
      Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒴.val.val.p 𝒳.val.val.p
        (CatFiberedInGroupoids.homFunctor a.hom) →
      IsQuasiCompactMorphism B S hS a → AlgebraicStacks.IsQuasiSeparated B S hS a →
      AlgebraicStacks.IsFlat B S hS a →
      Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒵.val.val.p 𝒳.val.val.p
        (CatFiberedInGroupoids.homFunctor b.hom) →
      IsQuasiCompactMorphism B S hS b → AlgebraicStacks.IsQuasiSeparated B S hS b →
      AlgebraicStacks.IsFlat B S hS b →
      Nonempty ((quasicoherentDirectImage B S hS a).obj (𝟙_ _) ⊗
          (quasicoherentDirectImage B S hS b).obj (𝟙_ _) ≅
        (quasicoherentDirectImage B S hS
          ((twoFibreProductSquareAlgebraicStacks B S hS a b).fst ≫ a)).obj (𝟙_ _))
```

**`AlgebraicGeometry.Stack.quasicoherentTensorPushforwardMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentTensorPushforward.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentTensorPushforward.lean#L358). The attribute's comment: “THE CANONICAL MAP ONLY, NOT THE ASSERTION. This is μ : a\_\{QCoh,*}𝒪\_𝒴 ⊗ b\_\{QCoh,*}𝒪\_𝒵 ⟶ f\_\{QCoh,*}𝒪\_𝒫, built from the two relative pullback maps of Stacks 06UM and the comparison of Remark 0GQR. Its INVERTIBILITY, which is what the tag asserts, is NOT PROVED here: the étale-local step (the content of Cohomology of Stacks Section 103.12, namely Lemma 0GQH plus the scheme-level Künneth of Lemma 0FLQ) does not compose with the stack-level QCoh monoidal product without further infrastructure. The reduction lemmas below that conclude invertibility from invertibility after a reflecting functor are deliberately left UNTAGGED, being instances of CategoryTheory.isIso\_of\_reflects\_iso rather than content of this tag”.

> **The canonical map `μ`.**  For 1-morphisms `a : 𝒴 ⟶ 𝒳`, `b : 𝒵 ⟶ 𝒳` of
> algebraic stacks and a 2-fibre product square `sq` over the cospan `(a, b)` with apex
> `𝒫 = 𝒴 ×_𝒳 𝒵` and projection `f = sq.fst ≫ a`, the map
>
> `μ : a_{QCoh, *}𝒪_𝒴 ⊗_{𝒪_𝒳} b_{QCoh, *}𝒪_𝒵 ⟶ f_{QCoh, *}𝒪_𝒫`
>
> given by the tensor product of the two relative pullback maps
> `AlgebraicGeometry.Stack.quasicoherentRelativePullbackMap` along the legs `sq.fst` and `sq.snd`,
> followed by the comparison of **Remark 0GQR** attached to the coherator of
> **Lemma 0778** at the relative cup product `cup`.

```lean
def quasicoherentTensorPushforwardMap :
    FibredSite.quasicoherentTensorObj B S hS 𝒳.val.val.p 𝒳.val.property
        ((flatBaseChangeQuasicoherator B E hE S hS 𝒳.val.val.p 𝒳.val.property hincX hclosed
            hpres hls hlsD hwp hsep).obj
          (aStar.obj ((quasicoherentToFlatBaseChange B E hE S hS 𝒴.val.val.p 𝒴.val.property
            hincY).obj (FibredSite.quasicoherentTensorUnit B S hS 𝒴.val.val.p 𝒴.val.property))))
        ((flatBaseChangeQuasicoherator B E hE S hS 𝒳.val.val.p 𝒳.val.property hincX hclosed
            hpres hls hlsD hwp hsep).obj
          (bStar.obj ((quasicoherentToFlatBaseChange B E hE S hS 𝒵.val.val.p 𝒵.val.property
            hincZ).obj (FibredSite.quasicoherentTensorUnit B S hS 𝒵.val.val.p
              𝒵.val.property)))) ⟶
      (flatBaseChangeQuasicoherator B E hE S hS 𝒳.val.val.p 𝒳.val.property hincX hclosed hpres
          hls hlsD hwp hsep).obj
        (fStar.obj ((quasicoherentToFlatBaseChange B E hE S hS sq.pt.val.val.p
          sq.pt.val.property hincP).obj
            (FibredSite.quasicoherentTensorUnit B S hS sq.pt.val.val.p sq.pt.val.property)))
```

**`AlgebraicGeometry.Stack.quasicoherentTensorPushforwardMap_eq_coheratorCupProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentTensorPushforward.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentTensorPushforward.lean#L393). The attribute's comment: “the identification of μ with Q of the relative cup product precomposed with the two relative pullback maps on LQCoh^fbc, i.e. that applying the coherator commutes with tensoring the two maps of Stacks 06UM in”.

> **`μ` is the comparison of Remark 0GQR at a single map out of a tensor product.**  Tensoring
> the two relative pullback maps and then applying the comparison of the coherator is the same as
> applying the comparison to the relative cup product precomposed with those two maps on
> `LQCoh^fbc(𝒪_𝒳)`.

```lean
theorem quasicoherentTensorPushforwardMap_eq_coheratorCupProduct :
    (quasicoherentTensorPushforwardMap B E hE S hS a b sq hincX hincY hincZ hincP hclosed hpres hls
        hlsD hwp hsep
        aStar bStar fStar hlqY prStarY adjPrY cmpY hlqZ prStarZ adjPrZ cmpZ
        TLQ tcmp cup) =
      coheratorCupProduct (flatBaseChangeQuasicoheratorAdjunction B E hE S hS 𝒳.val.val.p
          𝒳.val.property hincX
      hclosed hpres hls hlsD hwp hsep)
        (Functor.uncurry.obj (FibredSite.quasicoherentTensorBifunctor B S hS
      𝒳.val.val.p 𝒳.val.property)) TLQ tcmp
        (TLQ.map ((locallyQuasicoherentStructurePullbackMap B E hE S hS hincY hincP aStar fStar
      sq.fst hlqY prStarY adjPrY cmpY) ×ₘ
            (locallyQuasicoherentStructurePullbackMap B E hE S hS hincZ hincP bStar fStar
      sq.snd hlqZ prStarZ adjPrZ cmpZ)) ≫ cup)
```

**`AlgebraicGeometry.Stack.map_quasicoherentTensorPushforwardMap_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentTensorPushforward.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentTensorPushforward.lean#L427). The attribute's comment: “commutativity of the diagram of Remark 0GQR at μ, over the same carried data”.

> **The diagram of Remark 0GQR commutes at `μ`.**  The inclusion of **Lemma 0778** applied to
> `μ`, followed by the counit of the coherator adjunction, is the comparison `tcmp` of
> **Lemma 0GQM** followed by the counit in each tensor factor and then by the relative cup product
> precomposed with the two relative pullback maps.

```lean
theorem map_quasicoherentTensorPushforwardMap_comp_counit :
    (quasicoherentToFlatBaseChange B E hE S hS 𝒳.val.val.p 𝒳.val.property hincX).map
          (quasicoherentTensorPushforwardMap B E hE S hS a b sq hincX hincY hincZ hincP hclosed
              hpres hls hlsD hwp hsep
        aStar bStar fStar hlqY prStarY adjPrY cmpY hlqZ prStarZ adjPrZ cmpZ
        TLQ tcmp cup) ≫
        (flatBaseChangeQuasicoheratorAdjunction B E hE S hS 𝒳.val.val.p 𝒳.val.property hincX
      hclosed hpres hls hlsD hwp hsep).counit.app
          (fStar.obj ((quasicoherentToFlatBaseChange B E hE S hS sq.pt.val.val.p sq.pt.val.property
              hincP).obj
        (FibredSite.quasicoherentTensorUnit B S hS sq.pt.val.val.p sq.pt.val.property))) =
      tcmp.app ((flatBaseChangeQuasicoherator B E hE S hS 𝒳.val.val.p 𝒳.val.property hincX hclosed
          hpres hls hlsD hwp hsep).obj (aStar.obj
            ((quasicoherentToFlatBaseChange B E hE S hS 𝒴.val.val.p 𝒴.val.property hincY).obj
                (FibredSite.quasicoherentTensorUnit B S hS 𝒴.val.val.p 𝒴.val.property))),
          (flatBaseChangeQuasicoherator B E hE S hS 𝒳.val.val.p 𝒳.val.property hincX hclosed hpres
              hls hlsD hwp hsep).obj (bStar.obj
            ((quasicoherentToFlatBaseChange B E hE S hS 𝒵.val.val.p 𝒵.val.property hincZ).obj
                (FibredSite.quasicoherentTensorUnit B S hS 𝒵.val.val.p 𝒵.val.property)))) ≫
        TLQ.map ((flatBaseChangeQuasicoheratorAdjunction B E hE S hS 𝒳.val.val.p 𝒳.val.property
            hincX
      hclosed hpres hls hlsD hwp hsep).counit.app
              (aStar.obj ((quasicoherentToFlatBaseChange B E hE S hS 𝒴.val.val.p 𝒴.val.property
                  hincY).obj
                (FibredSite.quasicoherentTensorUnit B S hS 𝒴.val.val.p 𝒴.val.property))) ×ₘ
            (flatBaseChangeQuasicoheratorAdjunction B E hE S hS 𝒳.val.val.p 𝒳.val.property hincX
      hclosed hpres hls hlsD hwp hsep).counit.app
              (bStar.obj ((quasicoherentToFlatBaseChange B E hE S hS 𝒵.val.val.p 𝒵.val.property
                  hincZ).obj
                (FibredSite.quasicoherentTensorUnit B S hS 𝒵.val.val.p 𝒵.val.property)))) ≫
          (TLQ.map ((locallyQuasicoherentStructurePullbackMap B E hE S hS hincY hincP aStar fStar
      sq.fst hlqY prStarY adjPrY cmpY) ×ₘ
              (locallyQuasicoherentStructurePullbackMap B E hE S hS hincZ hincP bStar fStar
      sq.snd hlqZ prStarZ adjPrZ cmpZ)) ≫ cup)
```

## Tag 0GRP, a lemma

[Tag 0GRP](https://stacks.math.columbia.edu/tag/0GRP) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.eq_and_exists_iso_pointPullbackTransportIso_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/PointPullbackFullyFaithful.lean, line 631](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/PointPullbackFullyFaithful.lean#L631). The attribute's comment: “points over possibly different structure morphisms; they agree”.

> **Stacks 0GRP.** Let `𝒳` be an algebraic stack with affine diagonal and `B` a ring. Let
> `f₁, f₂ : Spec B ⟶ 𝒳` be two morphisms, given as points `x₁`, `x₂` of `𝒳` over `Spec B`, with
> structure morphisms `q₁, q₂ : Spec B ⟶ S`, and let `t : f₁^* ≅ f₂^*` be an isomorphism of the
> tensor functors `f_i^* : QCoh(𝒪_𝒳) ⥤ Mod_B`
>     (`AlgebraicGeometry.Stack.AlgebraicStacks.pointPullback`,
> a braided monoidal additive functor; `t` is monoidal). Then `q₁ = q₂`, and there is a 2-arrow
> `f₁ ⟶ f₂`, an isomorphism `a : x₁ ≅ x₂` lying over the identity of `Spec B`, inducing `t`.
>
> "Affine diagonal" is absolute, as in the source (Morphisms of Stacks, Definition 050D): it is the
> diagonal of the view of `𝒳` over `Spec ℤ`,
>     `AlgebraicGeometry.Stack.AlgebraicStacks.viewOverIntegers`.
> The structure morphisms to `S` are not assumed equal: that they agree is part of the conclusion,
> read off from the functions `B ⟶ Γ(x_i, 𝒪)` which `t` preserves (it is monoidal). The form with
> equal structure morphisms is
> `AlgebraicGeometry.Stack.AlgebraicStacks.exists_iso_pointPullbackTransportIso_eq_of_over`.
>
> The proof does not follow the source's chart and descent, but takes the chart `g = f₁ : Spec B ⟶ 𝒳`
> itself (affine, the diagonal being affine): with `W_i = Spec B ×_{f_i, 𝒳, f₁} Spec B` and
> `g_*𝒪 = g_{QCoh,*}𝒪_{Spec B}`, `f_i^*(g_*𝒪) = Γ(W_i)`, and `t` gives a ring isomorphism
> `Γ(W₂) ⟶ Γ(W₁)` over both copies of `B` (it is monoidal and natural, the multiplication of
> `g_*𝒪` being `AlgebraicGeometry.Stack.AlgebraicStacks.affineDirectImageMul`), hence an arrow
> `W₁ ⟶ W₂`; the image of the identity 2-arrow of `f₁` in `W₁` is the 2-arrow `f₁ ≅ f₂`. That it
> induces `t` follows from naturality of `t` and the units `M ⟶ g_* g^* M`. This is the content of
> Stacks 0GRK (the algebra `C = F(g_{QCoh,*}𝒪_U)` with its map `A ⟶ C`) for the point pullbacks,
> computed directly.

```lean
theorem eq_and_exists_iso_pointPullbackTransportIso_eq
    (hΔ : Stack.IsAffineHom B (⊤_ Scheme.{u}) (contains_terminalScheme B)
      (Stack.diagonal.{u, u, u + 1} B (⊤_ Scheme.{u}) (contains_terminalScheme B)
        (AlgebraicStacks.viewOverIntegers B S hS (contains_terminalScheme B) 𝒳).val))
    {q₁ q₂ : B.obj hR ⟶ B.obj hS} {x₁ x₂ : 𝒳.val.val.obj}
    (hx₁ : 𝒳.val.val.p.obj x₁ = Over.mk q₁) (hx₂ : 𝒳.val.val.p.obj x₂ = Over.mk q₂)
    (t : pointPullback B S hS 𝒳 x₁ (overSpecIso B S hS 𝒳 hx₁) ≅
      pointPullback B S hS 𝒳 x₂ (overSpecIso B S hS 𝒳 hx₂)) [NatTrans.IsMonoidal t.hom] :
    q₁ = q₂ ∧ ∃ (a : x₁ ≅ x₂) (ha : (BigFppfOver.toScheme B S hS).map (𝒳.val.val.p.map a.hom) ≫
        (overSpecIso B S hS 𝒳 hx₂).hom = (overSpecIso B S hS 𝒳 hx₁).hom),
      pointPullbackTransportIso B S hS 𝒳 (overSpecIso B S hS 𝒳 hx₁) (overSpecIso B S hS 𝒳 hx₂)
        a ha = t
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_iso_pointPullbackTransportIso_eq_of_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/PointPullbackFullyFaithful.lean, line 662](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/PointPullbackFullyFaithful.lean#L662). The attribute's comment: “the source's form, with equal structure morphisms”.

> **Stacks 0GRP, with equal structure morphisms** (the source's statement). Let `𝒳` be an
> algebraic stack with affine diagonal (over `Spec ℤ`), `B` a ring and `f₁, f₂ : Spec B ⟶ 𝒳` two
> morphisms over `S`, given as points `x₁`, `x₂` of `𝒳` lying over the same object `Spec B ⟶ S` of
> the site. Every isomorphism `t : f₁^* ≅ f₂^*` of the tensor functors
> `f_i^* : QCoh(𝒪_𝒳) ⥤ Mod_B` is induced by a 2-arrow `f₁ ⟶ f₂`: an isomorphism `a : x₁ ≅ x₂` of
> the fibre over `Spec B`.

```lean
theorem exists_iso_pointPullbackTransportIso_eq_of_over
    (hΔ : Stack.IsAffineHom B (⊤_ Scheme.{u}) (contains_terminalScheme B)
      (Stack.diagonal.{u, u, u + 1} B (⊤_ Scheme.{u}) (contains_terminalScheme B)
        (AlgebraicStacks.viewOverIntegers B S hS (contains_terminalScheme B) 𝒳).val))
    {q : B.obj hR ⟶ B.obj hS} {x₁ x₂ : 𝒳.val.val.obj}
    (hx₁ : 𝒳.val.val.p.obj x₁ = Over.mk q) (hx₂ : 𝒳.val.val.p.obj x₂ = Over.mk q)
    (t : pointPullback B S hS 𝒳 x₁ (overSpecIso B S hS 𝒳 hx₁) ≅
      pointPullback B S hS 𝒳 x₂ (overSpecIso B S hS 𝒳 hx₂)) [NatTrans.IsMonoidal t.hom] :
    ∃ (a : x₁ ≅ x₂) (ha : 𝒳.val.val.p.map a.hom = eqToHom (hx₁.trans hx₂.symm)),
      pointPullbackTransportIso B S hS 𝒳 (overSpecIso B S hS 𝒳 hx₁) (overSpecIso B S hS 𝒳 hx₂)
        a (toScheme_map_comp_overSpecIso B S hS 𝒳 hx₁ hx₂ a ha) = t
```

## Tag 0GRQ, a lemma

[Tag 0GRQ](https://stacks.math.columbia.edu/tag/0GRQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.existsUnique_pointPullback_iso_of_tensorFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/TensorFunctorPoint.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/TensorFunctorPoint.lean#L110). The attribute's comment: “the morphism Spec R ⟶ 𝒳 is a point over Spec R in the site; uniqueness is up to the unique 2-arrow inducing the given isomorphism of tensor functors”.

> **Stacks 0GRQ.** Let `𝒳` be a Noetherian algebraic stack with affine diagonal (over
> `Spec ℤ`, as in the source), `R` a ring (with `Spec R` in the site) and `F : QCoh(𝒪_𝒳) ⥤ Mod_R` a
> right exact tensor functor (additive, preserving finite colimits, braided monoidal) which commutes
> with direct sums. Then `F` comes from a unique morphism `Spec R ⟶ 𝒳`:
>
> 1. there are a point `x` of `𝒳` over `Spec R` (lying over some `q : Spec R ⟶ S`) and an
>    isomorphism of tensor functors `e : F ≅ x^*`;
> 2. if `e₁ : F ≅ x₁^*` and `e₂ : F ≅ x₂^*` are two such, over `q₁` and `q₂`, then `q₁ = q₂` and
>    there is a unique 2-arrow `a : x₁ ≅ x₂` over the identity of `Spec R` whose induced isomorphism
>    `x₁^* ≅ x₂^*` is `e₁⁻¹ ≫ e₂`.

```lean
theorem existsUnique_pointPullback_iso_of_tensorFunctor
    (h𝒳 : IsNoetherianStack.{u, w, w'} B S hS 𝒳)
    (hΔ : Stack.IsAffineHom B (⊤_ Scheme.{u}) (contains_terminalScheme B)
      (Stack.diagonal.{u, u, u + 1} B (⊤_ Scheme.{u}) (contains_terminalScheme B)
        (viewOverIntegers B S hS (contains_terminalScheme B) 𝒳).val))
    {R : Type u} [CommRing R] (hR : B.Contains (Spec (CommRingCat.of R)))
    (F : quasicoherentModules B S hS 𝒳 ⥤ ModuleCat.{u} R) [F.Additive] [F.Braided]
    [PreservesFiniteColimits F] [∀ J : Type u, PreservesColimitsOfShape (Discrete J) F] :
    (∃ (q : B.obj hR ⟶ B.obj hS) (x : 𝒳.val.val.obj) (hx : 𝒳.val.val.p.obj x = Over.mk q)
        (e : F ≅ pointPullback B S hS 𝒳 x (overSpecIso B S hS 𝒳 hx)), NatTrans.IsMonoidal e.hom) ∧
    ∀ {q₁ q₂ : B.obj hR ⟶ B.obj hS} {x₁ x₂ : 𝒳.val.val.obj}
      (hx₁ : 𝒳.val.val.p.obj x₁ = Over.mk q₁) (hx₂ : 𝒳.val.val.p.obj x₂ = Over.mk q₂)
      (e₁ : F ≅ pointPullback B S hS 𝒳 x₁ (overSpecIso B S hS 𝒳 hx₁))
      (e₂ : F ≅ pointPullback B S hS 𝒳 x₂ (overSpecIso B S hS 𝒳 hx₂)),
      NatTrans.IsMonoidal e₁.hom → NatTrans.IsMonoidal e₂.hom →
      q₁ = q₂ ∧ ∃ (a : x₁ ≅ x₂) (ha : (BigFppfOver.toScheme B S hS).map (𝒳.val.val.p.map a.hom) ≫
          (overSpecIso B S hS 𝒳 hx₂).hom = (overSpecIso B S hS 𝒳 hx₁).hom),
        pointPullbackTransportIso B S hS 𝒳 (overSpecIso B S hS 𝒳 hx₁) (overSpecIso B S hS 𝒳 hx₂)
            a ha = e₁.symm ≪≫ e₂ ∧
          ∀ (b : x₁ ≅ x₂) (hb : (BigFppfOver.toScheme B S hS).map (𝒳.val.val.p.map b.hom) ≫
              (overSpecIso B S hS 𝒳 hx₂).hom = (overSpecIso B S hS 𝒳 hx₁).hom),
            pointPullbackTransportIso B S hS 𝒳 (overSpecIso B S hS 𝒳 hx₁)
              (overSpecIso B S hS 𝒳 hx₂) b hb = e₁.symm ≪≫ e₂ → b = a
```

## Tag 0GRR, a theorem

[Tag 0GRR](https://stacks.math.columbia.edu/tag/0GRR) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.existsUnique_coherentPointPullback_iso_of_tensorFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoherentTensorFunctorPoint.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoherentTensorFunctorPoint.lean#L61). The attribute's comment: “the morphism Spec R ⟶ 𝒳 is a point over Spec R in the site; uniqueness is up to a 2-arrow inducing the given isomorphism of tensor functors”.

> **Stacks 0GRR.** Let `𝒳` be a Noetherian algebraic stack with affine diagonal (over `Spec ℤ`,
> as in the source), `R` a Noetherian ring (with `Spec R` in the site) and
> `F : Coh(𝒪_𝒳) ⥤ Mod^{fg}_R` a right exact tensor functor (additive, preserving finite colimits,
> braided monoidal). Then `F` comes from a unique morphism `Spec R ⟶ 𝒳`:
>
> 1. there are a point `x` of `𝒳` over `Spec R` (lying over some `q : Spec R ⟶ S`) and an
>    isomorphism of tensor functors `F ≅ x^*|_{Coh}`;
> 2. if `E₁ : F ≅ x₁^*|_{Coh}` and `E₂ : F ≅ x₂^*|_{Coh}` are two such, over `q₁` and `q₂`, then
>    `q₁ = q₂` and there is a 2-arrow `a : x₁ ≅ x₂` over the identity of `Spec R` inducing
>    `E₁⁻¹ ≫ E₂` on coherent modules.

```lean
theorem existsUnique_coherentPointPullback_iso_of_tensorFunctor
    (h𝒳 : IsNoetherianStack.{u, w, w'} B S hS 𝒳)
    (hΔ : Stack.IsAffineHom B (⊤_ Scheme.{u}) (contains_terminalScheme B)
      (Stack.diagonal.{u, u, u + 1} B (⊤_ Scheme.{u}) (contains_terminalScheme B)
        (AlgebraicStacks.viewOverIntegers B S hS (contains_terminalScheme B) 𝒳).val))
    [IsNoetherianRing R] (hR : B.Contains (Spec (CommRingCat.of R)))
    (F : Coh.{u, u, w} B S hS 𝒳 ⥤ FGModuleCat.{u} R) [F.Additive] [F.Braided]
    [PreservesFiniteColimits F] :
    (∃ (q : B.obj hR ⟶ B.obj hS) (x : 𝒳.val.val.obj) (hx : 𝒳.val.val.p.obj x = Over.mk q)
      (E : F ≅ coherentPointPullback B S hS 𝒳 x (overSpecIso B S hS 𝒳 hx)),
        NatTrans.IsMonoidal E.hom) ∧
    ∀ {q₁ q₂ : B.obj hR ⟶ B.obj hS} {x₁ x₂ : 𝒳.val.val.obj}
      (hx₁ : 𝒳.val.val.p.obj x₁ = Over.mk q₁) (hx₂ : 𝒳.val.val.p.obj x₂ = Over.mk q₂)
      (E₁ : F ≅ coherentPointPullback B S hS 𝒳 x₁ (overSpecIso B S hS 𝒳 hx₁))
      (E₂ : F ≅ coherentPointPullback B S hS 𝒳 x₂ (overSpecIso B S hS 𝒳 hx₂)),
      NatTrans.IsMonoidal E₁.hom → NatTrans.IsMonoidal E₂.hom →
      q₁ = q₂ ∧ ∃ (a : x₁ ≅ x₂) (ha : (BigFppfOver.toScheme B S hS).map
          (𝒳.val.val.p.map a.hom) ≫ (overSpecIso B S hS 𝒳 hx₂).hom =
            (overSpecIso B S hS 𝒳 hx₁).hom),
        Functor.whiskerLeft (coherentQuasicoherentInclusion B S hS 𝒳)
            (pointPullbackTransportIso B S hS 𝒳 (overSpecIso B S hS 𝒳 hx₁)
              (overSpecIso B S hS 𝒳 hx₂) a ha).hom =
          (coherentPointPullbackCompIso B S hS 𝒳 x₁ _).inv ≫
            Functor.whiskerRight (E₁.inv ≫ E₂.hom)
              (forget₂ (FGModuleCat.{u} R) (ModuleCat.{u} R)) ≫
              (coherentPointPullbackCompIso B S hS 𝒳 x₂ _).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.16, Tag 0GRI](https://stacks.math.columbia.edu/tag/0GRI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
