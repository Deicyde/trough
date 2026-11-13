---
declaration: section
origin: cited
lean: Stacks.Resolution.trinomial_irreducible, Stacks.Resolution.trinomialRing_isDomain, Stacks.Resolution.trinomialRing_z_isPrime, Stacks.Resolution.trinomialRing_localization_equiv, Stacks.Resolution.trinomialRing_localization_uniqueFactorizationMonoid, Stacks.Resolution.trinomialRing_uniqueFactorizationMonoid, Stacks.MvPowerSeries.Brieskorn.not_uniqueFactorizationMonoid_brieskornHypersurface, Stacks.MvPowerSeries.Brieskorn.not_uniqueFactorizationMonoid_brieskornHypersurface_two_five_seven
statement: formalized
proof: formalized
---

# 89.9 Examples

Section 89.9 of the Stacks Project, [Tag 0AE8](https://stacks.math.columbia.edu/tag/0AE8). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AE9, an example

[Tag 0AE9](https://stacks.math.columbia.edu/tag/0AE9) in the Stacks Project.

**`Stacks.Resolution.trinomial_irreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/TrinomialHypersurface.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/TrinomialHypersurface.lean#L183). The attribute's comment: “irreducibility”.

> The defining trinomial is irreducible for positive pairwise coprime exponents.

```lean
theorem trinomial_irreducible (k : Type u) [Field k]
    (r s t : ℕ) (_hr : 0 < r) (_hs : 0 < s) (ht : 0 < t)
    (hrs : r.Coprime s) (_hrt : r.Coprime t) (_hst : s.Coprime t) :
    Irreducible (MvPolynomial.X (0 : Fin 3) ^ r +
      MvPolynomial.X (1 : Fin 3) ^ s +
      MvPolynomial.X (2 : Fin 3) ^ t : MvPolynomial (Fin 3) k)
```

**`Stacks.Resolution.trinomialRing_isDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/TrinomialHypersurface.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/TrinomialHypersurface.lean#L201). The attribute's comment: “integrality”.

> The trinomial hypersurface is integral.

```lean
theorem trinomialRing_isDomain (k : Type u) [Field k]
    (r s t : ℕ) (hr : 0 < r) (hs : 0 < s) (ht : 0 < t)
    (hrs : r.Coprime s) (hrt : r.Coprime t) (hst : s.Coprime t) :
    IsDomain (trinomialRing k r s t)
```

**`Stacks.Resolution.trinomialRing_z_isPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/TrinomialHypersurface.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/TrinomialHypersurface.lean#L263). The attribute's comment: “the prime element z”.

> The image of `z` generates a prime ideal in the hypersurface ring.

```lean
theorem trinomialRing_z_isPrime (k : Type u) [Field k]
    (r s t : ℕ) (_hr : 0 < r) (_hs : 0 < s) (ht : 0 < t)
    (hrs : r.Coprime s) :
    (Ideal.span ({Ideal.Quotient.mk _ (MvPolynomial.X (2 : Fin 3))} :
      Set (trinomialRing k r s t))).IsPrime
```

**`Stacks.Resolution.trinomialRing_localization_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/TrinomialHypersurface.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/TrinomialHypersurface.lean#L421). The attribute's comment: “localized polynomial presentation”.

> When `t = 1 + e r s`, localization at `z` is the localization of a polynomial
> ring in `x'`, `y'` at `-((x') ^ r + (y') ^ s)`, with the stated coordinate formulas.

```lean
theorem trinomialRing_localization_equiv (k : Type u) [Field k]
    (r s e : ℕ) :
    ∃ φ : Localization.Away
        (Ideal.Quotient.mk _ (MvPolynomial.X (2 : Fin 3)) :
          trinomialRing k r s (1 + e * r * s)) ≃ₐ[k]
        Localization.Away (-(MvPolynomial.X (0 : Fin 2) ^ r +
          MvPolynomial.X (1 : Fin 2) ^ s) : MvPolynomial (Fin 2) k),
      φ (algebraMap (trinomialRing k r s (1 + e * r * s)) _
          (Ideal.Quotient.mk _ (MvPolynomial.X (0 : Fin 3)))) =
        algebraMap (MvPolynomial (Fin 2) k) _
          (MvPolynomial.X (0 : Fin 2) *
            (-(MvPolynomial.X (0 : Fin 2) ^ r +
              MvPolynomial.X (1 : Fin 2) ^ s)) ^ (e * s)) ∧
      φ (algebraMap (trinomialRing k r s (1 + e * r * s)) _
          (Ideal.Quotient.mk _ (MvPolynomial.X (1 : Fin 3)))) =
        algebraMap (MvPolynomial (Fin 2) k) _
          (MvPolynomial.X (1 : Fin 2) *
            (-(MvPolynomial.X (0 : Fin 2) ^ r +
              MvPolynomial.X (1 : Fin 2) ^ s)) ^ (e * r)) ∧
      φ (algebraMap (trinomialRing k r s (1 + e * r * s)) _
          (Ideal.Quotient.mk _ (MvPolynomial.X (2 : Fin 3)))) =
        algebraMap (MvPolynomial (Fin 2) k) _
          (-(MvPolynomial.X (0 : Fin 2) ^ r +
            MvPolynomial.X (1 : Fin 2) ^ s))
```

**`Stacks.Resolution.trinomialRing_localization_uniqueFactorizationMonoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/TrinomialHypersurface.lean, line 491](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/TrinomialHypersurface.lean#L491). The attribute's comment: “factorial localization”.

> In the explicit presentation, inverting `z` gives a unique factorization monoid.

```lean
theorem trinomialRing_localization_uniqueFactorizationMonoid (k : Type u) [Field k]
    (r s e : ℕ) :
    UniqueFactorizationMonoid
      (Localization.Away
        (Ideal.Quotient.mk _ (MvPolynomial.X (2 : Fin 3)) :
          trinomialRing k r s (1 + e * r * s)))
```

**`Stacks.Resolution.trinomialRing_uniqueFactorizationMonoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/TrinomialHypersurface.lean, line 710](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/TrinomialHypersurface.lean#L710). The attribute's comment: “unique factorization”.

> The trinomial hypersurface is a unique factorization domain.

```lean
theorem trinomialRing_uniqueFactorizationMonoid (k : Type u) [Field k]
    (r s t : ℕ) (hr : 0 < r) (hs : 0 < s) (ht : 0 < t)
    (hrs : r.Coprime s) (hrt : r.Coprime t) (hst : s.Coprime t) :
    UniqueFactorizationMonoid (trinomialRing k r s t)
```

## Tag 0AEA, an example

[Tag 0AEA](https://stacks.math.columbia.edu/tag/0AEA) in the Stacks Project.

**`Stacks.MvPowerSeries.Brieskorn.not_uniqueFactorizationMonoid_brieskornHypersurface`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MvPowerSeries/BrieskornHypersurface.lean, line 963](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/MvPowerSeries/BrieskornHypersurface.lean#L963). The attribute's comment: “the general nonfactoriality assertion”.

> Apart from the `E₈` triple `(2, 3, 5)`, a Brieskorn hypersurface with ordered,
> pairwise coprime exponents greater than one is not factorial.

```lean
public theorem not_uniqueFactorizationMonoid_brieskornHypersurface
    {r s t : ℕ} (hr : 1 < r) (hrs : r < s) (hst : s < t)
    (hrs' : Nat.Coprime r s) (hrt' : Nat.Coprime r t) (hst' : Nat.Coprime s t)
    (hE8 : ¬ (r = 2 ∧ s = 3 ∧ t = 5)) :
    ¬ UniqueFactorizationMonoid (BrieskornHypersurface r s t)
```

**`Stacks.MvPowerSeries.Brieskorn.not_uniqueFactorizationMonoid_brieskornHypersurface_two_five_seven`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MvPowerSeries/BrieskornHypersurface.lean, line 973](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/MvPowerSeries/BrieskornHypersurface.lean#L973). The attribute's comment: “the explicit (2, 5, 7) example”.

> The hypersurface `ℂ⟦x,y,z⟧/(x²+y⁵+z⁷)` is not factorial.

```lean
public theorem not_uniqueFactorizationMonoid_brieskornHypersurface_two_five_seven :
    ¬ UniqueFactorizationMonoid (BrieskornHypersurface 2 5 7)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 89.9, Tag 0AE8](https://stacks.math.columbia.edu/tag/0AE8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
