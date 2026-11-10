---
declaration: section
origin: cited
lean: AlgebraicGeometry.isOpenImmersion_of_etale_universallyInjective, AlgebraicGeometry.universallyInjective_of_flat_of_separated_of_genericPoints_injOn, AlgebraicGeometry.isOpenImmersion_of_etale_of_separated_of_genericPoints_injOn, AlgebraicGeometry.isProperOver_of_fpqc, Stacks.Descent.isRelativelyAmple_pullbackModule_of_fpqcCover, Stacks.Descent.isRelativelyAmple_iff_forall_of_fpqcCover_of_iso_unitModule, Stacks.Descent.isRelativelyAmple_iff_forall_of_fpqcCover
statement: formalized
proof: formalized
---

# 35.25 Application of fpqc descent of properties of morphisms

Section 35.25 of the Stacks Project, [Tag 02LB](https://stacks.math.columbia.edu/tag/02LB). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02LC, a lemma

[Tag 02LC](https://stacks.math.columbia.edu/tag/02LC) in the Stacks Project.

**`AlgebraicGeometry.isOpenImmersion_of_etale_universallyInjective`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FpqcDescentApplication/OpenImmersion.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FpqcDescentApplication/OpenImmersion.lean#L53). References: EGA IV (17.9.1), “c) => a)”; SGA 1 IX (1.4), “étale+radicial ⇒ open”; SGA 1 I (5.1), “sufficiency”.

> A universally injective étale morphism of schemes is an open immersion.

```lean
public instance isOpenImmersion_of_etale_universallyInjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [Etale f] [UniversallyInjective f] :
    IsOpenImmersion f
```

## Tag 09NP, a lemma

[Tag 09NP](https://stacks.math.columbia.edu/tag/09NP) in the Stacks Project.

**`AlgebraicGeometry.universallyInjective_of_flat_of_separated_of_genericPoints_injOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SchemeProperty/UniversallyInjective.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SchemeProperty/UniversallyInjective.lean#L60).

> **Stacks Project, Tag 09NP.** A flat separated morphism with isomorphic residue fields
> at, and distinct images of, the generic points of its source is universally injective.

```lean
public theorem universallyInjective_of_flat_of_separated_of_genericPoints_injOn
    {X Y : Scheme.{u}} (f : X ⟶ Y) [Flat f] [IsSeparated f]
    (hres : ∀ ξ ∈ genericPoints X, IsIso (f.residueFieldMap ξ))
    (hinj : Set.InjOn f (genericPoints X)) :
    UniversallyInjective f
```

## Tag 09NQ, a lemma

[Tag 09NQ](https://stacks.math.columbia.edu/tag/09NQ) in the Stacks Project.

**`AlgebraicGeometry.isOpenImmersion_of_etale_of_separated_of_genericPoints_injOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FpqcDescentApplication/OpenImmersion.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FpqcDescentApplication/OpenImmersion.lean#L63).

> An étale separated morphism with isomorphic residue fields at, and distinct images of, the
> generic points of its source is an open immersion.

```lean
public theorem isOpenImmersion_of_etale_of_separated_of_genericPoints_injOn
    {X Y : Scheme.{u}} (f : X ⟶ Y) [Etale f] [IsSeparated f]
    (hres : ∀ ξ ∈ genericPoints X, IsIso (f.residueFieldMap ξ))
    (hinj : Set.InjOn f (genericPoints X)) :
    IsOpenImmersion f
```

## Tag 0F4J, a lemma

[Tag 0F4J](https://stacks.math.columbia.edu/tag/0F4J) in the Stacks Project.

**`AlgebraicGeometry.isProperOver_of_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/ProperClosedSubsetFpqc.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/ProperClosedSubsetFpqc.lean#L49).

> **Stacks 0F4J.** Properness over a base of a closed subset descends along an fpqc covering
> of the base.

```lean
public theorem isProperOver_of_fpqc {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f]
    (Z : Closeds X)
    (h : ∃ (ι : Type v) (Y' : ι → Scheme.{u}) (g : ∀ i, Y' i ⟶ Y),
      Presieve.ofArrows Y' g ∈ Scheme.fpqcPrecoverage Y ∧
        ∀ i, IsProperOver (pullback.snd f (g i))
          (Z.preimage (pullback.fst f (g i)).continuous)) :
    IsProperOver f Z
```

## Tag 0D2P, a lemma

[Tag 0D2P](https://stacks.math.columbia.edu/tag/0D2P) in the Stacks Project.

**`Stacks.Descent.isRelativelyAmple_pullbackModule_of_fpqcCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/RelativeAmpleFpqcLocalOnBase.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/RelativeAmpleFpqcLocalOnBase.lean#L181). The attribute's comment: “(1) implies (2)”.

> **Stacks Tag 0D2P, clause (1) implies clause (2).** Let `f : X ⟶ S` be a morphism of schemes,
> `L` an invertible `𝒪_X`-module and `{g i : S' i ⟶ S}` an fpqc covering of `S`. Let `f' i` be the
> base change of `f` along `g i`, presented by a cartesian square with the other projection
> `p i : X' i ⟶ X`. If `L` is ample relative to `f`, then `(p i)^* L` is ample relative to `f' i`
> for every `i`.
>
> This is [Stacks, Tag 0893] for a cartesian square,
> `Stacks.AmpleBridge.isRelativelyAmple_pullbackModule_of_isPullback`, applied one index at a time;
> no property of the covering enters, and the fpqc hypothesis is carried only so that the statement
> is literally the implication of the source.

```lean
theorem isRelativelyAmple_pullbackModule_of_fpqcCover {S : Scheme.{u}} {I : Type v}
    {S' : I → Scheme.{u}} (g : ∀ i, S' i ⟶ S)
    (_hg : Presieve.ofArrows S' g ∈ Scheme.fpqcPrecoverage S) {X : Scheme.{u}} (f : X ⟶ S)
    (L : X.Modules) [IsInvertibleModule X L] {X' : I → Scheme.{u}} {p : ∀ i, X' i ⟶ X}
    {f' : ∀ i, X' i ⟶ S' i} (hsq : ∀ i, IsPullback (p i) (f' i) f (g i))
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L) :
    ∀ i, Stacks.RelativeAmple.IsRelativelyAmple (f' i) (pullbackModule (p i) L)
```

**`Stacks.Descent.isRelativelyAmple_iff_forall_of_fpqcCover_of_iso_unitModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/RelativeAmpleFpqcLocalOnBase.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/RelativeAmpleFpqcLocalOnBase.lean#L238). The attribute's comment: “the full equivalence for an invertible module isomorphic to the structure sheaf”. References: SGA 1 VIII (7.8), “special case”.

> **Stacks Tag 0D2P, both directions, for an invertible module isomorphic to `𝒪_X`.** With
> `{g i : S' i ⟶ S}` an fpqc covering of `S` and each square with sides `p i`, `f' i`, `f` and
> `g i` cartesian, a module `L` isomorphic to the structure sheaf is ample relative to `f` if and
> only if `(p i)^* L` is ample relative to `f' i` for every `i`.
>
> Both sides are quasi-affineness: on the left by
> `Stacks.AmplePullback.isRelativelyAmple_iff_isQuasiAffineHom_of_iso_unitModule`, which is
> [Stacks, Tag 0891] for a module merely isomorphic to `𝒪_X`, and on the right by the same lemma
> applied to the isomorphism `Stacks.AmplePullback.modulePullbackIsoUnitModule` of `(p i)^* L` with
> `𝒪_{X' i}`. The equivalence between them is then [Stacks, Tag 02L7], that quasi-affine morphisms
> are fpqc local on the base.

```lean
theorem isRelativelyAmple_iff_forall_of_fpqcCover_of_iso_unitModule {S : Scheme.{u}} {I : Type v}
    {S' : I → Scheme.{u}} {g : ∀ i, S' i ⟶ S}
    (hg : Presieve.ofArrows S' g ∈ Scheme.fpqcPrecoverage S) {X : Scheme.{u}} (f : X ⟶ S)
    (L : X.Modules) [IsInvertibleModule X L] (e : L ≅ unitModule X) {X' : I → Scheme.{u}}
    {p : ∀ i, X' i ⟶ X} {f' : ∀ i, X' i ⟶ S' i}
    (hsq : ∀ i, IsPullback (p i) (f' i) f (g i)) :
    Stacks.RelativeAmple.IsRelativelyAmple f L ↔
      ∀ i, Stacks.RelativeAmple.IsRelativelyAmple (f' i) (pullbackModule (p i) L)
```

**`Stacks.Descent.isRelativelyAmple_iff_forall_of_fpqcCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/RelativeAmpleFpqcLocalOnBaseFull.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/RelativeAmpleFpqcLocalOnBaseFull.lean#L363). References: SGA 1 VIII (7.8), “more general”.

> **Stacks Tag 0D2P.** Let `f : X ⟶ S` be a morphism of schemes, `L` an invertible
> `𝒪_X`-module and `{g i : S' i ⟶ S}_{i ∈ I}` an fpqc covering of `S`. Let `f' i : X' i ⟶ S' i` be
> the base change of `f` along `g i`, presented by a cartesian square with other projection
> `p i : X' i ⟶ X`, and let `(p i)^* L` be the pullback of `L`. The following are equivalent:
>
> 1. `L` is ample on `X / S`;
> 2. `(p i)^* L` is ample on `X' i / S' i` for every `i ∈ I`.
>
> Clause (1) implies clause (2) by [Stacks, Tag 0893] applied to each square,
> `Stacks.Descent.isRelativelyAmple_pullbackModule_of_fpqcCover`. Clause (2) implies clause (1) is
> `Stacks.Descent.isRelativelyAmple_of_forall_of_fpqcCover`.

```lean
theorem isRelativelyAmple_iff_forall_of_fpqcCover {S : Scheme.{u}} {I : Type v}
    {S' : I → Scheme.{u}} {g : ∀ i, S' i ⟶ S}
    (hg : Presieve.ofArrows S' g ∈ Scheme.fpqcPrecoverage S) {X : Scheme.{u}} (f : X ⟶ S)
    (L : X.Modules) [IsInvertibleModule X L] {X' : I → Scheme.{u}} {p : ∀ i, X' i ⟶ X}
    {f' : ∀ i, X' i ⟶ S' i} (hsq : ∀ i, IsPullback (p i) (f' i) f (g i)) :
    Stacks.RelativeAmple.IsRelativelyAmple f L ↔
      ∀ i, Stacks.RelativeAmple.IsRelativelyAmple (f' i) (pullbackModule (p i) L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.25, Tag 02LB](https://stacks.math.columbia.edu/tag/02LB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
