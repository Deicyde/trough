---
declaration: section
origin: cited
lean: AlgebraicGeometry.abelianEtaleSheafStalkEquivalence, AlgebraicGeometry.etaleContinuousGModuleEquivalence, AlgebraicGeometry.etaleH0AddEquivGaloisInvariants, AlgebraicGeometry.etaleH0AddEquivGaloisInvariants_coe, AlgebraicGeometry.etaleH0AddEquivGaloisInvariants_abelianEtaleStalkGerm, AlgebraicGeometry.additiveSheafHAddEquivContinuousGroupCohomology, AlgebraicGeometry.etaleRightDerivedGammaIsoContinuousGroupCohomologyFunctor, AlgebraicGeometry.etaleSheafCohomologyIsoContinuousGroupCohomologyFunctor
statement: formalized
proof: formalized
---

# 59.59 Cohomology of a point

Section 59.59 of the Stacks Project, [Tag 03QQ](https://stacks.math.columbia.edu/tag/03QQ). 4 tags here are carried by 18 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04JQ, a lemma

[Tag 04JQ](https://stacks.math.columbia.edu/tag/04JQ) in the Stacks Project.

**`AlgebraicGeometry.abelianEtaleSheafStalkEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkEquivalence/AbelianSheafStalk.lean, line 737](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkEquivalence/AbelianSheafStalk.lean#L737). References: SGA 4 VIII (2.2).

> For a geometric point of the spectrum of a field, taking stalks is an equivalence from abelian
> sheaves on the small étale site to discrete modules over the absolute Galois group at that point,
> naturally identified with the abelian-group-valued stalk functor, and the Galois action on a germ
> changes the geometric lift of the étale neighbourhood by precomposition.

```lean
def abelianEtaleSheafStalkEquivalence :
    Σ e : Sheaf (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v} ≌
        ContinuousGAddCommGrp.{u, max u v} (GeometricPoint.absoluteGaloisGroup sbar),
      { α : e.functor ⋙
            ContinuousGAddCommGrp.forget (GeometricPoint.absoluteGaloisGroup sbar) ≅
          abelianEtaleStalkFunctor.{u, v} B (Spec (.of K)) hK sbar //
        ∀ (F : Sheaf (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v})
          (σ : GeometricPoint.absoluteGaloisGroup sbar),
          letI := GeometricPoint.residueFieldAlgebra sbar
          ∀ (τ : Gal(sbar.residueField /
              (Spec (.of K)).residueField (sbar.hom default)))
            (_hτ : ∀ a : GeometricPoint.separableClosure sbar,
              (σ a : sbar.residueField) = τ (a : sbar.residueField))
            (U : (geometricPointFiber B (Spec (.of K)) hK sbar).Elements)
            (q : (geometricPointFiber B (Spec (.of K)) hK sbar).obj U.1)
            (_hq : q.1 = Spec.map (CommRingCat.ofHom τ.toRingHom) ≫ U.2.1)
            (t : ((sheafToPresheaf _ _).obj F).obj (op U.1)),
            let V : (geometricPointFiber B (Spec (.of K)) hK sbar).Elements := ⟨q⟩
            ConcreteCategory.hom (α.app F).hom
                (ConcreteCategory.hom ((e.functor.obj F).obj.obj.ρ σ).asHom
                  (ConcreteCategory.hom (α.app F).inv
                    (abelianEtaleStalkGerm.{u, v} B (Spec (.of K)) hK sbar F U t))) =
              abelianEtaleStalkGerm.{u, v} B (Spec (.of K)) hK sbar F V t }
```

Declarations registered for the tag:

- [`AlgebraicGeometry.etaleContinuousGModuleEquivalence`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleStalkModules.lean#L245), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleStalkModules.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleStalkModules.lean#L304) (StacksFrontier): “the stalk equivalence in the coefficient category of continuous group cohomology”.

## Tag 03QU, a lemma

[Tag 03QU](https://stacks.math.columbia.edu/tag/03QU) in the Stacks Project.

**`AlgebraicGeometry.etaleH0AddEquivGaloisInvariants`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/GaloisInvariants.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/GaloisInvariants.lean#L232). The attribute's comment: “part (2)”.

> Let `K` be a field, let `sbar` be a geometric point of `Spec K` with absolute Galois group
> `G`, and let `F` be an abelian sheaf on the small étale site of `Spec K` corresponding to the
> `G`-module `M`.  Then the degree-zero étale cohomology of `Spec K` with coefficients in `F` is
> the group `M ^ G` of Galois invariants.

```lean
def etaleH0AddEquivGaloisInvariants
    [HasSheafify (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v}]
    [HasExt.{w} (Sheaf (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v})] :
    Sheaf.H.{w, max u v} F 0 ≃+ ↥(etaleStalkGaloisInvariants.{u, v} B K hK sbar F)
```

**`AlgebraicGeometry.etaleH0AddEquivGaloisInvariants_coe`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/GaloisInvariants.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/GaloisInvariants.lean#L243). The attribute's comment: “part (2), the comparison is taking germs at the geometric point”.

> The identification of degree-zero étale cohomology with the Galois invariants is taking
> germs at the geometric point: a cohomology class is sent to the germ of the global section which
> represents it.

```lean
theorem etaleH0AddEquivGaloisInvariants_coe
    [HasSheafify (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v}]
    [HasExt.{w} (Sheaf (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v})]
    (x : Sheaf.H.{w, max u v} F 0) :
    (etaleH0AddEquivGaloisInvariants B K hK sbar F x).1 =
      etaleGlobalSectionGerm.{u, v} B K hK sbar (abelianEtaleSheafOfSets.{u, v} B K hK F)
        (Sheaf.H.equiv₀ F (SmallEtale.finalIsTerminal B (Spec (.of K)) hK) x)
```

**`AlgebraicGeometry.etaleH0AddEquivGaloisInvariants_abelianEtaleStalkGerm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/GaloisInvariants.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/GaloisInvariants.lean#L256). The attribute's comment: “part (2), the comparison in the abelian stalk”.

> Read in the abelian-group-valued stalk, the identification of degree-zero étale cohomology
> with the Galois invariants sends a cohomology class to the germ, at the final pointed étale
> neighbourhood, of the global section which represents it.

```lean
theorem etaleH0AddEquivGaloisInvariants_abelianEtaleStalkGerm
    [HasSheafify (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v}]
    [HasExt.{w} (Sheaf (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v})]
    (x : Sheaf.H.{w, max u v} F 0) :
    etaleGaloisModuleAddEquivStalk.{u, v} B K hK sbar F
        (etaleH0AddEquivGaloisInvariants B K hK sbar F x).1 =
      abelianEtaleStalkGerm.{u, v} B (Spec (.of K)) hK sbar F
        (finalPointedNeighborhood B K hK sbar)
        (Sheaf.H.equiv₀ F (SmallEtale.finalIsTerminal B (Spec (.of K)) hK) x)
```

**`AlgebraicGeometry.additiveSheafHAddEquivContinuousGroupCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/AdditiveGroupGaloisModule.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/AdditiveGroupGaloisModule.lean#L269). The attribute's comment: “part (3) at 𝐆\_a, in every degree: the degree-q étale cohomology of the spectrum of a field with coefficients in the additive group is the degree-q continuous group cohomology of the absolute Galois group with coefficients in the separable closure under addition. This is the general objectwise form of part (3) on Mathlib's small étale site, smallEtaleSheafCohomologyAddEquivContinuousGroupCohomology, with its Galois module computed at 𝐆\_a by additiveContinuousGModuleIso -- the stalk computation additiveStalkIsoSepClosure packaged with its germwise Galois equivariance additiveSectionEval\_galoisFiberAction into an isomorphism of discrete Galois modules. Nothing is assumed of the field and nothing is carried. NOT proved here: parts (1) and (2) of the tag, which are separate registrations”.

> **Stacks Project, Tag 03QU, part (3), at `𝐆_a`.**  For a field `K`, a geometric point `sbar`
> of `Spec K` and every degree `q`,
>
> `H^q_étale(Spec K, 𝐆_a) ≅ H^q(Gal(Kˢᵉᵖ/κ), Kˢᵉᵖ)`,
>
> `κ` being the residue field at the image of `sbar` and `Kˢᵉᵖ` the Galois module with addition as
> group law.  This is the general comparison
> `AlgebraicGeometry.smallEtaleSheafCohomologyAddEquivContinuousGroupCohomology` with its Galois
> module identified at `𝐆_a` by `AlgebraicGeometry.additiveContinuousGModuleIso`.

```lean
def additiveSheafHAddEquivContinuousGroupCohomology (q : ℕ) :
    Sheaf.H.{u + 1, u + 1}
        (Stacks.ArtinSchreier.additiveSheaf.{u, u + 1} (Spec (.of K))) q ≃+
      continuousGroupCohomology.{u, u + 1} (GeometricPoint.absoluteGaloisGroup sbar) q
        (sepClosureAddGModule K sbar)
```

**`AlgebraicGeometry.etaleRightDerivedGammaIsoContinuousGroupCohomologyFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleGaloisCohomologyComparison.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleGaloisCohomologyComparison.lean#L134). The attribute's comment: “part (3), as an isomorphism of functors, with étale cohomology as the right derived functor of global sections”.

> In every degree `q`, the `q`-th right derived functor of the global sections functor
> `CategoryTheory.Sheaf.Γ` of the small étale site of `Spec K` is the stalk equivalence
> `AlgebraicGeometry.etaleContinuousGModuleEquivalence` followed by the `q`-th continuous group
> cohomology functor of the absolute Galois group.

```lean
def etaleRightDerivedGammaIsoContinuousGroupCohomologyFunctor (q : ℕ) :
    (Sheaf.Γ (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{u + 1}).rightDerived q ≅
      (etaleContinuousGModuleEquivalence.{u, u + 1} B K hK sbar).functor ⋙
        continuousGroupCohomologyFunctor.{u, u + 1}
          (GeometricPoint.absoluteGaloisGroup sbar) q
```

**`AlgebraicGeometry.etaleSheafCohomologyIsoContinuousGroupCohomologyFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleGaloisCohomologyComparison.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleGaloisCohomologyComparison.lean#L158). The attribute's comment: “part (3), in every degree, as a natural isomorphism of functors: sheaf cohomology on the small étale site of the spectrum of a field is the stalk equivalence of 04JQ followed by the continuous group cohomology functor of 04JR”.

> Let `K` be a field, let `sbar` be a geometric point of `Spec K` and let `G` be the absolute
> Galois group at `sbar`. For every `q`, Mathlib's degree-`q` sheaf cohomology functor
> `CategoryTheory.Sheaf.functorH` on the small étale site of `Spec K` is the stalk equivalence
> `AlgebraicGeometry.etaleContinuousGModuleEquivalence` followed by the degree-`q` continuous group
> cohomology functor of `G`.

```lean
def etaleSheafCohomologyIsoContinuousGroupCohomologyFunctor (q : ℕ) :
    Sheaf.functorH.{u + 1, u + 1, u, u + 1}
        (SmallEtale.topology B (Spec (.of K)) hK) q ≅
      (etaleContinuousGModuleEquivalence.{u, u + 1} B K hK sbar).functor ⋙
        continuousGroupCohomologyFunctor.{u, u + 1}
          (GeometricPoint.absoluteGaloisGroup sbar) q
```

**`AlgebraicGeometry.etaleSheafCohomologyAddEquivContinuousGroupCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleGaloisCohomologyComparison.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleGaloisCohomologyComparison.lean#L175). The attribute's comment: “part (3): in every degree q, the degree-q étale cohomology of the spectrum of a field with coefficients in an abelian sheaf is the degree-q continuous group cohomology of the absolute Galois group with coefficients in the sheaf's module of 04JQ”.

> Let `K` be a field, let `sbar` be a geometric point of `Spec K` with absolute Galois group `G`,
> and let `F` be an abelian sheaf on the small étale site of `Spec K`, corresponding to the
> `G`-module `M` under `AlgebraicGeometry.etaleContinuousGModuleEquivalence`. Then for every `q`
>
> `H^q_étale(Spec K, F) = H^q(G, M)`.

```lean
def etaleSheafCohomologyAddEquivContinuousGroupCohomology
    (F : Sheaf (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{u + 1}) (q : ℕ) :
    Sheaf.H.{u + 1, u + 1} F q ≃+
      continuousGroupCohomology.{u, u + 1} (GeometricPoint.absoluteGaloisGroup sbar) q
        ((etaleContinuousGModuleEquivalence.{u, u + 1} B K hK sbar).functor.obj F)
```

**`AlgebraicGeometry.etaleDerivedGlobalSectionsIsoDerivedGaloisInvariants`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleGaloisCohomologyComparison.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleGaloisCohomologyComparison.lean#L211). The attribute's comment: “part (1)”.

> Let `K` be a field, let `sbar` be a geometric point of `Spec K` with absolute Galois group `G`,
> let `F` be an abelian sheaf on the small étale site of `Spec K` and let `M` be the discrete
> `G`-module it corresponds to under `AlgebraicGeometry.etaleContinuousGModuleEquivalence`. Then in
> the derived category of abelian groups there is a canonical isomorphism
>
> `RΓ(Spec K, F) ≅ RΓ_G(M)`
>
> between the derived global sections of `F` and the derived `G`-invariants of `M`, both computed
> on bounded below derived categories and mapped to the unbounded one by `DerivedCategory.Plus.ι`.

```lean
def etaleDerivedGlobalSectionsIsoDerivedGaloisInvariants
    (F : Sheaf (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{u + 1}) :
    DerivedCategory.Plus.ι.obj
        ((Sheaf.Γ (SmallEtale.topology B (Spec (.of K)) hK)
          AddCommGrpCat.{u + 1}).rightDerivedFunctorPlus.obj
            ((DerivedCategory.Plus.singleFunctor _ 0).obj F)) ≅
      DerivedCategory.Plus.ι.obj
        ((continuousGModuleInvariants.{u, u + 1}
          (GeometricPoint.absoluteGaloisGroup sbar)).rightDerivedFunctorPlus.obj
            ((DerivedCategory.Plus.singleFunctor _ 0).obj
              ((etaleContinuousGModuleEquivalence.{u, u + 1} B K hK sbar).functor.obj F)))
```

**`AlgebraicGeometry.smallEtaleSheafCohomologyIsoContinuousGroupCohomologyFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleGaloisCohomologyComparison.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleGaloisCohomologyComparison.lean#L274). The attribute's comment: “part (3), in every degree, on Mathlib's small étale site of the spectrum of a field: sheaf cohomology there is restriction to the site of 021B followed by the stalk equivalence of 04JQ and the continuous group cohomology functor of 04JR”.

> For every `q`, Mathlib's degree-`q` sheaf cohomology functor on its small étale site of
> `Spec K` is the restriction `AlgebraicGeometry.smallEtaleSheafRestriction` to the site
> `AlgebraicGeometry.SmallEtale.topology`, followed by the stalk equivalence
> `AlgebraicGeometry.etaleContinuousGModuleEquivalence` and the degree-`q` continuous group
> cohomology functor of the absolute Galois group.

```lean
def smallEtaleSheafCohomologyIsoContinuousGroupCohomologyFunctor (q : ℕ) :
    Sheaf.functorH.{u + 1, u + 1, u, u + 1}
        ((Spec (.of K) : Scheme.{u})).smallEtaleTopology q ≅
      smallEtaleSheafRestriction B K hK ⋙
        ((etaleContinuousGModuleEquivalence.{u, u + 1} B K hK sbar).functor ⋙
          continuousGroupCohomologyFunctor.{u, u + 1}
            (GeometricPoint.absoluteGaloisGroup sbar) q)
```

**`AlgebraicGeometry.smallEtaleSheafCohomologyAddEquivContinuousGroupCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleGaloisCohomologyComparison.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleGaloisCohomologyComparison.lean#L298). The attribute's comment: “part (3) on Mathlib's small étale site, objectwise: the degree-q étale cohomology group of the spectrum of a field with coefficients in an abelian sheaf is the degree-q continuous group cohomology of the absolute Galois group with coefficients in the sheaf's Galois module”.

> For every abelian sheaf `F` on Mathlib's small étale site of `Spec K` and every degree `q`,
>
> `H^q_étale(Spec K, F) = H^q(G, M)`,
>
> `M` being the Galois module of the restriction of `F` to the site
> `AlgebraicGeometry.SmallEtale.topology`.

```lean
def smallEtaleSheafCohomologyAddEquivContinuousGroupCohomology
    (F : Sheaf ((Spec (.of K) : Scheme.{u})).smallEtaleTopology AddCommGrpCat.{u + 1})
    (q : ℕ) :
    Sheaf.H.{u + 1, u + 1} F q ≃+
      continuousGroupCohomology.{u, u + 1} (GeometricPoint.absoluteGaloisGroup sbar) q
        ((etaleContinuousGModuleEquivalence.{u, u + 1} B K hK sbar).functor.obj
          ((smallEtaleSheafRestriction B K hK).obj F))
```

**`AlgebraicGeometry.etaleGlobalSectionsIsoInvariants`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleStalkModules.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleStalkModules.lean#L225). The attribute's comment: “part (2), as a natural isomorphism of functors, in the abelian-group encoding of discrete Galois modules”.

> **Stacks Project, Tag 03QU, part (2), as an isomorphism of functors.**  Over a field, global
> sections of an abelian étale sheaf and the Galois invariants of its module of Tag 04JQ are
> isomorphic functors to abelian groups, by taking germs at the geometric point.

```lean
def etaleGlobalSectionsIsoInvariants :
    (sheafSections (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v}).obj
        (op (SmallEtale.final B (Spec (.of K)) hK)) ≅
      (abelianEtaleStalkEquivalence.{u, v} B K hK sbar).functor ⋙
        continuousGAddCommGrpInvariants.{u, max u v}
          (GeometricPoint.absoluteGaloisGroup sbar)
```

**`AlgebraicGeometry.etaleGlobalSectionsIsoContinuousGModuleInvariants`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleStalkModules.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleStalkModules.lean#L257). The attribute's comment: “part (2), as a natural isomorphism of functors, in the coefficient category of continuousGroupCohomology”.

> **Stacks Project, Tag 03QU, part (2), as an isomorphism of functors, in the vocabulary of
> continuous group cohomology.**  Global sections of an abelian étale sheaf over a field are the
> `continuousGModuleInvariants` of the discrete Galois module of Tag 04JQ.

```lean
def etaleGlobalSectionsIsoContinuousGModuleInvariants :
    (sheafSections (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v}).obj
        (op (SmallEtale.final B (Spec (.of K)) hK)) ≅
      (etaleContinuousGModuleEquivalence.{u, v} B K hK sbar).functor ⋙
        continuousGModuleInvariants.{u, max u v}
          (GeometricPoint.absoluteGaloisGroup sbar)
```

**`AlgebraicGeometry.etaleGammaIsoGaloisInvariants`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleStalkModules.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleStalkModules.lean#L281). The attribute's comment: “part (2), as an isomorphism of functors on the global sections functor”.

> **Stacks Project, Tag 03QU, part (2), functorially, for the global sections functor of the
> site.**  The global sections functor `CategoryTheory.Sheaf.Γ` of the small étale site of the
> spectrum of a field is the functor of Galois invariants of the module of Tag 04JQ, in the
> abelian-group encoding of discrete Galois modules.  This is
> `AlgebraicGeometry.etaleGlobalSectionsIsoInvariants` with sections over the final object
> rewritten as global sections.

```lean
def etaleGammaIsoGaloisInvariants
    [HasSheafify (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v}] :
    Sheaf.Γ (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v} ≅
      (abelianEtaleStalkEquivalence.{u, v} B K hK sbar).functor ⋙
        continuousGAddCommGrpInvariants.{u, max u v}
          (GeometricPoint.absoluteGaloisGroup sbar)
```

**`AlgebraicGeometry.etaleGammaIsoContinuousGModuleInvariants`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleStalkModules.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/EtaleStalkModules.lean#L295). The attribute's comment: “part (2), as an isomorphism of functors with the module invariants”.

> **Stacks Project, Tag 03QU, part (2), functorially and in the module encoding, for the global
> sections functor of the site.**  The global sections functor `CategoryTheory.Sheaf.Γ` of the
> small étale site of the spectrum of a field is the stalk equivalence of Tag 04JQ followed by the
> functor of `G`-invariants of discrete modules over the absolute Galois group.

```lean
def etaleGammaIsoContinuousGModuleInvariants
    [HasSheafify (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v}] :
    Sheaf.Γ (SmallEtale.topology B (Spec (.of K)) hK) AddCommGrpCat.{max u v} ≅
      (etaleContinuousGModuleEquivalence.{u, v} B K hK sbar).functor ⋙
        continuousGModuleInvariants.{u, max u v}
          (GeometricPoint.absoluteGaloisGroup sbar)
```

**`AlgebraicGeometry.multiplicativeSheafHAddEquivContinuousGroupCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupGaloisModule.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupGaloisModule.lean#L260). The attribute's comment: “part (3) at 𝐆\_m, in every degree: the degree-q étale cohomology of the spectrum of a field with coefficients in the multiplicative group is the degree-q continuous group cohomology of the absolute Galois group with coefficients in the units of the separable closure. This is the general objectwise form of part (3) on Mathlib's small étale site, smallEtaleSheafCohomologyAddEquivContinuousGroupCohomology, with its Galois module computed at 𝐆\_m by multiplicativeContinuousGModuleIso -- the stalk computation multiplicativeStalkIsoUnits packaged with its germwise Galois equivariance multiplicativeSectionEval\_galoisFiberAction into an isomorphism of discrete Galois modules. Nothing is assumed of the field and nothing is carried. NOT proved here: parts (1) and (2) of the tag, which are separate registrations”.

> For a field `K`, a geometric point `sbar` of `Spec K` and every degree `q`,
>
> `H^q_étale(Spec K, 𝐆_m) ≅ H^q(Gal(Kˢᵉᵖ/κ), (Kˢᵉᵖ)ˣ)`,
>
> `κ` being the residue field at the image of `sbar`.

```lean
def multiplicativeSheafHAddEquivContinuousGroupCohomology (q : ℕ) :
    Sheaf.H.{u + 1, u + 1}
        (Stacks.Kummer.multiplicativeSheaf.{u, u + 1} (Spec (.of K))) q ≃+
      continuousGroupCohomology.{u, u + 1} (GeometricPoint.absoluteGaloisGroup sbar) q
        (sepClosureUnitsGModule K sbar)
```

## Tag 03QV, an example

[Tag 03QV](https://stacks.math.columbia.edu/tag/03QV) in the Stacks Project.

**`AlgebraicGeometry.stacks03QV`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/SheavesOnAPoint.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/SheavesOnAPoint.lean#L138).

> **Stacks Project, Tag 03QV, whole.**  Sheaves on `Spec(K)_étale` for `K` a field, with
> `G = Gal(Kˢᵉᵖ/K)` the absolute Galois group.
>
> Under the equivalence of Tag 04JQ between abelian sheaves on the small étale site of `Spec K` and
> discrete `G`-modules: (1) the constant sheaf `𝐙/n𝐙` corresponds to `𝐙/n𝐙` with the trivial
> `G`-action, (2) `𝐆_m` corresponds to `(Kˢᵉᵖ)^*`, (3) `𝐆_a` corresponds to `(Kˢᵉᵖ, +)`, and
> (4) `μ_n` corresponds to `μ_n(Kˢᵉᵖ)`, each with its `G`-action.  Moreover
>
>   `0 = Pic(Spec K) = H¹_étale(Spec(K)_étale, 𝐆_m) = H¹(G, (Kˢᵉᵖ)^*)`,
>
> which is Hilbert's 90 theorem, and, for every `i ≥ 1`,
>
>   `0 = H^i(Spec K, 𝒪) = H^i_étale(Spec(K)_étale, 𝐆_a) = H^i(G, Kˢᵉᵖ)`.
>
> The module docstring lists the declaration proving each component.

```lean
public def stacks03QV :
    ((etaleContinuousGModuleEquivalence.{u, u + 1} B K hK sbar).functor.obj
        (constantEtaleSheaf B K hK (ULift.{u + 1} (ZMod n))) ≅
      constantGModule K sbar (ULift.{u + 1} (ZMod n))) ×
    ((etaleContinuousGModuleEquivalence.{u, u + 1} B K hK sbar).functor.obj
        (multiplicativeSheafRestriction B K hK) ≅ sepClosureUnitsGModule K sbar) ×
    ((etaleContinuousGModuleEquivalence.{u, u + 1} B K hK sbar).functor.obj
        (additiveSheafRestriction B K hK) ≅ sepClosureAddGModule K sbar) ×
    ((etaleContinuousGModuleEquivalence.{u, u + 1} B K hK sbar).functor.obj
        (rootsOfUnitySheafRestriction B K hK n) ≅ sepClosureRootsOfUnityGModule K sbar n) ×
    (Sheaf.H.{u + 1, u + 1}
        (Stacks.Kummer.multiplicativeSheaf.{u, u + 1} (Spec (.of K))) 1 ≃+
      continuousGroupCohomology.{u, u + 1} (GeometricPoint.absoluteGaloisGroup sbar) 1
        (sepClosureUnitsGModule K sbar)) ×
    (∀ i : ℕ, Hgroup (Spec (CommRingCat.of K)).ringCatSheaf ⊤ (i + 1)
          (Scheme.unitModule (Spec (CommRingCat.of K))) ≃+
        Sheaf.H.{u + 1, u + 1}
          (Stacks.ArtinSchreier.additiveSheaf.{u, u + 1} (Spec (.of K))) (i + 1)) ×
    (∀ q : ℕ, Sheaf.H.{u + 1, u + 1}
          (Stacks.ArtinSchreier.additiveSheaf.{u, u + 1} (Spec (.of K))) q ≃+
        continuousGroupCohomology.{u, u + 1} (GeometricPoint.absoluteGaloisGroup sbar) q
          (sepClosureAddGModule K sbar)) ×
    PLift (Subsingleton (Spec (CommRingCat.of K)).picardGroup ∧
      Subsingleton (Sheaf.H.{u + 1, u + 1}
        (Stacks.Kummer.multiplicativeSheaf.{u, u + 1} (Spec (.of K))) 1) ∧
      IsZero (continuousGroupCohomology.{u, u + 1}
        (GeometricPoint.absoluteGaloisGroup sbar) 1 (sepClosureUnitsGModule K sbar)) ∧
      (∀ i : ℕ, 0 < i → IsZero (Hgroup (Spec (CommRingCat.of K)).ringCatSheaf ⊤ i
        (Scheme.unitModule (Spec (CommRingCat.of K))))) ∧
      (∀ i : ℕ, 0 < i → Subsingleton (Sheaf.H.{u + 1, u + 1}
        (Stacks.ArtinSchreier.additiveSheaf.{u, u + 1} (Spec (.of K))) i)) ∧
      (∀ i : ℕ, 0 < i → IsZero (continuousGroupCohomology.{u, u + 1}
        (GeometricPoint.absoluteGaloisGroup sbar) i (sepClosureAddGModule K sbar))))
```

## Tag 0D1W, a lemma

[Tag 0D1W](https://stacks.math.columbia.edu/tag/0D1W) in the Stacks Project.

**`Stacks.EtaleCohomology.SmallEtaleModules.allModules_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/ZeroDimensionalLocalRing.lean, line 1199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/ZeroDimensionalLocalRing.lean#L1199).

> Every module on the small étale site of a zero-dimensional local ring is
> quasi-coherent.

```lean
public theorem allModules_isQuasicoherent
    (R : Type u) [CommRing R] [IsLocalRing R] (hdim : ringKrullDim R = 0)
    (B : BigEtaleSite.{u})
    (hS : B.Contains (Spec (.of R)))
    (F : SheafOfModules.{u}
      (AlgebraicGeometry.SmallEtale.structureSheaf B (Spec (.of R)) hS)) :
    F.IsQuasicoherent
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.59, Tag 03QQ](https://stacks.math.columbia.edu/tag/03QQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
