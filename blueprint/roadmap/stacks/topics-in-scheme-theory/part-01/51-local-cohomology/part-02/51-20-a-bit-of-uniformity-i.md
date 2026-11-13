---
declaration: section
origin: cited
lean: factor_through_free_of_tor_one_map_eq_zero, CategoryTheory.exists_shortExact_pushout, tfae_lift_ext_conditions, canonicalExtClassPullbackVanishes_imp_torMapVanishesAbove, tfae_tor_conditions, tfae_of_isPseudoCoherentFrom, tfae_of_isNoetherianRing_of_finite, Stacks.LocalCohomology.exists_quotientPower_extMapVanishesAbove
statement: formalized
proof: formalized
---

# 51.20 A bit of uniformity, I

Section 51.20 of the Stacks Project, [Tag 0G9S](https://stacks.math.columbia.edu/tag/0G9S). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G9T, a lemma

[Tag 0G9T](https://stacks.math.columbia.edu/tag/0G9T) in the Stacks Project.

**`factor_through_free_of_tor_one_map_eq_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/FactorThroughFree.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/FactorThroughFree.lean#L300).

> **Stacks Project, Tag 0G9T.** A map from a finitely presented module which induces the zero
> map on `Tor₁` with every module factors through a free module.

```lean
lemma factor_through_free_of_tor_one_map_eq_zero
    {R : Type u} [CommRing R] {M M' : ModuleCat.{u} R} (f : M ⟶ M')
    [Module.FinitePresentation R M]
    (hf : ∀ N : ModuleCat.{u} R,
      ((Tor' (ModuleCat.{u} R) 1).map f).app N = 0) :
    FactorsThroughFree f.hom
```

## Tag 0G9U, an equation

[Tag 0G9U](https://stacks.math.columbia.edu/tag/0G9U) in the Stacks Project.

**`CategoryTheory.exists_shortExact_pushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/Support/ShortExactPushout.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/Support/ShortExactPushout.lean#L38).

> The pushout of the left-hand map in a short exact sequence is again a short exact sequence,
> with the same right-hand object.

```lean
theorem exists_shortExact_pushout
    {C : Type u} [Category C] [Abelian C]
    {K P M K' : C} {i : K ⟶ P} {p : P ⟶ M}
    (hip : i ≫ p = 0) (h : (ShortComplex.mk i p hip).ShortExact) (a : K ⟶ K') :
    ∃ (E : C) (j : P ⟶ E) (i' : K' ⟶ E) (q : E ⟶ M)
      (hi'q : i' ≫ q = 0),
      IsPushout i a j i' ∧ j ≫ q = p ∧ (ShortComplex.mk i' q hi'q).ShortExact
```

## Tag 0G9V, a lemma

[Tag 0G9V](https://stacks.math.columbia.edu/tag/0G9V) in the Stacks Project.

**`tfae_lift_ext_conditions`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/VanishingEquivalences.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/VanishingEquivalences.lean#L416). The attribute's comment: “equivalence of conditions (1)--(5)”.

> Conditions (1)--(5) are equivalent.

```lean
lemma tfae_lift_ext_conditions :
    List.TFAE [
      HasLiftVanishingAbove p p' alpha e,
      HasLiftVanishingAtSucc p p' alpha e,
      ExtMapVanishesAbove alpha e,
      ExtMapVanishesAtSucc alpha e,
      CanonicalExtClassPullbackVanishes p p' alpha e]
```

**`canonicalExtClassPullbackVanishes_imp_torMapVanishesAbove`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/VanishingEquivalences.lean, line 509](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/VanishingEquivalences.lean#L509). The attribute's comment: “condition (5) implies condition (6)”.

> Condition (5) implies condition (6).

```lean
lemma canonicalExtClassPullbackVanishes_imp_torMapVanishesAbove :
    CanonicalExtClassPullbackVanishes p p' alpha e → TorMapVanishesAbove alpha e
```

**`tfae_tor_conditions`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/VanishingEquivalences.lean, line 516](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/VanishingEquivalences.lean#L516). The attribute's comment: “equivalence of conditions (6) and (7)”.

> Conditions (6) and (7) are equivalent.

```lean
lemma tfae_tor_conditions :
    List.TFAE [TorMapVanishesAbove alpha e, TorMapVanishesAtSucc alpha e]
```

**`tfae_of_isPseudoCoherentFrom`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/VanishingEquivalences.lean, line 686](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/VanishingEquivalences.lean#L686). The attribute's comment: “all conditions under pseudo-coherence”.

> If `M` is `(-e-1)`-pseudo-coherent, all seven conditions are equivalent.

```lean
lemma tfae_of_isPseudoCoherentFrom
    (hM : StacksDraft.PseudoCoherence.IsPseudoCoherentFrom
      ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj M) (-(e : ℤ) - 1)) :
    List.TFAE [
      HasLiftVanishingAbove p p' alpha e,
      HasLiftVanishingAtSucc p p' alpha e,
      ExtMapVanishesAbove alpha e,
      ExtMapVanishesAtSucc alpha e,
      CanonicalExtClassPullbackVanishes p p' alpha e,
      TorMapVanishesAbove alpha e,
      TorMapVanishesAtSucc alpha e]
```

**`tfae_of_isNoetherianRing_of_finite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/VanishingEquivalences.lean, line 710](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/VanishingEquivalences.lean#L710). The attribute's comment: “Noetherian finite-module case”.

> Over a Noetherian ring, all seven conditions are equivalent when `M` is finite.

```lean
lemma tfae_of_isNoetherianRing_of_finite [IsNoetherianRing R] [Module.Finite R M] :
    List.TFAE [
      HasLiftVanishingAbove p p' alpha e,
      HasLiftVanishingAtSucc p p' alpha e,
      ExtMapVanishesAbove alpha e,
      ExtMapVanishesAtSucc alpha e,
      CanonicalExtClassPullbackVanishes p p' alpha e,
      TorMapVanishesAbove alpha e,
      TorMapVanishesAtSucc alpha e]
```

## Tag 0EH1, a lemma

[Tag 0EH1](https://stacks.math.columbia.edu/tag/0EH1) in the Stacks Project.

**`Stacks.LocalCohomology.exists_quotientPower_extMapVanishesAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/QuotientPowerVanishing.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityI/QuotientPowerVanishing.lean#L212).

> **[Stacks, Tag 0EH1].** Let `I` be an ideal of a Noetherian ring `A` and let `e` be the
> cohomological dimension of `I` in `A`. For every `n` there is an `m > n` for which the quotient
> map `A/I^m → A/I^n` satisfies the equivalent conditions of [Stacks, Tag 0G9V] in degree `e`:
> `Ext^i(A/I^n, N) → Ext^i(A/I^m, N)` is zero for every `A`-module `N` and every `i > e`.

```lean
theorem exists_quotientPower_extMapVanishesAbove
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A) (n : ℕ) :
    ∃ m : ℕ, ∃ hnm : n < m,
      ExtMapVanishesAbove
        (ModuleCat.ofHom (Ideal.Quotient.factorₐ A
          (Ideal.pow_le_pow_right (I := I) (Nat.le_of_lt hnm))).toLinearMap)
        (cohomologicalDimension A I (IsNoetherian.noetherian I)).toNat
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.20, Tag 0G9S](https://stacks.math.columbia.edu/tag/0G9S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
