---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.ComplexLifting.exists_liftedComplex, Deformation.ComplexLift.unit_comp_curvature, Deformation.ComplexLift.obstructionMap, Deformation.ComplexLift.obstructionMap_natural, Deformation.ComplexLift.obstructionMap_eq_of_hom, Deformation.ComplexLift.tensorOmega, Deformation.ComplexLift.tensorOmega_natural_derived, Deformation.ComplexLift.tensorOmegaObj
statement: formalized
proof: formalized
---

# 91.16 Deformations of complexes on ringed topoi

Section 91.16 of the Stacks Project, [Tag 0DIS](https://stacks.math.columbia.edu/tag/0DIS). 7 tags here are carried by 47 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DIT, a lemma

[Tag 0DIT](https://stacks.math.columbia.edu/tag/0DIT) in the Stacks Project.

**`Stacks.SheafOfModules.ComplexLifting.exists_liftedComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/ComplexLifting.lean, line 582](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/ComplexLifting.lean#L582).

> **Stacks 0DIT.** A bounded-above flat lifting exists for a bounded-above complex and a
> bounded-above graded flat family whose given maps form a map of complexes after extension of
> scalars. The ambient module universe contains the site and the ring sheaves.

```lean
theorem exists_liftedComplex [J.WEqualsLocallyBijective AddCommGrpCat.{max u v w z}]
    [HasSheafify J AddCommGrpCat.{max u v w z}] {O O₀ : Sheaf J CommRingCat.{w}} (f : O ⟶ O₀)
    (hf : Sheaf.IsLocallySurjective f)
    (G : GradedDifferential
      (_root_.SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf O)))
    (K₀ : CochainComplex
      (_root_.SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf O₀)) ℤ)
    (g : ∀ n, G.X n ⟶
      (_root_.SheafOfModules.restrictScalars (ringSheafMap f)).obj (K₀.X n))
    (hGflat : ∀ n, AlgebraicGeometry.SheafOfModules.IsFlat (G.X n))
    (hGbounded : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (G.X n))
    (hKbounded : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (K₀.homology n))
    (hG₀ : BaseChangeTo f G K₀ g) :
    Nonempty (LiftedComplex f G K₀ g)
```

## Tag 0DIU, a lemma

[Tag 0DIU](https://stacks.math.columbia.edu/tag/0DIU) in the Stacks Project.

**`Deformation.ComplexLift.unit_comp_curvature`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureClass.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureClass.lean#L289). The attribute's comment: “variant: the curvature d ∘ d of the lifted differential, the complex-level map; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> The curvature computes the square of the lifted differential: pulled back to the lift and
> followed by the ideal inclusion it is `d ∘ d`. This is the identification of `ω` with the
> curvature class, read on the complex representing it.

```lean
theorem unit_comp_curvature (n : ℤ) :
    L.baseChange.unit n ≫ (restrict f).map (curvature T n) ≫ T.emb (n + 1 + 1) =
      L.F.d n ≫ L.F.d (n + 1)
