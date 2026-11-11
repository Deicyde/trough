---
declaration: section
origin: cited
lean: AlgebraicGeometry.canonicalDescentData_etale, AlgebraicGeometry.etaleDescentFunctor, AlgebraicGeometry.etaleDescentFunctor_faithful, AlgebraicGeometry.etaleDescentFunctor_fullyFaithful_of_submersive_baseChange, AlgebraicGeometry.etaleDescentFunctor_fullyFaithful_of_universallyClosed, AlgebraicGeometry.etaleDescentFunctor_fullyFaithful_of_universallyOpen, AlgebraicGeometry.etaleDescentFunctor_fullyFaithful_of_quasiCompact_of_flat, AlgebraicGeometry.DescentDatum.isEtaleEffective_of_isOpenCover
statement: formalized
proof: formalized
---

# 41.20 Descending étale morphisms

Section 41.20 of the Stacks Project, [Tag 0BTH](https://stacks.math.columbia.edu/tag/0BTH). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BTI, an equation

[Tag 0BTI](https://stacks.math.columbia.edu/tag/0BTI) in the Stacks Project.

**`AlgebraicGeometry.canonicalDescentData_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Descent.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Descent.lean#L91). The attribute's comment: “étale objects”.

> The canonical descent datum of an étale scheme over `S` has an étale underlying scheme
> over `X`.

```lean
theorem canonicalDescentData_etale (f : X ⟶ S) (U : S.Etale) :
    IsEtaleDescentData f
      ((DescentData.canonicalFunctor f).obj ((Scheme.Etale.forget S).obj U))
```

**`AlgebraicGeometry.etaleDescentFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Descent.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Descent.lean#L113). The attribute's comment: “the functor”.

> The canonical functor, given by pullback along `f`, from étale `S`-schemes to descent data
> relative to `f` with étale underlying `X`-scheme.

```lean
def etaleDescentFunctor (f : X ⟶ S) :
    S.Etale ⥤ EtaleDescentData f
```

## Tag 0BTJ, a lemma

[Tag 0BTJ](https://stacks.math.columbia.edu/tag/0BTJ) in the Stacks Project.

**`AlgebraicGeometry.etaleDescentFunctor_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/DescentFullyFaithful.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/DescentFullyFaithful.lean#L128).

> Pullback to a surjective scheme detects equality of morphisms
> between étale schemes over the base.

```lean
theorem etaleDescentFunctor_faithful (f : X ⟶ S) [Surjective f] :
    (etaleDescentFunctor f).Faithful
```

## Tag 0BTK, a lemma

[Tag 0BTK](https://stacks.math.columbia.edu/tag/0BTK) in the Stacks Project.

**`AlgebraicGeometry.etaleDescentFunctor_fullyFaithful_of_submersive_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/DescentFullyFaithful.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/DescentFullyFaithful.lean#L275). References: SGA 1 IX (3.4), “fully faithful”.

> Étale descent is fully faithful when the morphism and all its
> étale base changes are submersive.

```lean
theorem etaleDescentFunctor_fullyFaithful_of_submersive_baseChange (f : X ⟶ S)
    (hf : Topology.IsQuotientMap f)
    (hbase : ∀ {U : Scheme.{u}} (g : U ⟶ S), Etale g →
      Topology.IsQuotientMap (pullback.snd f g)) :
    Nonempty (etaleDescentFunctor f).FullyFaithful
```

## Tag 0BTL, a lemma

[Tag 0BTL](https://stacks.math.columbia.edu/tag/0BTL) in the Stacks Project.

**`AlgebraicGeometry.etaleDescentFunctor_fullyFaithful_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/DescentFullyFaithful.lean, line 508](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/DescentFullyFaithful.lean#L508). The attribute's comment: “universally\_closed”. References: SGA 1 IX (6.9), “fully faithful half”.

> Étale descent along a
> surjective universally closed morphism is fully faithful.

```lean
theorem etaleDescentFunctor_fullyFaithful_of_universallyClosed (f : X ⟶ S) [Surjective f]
    [UniversallyClosed f] : Nonempty (etaleDescentFunctor f).FullyFaithful
```

**`AlgebraicGeometry.etaleDescentFunctor_fullyFaithful_of_universallyOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/DescentFullyFaithful.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/DescentFullyFaithful.lean#L518). The attribute's comment: “universally\_open”.

> Étale descent along a
> surjective universally open morphism is fully faithful.

```lean
theorem etaleDescentFunctor_fullyFaithful_of_universallyOpen (f : X ⟶ S) [Surjective f]
    [UniversallyOpen f] : Nonempty (etaleDescentFunctor f).FullyFaithful
```

**`AlgebraicGeometry.etaleDescentFunctor_fullyFaithful_of_quasiCompact_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/DescentFullyFaithful.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/DescentFullyFaithful.lean#L528). The attribute's comment: “quasi\_compact\_flat”.

> Étale descent along a
> surjective quasi-compact flat morphism is fully faithful.

```lean
theorem etaleDescentFunctor_fullyFaithful_of_quasiCompact_of_flat (f : X ⟶ S) [Surjective f]
    [QuasiCompact f] [Flat f] : Nonempty (etaleDescentFunctor f).FullyFaithful
```

## Tag 0BTM, a lemma

[Tag 0BTM](https://stacks.math.columbia.edu/tag/0BTM) in the Stacks Project.

**`AlgebraicGeometry.DescentDatum.isEtaleEffective_of_isOpenCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Scheme/EtaleBaseLocal.lean, line 659](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Scheme/EtaleBaseLocal.lean#L659). References: SGA 1 IX (4.3), “sufficiency”; SGA 1 VIII (7.3), “partial”.

> **Effectivity of an étale descent datum is Zariski-local on the base.** Let `f : X ⟶ S` be a
> morphism of schemes and `(V, φ)` a descent datum relative to `X/S` with `V ⟶ X` étale, and let
> `S = ⋃ Sᵢ` be an open covering. Assume that the pullback of `(V, φ)` to `X ×_S Sᵢ / Sᵢ` is
> effective by an étale scheme for every `i`, that the étale descent functor for
> `X ×_S (Sᵢ ∩ Sⱼ) ⟶ Sᵢ ∩ Sⱼ` is fully faithful, and that the étale descent functor for
> `X ×_S (Sᵢ ∩ Sⱼ ∩ Sₖ) ⟶ Sᵢ ∩ Sⱼ ∩ Sₖ` is faithful. Then `(V, φ)` is effective, by a scheme
> étale over `S`.

```lean
theorem isEtaleEffective_of_isOpenCover {S X : Scheme.{u}} {f : X ⟶ S} (D : DescentDatum f)
    [Etale D.over.hom] {ι : Type v} (U : ι → S.Opens) (hU : ⨆ i, U i = ⊤)
    (hlocal : ∀ i, (D.baseDatum (U i)).IsEtaleEffective)
    (hpair : ∀ i j, (etaleDescentFunctor (pullback.snd f (U i ⊓ U j).ι)).FullyFaithful)
    (htriple : ∀ i j k,
      (etaleDescentFunctor (pullback.snd f (U i ⊓ U j ⊓ U k).ι)).Faithful) :
    D.IsEtaleEffective
```

## Tag 0BTN, a lemma

[Tag 0BTN](https://stacks.math.columbia.edu/tag/0BTN) in the Stacks Project.

**`Stacks.Etale.exists_coprod_isFinite_and_isEmpty_closedFiber`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DescentEffectivity/HenselianSplitting.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/DescentEffectivity/HenselianSplitting.lean#L387).

> **Stacks Project, Tag 0BTN.** A quasi-compact separated étale scheme over a henselian pair,
> with finite closed fibre, is the disjoint union of a finite scheme over the base and a scheme
> with empty closed fibre.

```lean
lemma exists_coprod_isFinite_and_isEmpty_closedFiber
    (A : Type u) [CommRing A] (I : Ideal A) (hI : HenselianPair A I)
    (U : Scheme.{u}) (f : U ⟶ Spec (.of A))
    [QuasiCompact f] [IsSeparated f] [Etale f]
    [IsFinite (pullback.snd f
      (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))))] :
    ∃ (Ufin Uaway : Scheme.{u}) (iFin : Ufin ⟶ U) (iAway : Uaway ⟶ U),
      IsIso (coprod.desc iFin iAway) ∧ IsFinite (iFin ≫ f) ∧
        IsEmpty ((pullback (iAway ≫ f)
          (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))) : Scheme.{u}))
```

## Tag 0BTP, a proposition

[Tag 0BTP](https://stacks.math.columbia.edu/tag/0BTP) in the Stacks Project.

**`AlgebraicGeometry.fullyFaithful_quasiCompactSeparatedEtaleDescentFunctor_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/IntegralEtaleDescent.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/IntegralEtaleDescent.lean#L224). The attribute's comment: “the fully faithful half of the equivalence”.

> **Stacks Project, Tag 0BTP, the fully faithful half.** Let `f : X ⟶ S` be a surjective
> integral morphism. The functor of Tag 0BTI, restricted to the schemes quasi-compact, separated
> and étale over `S` and to the descent data relative to `X/S` whose underlying `X`-scheme is
> quasi-compact, separated and étale, is fully faithful.
>
> Fullness is Tag 0BTL for a surjective universally closed morphism, which a surjective integral
> morphism is, and faithfulness is Tag 0BTJ.

```lean
theorem fullyFaithful_quasiCompactSeparatedEtaleDescentFunctor_of_isIntegralHom
    (f : X ⟶ S) [Surjective f] [IsIntegralHom f] :
    Nonempty (quasiCompactSeparatedEtaleDescentFunctor f).FullyFaithful
```

**`AlgebraicGeometry.isEquivalence_quasiCompactSeparatedEtaleDescentFunctor_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DescentEffectivity/HenselianCase.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/DescentEffectivity/HenselianCase.lean#L267). References: SGA 1 IX (4.11), “more general”; SGA 1 IX (4.7).

> **[Stacks, Tag 0BTP](https://stacks.math.columbia.edu/tag/0BTP).** Let `f : X ⟶ S` be a
> surjective integral morphism. The functor of Tag 0BTI induces an equivalence between the category
> of schemes quasi-compact, separated and étale over `S` and the category of descent data `(V, φ)`
> relative to `X/S` with `V` quasi-compact, separated and étale over `X`.

```lean
theorem isEquivalence_quasiCompactSeparatedEtaleDescentFunctor_of_isIntegralHom
    {S X : Scheme.{u}} (f : X ⟶ S) [Surjective f] [IsIntegralHom f] :
    (quasiCompactSeparatedEtaleDescentFunctor f).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.20, Tag 0BTH](https://stacks.math.columbia.edu/tag/0BTH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
