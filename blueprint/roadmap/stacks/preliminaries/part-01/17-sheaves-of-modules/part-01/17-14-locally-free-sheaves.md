---
declaration: section
origin: cited
lean: SheafOfModules.IsLocallyFree, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank, SheafOfModules.instIsQuasicoherentOfIsLocallyFree, pullback_isLocallyFree, LocallyFreeRank.exists_locallyConstant_rank, Stacks.SheafOfModules.isIso_iff_epi_of_isFiniteLocallyFreeOfRank, AlgebraicGeometry.SheafOfModules.isFiniteLocallyFree_of_retract
statement: formalized
proof: formalized
---

# 17.14 Locally free sheaves

Section 17.14 of the Stacks Project, [Tag 01C5](https://stacks.math.columbia.edu/tag/01C5). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 11 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01C5, the section

[Tag 01C5](https://stacks.math.columbia.edu/tag/01C5) in the Stacks Project.

Declarations registered for the tag:

- [`SheafOfModules.IsLocallyFree`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.IsLocallyFree#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean#L68) (StacksFrontier): “section tag; 01C6 (1), locally free”. References: EGA 0 (5.4.1), “more general”; EGA III (7.9.1); EGA IV (21.5.3), “partial”.
- [`AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFree.lean#L73), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean#L72) (StacksFrontier): “section tag; 01C6 (2), finite locally free”.
- [`AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFree.lean#L81), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean#L74) (StacksFrontier): “section tag; 01C6 (3), of rank r”.
- [`SheafOfModules.instIsQuasicoherentOfIsLocallyFree`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.instIsQuasicoherentOfIsLocallyFree#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean#L76) (StacksFrontier): “section tag; 01C7, locally free ⇒ quasi-coherent”. References: EGA 0 (5.4.1), “loc. free ⇒ qcoh”.
- [`pullback_isLocallyFree`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreePullback.lean#L258), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean#L78) (StacksFrontier): “section tag; 01C8, pullback is locally free”.
- [`LocallyFreeRank.exists_locallyConstant_rank`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreeRank.lean#L1240), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean#L79) (StacksFrontier): “section tag; 01C9, locally constant rank”.
- [`Stacks.SheafOfModules.isIso_iff_epi_of_isFiniteLocallyFreeOfRank`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/EpiOfConstantRank.lean#L232), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean#L81) (StacksFrontier): “section tag; 089Q, iso iff surjective in equal rank”.
- [`AlgebraicGeometry.SheafOfModules.isFiniteLocallyFree_of_retract`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFreeRetract.lean#L347), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFreeSection.lean#L83) (StacksFrontier): “section tag; 0BCI, summand of finite locally free”.

## Tag 01C6, a definition

[Tag 01C6](https://stacks.math.columbia.edu/tag/01C6) in the Stacks Project.

**`RS.Modules.IsLocallyFree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreePullback.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreePullback.lean#L163). The attribute's comment: “part (1), locally free with an arbitrary index set”. References: EGA 0 (5.4.1); EGA III (7.9.1); EGA IV (2.1.12); EGA IV (21.5.3), “partial”.

> Definition 1 (locally free, Tag 01C6): a sheaf of `O_X`-modules `M` is locally free if
> every point `x ∈ X` has an open neighbourhood `U` such that the restriction `M|_U` is
> isomorphic, as a sheaf of `O_X|_U`-modules, to a free module `⨁_{i ∈ I} (O_X|_U)` for some
> index type `I` (allowed to be arbitrary and to depend on `x`).
>
> No finiteness is imposed on `I`, nor any bound on its cardinality: it ranges over all of
> `Type u`, the universe in which the structure sheaf of `X` takes its values and hence the only
> one in which `SheafOfModules.free` forms a direct sum of copies of `O_X|_U`. The finite and
> fixed-rank refinements, parts (2) and (3) of the same definition, are
> `AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree` and `.IsFiniteLocallyFreeOfRank`.

```lean
def RS.Modules.IsLocallyFree {X : AlgebraicGeometry.RingedSpace.{u, u}}
    (M : RS.Modules X) : Prop
```

**`AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/LocallyFree.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFree.lean#L73). The attribute's comment: “(2)”. References: EGA 0 (5.4.1), “finite rank”.

> A sheaf of modules is finite locally free if it has local free presentations whose
> basis-indexing types are finite.

```lean
class IsFiniteLocallyFree (M : _root_.SheafOfModules.{u} R) : Prop
```

**`AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/LocallyFree.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFree.lean#L81). The attribute's comment: “(3)”. References: EGA 0 (5.4.1), “rank n”.

> A sheaf of modules is finite locally free of rank `r` if it has local free presentations
> whose basis-indexing types are equivalent to `Fin r`.

```lean
class IsFiniteLocallyFreeOfRank (M : _root_.SheafOfModules.{u} R) (r : ℕ) : Prop
```

## Tag 01C7, a lemma

[Tag 01C7](https://stacks.math.columbia.edu/tag/01C7) in the Stacks Project.

Declarations registered for the tag:

- [`SheafOfModules.instIsQuasicoherentOfIsLocallyFree`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.instIsQuasicoherentOfIsLocallyFree#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFree.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFree.lean#L16) (StacksFrontier): “loc. free ⇒ qcoh”. References: EGA 0 (5.4.1), “loc. free ⇒ qcoh”.
- [`SheafOfModules.IsLocallyFree.exists_isLocallyFreeData`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.IsLocallyFree.exists_isLocallyFreeData#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFree.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFree.lean#L17) (StacksFrontier): “locally free data”.
- [`SheafOfModules.LocalGeneratorsData.quasiCoherentData`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.LocalGeneratorsData.quasiCoherentData#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFree.lean, line 18](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFree.lean#L18) (StacksFrontier): “presentation, no rels”. References: EGA 0 (5.4.1).

## Tag 01C8, a lemma

[Tag 01C8](https://stacks.math.columbia.edu/tag/01C8) in the Stacks Project.

**`pullback_isLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreePullback.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreePullback.lean#L258). References: EGA 0 (5.4.5), “locally free case”; EGA II (6.4.8), “partial”; EGA IV (8.5.5), “Sufficiency”.

> Statement 1 (Stacks Tag 01C8, Lemma 17.14.3): the pullback `f^*G` of a locally free
> sheaf of modules `G` along a morphism of ringed spaces `f` is locally free.

```lean
theorem pullback_isLocallyFree {X Y : AlgebraicGeometry.RingedSpace.{u, u}} (f : X ⟶ Y)
    (G : RS.Modules Y) (hG : RS.Modules.IsLocallyFree G) :
    RS.Modules.IsLocallyFree ((RS.Modules.pullback f).obj G)
```

## Tag 01C9, a lemma

[Tag 01C9](https://stacks.math.columbia.edu/tag/01C9) in the Stacks Project.

**`LocallyFreeRank.exists_locallyConstant_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreeRank.lean, line 1240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreeRank.lean#L1240). References: EGA 0 (5.4.1), “n(x) locally constant”; EGA II (6.4.8), “partial”; EGA IV (19.7.4), “partial”; SGA 6 I (6.0), “existence of rg_U(L)”; SGA 5 VII (3.2), “more general”; SGA 6 I (6.10), “special case”; SGA 6 III (5.4.1), “special case”.

> **Stacks Tag 01C9.**  Let `X` be a ringed space whose structure sheaf `O_X` is a sheaf
> of commutative rings all of whose stalks `O_{X,x}` are nonzero, and let `F` be a locally
> free sheaf of `O_X`-modules.  Then there is a locally constant function
> `rank_F : X → Cardinal` such that for every point `x` and every trivialisation `t` of `F` on
> an open neighbourhood `U` of `x`, the cardinality of the index set of `t` equals `rank_F x`.
>
> This single statement encodes both that the rank at a point is well defined (independent of
> the trivialisation chosen) and that the resulting function is locally constant.

```lean
theorem exists_locallyConstant_rank
    (X : TopCat.{u})
    (O : Sheaf (Opens.grothendieckTopology X) CommRingCat.{u})
    (hO : StalksNontrivial X O)
    (F : SheafOfModules.{u} (toRingSheaf X O))
    (hF : IsLocallyFree X (toRingSheaf X O) F) :
    ∃ rankF : X → Cardinal.{u},
      IsLocallyConstant rankF ∧
      ∀ (x : X) (U : Opens X), x ∈ U →
        ∀ t : Trivialization X (toRingSheaf X O) F U, t.rank = rankF x
```

## Tag 089Q, a lemma

[Tag 089Q](https://stacks.math.columbia.edu/tag/089Q) in the Stacks Project.

**`Stacks.SheafOfModules.isIso_iff_epi_of_isFiniteLocallyFreeOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/EpiOfConstantRank.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/EpiOfConstantRank.lean#L232).

> **Stacks 089Q.** A morphism between finite locally free sheaves of modules of the same
> rank is an isomorphism if and only if it is surjective.

```lean
theorem isIso_iff_epi_of_isFiniteLocallyFreeOfRank
    (X : RingedSpace.{u, u})
    [∀ U : Opens X, HasWeakSheafify ((Opens.grothendieckTopology X).over U) AddCommGrpCat.{u}]
    [∀ U : Opens X, ((Opens.grothendieckTopology X).over U).WEqualsLocallyBijective
      AddCommGrpCat.{u}]
    {F G : _root_.SheafOfModules.{u} (StrictlyPerfect.structureSheafOfRings X)} (r : ℕ)
    [@AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank _ _ _
      (StrictlyPerfect.structureSheafOfRings X) _ _ F r]
    [@AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank _ _ _
      (StrictlyPerfect.structureSheafOfRings X) _ _ G r] (f : F ⟶ G) :
    IsIso f ↔ Epi f
```

## Tag 0BCI, a lemma

[Tag 0BCI](https://stacks.math.columbia.edu/tag/0BCI) in the Stacks Project.

**`Stacks.AffineTilde.exists_finite_span_free_away_of_retract_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherentRelative/TildeRetract.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherentRelative/TildeRetract.lean#L174). The attribute's comment: “affine case: a direct summand of a finite free module on Spec R”. References: SGA 6 I (2.15.1), “affine case”.

> **The affine case of Stacks 0BCI, in standard opens.** A direct summand `F` of a finite free
> `𝒪_{Spec R}`-module is `N^~` for an `R`-module `N` which becomes finite free over `R_g` for each
> `g` in a finite family generating the unit ideal; equivalently, `F` is finite free on each member
> of a finite covering of `Spec R` by standard opens.
>
> This is `Stacks.AffineTilde.exists_finiteProjective_tilde_of_retract_free` followed by the
> equivalence of "finite projective" with "finite locally free" (Stacks 00NX), whose spanning set
> is shrunk to a finite one by `Ideal.span_eq_top_iff_finite`.

```lean
public theorem exists_finite_span_free_away_of_retract_free {ι : Type u} [Finite ι]
    {F : (Spec R).Modules} (h : Retract F (SheafOfModules.free.{u} ι)) :
    ∃ N : ModuleCat.{u} R, Nonempty ((tilde.functor R).obj N ≅ F) ∧
      ∃ s : Finset R, Ideal.span (s : Set R) = ⊤ ∧
        ∀ g ∈ s, Module.Free (Localization.Away g) (LocalizedModule.Away g N) ∧
          Module.Finite (Localization.Away g) (LocalizedModule.Away g N)
```

**`AlgebraicGeometry.SheafOfModules.isFiniteLocallyFree_of_retract`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/LocallyFreeRetract.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/LocallyFreeRetract.lean#L347). References: SGA 6 I (2.15.1), “ringed space case”.

> **Stacks Project, Tag 0BCI.** A direct summand of a finite locally free sheaf of modules on
> a ringed space whose stalks are local rings is finite locally free.
>
> The tag attribute for 0BCI belongs on this declaration and on no other: the tag's covering set
> is this one statement. It is deliberately not placed here, attribute placement being the lead's.

```lean
theorem isFiniteLocallyFree_of_retract
    [∀ x : X, IsLocalRing (ToType (TopCat.Presheaf.stalk O.obj x))]
    {F H : _root_.SheafOfModules.{u} (LocallyFreeRank.toRingSheaf X O)}
    (hF : Nonempty (Retract F H))
    (hH : @IsFiniteLocallyFree (Opens X) inferInstance (Opens.grothendieckTopology X)
      (LocallyFreeRank.toRingSheaf X O) (fun _ ↦ inferInstance) (fun _ ↦ inferInstance) H) :
    @IsFiniteLocallyFree (Opens X) inferInstance (Opens.grothendieckTopology X)
      (LocallyFreeRank.toRingSheaf X O) (fun _ ↦ inferInstance) (fun _ ↦ inferInstance) F
```

**`Stacks.SheafOfModules.isFiniteLocallyFree_of_retract`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RecoveryExtend/FiniteLocallyFreeRetract.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/RecoveryExtend/FiniteLocallyFreeRetract.lean#L325). References: SGA 6 I (2.15.1), “ringed space case”.

> **Stacks Project, Tag 0BCI.** A direct summand of a finite locally free sheaf of modules
> on a ringed space whose structure-sheaf stalks are local rings is finite locally free.

```lean
theorem isFiniteLocallyFree_of_retract
    {X : TopCat.{u}} {O : TopCat.Sheaf CommRingCat.{u} X}
    [∀ x : X, IsLocalRing (ToType (O.presheaf.stalk x))]
    {F H : _root_.SheafOfModules.{u}
      ((sheafCompose (Opens.grothendieckTopology X)
        (forget₂ CommRingCat RingCat)).obj O)}
    (hF : Nonempty (@Retract (_root_.SheafOfModules.{u}
      ((sheafCompose (Opens.grothendieckTopology X)
        (forget₂ CommRingCat RingCat)).obj O))
      _root_.SheafOfModules.instCategory F H))
    (hH : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree
      (R := (sheafCompose (Opens.grothendieckTopology X)
        (forget₂ CommRingCat RingCat)).obj O) H) :
    AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree
      (R := (sheafCompose (Opens.grothendieckTopology X)
        (forget₂ CommRingCat RingCat)).obj O) F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.14, Tag 01C5](https://stacks.math.columbia.edu/tag/01C5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
