---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsRelativeEquivalenceKernel, AlgebraicGeometry.isEquivalence_quasiCoherentFourierMukai_of_isRelativeEquivalenceKernel, AlgebraicGeometry.isEquivalence_perfectFourierMukai_of_isRelativeEquivalenceKernel, AlgebraicGeometry.isEquivalence_quasiCoherentFourierMukai, AlgebraicGeometry.isEquivalence_perfectFourierMukai, AlgebraicGeometry.isRelativeEquivalenceKernel_derivedPullback, AlgebraicGeometry.isRelativeEquivalenceKernel_baseChange, AlgebraicGeometry.exists_isRelativeEquivalenceKernel_of_descentSituation
statement: formalized
proof: formalized
---

# 57.15 Relative equivalences

Section 57.15 of the Stacks Project, [Tag 0G0H](https://stacks.math.columbia.edu/tag/0G0H). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G0I, a definition

[Tag 0G0I](https://stacks.math.columbia.edu/tag/0G0I) in the Stacks Project.

**`AlgebraicGeometry.IsRelativeEquivalenceKernel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalence.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalence.lean#L123). The attribute's comment: “the Fourier-Mukai kernel of a relative equivalence from `X` to `Y` over `S`, as the predicate on a perfect object of `D(𝒪_{X ×_S Y})` asserting the existence of a perfect `K'` on `Y ×_S X` with the two convolution isomorphisms; stated for arbitrary `f` and `g` rather than only smooth proper ones”.

> **[Stacks, Tag 0G0I]**: `K` is *the Fourier-Mukai kernel of a relative equivalence from `X`
> to `Y` over `S`*.
>
> Explicitly: `K` is a perfect object of `D(𝒪_{X ×_S Y})`, and there is a perfect object `K'` of
> `D(𝒪_{Y ×_S X})` such that the two convolutions of [Stacks, Tag 0FYS],
>
> `R pr_{13,*}(L pr_{12}^*K ⊗^𝐋 L pr_{23}^*K')` on `X ×_S X` and
> `R pr_{13,*}(L pr_{12}^*K' ⊗^𝐋 L pr_{23}^*K)` on `Y ×_S Y`,
>
> are isomorphic to the diagonal kernels `Δ_{X/S,*}𝒪_X` and `Δ_{Y/S,*}𝒪_Y` of
> [Stacks, Tag 0FYV] respectively. In other words the isomorphism class of `K` is an invertible
> arrow of the category of the source's Section 0G0F.
>
> The source states this for smooth proper `f` and `g`; those hypotheses are not used by the
> definition and are not imposed here, so this is a generalization — see the module docstring.

```lean
def IsRelativeEquivalenceKernel (K : DerivedCategory (Limits.pullback f g).Modules) : Prop
```

## Tag 0G0J, a lemma

[Tag 0G0J](https://stacks.math.columbia.edu/tag/0G0J) in the Stacks Project.

**`AlgebraicGeometry.isEquivalence_quasiCoherentFourierMukai_of_isRelativeEquivalenceKernel`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceEquivalences.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceEquivalences.lean#L116). The attribute's comment: “Phi_K : D_QCoh(O_X) -> D_QCoh(O_Y) is an equivalence”.

> **[Stacks, Tag 0G0J], the clause for `D_QCoh`.** Let `S` be a scheme, let `f : X ⟶ S` and
> `g : Y ⟶ S` be smooth and proper, and let `K` be the Fourier-Mukai kernel of a relative
> equivalence from `X` to `Y` over `S`, [Stacks, Tag 0G0I]. Then the Fourier-Mukai functor
> `Φ_K : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` of [Stacks, Tag 0FYR] is an equivalence.
>
> Its inverse is `Φ_{K'}` for the kernel `K'` that the definition of a relative equivalence
> supplies: by [Stacks, Tag 0FYS] the two composites are the Fourier-Mukai functors of the two
> convolutions, which the definition identifies with the diagonal kernels, whose Fourier-Mukai
> functors are the identities by [Stacks, Tag 0FYV]. This is another name for
> `AlgebraicGeometry.isEquivalence_quasiCoherentFourierMukai`.

```lean
public alias isEquivalence_quasiCoherentFourierMukai_of_isRelativeEquivalenceKernel
```

**`AlgebraicGeometry.isEquivalence_perfectFourierMukai_of_isRelativeEquivalenceKernel`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceEquivalences.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceEquivalences.lean#L130). The attribute's comment: “Phi_K : D_perf(O_X) -> D_perf(O_Y) is an equivalence”.

> **[Stacks, Tag 0G0J], the clause for `D_perf`.** Let `S` be a scheme, let `f : X ⟶ S` and
> `g : Y ⟶ S` be smooth and proper, and let `K` be the Fourier-Mukai kernel of a relative
> equivalence from `X` to `Y` over `S`, [Stacks, Tag 0G0I]. Then the Fourier-Mukai functor
> `Φ_K : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)` of [Stacks, Tag 0FYT] is an equivalence.
>
> The functor exists by clause (3) of [Stacks, Tag 0FYT], `f` being proper, flat and of finite
> presentation and `K` perfect. Its inverse is `Φ_{K'}`, as in the `D_QCoh` clause
> `AlgebraicGeometry.isEquivalence_quasiCoherentFourierMukai_of_isRelativeEquivalenceKernel`,
> whose two composite isomorphisms restrict to `D_perf(𝒪_X) ⊆ D_QCoh(𝒪_X)`. This is another name
> for `AlgebraicGeometry.isEquivalence_perfectFourierMukai`.

```lean
public alias isEquivalence_perfectFourierMukai_of_isRelativeEquivalenceKernel
```

**`AlgebraicGeometry.isEquivalence_quasiCoherentFourierMukai`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceIsEquivalence.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceIsEquivalence.lean#L296). The attribute's comment: “Phi_K : D_QCoh(O_X) -> D_QCoh(O_Y) is an equivalence”.

> **[Stacks, Tag 0G0J], the clause for `D_QCoh`.** Let `f : X ⟶ S` and `g : Y ⟶ S` be smooth
> and proper and let `K` be the Fourier-Mukai kernel of a relative equivalence from `X` to `Y` over
> `S`, [Stacks, Tag 0G0I]. Then the Fourier-Mukai functor
> `Φ_K : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` of [Stacks, Tag 0FYR] is an equivalence.
>
> The inverse is `Φ_{K'}` for the kernel `K'` the definition of a relative equivalence supplies:
> its two composites with `Φ_K` are, by [Stacks, Tag 0FYS], the Fourier-Mukai functors of the two
> convolutions, which the definition identifies with the diagonal kernels, whose Fourier-Mukai
> functors are the identities. [Stacks, Tag 0FYS] is used through
> `AlgebraicGeometry.quasiCoherentFourierMukaiComp`, whose two inputs [Stacks, Tag 08IB] and
> [Stacks, Tag 08EU] are the theorems `AlgebraicGeometry.derivedBaseChangeIsIsoOnQuasicoherent` and
> `AlgebraicGeometry.projectionFormulaIsIsoOnQuasicoherent`; the clause of [Stacks, Tag 0FYV] that
> `Φ_{𝒪_Δ}` is the identity is `AlgebraicGeometry.fourierMukaiDiagonalKernelIso`.

```lean
theorem isEquivalence_quasiCoherentFourierMukai
    [Smooth f] [Smooth g] [IsProper f] [IsProper g]
    {K : DerivedCategory (Limits.pullback f g).Modules}
    (hK : IsRelativeEquivalenceKernel f g K) :
    (quasiCoherentFourierMukai f g K
      (isQuasicoherent_homology_of_isRelativeEquivalenceKernel f g hK)).IsEquivalence
```

**`AlgebraicGeometry.isEquivalence_perfectFourierMukai`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceIsEquivalence.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceIsEquivalence.lean#L325). The attribute's comment: “Phi_K : D_perf(O_X) -> D_perf(O_Y) is an equivalence”.

> **[Stacks, Tag 0G0J], the clause for `D_perf`.** Let `f : X ⟶ S` and `g : Y ⟶ S` be smooth
> and proper and let `K` be the Fourier-Mukai kernel of a relative equivalence from `X` to `Y` over
> `S`, [Stacks, Tag 0G0I]. Then the Fourier-Mukai functor
> `Φ_K : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)` of [Stacks, Tag 0FYT] is an equivalence.
>
> A perfect complex has quasi-coherent cohomology, so `D_perf(𝒪_X)` is a full subcategory of
> `D_QCoh(𝒪_X)` on which the two functors agree with their quasi-coherent counterparts. The two
> composite isomorphisms of the quasi-coherent clause therefore whisker down to `D_perf`, and the
> fully faithful inclusion of `D_perf(𝒪_X)` into `D(𝒪_X)` may be cancelled. What makes the two
> functors on `D_perf` exist at all is clause (3) of [Stacks, Tag 0FYT], the theorem
> `AlgebraicGeometry.isPerfect_fourierMukai_of_isPerfect_kernel_of_properFlatFinitePresentation`,
> appealed to inside `AlgebraicGeometry.perfectFourierMukai`.

```lean
theorem isEquivalence_perfectFourierMukai
    [Smooth f] [Smooth g] [IsProper f] [IsProper g]
    {K : DerivedCategory (Limits.pullback f g).Modules}
    (hK : IsRelativeEquivalenceKernel f g K) :
    (perfectFourierMukai f g K hK.1).IsEquivalence
```

## Tag 0G0K, a lemma

[Tag 0G0K](https://stacks.math.columbia.edu/tag/0G0K) in the Stacks Project.

**`AlgebraicGeometry.isRelativeEquivalenceKernel_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceBaseChange.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceBaseChange.lean#L428). The attribute's comment: “stability of relative-equivalence kernels under an ARBITRARY base change S1 -> S; f and g are only flat, separated and qcqs, all implied by the source's ambient smooth proper hypotheses. GRANTED: h08IB, the conclusion of Tag 08IB, which this tree lacks (it has the map of Tag 08HY and the affine input, not the globalization Tag 0DJ9) -- the same carry Tag 0FYS makes. All else (Tag 0CTA, Tag 09UA, flatness of pr13, Lp^*O_X[0] iso O_X1[0]) is proved here”.

> **[Stacks, Tag 0G0K]: a relative equivalence is stable under base change.** Let `f : X ⟶ S`
> and `g : Y ⟶ S` and let `K` be the Fourier-Mukai kernel of a relative equivalence from `X` to
> `Y` over `S` ([Stacks, Tag 0G0I]). Let `s : S₁ ⟶ S` be *any* morphism of schemes, and write
> `X₁ = X ×_S S₁` and `Y₁ = Y ×_S S₁` with their projections to `S₁`. Then
>
> `K₁ = L(X₁ ×_{S₁} Y₁ ⟶ X ×_S Y)^* K`
>
> is the Fourier-Mukai kernel of a relative equivalence from `X₁` to `Y₁` over `S₁`.
>
> The proof is the source's. Take the partner `K'` of `K` and pull it back to `K'₁` along
> `Y₁ ×_{S₁} X₁ ⟶ Y ×_S X`. The square carrying `pr₁₃` on `X₁ ×_{S₁} Y₁ ×_{S₁} X₁` to `pr₁₃` on
> `X ×_S Y ×_S X` is cartesian, and `pr₁₃` is flat because `g` is, so derived base change
> ([Stacks, Tag 08IB], granted) identifies `L^*` of the convolution with the convolution of the
> pulled back kernels — the monoidality of derived pullback ([Stacks, Tag 079U]) and the
> composition isomorphism ([Stacks, Tag 0D5S]) being what turn the pullback of
> `L pr_{12}^*K ⊗^𝐋 L pr_{23}^*K'` into `L pr_{12}^*K₁ ⊗^𝐋 L pr_{23}^*K'₁`. On the other side the
> square carrying `Δ_{X₁/S₁}` to `Δ_{X/S}` is cartesian, `X₁ ×_{S₁} X₁` and `X` are Tor
> independent over `X ×_S X` by [Stacks, Tag 0CTA] (which is where flatness of `f` is used), and
> `L^*𝒪_X[0] ≅ 𝒪_{X₁}[0]` because `𝒪_X` is flat; so `L^*` of the diagonal kernel is the diagonal
> kernel. Perfectness transports by [Stacks, Tag 09UA].
>
> Where the source uses smooth proper `f` and `g`, only flatness, separatedness and
> quasi-compactness/quasi-separatedness are used here, so the hypotheses are weaker than the
> source's; and `s` is arbitrary, as the source demands. The one granted input is `h08IB`.

```lean
theorem isRelativeEquivalenceKernel_derivedPullback
    (h08IB : DerivedBaseChangeIsIsoOnQuasicoherent.{u})
    {S X Y S₁ : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S) (s : S₁ ⟶ S)
    [IsSeparated f] [IsSeparated g] [Flat f] [Flat g]
    [QuasiCompact f] [QuasiSeparated f] [QuasiCompact g] [QuasiSeparated g]
    {K : DerivedCategory (pullback f g).Modules}
    (hK : IsRelativeEquivalenceKernel f g K) :
    IsRelativeEquivalenceKernel (pullback.snd f s) (pullback.snd g s)
      ((derivedPullback (fourierMukaiBaseChangeMap f g s).toLRSHom.toShHom).obj K)
```

**`AlgebraicGeometry.isRelativeEquivalenceKernel_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceBaseChangeDischarged.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceBaseChangeDischarged.lean#L71). The attribute's comment: “the whole lemma, for an arbitrary base change S1 -> S; f and g need only be flat, separated and qcqs, all implied by the source's smooth proper hypotheses. Tag 08IB enters through AlgebraicGeometry.derivedBaseChangeIsIsoOnQuasicoherent, which proves it”.

> **[Stacks, Tag 0G0K]: a relative equivalence is stable under base change.** Let `f : X ⟶ S`
> and `g : Y ⟶ S` be flat, separated, quasi-compact and quasi-separated (for instance smooth and
> proper, as in the source), and let `K` be the Fourier-Mukai kernel of a relative equivalence
> from `X` to `Y` over `S` ([Stacks, Tag 0G0I]). Let `s : S₁ ⟶ S` be any morphism of schemes, and
> write `X₁ = X ×_S S₁` and `Y₁ = Y ×_S S₁` with their projections to `S₁`. Then
>
> `K₁ = L(X₁ ×_{S₁} Y₁ ⟶ X ×_S Y)^* K`
>
> is the Fourier-Mukai kernel of a relative equivalence from `X₁` to `Y₁` over `S₁`.
>
> This is `AlgebraicGeometry.isRelativeEquivalenceKernel_derivedPullback` at
> `AlgebraicGeometry.derivedBaseChangeIsIsoOnQuasicoherent`, which is [Stacks, Tag 08IB].

```lean
theorem isRelativeEquivalenceKernel_baseChange
    {S X Y S₁ : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S) (s : S₁ ⟶ S)
    [IsSeparated f] [IsSeparated g] [Flat f] [Flat g]
    [QuasiCompact f] [QuasiSeparated f] [QuasiCompact g] [QuasiSeparated g]
    {K : DerivedCategory (pullback f g).Modules}
    (hK : IsRelativeEquivalenceKernel f g K) :
    IsRelativeEquivalenceKernel (pullback.snd f s) (pullback.snd g s)
      ((derivedPullback (fourierMukaiBaseChangeMap f g s).toLRSHom.toShHom).obj K)
```

## Tag 0G0L, a lemma

[Tag 0G0L](https://stacks.math.columbia.edu/tag/0G0L) in the Stacks Project.

**`AlgebraicGeometry.exists_isRelativeEquivalenceKernel_of_descentSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceLimit.lean, line 552](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceLimit.lean#L552). The attribute's comment: “the existence of a relative-equivalence kernel at SOME stage i >= 0 of a directed inverse system of qcqs schemes with affine transitions, given one over the limit. GRANTED, each an input the source's own proof cites and this tree lacks in applicable form: h09RFobj and h09RFiso, the two halves of Tag 09RF read along the tower of fibre products (the tree has only the coherent cocone); hbc, the two base-change isomorphisms established inside the proof of Tag 0G0K but private there (RelativeEquivalenceBaseChange.lean:404 and :427, exported only in the opposite direction as :518); hperf, perfectness of the diagonal kernel (Tag 0FDP with Tag 0B6G, whose tree form the proper direct image theorem grants its own Tor-dimension input) and of the convolution kernel (Tag 0B91, whose tree form StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPushforwardBaseChange.lean:263 proves only the base-change half in tensor form). No hypothesis mentions relative equivalences, so nothing of the conclusion is assumed; the affineness of the transitions and the qcqs hypothesis on every stage enter through DescentSituation, and smoothness and properness of X_0 -> S_0 and Y_0 -> S_0 are instance hypotheses”.

> **[Stacks, Tag 0G0L]: a relative equivalence over a limit of schemes comes from a finite
> stage.** Let `S = lim S_i` be the limit of a directed inverse system of quasi-compact and
> quasi-separated schemes with affine transition morphisms, with a chosen index `0`, let
> `X_0 ⟶ S_0` and `Y_0 ⟶ S_0` be smooth and proper, and put `X_i = X_0 ×_{S_0} S_i`,
> `X = X_0 ×_{S_0} S` and likewise for `Y_0`. If `K` is the Fourier-Mukai kernel of a relative
> equivalence from `X` to `Y` over `S`, then for some `i ≥ 0` there is a Fourier-Mukai kernel of a
> relative equivalence from `X_i` to `Y_i` over `S_i`.
>
> The proof is the source's. The kernel `K` and its partner `K'` descend to perfect objects `K_i`
> and `K'_i` at a common stage `i` by [Stacks, Tag 09RF]; both displayed isomorphisms of
> [Stacks, Tag 0G0I] then hold over the limit for the derived pullbacks of `K_i` and `K'_i`, since
> the diagonal kernel and the convolution kernel commute with base change, so by
> [Stacks, Tag 09RF] again the first of them already holds at some stage `j ≥ i`, and, after
> transporting `K_i` and `K'_i` to `j`, the second at some stage `k ≥ j`. Transporting the first
> isomorphism from `j` to `k` puts both at the stage `k`.

```lean
theorem exists_isRelativeEquivalenceKernel_of_descentSituation
    (h09RFobj : PerfectDescendsAlongBaseChangedTower.{v, u})
    (h09RFiso : PerfectIsoDescendsAlongBaseChangedTower.{v, u})
    (hbc : DiagonalKernelAndConvolutionBaseChange.{u})
    (hperf : DiagonalKernelAndConvolutionPerfect.{u})
    {X₀ Y₀ : Scheme.{u}} (x : X₀ ⟶ D.stage D.base) (y : Y₀ ⟶ D.stage D.base)
    [Smooth x] [IsProper x] [Smooth y] [IsProper y]
    {K : DerivedCategory (pullback (pullback.snd x (D.projection D.base))
      (pullback.snd y (D.projection D.base))).Modules}
    (hK : IsRelativeEquivalenceKernel (pullback.snd x (D.projection D.base))
      (pullback.snd y (D.projection D.base)) K) :
    ∃ (i : I) (hi : D.base ≤ i) (Ki : DerivedCategory (pullback
      (pullback.snd x (D.transition hi)) (pullback.snd y (D.transition hi))).Modules),
      IsRelativeEquivalenceKernel (pullback.snd x (D.transition hi))
        (pullback.snd y (D.transition hi)) Ki
```

**`AlgebraicGeometry.exists_isRelativeEquivalenceKernel_of_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceLimitDescent.lean, line 746](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RelativeEquivalenceLimitDescent.lean#L746).

> **[Stacks, Tag 0G0L]: a relative equivalence over a limit of schemes comes from a finite
> stage.** Let `S = lim S_i` be the limit of a directed inverse system of quasi-compact and
> quasi-separated schemes with affine transition morphisms, with a chosen index `0`, let
> `X_0 ⟶ S_0` and `Y_0 ⟶ S_0` be smooth and proper, and put `X_i = X_0 ×_{S_0} S_i`,
> `X = X_0 ×_{S_0} S` and likewise for `Y_0`. If `K` is the Fourier-Mukai kernel of a relative
> equivalence from `X` to `Y` over `S`, then for some `i ≥ 0` there is a Fourier-Mukai kernel of a
> relative equivalence from `X_i` to `Y_i` over `S_i`.
>
> The proof is the source's, performed by
> `AlgebraicGeometry.exists_isRelativeEquivalenceKernel_of_descentSituation`: the kernel and its
> partner descend to a stage by [Stacks, Tag 09RF]
> (`AlgebraicGeometry.perfectDescendsAlongBaseChangedTower`), the diagonal kernel and the
> convolution kernel commute with base change ([Stacks, Tag 08IB], [Stacks, Tag 0CTA]:
> `AlgebraicGeometry.diagonalKernelAndConvolutionBaseChange`) and are perfect
> (`AlgebraicGeometry.diagonalKernelAndConvolutionPerfect`), and the two displayed isomorphisms of
> [Stacks, Tag 0G0I] descend to a later stage by [Stacks, Tag 09RF] again
> (`AlgebraicGeometry.perfectIsoDescendsAlongBaseChangedTower`).
>
> The source writes `X_i = S_i ×_{S_0} X_0`; the base change is taken here on the other side,
> which differs by the symmetry of the fibre product.

```lean
theorem exists_isRelativeEquivalenceKernel_of_limit {I : Type u} [Preorder I]
    [IsDirected I (· ≤ ·)] (D : DescentSituation.{u, u} I)
    {X₀ Y₀ : Scheme.{u}} (x : X₀ ⟶ D.stage D.base) (y : Y₀ ⟶ D.stage D.base)
    [Smooth x] [IsProper x] [Smooth y] [IsProper y]
    {K : DerivedCategory (pullback (pullback.snd x (D.projection D.base))
      (pullback.snd y (D.projection D.base))).Modules}
    (hK : IsRelativeEquivalenceKernel (pullback.snd x (D.projection D.base))
      (pullback.snd y (D.projection D.base)) K) :
    ∃ (i : I) (hi : D.base ≤ i) (Ki : DerivedCategory (pullback
      (pullback.snd x (D.transition hi)) (pullback.snd y (D.transition hi))).Modules),
      IsRelativeEquivalenceKernel (pullback.snd x (D.transition hi))
        (pullback.snd y (D.transition hi)) Ki
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.15, Tag 0G0H](https://stacks.math.columbia.edu/tag/0G0H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
