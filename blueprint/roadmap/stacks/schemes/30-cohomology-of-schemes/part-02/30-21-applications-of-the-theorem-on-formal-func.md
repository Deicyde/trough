---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsFinite.tfae_isProper_finite_preimage_singleton, Stacks.FormalFunctions.exists_isFinite_morphismRestrict_of_finite_fibre, Stacks.FormalFunctions.exists_isZero_stalk_rightDerived_and_surjective_fiberTwist, Stacks.AmpleFibreNeighbourhood.exists_mem_isRelativelyAmple_of_isAmple_fibre
statement: formalized
proof: formalized
---

# 30.21 Applications of the theorem on formal functions

Section 30.21 of the Stacks Project, [Tag 02OF](https://stacks.math.columbia.edu/tag/02OF). 4 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02OG, a lemma

[Tag 02OG](https://stacks.math.columbia.edu/tag/02OG) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsFinite.tfae_isProper_finite_preimage_singleton`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/FiniteFibres.lean#L62), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalFunctions/FiniteIffProperFiniteFibres.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalFunctions/FiniteIffProperFiniteFibres.lean#L32) (StacksFrontier): “the equivalence of the first two conditions, for an arbitrary target; the source assumes it locally Noetherian”.

## Tag 02OH, a lemma

[Tag 02OH](https://stacks.math.columbia.edu/tag/02OH) in the Stacks Project.

**`Stacks.FormalFunctions.exists_isFinite_morphismRestrict_of_finite_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/FiniteFibreVanishing.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalFunctions/FiniteFibreVanishing.lean#L161). References: EGA III (4.8.11), “ordinary schemes”.

> **Stacks Project, Tag 02OH.** Let `f : X ⟶ Y` be a morphism of schemes and let `y : Y`.
> Assume `Y` is locally Noetherian, `f` is proper, and the fibre `f ⁻¹' {y}` is finite. Then `y` has
> an open neighbourhood `V` over which `f` is finite, that is, `f ∣_ V : f ⁻¹ᵁ V ⟶ V` is finite.
>
> This is Zariski's main theorem in the form of [Stacks, Tag 02UP]
> (`AlgebraicGeometry.exists_isFinite_morphismRestrict_of_finite_preimage_singleton`), which needs
> no hypothesis on `Y`; local Noetherianness is kept here because the tag states it. The source
> instead deduces the lemma from Tag 02OG, finiteness being equivalent to properness with finite
> fibres over a locally Noetherian base; that route is unavailable here, and it would in any case be
> circular, since Tag 02OG rests on Tag 02OE above.

```lean
theorem exists_isFinite_morphismRestrict_of_finite_fibre {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsLocallyNoetherian Y] [IsProper f] (y : Y) (hfin : (f ⁻¹' {y}).Finite) :
    ∃ V : Y.Opens, y ∈ V ∧ IsFinite (f ∣_ V)
```

## Tag 0D2M, a lemma

[Tag 0D2M](https://stacks.math.columbia.edu/tag/0D2M) in the Stacks Project.

**`Stacks.FormalFunctions.exists_isZero_stalk_rightDerived_and_surjective_fiberTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/AmpleFibreTwistStalkSurjective.lean, line 701](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalFunctions/AmpleFibreTwistStalkSurjective.lean#L701).

> **[Stacks, Tag 0D2M].**
>
> Let `f : X ⟶ Y` be a proper morphism of schemes with `Y` Noetherian, let `ℒ` be an invertible
> `𝒪_X`-module, let `ℱ` be a coherent `𝒪_X`-module and let `y ∈ Y` be a point such that
> `ℒ_y` is ample on the fibre `X_y`. Then there exists a `d₀` such that for all `d ≥ d₀`
>
> 1. `R ᵖ f_*(ℱ ⊗_{𝒪_X} ℒ ^⊗ d)_y = 0` for `p > 0`, and
> 2. the map `f_*(ℱ ⊗_{𝒪_X} ℒ ^⊗ d)_y ⟶ H ⁰(X_y, ℱ_y ⊗_{𝒪_{X_y}} ℒ_y ^⊗ d)` is surjective.
>
> Here `X_y` is `f.fiber y` with its morphism `f.fiberι y` to `X`, `ℱ_y` and `ℒ_y` are the
> restrictions of `ℱ` and `ℒ` to it, `R ᵖ f_*` is the `p`-th right derived functor of
> `Scheme.Modules.pushforward f`, and `H ⁰(X_y, -)` is the module of global sections. The map in
> the second clause is `Stacks.FormalFunctions.fiberTwistSectionsStalkHom`: the germ at `y` of a
> section over `f ⁻¹ U` goes to its restriction to the fibre. The proof is
> `exists_isZero_stalk_rightDerived_and_surjective_twistModule` together with the identification
> `(f.fiberι y) ^* (ℱ ⊗ ℒ ^⊗ d) ≅ ℱ_y ⊗ ℒ_y ^⊗ d` of [Stacks, Tag 0EGK].

```lean
public theorem exists_isZero_stalk_rightDerived_and_surjective_fiberTwist (f : X ⟶ Y)
    [IsProper f] [AlgebraicGeometry.IsNoetherian Y] (y : Y) (F L : X.Modules)
    [IsInvertibleModule X L] [F.IsCoherent]
    (hL : IsAmple (f.fiber y) (pullbackModule (f.fiberι y) L)) :
    ∃ d₀ : ℤ, ∀ d : ℤ, d₀ ≤ d →
      (∀ p : ℕ, 0 < p →
          IsZero ((((Scheme.Modules.pushforward f).rightDerived p).obj
            (twistModule X L F d)).presheaf.stalk y)) ∧
        Function.Surjective (fiberTwistSectionsStalkHom f y F L d)
```

## Tag 0D2N, a lemma

[Tag 0D2N](https://stacks.math.columbia.edu/tag/0D2N) in the Stacks Project.

**`Stacks.AmpleFibreNeighbourhood.exists_mem_isRelativelyAmple_of_isAmple_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleFibreNeighbourhood/RelativelyAmpleNeighbourhood.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AmpleFibreNeighbourhood/RelativelyAmpleNeighbourhood.lean#L71).

> **Stacks Project, Tag 0D2N.**  Let `f : X ⟶ Y` be a proper morphism of schemes with `Y`
> Noetherian, let `ℒ` be an invertible `𝒪_X`-module and let `y` be a point of `Y` such that `ℒ_y`
> is ample on the fibre `X_y`.  Then there is an open neighbourhood `V` of `y` such that
> `ℒ|_{f⁻¹V}` is ample relative to `f⁻¹V / V`.
>
> Invertibility of `ℒ_y` is not a hypothesis: it is an instance, the pullback of an invertible
> module being invertible (`Stacks.InvertiblePullback.isInvertibleModule_pullback`).
>
> The two halves are
> `Stacks.AmpleFibreNeighbourhood.exists_mem_pullbackSection_fiberι_eq` — the lifting of sections
> from the fibre, which is where [Stacks, Tag 0D2M] and the reduction to `Spec 𝒪_{Y, y}` live — and
> `Stacks.AmpleFibreNeighbourhood.exists_mem_isRelativelyAmple_of_exists_lift`, which is the rest
> of the source's argument.

```lean
theorem exists_mem_isRelativelyAmple_of_isAmple_fibre {X S : Scheme.{u}} (f : X ⟶ S)
    [IsProper f] [IsNoetherian S] (L : X.Modules) [IsInvertibleModule X L] (y : S)
    (hL : IsAmple (f.fiber y) (pullbackModule (f.fiberι y) L)) :
    ∃ V : S.Opens, y ∈ V ∧
      Stacks.RelativeAmple.IsRelativelyAmple (f ∣_ V) (pullbackModule (f ⁻¹ᵁ V).ι L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.21, Tag 02OF](https://stacks.math.columbia.edu/tag/02OF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
