---
declaration: section
origin: cited
lean: ProetaleWContractible.everyProetaleCoverHasZariskiRefinement_of_wContractible, ProetaleWContractible.isWContractible_of_zariskiRefinement, AlgebraicGeometry.ProEtale.isWContractible_globalSections_tfae, AlgebraicGeometry.ProEtale.BigProetaleOver.hasEnoughObjects_isAffine_isWContractible, AlgebraicGeometry.ProEtale.exists_covering_affine_wContractible, AlgebraicGeometry.ProEtale.hasEnoughObjects_isAffine_isWeaklyContractible, AlgebraicGeometry.ProEtale.hasEnoughWeaklyContractibleObjects_proetale, AlgebraicGeometry.ProEtale.affineIndEtaleProetale_hasEnough_quasiCompact_weaklyContractible
statement: formalized
proof: formalized
---

# 61.13 Weakly contractible objects

Section 61.13 of the Stacks Project, [Tag 0F4N](https://stacks.math.columbia.edu/tag/0F4N). 5 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 098F, a lemma

[Tag 098F](https://stacks.math.columbia.edu/tag/098F) in the Stacks Project.

Declarations registered for the tag:

- [`ProetaleWContractible.everyProetaleCoverHasZariskiRefinement_of_wContractible`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/WeaklyContractible/WContractibleRings.lean#L863), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractible.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractible.lean#L36) (StacksFrontier): “w-contractible implies the covering-refinement condition”.
- [`ProetaleWContractible.isWContractible_of_zariskiRefinement`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/WeaklyContractible/WContractibleRings.lean#L320), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractible.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractible.lean#L39) (StacksFrontier): “the covering-refinement condition implies w-contractibility”.

## Tag 098H, a lemma

[Tag 098H](https://stacks.math.columbia.edu/tag/098H) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isWContractible_globalSections_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/ClopenRefinement.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/ClopenRefinement.lean#L497).

> **Stacks 098H.** For an affine object `T` of a chosen big pro-étale site the following are
> equivalent: the ring of global sections of `T` is w-contractible; `T` is a weakly contractible
> object of the site; every covering sieve of `T` is refined by a finite family of objects of the
> site whose images form a disjoint clopen cover of `T`.

```lean
theorem isWContractible_globalSections_tfae (B : BigProetaleSite.{u}) (T : B.Scheme)
    [IsAffine T.obj] :
    [IsWContractible.{u, u} Γ(T.obj, ⊤),
      B.topology.IsWeaklyContractible T,
      ∀ S : Sieve T, S ∈ B.topology T →
        ∃ (n : ℕ) (U : Fin n → B.Scheme) (f : (i : Fin n) → U i ⟶ T),
          IsClopenDecompositionCover (fun i ↦ (U i).obj) (fun i ↦ B.inclusion.map (f i)) ∧
          ∀ i, S.arrows (f i)].TFAE
```

## Tag 098I, a lemma

[Tag 098I](https://stacks.math.columbia.edu/tag/098I) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.BigProetaleOver.hasEnoughObjects_isAffine_isWContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/CompactGeneration.lean#L176). The attribute's comment: “in the big pro-étale site of a scheme”.

> Every object of the big pro-étale site of `S` is covered by objects whose underlying schemes
> are affine with w-contractible ring of global sections.

```lean
theorem hasEnoughObjects_isAffine_isWContractible (T : BigProetaleOver B S hS) :
    ∃ (I : Type (u + 1)) (V : I → BigProetaleOver B S hS) (p : (i : I) → V i ⟶ T),
      Sieve.ofArrows V p ∈ topology B S hS T ∧
        ∀ i, IsAffine ((toScheme B S hS).obj (V i)) ∧
          IsWContractible.{u, u} Γ((toScheme B S hS).obj (V i), ⊤)
```

**`AlgebraicGeometry.ProEtale.exists_covering_affine_wContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleCovers.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleCovers.lean#L81).

> **Stacks 098I.** Every object `T` of a chosen big pro-étale site admits a chosen covering
> family `{T_i → T}` of that site with each `T_i` affine and the spectrum of a w-contractible
> ring; in particular each `T_i` is a weakly contractible object of the site.
>
> The covering is the chosen representative of the composite of the chosen affine open cover of
> the underlying scheme of `T` with the single affine w-contractible cover of each of its
> members.

```lean
theorem exists_covering_affine_wContractible :
    ∃ E : PreZeroHypercover.{u + 1} T,
      B.covering ⟨T, E⟩ ∧
        ∀ i : E.I₀,
          IsAffine (E.X i).obj ∧
            IsWContractible.{u, u} Γ((E.X i).obj, ⊤) ∧
            B.topology.IsWeaklyContractible (E.X i)
```

## Tag 0990, a lemma

[Tag 0990](https://stacks.math.columbia.edu/tag/0990) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.hasEnoughObjects_isAffine_isWeaklyContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenClosedSequence.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenClosedSequence.lean#L574). The attribute's comment: “the small pro-etale site of a scheme, in the unrestricted form of AlgebraicGeometry.Scheme.ProEt: every object is covered by affine weakly contractible ones”.

> **Stacks 0990 for the small pro-étale site of a scheme.** Every object of `X_proétale` is
> covered by affine objects which are weakly contractible objects of the site.

```lean
theorem hasEnoughObjects_isAffine_isWeaklyContractible (X : Scheme.{u}) :
    (Scheme.ProEt.topology X).HasEnoughObjects
      (fun V : X.ProEt ↦ IsAffine V.left ∧
        (Scheme.ProEt.topology X).IsWeaklyContractible V)
```

**`AlgebraicGeometry.ProEtale.hasEnoughWeaklyContractibleObjects_proetale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenClosedSequence.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/OpenClosedSequence.lean#L606). The attribute's comment: “the small pro-etale site of a scheme has enough weakly contractible objects, the form HasEnoughWeaklyContractibleObjects asks for”.

> **Stacks 0990, in the form the derived-completeness results consume.** The small pro-étale
> site of a scheme has enough weakly contractible objects.
>
> This is the theorem above with the affineness of the covering objects forgotten, which is the
> shape `CategoryTheory.GrothendieckTopology.HasEnoughWeaklyContractibleObjects` asks for — it
> unfolds to `HasEnoughObjects J (IsWeaklyContractible J)`. It is what supplies the `hX` hypothesis
> of the derived-completeness results for this site, among them Stacks 09BY in
> `StacksFrontier.AlgebraicGeometry.ProEtale.AdicCompletionCriterion`.

```lean
theorem hasEnoughWeaklyContractibleObjects_proetale (X : Scheme.{u}) :
    (Scheme.ProEt.topology X).HasEnoughWeaklyContractibleObjects
```

**`AlgebraicGeometry.ProEtale.affineIndEtaleProetale_hasEnough_quasiCompact_weaklyContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AffineIndEtaleWeaklyContractible.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AffineIndEtaleWeaklyContractible.lean#L410). The attribute's comment: “affine ind-étale pro-étale site”.

> **Stacks 0990, the affine ind-étale pro-étale site.** For an affine base, the affine
> ind-étale pro-étale site has enough quasi-compact weakly contractible objects: every object is
> covered by a single object which is quasi-compact and weakly contractible.

```lean
theorem affineIndEtaleProetale_hasEnough_quasiCompact_weaklyContractible [IsAffine S.obj] :
    (AffineIndEtaleProetale.topology B S).HasEnoughObjects
      (fun U : AffineIndEtaleProetale B S ↦
        (AffineIndEtaleProetale.topology B S).IsQuasiCompactObject U ∧
        (AffineIndEtaleProetale.topology B S).IsWeaklyContractible U)
```

**`AlgebraicGeometry.ProEtale.BigProetaleOver.hasEnough_affine_quasiCompact_weaklyContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/EnoughWeaklyContractible.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/EnoughWeaklyContractible.lean#L134). The attribute's comment: “the big pro-étale site (Sch/S)_proétale”.

> **Stacks 0990 for the big pro-étale site `(Sch/S)_proétale`.** Every object of the big
> pro-étale site of `S` is covered by objects which are affine, quasi-compact objects of the site
> and weakly contractible in it.
>
> The covering is Stacks 098I, lifted to the slice by composing with the structure morphism; the
> two properties of its members are
> `AlgebraicGeometry.ProEtale.BigProetaleOver.isQuasiCompactObject_of_isWContractible` and
> `AlgebraicGeometry.ProEtale.BigProetaleOver.isWeaklyContractible_of_isWContractible`.

```lean
theorem BigProetaleOver.hasEnough_affine_quasiCompact_weaklyContractible :
    (BigProetaleOver.topology B S hS).HasEnoughObjects
      (fun T : BigProetaleOver B S hS ↦
        IsAffine ((BigProetaleOver.toScheme B S hS).obj T) ∧
          (BigProetaleOver.topology B S hS).IsQuasiCompactObject T ∧
          (BigProetaleOver.topology B S hS).IsWeaklyContractible T)
```

**`AlgebraicGeometry.ProEtale.SmallProetale.hasEnough_affine_quasiCompact_weaklyContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/EnoughWeaklyContractible.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/EnoughWeaklyContractible.lean#L159). The attribute's comment: “the small pro-étale site S_proétale”.

> **Stacks 0990 for the small pro-étale site `S_proétale`.** Every object of the small
> pro-étale site of `S` is covered by objects which are affine, quasi-compact objects of the site
> and weakly contractible in it.
>
> The covering is Stacks 098I in the small site,
> `AlgebraicGeometry.ProEtale.SmallProetale.hasEnoughObjects_isWContractible`; the two properties
> of its members are
> `AlgebraicGeometry.ProEtale.SmallProetale.isQuasiCompactObject_of_isWContractible` and
> `AlgebraicGeometry.ProEtale.SmallProetale.isWeaklyContractible_of_isWContractible`.

```lean
theorem SmallProetale.hasEnough_affine_quasiCompact_weaklyContractible :
    (SmallProetale.topology B S hS).HasEnoughObjects
      (fun U : SmallProetale B S hS ↦
        IsAffine ((SmallProetale.toScheme B S hS).obj U) ∧
          (SmallProetale.topology B S hS).IsQuasiCompactObject U ∧
          (SmallProetale.topology B S hS).IsWeaklyContractible U)
```

**`AlgebraicGeometry.ProEtale.BigAffineProetale.hasEnough_affine_quasiCompact_weaklyContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/EnoughWeaklyContractible.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/EnoughWeaklyContractible.lean#L336). The attribute's comment: “the big affine pro-étale site (Aff/S)_proétale”.

> **Stacks 0990 for the big affine pro-étale site `(Aff/S)_proétale`.** Every object of the
> big affine pro-étale site of `S` is covered by objects which are affine, quasi-compact objects
> of the site and weakly contractible in it.

```lean
theorem BigAffineProetale.hasEnough_affine_quasiCompact_weaklyContractible :
    (BigAffineProetale.topology B S hS).HasEnoughObjects
      (fun U : BigAffineProetale B S hS ↦
        IsAffine ((BigAffineProetale.toScheme B S hS).obj U) ∧
          (BigAffineProetale.topology B S hS).IsQuasiCompactObject U ∧
          (BigAffineProetale.topology B S hS).IsWeaklyContractible U)
```

**`AlgebraicGeometry.ProEtale.SmallAffineProetale.hasEnough_affine_quasiCompact_weaklyContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/EnoughWeaklyContractible.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/EnoughWeaklyContractible.lean#L439). The attribute's comment: “the affine small pro-étale site S_{affine, pro-étale}”.

> **Stacks 0990 for the affine small pro-étale site `S_{affine, proétale}`.** Every object of
> the affine small pro-étale site of `S` is covered by objects which are affine, quasi-compact
> objects of the site and weakly contractible in it.

```lean
theorem SmallAffineProetale.hasEnough_affine_quasiCompact_weaklyContractible :
    (SmallAffineProetale.topology B S hS).HasEnoughObjects
      (fun U : SmallAffineProetale B S hS ↦
        IsAffine ((SmallAffineProetale.toScheme B S hS).obj U) ∧
          (SmallAffineProetale.topology B S hS).IsQuasiCompactObject U ∧
          (SmallAffineProetale.topology B S hS).IsWeaklyContractible U)
```

## Tag 0F4P, a lemma

[Tag 0F4P](https://stacks.math.columbia.edu/tag/0F4P) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_weaklyContractible_singleton_covering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleOneElementCovers.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleOneElementCovers.lean#L311).

> Every object `U` of a chosen big pro-étale site admits a one-element chosen covering
> `{V → U}` whose source is a weakly contractible object of the site.

```lean
theorem exists_weaklyContractible_singleton_covering (U : B.Scheme) :
    ∃ (V : B.Scheme) (p : V ⟶ U),
      B.covering ⟨U, PreZeroHypercover.singleton p⟩ ∧
        B.topology.IsWeaklyContractible V
```

**`AlgebraicGeometry.ProEtale.exists_affine_weaklyContractible_singleton_covering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleOneElementCovers.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleOneElementCovers.lean#L378). The attribute's comment: “the quasi-compact case”.

> If the underlying scheme of an object `U` of a chosen big pro-étale site is quasi-compact,
> the one-element covering of
> `AlgebraicGeometry.ProEtale.exists_weaklyContractible_singleton_covering` can be chosen with
> affine source.

```lean
theorem exists_affine_weaklyContractible_singleton_covering (U : B.Scheme)
    [CompactSpace U.obj] :
    ∃ (V : B.Scheme) (p : V ⟶ U),
      B.covering ⟨U, PreZeroHypercover.singleton p⟩ ∧
        IsAffine V.obj ∧ B.topology.IsWeaklyContractible V
```

**`AlgebraicGeometry.ProEtale.exists_weaklyContractible_singleton_covering_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleOneElementCoversSmall.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleOneElementCoversSmall.lean#L117). The attribute's comment: “the big site over a scheme”.

> **Stacks 0F4P for the big pro-étale site over a scheme.** Every object `U` of the big
> pro-étale site over `S` in a chosen big pro-étale site admits a one-element covering `{V → U}`
> whose source is a weakly contractible object of that site.
>
> The covering is the one of
> `AlgebraicGeometry.ProEtale.exists_weaklyContractible_singleton_covering` for the underlying
> object of the chosen big site, viewed over `S` through the composite to `U`; its source stays
> weakly contractible in the slice by
> `Stacks.WeaklyContractible.weaklyContractible_over`.

```lean
theorem exists_weaklyContractible_singleton_covering_over (U : BigProetaleOver B S hS) :
    ∃ (V : BigProetaleOver B S hS) (p : V ⟶ U),
      BigProetaleOver.IsCovering B S hS ⟨U, PreZeroHypercover.singleton p⟩ ∧
        (BigProetaleOver.topology B S hS).IsWeaklyContractible V
```

**`AlgebraicGeometry.ProEtale.exists_affine_weaklyContractible_singleton_covering_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleOneElementCoversSmall.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleOneElementCoversSmall.lean#L132). The attribute's comment: “the big site over a scheme, quasi-compact case”.

> **Stacks 0F4P for the big pro-étale site over a scheme, the quasi-compact case.** If the
> underlying scheme of an object `U` of the big pro-étale site over `S` is quasi-compact, the
> one-element covering of
> `AlgebraicGeometry.ProEtale.exists_weaklyContractible_singleton_covering_over` can be chosen
> with affine source.

```lean
theorem exists_affine_weaklyContractible_singleton_covering_over
    (U : BigProetaleOver B S hS) [CompactSpace ((BigProetaleOver.toScheme B S hS).obj U)] :
    ∃ (V : BigProetaleOver B S hS) (p : V ⟶ U),
      BigProetaleOver.IsCovering B S hS ⟨U, PreZeroHypercover.singleton p⟩ ∧
        IsAffine ((BigProetaleOver.toScheme B S hS).obj V) ∧
        (BigProetaleOver.topology B S hS).IsWeaklyContractible V
```

**`AlgebraicGeometry.ProEtale.exists_weaklyContractible_singleton_covering_small`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleOneElementCoversSmall.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleOneElementCoversSmall.lean#L314). The attribute's comment: “the small site”.

> **Stacks 0F4P for the small pro-étale site.** Every object `U` of the small pro-étale site
> of `S` in a chosen big pro-étale site admits a one-element covering `{V → U}` whose source is a
> weakly contractible object of that site.
>
> The covering is the one of
> `AlgebraicGeometry.ProEtale.exists_weaklyContractible_coproduct_singleton_covering` for the
> underlying object of the chosen big site: its covering morphism is weakly étale, so its source
> is again weakly étale over `S`, and the source is a disjoint union of affine objects with
> w-contractible rings of global sections, hence weakly contractible in the small site by
> `AlgebraicGeometry.ProEtale.isWeaklyContractible_small_of_coproduct`.

```lean
theorem exists_weaklyContractible_singleton_covering_small (U : SmallProetale B S hS) :
    ∃ (V : SmallProetale B S hS) (p : V ⟶ U),
      SmallProetale.IsCovering B S hS ⟨U, PreZeroHypercover.singleton p⟩ ∧
        (SmallProetale.topology B S hS).IsWeaklyContractible V
```

**`AlgebraicGeometry.ProEtale.exists_affine_weaklyContractible_singleton_covering_small`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleOneElementCoversSmall.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/WeaklyContractibleOneElementCoversSmall.lean#L335). The attribute's comment: “the small site, quasi-compact case”.

> **Stacks 0F4P for the small pro-étale site, the quasi-compact case.** If the underlying
> scheme of an object `U` of the small pro-étale site of `S` is quasi-compact, the one-element
> covering of
> `AlgebraicGeometry.ProEtale.exists_weaklyContractible_singleton_covering_small` can be chosen
> with affine source.
>
> An affine weakly contractible object of the chosen big site has w-contractible ring of global
> sections by Stacks 098H, which is weak contractibility in the small site by Stacks 0990.

```lean
theorem exists_affine_weaklyContractible_singleton_covering_small
    (U : SmallProetale B S hS) [CompactSpace ((SmallProetale.toScheme B S hS).obj U)] :
    ∃ (V : SmallProetale B S hS) (p : V ⟶ U),
      SmallProetale.IsCovering B S hS ⟨U, PreZeroHypercover.singleton p⟩ ∧
        IsAffine ((SmallProetale.toScheme B S hS).obj V) ∧
        (SmallProetale.topology B S hS).IsWeaklyContractible V
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.13, Tag 0F4N](https://stacks.math.columbia.edu/tag/0F4N)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