```

**`Deformation.ComplexLift.obstructionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureClass.lean, line 444](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureClass.lean#L444). The attribute's comment: “variant: at a supplied derived ideal tensor datum D; the tag is Deformation.ComplexLift.tensorOmegaMinus, the map K₀ ⟶ (K₀ ⊗^L I)[2]”.

> **Stacks 0DIU.** The canonical map `ω(K₀) : K₀ ⟶ (K₀ ⊗^L_{O₀} I)[2]` attached to a
> square-zero extension of sheaves of rings with ideal sheaf `I`. It is the curvature of the
> lifted differential of a bounded above flat lift of `K₀`, transported along the
> quasi-isomorphism identifying the reduction of that lift with `K₀`.

```lean
def obstructionMap {L : FlatLift f K₀} (T : IdealKernel S L) :
    DerivedCategory.Q.obj K₀ ⟶ (D.functor.obj (DerivedCategory.Q.obj K₀))⟦(2 : ℤ)⟧
```

**`Deformation.ComplexLift.obstructionMap_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureClass.lean, line 479](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureClass.lean#L479). The attribute's comment: “variant: naturality of ω along a morphism of flat lifts at a supplied derived ideal tensor datum D; the tag is Deformation.ComplexLift.tensorOmegaMinus\_natural”.

> **Stacks 0DIU.** Naturality of `ω`: for a map `φ : K₀ ⟶ L₀` of bounded above complexes
> covered by a morphism of flat lifts, the square formed by `ω(K₀)`, `ω(L₀)` and the maps induced
> by `φ` commutes.

```lean
theorem obstructionMap_natural :
    DerivedCategory.Q.map φ ≫ obstructionMap D TM =
      obstructionMap D TL ≫
        (CategoryTheory.shiftFunctor (DerivedCategory (SheafMod O₀)) (2 : ℤ)).map
          (D.functor.map (DerivedCategory.Q.map φ))
```

**`Deformation.ComplexLift.obstructionMap_eq_of_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureClass.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureClass.lean#L512). The attribute's comment: “variant: independence of the flat lift at a supplied derived ideal tensor datum D; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU.** Two flat lifts of the same complex joined by a morphism of lifts over the
> identity give the same map `ω(K₀)`. Together with the existence of a lift receiving maps from
> any two, this is the independence of `ω` of the lift, hence its canonicality.

```lean
theorem obstructionMap_eq_of_hom {L M : FlatLift f K₀} (h : FlatLiftHom L M (𝟙 K₀))
    (TL : IdealKernel S L) (TM : IdealKernel S M)
    (hemb : ∀ n : ℤ, (restrict f).map (((idealTensorFunctor O₀ I).map h.red).f n) ≫
      TM.emb n = TL.emb n ≫ h.hom n) :
    obstructionMap D TL = obstructionMap D TM
```

**`Deformation.ComplexLift.tensorOmega`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureClassDerivedTensor.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureClassDerivedTensor.lean#L268). The attribute's comment: “the canonical map ω(K₀) : K₀ ⟶ (K₀ ⊗^L I)[2], on a bounded above complex”.

> **The map `ω(K₀) : K₀ ⟶ (K₀ ⊗^L_{O₀} I)[2]` of a bounded above complex.** It is the curvature
> class of a bounded above flat lift of `K₀` (Tag 0DIT), read through the canonical identification
> of the ideal part of the lift with the kernel of its reduction; by
> `Deformation.ComplexLift.tensorObstruction_eq_of_lift` it does not depend on the lift.

```lean
def tensorOmega (hf : Sheaf.IsLocallySurjective f) (S : SquareZeroIdeal f I)
    (K₀ : CochainComplex (SheafMod O₀) ℤ)
    (hK : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (K₀.homology n)) :
    DerivedCategory.Q.obj K₀ ⟶
      ((derivedTensorRight.{d} I).obj (DerivedCategory.Q.obj K₀))⟦(2 : ℤ)⟧
```

**`Deformation.ComplexLift.tensorOmega_natural_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureClassDerivedTensor.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureClassDerivedTensor.lean#L303). The attribute's comment: “naturality of ω, on bounded above complexes”.

> **Naturality of `ω` along an arbitrary morphism of `D(O₀)`** between bounded above
> complexes: such a morphism is a roof `K₀ ⟶ M ⟵ L₀` of maps of complexes with the second leg a
> quasi-isomorphism, and `ω` is natural along both legs.

```lean
theorem tensorOmega_natural_derived (hf : Sheaf.IsLocallySurjective f) (S : SquareZeroIdeal f I)
    {K₀ L₀ : CochainComplex (SheafMod O₀) ℤ}
    (hK : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (K₀.homology n))
    (hL : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (L₀.homology n))
    (ψ : DerivedCategory.Q.obj K₀ ⟶ DerivedCategory.Q.obj L₀) :
    ψ ≫ tensorOmega.{v, u, w, d} hf S L₀ hL =
      tensorOmega.{v, u, w, d} hf S K₀ hK ≫
        (CategoryTheory.shiftFunctor (DerivedCategory (SheafMod O₀)) (2 : ℤ)).map
          ((derivedTensorRight.{d} I).map ψ)
```

**`Deformation.ComplexLift.tensorOmegaObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureClassDerivedTensor.lean, line 349](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureClassDerivedTensor.lean#L349). The attribute's comment: “the canonical map ω(K₀) : K₀ ⟶ (K₀ ⊗^L I)[2], on an object with bounded above cohomology”.

> **Stacks 0DIU.** Let `f : O ⟶ O₀` be a surjection of sheaves of commutative rings on a site
> whose kernel is an ideal sheaf `I` of square zero (`S`). For every object `K₀` of `D⁻(O₀)` --
> an object of `D(O₀)` whose cohomology vanishes in all sufficiently large degrees -- this is the
> canonical map
>
> `ω(K₀) : K₀ ⟶ (K₀ ⊗^L_{O₀} I)[2]`
>
> in `D(O₀)`: it is `Deformation.ComplexLift.tensorOmega` on a complex representing `K₀`, the
> curvature of the lifted differential of a bounded above flat lift.

```lean
def tensorOmegaObj (hf : Sheaf.IsLocallySurjective f) (S : SquareZeroIdeal f I)
    (X : DerivedCategory (SheafMod O₀))
    (hX : ∃ N : ℤ, ∀ n : ℤ, N ≤ n →
      IsZero ((DerivedCategory.homologyFunctor (SheafMod O₀) n).obj X)) :
    X ⟶ ((derivedTensorRight.{d} I).obj X)⟦(2 : ℤ)⟧
```

**`Deformation.ComplexLift.tensorOmegaObj_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureClassDerivedTensor.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureClassDerivedTensor.lean#L365). The attribute's comment: “naturality of ω, on objects with bounded above cohomology”.

> **Stacks 0DIU, naturality of `ω`.** For every map `ψ : K₀ ⟶ L₀` in `D⁻(O₀)` the square
>
> `ω(L₀) ∘ ψ = (ψ ⊗^L I)[2] ∘ ω(K₀)`
>
> commutes.

```lean
theorem tensorOmegaObj_natural (hf : Sheaf.IsLocallySurjective f) (S : SquareZeroIdeal f I)
    {X Y : DerivedCategory (SheafMod O₀)}
    (hX : ∃ N : ℤ, ∀ n : ℤ, N ≤ n →
      IsZero ((DerivedCategory.homologyFunctor (SheafMod O₀) n).obj X))
    (hY : ∃ N : ℤ, ∀ n : ℤ, N ≤ n →
      IsZero ((DerivedCategory.homologyFunctor (SheafMod O₀) n).obj Y))
    (ψ : X ⟶ Y) :
    ψ ≫ tensorOmegaObj.{v, u, w, d} hf S Y hY =
      tensorOmegaObj.{v, u, w, d} hf S X hX ≫
        (CategoryTheory.shiftFunctor (DerivedCategory (SheafMod O₀)) (2 : ℤ)).map
          ((derivedTensorRight.{d} I).map ψ)
```

**`Deformation.ComplexLift.tensorOmegaMinus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureClassDerivedTensor.lean, line 407](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureClassDerivedTensor.lean#L407). The attribute's comment: “the canonical map ω(K₀) : K₀ ⟶ (K₀ ⊗^L I)[2] for every K₀ in D⁻(O₀)”.

> **Stacks 0DIU.** Let `f : O ⟶ O₀` be a surjection of sheaves of commutative rings on a site
> whose kernel is an ideal sheaf `I` of square zero (`S`). For every object `K₀` of `D⁻(O₀)` there
> is a canonical map
>
> `ω(K₀) : K₀ ⟶ (K₀ ⊗^L_{O₀} I)[2]`
>
> in `D(O₀)`, where `- ⊗^L_{O₀} I` is `Deformation.ComplexLift.derivedTensorRight I`. On a complex
> representing `K₀` it is the curvature `d ∘ d` of the lifted differential of a bounded above flat
> lift; its naturality is `Deformation.ComplexLift.tensorOmegaMinus_natural`.

```lean
def tensorOmegaMinus (hf : Sheaf.IsLocallySurjective f) (S : SquareZeroIdeal f I)
    (K₀ : DerivedCategory.Minus (SheafMod O₀)) :
    K₀.obj ⟶ ((derivedTensorRight.{d} I).obj K₀.obj)⟦(2 : ℤ)⟧
```

**`Deformation.ComplexLift.tensorOmegaMinus_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureClassDerivedTensor.lean, line 418](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureClassDerivedTensor.lean#L418). The attribute's comment: “naturality of ω along every map K₀ ⟶ L₀ in D⁻(O₀)”.

> **Stacks 0DIU, naturality of `ω`.** For every map `ψ : K₀ ⟶ L₀` in `D⁻(O₀)` the square
>
> `ω(L₀) ∘ ψ = (ψ ⊗^L I)[2] ∘ ω(K₀)`
>
> in `D(O₀)` commutes.

```lean
theorem tensorOmegaMinus_natural (hf : Sheaf.IsLocallySurjective f) (S : SquareZeroIdeal f I)
    {K₀ L₀ : DerivedCategory.Minus (SheafMod O₀)} (ψ : K₀.obj ⟶ L₀.obj) :
    ψ ≫ tensorOmegaMinus.{v, u, w, d} hf S L₀ =
      tensorOmegaMinus.{v, u, w, d} hf S K₀ ≫
        (CategoryTheory.shiftFunctor (DerivedCategory (SheafMod O₀)) (2 : ℤ)).map
          ((derivedTensorRight.{d} I).map ψ)
```

**`Deformation.ComplexLift.emb_coherence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureKernelCoherence.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureKernelCoherence.lean#L185). The attribute's comment: “variant: a morphism of flat lifts carries the kernel identification to the kernel identification, a step of the proof; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU, coherence of the kernel identifications.** A morphism of flat lifts carries
> the identification of the ideal part of the source to that of the target. This is the hypothesis
> `hemb` of `Deformation.ComplexLift.obstructionMap_natural` and of
> `Deformation.ComplexLift.obstructionMap_eq_of_hom`, and it holds for *every* pair of
> identifications, because both are normalized by the same pure-tensor formula
> `Deformation.ComplexLift.IdealKernel.emb_tmul`.

```lean
theorem emb_coherence (hf : Sheaf.IsLocallySurjective f)
    {L : FlatLift f K₀} {M : FlatLift f L₀} {φ : K₀ ⟶ L₀} (h : FlatLiftHom L M φ)
    (TL : IdealKernel S L) (TM : IdealKernel S M) (n : ℤ) :
    (restrict f).map (((idealTensorFunctor O₀ I).map h.red).f n) ≫ TM.emb n =
      TL.emb n ≫ h.hom n
```

**`Deformation.ComplexLift.obstructionMap_eq_of_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureKernelCoherence.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureKernelCoherence.lean#L262). The attribute's comment: “variant: ω depends on the complex alone at a supplied derived ideal tensor datum D; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU, `ω(K₀)` does not depend on the flat lift.** Given a kernel identification on
> every bounded above flat lift of `K₀` -- no compatibility between them assumed, since
> `Deformation.ComplexLift.emb_coherence` supplies it -- the map `ω(K₀)` computed from any two
> flat lifts is the same. The comparison that forces the agreement is
> `Deformation.ComplexLift.exists_flatLiftHom_pair`, Stacks 0DIT applied to the direct sum of the
> two lifted families.

```lean
theorem obstructionMap_eq_of_lift (hf : Sheaf.IsLocallySurjective f)
    (hK : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (K₀.homology n))
    (kern : ∀ M : FlatLift f K₀, IdealKernel S M) (L L' : FlatLift f K₀) :
    obstructionMap D (kern L) = obstructionMap D (kern L')
```

**`Deformation.ComplexLift.exists_flatLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean#L139). The attribute's comment: “variant: existence of a flat lift of a bounded above complex, a step of the proof; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU, existence of a flat lift.** A complex of `O₀`-modules whose cohomology
> vanishes in sufficiently high degrees admits a bounded above flat lift across a locally
> surjective `f : O ⟶ O₀`.

```lean
theorem exists_flatLift (hf : Sheaf.IsLocallySurjective f)
    (K₀ : CochainComplex (SheafMod O₀) ℤ)
    (hK : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (K₀.homology n)) :
    Nonempty (FlatLift f K₀)
```

**`Deformation.ComplexLift.exists_flatLiftHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean#L225). The attribute's comment: “variant: lifting a map of complexes to the flat lifts, a step of the proof; the tag is Deformation.ComplexLift.tensorOmegaMinus\_natural”.

> **Stacks 0DIU, lifting a map of complexes.** A map `φ : K₀ ⟶ L₀` of complexes of
> `O₀`-modules, with the cohomology of `L₀` vanishing in sufficiently high degrees, is covered by
> a morphism of flat lifts out of any given bounded above flat lift of `K₀`.

```lean
theorem exists_flatLiftHom (hf : Sheaf.IsLocallySurjective f)
    (L : FlatLift f K₀) (φ : K₀ ⟶ L₀)
    (hL₀ : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (L₀.homology n)) :
    ∃ M : FlatLift f L₀, Nonempty (FlatLiftHom L M φ)
```

**`Deformation.ComplexLift.exists_flatLiftHom_pair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean#L440). The attribute's comment: “variant: two flat lifts of a complex map to a common flat lift, a step of the proof; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU, a common enlargement of two flat lifts.** Two bounded above flat lifts of
> the same complex both map to a third one, over the identity. This is the comparison that the
> well-definedness of the canonical class rests on; it is Stacks 0DIT applied to the direct sum
> of the two lifted families.

```lean
theorem exists_flatLiftHom_pair (hf : Sheaf.IsLocallySurjective f)
    (hK : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (K₀.homology n)) :
    ∃ M : FlatLift f K₀,
      Nonempty (FlatLiftHom L M (𝟙 K₀)) ∧ Nonempty (FlatLiftHom L' M (𝟙 K₀))
```

**`Deformation.ComplexLift.exists_flatLift_of_isLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean#L488). The attribute's comment: “variant: a flat lift of a derived object with bounded above cohomology, a step of the proof; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU, a flat lift for an object of the derived category.** An object of `D(O₀)`
> with no cohomology above `b` is represented by a complex of `O₀`-modules carrying a bounded
> above flat lift across a locally surjective `f : O ⟶ O₀`.

```lean
theorem exists_flatLift_of_isLE (hf : Sheaf.IsLocallySurjective f) (b : ℤ)
    (E : DerivedCategory (SheafMod O₀)) [E.IsLE b] :
    ∃ K₀ : CochainComplex (SheafMod O₀) ℤ,
      Nonempty (DerivedCategory.Q.obj K₀ ≅ E) ∧ Nonempty (FlatLift f K₀)
```

**`Deformation.ComplexLift.exists_flatLift_of_minus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean, line 500](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean#L500). The attribute's comment: “variant: a flat lift of a bounded above derived object, a step of the proof; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU, a flat lift for a bounded above object.** Every object of `D⁻(O₀)` is
> represented by a complex carrying a bounded above flat lift.

```lean
theorem exists_flatLift_of_minus (hf : Sheaf.IsLocallySurjective f)
    (E : DerivedCategory.Minus (SheafMod O₀)) :
    ∃ K₀ : CochainComplex (SheafMod O₀) ℤ,
      Nonempty (DerivedCategory.Q.obj K₀ ≅ E.obj) ∧ Nonempty (FlatLift f K₀)
```

**`Deformation.ComplexLift.obstructionMap_eq_of_common_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean, line 521](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean#L521). The attribute's comment: “variant: independence of ω of the flat lift through a common enlargement at a supplied derived ideal tensor datum D; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU, independence of the flat lift.** Two flat lifts of the same complex that
> both map to a third one, compatibly with the kernel identifications, give the same canonical
> map `ω(K₀)`.

```lean
theorem obstructionMap_eq_of_common_lift {L L' M : FlatLift f K₀}
    (h : FlatLiftHom L M (𝟙 K₀)) (h' : FlatLiftHom L' M (𝟙 K₀))
    (TL : IdealKernel S L) (TL' : IdealKernel S L') (TM : IdealKernel S M)
    (hemb : ∀ n : ℤ, (restrict f).map (((idealTensorFunctor O₀ I).map h.red).f n) ≫ TM.emb n =
      TL.emb n ≫ h.hom n)
    (hemb' : ∀ n : ℤ, (restrict f).map (((idealTensorFunctor O₀ I).map h'.red).f n) ≫ TM.emb n =
      TL'.emb n ≫ h'.hom n) :
    obstructionMap D TL = obstructionMap D TL'
```

**`Deformation.ComplexLift.obstructionMap_eq_of_coherentKernels`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean, line 542](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/CurvatureLiftExistence.lean#L542). The attribute's comment: “variant: ω depends only on the complex at a supplied derived ideal tensor datum D; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU, the canonical map does not depend on the flat lift.** Suppose every bounded
> above flat lift of `K₀` carries a kernel identification, and that these are carried to one
> another by every morphism of flat lifts over the identity -- which is the assertion that the
> identifications are the canonical ones, normalized by the pure-tensor formula of
> `Deformation.ComplexLift.IdealKernel.emb_tmul`. Then the map `ω(K₀)` computed from any two
> flat lifts of `K₀` is the same, so `ω(K₀)` depends on `K₀` alone.
>
> The common enlargement that forces the agreement is `exists_flatLiftHom_pair`, Stacks 0DIT
> applied to the direct sum of the two lifted families.

```lean
theorem obstructionMap_eq_of_coherentKernels (hf : Sheaf.IsLocallySurjective f)
    (hK : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (K₀.homology n))
    (kern : ∀ M : FlatLift f K₀, IdealKernel S M)
    (hcoh : ∀ {A B : FlatLift f K₀} (h : FlatLiftHom A B (𝟙 K₀)) (n : ℤ),
      (restrict f).map (((idealTensorFunctor O₀ I).map h.red).f n) ≫ (kern B).emb n =
        (kern A).emb n ≫ h.hom n)
    (L L' : FlatLift f K₀) :
    obstructionMap D (kern L) = obstructionMap D (kern L')
```

**`Deformation.ComplexLift.nonempty_idealKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/IdealKernelExistence.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/IdealKernelExistence.lean#L379). The attribute's comment: “variant: the ideal part of a flat lift is the kernel of its reduction, a step of the proof; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU.** Every bounded above flat lift carries an identification of its ideal part
> with the kernel of its reduction, normalized by the pure-tensor formula `x̄ ⊗ a ↦ a · x`.
>
> The identification is `Deformation.ComplexLift.idealKernel`; this is its existence statement,
> which is what the independence argument consumes.

```lean
theorem nonempty_idealKernel (hf : Sheaf.IsLocallySurjective f) (S : SquareZeroIdeal f I)
    (L : FlatLift f K₀) : Nonempty (IdealKernel S L)
```

**`Deformation.ComplexLift.obstructionMap_eq_of_lift'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/IdealKernelExistence.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/IdealKernelExistence.lean#L448). The attribute's comment: “variant: independence of the flat lift at a supplied derived ideal tensor datum D; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU, `ω(K₀)` depends on the complex alone.** Any two bounded above flat lifts of
> `K₀`, with any kernel identifications on them, compute the same map.

```lean
theorem obstructionMap_eq_of_lift' (hf : Sheaf.IsLocallySurjective f)
    (S : SquareZeroIdeal f I) (D : DerivedIdealTensor I)
    {K₀ : CochainComplex (SheafMod O₀) ℤ}
    (hK : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (K₀.homology n))
    {L L' : FlatLift f K₀} (T : IdealKernel S L) (T' : IdealKernel S L') :
    obstructionMap D T = obstructionMap D T'
```

**`Deformation.ComplexLift.omega`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/IdealKernelExistence.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/IdealKernelExistence.lean#L473). The attribute's comment: “variant: the map ω(K₀) of a bounded above complex at a supplied derived ideal tensor datum D; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU.** The canonical map `ω(K₀) : K₀ ⟶ (K₀ ⊗^L_{O₀} I)[2]` attached to a
> square-zero extension `f : O ⟶ O₀` of sheaves of rings with ideal sheaf `I`, as a function of
> the bounded above complex `K₀` alone: it is the curvature of the lifted differential of any
> bounded above flat lift of `K₀`, read through the canonical identification of the ideal part of
> that lift with the kernel of its reduction.
>
> The kernel identification is not chosen: it is `Deformation.ComplexLift.idealKernel`, built
> from the lift. The lift itself is chosen -- `Deformation.ComplexLift.exists_flatLift` -- and
> that is irreducible here, because the bound the lifting construction is indexed by is available
> only inside the propositional hypothesis `hK`. That the choice does not matter is
> `Deformation.ComplexLift.obstructionMap_eq_of_lift'`, and `Deformation.ComplexLift.omega_eq`
> computes `ω(K₀)` from any lift and any kernel identification, so nothing about `ω(K₀)` is
> hidden by it.

```lean
def omega (hf : Sheaf.IsLocallySurjective f) (S : SquareZeroIdeal f I)
    (D : DerivedIdealTensor I) (K₀ : CochainComplex (SheafMod O₀) ℤ)
    (hK : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (K₀.homology n)) :
    DerivedCategory.Q.obj K₀ ⟶ (D.functor.obj (DerivedCategory.Q.obj K₀))⟦(2 : ℤ)⟧
```

**`Deformation.ComplexLift.omega_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/IdealKernelExistence.lean, line 483](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/IdealKernelExistence.lean#L483). The attribute's comment: “variant: ω is computed by any flat lift at a supplied derived ideal tensor datum D; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU.** The canonical map is computed by *any* bounded above flat lift and any
> kernel identification on it.

```lean
theorem omega_eq (hf : Sheaf.IsLocallySurjective f) (S : SquareZeroIdeal f I)
    (D : DerivedIdealTensor I) {K₀ : CochainComplex (SheafMod O₀) ℤ}
    (hK : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (K₀.homology n))
    {L : FlatLift f K₀} (T : IdealKernel S L) :
    omega hf S D K₀ hK = obstructionMap D T
```

**`Deformation.ComplexLift.omega_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/IdealKernelExistence.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/IdealKernelExistence.lean#L497). The attribute's comment: “variant: naturality of ω along a map of complexes at a supplied derived ideal tensor datum D; the tag is Deformation.ComplexLift.tensorOmegaMinus\_natural”.

> **Stacks 0DIU, naturality of `ω`.** For a map `φ : K₀ ⟶ L₀` of bounded above complexes of
> `O₀`-modules the square formed by `ω(K₀)`, `ω(L₀)` and the maps induced by `φ` commutes. No
> compatibility of lifts is assumed: the lift of `φ` is
> `Deformation.ComplexLift.exists_flatLiftHom` and the lift-independence is
> `Deformation.ComplexLift.omega_eq`.

```lean
theorem omega_natural (hf : Sheaf.IsLocallySurjective f) (S : SquareZeroIdeal f I)
    (D : DerivedIdealTensor I) {K₀ L₀ : CochainComplex (SheafMod O₀) ℤ} (φ : K₀ ⟶ L₀)
    (hK : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (K₀.homology n))
    (hL : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (L₀.homology n)) :
    DerivedCategory.Q.map φ ≫ omega hf S D L₀ hL =
      omega hf S D K₀ hK ≫
        (CategoryTheory.shiftFunctor (DerivedCategory (SheafMod O₀)) (2 : ℤ)).map
          (D.functor.map (DerivedCategory.Q.map φ))
```

**`Deformation.ComplexLift.omega_natural_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/IdealKernelExistence.lean, line 521](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/IdealKernelExistence.lean#L521). The attribute's comment: “variant: naturality of ω along a derived map at a supplied derived ideal tensor datum D; the tag is Deformation.ComplexLift.tensorOmegaMinus\_natural”.

> **Stacks 0DIU, naturality of `ω` for an arbitrary morphism of the derived category.** For
> any `ψ : K₀ ⟶ L₀` in `D(O₀)` between bounded above complexes -- not merely one coming from a map
> of complexes -- the square formed by `ω(K₀)`, `ω(L₀)` and the maps induced by `ψ` commutes.
>
> Every such `ψ` is a roof `K₀ ⟶ M ⟵ L₀` of maps of complexes with the second leg a
> quasi-isomorphism (`Deformation.ComplexLift.exists_roof_of_derived_hom`), so this follows from
> naturality along maps of complexes applied to the two legs.

```lean
theorem omega_natural_derived (hf : Sheaf.IsLocallySurjective f) (S : SquareZeroIdeal f I)
    (D : DerivedIdealTensor I) {K₀ L₀ : CochainComplex (SheafMod O₀) ℤ}
    (hK : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (K₀.homology n))
    (hL : ∃ N : ℤ, ∀ n : ℤ, N ≤ n → IsZero (L₀.homology n))
    (ψ : DerivedCategory.Q.obj K₀ ⟶ DerivedCategory.Q.obj L₀) :
    ψ ≫ omega hf S D L₀ hL =
      omega hf S D K₀ hK ≫
        (CategoryTheory.shiftFunctor (DerivedCategory (SheafMod O₀)) (2 : ℤ)).map
          (D.functor.map ψ)
```

**`Deformation.ComplexLift.obstructionMap_eq_of_hom'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/IdealKernelNaturality.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/IdealKernelNaturality.lean#L188). The attribute's comment: “variant: independence of the flat lift at a supplied derived ideal tensor datum D; the tag is Deformation.ComplexLift.tensorOmegaMinus”.

> **Stacks 0DIU.** Two flat lifts of the same complex joined by a morphism of flat lifts over
> the identity give the same canonical class `ω(K₀)`. No compatibility of the ideal parts is
> assumed: it is automatic.

```lean
theorem obstructionMap_eq_of_hom' [HasDerivedCategory.{d} (SheafMod O₀)]
    (D : DerivedIdealTensor I) (hf : Sheaf.IsLocallySurjective f) {L M : FlatLift f K₀}
    (h : FlatLiftHom L M (𝟙 K₀)) (TL : IdealKernel S L) (TM : IdealKernel S M) :
    obstructionMap D TL = obstructionMap D TM
```

## Tag 0DIV, a lemma

[Tag 0DIV](https://stacks.math.columbia.edu/tag/0DIV) in the Stacks Project.

**`Stacks.DerivedTensor.RingedSite.isIso_homologyMap_derivedTensorSingle_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CohomologyAboveADegree.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CohomologyAboveADegree.lean#L132). The attribute's comment: “tensoring keeps the isomorphisms above the degree”.

> **Stacks 0DIV (2), the isomorphisms.** If `H^i(α)` is an isomorphism in every degree `> n`
> and a surjection in degree `n`, then `H^i(α ⊗_O^{L} 1_F)` is an isomorphism in every degree
> `> n`.

```lean
theorem isIso_homologyMap_derivedTensorSingle_of_epi
    {K L : DerivedModules R} (α : K ⟶ L) (F : Modules R) (n : ℤ)
    (hiso : ∀ i : ℤ, n < i → IsIso ((DerivedCategory.homologyFunctor (Modules R) i).map α))
    (hepi : Epi ((DerivedCategory.homologyFunctor (Modules R) n).map α))
    (i : ℤ) (hi : n < i) :
    IsIso ((DerivedCategory.homologyFunctor (Modules R) i).map
      ((derivedTensorSingle R F).map α))
```

**`Stacks.DerivedTensor.RingedSite.epi_homologyMap_derivedTensorSingle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CohomologyAboveADegree.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CohomologyAboveADegree.lean#L144). The attribute's comment: “tensoring keeps the surjection in the degree”.

> **Stacks 0DIV (2), the surjection.** If `H^i(α)` is an isomorphism in every degree `> n`
> and a surjection in degree `n`, then `H^n(α ⊗_O^{L} 1_F)` is a surjection.

```lean
theorem epi_homologyMap_derivedTensorSingle
    {K L : DerivedModules R} (α : K ⟶ L) (F : Modules R) (n : ℤ)
    (hiso : ∀ i : ℤ, n < i → IsIso ((DerivedCategory.homologyFunctor (Modules R) i).map α))
    (hepi : Epi ((DerivedCategory.homologyFunctor (Modules R) n).map α)) :
    Epi ((DerivedCategory.homologyFunctor (Modules R) n).map
      ((derivedTensorSingle R F).map α))
```

**`Stacks.DerivedTensor.RingedSite.isIso_homologyMap_derivedTensorSingle_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CohomologyAboveADegree.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/CohomologyAboveADegree.lean#L163). The attribute's comment: “tensoring keeps the isomorphisms in all degrees at least the bound”.

> **Stacks 0DIV (1).** If `H^i(α)` is an isomorphism in every degree `≥ n`, then so is
> `H^i(α ⊗_O^{L} 1_F)`.
>
> Above `n` this is part (2). In degree `n` surjectivity is again part (2), and injectivity comes
> from the vanishing of the connecting map `H^{n-1}(C ⊗^{L} F) ⟶ H^n(K ⊗^{L} F)` of the tensored
> triangle, equivalently from surjectivity of `H^{n-1}(L ⊗^{L} F) ⟶ H^{n-1}(C ⊗^{L} F)`. That is
> part (2) applied in degree `n - 1` to `τ^{<n} L ⟶ L ⟶ C`: this composite is surjective on
> `H^{n-1}` — the truncation map is an isomorphism there and `H^{n-1}(L) ⟶ H^{n-1}(C)` is
> surjective because `H^n(α)` is injective — and it is an isomorphism on cohomology above
> `n - 1` for the trivial reason that both its source and its target vanish there.

```lean
theorem isIso_homologyMap_derivedTensorSingle_of_isIso
    {K L : DerivedModules R} (α : K ⟶ L) (F : Modules R) (n : ℤ)
    (hα : ∀ i : ℤ, n ≤ i → IsIso ((DerivedCategory.homologyFunctor (Modules R) i).map α))
    (i : ℤ) (hi : n ≤ i) :
    IsIso ((DerivedCategory.homologyFunctor (Modules R) i).map
      ((derivedTensorSingle R F).map α))
```

## Tag 0DIW, a lemma

[Tag 0DIW](https://stacks.math.columbia.edu/tag/0DIW) in the Stacks Project.

**`Deformation.ComplexLift.tensorOmegaMinus_eq_zero_iff_nonempty_derivedLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ObstructionLiftCriterionDerivedTensor.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/ObstructionLiftCriterionDerivedTensor.lean#L205). The attribute's comment: “ω is the class tensorOmegaMinus with values in the derived tensor product K₀ ⊗^L I, and K ⊗^L O₀ the derived base change derivedExtensionOfScalarsData; no flatness on I”.

> **Stacks 0DIW.** Let `C` be a site and `f : O ⟶ O₀` a surjection of sheaves of commutative
> rings whose kernel is an ideal sheaf `I` of square zero (`S`), with no further hypothesis on
> `I`. For every object `K₀` of `D⁻(O₀)` the following are equivalent:
>
> 1. the canonical class `ω(K₀) : K₀ ⟶ (K₀ ⊗^L_{O₀} I)[2]` of Tag 0DIU,
>    `Deformation.ComplexLift.tensorOmegaMinus`, is zero;
> 2. there exists `K ∈ D⁻(O)` with `K ⊗^L_O O₀ ≅ K₀` in `D(O₀)`.
>
> Here `- ⊗^L_{O₀} I` is the derived tensor product `Deformation.ComplexLift.derivedTensorRight I`
> and `- ⊗^L_O O₀` the derived base change `Deformation.ComplexLift.derivedExtensionOfScalarsData`,
> both constructed from flat resolutions (Tag 0794).

```lean
theorem tensorOmegaMinus_eq_zero_iff_nonempty_derivedLift (hf : Sheaf.IsLocallySurjective f)
    (S : SquareZeroIdeal f I) (E : DerivedCategory.Minus (SheafMod O₀)) :
    tensorOmegaMinus.{v, u, w, d₀} hf S E = 0 ↔
      Nonempty (DerivedLift (derivedExtensionOfScalarsData.{d, d₀} f) E)
```

## Tag 0DIX, a lemma

[Tag 0DIX](https://stacks.math.columbia.edu/tag/0DIX) in the Stacks Project.

**`Deformation.ComplexLift.exists_quasiIso_with_extensionOfScalars_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ComplexMapLift.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/ComplexMapLift.lean#L316).

> A quasi-isomorphism to the extension of scalars of `F` can be lifted, after
> replacing `F` by a quasi-isomorphic complex, to a factorization in the
> homotopy category.

```lean
theorem exists_quasiIso_with_extensionOfScalars_factorization
    [HasSheafify J AddCommGrpCat.{u}]
    [J.WEqualsLocallyBijective AddCommGrpCat.{u}]
    [Epi f]
    (F : CochainComplex (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (O)))) ℤ)
    (K₀ : CochainComplex (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (O₀)))) ℤ)
    (q : K₀ ⟶ (extensionOfScalarsCochainComplex J f).obj F)
    (hq : QuasiIso q) :
    ∃ (G : CochainComplex (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (O)))) ℤ)
      (g : G ⟶ F),
      QuasiIso g ∧
    (∃ h :
          (HomotopyCategory.quotient
              (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (O₀))))
              (ComplexShape.up ℤ)).obj
                ((extensionOfScalarsCochainComplex J f).obj G) ⟶
            (HomotopyCategory.quotient
                (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (O₀))))
              (ComplexShape.up ℤ)).obj K₀,
          (HomotopyCategory.quotient
              (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (O₀))))
                (ComplexShape.up ℤ)).map
              ((extensionOfScalarsCochainComplex J f).map g) =
            h ≫
              (HomotopyCategory.quotient
                  (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (O₀))))
                (ComplexShape.up ℤ)).map q)
