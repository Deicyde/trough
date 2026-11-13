---
declaration: section
origin: cited
lean: Ring.finite_maximalSpectrum_and_sum_inertiaDeg_mul_ord_le_and_eq_iff_finite, Stacks.LocalizationOfFiniteAlgebra.essFiniteType_localization_finite, AdicCompletion.exists_isIdempotentElem_nonempty_algEquiv_prod_quotient
statement: formalized
proof: formalized
---

# 10.124 Applications of Zariski's Main Theorem

Section 10.124 of the Stacks Project, [Tag 03GB](https://stacks.math.columbia.edu/tag/03GB). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02MM, a lemma

[Tag 02MM](https://stacks.math.columbia.edu/tag/02MM) in the Stacks Project.

**`Ring.finite_maximalSpectrum_and_sum_inertiaDeg_mul_ord_le_and_eq_iff_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/OrderOfVanishing/Degree.lean, line 934](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/OrderOfVanishing/Degree.lean#L934). The attribute's comment: “`ord` is `Ring.ord`, valued in `ℕ∞`, applied to the image of `x : A`; the residue degrees are `Ideal.inertiaDeg`; semi-locality is `Finite (MaximalSpectrum B)`; the sum is a `finsum`. See the module docstring.”.

> **The degree inequality for orders of vanishing.** Let `A ⊆ B` be an extension of domains
> with `A` local Noetherian of dimension at most `1`, `B` of finite type over `A`, and the induced
> extension `L/K` of fraction fields finite. Then `B` is semi-local, and for every nonzero `x` in
> the maximal ideal of `A` the sum over the maximal ideals `𝔪` of `B` of
> `[κ(𝔪) : κ(𝔪_A)] · ord_{B_𝔪}(x)` is at most `[L : K] · ord_A(x)`, with equality if and only if
> `A → B` is finite.

```lean
public theorem Ring.finite_maximalSpectrum_and_sum_inertiaDeg_mul_ord_le_and_eq_iff_finite
    {A B : Type*} [CommRing A] [IsDomain A] [IsLocalRing A] [IsNoetherianRing A]
    [Ring.KrullDimLE 1 A] [CommRing B] [IsDomain B] [Algebra A B] [FaithfulSMul A B]
    [Algebra.FiniteType A B] {K L : Type*} [Field K] [Field L] [Algebra A K] [IsFractionRing A K]
    [Algebra B L] [IsFractionRing B L] [Algebra A L] [Algebra K L] [IsScalarTower A B L]
    [IsScalarTower A K L] [Module.Finite K L] :
    Finite (MaximalSpectrum B) ∧
      ∀ x ∈ IsLocalRing.maximalIdeal A, x ≠ 0 →
        (∑ᶠ m : MaximalSpectrum B, (m.asIdeal.inertiaDeg A : ℕ∞) *
              Ring.ord (Localization.AtPrime m.asIdeal)
                (algebraMap B (Localization.AtPrime m.asIdeal) (algebraMap A B x))
            ≤ (Module.finrank K L : ℕ∞) * Ring.ord A x) ∧
          ((∑ᶠ m : MaximalSpectrum B, (m.asIdeal.inertiaDeg A : ℕ∞) *
                Ring.ord (Localization.AtPrime m.asIdeal)
                  (algebraMap B (Localization.AtPrime m.asIdeal) (algebraMap A B x))
              = (Module.finrank K L : ℕ∞) * Ring.ord A x) ↔ Module.Finite A B)
```

## Tag 052V, a lemma

[Tag 052V](https://stacks.math.columbia.edu/tag/052V) in the Stacks Project.

**`Stacks.LocalizationOfFiniteAlgebra.essFiniteType_localization_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/EssentialFiniteness/ZariskiApplication.lean, line 305](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/EssentialFiniteness/ZariskiApplication.lean#L305).

> Let `f : (R, m_R) → (S, m_S)` be a local homomorphism of local rings. Assume `f` is
> essentially of finite type, the residue field extension `κ(m_R) ⊆ κ(m_S)` is finite, and the
> closed fiber `S / m_R S` has Krull dimension `0`. Then `S` is a localization of a finite
> `R`-algebra: there exist a ring `S''`, a finite ring map `g : R →+* S''`, a submonoid `T ≤ S''`,
> and a ring map `h : S'' →+* S` exhibiting `S` as the localization of `S''` at `T`, with
> `h ∘ g = f` as `R`-algebra maps.

```lean
theorem essFiniteType_localization_finite {R S : Type u} [CommRing R] [CommRing S]
    [IsLocalRing R] [IsLocalRing S] (f : R →+* S) [IsLocalHom f]
    (hft : f.EssFiniteType)
    (hres : @Module.Finite (IsLocalRing.ResidueField R) (IsLocalRing.ResidueField S)
      _ _ (residueAlgebra f).toModule)
    (hdim : ringKrullDim (closedFiber f) = 0) :
    ∃ (S'' : Type u) (_ : CommRing S'') (g : R →+* S'') (h : S'' →+* S)
      (T : Submonoid S''),
      g.Finite ∧ h.comp g = f ∧ @IsLocalization S'' _ T S _ h.toAlgebra
```

## Tag 07NC, a lemma

[Tag 07NC](https://stacks.math.columbia.edu/tag/07NC) in the Stacks Project.

**`AdicCompletion.exists_isIdempotentElem_nonempty_algEquiv_prod_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/QuasiFinite.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/QuasiFinite.lean#L448). The attribute's comment: “The source's `B` is named here as the explicit factor `(S ⊗[R] Rₚ^∧) ⧸ (e)` of an idempotent `e`, which is what makes it an `Rₚ^∧`-algebra. See the module docstring.”.

> Let `R` be a Noetherian ring, let `S` be an `R`-algebra of finite type, and
> let `q` be a prime of `S` lying over `p ⊂ R` at which `R → S` is quasi-finite. Let `Rₚ` and `S_q`
> be the local rings of `R` at `p` and of `S` at `q`. Then the base change of `S` along the
> completion `Rₚ^∧` of `Rₚ` at its maximal ideal is, as an `S`-algebra, the product of the
> completion `S_q^∧` of `S_q` at its maximal ideal with a complementary factor cut out by an
> idempotent: `Rₚ^∧ ⊗[R] S = S_q^∧ × B` for some `Rₚ^∧`-algebra `B`.

```lean
public theorem AdicCompletion.exists_isIdempotentElem_nonempty_algEquiv_prod_quotient
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S] [IsNoetherianRing R]
    [Algebra.FiniteType R S] (p : Ideal R) [p.IsPrime] (q : Ideal S) [q.IsPrime]
    [q.LiesOver p] [Algebra.QuasiFiniteAt R q]
    (Rp : Type*) [CommRing Rp] [Algebra R Rp] [IsLocalization.AtPrime Rp p] [IsLocalRing Rp]
    (Sq : Type*) [CommRing Sq] [Algebra S Sq] [IsLocalization.AtPrime Sq q] [IsLocalRing Sq] :
    ∃ e : S ⊗[R] AdicCompletion (maximalIdeal Rp) Rp, IsIdempotentElem e ∧
      Nonempty (S ⊗[R] AdicCompletion (maximalIdeal Rp) Rp ≃ₐ[S]
        AdicCompletion (maximalIdeal Sq) Sq ×
          ((S ⊗[R] AdicCompletion (maximalIdeal Rp) Rp) ⧸ Ideal.span {e}))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.124, Tag 03GB](https://stacks.math.columbia.edu/tag/03GB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
