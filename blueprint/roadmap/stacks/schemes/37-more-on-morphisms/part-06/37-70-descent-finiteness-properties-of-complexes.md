---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_forall_derivedPullback_of_mem_fppfPrecoverage, AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_derivedPullback_of_mem_fppfPrecoverage', AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_comp_iff_of_flat, AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_forall_pullback_snd_of_pseudoCoherent, AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_forall_pullback_snd
statement: formalized
proof: formalized
---

# 37.70 Descent finiteness properties of complexes

Section 37.70 of the Stacks Project, [Tag 0CSM](https://stacks.math.columbia.edu/tag/0CSM). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CSN, a lemma

[Tag 0CSN](https://stacks.math.columbia.edu/tag/0CSN) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_forall_derivedPullback_of_mem_fppfPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFppfDescentConverse.lean, line 432](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFppfDescentConverse.lean#L432). The attribute's comment: “both implications, at the source's hypotheses: f locally of finite type, an arbitrary fppf covering of X (Presieve.ofArrows in Scheme.fppfPrecoverage, any index universe), E with quasi-coherent cohomology sheaves, any m”.

> **Stacks 0CSN.** Let `f : X ⟶ S` be locally of finite type, let `{g i : Y i ⟶ X}` be an fppf
> covering of schemes, let `E` be an object of `D(𝒪_X)` with quasi-coherent cohomology sheaves and
> let `m` be an integer. Then `E` is `m`-pseudo-coherent relative to `S` if and only if every
> `L(g i)^*E` is `m`-pseudo-coherent relative to `S`.
>
> The forward implication is Stacks 0695 (a member of an fppf covering is flat and locally of
> finite presentation, hence pseudo-coherent) followed by Stacks 09US,
> `AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_comp_derivedPullback`; it needs neither joint
> surjectivity nor the quasi-coherence of `E`. The converse is
> `Scheme.Hom.isPseudoCoherentFrom_of_forall_derivedPullback_of_mem_fppfPrecoverage` (Stacks 05WN,
> 0683, 09US, 09UK, 08EU, 09UN and Zariski gluing). The membership of `g i ≫ f` in the class of
> morphisms locally of finite type, which the predicate takes as an instance argument, comes from the
> covering.

```lean
public theorem Scheme.Hom.isPseudoCoherentFrom_iff_forall_derivedPullback_of_mem_fppfPrecoverage
    {X S : Scheme.{u}} {ι : Type v} (Y : ι → Scheme.{u}) (g : ∀ i, Y i ⟶ X) (f : X ⟶ S)
    [LocallyOfFiniteType f] (hg : Presieve.ofArrows Y g ∈ Scheme.fppfPrecoverage X)
    (E : DerivedCategory X.Modules)
    (hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj E).IsQuasicoherent)
    (m : ℤ) :
    f.IsPseudoCoherentFrom E m ↔
      ∀ i, letI : LocallyOfFinitePresentation (g i) :=
          locallyOfFinitePresentation_of_mem_fppfPrecoverage Y g hg i
        (g i ≫ f).IsPseudoCoherentFrom ((derivedPullback (g i).toLRSHom.toShHom).obj E) m
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_derivedPullback_of_mem_fppfPrecoverage'`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFppfDescentPullback.lean#L85), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFppfDescentPullback.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFppfDescentPullback.lean#L99) (StacksFrontier): “THE FORWARD IMPLICATION ONLY, with the Stacks 09US hypothesis DISCHARGED; the tag is an iff and its converse is NOT proved. Base already registers the forward half at PseudoCoherent/RelativeFppfDescent.lean:148, which carries 09US as a hypothesis; that file's own notes say discharging it is what would make the implication unconditional. 09US is now proved (PseudoCoherent/DerivedPullback09US.lean:634), so this restatement carries only 0E23 (DerivedBaseChangeIsoOfTorIndependent), which 09US itself already requires -- strictly fewer hypotheses than the base form. The covering is genuinely fppf (Presieve.ofArrows in Scheme.fppfPrecoverage), not etale or Zariski; no quasi-compactness, finiteness or Noetherian hypothesis is added, and nothing is assumed about E's cohomology sheaves. THE CONVERSE needs exactly two things the library lacks: Stacks 08EU at a GENERAL K (the library has it only at K = O\_Y[0], and its docstring says the devissage to general K is not carried out), and the local splitting of O\_X -> pi\_* O\_Y for a surjective finite locally free pi, which is absent entirely.”.

## Tag 0CSP, a lemma

[Tag 0CSP](https://stacks.math.columbia.edu/tag/0CSP) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_comp_iff_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFlatBase.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFlatBase.lean#L56).

> **Stacks 0CSP.** Let `f : X ⟶ T` be locally of finite type, let `g : T ⟶ S` be flat and
> locally of finite presentation, let `E` be an object of `D(𝒪_X)` and let `m` be an integer. Then
> `E` is `m`-pseudo-coherent relative to `S` if and only if it is `m`-pseudo-coherent relative
> to `T`.

```lean
public theorem isPseudoCoherentFrom_comp_iff_of_flat
    {X T S : Scheme.{u}} (f : X ⟶ T) (g : T ⟶ S) [LocallyOfFiniteType f] [Flat g]
    [LocallyOfFinitePresentation g] (E : DerivedCategory X.Modules) (m : ℤ) :
    (f ≫ g).IsPseudoCoherentFrom E m ↔ f.IsPseudoCoherentFrom E m
```

## Tag 0CSQ, a lemma

[Tag 0CSQ](https://stacks.math.columbia.edu/tag/0CSQ) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_forall_pullback_snd_of_pseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFppfBaseChange.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFppfBaseChange.lean#L101). The attribute's comment: “both directions, for a pseudo-coherent f -- by Stacks 0684 this is every f locally of finite type over a locally Noetherian base; no hypothesis on the cohomology sheaves of E is used”.

> **Stacks 0CSQ for a pseudo-coherent `f`.** Let `f : X ⟶ S` be a pseudo-coherent morphism of
> schemes, let `{g i : S i ⟶ S}` be an fppf covering, let `E` be an object of `D(𝒪_X)` and let `m`
> be an integer. Then `E` is `m`-pseudo-coherent relative to `S` if and only if the derived pullback
> of `E` to `X ×_S S i` is `m`-pseudo-coherent relative to `S i` for every `i`.

```lean
public theorem Scheme.Hom.isPseudoCoherentFrom_iff_forall_pullback_snd_of_pseudoCoherent
    {X S : Scheme.{u}} (f : X ⟶ S) [PseudoCoherent f] {ι : Type v} (Y : ι → Scheme.{u})
    (g : ∀ i, Y i ⟶ S) (hg : Presieve.ofArrows Y g ∈ Scheme.fppfPrecoverage S)
    (E : DerivedCategory X.Modules) (m : ℤ) :
    f.IsPseudoCoherentFrom E m ↔
      ∀ i, (pullback.snd f (g i)).IsPseudoCoherentFrom
        ((derivedPullback (pullback.fst f (g i)).toLRSHom.toShHom).obj E) m
```

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_iff_forall_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFppfBaseChangeGeneral.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeFppfBaseChangeGeneral.lean#L330).

> **Stacks 0CSQ.** Let `f : X ⟶ S` be locally of finite type, let `{g a : Y a ⟶ S}` be an fppf
> covering, let `E` be an object of `D(𝒪_X)` and let `m` be an integer. Then `E` is
> `m`-pseudo-coherent relative to `S` if and only if the derived pullback of `E` to `X ×_S Y a` is
> `m`-pseudo-coherent relative to `Y a` for every `a`.
>
> The forward direction is Stacks 09UR at the flat morphism `g a`; the converse is
> `AlgebraicGeometry.Scheme.Hom.isPseudoCoherentFrom_of_forall_pullback_snd`. No hypothesis on the
> cohomology sheaves of `E` is used.

```lean
public theorem Scheme.Hom.isPseudoCoherentFrom_iff_forall_pullback_snd {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFiniteType f] {ι : Type v} (Y : ι → Scheme.{u}) (g : ∀ a, Y a ⟶ S)
    (hg : Presieve.ofArrows Y g ∈ Scheme.fppfPrecoverage S) (E : DerivedCategory X.Modules)
    (m : ℤ) :
    f.IsPseudoCoherentFrom E m ↔
      ∀ a, (pullback.snd f (g a)).IsPseudoCoherentFrom
        ((derivedPullback (pullback.fst f (g a)).toLRSHom.toShHom).obj E) m
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.70, Tag 0CSM](https://stacks.math.columbia.edu/tag/0CSM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