```

## Tag 0DIY, a lemma

[Tag 0DIY](https://stacks.math.columbia.edu/tag/0DIY) in the Stacks Project.

**`Deformation.ComplexLift.DerivedReduction.liftObstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/DerivedLiftObstruction.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/DerivedLiftObstruction.lean#L142). The attribute's comment: “the obstruction class of a morphism of reductions”.

> **Stacks 0DIY.** The obstruction to lifting a morphism `α₀ : K₁ ⊗^L O₀ ⟶ K₂ ⊗^L O₀` of
> reductions to a morphism `K₁ ⟶ K₂`: the composite of the unit of the adjunction with `α₀` and
> the connecting morphism of the reduction triangle of `K₂`, a morphism
> `K₁ ⟶ (K₂ ⊗^L I)⟦1⟧`.

```lean
noncomputable def liftObstruction
    (K₁ K₂ : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (O)))))
    (α₀ : T.baseChange.obj K₁ ⟶ T.baseChange.obj K₂) :
    K₁ ⟶ (R.restriction.obj (idealTensor.obj (T.baseChange.obj K₂)))⟦(1 : ℤ)⟧
```

**`Deformation.ComplexLift.DerivedReduction.liftObstruction_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/DerivedLiftObstruction.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/DerivedLiftObstruction.lean#L155). The attribute's comment: “the vanishing criterion”.

> **Stacks 0DIY.** The obstruction class of `α₀` vanishes exactly when `α₀` is the derived
> base change of a morphism `K₁ ⟶ K₂`. The forward implication is exactness of `Hom(K₁, -)` at
> the third vertex of the reduction triangle of `K₂`, followed by the universal property of the
> unit; the converse is the vanishing of the composite of the last two morphisms of that
> triangle.

```lean
theorem liftObstruction_eq_zero_iff
    (K₁ K₂ : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (O)))))
    (α₀ : T.baseChange.obj K₁ ⟶ T.baseChange.obj K₂) :
    R.liftObstruction K₁ K₂ α₀ = 0 ↔ ∃ a : K₁ ⟶ K₂, T.baseChange.map a = α₀
