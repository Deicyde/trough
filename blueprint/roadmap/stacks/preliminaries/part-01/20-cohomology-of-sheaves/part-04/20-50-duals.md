---
declaration: section
origin: cited
lean: Stacks.Cohomology.MonoidalComplexes.symmetricMonoidalComplexes, Stacks.SheafOfModules.OnSpace.exists_exactPairing_ihomUnit_of_isLocallyBounded, Stacks.SheafOfModules.Strict.isLocallyBounded_and_isLocallyDirectSummand_and_isoDualComplex_of_exactPairing, Stacks.SheafOfModules.derivedSheafHomEvaluation_isIso_of_isPerfect, Stacks.SheafOfModules.derivedBidualIso, Stacks.SheafOfModules.isIso_derivedBidualMap, Stacks.SheafOfModules.isPerfect_derivedDual, Stacks.SheafOfModules.isPerfect_derivedDual_of_isPerfectSpace
statement: formalized
proof: formalized
---

# 20.50 Duals

Section 20.50 of the Stacks Project, [Tag 0FP7](https://stacks.math.columbia.edu/tag/0FP7). 8 tags here are carried by 24 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FP8, a lemma

[Tag 0FP8](https://stacks.math.columbia.edu/tag/0FP8) in the Stacks Project.

**`Stacks.Cohomology.MonoidalComplexes.symmetricMonoidalComplexes`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/MonoidalStructure.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/MonoidalStructure.lean#L79). References: EGA 0 (4.1.5), “partial”.

> Complexes of modules on a ringed space form a symmetric monoidal category; its tensor
> bifunctor is the total complex of the sheafified degreewise tensor product and its unit is the
> structure sheaf in degree zero.  This is Tag 0FPQ at the ringed site of opens of `X`.

```lean
public def symmetricMonoidalComplexes :
    Stacks.Cohomology.MonoidalComplexesOfModules.SymmetricMonoidalComplexes X.sheaf
```

## Tag 0FP9, an example

[Tag 0FP9](https://stacks.math.columbia.edu/tag/0FP9) in the Stacks Project.

**`Stacks.SheafOfModules.OnSpace.exists_exactPairing_ihomUnit_of_isLocallyBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfect/LocallyBoundedDualComplex.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/StrictlyPerfect/LocallyBoundedDualComplex.lean#L162).

> **[Stacks, Tag 0FP9].**  Let `(X, 𝒪_X)` be a ringed space and `ℱ^•` a locally bounded
> complex of `𝒪_X`-modules each of whose terms `ℱ^n` is locally a direct summand of a finite free
> `𝒪_X`-module, and let `𝒢^• = Hom^•(ℱ^•, 𝒪_X)`.  Let `ηₙ : 𝒪_X ⟶ ℱ^n ⊗ 𝒢^{-n}` and
> `εₙ : 𝒢^{-n} ⊗ ℱ^n ⟶ 𝒪_X` be the coevaluation and evaluation of the duality between `ℱ^n` and
> `𝒢^{-n}`.  Then there is a left dual structure on `𝒢^•` over `ℱ^•` in the monoidal category of
> complexes of `𝒪_X`-modules whose coevaluation is `η = ∑ ηₙ` and whose evaluation is
> `ε = ∑ εₙ`: in degree zero, read through the identification of the degree zero term of the unit
> complex with `𝒪_X`, the component of `η` on the summand `ℱ^n ⊗ 𝒢^{-n}` of
> `Tot(ℱ^• ⊗ 𝒢^•)^0` is `ηₙ`, and the component of `ε` on the summand `𝒢^{-n} ⊗ ℱ^n` of
> `Tot(𝒢^• ⊗ ℱ^•)^0` is `εₙ`.  The structure is `exactPairingIhomUnitComplexOfIsLocallyBounded`.

```lean
theorem exists_exactPairing_ihomUnit_of_isLocallyBounded
    (F : CochainComplex (Strict.Mod X.sheaf) ℤ)
    (hb : IsLocallyBounded X F) (hF : ∀ n : ℤ, IsLocallyFiniteFreeSummand X (F.X n)) :
    letI : MonoidalCategory (_root_.SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf X.sheaf)) :=
      Stacks.SheafOfModules.Strict.monoidalCategory X.sheaf.obj
        (Stacks.SheafOfModules.Tensor.ringSheaf X.sheaf).property
    letI : MonoidalPreadditive (Strict.Mod X.sheaf) :=
      Strict.monoidalPreadditiveRingSheaf X.sheaf
    letI : ∀ X₁ X₂ : GradedObject ℤ (Strict.Mod X.sheaf), GradedObject.HasTensor X₁ X₂ :=
      fun _ _ => inferInstance
    letI := Strict.monoidalCategoryCochainComplex X.sheaf
    letI := Strict.monoidalClosedCochainComplex X.sheaf
    ∃ P : ExactPairing F ((ihom F).obj (𝟙_ (CochainComplex (Strict.Mod X.sheaf) ℤ))),
      (∀ n : ℤ, P.coevaluation'.f 0 ≫
          GradedObject.Monoidal.πTensorObj F.X
            ((ihom F).obj (𝟙_ (CochainComplex (Strict.Mod X.sheaf) ℤ))).X n (-n) 0
            (add_neg_cancel n) =
        ((HomologicalComplex.tensorUnitIso (Strict.Mod X.sheaf) (ComplexShape.up ℤ)).inv 0 ≫
            GradedObject.Monoidal.tensorUnit₀.hom) ≫
          (Strict.exactPairingIhomComplexX X.sheaf F n
            (isLocallyDirectSummandOfFiniteFree_of_isLocallyFiniteFreeSummand X (F.X n)
              (hF n))).coevaluation') ∧
      ∀ n : ℤ, HomologicalComplex.ιTensorObj
          ((ihom F).obj (𝟙_ (CochainComplex (Strict.Mod X.sheaf) ℤ))) F (-n) n 0
          (neg_add_cancel n) ≫ P.evaluation'.f 0 =
        (Strict.exactPairingIhomComplexX X.sheaf F n
            (isLocallyDirectSummandOfFiniteFree_of_isLocallyFiniteFreeSummand X (F.X n)
              (hF n))).evaluation' ≫
          GradedObject.Monoidal.tensorUnit₀.inv ≫
            (HomologicalComplex.tensorUnitIso (Strict.Mod X.sheaf) (ComplexShape.up ℤ)).hom 0
```

## Tag 0FPA, a lemma

[Tag 0FPA](https://stacks.math.columbia.edu/tag/0FPA) in the Stacks Project.

**`Stacks.SheafOfModules.Strict.isLocallyBounded_and_isLocallyDirectSummand_and_isoDualComplex_of_exactPairing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/ComplexWithALeftDual.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Duals/ComplexWithALeftDual.lean#L106). The attribute's comment: “the WHOLE statement of the tag under the tag's OWN hypothesis, for a ringed site — of which the ringed space of the tag is a case — and over the monoidal structure on complexes of 𝒪-modules whose tensor product is the one of Tag 01CA: a complex `ℱ^•` with a left dual `𝒢^•` is (1) locally bounded, (2) has every term a local direct summand of a finite free module, and (3) has `𝒢^•` the complex of Example 0FP9, namely `SheafHom^•(ℱ^•, 𝒪)` — `Stacks.SheafOfModules.Strict.dualComplexOfLocallyStrictlyPerfect`, the dual sheaves of Tag 0FNY in the opposite degrees with the signed-transpose differential — together WITH its pairings: the isomorphism carries η and ε to the η = ∑ ηₙ and ε = ∑ εₙ that Tag 0FPR puts on that complex, so the triple `(𝒢^•, η, ε)` is identified with Example 0FP9's triple and not merely the underlying complexes. (3) is uniqueness of left duals (Tag 0FFR, `CategoryTheory.rightDualIso`) applied to the left dual Tag 0FPR builds from the local strict perfectness of Tag 0FPS, which (1) and (2) supply. The site-level analogue of the whole tag is Tag 0FPS, `Stacks.SheafOfModules.Strict.exists_cover_isStrictlyPerfect_of_exactPairing` for its first assertion”.

> **[Stacks, Tag 0FPA].** Let `(C, 𝒪)` be a ringed site and let `ℱ^•` be a complex of
> `𝒪`-modules. If `ℱ^•` has a left dual `𝒢^•` in the monoidal category of complexes of
> `𝒪`-modules, then all three of the following hold.
>
> 1. `ℱ^•` is locally bounded: every object of the site has a covering sieve on whose members all
>    but finitely many terms of `ℱ^•` restrict to zero, the finite set of surviving degrees
>    depending on the member.
> 2. Every term `ℱ^n` is locally a direct summand of a finite free `𝒪`-module.
> 3. The left dual is the one constructed in [Stacks, Tag 0FP9]: `𝒢^•` is isomorphic to the complex
>    `SheafHom^•(ℱ^•, 𝒪)` of [Stacks, Tag 0FPR] by an isomorphism carrying the coevaluation and the
>    evaluation of the given pairing to `η = ∑ ηₙ` and `ε = ∑ εₙ`.

```lean
theorem isLocallyBounded_and_isLocallyDirectSummand_and_isoDualComplex_of_exactPairing
    (p : @ExactPairing _ _ (monoidalCategoryCochainComplex R) K L) :
    letI := monoidalCategoryCochainComplex R
    letI := p
    letI := exactPairingDualComplexOfLocallyStrictlyPerfect
      (isLocallyStrictlyPerfect_of_exactPairing R K L p)
    (∀ U : C, ∃ T : Sieve U, T ∈ J U ∧ ∀ ⦃V : C⦄ (g : V ⟶ U), T g →
        ∃ S : Finset ℤ, ∀ n ∉ S, IsZero ((K.X n).over V)) ∧
      (∀ n : ℤ, IsLocallyDirectSummandOfFiniteFree R.obj (isSheaf_ringSheaf R) (K.X n)) ∧
      ∃ e : L ≅ dualComplexOfLocallyStrictlyPerfect R K
          (isLocallyStrictlyPerfect_of_exactPairing R K L p),
        η_ K L ≫ K ◁ e.hom =
            η_ K (dualComplexOfLocallyStrictlyPerfect R K
              (isLocallyStrictlyPerfect_of_exactPairing R K L p)) ∧
          e.hom ▷ K ≫ ε_ K (dualComplexOfLocallyStrictlyPerfect R K
              (isLocallyStrictlyPerfect_of_exactPairing R K L p)) = ε_ K L
```

## Tag 0G40, a lemma

[Tag 0G40](https://stacks.math.columbia.edu/tag/0G40) in the Stacks Project.

**`Stacks.SheafOfModules.derivedSheafHomEvaluation_isIso_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHomEvaluation/PerfectEvaluation.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHomEvaluation/PerfectEvaluation.lean#L210).

> **Stacks 0G40.** Let `(X, O_X)` be a ringed space and let `K`, `L`, `M` be objects of
> `D(O_X)` with `K` perfect. The evaluation morphism
>
> `RSheafHom(L, M) ⊗^L_{O_X} K ⟶ RSheafHom(RSheafHom(K, L), M)`
>
> of Stacks 0A8U is an isomorphism, for every `L` and `M`.
>
> This reads off the ringed-site statement
> `AlgebraicGeometry.RingedSite.isIso_derivedSheafHomEvaluation_of_isPerfect` at the site of opens
> of the space, for the canonical derived tensor product and the derived internal Hom of the ringed
> space; the two notions of perfection agree because the predicate used here *is* the site-level
> one of Stacks 08G5.

```lean
theorem derivedSheafHomEvaluation_isIso_of_isPerfect
    (K L M : DerivedCategory (StructureSheafModules Rc))
    (hK : (ringedSite Rc).IsPerfect K) :
    IsIso (derivedSheafHomEvaluation Rc K L M)
```

## Tag 08DQ, a lemma

[Tag 08DQ](https://stacks.math.columbia.edu/tag/08DQ) in the Stacks Project.

**`Stacks.SheafOfModules.derivedBidualIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectBidual.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectBidual.lean#L176). The attribute's comment: “the second assertion: `(K^∨)^∨ ≅ K` for a perfect `K`”.

> **Stacks 08DQ, second assertion.** Let `(X, O_X)` be a ringed space and let `K` be a perfect
> object of `D(O_X)`. Then `K` is reflexive: the canonical map `K ⟶ (K^∨)^∨` of
> `derivedBidualMap` is an isomorphism, so `(K^∨)^∨ ≅ K`.
>
> This is the isomorphism form of `isIso_derivedBidualMap`; its `.symm` is the orientation
> `(K^∨)^∨ ≅ K` in which the source states the assertion. The three factors are the left unitor,
> the trivialisation `O_X ≅ RSheafHom(O_X, O_X)` and the derived evaluation morphism of
> Stacks 0A8U, the last being invertible by Stacks 0G40.
>
> Perfectness is the site-level notion of Stacks 08G5 read at the site of opens of the space, as in
> `StacksFrontier.Topology.Sheaves.Cohomology.InternalHomEvaluation.PerfectEvaluation`, whose section
> "Perfectness model" records why that notion and not the ringed-space one of Stacks 08CM.

```lean
def derivedBidualIso (K : DerivedCategory (StructureSheafModules Rc))
    (hK : (ringedSite Rc).IsPerfect K) :
    K ≅ derivedDual Rc (derivedDual Rc K)
```

**`Stacks.SheafOfModules.isIso_derivedBidualMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectBidual.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectBidual.lean#L214). The attribute's comment: “the second assertion: the canonical map `K = RSheafHom(O_X, O_X) ⊗^L K ⟶ (K^∨)^∨` of Stacks 0A8U is an isomorphism for a perfect `K`”. References: SGA 6 I (7.2), “special case”.

> **Stacks 08DQ, second assertion.** Let `(X, O_X)` be a ringed space and let `K` be a perfect
> object of `D(O_X)`. The canonical map
>
> `K = RSheafHom(O_X, O_X) ⊗^L_{O_X} K ⟶ RSheafHom(RSheafHom(K, O_X), O_X) = (K^∨)^∨`
>
> of `derivedBidualMap` is an isomorphism; equivalently `(K^∨)^∨ ≅ K`, which is
> `derivedBidualIso`.
>
> Perfectness of `K` is the only hypothesis. Its two outer factors are isomorphisms by
> construction, and its middle factor — the derived evaluation morphism of Stacks 0A8U at
> `L = M = O_X` — is an isomorphism by Stacks 0G40, which holds for every value of the two
> variables specialised here.

```lean
theorem isIso_derivedBidualMap (K : DerivedCategory (StructureSheafModules Rc))
    (hK : (ringedSite Rc).IsPerfect K) :
    IsIso (derivedBidualMap Rc K)
```

**`Stacks.SheafOfModules.isPerfect_derivedDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDual.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDual.lean#L145). The attribute's comment: “the dual of a perfect object is perfect”.

> **Stacks 08DQ, first assertion.** Let `(X, O_X)` be a ringed space and let `K` be a perfect
> object of `D(O_X)`. Then the dual `K^∨ = RSheafHom(K, O_X)` is perfect as well.
>
> Perfectness is local, so it is enough to model `K^∨` above a covering of each open. Over a
> member `V` on which `K` is modelled by a strictly perfect complex `E`, the restriction of `K^∨`
> is `RSheafHom(K|_V, O_V)`, which is the class of the internal Hom complex `SheafHom(E, O_V)`;
> and that complex is strictly perfect because the dual of a direct summand of a finite free
> module is again one.

```lean
theorem isPerfect_derivedDual (K : DerivedCategory (StructureSheafModules Rc))
    (hK : (ringedSite Rc).IsPerfect K) :
    (ringedSite Rc).IsPerfect (derivedDual Rc K)
```

**`Stacks.SheafOfModules.isPerfect_derivedDual_of_isPerfectSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualAtTheSpaceHypothesis.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualAtTheSpaceHypothesis.lean#L69). The attribute's comment: “the first assertion with perfectness in the RINGED-SPACE reading of Tag 08CM on both sides, rather than the site reading of Tag 08G5 that `Stacks.SheafOfModules.isPerfect_derivedDual` uses; the two are equivalent by `Stacks.Cohomology.PerfectComplexes.isPerfect_of_ringedSite` and `Stacks.Cohomology.PerfectComplexes.isPerfect_ringedSite_of_isPerfect`”.

> Let `(X, O_X)` be a ringed space and let `K` be a perfect object of `D(O_X)` in the sense of
> [Stacks, Tag 08CM]. Then the dual `K^∨ = RSheafHom(K, O_X)` is perfect in that same sense.

```lean
theorem isPerfect_derivedDual_of_isPerfectSpace
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X) K) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X) (derivedDual X.sheaf K)
```

**`Stacks.SheafOfModules.isIso_derivedBidualMap_of_isPerfectSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualAtTheSpaceHypothesis.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualAtTheSpaceHypothesis.lean#L81). The attribute's comment: “the second assertion with perfectness in the RINGED-SPACE reading of Tag 08CM rather than the site reading of Tag 08G5 that `Stacks.SheafOfModules.isIso_derivedBidualMap` uses”. References: SGA 6 I (7.2), “special case”.

> For a perfect object `K` of `D(O_X)` in the sense of [Stacks, Tag 08CM] the canonical map
> `K ⟶ (K^∨)^∨` of `Stacks.SheafOfModules.derivedBidualMap` is an isomorphism.

```lean
theorem isIso_derivedBidualMap_of_isPerfectSpace
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X) K) :
    IsIso (derivedBidualMap X.sheaf K)
```

**`Stacks.SheafOfModules.derivedBidualIsoOfIsPerfectSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualAtTheSpaceHypothesis.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualAtTheSpaceHypothesis.lean#L92). The attribute's comment: “the second assertion as an isomorphism, with perfectness in the RINGED-SPACE reading of Tag 08CM rather than the site reading of Tag 08G5 that `Stacks.SheafOfModules.derivedBidualIso` uses”.

> For a perfect object `K` of `D(O_X)` in the sense of [Stacks, Tag 08CM], the isomorphism
> `K ≅ (K^∨)^∨`.

```lean
def derivedBidualIsoOfIsPerfectSpace
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X) K) :
    K ≅ derivedDual X.sheaf (derivedDual X.sheaf K)
