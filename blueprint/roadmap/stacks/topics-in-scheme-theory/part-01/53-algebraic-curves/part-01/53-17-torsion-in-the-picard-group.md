---
declaration: section
origin: cited
lean: Stacks.Picard.nonempty_torsionBy_addEquiv_pi_zmod_of_smoothProjectiveCurve, Stacks.Picard.exists_rank_torsionBy_prime_pow_addEquiv_pi_zmod_of_smoothProjectiveCurve, Stacks.Picard.exists_finite_separable_torsionBy_of_genus_eq_one, Stacks.Picard.exists_finite_separable_torsionBy_of_two_le_genus, AlgebraicGeometry.finrank_picardTorsion_le_genus_add_geometricGenus_of_isReduced_dim_one, AlgebraicGeometry.finrank_picardTorsion_eq_iff_forall_isMulticrossSingularity_of_isReduced_dim_one
statement: formalized
proof: formalized
---

# 53.17 Torsion in the Picard group

Section 53.17 of the Stacks Project, [Tag 0C1Y](https://stacks.math.columbia.edu/tag/0C1Y). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C1Z, a lemma

[Tag 0C1Z](https://stacks.math.columbia.edu/tag/0C1Z) in the Stacks Project.

**`Stacks.Picard.nonempty_torsionBy_addEquiv_pi_zmod_of_smoothProjectiveCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/TorsionSmoothProjectiveCurve/Unconditional.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/TorsionSmoothProjectiveCurve/Unconditional.lean#L121). The attribute's comment: “clause (1)”.

> **Stacks Project, Tag 0C1Z (1).** Let `k` be an algebraically closed field and `X` a smooth
> projective curve of genus `g` over `k`. If `n ≥ 1` is invertible in `k`, then
> `Pic(X)[n] ≅ (ℤ/nℤ)^{⊕2g}`.

```lean
theorem nonempty_torsionBy_addEquiv_pi_zmod_of_smoothProjectiveCurve (k : Type u) [Field k]
    [IsAlgClosed k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsCurve k f]
    [IsProjectiveVariety k f] [Smooth f] (n : ℕ) (hn : 1 ≤ n) (hnk : IsUnit (n : k)) :
    Nonempty (Submodule.torsionBy ℤ (ofScheme X) (n : ℤ) ≃+ (Fin (2 * genus f) → ZMod n))
```

**`Stacks.Picard.exists_rank_torsionBy_prime_pow_addEquiv_pi_zmod_of_smoothProjectiveCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/TorsionSmoothProjectiveCurve/Unconditional.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/TorsionSmoothProjectiveCurve/Unconditional.lean#L134). The attribute's comment: “clause (2)”.

> **Stacks Project, Tag 0C1Z (2).** Let `k` be an algebraically closed field of characteristic
> `p > 0` and `X` a smooth projective curve of genus `g` over `k`. Then there is an integer
> `0 ≤ r ≤ g` with `Pic(X)[p^m] ≅ (ℤ/p^mℤ)^{⊕r}` for all `m ≥ 1` (the source's `f`).

```lean
theorem exists_rank_torsionBy_prime_pow_addEquiv_pi_zmod_of_smoothProjectiveCurve (k : Type u)
    [Field k] [IsAlgClosed k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsCurve k f]
    [IsProjectiveVariety k f] [Smooth f] (p : ℕ) [CharP k p] (hp : 0 < p) :
    ∃ r : ℕ, r ≤ genus f ∧ ∀ m : ℕ, 1 ≤ m →
      Nonempty (Submodule.torsionBy ℤ (ofScheme X) ((p : ℤ) ^ m) ≃+ (Fin r → ZMod (p ^ m)))
```

## Tag 0CDU, a lemma

[Tag 0CDU](https://stacks.math.columbia.edu/tag/0CDU) in the Stacks Project.

**`Stacks.Picard.exists_finite_separable_torsionBy_of_genus_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PicardTorsionVisible.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PicardTorsionVisible.lean#L112). The attribute's comment: “(1)”.

> **Stacks Project, Tag 0CDU (1).** Let `k` be a field, let `n` be prime to the characteristic
> of `k`, and let `X` be a smooth proper curve over `k` with `H⁰(X, 𝒪_X) = k` and of genus `1`.
> Then there is a finite separable extension `k'/k` such that `X_{k'}` has a `k'`-rational point
> and `Pic(X_{k'})[n] ≅ (ℤ/nℤ)^{⊕2}`.
>
> The point is a closed point with finite separable residue field, which exists by Tag 056U.

```lean
theorem exists_finite_separable_torsionBy_of_genus_eq_one [IsCurve k f] [Smooth f] [IsProper f]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)] (hg : genus f = 1) {n : ℕ}
    (hn : (n : k) ≠ 0) :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k'), FiniteDimensional k k' ∧
      Algebra.IsSeparable k k' ∧
      (∃ t : Spec (.of k') ⟶ pullback f (Spec.map (CommRingCat.ofHom (algebraMap k k'))),
        t ≫ pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k k'))) = 𝟙 _) ∧
      Nonempty (Submodule.torsionBy ℤ
        (ofScheme (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k k'))))) (n : ℤ) ≃+
        (Fin 2 → ZMod n))
```

**`Stacks.Picard.exists_finite_separable_torsionBy_of_two_le_genus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PicardTorsionVisible.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PicardTorsionVisible.lean#L137). The attribute's comment: “(2)”.

> **Stacks Project, Tag 0CDU (2).** Let `k` be a field, let `n` be prime to the characteristic
> of `k`, and let `X` be a smooth proper curve over `k` with `H⁰(X, 𝒪_X) = k` and of genus
> `g ≥ 2`. Then there is a finite separable extension `k'/k` with `[k' : k] ≤ (2g - 2)(n^{2g})!`
> such that `X_{k'}` has a `k'`-rational point and `Pic(X_{k'})[n] ≅ (ℤ/nℤ)^{⊕2g}`.
>
> The closed point of degree at most `2g - 2` with separable residue field is Tag 0CD4.

```lean
theorem exists_finite_separable_torsionBy_of_two_le_genus [IsCurve k f] [Smooth f] [IsProper f]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)] (hg : 2 ≤ genus f) {n : ℕ}
    (hn : (n : k) ≠ 0) :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k'), FiniteDimensional k k' ∧
      Algebra.IsSeparable k k' ∧
      Module.finrank k k' ≤ (2 * genus f - 2) * (n ^ (2 * genus f)).factorial ∧
      (∃ t : Spec (.of k') ⟶ pullback f (Spec.map (CommRingCat.ofHom (algebraMap k k'))),
        t ≫ pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k k'))) = 𝟙 _) ∧
      Nonempty (Submodule.torsionBy ℤ
        (ofScheme (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k k'))))) (n : ℤ) ≃+
        (Fin (2 * genus f) → ZMod n))
```

## Tag 0C20, a proposition

[Tag 0C20](https://stacks.math.columbia.edu/tag/0C20) in the Stacks Project.

**`AlgebraicGeometry.finrank_picardTorsion_le_genus_add_geometricGenus_of_isReduced_dim_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/TorsionReducedProperCurve.lean, line 768](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/TorsionReducedProperCurve.lean#L768). The attribute's comment: “the bound dim Pic(X)[l] ≤ g + g_geom (connectedness not needed)”.

> **Stacks Project, Tag 0C20, the bound.**
>
> Let `k` be an algebraically closed field, let `X` be a proper scheme over `k` which is reduced and
> of dimension one, let `g = h¹(X, 𝒪_X)` be its genus and let `g_geom` be the sum of the geometric
> genera of its irreducible components, and let `ℓ` be a prime different from the characteristic of
> `k`.  Then the `ℓ`-torsion of `Pic(X)` is finite-dimensional over `F_ℓ` and
>
> `dim_{F_ℓ} Pic(X)[ℓ] ≤ g + g_geom`.
>
> Connectedness, which the source assumes, is not needed; the source's statement is the special
> case `[ConnectedSpace X]`.
>
> The proof is the source's: the normalization is factored by [Stacks, Tag 0C1L], the two
> invariants are compared along the factorization by the three lines of the source's table, and at
> the far end `h¹(X^ν) = g_geom`
> (`AlgebraicGeometry.genus_normalizationOverField_eq_geometricGenus`) and
> `dim_{F_ℓ} Pic(X^ν)[ℓ] = 2 g_geom`, the latter from clause (1) of [Stacks, Tag 0C1Z]
> (`Stacks.Picard.nonempty_torsionBy_addEquiv_pi_zmod_of_smoothProjectiveCurve`) by
> `AlgebraicGeometry.rank_picardTorsion_normalizationSchemeOverField_eq_two_mul_geometricGenus`.

```lean
theorem finrank_picardTorsion_le_genus_add_geometricGenus_of_isReduced_dim_one (k : Type u)
    [Field k] [IsAlgClosed k]
    (X : Scheme.{u}) [X.Over (Spec (.of k))] [IsProper (X ↘ Spec (.of k))] [IsReduced X]
    (hdim : topologicalKrullDim (X : Type u) = 1) (ℓ : ℕ) [Fact ℓ.Prime] (hℓ : (ℓ : k) ≠ 0) :
    FiniteDimensional (ZMod ℓ) (AddSubgroup.torsionBy (ofScheme X) (ℓ : ℤ)) ∧
      Module.finrank (ZMod ℓ) (AddSubgroup.torsionBy (ofScheme X) (ℓ : ℤ)) ≤
        genus (X ↘ Spec (.of k)) + geometricGenus k (X ↘ Spec (.of k))
```

**`AlgebraicGeometry.finrank_picardTorsion_eq_iff_forall_isMulticrossSingularity_of_isReduced_dim_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/TorsionReducedProperCurve.lean, line 802](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/TorsionReducedProperCurve.lean#L802). The attribute's comment: “the equality criterion: equality iff all singularities are multicross”.

> **Stacks Project, Tag 0C20, the equality criterion.**
>
> In the situation of the bound
> `AlgebraicGeometry.finrank_picardTorsion_le_genus_add_geometricGenus_of_isReduced_dim_one`, the
> `ℓ`-torsion of `Pic(X)` is finite-dimensional over `F_ℓ`, and equality
> `dim_{F_ℓ} Pic(X)[ℓ] = g + g_geom` holds if and only if every singularity of `X` is multicross.
>
> Equality holds exactly when the factorization of the normalization contains no squishing, in
> both directions — the forward direction from the strict drop a squishing causes, the backward
> direction from the equality case of the arithmetic along a glueing chain — and the
> factorization contains no squishing exactly when every singularity of `X` is multicross
> (`Stacks.Curves.isGlueingChain_normalizationOver_iff_forall_isMulticrossSingularity`, the step
> the source leaves out: "just glue the local sequences for each point to find one that works for
> all singular points").

```lean
theorem finrank_picardTorsion_eq_iff_forall_isMulticrossSingularity_of_isReduced_dim_one
    (k : Type u) [Field k]
    [IsAlgClosed k] (X : Scheme.{u}) [X.Over (Spec (.of k))] [IsProper (X ↘ Spec (.of k))]
    [IsReduced X] (hdim : topologicalKrullDim (X : Type u) = 1) (ℓ : ℕ) [Fact ℓ.Prime]
    (hℓ : (ℓ : k) ≠ 0) :
    FiniteDimensional (ZMod ℓ) (AddSubgroup.torsionBy (ofScheme X) (ℓ : ℤ)) ∧
      (Module.finrank (ZMod ℓ) (AddSubgroup.torsionBy (ofScheme X) (ℓ : ℤ)) =
        genus (X ↘ Spec (.of k)) + geometricGenus k (X ↘ Spec (.of k)) ↔
      ∀ x : X, ¬ IsRegularLocalRing (X.presheaf.stalk x) →
        Stacks.Curves.IsMulticrossSingularity k X x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.17, Tag 0C1Y](https://stacks.math.columbia.edu/tag/0C1Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
