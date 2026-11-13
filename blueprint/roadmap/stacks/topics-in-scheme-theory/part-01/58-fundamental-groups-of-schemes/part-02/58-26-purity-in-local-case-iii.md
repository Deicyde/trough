---
declaration: section
origin: cited
lean: Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_restrict_mvPowerSeries, Stacks.FundamentalGroup.isEquivalence_finiteEtaleBaseChange_and_hasPurity_mvPowerSeries, Stacks.FundamentalGroup.isEquivalence_finiteEtaleBaseChange_mvPowerSeries, Stacks.FundamentalGroup.isEquivalence_finiteEtaleBaseChange_of_smooth_of_fibrewise_dense, Stacks.FundamentalGroup.isEquivalence_finiteEtaleBaseChange_of_formallySmoothNAdic_of_depth, Stacks.FundamentalGroup.hasPurity_of_formallySmoothNAdic
statement: formalized
proof: formalized
---

# 58.26 Purity in local case, III

Section 58.26 of the Stacks Project, [Tag 0EY8](https://stacks.math.columbia.edu/tag/0EY8). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EY9, a lemma

[Tag 0EY9](https://stacks.math.columbia.edu/tag/0EY9) in the Stacks Project.

**`Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_restrict_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityPowerSeriesRestriction.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityPowerSeriesRestriction.lean#L139). The attribute's comment: “the full statement under the source's hypotheses; nothing is assumed”.

> Let `(A, 𝔪)` be a Noetherian local ring of depth at least two, let `B = A[[x_1, …, x_d]]`
> with `d ≥ 1`, set `Y = Spec B` and let `Y_0 = V(x_1, …, x_d)` be the closed fibre, the image of the
> closed immersion `Spec A ⟶ Y` induced by the constant coefficient. For any open `V ⊆ Y` with
> `V ∩ Y_0` the punctured spectrum of `A`, the restriction functor `FÉt_V ⟶ FÉt_{V ∩ Y_0}` is fully
> faithful.
>
> The condition on `V` is the hypothesis `hV`: the inverse image of `V` under the closed immersion
> `Spec A ⟶ Y` is the complement of the closed point of `Spec A`.

```lean
public theorem fullyFaithful_finiteEtaleBaseChange_restrict_mvPowerSeries (A : Type u)
    [CommRing A] [IsLocalRing A] [IsNoetherianRing A] (d : ℕ) (hd : 0 < d)
    (hdepth : (2 : ℕ∞) ≤ Module.depth A (IsLocalRing.maximalIdeal A) A)
    (V : (Spec (.of (MvPowerSeries (Fin d) A))).Opens)
    (hV : (Spec.map (CommRingCat.ofHom
        (MvPowerSeries.constantCoeff : MvPowerSeries (Fin d) A →+* A)) ⁻¹ᵁ V :
      Set (Spec (.of A))) = {IsLocalRing.closedPoint A}ᶜ) :
    Nonempty (finiteEtaleBaseChange (Spec.map (CommRingCat.ofHom
      (MvPowerSeries.constantCoeff : MvPowerSeries (Fin d) A →+* A)) ∣_ V)).FullyFaithful
```

## Tag 0EYA, a lemma

[Tag 0EYA](https://stacks.math.columbia.edu/tag/0EYA) in the Stacks Project.

**`Stacks.FundamentalGroup.isEquivalence_finiteEtaleBaseChange_and_hasPurity_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityPowerSeries.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityPowerSeries.lean#L57). The attribute's comment: “the full statement under the tag's hypotheses: for every open `V` containing the primes `𝔮` with `𝔮 ∩ A ≠ 𝔪` and the prime `𝔪B`, the restriction `FÉt_Y ⟶ FÉt_V` is an equivalence, and purity holds for `B`.”. References: SGA 1 XIII (4.7), “special case”.

> **[Stacks, Tag 0EYA]** (Ramanujam--Samuel for finite étale covers). Let `(A, 𝔪)` be a
> Noetherian local ring of depth at least two and let `B = A[[x_1, …, x_d]]` with `d ≥ 1`. Let
> `V ⊆ Y = Spec B` be an open which contains every prime `𝔮` of `B` with `𝔮 ∩ A ≠ 𝔪` (`hV₁`)
> and contains the prime `𝔪B` (`hV₂`). Then the restriction functor `FÉt_Y ⟶ FÉt_V` is an
> equivalence, and purity holds for `B`.
>
> The equivalence is `isEquivalence_finiteEtaleBaseChange_mvPowerSeries` with its two hypotheses
> discharged: the density of `V` by `dense_of_comap_ne_maximalIdeal_mem_of_flat`, `B` being flat
> over `A` ([Stacks, Tag 059T]) and `A` of positive depth, and essential surjectivity by
> `essSurj_finiteEtaleBaseChange_mvPowerSeries`. Purity for `B` is the equivalence for the
> punctured spectrum of `B`, which satisfies both conditions on `V`
> (`mem_puncturedSpectrum_of_comap_ne_maximalIdeal`, `mem_puncturedSpectrum_of_eq_map_maximalIdeal`;
> the latter is where `d ≥ 1` is used).

```lean
public theorem isEquivalence_finiteEtaleBaseChange_and_hasPurity_mvPowerSeries (A : Type u)
    [CommRing A] [IsLocalRing A] [IsNoetherianRing A] (d : ℕ) (hd : 0 < d)
    (hdepth : (2 : ℕ∞) ≤ Module.depth A (maximalIdeal A) A)
    (V : (Spec (.of (MvPowerSeries (Fin d) A))).Opens)
    (hV₁ : ∀ q : PrimeSpectrum (MvPowerSeries (Fin d) A),
      q.asIdeal.comap (MvPowerSeries.C : A →+* MvPowerSeries (Fin d) A) ≠ maximalIdeal A →
        q ∈ V)
    (hV₂ : ∀ q : PrimeSpectrum (MvPowerSeries (Fin d) A),
      q.asIdeal = Ideal.map (MvPowerSeries.C : A →+* MvPowerSeries (Fin d) A)
        (maximalIdeal A) → q ∈ V) :
    (finiteEtaleBaseChange V.ι).IsEquivalence ∧ HasPurity (MvPowerSeries (Fin d) A)
```

**`Stacks.FundamentalGroup.isEquivalence_finiteEtaleBaseChange_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityPowerSeriesEquivalence.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityPowerSeriesEquivalence.lean#L249). The attribute's comment: “the fully faithful half unconditionally: a point of `Spec B` outside `V` lies over `𝔪` by the tag's condition (1), hence its local ring has depth at least two, by flatness of `B` over `A` (Tag 059T) fed to Tag 0337, which is the source's first paragraph; Tag 0BLR through `isConnectedPuncturedStrictHenselization_of_two_le_depth` turns that into the local hypothesis of Tag 0BQF, which gives full faithfulness. Two hypotheses are carried. `hessSurj` is the essential surjectivity half, that is the whole of the source's second paragraph, standing for Tag 0EY6 and Tag 0EY9 together with the step the source itself marks `small detail omitted`. `hdense` is the density of `V` in `Spec B`, which Tag 0BQF requires and which the source does not verify. The tag's condition (2) on `V` and its hypothesis `d ≥ 1` are stated; they are used by the purity corollary `hasPurity_mvPowerSeries` below rather than by the equivalence itself.”.

> **[Stacks, Tag 0EYA]** (Ramanujam--Samuel for finite étale covers). Let `(A, 𝔪)` be a
> Noetherian local ring of depth at least two and let `B = A[[x_1, …, x_d]]` with `d ≥ 1`. Let
> `V ⊆ Y = Spec B` be an open which contains every prime `𝔮` of `B` with `𝔮 ∩ A ≠ 𝔪` and contains
> the prime `𝔪B`. Then the restriction functor `FÉt_Y ⟶ FÉt_V` is an equivalence.
>
> The two conditions on `V` are `hV₁` and `hV₂`. `hV₂` is phrased as a condition on the points of
> `Spec B` rather than on the ideal `𝔪B`, so that the primality of `𝔪B` need not be produced.
>
> The fully faithful half is proved: a point of `Spec B` outside `V` lies over `𝔪` by `hV₁`, so its
> local ring has depth at least two by `two_le_depth_stalk_of_notMem_mvPowerSeries`, which is
> flatness of `B` over `A` ([Stacks, Tag 059T]) fed to [Stacks, Tag 0337];
> `isConnectedPuncturedStrictHenselization_of_two_le_depth` ([Stacks, Tag 0BLR]) turns that into
> the local hypothesis of [Stacks, Tag 0BQF], which concludes. That is the source's first
> paragraph.
>
> Two hypotheses are carried.
>
> * `hdense` is the density of `V` in `Spec B`, which [Stacks, Tag 0BQF] requires and which the
>   source does not verify when it appeals to that tag.
> * `hessSurj` is essential surjectivity, the source's second paragraph: the unique finite
>   extension `Spec C ⟶ Y` of a finite étale `W ⟶ V` from [Stacks, Tag 0EY6], the isomorphism
>   `C ≅ C₀ ⊗_A B` obtained from [Stacks, Tag 0EY9] over `U ×_X Y` through the compatibility of
>   that construction with flat base change and with change of opens, and the deduction that
>   `A ⟶ C₀` is finite étale — a step at which the source itself writes "small detail omitted".

```lean
public theorem isEquivalence_finiteEtaleBaseChange_mvPowerSeries (A : Type u) [CommRing A]
    [IsLocalRing A] [IsNoetherianRing A] (d : ℕ) (hd : 0 < d)
    (hdepth : (2 : ℕ∞) ≤ Module.depth A (maximalIdeal A) A)
    (V : (Spec (.of (MvPowerSeries (Fin d) A))).Opens)
    (hV₁ : ∀ q : PrimeSpectrum (MvPowerSeries (Fin d) A),
      q.asIdeal.comap (MvPowerSeries.C : A →+* MvPowerSeries (Fin d) A) ≠ maximalIdeal A →
        q ∈ V)
    (hV₂ : ∀ q : PrimeSpectrum (MvPowerSeries (Fin d) A),
      q.asIdeal = Ideal.map (MvPowerSeries.C : A →+* MvPowerSeries (Fin d) A)
        (maximalIdeal A) → q ∈ V)
    (hdense : Dense (V : Set (Spec (.of (MvPowerSeries (Fin d) A)))))
    (hessSurj : (finiteEtaleBaseChange V.ι).EssSurj) :
    (finiteEtaleBaseChange V.ι).IsEquivalence
```

## Tag 0EYB, a lemma

[Tag 0EYB](https://stacks.math.columbia.edu/tag/0EYB) in the Stacks Project.

**`Stacks.FundamentalGroup.isEquivalence_finiteEtaleBaseChange_of_smooth_of_fibrewise_dense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PuritySmooth.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PuritySmooth.lean#L97). The attribute's comment: “the full statement under the tag's four hypotheses and nothing else: (1) `Smooth f`, (2) `IsNoetherian S`, (3) `hfib`, the tag's `X_s = U_s` at every `s` with `depth 𝒪_{S, s} ≤ 1`, spelled as containment of the fibre `f⁻¹(s)` in `U`, and (4) `hdense`, the density of `U_s` in `X_s`, spelled as every point of `f⁻¹(s)` lying in the closure of `U ∩ f⁻¹(s)`; the conclusion is that the restriction `finiteEtaleBaseChange U.ι` is an equivalence `FÉt_X ⟶ FÉt_U`.”.

> **[Stacks, Tag 0EYB].** Let `f : X ⟶ S` be a morphism of schemes and `U ⊆ X` an open
> subscheme. Assume that
>
> 1. `f` is smooth,
> 2. `S` is Noetherian,
> 3. for every `s ∈ S` with `depth 𝒪_{S, s} ≤ 1` we have `X_s = U_s`, spelled as containment of
>    the fibre `f⁻¹(s)` in `U` (`hfib`), and
> 4. `U_s ⊆ X_s` is dense for every `s ∈ S`, spelled as every point of `f⁻¹(s)` lying in the
>    closure of `U ∩ f⁻¹(s)` (`hdense`).
>
> Then the restriction functor `FÉt_X ⟶ FÉt_U` is an equivalence of categories.
>
> Full faithfulness is `nonempty_fullyFaithful_finiteEtaleBaseChange_of_smooth` (the source's first
> paragraph, by [Stacks, Tag 0BQF], [Stacks, Tag 0BLR] and [Stacks, Tag 0337]) and essential
> surjectivity is `essSurj_finiteEtaleBaseChange_of_smooth` (the source's second paragraph, by
> [Stacks, Tag 0EY6] and [Stacks, Tag 0EYA]).

```lean
public theorem isEquivalence_finiteEtaleBaseChange_of_smooth_of_fibrewise_dense
    {X S : Scheme.{u}} (f : X ⟶ S) [Smooth f] [IsNoetherian S] (U : X.Opens)
    (hfib : ∀ s : S, Module.depth (S.presheaf.stalk s) (maximalIdeal (S.presheaf.stalk s))
      (S.presheaf.stalk s) ≤ 1 → f.base ⁻¹' {s} ⊆ (U : Set X))
    (hdense : ∀ s : S, f.base ⁻¹' {s} ⊆ closure ((U : Set X) ∩ f.base ⁻¹' {s})) :
    (finiteEtaleBaseChange U.ι).IsEquivalence
```

## Tag 0EYC, a proposition

[Tag 0EYC](https://stacks.math.columbia.edu/tag/0EYC) in the Stacks Project.

**`Stacks.FundamentalGroup.isEquivalence_finiteEtaleBaseChange_of_formallySmoothNAdic_of_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FormallySmoothPurity.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FormallySmoothPurity.lean#L197). The attribute's comment: “the equivalence FÉt\_Y → FÉt\_V for a local homomorphism A → B of Noetherian local rings with depth(A) ≥ 2, formally smooth for the 𝔪\_B-adic topology, with dim(B) > dim(A), and any open V of Spec B containing every prime 𝔮 with 𝔮 ∩ A ≠ 𝔪\_A and the prime 𝔪\_A B; flatness of A → B and essential surjectivity are proved here”. References: SGA 1 XIII (4.7), “special case”.

> **[Stacks, Tag 0EYC]** (Ramanujam--Samuel for finite étale covers). Let `A → B` be a local
> homomorphism of Noetherian local rings. Assume `A` has depth at least two, `A → B` is formally
> smooth for the `𝔪_B`-adic topology, and `dim(B) > dim(A)`. For any open `V ⊆ Y = Spec B` which
> contains every prime `𝔮 ⊆ B` with `𝔮 ∩ A ≠ 𝔪_A` (`hV₁`) and the prime `𝔪_A B` (`hV₂`, phrased as
> a condition on the points of `Spec B`), the restriction functor `FÉt_Y ⟶ FÉt_V` is an
> equivalence.
>
> Full faithfulness is the source's first paragraph,
> `isEquivalence_finiteEtaleBaseChange_of_formallySmoothNAdic`; flatness of `A → B` is
> [Stacks, Tag 07NP]; essential surjectivity is
> `essSurj_finiteEtaleBaseChange_of_formallySmoothNAdic`. The hypothesis `dim(B) > dim(A)` is the
> source's own; it is what makes the punctured spectrum an open as in the tag (see
> `hasPurity_of_formallySmoothNAdic`) and is not needed for the equivalence itself.

```lean
public theorem isEquivalence_finiteEtaleBaseChange_of_formallySmoothNAdic_of_depth
    (A B : Type u) [CommRing A] [CommRing B] [IsLocalRing A] [IsLocalRing B] [IsNoetherianRing A]
    [IsNoetherianRing B] [Algebra A B] [IsLocalHom (algebraMap A B)]
    (hdepth : (2 : ℕ∞) ≤ Module.depth A (maximalIdeal A) A)
    (hsmooth : RingHom.FormallySmoothNAdic.{u} (algebraMap A B) (maximalIdeal B))
    (hdim : ringKrullDim A < ringKrullDim B)
    (V : (Spec (.of B)).Opens)
    (hV₁ : ∀ q : PrimeSpectrum B, q.asIdeal.comap (algebraMap A B) ≠ maximalIdeal A → q ∈ V)
    (hV₂ : ∀ q : PrimeSpectrum B,
      q.asIdeal = Ideal.map (algebraMap A B) (maximalIdeal A) → q ∈ V) :
    (finiteEtaleBaseChange V.ι).IsEquivalence
```

**`Stacks.FundamentalGroup.hasPurity_of_formallySmoothNAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FormallySmoothPurity.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FormallySmoothPurity.lean#L223). The attribute's comment: “the clause 'in particular purity holds for B': every finite étale cover of the punctured spectrum of B extends to Spec B, for A → B as in the tag (Noetherian local, local homomorphism, depth(A) ≥ 2, formally smooth for the 𝔪\_B-adic topology, dim(B) > dim(A))”.

> **[Stacks, Tag 0EYC], "in particular purity holds for `B`".** Let `A → B` be a local
> homomorphism of Noetherian local rings with `depth(A) ≥ 2`, formally smooth for the `𝔪_B`-adic
> topology, with `dim(B) > dim(A)`. Then every finite étale cover of the punctured spectrum of `B`
> extends to a finite étale cover of `Spec B`.
>
> The punctured spectrum is an open as in the tag: condition (1) because the closed point contracts
> to `𝔪_A`, condition (2) because `𝔪_A B ≠ 𝔪_B`, which is where `dim(A) < dim(B)` enters
> (`mem_puncturedSpectrum_of_eq_map_maximalIdeal_of_ringKrullDim_lt`).

```lean
public theorem hasPurity_of_formallySmoothNAdic (A B : Type u) [CommRing A] [CommRing B]
    [IsLocalRing A] [IsLocalRing B] [IsNoetherianRing A] [IsNoetherianRing B] [Algebra A B]
    [IsLocalHom (algebraMap A B)]
    (hdepth : (2 : ℕ∞) ≤ Module.depth A (maximalIdeal A) A)
    (hsmooth : RingHom.FormallySmoothNAdic.{u} (algebraMap A B) (maximalIdeal B))
    (hdim : ringKrullDim A < ringKrullDim B) :
    HasPurity B
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.26, Tag 0EY8](https://stacks.math.columbia.edu/tag/0EY8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