```

**`Deformation.ComplexLift.DerivedReduction.extLiftObstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/DerivedLiftObstruction.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/DerivedLiftObstruction.lean#L212). The attribute's comment: “the obstruction class in Ext¹”.

> **Stacks 0DIY.** The obstruction class `o(α₀)` of a morphism `α₀ : K₀ ⟶ L₀` of reductions
> as an element of `Ext¹_{O₀}(K₀, L₀ ⊗^L_{O₀} I)`, the group the tag states it in:
> `Deformation.ComplexLift.DerivedReduction.liftObstruction` read through the adjunction.

```lean
noncomputable def extLiftObstruction
    (K₁ K₂ : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf O)))
    (α₀ : T.baseChange.obj K₁ ⟶ T.baseChange.obj K₂) :
    T.baseChange.obj K₁ ⟶ (idealTensor.obj (T.baseChange.obj K₂))⟦(1 : ℤ)⟧
```

**`Deformation.ComplexLift.DerivedReduction.extLiftObstruction_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/DerivedLiftObstruction.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/DerivedLiftObstruction.lean#L234). The attribute's comment: “the vanishing criterion in Ext¹”.

> **Stacks 0DIY.** The obstruction class in `Ext¹_{O₀}(K₀, L₀ ⊗^L_{O₀} I)` vanishes exactly
> when `α₀` is the derived base change of a morphism `K₁ ⟶ K₂`: the identification of that group
> with the group of morphisms `K₁ ⟶ ((L₀ ⊗^L_{O₀} I)|_O)⟦1⟧` is an isomorphism, so it reflects
> vanishing from `Deformation.ComplexLift.DerivedReduction.liftObstruction_eq_zero_iff`.

```lean
theorem extLiftObstruction_eq_zero_iff
    (K₁ K₂ : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf O)))
    (α₀ : T.baseChange.obj K₁ ⟶ T.baseChange.obj K₂) :
    R.extLiftObstruction K₁ K₂ α₀ = 0 ↔ ∃ a : K₁ ⟶ K₂, T.baseChange.map a = α₀