```

**`Stacks.SheafOfModules.isIso_derivedTensorDualToSheafHom_of_isPerfectSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualAtTheSpaceHypothesis.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualAtTheSpaceHypothesis.lean#L107). The attribute's comment: “the third assertion with perfectness in the RINGED-SPACE reading of Tag 08CM rather than the site reading of Tag 08G5 that `Stacks.SheafOfModules.isIso_derivedTensorDualToSheafHom_of_isPerfect` uses”.

> For a perfect object `K` of `D(O_X)` in the sense of [Stacks, Tag 08CM] and any object `M`, the
> canonical map of [Stacks, Tag 08I1]
>
> `M ⊗^L_{O_X} K^∨ ⟶ RSheafHom(K, M)`
>
> is an isomorphism.

```lean
theorem isIso_derivedTensorDualToSheafHom_of_isPerfectSpace
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X) K) :
    IsIso (derivedTensorDualToSheafHom X.sheaf K M)
```

**`Stacks.SheafOfModules.bijective_derivedTensorDualGlobalSectionsMap_of_isPerfectSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualAtTheSpaceHypothesis.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualAtTheSpaceHypothesis.lean#L122). The attribute's comment: “the fourth assertion with perfectness in the RINGED-SPACE reading of Tag 08CM rather than the site reading of Tag 08G5 that `Stacks.SheafOfModules.bijective_derivedTensorDualGlobalSectionsMap_of_isPerfect` uses”.

> For a perfect object `K` of `D(O_X)` in the sense of [Stacks, Tag 08CM] and any object `M`, the
> canonical map of [Stacks, Tag 08I1] on degree-zero global hypercohomology
>
> `H⁰(X, M ⊗^L_{O_X} K^∨) ⟶ Hom_{D(O_X)}(K, M)`
>
> is bijective.

```lean
theorem bijective_derivedTensorDualGlobalSectionsMap_of_isPerfectSpace
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X) K) :
    Function.Bijective (derivedTensorDualGlobalSectionsMap X.sheaf K M)
