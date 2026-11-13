---
declaration: section
origin: cited
lean: AlgebraicGeometry.isIso_pushforwardToRightDerived_of_isAffine, AlgebraicGeometry.reflectsIsomorphisms_derivedQuasicoherentPushforward_specMap, AlgebraicGeometry.reflectsIsomorphisms_derivedQuasicoherentPushforward, Stacks.AlgebraicGeometry.AffinePushforwardTExactness.isIso_of_isIso_derivedPushforward, AlgebraicGeometry.AffineProjectionFormula.isIso_pullbackPushforwardTensorMap_unconditional, Stacks.AlgebraicGeometry.AffinePushforwardTExactness.derivedPushforwardDerivedPullbackTensorIso, Stacks.AlgebraicGeometry.DerivedAffinePushforward.derivedPushforwardPullbackTensorIso, Stacks.AlgebraicGeometry.DerivedAffinePushforward.derivedPushforwardDerivedPullbackTensorIso
statement: formalized
proof: formalized
---

# 36.5 Affine morphisms

Section 36.5 of the Stacks Project, [Tag 0AVV](https://stacks.math.columbia.edu/tag/0AVV). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G9R, a lemma

[Tag 0G9R](https://stacks.math.columbia.edu/tag/0G9R) in the Stacks Project.

**`AlgebraicGeometry.isIso_pushforwardToRightDerived_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAcyclic/AffineMorphism.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedAcyclic/AffineMorphism.lean#L76).

> **Stacks Project, Tag 0G9R.** Let `f : X ⟶ Y` be an affine morphism of schemes and let `K`
> be a complex of quasi-coherent `𝒪_X`-modules. Then `f_* K = Rf_* K`: the right derived direct
> image is defined at `K` and the canonical map from the termwise direct image to it is an
> isomorphism.

```lean
theorem isIso_pushforwardToRightDerived_of_isAffine
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsAffineHom f]
    [HasDerivedCategory Y.Modules]
    (K : HomologicalComplex X.Modules (ComplexShape.up ℤ))
    (hK : ∀ i, (K.X i).IsQuasicoherent) :
    ((Scheme.Modules.pushforward f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh).ComputesRightDerived
        (HomotopyCategory.quasiIso X.Modules (ComplexShape.up ℤ))
        ((HomotopyCategory.quotient X.Modules (ComplexShape.up ℤ)).obj K)
```

## Tag 08I8, a lemma

[Tag 08I8](https://stacks.math.columbia.edu/tag/08I8) in the Stacks Project.

**`AlgebraicGeometry.reflectsIsomorphisms_derivedQuasicoherentPushforward_specMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/ReflectsIsomorphisms.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/ReflectsIsomorphisms.lean#L114). The attribute's comment: “a morphism Spec φ of affine schemes”.

> **[Stacks, Tag 08I8] for a morphism of affine schemes.** Let `φ : R ⟶ S` and let
> `f = Spec φ : Spec S ⟶ Spec R`. Then `Rf_* : D_QCoh(𝒪_{Spec S}) ⥤ D_QCoh(𝒪_{Spec R})` reflects
> isomorphisms: a map of complexes with quasi-coherent cohomology is invertible as soon as its
> derived pushforward is.
>
> Derived sheafification is an equivalence `D(S) ≌ D_QCoh(𝒪_{Spec S})` [Stacks, Tag 06Z0] carrying
> `Rf_*` to derived restriction of scalars along `φ` [Stacks, Tag 0DJK], and that functor reflects
> isomorphisms.

```lean
public theorem reflectsIsomorphisms_derivedQuasicoherentPushforward_specMap :
    (derivedQuasicoherentPushforward (Spec.map φ)).ReflectsIsomorphisms
```

**`AlgebraicGeometry.reflectsIsomorphisms_derivedQuasicoherentPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/ReflectsIsomorphismsAffineHom.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/ReflectsIsomorphismsAffineHom.lean#L285).

> **[Stacks, Tag 08I8].** Let `f : X ⟶ Y` be an affine morphism of schemes, with `Y` an
> arbitrary scheme. Then `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` reflects isomorphisms.
>
> `AlgebraicGeometry.derivedQuasicoherentPushforward` is by construction the lift of
> `D_QCoh(𝒪_X) ⥤ D(𝒪_X) ⥤ D(𝒪_Y)` through the inclusion of `D_QCoh(𝒪_Y)`, so a map of
> `D_QCoh(𝒪_X)` whose derived direct image is invertible in `D_QCoh(𝒪_Y)` has invertible derived
> direct image in `D(𝒪_Y)`;
> `AlgebraicGeometry.AnyModel.isIso_of_isIso_derivedPushforward_map_of_isAffineHom` makes it
> invertible in `D(𝒪_X)`, and the inclusion of `D_QCoh(𝒪_X)` is fully faithful, hence reflects
> isomorphisms.

```lean
public theorem reflectsIsomorphisms_derivedQuasicoherentPushforward [IsAffineHom f] :
    (derivedQuasicoherentPushforward f).ReflectsIsomorphisms
```

**`Stacks.AlgebraicGeometry.AffinePushforwardTExactness.isIso_of_isIso_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/ReflectsIsomorphismsQuasicoherent.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/ReflectsIsomorphismsQuasicoherent.lean#L86).

> **[Stacks, Tag 08I8].**  Let `f : W ⟶ Y` be an affine morphism of schemes and let
> `α : E ⟶ F` be a morphism of `D(𝒪_W)` between complexes whose cohomology sheaves are
> quasi-coherent.  If the derived direct image `Rf_*α` is invertible in `D(𝒪_Y)`, then `α` is
> invertible.  This is the assertion that `Rf_* : D_QCoh(𝒪_W) ⥤ D_QCoh(𝒪_Y)` reflects
> isomorphisms.

```lean
theorem isIso_of_isIso_derivedPushforward (f : W ⟶ Y) [IsAffineHom f]
    {E F : DerivedCategory W.Modules}
    (hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor W.Modules i).obj E).IsQuasicoherent)
    (hF : ∀ i : ℤ, ((DerivedCategory.homologyFunctor W.Modules i).obj F).IsQuasicoherent)
    (α : E ⟶ F)
    (h : IsIso ((derivedPushforward f.toLRSHom.toShHom).map α)) : IsIso α
```

## Tag 08I9, a lemma

[Tag 08I9](https://stacks.math.columbia.edu/tag/08I9) in the Stacks Project.

**`AlgebraicGeometry.AffineProjectionFormula.isIso_pullbackPushforwardTensorMap_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/AffineProjectionFormulaGeneralBase.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/AffineProjectionFormulaGeneralBase.lean#L160). The attribute's comment: “the canonical morphism Rf\_*O\_X ⊗^L E ⟶ Rf\_*Lf^*E is invertible for every affine morphism of schemes f : X ⟶ S and every object E of D\_QCoh(O\_S), with the genuine derived pullback Lf^* and the genuine derived tensor product ⊗^L, no boundedness, flatness or finiteness hypothesis on E and no hypothesis on S”.

> **Stacks, Tag 08I9.**  Let `f : X ⟶ S` be an affine morphism of schemes and let `E` be an
> object of `D_QCoh(𝒪_S)`, that is, an object of `D(𝒪_S)` all of whose cohomology sheaves are
> quasi-coherent.  Then the canonical morphism
>
> `Rf_*𝒪_X ⊗^𝐋_{𝒪_S} E ⟶ Rf_*Lf^*E`
>
> is an isomorphism.  The derived pullback is the genuine `Lf^*` of [Stacks, Tag 06YJ], the tensor
> product is the genuine `⊗^𝐋`, and there is no boundedness, flatness or finiteness hypothesis on
> `E` and no hypothesis on `S`.
>
> The proof is the source's.  The question is local on `S`, which is
> `Stacks.Cohomology.DerivedProjectionFormula.isIso_pullbackPushforwardTensorMap_of_openCover` over
> the cover of `S` by its affine opens; each restriction `f|_U` is an affine morphism over an affine
> scheme, and the restricted complex still has quasi-coherent cohomology by
> `isQuasicoherent_homology_derivedPullback_of_isOpenImmersion`, so
> `isIso_pullbackPushforwardTensorMap_of_isAffine` applies to it.

```lean
theorem isIso_pullbackPushforwardTensorMap_unconditional {X S : Scheme.{u}} (f : X ⟶ S)
    [IsAffineHom f] (E : DerivedCategory S.Modules)
    (hE : ∀ n : ℤ, ((DerivedCategory.homologyFunctor S.Modules n).obj E).IsQuasicoherent) :
    IsIso (pullbackPushforwardTensorMap' f.toLRSHom.toShHom E)
```

**`Stacks.AlgebraicGeometry.AffinePushforwardTExactness.derivedPushforwardDerivedPullbackTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/PullbackPushforwardDerivedTensor.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/PullbackPushforwardDerivedTensor.lean#L114).

> For an affine morphism of schemes `f : X ⟶ S` and a complex `E` on `S` with quasi-coherent
> cohomology,
>
> `f_*𝒪_X ⊗^𝐋_{𝒪_S} E ≅ Rf_* Lf^* E`,
>
> with the derived tensor product and with no boundedness hypothesis on `E`.

```lean
def derivedPushforwardDerivedPullbackTensorIso (f : X ⟶ S) [IsAffineHom f]
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing S.toRingedSpace)))
    (hE : ∀ j : ℤ, ((DerivedCategory.homologyFunctor
      (SheafOfModules.{u} (structureSheafRing S.toRingedSpace)) j).obj E).IsQuasicoherent) :
    ((derivedTensorProductFunctor S.toRingedSpace.sheaf).obj
        ((DerivedCategory.singleFunctor
          (SheafOfModules.{u} (structureSheafRing S.toRingedSpace)) 0).obj
          ((modulePushforward f.toLRSHom.toShHom).obj
            (SheafOfModules.unit (structureSheafRing X.toRingedSpace))))).obj E ≅
      (derivedPushforward f.toLRSHom.toShHom).obj
        ((derivedPullback f.toLRSHom.toShHom).obj E)
```

**`Stacks.AlgebraicGeometry.DerivedAffinePushforward.derivedPushforwardPullbackTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/PullbackPushforwardTensor.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/PullbackPushforwardTensor.lean#L198). The attribute's comment: “a SPECIAL CASE of the general statement, which is proved — the tag is closed by AlgebraicGeometry.AffineProjectionFormula.isIso\_pullbackPushforwardTensorMap\_unconditional. The degree-zero clause: Rf\_*((f^*H)[0]) ≅ (f\_*𝒪\_X ⊗\_\{𝒪\_S} H)[0] for H a quasi-coherent 𝒪\_S-module, with the underived f^* and ⊗ in place of the general statement's Lf^* and ⊗ᴸ and E restricted to a module in degree zero”.

> **[Stacks, Tag 08I9] for `E` a quasi-coherent module in degree zero, with the underived
> inverse image and tensor product**: for an affine morphism of schemes `f : X ⟶ S` and a
> quasi-coherent `𝒪_S`-module `H`,
>
> `Rf_*((f^*H)[0]) ≅ (f_*𝒪_X ⊗_{𝒪_S} H)[0]`
>
> in `D(𝒪_S)`. Unconditional.
>
> The source states `Rf_*Lf^*E ≅ E ⊗^𝐋_{𝒪_S} f_*𝒪_X`; here both derived functors on the
> right-hand side of that identity are replaced by their underived counterparts `f^*` and `⊗`.
> See the module documentation for what that costs. The proof is
> `pushforwardStructureSheafTensorIso` followed by [Stacks, Tag 01XC] in the form
> `derivedPushforwardSingleIso`: `f^*H` is quasi-coherent and `f` is affine, so the ordinary direct
> image of `f^*H` in degree zero is already its derived direct image.

```lean
def derivedPushforwardPullbackTensorIso [IsAffineHom f] (H : S.Modules)
    (hH : H.IsQuasicoherent) :
    (Stacks.Duality.derivedPushforward f).obj
        ((DerivedCategory.singleFunctor X.Modules 0).obj ((Scheme.Modules.pullback f).obj H)) ≅
      (DerivedCategory.singleFunctor S.Modules 0).obj
        (((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor
            ⟨((S.toRingedSpace)).presheaf, ((S.toRingedSpace)).IsSheaf⟩))).obj
          ((Scheme.Modules.pushforward f).obj (SheafOfModules.unit X.ringCatSheaf : X.Modules),
            H))
```

**`Stacks.AlgebraicGeometry.DerivedAffinePushforward.derivedPushforwardDerivedPullbackTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/PullbackPushforwardTensor.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/PullbackPushforwardTensor.lean#L250). The attribute's comment: “a SPECIAL CASE of the general statement, which is proved — the tag is closed by AlgebraicGeometry.AffineProjectionFormula.isIso\_pullbackPushforwardTensorMap\_unconditional. E = H[0] for f affine and H a flat quasi-coherent 𝒪\_S-module, with the genuine Lf^* and nothing carried: Rf\_*Lf^*(H[0]) ≅ (f\_*𝒪\_X ⊗\_\{𝒪\_S} H)[0]; the right-hand tensor product is the underived ⊗, not ⊗ᴸ, and E is restricted to a module in degree zero”.

> **[Stacks, Tag 08I9] for `E` a flat quasi-coherent module in degree zero, with the genuine
> derived pullback**: for an affine morphism of schemes `f : X ⟶ S` and a flat quasi-coherent
> `𝒪_S`-module `H`,
>
> `Rf_*Lf^*(H[0]) ≅ (f_*𝒪_X ⊗_{𝒪_S} H)[0]`,
>
> with nothing assumed beyond those restrictions on `f` and `H`. Flatness of `H` makes `H[0]`
> K-flat, so the degree-zero comparison `Lf^*(H[0]) ≅ (f^*H)[0]` is
> `derivedPullbackSingleIsoOfFlat`; the tensor product on the right-hand side is still the
> underived one.

```lean
def derivedPushforwardDerivedPullbackTensorIso [IsAffineHom f] (H : S.Modules)
    (hH : H.IsQuasicoherent)
    (hHflat : SheafOfModules.IsFlat.{u, u, u, u} (O := S.toRingedSpace.sheaf) H) :
    (Stacks.Duality.derivedPushforward f).obj
        ((Stacks.Duality.derivedPullback f).obj
          ((DerivedCategory.singleFunctor S.Modules 0).obj H)) ≅
      (DerivedCategory.singleFunctor S.Modules 0).obj
        (((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor
            ⟨((S.toRingedSpace)).presheaf, ((S.toRingedSpace)).IsSheaf⟩))).obj
          ((Scheme.Modules.pushforward f).obj (SheafOfModules.unit X.ringCatSheaf : X.Modules),
            H))
```

**`Stacks.AlgebraicGeometry.DerivedAffinePushforward.derivedPushforwardDerivedPullbackTensorIsoOfExact`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/PullbackPushforwardTensor.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/PullbackPushforwardTensor.lean#L299). The attribute's comment: “a SPECIAL CASE of the general statement, which is proved — the tag is closed by AlgebraicGeometry.AffineProjectionFormula.isIso\_pullbackPushforwardTensorMap\_unconditional. E = H[0] for f affine with f^* exact (f flat) and H quasi-coherent, with the genuine Rf\_* and Lf^* and nothing carried: Rf\_*Lf^*(H[0]) ≅ (f\_*𝒪\_X ⊗\_\{𝒪\_S} H)[0]; the right-hand tensor product is the underived ⊗, not ⊗ᴸ, and E is restricted to a module in degree zero”.

> **[Stacks, Tag 08I9] for a flat affine morphism and `E` a quasi-coherent module in degree
> zero**: for `f : X ⟶ S` affine with `f^*` exact and `H` a quasi-coherent `𝒪_S`-module,
>
> `Rf_*Lf^*(H[0]) ≅ (f_*𝒪_X ⊗_{𝒪_S} H)[0]`
>
> in `D(𝒪_S)`, with no hypothesis carried. Flatness of `f` replaces the flatness of `H` asked by
> `derivedPushforwardDerivedPullbackTensorIso`: it supplies the degree-zero comparison
> `Lf^*(H[0]) ≅ (f^*H)[0]` through `derivedPullbackSingleIsoOfExact` instead.
>
> Both sides are the source's, except that the tensor product on the right is the ordinary one
> rather than `⊗^𝐋`; for `f` flat the two agree, but that identification is not proved here.

```lean
def derivedPushforwardDerivedPullbackTensorIsoOfExact [IsAffineHom f]
    [PreservesFiniteLimits (Scheme.Modules.pullback f)] (H : S.Modules)
    (hH : H.IsQuasicoherent) :
    (Stacks.Duality.derivedPushforward f).obj
        ((Stacks.Duality.derivedPullback f).obj
          ((DerivedCategory.singleFunctor S.Modules 0).obj H)) ≅
      (DerivedCategory.singleFunctor S.Modules 0).obj
        (((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor
            ⟨((S.toRingedSpace)).presheaf, ((S.toRingedSpace)).IsSheaf⟩))).obj
          ((Scheme.Modules.pushforward f).obj (SheafOfModules.unit X.ringCatSheaf : X.Modules),
            H))
```

**`Stacks.AlgebraicGeometry.AffinePullbackPushforwardTensor.derivedPushforwardDerivedPullbackTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/PullbackPushforwardTensorQCoh.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/PullbackPushforwardTensorQCoh.lean#L158). The attribute's comment: “the whole lemma: for an affine morphism of schemes f : X ⟶ S and every K in D\_QCoh(𝒪\_S), the canonical map f\_*𝒪\_X ⊗ᴸ K ⟶ Rf\_*Lf^*K is invertible. The tensor factors are written in the opposite order from the source, the derived tensor product of a ringed space being symmetric”.

> **[Stacks, Tag 08I9].**  Let `f : X ⟶ S` be an affine morphism of schemes.  For every `K`
> in `D_QCoh(𝒪_S)`,
>
> `f_*𝒪_X ⊗^𝐋_{𝒪_S} K ≅ Rf_*Lf^*K`,
>
> with the *ordinary* direct image of the structure sheaf placed in degree zero on the left and
> the *derived* tensor product.  The left-hand factor is `(f_*𝒪_X)[0]` rather than `Rf_*(𝒪_X[0])`
> by [Stacks, Tag 01XC] for an affine morphism, which is the first step of the source's proof.

```lean
def derivedPushforwardDerivedPullbackTensorIso (f : X ⟶ S) [IsAffineHom f]
    (K : DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing S.toRingedSpace)))
    (hK : Stacks.DerivedQCoh.IsDQCoh (R := structureSheafRing S.toRingedSpace) K) :
    ((derivedTensorProductFunctor S.toRingedSpace.sheaf).obj
        ((DerivedCategory.singleFunctor
            (_root_.SheafOfModules.{u} (structureSheafRing S.toRingedSpace)) 0).obj
          ((modulePushforward f.toLRSHom.toShHom).obj
            (_root_.SheafOfModules.unit
              (Stacks.SheafOfModules.Tensor.ringSheaf X.toRingedSpace.sheaf))))).obj K ≅
      (derivedPushforward f.toLRSHom.toShHom).obj
        ((derivedPullback f.toLRSHom.toShHom).obj K)
```

## Tag 0AVW, a lemma

[Tag 0AVW](https://stacks.math.columbia.edu/tag/0AVW) in the Stacks Project.

**`Stacks.AlgebraicGeometry.DerivedAffinePushforward.derivedPushforwardOverRingCompRestrictScalarsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/DerivedPushforwardOverPushforwardRing.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/DerivedPushforwardOverPushforwardRing.lean#L354). The attribute's comment: “the factorisation of Rf\_* through D(f\_*𝒪\_X); the equivalence clause is proved in isEquivalence\_derivedQuasicoherentPushforwardOverRing (QuasicoherentEquivalenceOverPushforwardRing.lean), on the whole derived categories”.

> **The factorisation asserted by [Stacks, Tag 0AVW]**: the derived direct image `Rf_*` is
> `Φ` followed by the functor `D(f_* 𝒪_X) ⥤ D(𝒪_S)` induced by restriction of scalars along
> `𝒪_S ⟶ f_* 𝒪_X`.  Both functors are right derived functors of degreewise direct image, so they
> agree by the uniqueness of right derived functors.
>
> This is the second of the tag's two clauses, and the attribute carries a phrase naming it.  The
> first clause — that `Φ` is an *equivalence* onto `D_QCoh(f_* 𝒪_X)` for `f` affine — is
> `isEquivalence_derivedQuasicoherentPushforwardOverRing`.  The factorisation below holds for every
> morphism of schemes, with no affineness needed, and is read on the whole derived categories
> rather than on the quasi-coherent ones, so it is stronger than the source's clause on both
> counts.

```lean
def derivedPushforwardOverRingCompRestrictScalarsIso :
    AlgebraicGeometry.AnyModel.derivedPushforward.{w} f ≅
      derivedPushforwardOverRing.{w} f ⋙ (scalarRestriction f).mapDerivedCategory
```

**`Stacks.AlgebraicGeometry.DerivedAffinePushforward.isEquivalence_and_factorisation_derivedQuasicoherentPushforwardOverRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/QuasicoherentEquivalenceOverPushforwardRing.lean, line 709](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/QuasicoherentEquivalenceOverPushforwardRing.lean#L709).

> **[Stacks, Tag 0AVW], the whole statement.**  Let `f : X ⟶ S` be an affine morphism of
> schemes.  Then direct image induces an **equivalence**
> `Φ : D_QCoh(𝒪_X) ⥤ D_QCoh(f_* 𝒪_X)`, and the composition of `Φ` with the functor
> `D_QCoh(f_* 𝒪_X) ⥤ D_QCoh(𝒪_S)` given by restriction of scalars along `𝒪_S ⟶ f_* 𝒪_X` **is**
> `Rf_*`.
>
> Both clauses are read on the quasi-coherent subcategories and under the source's condition that
> `f` be affine, which is where the tag's own statement puts them; the existing registration on
> `derivedPushforwardOverRingCompRestrictScalarsIso` carries the second clause alone, for every
> morphism of schemes and on the whole derived categories.

```lean
theorem isEquivalence_and_factorisation_derivedQuasicoherentPushforwardOverRing :
    (derivedQuasicoherentPushforwardOverRing f).IsEquivalence ∧
      Nonempty (derivedQuasicoherentPushforwardOverRing f ⋙
          derivedQuasicoherentScalarRestriction f ≅
        derivedQuasicoherentPushforwardAtModel f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.5, Tag 0AVV](https://stacks.math.columbia.edu/tag/0AVV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