```

**`Deformation.ComplexLift.squareZeroObstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SquareZeroDerivedObstruction.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/SquareZeroDerivedObstruction.lean#L285). The attribute's comment: “the obstruction class o(α₀) in Ext¹\_\{O₀}(K₀, L₀ ⊗^L\_\{O₀} I)”.

> **Stacks 0DIY, the obstruction class.** Let `f : O ⟶ O₀` be a surjection of sheaves of
> commutative rings whose kernel `I` has square zero, let `K, L ∈ D⁻(O)`, and write
> `K₀ = K ⊗^L_O O₀`, `L₀ = L ⊗^L_O O₀` for their derived base changes. For a morphism
> `α₀ : K₀ ⟶ L₀` in `D(O₀)` this is the class
> `o(α₀) ∈ Ext¹_{O₀}(K₀, L₀ ⊗^L_{O₀} I) = Hom_{D(O₀)}(K₀, (L₀ ⊗^L_{O₀} I)⟦1⟧)`: the composite
> `K ⟶ K₀ ⟶ L₀ ⟶ (L ⊗^L_O I)⟦1⟧` of the unit, `α₀` and the connecting morphism of the reduction
> triangle of `L`, read through the adjunction.

```lean
def squareZeroObstruction
    (K L : DerivedCategory.Minus (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf O)))
    (α₀ : (derivedExtensionOfScalars.{d, d₀} f).obj K.obj ⟶
      (derivedExtensionOfScalars.{d, d₀} f).obj L.obj) :
    (derivedExtensionOfScalars.{d, d₀} f).obj K.obj ⟶
      ((derivedTensorRight.{d₀, u, u, u'} (squareZeroIdeal.{u, u, u'} f hf hsq)).obj
        ((derivedExtensionOfScalars.{d, d₀} f).obj L.obj))⟦(1 : ℤ)⟧
```