```

**`Stacks.SheafOfModules.derivedTensorDualGlobalSectionsAddEquivOfIsPerfectSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualAtTheSpaceHypothesis.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualAtTheSpaceHypothesis.lean#L136). The attribute's comment: “the fourth assertion as an isomorphism of abelian groups, with perfectness in the RINGED-SPACE reading of Tag 08CM rather than the site reading of Tag 08G5 that `Stacks.SheafOfModules.derivedTensorDualGlobalSectionsAddEquiv` uses; functoriality in `M` is `Stacks.SheafOfModules.derivedTensorDualSections_naturality` together with `AlgebraicGeometry.RingedSite.derivedTensorDualGlobalSectionsMap_naturality`”.

> For a perfect object `K` of `D(O_X)` in the sense of [Stacks, Tag 08CM] and any object `M`,
> `H⁰(X, M ⊗^L_{O_X} K^∨) = Hom_{D(O_X)}(K, M)` as abelian groups, the identification being the
> canonical map of [Stacks, Tag 08I1].

```lean
def derivedTensorDualGlobalSectionsAddEquivOfIsPerfectSpace
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X) K) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
        ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
          (((derivedTensor X.sheaf).obj M).obj (derivedDual X.sheaf K))) : Type u) ≃+ (K ⟶ M)
```

