---
declaration: section
origin: cited
lean: Deformation.Examples.bijective_adicCompletionMap_henselizedLocalRing, Deformation.Examples.bijective_adicCompletion_iInf_to_pi_completedLocalRing, Deformation.Examples.exists_ringEquiv_henselization_iInf_pi_henselizedLocalRing, Deformation.Examples.isSmooth_piCompletedLocalRingFunctor, Deformation.Examples.bijective_differential_piCompletedLocalRingFunctor, Deformation.Examples.bijective_differential_localizationFunctors, Deformation.Examples.isSmooth_localizationFunctors, Deformation.Examples.isSmooth_henselizationFunctors
statement: formalized
proof: formalized
---

# 93.15 Application to isolated singularities

Section 93.15 of the Stacks Project, [Tag 0DZE](https://stacks.math.columbia.edu/tag/0DZE). 1 tag here is carried by 13 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DZF, a lemma

[Tag 0DZF](https://stacks.math.columbia.edu/tag/0DZF) in the Stacks Project.

**`Deformation.Examples.bijective_adicCompletionMap_henselizedLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularities.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularities.lean#L157). The attribute's comment: “the identification of the last term of the chain: the completion of the henselization of the local ring is the completion of the local ring, which the source records as the parenthetical `the completion of the henselization is the completion`. Stated with no hypothesis at all beyond a commutative ring and a prime of it, so in particular without the tag's finite type and smooth-away-from-the-maximal-ideals hypotheses, which this step of the proof does not use”.

> **Stacks 0DZF.** The completion of the local ring `P_𝔪` is the completion of its
> henselization `P^h_𝔪`: the canonical map induced by `P_𝔪 → P^h_𝔪` on adic completions is
> bijective.
>
> This is the identification of the final term `∏ Def_{P^∧_{𝔪 i}}` of the chain of Stacks 0DZF,
> whose functor out of `∏ Def_{P^h_{𝔪 i}}` is completion of the henselization; the source records
> it as the parenthetical remark that "the completion of the henselization is the completion".

```lean
public theorem bijective_adicCompletionMap_henselizedLocalRing
    {P : Type w} [CommRing P] (q : PrimeSpectrum P) :
    Function.Bijective
      (adicCompletionMap (algebraMap (localRingAt q) (henselizedLocalRingAt q))
        (IsLocalRing.maximalIdeal (localRingAt q)) (henselizedMaximalIdealAt q) le_rfl)
```

**`Deformation.Examples.bijective_adicCompletion_iInf_to_pi_completedLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularities.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularities.lean#L201). The attribute's comment: “the decomposition of the completion used by the proof: the completion of `P` along the intersection of the maximal ideals `𝔪 1, ..., 𝔪 n` is the product of the completions of the local rings `P_{𝔪 i}`, which the source states as `P^ = ∏ P_{𝔪 i}^`. Under the tag's own hypotheses on the family: the `𝔪 i` are maximal and distinct. Finite type of `P` and smoothness away from the `𝔪 i` are not used by this step and are not assumed”. References: EGA IV (18.6.7), “more general”.

> **Stacks 0DZF.** The completion of `P` along `J = 𝔪 1 ∩ … ∩ 𝔪 n` is the product of the
> completions of the local rings `P_{𝔪 i}`. This is the step the source states as "`P^∧` is
> `∏ P^∧_{𝔪 i}`", and it is what carries the completion leg of the chain from the finite type
> algebra `P` to the family of its local rings.
>
> The map is the product of the canonical maps `P^∧_J → (P_{𝔪 i})^∧`; the proof is the Chinese
> remainder theorem on the levels `P / Jⁿ ≅ ∏ P / 𝔪 iⁿ`, by
> `Stacks.AdicCompletion.bijective_adicCompletion_iInf_to_pi`, followed by the identification of
> each `𝔪 i`-adic completion of `P` with the completion of `P_{𝔪 i}`, by
> `Stacks.AdicCompletion.bijective_adicCompletionMap_localization_atPrime`.

```lean
public theorem bijective_adicCompletion_iInf_to_pi_completedLocalRing
    {P : Type w} [CommRing P] {ι : Type uι} [Finite ι] (m : ι → PrimeSpectrum P)
    (hmax : ∀ i, (m i).asIdeal.IsMaximal) (hinj : Function.Injective m) :
    Function.Bijective (RingHom.pi fun i =>
      adicCompletionMap (algebraMap P (localRingAt (m i))) (⨅ j, (m j).asIdeal)
        (IsLocalRing.maximalIdeal (localRingAt (m i)))
        ((Ideal.map_mono (iInf_le (fun j => (m j).asIdeal) i)).trans_eq
          (IsLocalization.AtPrime.map_eq_maximalIdeal (m i).asIdeal (localRingAt (m i)))))
```

**`Deformation.Examples.exists_ringEquiv_henselization_iInf_pi_henselizedLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularities.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularities.lean#L264). The attribute's comment: “the decomposition of the henselization used by the proof: the henselization of the pair `(P, J)` for `J` the intersection of the maximal ideals `𝔪 1, ..., 𝔪 n` is the product of the henselizations `P^h_{𝔪 i}` of the local rings, which the source states as `P^h = ∏ P^h_{𝔪 i}`. Under the tag's own hypotheses on the family: the `𝔪 i` are maximal and distinct. Finite type of `P` and smoothness away from the `𝔪 i` are not used by this step and are not assumed”.

> **Stacks 0DZF.** The henselization of the pair `(P, J)` for `J = 𝔪 1 ∩ … ∩ 𝔪 n` is the
> product of the henselizations `P^h_{𝔪 i}` of the local rings. This is the step the source
> states as "`P^h = ∏ P^h_{𝔪 i}`", proved there by looking at idempotents together with More on
> Algebra, Lemma 15.11.6; it is what carries the henselization leg of the chain from the finite
> type algebra `P` to the family of its local rings.

```lean
public theorem exists_ringEquiv_henselization_iInf_pi_henselizedLocalRing
    {P : Type w} [CommRing P] {ι : Type uι} [Finite ι] (m : ι → PrimeSpectrum P)
    (hmax : ∀ i, (m i).asIdeal.IsMaximal) (hinj : Function.Injective m) :
    ∃ e : (henselization P (⨅ i, (m i).asIdeal) : Type w) ≃+*
        (∀ i, henselizedLocalRingAt (m i)),
      ∀ (r : P) (i : ι),
        e (algebraMap P (henselization P (⨅ j, (m j).asIdeal) : Type w) r) i =
          algebraMap (localRingAt (m i)) (henselizedLocalRingAt (m i))
            (algebraMap P (localRingAt (m i)) r)
```

**`Deformation.Examples.isSmooth_piCompletedLocalRingFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularities.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularities.lean#L421). The attribute's comment: “the smoothness half of the source's second step: the composite `Def_P -> ∏ Def_{P^∧_{𝔪 i}}` of all three maps of the chain is smooth, which the source obtains from Stacks 0DZ5 at `P` with `J = 𝔪 1 ∩ ... ∩ 𝔪 n` followed by the decomposition `P^∧ = ∏ P^∧_{𝔪 i}`. The product of deformation categories is read here as the deformation category of the product ring `∏ P^∧_{𝔪 i}`; the identification of that with the product of the deformation categories of the factors is `Deformation.Examples.piDeformationFunctor_full` and `Deformation.Examples.piDeformationFunctor_faithful`, and the clause of the tag for the third map of the chain itself is `Deformation.Examples.isSmooth_completedLocalRingFunctors`. Hypotheses: the tag's own, namely `P` of finite type over `k`, the `𝔪 i` maximal and distinct, and `hsm`, smoothness away from `V(J)` -- which the tag's `smooth except at 𝔪 1, ..., 𝔪 n` supplies, since every prime not containing `J` is none of the `𝔪 i`”.

> **Stacks 0DZF, smoothness of the composite of the chain.** The map
> `𝓓_P → ∏ 𝓓_{P^∧_{𝔪 i}}` is smooth.
>
> This is the source's second step, in its own order: **Stacks 0DZ5** applied to `P` itself with
> `J = 𝔪 1 ∩ … ∩ 𝔪 n` — for which `P` really is of finite type over `k` — gives smoothness of
> `𝓓_P → 𝓓_{P^∧_J}`, and the transport of
> `Deformation.Examples.isSmooth_ringDeformationTransport` along
> `Deformation.Examples.adicCompletionIInfPiEquiv` carries it to the decomposed target.

```lean
public theorem isSmooth_piCompletedLocalRingFunctor [Algebra.FiniteType k P]
    (hsm : ∀ q : PrimeSpectrum P, ¬ (⨅ j, (m j).asIdeal) ≤ q.asIdeal →
      Algebra.IsSmoothAt k q.asIdeal) :
    IsSmooth (piCompletedLocalRingFunctor (Λ := Λ) (k := k) m hmax hinj)
```

**`Deformation.Examples.bijective_differential_piCompletedLocalRingFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularities.lean, line 445](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularities.lean#L445). The attribute's comment: “the tangent-space half of the source's second step: the composite `Def_P -> ∏ Def_{P^∧_{𝔪 i}}` of all three maps of the chain induces an isomorphism on tangent spaces, which the source obtains from Stacks 0DZ5 at `P` with `J = 𝔪 1 ∩ ... ∩ 𝔪 n` followed by the decomposition `P^∧ = ∏ P^∧_{𝔪 i}`. As for smoothness, the product of deformation categories is read as the deformation category of the product ring, the identification of the two being `Deformation.Examples.piDeformationFunctor_full` and `Deformation.Examples.piDeformationFunctor_faithful`; the clause of the tag for the third map of the chain itself is `Deformation.Examples.bijective_differential_completedLocalRingFunctors`. Hypotheses: the tag's own”.

> **Stacks 0DZF, the tangent-space conclusion for the composite of the chain.** The map
> `𝓓_P → ∏ 𝓓_{P^∧_{𝔪 i}}` induces an isomorphism on tangent spaces.
>
> Same route as `Deformation.Examples.isSmooth_piCompletedLocalRingFunctor`: the tangent-space
> half of **Stacks 0DZ5** at `(P, J)`, carried along the decomposition by
> `Deformation.Examples.bijective_differential_ringDeformationTransport`.

```lean
public theorem bijective_differential_piCompletedLocalRingFunctor [Algebra.FiniteType k P]
    (hsm : ∀ q : PrimeSpectrum P, ¬ (⨅ j, (m j).asIdeal) ≤ q.asIdeal →
      Algebra.IsSmoothAt k q.asIdeal) :
    Function.Bijective (differential
      (isCofiberedInGroupoids_ringDeformationProjection (Λ := Λ) (k := k) (P := P))
      (isCofiberedInGroupoids_ringDeformationProjection (Λ := Λ) (k := k)
        (P := ∀ i, AdicCompletion (IsLocalRing.maximalIdeal (localRingAt (m i)))
          (localRingAt (m i))))
      (piCompletedLocalRingFunctor (Λ := Λ) (k := k) m hmax hinj))
```

**`Deformation.Examples.bijective_differential_localizationFunctors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean, line 1235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean#L1235). The attribute's comment: “clause 2 of seven: the first map of the chain, `Def_P -> ∏ Def_{P_{𝔪 i}}`, induces an isomorphism on tangent spaces. Under the tag's own hypotheses and no others: `P` of finite type over `k`, the `𝔪 i` maximal and pairwise distinct, and every prime at which `P` is not smooth one of the `𝔪 i`. The product of deformation categories is the product over `𝒞_Λ`, which is the reading the proof of Stacks 0DZN records. The index type is required to live in the universe of `P`; any finite family can be reindexed into it”.

> **Stacks 0DZF, clause 2.** The first map `Def_P → ∏ Def_{P_{𝔪 i}}` of the chain induces an
> isomorphism on tangent spaces.

```lean
public theorem bijective_differential_localizationFunctors [Algebra.FiniteType k P] :
    Function.Bijective (differential
      (isCofiberedInGroupoids_ringDeformationProjection (Λ := Λ) (k := k) (P := P))
      (isCofiberedInGroupoids_pi_ringDeformation (Λ := Λ) (k := k) fun i => localRingAt (m i))
      (localizationFunctors (Λ := Λ) (k := k) m))
```

**`Deformation.Examples.isSmooth_localizationFunctors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean, line 1253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean#L1253). The attribute's comment: “clause 1 of seven: the first map of the chain, `Def_P -> ∏ Def_{P_{𝔪 i}}`, is smooth. Under the tag's own hypotheses and no others. Obtained from the criterion of Stacks 0DYP: its differential is surjective by clause 2, and a deformation of `P` lifts along a small extension whenever its image under the composite of the first two maps does, which is smoothness of that composite”.

> **Stacks 0DZF, clause 1.** The first map `Def_P → ∏ Def_{P_{𝔪 i}}` of the chain is smooth.

```lean
public theorem isSmooth_localizationFunctors [Algebra.FiniteType k P] :
    IsSmooth (localizationFunctors (Λ := Λ) (k := k) m)
```

**`Deformation.Examples.isSmooth_henselizationFunctors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean, line 1268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean#L1268). The attribute's comment: “clause 3 of seven: the second map of the chain, `∏ Def_{P_{𝔪 i}} -> ∏ Def_{P^h_{𝔪 i}}`, is smooth. Under the tag's own hypotheses and no others. Obtained by cancelling the first map out of the composite of the first two: the first map is smooth by clause 1, hence essentially surjective”.

> **Stacks 0DZF, clause 3.** The second map `∏ Def_{P_{𝔪 i}} → ∏ Def_{P^h_{𝔪 i}}` of the chain
> is smooth.

```lean
public theorem isSmooth_henselizationFunctors [Algebra.FiniteType k P] :
    IsSmooth (henselizationFunctors (Λ := Λ) (k := k) m)
```

**`Deformation.Examples.bijective_differential_henselizationFunctors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean, line 1281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean#L1281). The attribute's comment: “clause 4 of seven: the second map of the chain, `∏ Def_{P_{𝔪 i}} -> ∏ Def_{P^h_{𝔪 i}}`, induces an isomorphism on tangent spaces. Under the tag's own hypotheses and no others. Obtained by cancelling the first map, which is bijective on tangent spaces by clause 2, out of the composite of the first two”.

> **Stacks 0DZF, clause 4.** The second map `∏ Def_{P_{𝔪 i}} → ∏ Def_{P^h_{𝔪 i}}` of the chain
> induces an isomorphism on tangent spaces.

```lean
public theorem bijective_differential_henselizationFunctors [Algebra.FiniteType k P] :
    Function.Bijective (differential
      (isCofiberedInGroupoids_pi_ringDeformation (Λ := Λ) (k := k) fun i => localRingAt (m i))
      (isCofiberedInGroupoids_pi_ringDeformation (Λ := Λ) (k := k)
        fun i => henselizedLocalRingAt (m i))
      (henselizationFunctors (Λ := Λ) (k := k) m))
```

**`Deformation.Examples.isSmooth_completedLocalRingFunctors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean, line 1305](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean#L1305). The attribute's comment: “clause 5 of seven: the third map of the chain, `∏ Def_{P^h_{𝔪 i}} -> ∏ Def_{P^∧_{𝔪 i}}`, is smooth, with the target the tag's own -- the completions of the local rings, not of the henselizations, the two being identified by `Deformation.Examples.bijective_adicCompletionMap_henselizedLocalRing`, which is the source's parenthetical `the completion of the henselization is the completion`. Under the tag's own hypotheses and no others. Obtained by cancelling the composite of the first two maps, which is smooth, out of the composite of all three”.

> **Stacks 0DZF, clause 5.** The third map `∏ Def_{P^h_{𝔪 i}} → ∏ Def_{P^∧_{𝔪 i}}` of the
> chain is smooth. The target is the tag's own: the deformation categories of the completions of
> the *local rings*, which the completions of the henselizations are by
> `Deformation.Examples.bijective_adicCompletionMap_henselizedLocalRing`.

```lean
public theorem isSmooth_completedLocalRingFunctors [Algebra.FiniteType k P] :
    IsSmooth (completedLocalRingFunctors (Λ := Λ) (k := k) m)
```

**`Deformation.Examples.bijective_differential_completedLocalRingFunctors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean, line 1319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean#L1319). The attribute's comment: “clause 6 of seven: the third map of the chain, `∏ Def_{P^h_{𝔪 i}} -> ∏ Def_{P^∧_{𝔪 i}}`, induces an isomorphism on tangent spaces, with the target the tag's own -- the completions of the local rings. Under the tag's own hypotheses and no others. Obtained by cancelling the composite of the first two maps out of the composite of all three”.

> **Stacks 0DZF, clause 6.** The third map `∏ Def_{P^h_{𝔪 i}} → ∏ Def_{P^∧_{𝔪 i}}` of the
> chain induces an isomorphism on tangent spaces.

```lean
public theorem bijective_differential_completedLocalRingFunctors [Algebra.FiniteType k P] :
    Function.Bijective (differential
      (isCofiberedInGroupoids_pi_ringDeformation (Λ := Λ) (k := k)
        fun i => henselizedLocalRingAt (m i))
      (isCofiberedInGroupoids_pi_ringDeformation (Λ := Λ) (k := k) fun i =>
        AdicCompletion (IsLocalRing.maximalIdeal (localRingAt (m i))) (localRingAt (m i)))
      (completedLocalRingFunctors (Λ := Λ) (k := k) m))
```

**`Deformation.Examples.finiteDimensional_artinianTangentSpace_chain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean, line 1343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesChain.lean#L1343). The attribute's comment: “clause 7 of seven: the tangent spaces of all four terms of the chain are finite dimensional over `k`, which is the tag's `finite dimensional tangent spaces`. Under the tag's own hypotheses and no others -- in particular the finiteness of the non-smooth locus that Stacks 0DY4 wants is derived here from the tag's `smooth except at 𝔪 1, ..., 𝔪 n`. The source's tangent space is `Ext¹_P(NL_{P/k}, P)` by Stacks 0DY3; the other three are carried along by clauses 2, 4 and 6, each differential being `k`-linear by Stacks 06IJ”.

> **Stacks 0DZF, clause 7.** All four tangent spaces along the chain are finite dimensional
> over `k`. The source's is `Ext¹_P(NL_{P/k}, P)` by **Stacks 0DY3** and is finite dimensional by
> **Stacks 0DY4(2)**; the other three are carried along by the tangent-space isomorphisms of
> clauses 2, 4 and 6, each of which is `k`-linear by **Stacks 06IJ**.

```lean
public theorem finiteDimensional_artinianTangentSpace_chain
    {ι : Type w} [Finite ι] (m : ι → PrimeSpectrum P) [Algebra.FiniteType k P]
    (hmax : ∀ i, (m i).asIdeal.IsMaximal) (hinj : Function.Injective m)
    (hsm : ∀ q : PrimeSpectrum P, ¬ Algebra.IsSmoothAt k q.asIdeal → ∃ i, m i = q) :
    letI : Fact (IsPredeformationCategory (ringDeformationBasedCategory Λ k P).p) :=
      ⟨(ringDeformationCategory_isDeformationCategory P).predeformation⟩
    letI : Fact (SchlessingerConditionS2 (Functor.Elements.π
      (isomorphismClasses (ringDeformationBasedCategory Λ k P)
        isCofiberedInGroupoids_ringDeformationProjection))) :=
      ⟨schlessingerConditionS2_ringDeformation Λ k P⟩
    letI : Fact (IsPredeformationCategory
        (piBasedCategory fun i => ringDeformationBasedCategory Λ k (localRingAt (m i))).p) :=
      ⟨(isDeformationCategory_pi_ringDeformation (Λ := Λ) (k := k)
        fun i => localRingAt (m i)).predeformation⟩
    letI : Fact (SchlessingerConditionS2 (Functor.Elements.π
      (isomorphismClasses (piBasedCategory fun i =>
          ringDeformationBasedCategory Λ k (localRingAt (m i)))
        (isCofiberedInGroupoids_pi_ringDeformation fun i => localRingAt (m i))))) :=
      ⟨schlessingerConditionS2_pi_ringDeformation (Λ := Λ) (k := k) fun i => localRingAt (m i)⟩
    letI : Fact (IsPredeformationCategory
        (piBasedCategory fun i =>
          ringDeformationBasedCategory Λ k (henselizedLocalRingAt (m i))).p) :=
      ⟨(isDeformationCategory_pi_ringDeformation (Λ := Λ) (k := k)
        fun i => henselizedLocalRingAt (m i)).predeformation⟩
    letI : Fact (SchlessingerConditionS2 (Functor.Elements.π
      (isomorphismClasses (piBasedCategory fun i =>
          ringDeformationBasedCategory Λ k (henselizedLocalRingAt (m i)))
        (isCofiberedInGroupoids_pi_ringDeformation fun i => henselizedLocalRingAt (m i))))) :=
      ⟨schlessingerConditionS2_pi_ringDeformation (Λ := Λ) (k := k)
        fun i => henselizedLocalRingAt (m i)⟩
    letI : Fact (IsPredeformationCategory
        (piBasedCategory fun i => ringDeformationBasedCategory Λ k
          (AdicCompletion (IsLocalRing.maximalIdeal (localRingAt (m i)))
            (localRingAt (m i)))).p) :=
      ⟨(isDeformationCategory_pi_ringDeformation (Λ := Λ) (k := k) fun i =>
        AdicCompletion (IsLocalRing.maximalIdeal (localRingAt (m i)))
          (localRingAt (m i))).predeformation⟩
    letI : Fact (SchlessingerConditionS2 (Functor.Elements.π
      (isomorphismClasses (piBasedCategory fun i => ringDeformationBasedCategory Λ k
          (AdicCompletion (IsLocalRing.maximalIdeal (localRingAt (m i))) (localRingAt (m i))))
        (isCofiberedInGroupoids_pi_ringDeformation fun i =>
          AdicCompletion (IsLocalRing.maximalIdeal (localRingAt (m i)))
            (localRingAt (m i)))))) :=
      ⟨schlessingerConditionS2_pi_ringDeformation (Λ := Λ) (k := k) fun i =>
        AdicCompletion (IsLocalRing.maximalIdeal (localRingAt (m i))) (localRingAt (m i))⟩
    FiniteDimensional k (artinianTangentSpace Λ k
        (isomorphismClasses (ringDeformationBasedCategory Λ k P)
          isCofiberedInGroupoids_ringDeformationProjection)) ∧
      FiniteDimensional k (artinianTangentSpace Λ k
        (isomorphismClasses (piBasedCategory fun i =>
            ringDeformationBasedCategory Λ k (localRingAt (m i)))
          (isCofiberedInGroupoids_pi_ringDeformation fun i => localRingAt (m i)))) ∧
      FiniteDimensional k (artinianTangentSpace Λ k
        (isomorphismClasses (piBasedCategory fun i =>
            ringDeformationBasedCategory Λ k (henselizedLocalRingAt (m i)))
          (isCofiberedInGroupoids_pi_ringDeformation fun i => henselizedLocalRingAt (m i)))) ∧
      FiniteDimensional k (artinianTangentSpace Λ k
        (isomorphismClasses (piBasedCategory fun i => ringDeformationBasedCategory Λ k
            (AdicCompletion (IsLocalRing.maximalIdeal (localRingAt (m i))) (localRingAt (m i))))
          (isCofiberedInGroupoids_pi_ringDeformation fun i =>
            AdicCompletion (IsLocalRing.maximalIdeal (localRingAt (m i)))
              (localRingAt (m i)))))
```

**`Deformation.Examples.nonempty_basedIso_adicCompletionFunctor_completionFunctors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesCompletionComparison.lean, line 666](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularitiesCompletionComparison.lean#L666). The attribute's comment: “the identification the source's proof makes when, after applying Stacks 0DZ5 to `P` itself with `J = 𝔪 1 ∩ ... ∩ 𝔪 n`, it says `P^ = ∏ P^_{𝔪 i}`: completing a deformation along `J` and transporting along a ring isomorphism `P^∧_J ≅ ∏ (P^h_{𝔪 i})^∧` is isomorphic, over `𝒞_Λ`, to localizing at each `𝔪 i`, henselizing, completing, and reading the family as a deformation of the product ring. Hypotheses: the tag's own on the family -- the `𝔪 i` maximal and distinct -- plus `P` of finite type over `k`, and the ring isomorphism together with its description on elements of `P`, which are inputs rather than existentials”.

> **The comparison of Stacks 0DZF for the completion leg.** Completing a deformation of `P`
> along `J = 𝔪 1 ∩ … ∩ 𝔪 n` and then transporting along a ring isomorphism
> `P^∧_J ≅ ∏ (P^h_{𝔪 i})^∧` gives the *same* functor over `𝒞_Λ` as localizing at each `𝔪 i`,
> henselizing, completing each henselized local ring, and reading the resulting family as a
> deformation of the product ring.
>
> This is the step the source of Stacks 0DZF makes when, having applied **Stacks 0DZ5** to `P`
> itself — where the finite type hypothesis genuinely holds — it says "`P^∧ = ∏ P^∧_{𝔪 i}`". The
> ring isomorphism and its description on elements coming from `P` are hypotheses, so a caller may
> supply the one it already has; `Deformation.Examples.adicCompletionPiHenselizedEquiv`,
> `Deformation.Examples.algebraMap_adicCompletionPiHenselizedEquiv` and
> `Deformation.Examples.apply_algebraMap_adicCompletionPiHenselizedEquiv` are such a triple.

```lean
public theorem nonempty_basedIso_adicCompletionFunctor_completionFunctors
    {ι : Type w} [Finite ι] [Algebra.FiniteType k P] [IsNoetherianRing P]
    (m : ι → PrimeSpectrum P) (hmax : ∀ i, (m i).asIdeal.IsMaximal)
    (hinj : Function.Injective m)
    (e : AdicCompletion (⨅ j, (m j).asIdeal) P ≃+*
      (∀ i, AdicCompletion (henselizedMaximalIdealAt (m i)) (henselizedLocalRingAt (m i))))
    (he : ∀ a : k, e (algebraMap k (AdicCompletion (⨅ j, (m j).asIdeal) P) a) =
      algebraMap k (∀ i, AdicCompletion (henselizedMaximalIdealAt (m i))
        (henselizedLocalRingAt (m i))) a)
    (hchar : ∀ (x : P) (i : ι),
      e (algebraMap P (AdicCompletion (⨅ j, (m j).asIdeal) P) x) i =
        algebraMap (henselizedLocalRingAt (m i))
          (AdicCompletion (henselizedMaximalIdealAt (m i)) (henselizedLocalRingAt (m i)))
          (algebraMap (localRingAt (m i)) (henselizedLocalRingAt (m i))
            (algebraMap P (localRingAt (m i)) x))) :
    Nonempty (BasedFunctor.comp
        (adicCompletionFunctor (Λ := Λ) (k := k) P (⨅ j, (m j).asIdeal)).functor
        (ringDeformationTransport e he) ≅
      BasedFunctor.comp (localizationFunctors (Λ := Λ) (k := k) m)
        (BasedFunctor.comp (henselizationFunctors (Λ := Λ) (k := k) m)
          (BasedFunctor.comp (completionFunctors (Λ := Λ) (k := k) m)
            (piDeformationFunctor (Λ := Λ) (k := k) fun i =>
              AdicCompletion (henselizedMaximalIdealAt (m i))
                (henselizedLocalRingAt (m i))))))
```

Declarations registered for the tag:

- [`finiteDimensional_naiveCotangentExtOne`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=finiteDimensional_naiveCotangentExtOne#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularities.lean, line 469](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/IsolatedSingularities.lean#L469) (StacksFrontier): “the finite-dimensionality of the tangent space of the source `Def_P` of the chain, which the source's proof obtains from Stacks 0DY4 and which this declaration carries. The tangent space is the group `Ext¹_P(NL_{P/k}, P)` of Stacks 0DY3. No extra hypothesis: `hfinite` asks only that the non-smooth locus be finite, which 0DZF's own hypothesis -- smooth except at the maximal ideals `𝔪 1, ..., 𝔪 n` -- gives. Finite-dimensionality for all four terms of the chain, which is the tag's own `finite dimensional tangent spaces`, is `Deformation.Examples.finiteDimensional_artinianTangentSpace_chain`”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.15, Tag 0DZE](https://stacks.math.columbia.edu/tag/0DZE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