**`Deformation.ComplexLift.squareZeroObstruction_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SquareZeroDerivedObstruction.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/SquareZeroDerivedObstruction.lean#L297). The attribute's comment: “o(α₀) = 0 iff α₀ = α ⊗^L\_O id for some α : K → L in D(O)”.

> **Stacks 0DIY.** The obstruction class `o(α₀)` vanishes if and only if `α₀` is the derived
> base change `α ⊗^L_O id` of a morphism `α : K ⟶ L` in `D(O)`.

```lean
theorem squareZeroObstruction_eq_zero_iff
    (K L : DerivedCategory.Minus (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf O)))
    (α₀ : (derivedExtensionOfScalars.{d, d₀} f).obj K.obj ⟶
      (derivedExtensionOfScalars.{d, d₀} f).obj L.obj) :
    squareZeroObstruction f hf hsq K L α₀ = 0 ↔
      ∃ α : K.obj ⟶ L.obj, (derivedExtensionOfScalars.{d, d₀} f).map α = α₀
```

**`Deformation.ComplexLift.squareZeroObstructionMinus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SquareZeroDerivedObstruction.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/SquareZeroDerivedObstruction.lean#L312). The attribute's comment: “the obstruction class o(α₀) in Ext¹\_\{O₀}(K₀, L₀ ⊗^L\_\{O₀} I), with K₀ and L₀ in D⁻(O₀)”.