**`Stacks.SheafOfModules.bijective_derivedTensorDualGlobalSectionsMap_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualGlobalSections.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualGlobalSections.lean#L133). The attribute's comment: “the fourth assertion: the canonical map `H⁰(X, M ⊗^L K^∨) ⟶ Hom_{D(O_X)}(K, M)` of Stacks 08I1 is bijective for a perfect `K`”.

> **Stacks 08DQ, fourth assertion.** Let `(X, O_X)` be a ringed space, let `K` be a perfect
> object of `D(O_X)` and let `M` be any object. The canonical map of Stacks 08I1 on degree-zero
> global hypercohomology
>
> `H⁰(X, M ⊗^L_{O_X} K^∨) ⟶ Hom_{D(O_X)}(K, M)`
>
> is bijective.
>
> Perfectness of `K` is in the site-level reading of Stacks 08G5, and `M` is arbitrary. The proof is
> the source's: by Stacks 08I1 the assertion reduces to invertibility of the canonical map
> `M ⊗^L_{O_X} K^∨ ⟶ RSheafHom(K, M)`, which is the third assertion of the tag,
> `isIso_derivedTensorDualToSheafHom_of_isPerfect`.

```lean
theorem bijective_derivedTensorDualGlobalSectionsMap_of_isPerfect
    (K M : DerivedCategory (StructureSheafModules Rc))
    (hK : (ringedSite Rc).IsPerfect K) :
    Function.Bijective (derivedTensorDualGlobalSectionsMap Rc K M)
