---
declaration: section
origin: cited
lean: Stacks.Cech.Linear.sectionsToTotalCech, Stacks.Cech.globalSectionsToCech, Stacks.Cech.cechTotalComplexRefinement, Stacks.Cech.exists_cechToDerivedComparison_and_cechSpectralSequence, Stacks.Cech.exists_cechSpectralSequence, Stacks.Cech.cechToDerivedGlobalSections, Stacks.Cech.Linear.cechToDerivedSections, Stacks.Cech.isIso_cechToDerivedGlobalSections_app
statement: formalized
proof: formalized
---

# 20.25 Čech cohomology of complexes

Section 20.25 of the Stacks Project, [Tag 01FP](https://stacks.math.columbia.edu/tag/01FP). 7 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07M9, an equation

[Tag 07M9](https://stacks.math.columbia.edu/tag/07M9) in the Stacks Project.

**`Stacks.Cech.Linear.sectionsToTotalCech`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/ModuleValuedTotalComplex.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/ModuleValuedTotalComplex.lean#L111). The attribute's comment: “the augmentation, with module coefficients”.

> Restriction of a section over `U` into Čech degree zero, followed by the inclusion of that
> summand of the total complex: the map `Γ(U, K^•) ⟶ Tot(Č^•(Ui, K^•))` of complexes of
> `O_X(U)`-modules, natural in `K^•`.

```lean
def sectionsToTotalCech :
    sectionsComplexFunctor X O U ⟶ totalCechComplexFunctor X O U Ui hU
```

**`Stacks.Cech.globalSectionsToCech`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RecoveryA/GlobalSectionsToCech.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RecoveryA/GlobalSectionsToCech.lean#L250).

> **Stacks Project, Tag 07M9.** Restriction into Čech degree zero, followed by
> inclusion into the total complex.

```lean
noncomputable def globalSectionsToCech :
    globalSectionsComplexFunctor X ⟶ cechTotalComplexFunctor U
```

## Tag 08BM, an equation

[Tag 08BM](https://stacks.math.columbia.edu/tag/08BM) in the Stacks Project.

**`Stacks.Cech.cechTotalComplexRefinement`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/TotalComplexRefinement.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Cech/TotalComplexRefinement.lean#L148). References: EGA III (6.6.7), “partial”.

> **Stacks 08BM.** A refinement `t : V ⟶ U` induces, naturally in a complex of presheaves,
> the restriction map `Tot(Č^•(U, F^•)) ⟶ Tot(Č^•(V, F^•))`.

```lean
noncomputable def cechTotalComplexRefinement {I J : Type w} (U : I → C) (V : J → C)
    (t : FormalCoproduct.mk J V ⟶ FormalCoproduct.mk I U) :
    CechRefinementTransformation U V t
```

## Tag 08BN, a lemma

[Tag 08BN](https://stacks.math.columbia.edu/tag/08BN) in the Stacks Project.

**`Stacks.Cech.exists_cechToDerivedComparison_and_cechSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechSpectralSequence/BoundedBelowComplexFullStatement.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechSpectralSequence/BoundedBelowComplexFullStatement.lean#L86). The attribute's comment: “the whole lemma: the canonical map `Tot(Č(U, F)) ⟶ RΓ(X, F)`, functorial in `F` and compatible with the augmentation of (20.25.0.1) = Tag 07M9 and the refinement map of (20.25.0.2) = Tag 08BM, together with the spectral sequence `E_2^{p,q} = H^p(Tot(Č(U, H^q(F))))` abutting to `H^{p+q}(X, F)` -- for a ringed space, an open covering of `X` and a bounded below complex of `O_X`-modules, which are the lemma's three inputs and all of them”.

> **Tag 08BN.** Let `(X, O_X)` be a ringed space, let `U : X = ⋃_{i ∈ I} U_i` be an open
> covering and let `F^•` be a bounded below complex of `O_X`-modules. Then
>
> 1. there is a canonical map `Tot(Č^•(U, F^•)) ⟶ RΓ(X, F^•)`, functorial in `F^•` -- it is a
>    morphism of functors on bounded below complexes -- and compatible both with the augmentation
>    of equation (20.25.0.1) ([Stacks, Tag 07M9]) and with the refinement map of equation
>    (20.25.0.2) ([Stacks, Tag 08BM]); and
> 2. there is a cohomological spectral sequence with
>    `E_2^{p,q} = H^p(Tot(Č^•(U, H^q(F^•))))` abutting to `H^{p+q}(X, F^•)`, where `H^q(F^•)` is
>    the complex `n ↦ R^q i(F^n)` of cohomology presheaves of [Stacks, Tag 01ER].
>
> Both halves are read off the library's wider statements: the comparison from the system of
> comparisons for all coverings at once, `cechToDerivedGlobalSections`, and the spectral sequence
> from `exists_cechSpectralSequence`.

```lean
theorem exists_cechToDerivedComparison_and_cechSpectralSequence
    {I : Type u} (U : I → Opens X) (hU : ⊤ = iSup U)
    (K : CochainComplex.Plus (SheafOfModules.{u} R)) :
    ((globalSectionsToCechDerived X R U).app K ≫
          ((cechToDerivedGlobalSections X R).map U hU).app K =
          globalSectionsToDerived X R K ∧
        ∀ (J : Type u) (V : J → Opens X) (hV : ⊤ = iSup V)
            (t : FormalCoproduct.mk J V ⟶ FormalCoproduct.mk I U),
          cechRefinementDerived X R U V t ≫ (cechToDerivedGlobalSections X R).map V hV =
            (cechToDerivedGlobalSections X R).map U hU) ∧
      ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{u} 2,
        (∀ p q : ℤ,
          Nonempty ((E.page 2).X (p, q) ≅
            ((cechTotalComplexFunctor U).obj
              ((((underlyingPresheafFunctor X R).rightDerivedPlus q).mapHomologicalComplex
                (up ℤ)).obj K.1)).homology p)) ∧
          SpectralSequence.AbutsTo E (fun n =>
            (DerivedCategory.homologyFunctor AddCommGrpCat.{u} n).obj
              ((derivedGlobalSectionsFunctor X R).obj K))
```

**`Stacks.Cech.exists_cechSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechSpectralSequence/BoundedBelowComplexSpectralSequence.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechSpectralSequence/BoundedBelowComplexSpectralSequence.lean#L210). The attribute's comment: “the tag's spectral sequence: `E_2^{p,q} = H^p(Tot(Č(U, H^q(F))))`, both coordinates ranging over `ℤ`, abutting to `H^{p+q}(X, F)`, for a ringed space, an open covering of `X` and a bounded below complex of `O_X`-modules. The tag's comparison map `Tot(Č(U, F)) ⟶ RΓ(X, F)`, with its Tag 07M9 and Tag 08BM compatibilities, is `Stacks.Cech.cechToDerivedGlobalSections`, and the two halves are asserted together at the lemma's own three inputs by `Stacks.Cech.exists_cechToDerivedComparison_and_cechSpectralSequence`”.

> For a ringed space `(X, O_X)`, an open covering `U : I → Opens X` of `X` and a bounded below
> complex `F^•` of `O_X`-modules there is a cohomological spectral sequence, starting on page two,
> with
>
> ```
> E_2^{p,q} = H^p(Tot(Č^•(U, H^q(F^•))))
> ```
>
> where `H^q(F^•)` is the complex `n ↦ R^q i(F^n)` of cohomology presheaves, abutting to
> `H^{p+q}(X, F^•)`.

```lean
theorem exists_cechSpectralSequence {I : Type u} (U : I → Opens X) (hU : ⊤ = iSup U)
    (K : CochainComplex.Plus (SheafOfModules.{u} R)) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{u} 2,
      (∀ p q : ℤ,
        Nonempty ((E.page 2).X (p, q) ≅
          ((cechTotalComplexFunctor U).obj
            ((((underlyingPresheafFunctor X R).rightDerivedPlus q).mapHomologicalComplex
              (up ℤ)).obj K.1)).homology p)) ∧
      SpectralSequence.AbutsTo E (fun n =>
        (DerivedCategory.homologyFunctor AddCommGrpCat.{u} n).obj
          ((derivedGlobalSectionsFunctor X R).obj K))
```

**`Stacks.Cech.cechToDerivedGlobalSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/DerivedGlobalSections.lean, line 537](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/DerivedGlobalSections.lean#L537). The attribute's comment: “the tag's comparison map: the total Čech complex of a bounded below complex of `O_X`-modules maps canonically to its derived global sections, functorially in the complex -- the map is a morphism of functors on bounded below complexes -- and compatibly both with the Tag 07M9 augmentation and with the Tag 08BM refinement map, simultaneously for every open covering of `X`. The tag's spectral sequence `E_2^{p,q} = H^p(Tot(Č(U, H^q(F))))` abutting to `H^{p+q}(X, F)` is `Stacks.Cech.exists_cechSpectralSequence`, and the two halves are asserted together at the lemma's own three inputs by `Stacks.Cech.exists_cechToDerivedComparison_and_cechSpectralSequence`”.

> **Tag 08BN, the comparison map.** For a ringed space `(X, O_X)` the total Čech complex of a
> bounded below complex of `O_X`-modules has a canonical map to its derived global sections,
> functorial in the complex, compatible with the augmentation of Tag 07M9 — hence independent of
> the covering — and compatible with the refinement map of Tag 08BM.

```lean
noncomputable def cechToDerivedGlobalSections
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) :
    CechToDerivedGlobalSectionsSystem X R
```

**`Stacks.Cech.Linear.cechToDerivedSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/ModuleValuedDerivedSections.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/ModuleValuedDerivedSections.lean#L440). The attribute's comment: “the tag's comparison map, generalised to module coefficients over an arbitrary open: for a ringed space `(X, O_X)` and an open `U`, the total Čech complex of a bounded below complex of `O_X`-modules maps canonically to its derived sections in `D(O_X(U))`, functorially in the complex and compatibly with the Tag 07M9 augmentation, simultaneously for every open covering of `U`. The tag's own statement -- the comparison over `X`, compatible with both the Tag 07M9 and the Tag 08BM maps, together with the tag's spectral sequence -- is `Stacks.Cech.cechToDerivedGlobalSections` and `Stacks.Cech.exists_cechSpectralSequence`, conjoined at the lemma's three inputs by `Stacks.Cech.exists_cechToDerivedComparison_and_cechSpectralSequence`”.

> **Stacks 08BN, the comparison map with module coefficients.**  For a ringed space `(X, O_X)`
> and an open subset `U` the total Čech complex of a bounded below complex of `O_X`-modules has a
> canonical map to its derived sections over `U`, a morphism of `D(O_X(U))` functorial in the
> complex and compatible with the augmentation of [Stacks, Tag 07M9] -- hence independent of the
> covering.

```lean
def cechToDerivedSections : CechToDerivedSectionsSystem X O U
```

## Tag 0FLH, a lemma

[Tag 0FLH](https://stacks.math.columbia.edu/tag/0FLH) in the Stacks Project.

**`Stacks.Cech.isIso_cechToDerivedGlobalSections_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/AcyclicCoveringComputesDerivedSections.lean, line 447](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/AcyclicCoveringComputesDerivedSections.lean#L447). The attribute's comment: “the vanishing condition is the one of Tag 01ET: the higher right derived functors of sections over each intersection vanish on each term of the complex”.

> **[Stacks, Tag 0FLH]** Let `(X, O_X)` be a ringed space, let `U : I → Opens X` be an open
> covering of `X` and let `K^•` be a bounded below complex of `O_X`-modules with
> `H^i(U_{i_0 … i_p}, K^q) = 0` for all `i > 0`, all tuples `i_0, …, i_p` of members of the
> covering, and all degrees `q`. Then the comparison map `Tot(Č^•(U, K^•)) ⟶ RΓ(X, K^•)` of
> Tag 08BN is an isomorphism.

```lean
theorem isIso_cechToDerivedGlobalSections_app
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) (hU : ⊤ = iSup U)
    (K : CochainComplex.Plus (SheafOfModules.{u} R))
    (hacyclic : ∀ (n : ℕ) (s : Fin (n + 1) → I) (q : ℤ) (i : ℕ), 0 < i →
      IsZero (((SheafOfModules.evaluation.{u} R
        (op (⨅ k, U (s k)))).rightDerived i).obj (K.1.X q))) :
    IsIso (((cechToDerivedGlobalSections X R).map U hU).app K)
```

## Tag 07MB, an equation

[Tag 07MB](https://stacks.math.columbia.edu/tag/07MB) in the Stacks Project.

**`Stacks.Cech.LinearCupProduct.cechCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/LinearCupProduct.lean, line 1109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/LinearCupProduct.lean#L1109). The attribute's comment: “at module coefficients over a base ring, relative to a coefficient pairing”.

> **The Čech cup product** at coefficients in presheaves of modules over a base ring `R`: the
> signed Alexander--Whitney map
>
> `Tot(Tot(Č(W,K)) ⊗_R Tot(Č(W,L))) ⟶ Tot(Č(W,M))`
>
> attached to a pairing `D` of the coefficient complexes.  On the summand on which the first
> factor has total degree `n`, the target has Čech degree `p`, and the front face has Čech
> degree `r`, its coefficient is `cupProductSign n p r = (-1)^((p+r)n+rp+r)`.
>
> The source tensors over `R`; the pairing `D` is where the coefficients are tensored, and it is
> not required to be a tensor product over `R`.

```lean
noncomputable def cechCupProduct (D : ComplexPairing R K L M) :
    HomologicalComplex.mapBifunctor ((totalCechComplexFunctor W R).obj K)
        ((totalCechComplexFunctor W R).obj L) (tensorModules R) (up ℤ) ⟶
      (totalCechComplexFunctor W R).obj M
```

**`Stacks.Cech.LinearCupProduct.cechCupProduct_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/LinearCupProduct.lean, line 1122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/LinearCupProduct.lean#L1122). The attribute's comment: “the signed Alexander--Whitney formula at module coefficients over a base ring”.

> **On homogeneous summands the cup product is the front/back restriction formula** with the
> sign `(-1)^((p+r)n+rp+r)`, the restrictions being paired by `D`.

```lean
theorem cechCupProduct_ι (D : ComplexPairing R K L M) (r s : ℕ) (a b : ℤ) :
    tensorModulesMap R (ιTotalCech W R K r a) (ιTotalCech W R L s b) ≫
        HomologicalComplex.ιMapBifunctor ((totalCechComplexFunctor W R).obj K)
          ((totalCechComplexFunctor W R).obj L) (tensorModules R) (up ℤ)
          ((r : ℤ) + a) ((s : ℤ) + b) (((r : ℤ) + a) + ((s : ℤ) + b)) rfl ≫
        (cechCupProduct W R D).f (((r : ℤ) + a) + ((s : ℤ) + b)) =
      cupProductSign ((r : ℤ) + a) ((r : ℤ) + (s : ℤ)) (r : ℤ) •
        (cechAlexanderWhitney W R (D.μ a b (a + b) rfl) r s ≫
          ιTotalCech W R M (r + s) (a + b) ≫
          eqToHom (congrArg (((totalCechComplexFunctor W R).obj M).X) (by push_cast; ring)))
```

**`Stacks.Cech.ModuleCupProduct.cechCupProductA`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/ModuleCupProduct.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/ModuleCupProduct.lean#L140). The attribute's comment: “at 𝒪\_X-module coefficients over the ring of sections”.

> **The Čech cup product at `𝒪_X`-module coefficients.** The signed Alexander--Whitney
> cup-product map
>
> `Tot(Tot(Č(U,K)) ⊗_A Tot(Č(U,L))) ⟶ Tot(Č(U,M))`
>
> for `A = 𝒪_X(V)`, attached to a pairing `D` of the coefficient sections presheaves into those
> of `M`. On a homogeneous summand it is the front/back restriction formula with the
> Alexander--Whitney sign `cupProductSign n p r = (-1)^((p+r)n+rp+r)`.

```lean
noncomputable abbrev cechCupProductA
    (D : ComplexPairing (CoeffRing O V) ((sectionsComplexFunctor O V).obj K)
      ((sectionsComplexFunctor O V).obj L) ((sectionsComplexFunctor O V).obj M))
```

**`Stacks.Cech.SheafTensorPairing.cechCupProductSheafTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/SheafTensorPairing.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/SheafTensorPairing.lean#L360). The attribute's comment: “the sheaf-tensor instantiation: source over the section ring, coefficients over the structure sheaf”.

> **The Čech cup product at sheaf-tensor coefficients**: the signed Alexander--Whitney
> cup-product map
>
> `Tot(Tot(Č(𝒰,𝒦)) ⊗_A Tot(Č(𝒰,ℳ))) ⟶ Tot(Č(𝒰, Tot(𝒦 ⊗_{𝒪_X} ℳ)))`
>
> for a covering `𝒰` of `V` and `A = 𝒪_X(V)`.  This is the left-hand column of the diagram of
> Stacks Tag 0FKV: the source tensors the two total Čech complexes over the *ring* `A` of
> sections on `V`, while in the target the coefficients are tensored over the *structure sheaf*,
> the coefficient pairing being `sheafTensorComplexPairing`.
>
> Its value on a homogeneous summand is the front/back restriction formula with the
> Alexander--Whitney sign `cupProductSign n p r = (-1)^((p+r)n+rp+r)`: see
> `Stacks.Cech.LinearCupProduct.cechCupProduct_ι`, which applies by
> `Stacks.Cech.ModuleCupProduct.cechCupProductA_eq`.

```lean
noncomputable def cechCupProductSheafTensor :
    HomologicalComplex.mapBifunctor ((totalCechComplexFunctorA O V U hU).obj K)
        ((totalCechComplexFunctorA O V U hU).obj L) (tensorModules (CoeffRing O V)) (up ℤ) ⟶
      (totalCechComplexFunctorA O V U hU).obj
        (HomologicalComplex.mapBifunctor K L (sheafTensor O) (up ℤ))
```

**`Stacks.Cech.CupProduct.cechCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RecoveryC/CechCupProduct/CupProductMap.lean, line 810](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RecoveryC/CechCupProduct/CupProductMap.lean#L810).

> The signed Alexander--Whitney cup-product map
>
> `Tot(Tot(Č(U,F)) ⊗_ℤ Tot(Č(U,G))) ⟶ Tot(Č(U,Tot(F ⊗_ℤ G)))`.
>
> On the summand on which `α` has total degree `n`, the target has Čech degree `p`, and
> the front face of `α` has Čech degree `r`, its coefficient is
> `cupProductSign n p r = (-1)^((p+r)n+rp+r)`.

```lean
noncomputable def cechCupProduct
    (F : CochainComplex (ZPresheaf.{u, max u v w} X) ℤ)
    (G : CochainComplex (ZPresheaf.{u, max u v w'} X) ℤ) :
    HomologicalComplex.mapBifunctor ((totalCechComplexFunctor.{u, v, max u w} X U).obj F)
        ((totalCechComplexFunctor.{u, v, max u w'} X U).obj G)
        (tensorModules.{max u v w, max u v w'} ℤ) (up ℤ) ⟶
      (totalCechComplexFunctor.{u, v, max u w w'} X U).obj
        (tensorSheafComplex.{u, max v w, max v w'} X F G)
```

**`Stacks.Cech.CupProduct.cechCupProduct_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RecoveryC/CechCupProduct/CupProductMap.lean, line 826](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RecoveryC/CechCupProduct/CupProductMap.lean#L826). The attribute's comment: “the signed Alexander--Whitney formula”.

> On homogeneous summands the cup product is the front/back restriction formula with
> the sign `(-1)^((p+r)n+rp+r)`.

```lean
theorem cechCupProduct_ι (F : CochainComplex (ZPresheaf.{u, max u v w} X) ℤ)
    (G : CochainComplex (ZPresheaf.{u, max u v w'} X) ℤ) (r s : ℕ) (a b : ℤ) :
    tensorModulesMap ℤ (ιTotalCech.{u, v, max u w} X U F r a)
      (ιTotalCech.{u, v, max u w'} X U G s b) ≫
        HomologicalComplex.ιMapBifunctor ((totalCechComplexFunctor.{u, v, max u w} X U).obj F)
          ((totalCechComplexFunctor.{u, v, max u w'} X U).obj G)
          (tensorModules.{max u v w, max u v w'} ℤ)
          (up ℤ) (r + a) (s + b) ((r + a) + (s + b)) rfl ≫
        (cechCupProduct.{u, v, w, w'} X U F G).f ((r + a) + (s + b)) =
      cupProductSign (r + a) (r + s) r •
        (cechAlexanderWhitney.{u, v, max u w, max u w'} X U (F.X a) (G.X b) r s ≫
          cechCochainsMap.{u, v, max u w w'} X U
            (ιTensorSheafComplex.{u, max v w, max v w'} X F G a b) (r + s) ≫
          ιTotalCech.{u, v, max u w w'} X U
            (tensorSheafComplex.{u, max v w, max v w'} X F G) (r + s) (a + b) ≫
          eqToHom (congrArg
            (((totalCechComplexFunctor.{u, v, max u w w'} X U).obj
              (tensorSheafComplex.{u, max v w, max v w'} X F G)).X)
            (by push_cast; ring)))
```

## Tag 07MC, a lemma

[Tag 07MC](https://stacks.math.columbia.edu/tag/07MC) in the Stacks Project.

**`Stacks.Cech.Hypercohomology.cup_boundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/HypercohomologyCupBoundaryTensor.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/HypercohomologyCupBoundaryTensor.lean#L199). The attribute's comment: “for complexes of modules over an arbitrary sheaf of commutative rings `𝒪_X` and `⊗_{𝒪_X}`; the source's abelian sheaves and `⊗_𝐙` are the case `𝒪_X = 𝐙_X`, whose modules are the abelian sheaves (`Stacks.Cech.Hypercohomology.isEquivalence_toSheaf_integerRingSheaf`) and whose tensor product is `⊗_𝐙`. `cup` is the cup product of Čech cocycles on a common covering and `boundary` the connecting map of the long exact cohomology sequence”.

> **[Stacks, Tag 07MC].**  Let `0 ⟶ F₁ ⟶ F₂ ⟶ F₃ ⟶ 0` (the short complex `S`) and
> `0 ⟶ G₃ ⟶ G₂ ⟶ G₁ ⟶ 0` (the short complex `T`) be short exact sequences of bounded below
> complexes of `𝒪_X`-modules, `H` a bounded below complex and `γᵢ : Tot(Fᵢ ⊗_{𝒪_X} Gᵢ) ⟶ H` maps of
> complexes such that the squares
>
> `γ₁ ∘ Tot(1 ⊗ (G₂ → G₁)) = γ₂ ∘ Tot((F₁ → F₂) ⊗ 1)` and
> `γ₂ ∘ Tot(1 ⊗ (G₃ → G₂)) = γ₃ ∘ Tot((F₂ → F₃) ⊗ 1)`
>
> commute.  If Čech cohomology agrees with cohomology for the sheaves `Fᵢᵖ` and `Gⱼ^q`, then for
> `a₃ ∈ Hⁿ(X, F₃)` and `b₁ ∈ Hᵐ(X, G₁)`
>
> `γ₁(∂a₃ ∪ b₁) = (-1)^{n+1} γ₃(a₃ ∪ ∂b₁)`  in `H^{n+m+1}(X, H)`.
>
> The source states this for complexes of abelian sheaves and `⊗_𝐙`. That is the case where
> `𝒪_X` is the constant sheaf of rings `𝐙_X`: sheaves of `𝐙_X`-modules are the abelian sheaves
> (`Stacks.Cech.Hypercohomology.isEquivalence_toSheaf_integerRingSheaf`), and `⊗_{𝐙_X}` is `⊗_𝐙`,
> since both are the sheafification of presheaves whose stalks are `Fₓ ⊗_𝐙 Gₓ`.

```lean
theorem cup_boundary
    (S : ShortComplex (CochainComplex.Plus (SheafOfModules.{u} (ringSheaf O))))
    (hS : (toSC S).ShortExact)
    (T : ShortComplex (CochainComplex.Plus (SheafOfModules.{u} (ringSheaf O))))
    (hT : (toSC T).ShortExact) (H : CochainComplex.Plus (SheafOfModules.{u} (ringSheaf O)))
    (γ₁ : letI : (Opens.grothendieckTopology X).WEqualsLocallyBijective AddCommGrpCat.{u} :=
        inferInstance
      HomologicalComplex.mapBifunctor S.X₁.obj T.X₃.obj (sheafTensor O) (up ℤ) ⟶ H.obj)
    (γ₂ : letI : (Opens.grothendieckTopology X).WEqualsLocallyBijective AddCommGrpCat.{u} :=
        inferInstance
      HomologicalComplex.mapBifunctor S.X₂.obj T.X₂.obj (sheafTensor O) (up ℤ) ⟶ H.obj)
    (γ₃ : letI : (Opens.grothendieckTopology X).WEqualsLocallyBijective AddCommGrpCat.{u} :=
        inferInstance
      HomologicalComplex.mapBifunctor S.X₃.obj T.X₁.obj (sheafTensor O) (up ℤ) ⟶ H.obj)
    (h₁ : letI : (Opens.grothendieckTopology X).WEqualsLocallyBijective AddCommGrpCat.{u} :=
        inferInstance
      HomologicalComplex.mapBifunctorMap (𝟙 S.X₁.obj) T.g.hom (sheafTensor O) (up ℤ) ≫ γ₁ =
      HomologicalComplex.mapBifunctorMap S.f.hom (𝟙 T.X₂.obj) (sheafTensor O) (up ℤ) ≫ γ₂)
    (h₂ : letI : (Opens.grothendieckTopology X).WEqualsLocallyBijective AddCommGrpCat.{u} :=
        inferInstance
      HomologicalComplex.mapBifunctorMap (𝟙 S.X₂.obj) T.f.hom (sheafTensor O) (up ℤ) ≫ γ₂ =
      HomologicalComplex.mapBifunctorMap S.g.hom (𝟙 T.X₁.obj) (sheafTensor O) (up ℤ) ≫ γ₃)
    (hF₁ : ∀ p, CechComputesSheaf O (S.X₁.obj.X p)) (hF₂ : ∀ p, CechComputesSheaf O (S.X₂.obj.X p))
    (hF₃ : ∀ p, CechComputesSheaf O (S.X₃.obj.X p)) (hG₁ : ∀ q, CechComputesSheaf O (T.X₃.obj.X q))
    (hG₂ : ∀ q, CechComputesSheaf O (T.X₂.obj.X q)) (hG₃ : ∀ q, CechComputesSheaf O (T.X₁.obj.X q))
    (n m : ℤ) (a₃ : hypercohomology O S.X₃ n) (b₁ : hypercohomology O T.X₃ m) :
    cup O (cechComputes_of_terms O _ hF₁) (cechComputes_of_terms O _ hG₁) (tensorPairing O γ₁)
        (n + 1) m (n + m + 1) (by omega) (boundary O S hS n (n + 1) rfl a₃) b₁ =
      ((n + 1).negOnePow : ℤ) •
        cup O (cechComputes_of_terms O _ hF₃) (cechComputes_of_terms O _ hG₃) (tensorPairing O γ₃)
          n (m + 1) (n + m + 1) (by omega) a₃ (boundary O T hT m (m + 1) rfl b₁)
```

## Tag 0B8S, a lemma

[Tag 0B8S](https://stacks.math.columbia.edu/tag/0B8S) in the Stacks Project.

**`Stacks.Cohomology.SquareZeroBoundary.SquareZeroKernel.moduleCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SquareZeroExtensionBoundaryDerivation.lean, line 770](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/SquareZeroExtensionBoundaryDerivation.lean#L770). The attribute's comment: “the `H⁰(X, O)`-module structure on `H¹(X, I)`”.

> **Stacks 0B8S**, first clause: `M = H¹(X, I)` is a module over `R = H⁰(X, O)`.  The kernel
> is a sheaf of `O`-modules (`Stacks.Cohomology.SquareZeroBoundary.SquareZeroKernel.incl_smul`),
> and a global section of `O` acts on `M` through the endomorphism of the kernel it induces.

```lean
noncomputable def moduleCohomology :
    Module (ToType (O.obj (op (⊤ : Opens X)))) (cohomologyOne I)
```

**`Stacks.Cohomology.SquareZeroBoundary.SquareZeroKernel.boundary`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SquareZeroExtensionBoundaryDerivation.lean, line 874](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/SquareZeroExtensionBoundaryDerivation.lean#L874). The attribute's comment: “the boundary map, in the Čech description of Stacks 02AP”.

> **The boundary map `∂ : H⁰(X, O) → H¹(X, I)`** of the short exact sequence
> `0 → I → O' → O → 0`, in the Čech description of Stacks 02AP: the class of the cocycle of
> differences of local lifts, transported to `H¹(X, I)` by the comparison of Stacks 01EQ.

```lean
noncomputable def boundary (f : ToType (O.obj (op (⊤ : Opens X)))) : cohomologyOne I
```

**`Stacks.Cohomology.SquareZeroBoundary.SquareZeroKernel.boundary_leibniz`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SquareZeroExtensionBoundaryDerivation.lean, line 1012](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/SquareZeroExtensionBoundaryDerivation.lean#L1012). The attribute's comment: “the Leibniz rule for the boundary map”.

> **Stacks 0B8S**, the Leibniz rule.  On a covering over which both `f` and `g` lift, the
> cocycle attached to `f * g` is `α g + f β`, where `α` and `β` are the cocycles attached to `f`
> and to `g` and the products are taken for the `O`-module structure on the kernel.

```lean
theorem boundary_leibniz (f g : ToType (O.obj (op (⊤ : Opens X)))) :
    E.boundary (f * g) =
      E.smulCohomology f (E.boundary g) + E.smulCohomology g (E.boundary f)
```

**`Stacks.Cohomology.SquareZeroBoundary.SquareZeroKernel.boundaryDerivation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SquareZeroExtensionBoundaryDerivation.lean, line 1080](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/SquareZeroExtensionBoundaryDerivation.lean#L1080). The attribute's comment: “the boundary map of the square-zero extension is a derivation”.

> **Stacks 0B8S.**  Let `X` be a topological space and `π : O' ⟶ O` a surjection of sheaves of
> commutative rings whose kernel `I` has square zero.  Then `M = H¹(X, I)` is a module over
> `R = H⁰(X, O)`, and the boundary map `∂ : R → M` of the short exact sequence
> `0 → I → O' → O → 0` is a derivation.

```lean
noncomputable def boundaryDerivation :
    letI := E.moduleCohomology
    Derivation ℤ (ToType (O.obj (op (⊤ : Opens X)))) (cohomologyOne I)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.25, Tag 01FP](https://stacks.math.columbia.edu/tag/01FP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