> **Stacks 0DIY, the obstruction class, with `K₀` and `L₀` in `D⁻(O₀)`.** For `K, L ∈ D⁻(O)`
> the derived base changes `K₀ = K ⊗^L_O O₀` and `L₀ = L ⊗^L_O O₀` are bounded above
> (`Deformation.ComplexLift.DerivedExtensionOfScalars.baseChangeMinus`), and a morphism
> `α₀ : K₀ ⟶ L₀` of `D⁻(O₀)` has the class `o(α₀) ∈ Ext¹_{O₀}(K₀, L₀ ⊗^L_{O₀} I)` of
> `Deformation.ComplexLift.squareZeroObstruction`.

```lean
def squareZeroObstructionMinus
    (K L : DerivedCategory.Minus (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf O)))
    (α₀ : (derivedExtensionOfScalarsData.{d, d₀} f).baseChangeMinus.obj K ⟶
      (derivedExtensionOfScalarsData.{d, d₀} f).baseChangeMinus.obj L) :
    ((derivedExtensionOfScalarsData.{d, d₀} f).baseChangeMinus.obj K).obj ⟶
      ((derivedTensorRight.{d₀, u, u, u'} (squareZeroIdeal.{u, u, u'} f hf hsq)).obj
        ((derivedExtensionOfScalarsData.{d, d₀} f).baseChangeMinus.obj L).obj)⟦(1 : ℤ)⟧
```

**`Deformation.ComplexLift.squareZeroObstructionMinus_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SquareZeroDerivedObstruction.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/SquareZeroDerivedObstruction.lean#L326). The attribute's comment: “o(α₀) = 0 iff α₀ = α ⊗^L\_O id for some α : K → L, with K₀, L₀ in D⁻(O₀)”.

> **Stacks 0DIY, with `K₀` and `L₀` in `D⁻(O₀)`.** The obstruction class of a morphism
> `α₀ : K₀ ⟶ L₀` of `D⁻(O₀)` vanishes if and only if `α₀ = α ⊗^L_O id` for a morphism
> `α : K ⟶ L` of `D⁻(O)`, the functor `- ⊗^L_O O₀ : D⁻(O) ⥤ D⁻(O₀)` being
> `Deformation.ComplexLift.DerivedExtensionOfScalars.baseChangeMinus`.

```lean
theorem squareZeroObstructionMinus_eq_zero_iff
    (K L : DerivedCategory.Minus (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf O)))
    (α₀ : (derivedExtensionOfScalarsData.{d, d₀} f).baseChangeMinus.obj K ⟶
      (derivedExtensionOfScalarsData.{d, d₀} f).baseChangeMinus.obj L) :
    squareZeroObstructionMinus f hf hsq K L α₀ = 0 ↔
      ∃ α : K ⟶ L, (derivedExtensionOfScalarsData.{d, d₀} f).baseChangeMinus.map α = α₀
```

## Tag 0DIZ, a lemma

[Tag 0DIZ](https://stacks.math.columbia.edu/tag/0DIZ) in the Stacks Project.

**`Deformation.ComplexLift.DerivedLift`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/DerivedComplexLift.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/DerivedComplexLift.lean#L115). The attribute's comment: “a lift of a bounded above derived complex”.

> **Stacks 0DIZ.** A lift of a bounded above object `K₀` of the derived category of
> `O₀`-modules across the derived base change `T` along `f : O ⟶ O₀`: a bounded above object `K`
> of the derived category of `O`-modules together with an isomorphism
> `K ⊗_O^L O₀ ≅ K₀` in the derived category of `O₀`-modules.

```lean
structure DerivedLift (T : DerivedExtensionOfScalars f)
    (K₀ : DerivedCategory.Minus
      (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (O₀)))))
```

**`Deformation.ComplexLift.automorphismsOfLift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/DerivedLiftAutomorphisms.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/DerivedLiftAutomorphisms.lean#L137). The attribute's comment: “the automorphism group of a lift”.