```

**`Stacks.SheafOfModules.derivedTensorDualGlobalSectionsAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualGlobalSections.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualGlobalSections.lean#L152). The attribute's comment: “the fourth assertion: `H⁰(X, M ⊗^L K^∨) = Hom_{D(O_X)}(K, M)` for a perfect `K`, as an isomorphism of abelian groups along the canonical map of Stacks 08I1; not its functoriality in `M`”.

> **Stacks 08DQ, fourth assertion**, in the equality form the source states it in: for a
> perfect object `K` of `D(O_X)` and any object `M`,
>
> `H⁰(X, M ⊗^L_{O_X} K^∨) = Hom_{D(O_X)}(K, M)`
>
> as abelian groups, the identification being the canonical map of Stacks 08I1.
>
> Functoriality of this identification in `M` is *not* claimed; see the section "What is still
> missing" of this file.

```lean
def derivedTensorDualGlobalSectionsAddEquiv
    (K M : DerivedCategory (StructureSheafModules Rc))
    (hK : (ringedSite Rc).IsPerfect K) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
        ((derivedModuleGlobalSections (ringedSite Rc)).obj
          (((derivedTensor Rc).obj M).obj (derivedDual Rc K))) : Type u) ≃+ (K ⟶ M)
```

**`Stacks.SheafOfModules.isIso_derivedTensorDualToSheafHom_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualTensorHom.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualTensorHom.lean#L152). The attribute's comment: “the third assertion: the canonical map `M ⊗^L K^∨ ⟶ RSheafHom(K, M)` of Stacks 08I1 is an isomorphism for a perfect `K`”. References: SGA 6 I (7.7), “special case”.

> **Stacks 08DQ, third assertion.** Let `(X, O_X)` be a ringed space, let `K` be a perfect
> object of `D(O_X)` and let `M` be any object. The canonical map of Stacks 08I1
>
> `Φ : M ⊗^L_{O_X} K^∨ ⟶ RSheafHom(K, M)`
>
> is an isomorphism.
>
> The only hypothesis is perfectness of `K`, in the site-level reading of Stacks 08G5: there is a
> complex of `O_X`-modules representing `K` and a covering of the space on each member of which the
> restriction of that complex receives a quasi-isomorphism from a strictly perfect complex. The
> object `M` is arbitrary.
>
> This is the ringed-site statement
> `AlgebraicGeometry.RingedSite.isIso_derivedTensorDualToSheafHom_of_isPerfect` read at the site of
> opens of the space, for the canonical derived tensor product. The section "How it is proved" of
> this file sets out the argument.
>
> The instances in the ambient variable block are setup, not hypotheses on the lemma: a ringed
> space whose slice sites admit sheafification and on which the tensor product of sheaves of
> modules is additive and totalisable is what it takes for the objects in the statement — the
> derived tensor product, the derived dual, and their restrictions to the slices appearing in the
> definition of perfection — to exist at all.

```lean
theorem isIso_derivedTensorDualToSheafHom_of_isPerfect
    (K M : DerivedCategory (StructureSheafModules Rc))
    (hK : (ringedSite Rc).IsPerfect K) :
    IsIso (derivedTensorDualToSheafHom Rc K M)
