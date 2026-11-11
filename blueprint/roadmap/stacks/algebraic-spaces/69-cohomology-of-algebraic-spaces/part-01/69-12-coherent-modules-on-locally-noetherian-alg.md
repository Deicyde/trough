---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsCoherent, AlgebraicGeometry.Space.isCoherent_iff_forall_over, AlgebraicGeometry.Space.isCoherent_iff_exists_surjective_over, AlgebraicGeometry.Space.forall_over_iff_exists_surjective_over, AlgebraicGeometry.Space.isCoherent_iff_isFinitePresentationOnSite, AlgebraicGeometry.Space.isCoherent_structureSheaf, AlgebraicGeometry.Space.isCoherent_iff_isQuasicoherentOnSite_and_isFiniteType, AlgebraicGeometry.Space.isCoherent_of_fact_isFiniteLocallyFreeOnSite
statement: formalized
proof: formalized
---

# 69.12 Coherent modules on locally Noetherian algebraic spaces

Section 69.12 of the Stacks Project, [Tag 07U9](https://stacks.math.columbia.edu/tag/07U9). 9 tags here are carried by 33 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07UA, a definition

[Tag 07UA](https://stacks.math.columbia.edu/tag/07UA) in the Stacks Project.

**`AlgebraicGeometry.Space.IsCoherent`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentModules.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentModules.lean#L389).

> A coherent module on an algebraic space is a quasi-coherent module which is coherent on its
> small étale ringed site.
>
> The predicate is on all modules rather than only on the quasi-coherent ones, so that it
> applies directly to kernels, cokernels and extensions formed in the ambient category of
> modules.  It does not need the locally Noetherian assumption; that assumption enters the
> characterizations of Stacks 07UB and the closure results of Stacks 07UC.

```lean
class IsCoherent (M : Modules.{u, m} B S hS F hF) : Prop
    extends SheafOfModules.IsQuasicoherentOnSite M, SheafOfModules.IsCoherentOnSite M
```

## Tag 07UB, a lemma

[Tag 07UB](https://stacks.math.columbia.edu/tag/07UB) in the Stacks Project.

**`AlgebraicGeometry.Space.isCoherent_iff_forall_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentEtaleChartTfae.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentEtaleChartTfae.lean#L149). The attribute's comment: “conditions (1) and (4)”.

> **Stacks 07UB, conditions (1) and (4).**  A module on an algebraic space is coherent if and
> only if its restriction to the slice at every étale chart is coherent there.
>
> The restriction is restriction to the slice of the small étale site at the chart; see the
> implementation notes.  The module universe is the universe of the structure rings, which
> `AlgebraicGeometry.Space.isCoherent_iff_isCoherentOnSite` pins.

```lean
theorem isCoherent_iff_forall_over (M : Modules.{u, u} B S hS F hF) :
    IsCoherent B S hS F hF M ↔
      ∀ U : (smallEtaleRingedSite B S hS F hF).C,
        SheafOfModules.IsCoherentOnSite
          (R := (Stacks.SheafOfModules.Tensor.ringSheaf
            ((smallEtaleRingedSite B S hS F hF).over U).O)) (M.over U)
```

**`AlgebraicGeometry.Space.isCoherent_iff_exists_surjective_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentEtaleChartTfae.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentEtaleChartTfae.lean#L168). The attribute's comment: “conditions (1) and (5)”.

> **Stacks 07UB, conditions (1) and (5).**  A module on an algebraic space is coherent if and
> only if there is an étale chart whose structure morphism is surjective on points and whose
> slice restriction is coherent.
>
> The forward implication uses that an algebraic space has such a chart at all, namely its
> atlas: `AlgebraicGeometry.Space.exists_surjective_smallEtale_chart`.  The restriction is
> restriction to the slice of the small étale site at the chart; see the implementation notes.
> The module universe is the universe of the structure rings, which
> `AlgebraicGeometry.Space.isCoherent_iff_isCoherentOnSite` pins.

```lean
theorem isCoherent_iff_exists_surjective_over (M : Modules.{u, u} B S hS F hF) :
    IsCoherent B S hS F hF M ↔
      ∃ U : (smallEtaleRingedSite B S hS F hF).C, IsSurjective B S hS U.1.hom ∧
        SheafOfModules.IsCoherentOnSite
          (R := (Stacks.SheafOfModules.Tensor.ringSheaf
            ((smallEtaleRingedSite B S hS F hF).over U).O)) (M.over U)
```

**`AlgebraicGeometry.Space.forall_over_iff_exists_surjective_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentEtaleChartTfae.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentEtaleChartTfae.lean#L190). The attribute's comment: “conditions (4) and (5)”.

> **Stacks 07UB, conditions (4) and (5).**  The slice restriction of a module on an algebraic
> space is coherent at *every* étale chart if and only if it is coherent at *one* étale chart
> whose structure morphism is surjective on points.
>
> This is the adjacent equivalence at the bottom of the chain of Stacks 07UB, stated without
> reference to its condition (1).  Unlike the two equivalences with condition (1) it is at a free
> module universe: both implications pass through coherence of the module on the whole small
> étale ringed site, and only the identification of that with condition (1) needs the universe
> fixed.  The restriction is restriction to the slice of the small étale site at the chart; see
> the implementation notes.

```lean
theorem forall_over_iff_exists_surjective_over (M : Modules.{u, m} B S hS F hF) :
    (∀ U : (smallEtaleRingedSite B S hS F hF).C,
        SheafOfModules.IsCoherentOnSite
          (R := (Stacks.SheafOfModules.Tensor.ringSheaf
            ((smallEtaleRingedSite B S hS F hF).over U).O)) (M.over U)) ↔
      ∃ U : (smallEtaleRingedSite B S hS F hF).C, IsSurjective B S hS U.1.hom ∧
        SheafOfModules.IsCoherentOnSite
          (R := (Stacks.SheafOfModules.Tensor.ringSheaf
            ((smallEtaleRingedSite B S hS F hF).over U).O)) (M.over U)
```

**`AlgebraicGeometry.Space.isCoherent_iff_isFinitePresentationOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentFinitePresentation.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentFinitePresentation.lean#L44). The attribute's comment: “conditions (1) and (3)”.

> A module on a locally Noetherian algebraic space is coherent if and only if it is an
> `𝒪_F`-module of finite presentation.

```lean
theorem isCoherent_iff_isFinitePresentationOnSite
    [Fact (HasEtaleLocalProperty B S hS F (fun V : Scheme.{u} => IsLocallyNoetherian V))]
    (M : Modules.{u, u} B S hS F hF) :
    IsCoherent B S hS F hF M ↔ M.IsFinitePresentationOnSite
```

**`AlgebraicGeometry.Space.isCoherent_structureSheaf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentStructureSheaf.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentStructureSheaf.lean#L391). The attribute's comment: “structure sheaf”.

> **Stacks 07UB, the structure sheaf.**  The structure sheaf of a locally Noetherian
> algebraic space is a coherent `𝒪_F`-module.
>
> Quasi-coherence is `SheafOfModules.isQuasicoherentOnSite_unit` and finite type is
> `PresheafOfModules.isFiniteType_unit`, neither of which needs the hypothesis; the relations
> clause is `AlgebraicGeometry.RingedSite.isFiniteType_relations_unit`, applied to the covering
> by Noetherian affine charts of
> `AlgebraicGeometry.Space.exists_covering_through_noetherianAffine`.

```lean
instance isCoherent_structureSheaf
    [Fact (HasEtaleLocalProperty B S hS F (fun V : Scheme.{u} => IsLocallyNoetherian V))] :
    IsCoherent B S hS F hF
      (SheafOfModules.unit (ringSheaf (smallEtaleRingedSite B S hS F hF).O))
```

**`AlgebraicGeometry.Space.isCoherent_iff_isQuasicoherentOnSite_and_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteDirectImageCoherence.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteDirectImageCoherence.lean#L124). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 07UB, conditions (1) and (2).**  A module on a locally Noetherian algebraic space
> is coherent if and only if it is quasi-coherent and of finite type.
>
> The base change property of the sections over the affine charts, which the conditional form in
> `StacksFrontier.AlgebraicGeometry.Spaces.CoherentNoetherian` carries, is Descent, Proposition
> 03DX (2) and follows from quasi-coherence, which is a hypothesis in the direction that needs
> it.

```lean
theorem isCoherent_iff_isQuasicoherentOnSite_and_isFiniteType
    [Fact (HasEtaleLocalProperty B S hS F (fun V : Scheme.{u} => IsLocallyNoetherian V))]
    (M : Modules.{u, u} B S hS F hF) :
    IsCoherent B S hS F hF M ↔
      (M.IsQuasicoherentOnSite ∧
        PresheafOfModules.IsFiniteType (smallEtaleRingedSite B S hS F hF).J M.val)
```

**`AlgebraicGeometry.Space.isCoherent_of_fact_isFiniteLocallyFreeOnSite`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeCoherent.lean, line 567](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeCoherent.lean#L567). The attribute's comment: “finite locally free modules”.

> **Stacks 07UB, finite locally free modules.**  A finite locally free module on a locally
> Noetherian algebraic space is coherent, as an instance.
>
> This is `AlgebraicGeometry.Space.isCoherent_of_isFiniteLocallyFreeOnSite` with finite local
> freeness supplied by instance search through `Fact`, which is how the predicate — an `abbrev`
> and not a class — can be an instance hypothesis.  The same wrapping is used by the locally
> Noetherian hypothesis of `AlgebraicGeometry.Space.isCoherent_structureSheaf`.

```lean
instance isCoherent_of_fact_isFiniteLocallyFreeOnSite
    [Fact (HasEtaleLocalProperty B S hS F (fun V : Scheme.{u} => IsLocallyNoetherian V))]
    (M : Modules.{u, m} B S hS F hF)
    [Fact (SheafOfModules.IsFiniteLocallyFreeOnSite M)] :
    IsCoherent B S hS F hF M
```

**`AlgebraicGeometry.Space.isCoherent_of_isInvertible_instance`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvertibleCoherent.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/InvertibleCoherent.lean#L636). The attribute's comment: “invertible modules”.

> **Stacks 07UB, invertible modules.**  An invertible module on a locally Noetherian algebraic
> space is coherent, as an instance.
>
> This is `AlgebraicGeometry.Space.isCoherent_of_isInvertible` with invertibility taken as an
> instance-implicit binder, discharged from the local context.
> `Stacks.SheafOfModules.IsInvertible` is a class, which is what lets the hypothesis be written
> that way; it does not mean instance search *finds* invertibility, and on this site it finds it
> for nothing at all, the structure sheaf included —
> `Stacks.SheafOfModules.isInvertible_unit` does not apply here, its
> `CategoryTheory.GrothendieckTopology.WEqualsLocallyBijective` hypothesis not being synthesized
> for the topology as the small étale ringed site spells it.  That is also what makes the instance
> free: the branch it adds to the search for `AlgebraicGeometry.Space.IsCoherent` closes on the
> invertibility subgoal unless the caller has already put invertibility in its context, which is
> the only situation the instance is for.

```lean
instance isCoherent_of_isInvertible_instance
    [Fact (HasEtaleLocalProperty B S hS F (fun V : Scheme.{u} => IsLocallyNoetherian V))]
    (M : Modules.{u, u} B S hS F hF)
    [Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS F)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O)).property M] :
    IsCoherent B S hS F hF M
```

## Tag 07UC, a lemma

[Tag 07UC](https://stacks.math.columbia.edu/tag/07UC) in the Stacks Project.

**`AlgebraicGeometry.Space.isCoherent_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAbelian.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAbelian.lean#L94). The attribute's comment: “kernel”.

> **[Stacks, Tag 07UC].** The kernel of a map of coherent modules on an algebraic space is
> coherent.
>
> The kernel of a map of coherent sheaves of modules on an arbitrary site is coherent, by
> Stacks 01BY (3); quasi-coherence of the kernel is then free at this module universe.

```lean
theorem isCoherent_kernel {M N : Modules.{u, u} B S hS F hF} (hM : IsCoherent B S hS F hF M)
    (hN : IsCoherent B S hS F hF N) (φ : M ⟶ N) : IsCoherent B S hS F hF (kernel φ)
```

**`AlgebraicGeometry.Space.isCoherent_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAbelian.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAbelian.lean#L106). The attribute's comment: “cokernel”.

> **[Stacks, Tag 07UC].** The cokernel of a map of coherent modules on an algebraic space is
> coherent.
>
> The cokernel of a map of coherent sheaves of modules on an arbitrary site is coherent, by
> Stacks 01BY (3); quasi-coherence of the cokernel is then free at this module universe.

```lean
theorem isCoherent_cokernel {M N : Modules.{u, u} B S hS F hF} (hM : IsCoherent B S hS F hF M)
    (hN : IsCoherent B S hS F hF N) (φ : M ⟶ N) : IsCoherent B S hS F hF (cokernel φ)
```

**`AlgebraicGeometry.Space.isCoherent_X₂_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAbelian.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAbelian.lean#L122). The attribute's comment: “extensions”.

> **[Stacks, Tag 07UC].** An extension of coherent modules on an algebraic space is coherent:
> the middle term of a short exact sequence of `𝒪_F`-modules whose outer terms are coherent is
> coherent.
>
> An extension is represented by a short exact complex of `𝒪_F`-modules, so the statement
> quantifies over all extensions of the third term by the first rather than over a choice of one.
> The content is Stacks 01BY (4) on the small étale ringed site of `F`; quasi-coherence of the
> middle term is free at this module universe.

```lean
theorem isCoherent_X₂_of_shortExact {T : ShortComplex (Modules.{u, u} B S hS F hF)}
    (hT : T.ShortExact) (h₁ : IsCoherent B S hS F hF T.X₁)
    (h₃ : IsCoherent B S hS F hF T.X₃) : IsCoherent B S hS F hF T.X₂
```

**`AlgebraicGeometry.Space.nonempty_abelian_coherentModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAbelian.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAbelian.lean#L166). The attribute's comment: “abelian category”.

> **[Stacks, Tag 07UC].** The category `Coh(𝒪_F)` of coherent modules on an algebraic space is
> abelian.
>
> The abelian structure is the one a full subcategory of an abelian category closed under kernels,
> cokernels and finite coproducts carries, assembled by
> `AlgebraicGeometry.Space.coherentModules_abelian_of_closure`; the kernel and cokernel closure
> properties are Stacks 01BY (3) on the small étale ringed site and the coproduct one comes from
> the extension result above.

```lean
theorem nonempty_abelian_coherentModules :
    Nonempty (Abelian (CoherentModules.{u, u} B S hS F hF))
```

## Tag 07UD, a lemma

[Tag 07UD](https://stacks.math.columbia.edu/tag/07UD) in the Stacks Project.

**`AlgebraicGeometry.Space.isCoherentOnSite_of_mono_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentSubquotientNoetherian.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentSubquotientNoetherian.lean#L359). The attribute's comment: “a quasi-coherent submodule of a coherent module is coherent”.

> **The submodule clause of Stacks 07UD on the small étale ringed site.**  A quasi-coherent
> submodule of a module coherent on the small étale ringed site of a locally Noetherian algebraic
> space is itself coherent on that site.
>
> The submodule is of finite type by
> `AlgebraicGeometry.Space.isFiniteType_of_mono_of_isQuasicoherentOnSite`, and a submodule of finite
> type of a coherent module is coherent by
> `AlgebraicGeometry.Space.isCoherentOnSite_of_mono_of_isFiniteType`.

```lean
theorem isCoherentOnSite_of_mono_of_isQuasicoherentOnSite
    [Fact (HasEtaleLocalProperty B S hS F (fun V : Scheme.{u} => IsLocallyNoetherian V))]
    {M N : Modules.{u, u} B S hS F hF} (ι : N ⟶ M) [Mono ι]
    (hN : N.IsQuasicoherentOnSite) (hM : SheafOfModules.IsCoherentOnSite M) :
    SheafOfModules.IsCoherentOnSite N
```

**`AlgebraicGeometry.Space.isCoherent_of_mono_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentSubquotientNoetherian.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentSubquotientNoetherian.lean#L371). The attribute's comment: “a quasi-coherent submodule of a coherent module is coherent”.

> **The submodule clause of Stacks 07UD.**  A quasi-coherent submodule of a coherent module on a
> locally Noetherian algebraic space is coherent, for the predicate
> `AlgebraicGeometry.Space.IsCoherent` of Stacks 07UA.

```lean
theorem isCoherent_of_mono_of_isQuasicoherentOnSite
    [Fact (HasEtaleLocalProperty B S hS F (fun V : Scheme.{u} => IsLocallyNoetherian V))]
    {M N : Modules.{u, u} B S hS F hF} (ι : N ⟶ M) [Mono ι]
    (hN : N.IsQuasicoherentOnSite) (hM : IsCoherent B S hS F hF M) :
    IsCoherent B S hS F hF N
```

**`AlgebraicGeometry.Space.isCoherentOnSite_of_epi_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentSubquotientNoetherian.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentSubquotientNoetherian.lean#L391). The attribute's comment: “a quasi-coherent quotient module of a coherent module is coherent”.

> **The quotient clause of Stacks 07UD on the small étale ringed site.**  A quasi-coherent
> quotient module of a module coherent on the small étale ringed site of a locally Noetherian
> algebraic space is itself coherent on that site.  The quotient is given by an epimorphism
> `p : M ⟶ Q` of `𝒪_F`-modules.
>
> The kernel of `p` is a quasi-coherent submodule of `M`, being cartesian on affine charts by
> `AlgebraicGeometry.Space.isCartesianOnAffineCharts_kernel`, so it is of finite type by
> `AlgebraicGeometry.Space.isFiniteType_of_mono_of_isQuasicoherentOnSite`, and a quotient of a
> coherent module by a submodule of finite type is coherent by
> `AlgebraicGeometry.Space.isCoherentOnSite_of_epi_of_isFiniteType_kernel`.

```lean
theorem isCoherentOnSite_of_epi_of_isQuasicoherentOnSite
    [Fact (HasEtaleLocalProperty B S hS F (fun V : Scheme.{u} => IsLocallyNoetherian V))]
    {M Q : Modules.{u, u} B S hS F hF} (p : M ⟶ Q) [Epi p]
    (hQ : Q.IsQuasicoherentOnSite) (hM : SheafOfModules.IsCoherentOnSite M) :
    SheafOfModules.IsCoherentOnSite Q
```

**`AlgebraicGeometry.Space.isCoherent_of_epi_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentSubquotientNoetherian.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentSubquotientNoetherian.lean#L408). The attribute's comment: “a quasi-coherent quotient module of a coherent module is coherent”.

> **The quotient clause of Stacks 07UD.**  A quasi-coherent quotient module of a coherent module
> on a locally Noetherian algebraic space is coherent, for the predicate
> `AlgebraicGeometry.Space.IsCoherent` of Stacks 07UA.

```lean
theorem isCoherent_of_epi_of_isQuasicoherentOnSite
    [Fact (HasEtaleLocalProperty B S hS F (fun V : Scheme.{u} => IsLocallyNoetherian V))]
    {M Q : Modules.{u, u} B S hS F hF} (p : M ⟶ Q) [Epi p]
    (hQ : Q.IsQuasicoherentOnSite) (hM : IsCoherent B S hS F hF M) :
    IsCoherent B S hS F hF Q
```

## Tag 07UE, a lemma

[Tag 07UE](https://stacks.math.columbia.edu/tag/07UE) in the Stacks Project.

**`AlgebraicGeometry.Space.isCoherent_smallEtaleInternalHomSmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentInternalHom.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentInternalHom.lean#L164). The attribute's comment: “internal Hom”.

> **Stacks 07UE, the sheaf-hom clause.**  The internal Hom `𝓗om_{𝒪_F}(M, N)` of two coherent
> `𝒪_F`-modules on an algebraic space is coherent.

```lean
theorem isCoherent_smallEtaleInternalHomSmall (M N : Modules.{u, u} B S hS F hF)
    [IsCoherent B S hS F hF M] [IsCoherent B S hS F hF N] :
    IsCoherent B S hS F hF (smallEtaleInternalHomSmall B S hS F hF M N)
```

**`AlgebraicGeometry.Space.isCoherent_tensorModule_and_smallEtaleInternalHomSmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentInternalHom.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentInternalHom.lean#L174).

> **Stacks 07UE.**  Let `F` be an algebraic space over a scheme `S` and let `M`, `N` be
> coherent `𝒪_F`-modules.  Then `M ⊗_{𝒪_F} N` and `𝓗om_{𝒪_F}(M, N)` are coherent.

```lean
theorem isCoherent_tensorModule_and_smallEtaleInternalHomSmall
    (M N : Modules.{u, u} B S hS F hF)
    [IsCoherent B S hS F hF M] [IsCoherent B S hS F hF N] :
    IsCoherent B S hS F hF (tensorModule B S hS F hF M N) ∧
      IsCoherent B S hS F hF (smallEtaleInternalHomSmall B S hS F hF M N)
```

**`AlgebraicGeometry.Space.isCoherent_tensorModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentTensorProduct.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentTensorProduct.lean#L78). The attribute's comment: “tensor product”.

> The tensor product `AlgebraicGeometry.Space.tensorModule` of two coherent `𝒪_F`-modules on an
> algebraic space is coherent.

```lean
theorem isCoherent_tensorModule (M N : Modules.{u, u} B S hS F hF)
    [IsCoherent B S hS F hF M] [IsCoherent B S hS F hF N] :
    IsCoherent B S hS F hF (tensorModule B S hS F hF M N)
```

## Tag 07UF, a lemma

[Tag 07UF](https://stacks.math.columbia.edu/tag/07UF) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpen_isZero_restrictToOpenPoints_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentStalkLocalProperties.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentStalkLocalProperties.lean#L458). The attribute's comment: “part (1)”.

> **Stacks 07UF, part (1).**  A coherent `𝒪_X`-module whose stalk at a geometric point `x̄`
> vanishes vanishes on an open subspace of `X` containing the image of `x̄`.
>
> The locally Noetherian hypothesis of the cited statement is not used: the support of a module of
> finite type is closed by Stacks 07TZ on any algebraic space, so the statement here is a strict
> generalisation.

```lean
theorem exists_isOpen_isZero_restrictToOpenPoints_of_isCoherent (X : AlgebraicSpaces B S hS)
    (M : Modules.{u, u} B S hS X.1 X.2) [IsCoherent B S hS X.1 X.2 M]
    (x : points B S hS X.1) (p : GeometricPoint B S hS X.1) (hp : p.LiesOver x)
    (hstalk : Subsingleton (stalkSet p (M.val.presheaf ⋙ forget AddCommGrpCat.{u}))) :
    ∃ (W : Set (points B S hS X.1)) (hW : IsOpen W), x ∈ W ∧
      IsZero ((restrictToOpenPoints.{u, u} B S hS X W hW).obj M)
```

**`AlgebraicGeometry.Space.exists_isOpen_mono_restrictToOpenPoints_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentStalkLocalProperties.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentStalkLocalProperties.lean#L475). The attribute's comment: “part (2)”.

> **Stacks 07UF, part (2).**  A morphism of coherent `𝒪_X`-modules injective on the stalk at a
> geometric point `x̄` is a monomorphism after restriction to an open subspace of `X` containing
> the image of `x̄`.
>
> The kernel is coherent on the small étale site, hence of finite type, and its stalk at `x̄`
> vanishes; part (1) applies to it, and étale restriction is left exact.  The locally Noetherian
> hypothesis of the cited statement is not used.

```lean
theorem exists_isOpen_mono_restrictToOpenPoints_map (X : AlgebraicSpaces B S hS)
    {M N : Modules.{u, u} B S hS X.1 X.2} [IsCoherent B S hS X.1 X.2 M]
    [IsCoherent B S hS X.1 X.2 N] (φ : M ⟶ N)
    (x : points B S hS X.1) (p : GeometricPoint B S hS X.1) (hp : p.LiesOver x)
    (hinj : Function.Injective (moduleStalkSetMap B S hS X p φ)) :
    ∃ (W : Set (points B S hS X.1)) (hW : IsOpen W), x ∈ W ∧
      Mono ((restrictToOpenPoints.{u, u} B S hS X W hW).map φ)
```

**`AlgebraicGeometry.Space.exists_isOpen_epi_restrictToOpenPoints_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentStalkLocalProperties.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentStalkLocalProperties.lean#L496). The attribute's comment: “part (3)”.

> **Stacks 07UF, part (3).**  A morphism of coherent `𝒪_X`-modules surjective on the stalk at
> a geometric point `x̄` is an epimorphism after restriction to an open subspace of `X` containing
> the image of `x̄`.
>
> The cokernel is coherent on the small étale site, hence of finite type, and its stalk at `x̄`
> vanishes; part (1) applies to it, and étale restriction is right exact.  The locally Noetherian
> hypothesis of the cited statement is not used.

```lean
theorem exists_isOpen_epi_restrictToOpenPoints_map (X : AlgebraicSpaces B S hS)
    {M N : Modules.{u, u} B S hS X.1 X.2} [IsCoherent B S hS X.1 X.2 M]
    [IsCoherent B S hS X.1 X.2 N] (φ : M ⟶ N)
    (x : points B S hS X.1) (p : GeometricPoint B S hS X.1) (hp : p.LiesOver x)
    (hsurj : Function.Surjective (moduleStalkSetMap B S hS X p φ)) :
    ∃ (W : Set (points B S hS X.1)) (hW : IsOpen W), x ∈ W ∧
      Epi ((restrictToOpenPoints.{u, u} B S hS X W hW).map φ)
```

**`AlgebraicGeometry.Space.exists_isOpen_isIso_restrictToOpenPoints_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentStalkLocalProperties.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentStalkLocalProperties.lean#L518). The attribute's comment: “part (4)”.

> **Stacks 07UF, part (4).**  A morphism of coherent `𝒪_X`-modules bijective on the stalk at a
> geometric point `x̄` becomes an isomorphism after restriction to an open subspace of `X`
> containing the image of `x̄`.
>
> Kernel and cokernel are both of finite type with vanishing stalk at `x̄`, so both vanish on the
> complement of the union of their two closed supports; there the restriction is both a
> monomorphism and an epimorphism.  The locally Noetherian hypothesis of the cited statement is
> not used.

```lean
theorem exists_isOpen_isIso_restrictToOpenPoints_map (X : AlgebraicSpaces B S hS)
    {M N : Modules.{u, u} B S hS X.1 X.2} [IsCoherent B S hS X.1 X.2 M]
    [IsCoherent B S hS X.1 X.2 N] (φ : M ⟶ N)
    (x : points B S hS X.1) (p : GeometricPoint B S hS X.1) (hp : p.LiesOver x)
    (hbij : Function.Bijective (moduleStalkSetMap B S hS X p φ)) :
    ∃ (W : Set (points B S hS X.1)) (hW : IsOpen W), x ∈ W ∧
      IsIso ((restrictToOpenPoints.{u, u} B S hS X W hW).map φ)
```

## Tag 07UG, a lemma

[Tag 07UG](https://stacks.math.columbia.edu/tag/07UG) in the Stacks Project.

**`AlgebraicGeometry.Space.isCoherent_module_on_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentSchemeTheoreticSupport.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentSchemeTheoreticSupport.lean#L142).

> **Stacks 07UG.**  Let `X` be a locally Noetherian algebraic space over `S`, let `F` be a
> coherent `𝒪_X`-module, let `i : Z → X` be the scheme-theoretic support of `F` and let `G` be
> the quasi-coherent `𝒪_Z`-module with `i_*G ≅ F`.  Then `G` is a coherent `𝒪_Z`-module.
>
> Here the witness `hZ` that the support is a closed subspace is an argument; it is a
> proposition that always holds, by
> `AlgebraicGeometry.Space.isClosedSubspace_schemeTheoreticSupport_of_isCoherent`, and the form
> with no such argument is
> `AlgebraicGeometry.Space.isCoherent_module_on_coherentSchemeTheoreticSupport`.

```lean
theorem isCoherent_module_on_schemeTheoreticSupport
    (hX : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (F : Modules.{u, u} B S hS X.1 X.2) [IsCoherent B S hS X.1 X.2 F]
    (hZ : IsClosedSubspace B S hS (schemeTheoreticSupport B S hS X F))
    (G : Modules.{u, u} B S hS
      (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).1
      (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).2)
    (hG : G.IsQuasicoherentOnSite)
    (e : (modulePushforward B S hS (closedSubspaceInclusion B S hS X
      ⟨schemeTheoreticSupport B S hS X F, hZ⟩)).obj G ≅ F) :
    IsCoherent B S hS
      (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).1
      (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).2 G
```

**`AlgebraicGeometry.Space.isCoherent_module_on_coherentSchemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentSchemeTheoreticSupport.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentSchemeTheoreticSupport.lean#L166).

> **Stacks 07UG.**  Let `X` be a locally Noetherian algebraic space over `S`, let `F` be a
> coherent `𝒪_X`-module, let `i : Z → X` be the scheme-theoretic support of `F` and let `G` be
> the quasi-coherent `𝒪_Z`-module with `i_*G ≅ F`.  Then `G` is a coherent `𝒪_Z`-module.
>
> The scheme-theoretic support is read as the closed subspace
> `AlgebraicGeometry.Space.coherentSchemeTheoreticSupport`, so no witness of closedness is
> assumed.

```lean
theorem isCoherent_module_on_coherentSchemeTheoreticSupport
    (hX : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (F : Modules.{u, u} B S hS X.1 X.2) [IsCoherent B S hS X.1 X.2 F]
    (G : Modules.{u, u} B S hS
      (closedSubspaceToSpace B S hS X (coherentSchemeTheoreticSupport B S hS X F)).1
      (closedSubspaceToSpace B S hS X (coherentSchemeTheoreticSupport B S hS X F)).2)
    (hG : G.IsQuasicoherentOnSite)
    (e : (modulePushforward B S hS (closedSubspaceInclusion B S hS X
      (coherentSchemeTheoreticSupport B S hS X F))).obj G ≅ F) :
    IsCoherent B S hS
      (closedSubspaceToSpace B S hS X (coherentSchemeTheoreticSupport B S hS X F)).1
      (closedSubspaceToSpace B S hS X (coherentSchemeTheoreticSupport B S hS X F)).2 G
```

## Tag 08AM, a lemma

[Tag 08AM](https://stacks.math.columbia.edu/tag/08AM) in the Stacks Project.

**`AlgebraicGeometry.Space.pushforwardCoherentEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionCoherentEquivalence.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionCoherentEquivalence.lean#L299).

> **Stacks 08AM.**  Let `S` be a scheme, let `i : Z ⟶ X` be a closed immersion of locally
> Noetherian algebraic spaces over `S` and let `ℐ ⊆ 𝒪_X` be the quasi-coherent sheaf of ideals
> cutting out `Z`.  The functor `i_*` induces an equivalence between the category of coherent
> `𝒪_Z`-modules and the category of coherent `𝒪_X`-modules annihilated by `ℐ`.
>
> The equivalence comes paired with the natural isomorphism identifying its functor, composed with
> the inclusion of the full subcategory, with `AlgebraicGeometry.Space.modulePushforward` — so what
> is asserted is that **`i_*` itself** is an equivalence onto the coherent annihilated modules, and
> not merely that the two categories are equivalent.  The pairing is the shape in which the
> scheme-level Stacks 087T is stated at
> `Stacks.AlgebraicGeometry.Tag087TCoherentImage.coherentPushforwardEquivalence`.
>
> The functor is `AlgebraicGeometry.Space.pushforwardCoherent`, its full faithfulness is
> `AlgebraicGeometry.Space.fullyFaithfulPushforwardCoherent` — part (2) of Stacks 04CJ, the
> `67.14.1` of the source's proof — and its essential surjectivity is
> `AlgebraicGeometry.Space.essSurj_pushforwardCoherent`, which rests on coherence of the inverse
> image together with the essential-image clause of Stacks 08KS for algebraic spaces.  That the
> functor lands in the *coherent* annihilated modules is
> `AlgebraicGeometry.Space.isCoherent_modulePushforward_of_isClosedImmersion`.

```lean
def pushforwardCoherentEquivalence
    (hX : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hZ : HasEtaleLocalProperty B S hS Z.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (i : Z ⟶ X) (hi : IsClosedImmersion B S hS i.hom) :
    Σ e : CoherentModules.{u, u} B S hS Z.1 Z.2 ≌
        (coherentAnnihilatedByKerIdeal B S hS i).FullSubcategory,
      e.functor ⋙ ObjectProperty.ι (coherentAnnihilatedByKerIdeal B S hS i) ≅
        ObjectProperty.ι _ ⋙ modulePushforward B S hS i
```

**`AlgebraicGeometry.Space.coherentModulePushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean#L340). The attribute's comment: “the induced functor into the modules annihilated by the ideal”.

> **Stacks 08AM**, the induced functor, with the target weakened: direct image as a functor
> `Coh(𝒪_X) ⥤ {𝓕 ∈ Mod(𝒪_Y) | 𝓘𝓕 = 0}` from the coherent modules of Stacks 07UA.
>
> The source states the target as the *coherent* `𝒪_Y`-modules annihilated by `𝓘`, which would need
> coherence of `f_*` of a coherent module; see the implementation notes.

```lean
def coherentModulePushforward (f : X ⟶ Y) :
    CoherentModules.{u, u} B S hS X.1 X.2 ⥤
      (annihilatedByKerIdeal B S hS f).FullSubcategory
```

**`AlgebraicGeometry.Space.fullyFaithfulCoherentModulePushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean#L361). The attribute's comment: “full faithfulness of the direct image on coherent modules”.

> **Stacks 08AM**, the full-faithfulness half of the equivalence: direct image along a closed
> immersion of algebraic spaces is fully faithful on coherent modules.
>
> Essential surjectivity is not proved; see the implementation notes for the one input it is
> missing and for the coherence of `f_*` that its target needs.

```lean
def fullyFaithfulCoherentModulePushforward (f : X ⟶ Y)
    (hf : IsClosedImmersion B S hS f.hom) :
    (coherentModulePushforward B S hS f).FullyFaithful
```

## Tag 07UH, a lemma

[Tag 07UH](https://stacks.math.columbia.edu/tag/07UH) in the Stacks Project.

**`AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteDirectImageCoherence.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteDirectImageCoherence.lean#L150). The attribute's comment: “vanishing of the higher direct images, granted the étale-affine case h03DW of Stacks 03DW”.

> **The vanishing assertion of Stacks 07UH, granted the chart case `h03DW`.**  Let
> `f : X ⟶ Y` be a finite morphism of algebraic spaces over `S` whose chart base changes have
> vanishing degree-`n` higher direct images.  Then `R^n f_*𝓕 = 0`.
>
> A finite morphism is affine, `AlgebraicGeometry.Space.IsFinite.isAffineHom`, so this is
> `AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isAffineHom`, the reduction of
> Stacks 073H through Equation 69.3.0.1 of Stacks 071Z.  The source's hypotheses that `Y` be
> locally Noetherian, that `𝓕` be coherent and that `n > 0` are not used; `h03DW` is the
> étale-site form of Stacks 01Y6, that is Stacks 03DW, which this development does not carry.

```lean
theorem isZero_rightDerived_modulePushforward_of_isFinite (f : X ⟶ Y)
    (hf : IsFinite B S hS f.hom) (G : Modules.{u, u} B S hS X.obj X.property) (n : ℕ)
    (h03DW : ChartwiseIsZeroHigherDirectImage B S hS f
      (relativelyRepresentable_of_isAffineHom B S hS f hf.isAffineHom)
      G n) :
    have := hasInjectiveResolutions_modules B S hS X.obj X.property
    IsZero (((modulePushforward B S hS f).rightDerived n).obj G)
```

**`AlgebraicGeometry.Space.isCoherent_modulePushforward_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteDirectImageCoherence.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteDirectImageCoherence.lean#L206). The attribute's comment: “coherence of the direct image, granted the chart case hchart of Stacks 03DW”.

> **The coherence assertion of Stacks 07UH, granted the chart case `hchart`.**  Let
> `f : X ⟶ Y` be a finite morphism of algebraic spaces over `S` with `Y` locally Noetherian, let
> `𝓕` be a coherent `𝒪_X`-module, and let `V` be an étale scheme chart of `Y` surjective on
> points.  Then `f_*𝓕` is coherent.
>
> Coherence is tested on `V` by Stacks 07UB (1) and (5) and over `V` the direct image is the
> localized direct image of Stacks 04CF, by
> `AlgebraicGeometry.Space.isCoherentOnSite_modulePushforward_of_over_of_isSurjective`.  The two
> geometric premises of `hchart` are discharged: the base change of `f` along `V` is finite by
> Stacks 03ZS, and `V` is locally Noetherian by Stacks 03E8.  So `hchart` is the étale-site form
> of Stacks 01Y6, that is Stacks 03DW, which this development does not carry.
>
> Unlike `AlgebraicGeometry.Space.isCoherent_modulePushforward_of_isFinite_of_chartCase` the chart
> is the caller's, not the atlas that `hY` supplies, which is what lets `hchart` be met at an
> *affine* chart; that is possible here because local Noetherianity of an arbitrary chart is
> available, by `AlgebraicGeometry.Space.isLocallyNoetherian_chart`.

```lean
theorem isCoherent_modulePushforward_of_isFinite (f : X ⟶ Y) (hf : IsFinite B S hS f.hom)
    (hY : HasEtaleLocalProperty B S hS Y.1 (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (G : Modules.{u, u} B S hS X.1 X.2) (hG : IsCoherent B S hS X.1 X.2 G)
    (V : SmallEtale B S hS Y.1) (hsurj : IsSurjective B S hS V.1.hom)
    (hchart : IsFinite B S hS (chartBaseChangeProjection B S hS f V).hom →
      HasEtaleLocalProperty B S hS
        ((SpacesEtale.toSpaces B S hS Y).obj ((comparisonFunctor B S hS Y).obj V)).1
        (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) →
      IsCoherent B S hS X.1 X.2 G →
      ((chartLocalizedModulePushforward B S hS f V).obj
        ((moduleChartBaseChangeRestriction B S hS f V).obj G)).IsCoherentOnSite) :
    IsCoherent B S hS Y.1 Y.2 ((modulePushforward B S hS f).obj G)
```

**`AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isFinite_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteDirectImageVanishingUnconditional.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteDirectImageVanishingUnconditional.lean#L81). The attribute's comment: “vanishing of the higher direct images, with nothing carried”.

> **The vanishing half of Stacks 07UH.**  For a finite morphism `f : X ⟶ Y` of algebraic
> spaces over `S`, a coherent `𝒪_X`-module `𝓕` and `p > 0`, the higher direct image vanishes:
> `R^p f_* 𝓕 = 0`.
>
> A finite morphism is affine, `AlgebraicGeometry.Space.IsFinite.isAffineHom`, and a coherent
> module is quasi-coherent, so this is Stacks 073H,
> `AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isQuasicoherentOnSite`.
>
> `AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isFinite` is the same
> statement with the affine case carried as the hypothesis `h03DW` and with `𝓕` only required to
> be a module; that hypothesis is now discharged by
> `AlgebraicGeometry.Space.chartwiseIsZeroHigherDirectImage_of_isAffineHom`, which asks for `𝓕`
> quasi-coherent and `p > 0` — exactly what the source assumes here.
>
> The source also assumes `Y` locally Noetherian; that is used by the coherence half of the tag,
> not by this one.

```lean
theorem isZero_rightDerived_modulePushforward_of_isFinite_of_isCoherent
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsFinite B S hS f.hom)
    (G : Modules.{u, u} B S hS X.1 X.2) (hG : IsCoherent B S hS X.1 X.2 G) (p : ℕ)
    (hp : 0 < p) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    IsZero (((modulePushforward B S hS f).rightDerived p).obj G)
```

**`AlgebraicGeometry.Space.isCoherent_modulePushforward_of_isFinite'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperRepresentableDirectImageCoherence.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperRepresentableDirectImageCoherence.lean#L189). The attribute's comment: “coherence of the direct image”.

> **Stacks 07UH, coherence of the direct image.**  Let `f : X ⟶ Y` be a finite morphism of
> algebraic spaces over `S` with `Y` locally Noetherian, and let `𝓕` be a coherent `𝒪_X`-module.
> Then `f_*𝓕` is a coherent `𝒪_Y`-module.
>
> A finite morphism is affine, hence representable
> (`AlgebraicGeometry.Space.relativelyRepresentable_of_isAffineHom`), and proper by Stacks 04NZ
> (`AlgebraicGeometry.Space.isFinite_iff_isAffineHom_and_isProper`), so this is
> `AlgebraicGeometry.Space.isCoherent_modulePushforward_of_isProper`.  The vanishing assertion of
> Stacks 07UH is `AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isFinite`.

```lean
theorem isCoherent_modulePushforward_of_isFinite' (f : X ⟶ Y) (hf : IsFinite B S hS f.hom)
    (hY : HasEtaleLocalProperty B S hS Y.1 (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (M : Modules.{u, u} B S hS X.1 X.2) (hM : IsCoherent B S hS X.1 X.2 M) :
    IsCoherent B S hS Y.1 Y.2 ((modulePushforward B S hS f).obj M)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isFinite_of_isQuasicoherent`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteDirectImageVanishing.lean#L44), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePushforwardTwist.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePushforwardTwist.lean#L127) (StacksFrontier): “vanishing of the higher direct images R^p f\_* F, p > 0”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.12, Tag 07U9](https://stacks.math.columbia.edu/tag/07U9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