> **Stacks 0DIZ.** The automorphisms of a lift `(K, α)` of `K₀`: the automorphisms of `K`
> whose derived base change is the identity. Since `α` is an isomorphism these are exactly the
> automorphisms of the pair, and the subgroup does not depend on `α`.

```lean
noncomputable def automorphismsOfLift (T : DerivedExtensionOfScalars f)
    {K₀ :
      DerivedCategory.Minus (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (O₀))))}
    (L : DerivedLift T K₀) : Subgroup (Aut L.K.obj)
```

**`Deformation.ComplexLift.boundary`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/DerivedLiftAutomorphisms.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/DerivedLiftAutomorphisms.lean#L319). The attribute's comment: “part (1): the map whose cokernel the automorphism group is”.

> **Stacks 0DIZ.** The canonical map `Ext⁻¹(K₀, K₀) ⟶ Hom(K₀, K₀ ⊗^L I)`: the connecting map
> of the reduction triangle of `K`, read in the two groups of the source through the adjunction
> and the identification `α`.

```lean
noncomputable def boundary :
    (K₀.obj ⟶ K₀.obj⟦(-1 : ℤ)⟧) →+ (K₀.obj ⟶ idealTensor.obj K₀.obj)
```

**`Deformation.ComplexLift.automorphismsOfLiftMulEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/DerivedLiftAutomorphisms.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/DerivedLiftAutomorphisms.lean#L382). The attribute's comment: “part (1): the automorphisms of a lift are a cokernel”.

> **Stacks 0DIZ (1).** The automorphisms of a lift `(K, α)` of `K₀` form the cokernel of the
> canonical map `Ext⁻¹(K₀, K₀) ⟶ Hom(K₀, K₀ ⊗^L I)`.

```lean
noncomputable def automorphismsOfLiftMulEquiv :
    Multiplicative (K₀.obj ⟶ idealTensor.obj K₀.obj) ⧸
        AddSubgroup.toSubgroup (boundary R L).range ≃* automorphismsOfLift T L
```

**`Deformation.ComplexLift.squareZeroFlatLiftBoundary`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SquareZeroLiftTorsor.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/SquareZeroLiftTorsor.lean#L79). The attribute's comment: “(1), the map Ext⁻¹(K₀, K₀) → Hom(K₀, K₀ ⊗^L I)”.

> **Stacks 0DIZ (1), the map.** For a lift `(K, α)` of `K₀ ∈ D⁻(O₀)` across the square-zero
> surjection `f`, the canonical map
>
> `Ext⁻¹_{O₀}(K₀, K₀) ⟶ Hom_{O₀}(K₀, K₀ ⊗^L_{O₀} I)`
>
> whose cokernel the automorphism group of `(K, α)` is: the connecting map of the reduction
> triangle `K ⊗^L_O I ⟶ K ⟶ K ⊗^L_O O₀ ⟶ (K ⊗^L_O I)⟦1⟧` of `f` (computed by a flat resolution),
> read through the adjunction between derived base change and restriction of scalars and
> through `α`.

```lean
def squareZeroFlatLiftBoundary (L : DerivedLift (derivedExtensionOfScalarsData.{d, d₀} f) K₀) :
    (K₀.obj ⟶ K₀.obj⟦(-1 : ℤ)⟧) →+
      (K₀.obj ⟶ (derivedTensorRight.{d₀} (squareZeroIdeal f hf hsq)).obj K₀.obj)
```

**`Deformation.ComplexLift.squareZeroFlatLiftAutEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SquareZeroLiftTorsor.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/SquareZeroLiftTorsor.lean#L91). The attribute's comment: “(1)”.

> **Stacks 0DIZ (1).** Let `f : O ⟶ O₀` be a surjection of sheaves of commutative rings on a
> site whose kernel `I` is an ideal of square zero, let `K₀ ∈ D⁻(O₀)` and let `(K, α)` be a lift
> of `K₀`, i.e. `K ∈ D⁻(O)` with `α : K ⊗^L_O O₀ ≅ K₀` in `D(O₀)`. Then the group of
> automorphisms of the pair `(K, α)` is canonically the cokernel of the map
> `Ext⁻¹_{O₀}(K₀, K₀) ⟶ Hom_{O₀}(K₀, K₀ ⊗^L_{O₀} I)` of
> `Deformation.ComplexLift.squareZeroFlatLiftBoundary`.

```lean
def squareZeroFlatLiftAutEquiv (L : DerivedLift (derivedExtensionOfScalarsData.{d, d₀} f) K₀) :
    Multiplicative (K₀.obj ⟶
        (derivedTensorRight.{d₀} (squareZeroIdeal f hf hsq)).obj K₀.obj) ⧸
        AddSubgroup.toSubgroup (squareZeroFlatLiftBoundary.{d, d₀} f hf hsq L).range ≃*
      automorphismsOfLift (derivedExtensionOfScalarsData.{d, d₀} f) L
```

**`Deformation.ComplexLift.exists_addTorsor_squareZeroLifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SquareZeroLiftTorsor.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/SquareZeroLiftTorsor.lean#L106). The attribute's comment: “(2)”.

> **Stacks 0DIZ (2).** Let `f : O ⟶ O₀` be a surjection of sheaves of commutative rings on a
> site whose kernel `I` is an ideal of square zero, and let `K₀ ∈ D⁻(O₀)`. If `K₀` has a lift
> `(K, α)`, `K ∈ D⁻(O)`, `α : K ⊗^L_O O₀ ≅ K₀`, then the set of isomorphism classes of lifts of
> `K₀` is principal homogeneous under `Ext¹_{O₀}(K₀, K₀ ⊗^L_{O₀} I)`: there is a free and
> transitive action of that group on it under which `ξ` carries the class of `(K', α')` to the
> class of `(K'', α'')` exactly when `ξ` is the obstruction class of Stacks 0DIY of the comparison
> `α'' ∘ α'⁻¹` of the two lifts.

```lean
theorem exists_addTorsor_squareZeroLifts
    [Nonempty (DerivedLift (derivedExtensionOfScalarsData.{d, d₀} f) K₀)] :
    ∃ τ : AddTorsor (K₀.obj ⟶
        ((derivedTensorRight.{d₀} (squareZeroIdeal f hf hsq)).obj K₀.obj)⟦(1 : ℤ)⟧)
        (Quotient (DerivedLift.setoid (T := derivedExtensionOfScalarsData.{d, d₀} f) (K₀ := K₀))),
      ∀ (ξ : K₀.obj ⟶ ((derivedTensorRight.{d₀} (squareZeroIdeal f hf hsq)).obj K₀.obj)⟦(1 : ℤ)⟧)
        (L' L'' : DerivedLift (derivedExtensionOfScalarsData.{d, d₀} f) K₀),
        τ.vadd ξ ⟦L'⟧ = ⟦L''⟧ ↔
          liftDifference (squareZeroFlatReduction.{d, d₀} f hf hsq) L'' L' = ξ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.16, Tag 0DIS](https://stacks.math.columbia.edu/tag/0DIS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