```

**`Stacks.SheafOfModules.derivedTensorDualNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualTensorHomFunctorial.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualTensorHomFunctorial.lean#L105). The attribute's comment: “the third assertion as a natural isomorphism of functors on D(O\_X), i.e. together with the FUNCTORIALITY in M that the source asserts; its component at M is the canonical map of Tag 08I1 and is the content of `Stacks.SheafOfModules.isIso_derivedTensorDualToSheafHom_of_isPerfect`”.

> **Stacks 08DQ, third assertion, as a natural isomorphism.** For a perfect object `K` of
> `D(O_X)` the canonical maps `M ⊗^L_{O_X} K^∨ ⟶ RSheafHom(K, M)` of [Stacks, Tag 08I1] assemble
> into an isomorphism of functors
>
> `(- ⊗^L_{O_X} K^∨) ≅ RSheafHom(K, -)`,
>
> which is the source's assertion that the identification is functorial in `M`. Its component at
> `M` is the canonical map, invertible by
> `Stacks.SheafOfModules.isIso_derivedTensorDualToSheafHom_of_isPerfect`; the naturality square is
> `Stacks.SheafOfModules.derivedTensorDualToSheafHom_naturality`.

```lean
def derivedTensorDualNatIso (hK : (ringedSite Rc).IsPerfect K) :
    (derivedTensor Rc).flip.obj (derivedDual Rc K) ≅ (derivedSheafHom Rc).obj (op K)
```

**`Stacks.SheafOfModules.derivedTensorDualNatIsoOfIsPerfectSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualTensorHomFunctorial.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualTensorHomFunctorial.lean#L125). The attribute's comment: “the third assertion as a natural isomorphism of functors, with perfectness in the RINGED-SPACE reading of Tag 08CM rather than the site reading of Tag 08G5 that `Stacks.SheafOfModules.derivedTensorDualNatIso` uses”.

> **Stacks 08DQ, third assertion, as a natural isomorphism, at the ringed-space hypothesis.**
> As `Stacks.SheafOfModules.derivedTensorDualNatIso`, with perfectness of `K` read as
> `Stacks.Cohomology.PerfectComplexes.IsPerfect`, the notion of [Stacks, Tag 08CM].

```lean
def derivedTensorDualNatIsoOfIsPerfectSpace
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X) K) :
    (derivedTensor X.sheaf).flip.obj (derivedDual X.sheaf K) ≅
      (derivedSheafHom X.sheaf).obj (op K)
```

**`Stacks.SheafOfModules.derivedTensorDualNatIsoLeft`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualTensorHomLeftSlot.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualTensorHomLeftSlot.lean#L130). The attribute's comment: “the third assertion as a natural isomorphism of functors on D(O\_X), with the dual in the LEFT tensor slot rather than the right one in which Tag 08I1 writes the canonical map and in which `Stacks.SheafOfModules.derivedTensorDualNatIso` states it; the two differ by the commutativity constraint of Tag 0FPT, so this one is NOT claimed to be carried by the canonical map”.

> **Stacks 08DQ, third assertion, with the dual in the left tensor slot.** For a perfect
> object `K` of `D(O_X)` there is an isomorphism of functors
>
> `(K^∨ ⊗^L_{O_X} -) ≅ RSheafHom(K, -)`
>
> on `D(O_X)`, which is the source's assertion that the identification is functorial in the
> second variable, written with the dual tensored on the left.
>
> It is `Stacks.SheafOfModules.derivedTensorDualNatIso`, the same assertion with the dual in the
> right slot, precomposed with the commutativity constraint of
> `Stacks.SheafOfModules.derivedTensorBraidingNatIso`. Unlike the right-slot form, it is not
> claimed to be carried by the canonical map of [Stacks, Tag 08I1]; see the implementation
> notes.

```lean
def derivedTensorDualNatIsoLeft (hK : (ringedSite Rc).IsPerfect K) :
    (derivedTensor Rc).obj (derivedDual Rc K) ≅ (derivedSheafHom Rc).obj (op K)
```

**`Stacks.SheafOfModules.derivedTensorDualNatIsoLeftOfIsPerfectSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualTensorHomLeftSlot.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualTensorHomLeftSlot.lean#L146). The attribute's comment: “the third assertion as a natural isomorphism with the dual in the LEFT tensor slot, with perfectness in the RINGED-SPACE reading of Tag 08CM rather than the site reading of Tag 08G5 that `Stacks.SheafOfModules.derivedTensorDualNatIsoLeft` uses”.

> **Stacks 08DQ, third assertion in the left tensor slot, at the ringed-space hypothesis.**
> As `Stacks.SheafOfModules.derivedTensorDualNatIsoLeft`, with perfectness of `K` read as
> `Stacks.Cohomology.PerfectComplexes.IsPerfect`, the notion of [Stacks, Tag 08CM].

```lean
def derivedTensorDualNatIsoLeftOfIsPerfectSpace
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X) K) :
    (derivedTensor X.sheaf).obj (derivedDual X.sheaf K) ≅
      (derivedSheafHom X.sheaf).obj (op K)
```

## Tag 0FPB, a lemma

[Tag 0FPB](https://stacks.math.columbia.edu/tag/0FPB) in the Stacks Project.

**`Stacks.Cohomology.MonoidalDerived.symmetricMonoidalDerivedCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedMonoidalStructure.lean, line 586](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedMonoidalStructure.lean#L586).

> **The derived category of modules on a ringed space is a symmetric monoidal category**, with
> tensor product the derived tensor product, unit the structure sheaf in degree zero, and the
> usual associativity and commutativity constraints.  This is the ringed site statement at the
> site of opens of `X`, exactly as Tag 0FP8 is Tag 0FPQ there.

```lean
public def symmetricMonoidalDerivedCategory (X : RingedSpace.{u, u})
    [HasDerivedCategory.{d} (Mod X.sheaf)] :
    SymmetricMonoidalDerivedCategory X.sheaf
```

## Tag 0FPC, an example

[Tag 0FPC](https://stacks.math.columbia.edu/tag/0FPC) in the Stacks Project.

**`Stacks.SheafOfModules.derivedDual_isLeftDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualLeftDual.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/PerfectDualLeftDual.lean#L125).

> **Stacks 0FPC.**  Let `(X, O_X)` be a ringed space and let `K` be a perfect object of
> `D(O_X)` (Tag 08CM), with `K^∨ = RSheafHom(K, O_X)`.  Then
>
> * the map `c : K ⊗^L_{O_X} K^∨ ⟶ RSheafHom(K, K)` of Stacks 08I1 is an isomorphism;
> * the coevaluation `η : O_X ⟶ K ⊗^L_{O_X} K^∨` is the map sending `1` to the section
>   corresponding to `id_K` under `c`: `η ≫ c` is that section;
> * with `ε : K^∨ ⊗^L_{O_X} K ⟶ O_X` the evaluation map, `K^∨, η, ε` is a left dual of `K`
>   (Categories, Definition 0FFP): `(1 ⊗ ε) ∘ (η ⊗ 1) = id_K` and `(ε ⊗ 1) ∘ (1 ⊗ η) = id_{K^∨}`,
>   read through the associativity and unit constraints of the monoidal structure of Stacks 0FPT on
>   `D(O_X)`.
>
> The evaluation is `Stacks.SheafOfModules.derivedDualEvaluation`, the application morphism of
> Stacks 08J8 at target `O_X`
> (`Stacks.SheafOfModules.derivedSheafHomCounit_structureSheaf_eq_derivedDualEvaluation`), and
> the coevaluation is `Stacks.SheafOfModules.derivedDualCoevaluation`.

```lean
theorem derivedDual_isLeftDual (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X) K) :
    letI := derivedMonoidalStructure X.sheaf
    letI : MonoidalCategory (DerivedCategory (SheafOfModules.{u}
        (Tensor.ringSheaf.{u, u, u} X.sheaf))) := derivedMonoidalStructure X.sheaf
    IsIso (derivedTensorDualToSheafHom X.sheaf K K) ∧
      derivedDualCoevaluation X.sheaf K
          (Stacks.Cohomology.PerfectComplexes.isPerfect_ringedSite_of_isPerfect X K hK) ≫
          derivedTensorDualToSheafHom X.sheaf K K =
        RingedSite.derivedIdentitySection (ringedSite X.sheaf) K ∧
      derivedDualCoevaluation X.sheaf K
          (Stacks.Cohomology.PerfectComplexes.isPerfect_ringedSite_of_isPerfect X K hK) ▷ K ≫
          (α_ K (derivedDual X.sheaf K) K).hom ≫ K ◁ derivedDualEvaluation X.sheaf K =
        (λ_ K).hom ≫ (ρ_ K).inv ∧
      derivedDual X.sheaf K ◁ derivedDualCoevaluation X.sheaf K
          (Stacks.Cohomology.PerfectComplexes.isPerfect_ringedSite_of_isPerfect X K hK) ≫
          (α_ (derivedDual X.sheaf K) K (derivedDual X.sheaf K)).inv ≫
          derivedDualEvaluation X.sheaf K ▷ derivedDual X.sheaf K =
        (ρ_ (derivedDual X.sheaf K)).hom ≫ (λ_ (derivedDual X.sheaf K)).inv
```

## Tag 0FPD, a lemma

[Tag 0FPD](https://stacks.math.columbia.edu/tag/0FPD) in the Stacks Project.

**`Stacks.SheafOfModules.isIso_derivedDualToLeftDualMonoidal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/LeftDualOnARingedSpace.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/LeftDualOnARingedSpace.lean#L232). The attribute's comment: “conclusion (b) only: that the left dual of M is the object constructed in Example 0FPC, namely the derived dual RSheafHom(M, O\_X), the identification being the morphism matched with the evaluation of Example 0FPC by the pairing — see `Stacks.SheafOfModules.whiskerRight_derivedDualToLeftDualMonoidal` for the compatibility of the two evaluations and `Stacks.SheafOfModules.derivedDualEvaluation_eq_ringedSite` for the identification of that evaluation with the one Example 0FPC constructs. The monoidal structure on D(O\_X) is the one of Tag 0FPB and a left dual is Mathlib's `CategoryTheory.ExactPairing`, which is Definition 0FFP. Conclusion (a) of the tag — that M is PERFECT — is NOT proved here and NOT assumed here: it needs the pairing to restrict to the slices D(O\_X|\_U), for which the derived restriction functor would have to be monoidal, and nothing in this library makes it so. The naturality of the bijection of Tag 08DK/08JA in its source variable, which the argument uses, is the theorem `AlgebraicGeometry.RingedSite.derivedCurryHomEquiv_naturality_source`, so the exact pairing itself is the one remaining input”.

> **Stacks 0FPD, second assertion: a left dual of `M` in `D(O_X)` is the dual object of
> Example 0FPC.** The morphism `M^∨ = RSheafHom(M, O_X) ⟶ N` which the exact pairing matches with
> the evaluation of Example 0FPC is an isomorphism; its inverse is the morphism which the
> tensor–internal-Hom bijection of Stacks 08DK matches with the evaluation of the pairing.

```lean
theorem isIso_derivedDualToLeftDualMonoidal
    (pair : letI : MonoidalCategory (DerivedCategory (StructureSheafModules Rc)) :=
        RingedSite.derivedMonoidalStructure (ringedSite Rc)
      ExactPairing M N) :
    letI : @ExactPairing
        (DerivedCategory
          (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (ringedSite Rc).O)))
        inferInstance (RingedSite.derivedMonoidalStructure (ringedSite Rc)) M N := pair
    IsIso (RingedSite.derivedDualToLeftDual (X := ringedSite Rc) M N)
```

**`Stacks.Cohomology.LeftDualPerfect.isPerfect_and_isIso_derivedDualToLeftDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/LeftDualIsPerfect.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/LeftDualIsPerfect.lean#L96). The attribute's comment: “both conclusions, for one pairing: M is perfect, and the left dual is the derived dual of Example 0FPC”.

> **Stacks 0FPD.** Let `(X, O_X)` be a ringed space and let `M` be an object of `D(O_X)` with a
> left dual `N` in the symmetric monoidal category `D(O_X)` of Stacks 0FPB (an exact pairing,
> Categories, Definition 0FFP). Then
>
> * (a) `M` is perfect (Tag 08CM), and
> * (b) the left dual is the one constructed in Example 0FPC: the morphism
>   `M^∨ = RSheafHom(M, O_X) ⟶ N` which the pairing matches with the evaluation of Example 0FPC is
>   an isomorphism.
>
> The monoidal structure is written in its ringed-site spelling, which is the structure of
> Stacks 0FPB on the nose (`derivedCategoryMonoidalCategory_eq_ringedSite`, by `rfl`). Conclusion
> (a) is `isPerfect_of_exactPairing`; conclusion (b) is
> `Stacks.SheafOfModules.isIso_derivedDualToLeftDualMonoidal`, whose morphism carries the evaluation
> of the pairing to the evaluation of Example 0FPC
> (`Stacks.SheafOfModules.whiskerRight_derivedDualToLeftDualMonoidal`).

```lean
theorem isPerfect_and_isIso_derivedDualToLeftDual (X : RingedSpace.{u, u})
    (M N : DerivedModules X.sheaf)
    (pair : letI := derivedMonoidalSpace X; ExactPairing M N) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect M ∧
      (letI := derivedMonoidalSpace X
       let _ := pair
       IsIso (AlgebraicGeometry.RingedSite.derivedDualToLeftDual
        (X := Stacks.SheafOfModules.ringedSite X.sheaf) M N))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.50, Tag 0FP7](https://stacks.math.columbia.edu/tag/0FP7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
