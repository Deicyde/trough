---
declaration: section
origin: cited
lean: free_of_frobenius_baseChange_equiv, isIdealIndependent_snoc_left_of_mul, length_quotient_eq_add_of_isIndependent_mul, length_quotient_span_powers_eq_prod, isIdealIndependent_map_of_flat, isRegularRing_iff_frobeniusOfPrime_flat
statement: formalized
proof: formalized
---

# 51.17 Frobenius action

Section 51.17 of the Stacks Project, [Tag 0EBU](https://stacks.math.columbia.edu/tag/0EBU). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EBV, a lemma

[Tag 0EBV](https://stacks.math.columbia.edu/tag/0EBV) in the Stacks Project.

**`free_of_frobenius_baseChange_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/FrobeniusAction/FrobeniusBaseChange.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/FrobeniusAction/FrobeniusBaseChange.lean#L89).

> A finite Frobenius-periodic module over a Noetherian local ring is free.

```lean
theorem free_of_frobenius_baseChange_equiv
    {A : Type u} {M : Type v} [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    [AddCommGroup M] [Module A M] [Module.Finite A M]
    (p : ℕ) [Fact p.Prime] [CharP A p]
    (h : Nonempty (frobeniusBaseChange A p M ≃ₗ[A] M)) :
    Module.Free A M
```

## Tag 0EBW, a lemma

[Tag 0EBW](https://stacks.math.columbia.edu/tag/0EBW) in the Stacks Project.

**`isIdealIndependent_snoc_left_of_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/FrobeniusAction/IdealIndependent.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/FrobeniusAction/IdealIndependent.lean#L51).

> If an ideal-independent finite family ends in `x * y`, replacing its last member by
> `x` gives another ideal-independent family.

```lean
theorem isIdealIndependent_snoc_left_of_mul {A : Type*} [CommRing A] {n : ℕ}
    (f : Fin n → A) (x y : A)
    (h : IsIdealIndependent (Fin.snoc f (x * y))) :
    IsIdealIndependent (Fin.snoc f x)
```

## Tag 0EBX, a lemma

[Tag 0EBX](https://stacks.math.columbia.edu/tag/0EBX) in the Stacks Project.

**`length_quotient_eq_add_of_isIndependent_mul`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/FrobeniusAction/LengthQuotient.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/FrobeniusAction/LengthQuotient.lean#L91).

> **Stacks Project, Tag 0EBX.** If appending `f * g` to a list gives an independent list,
> then the length of the quotient by that list is the sum of the lengths of the quotients obtained
> by appending `f` and `g` separately.

```lean
lemma length_quotient_eq_add_of_isIndependent_mul (init : List A) (f g : A)
    (h : IsIdealIndependent (fun i : Fin (init ++ [f * g]).length ↦
      (init ++ [f * g])[i])) :
    Module.length A (A ⧸ Ideal.ofList (init ++ [f * g])) =
      Module.length A (A ⧸ Ideal.ofList (init ++ [f])) +
        Module.length A (A ⧸ Ideal.ofList (init ++ [g]))
```

## Tag 0EBY, a lemma

[Tag 0EBY](https://stacks.math.columbia.edu/tag/0EBY) in the Stacks Project.

**`length_quotient_span_powers_eq_prod`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/FrobeniusAction/LengthQuotientPowers.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/FrobeniusAction/LengthQuotientPowers.lean#L220).

> **Stacks Project, Tag 0EBY.** If `x` generates the maximal ideal of a local ring and
> the positive powers `x i ^ e i` are independent, then the quotient by those powers has length
> equal to the product of the exponents.

```lean
lemma length_quotient_span_powers_eq_prod {A : Type*} [CommRing A] [IsLocalRing A]
    {r : ℕ} (x : Fin r → A) (e : Fin r → ℕ)
    (hx : Ideal.span (Set.range x) = IsLocalRing.maximalIdeal A)
    (he : ∀ i, 0 < e i)
    (hind : ∀ (a : Fin r → A), (∑ i, a i * x i ^ e i) = 0 →
      ∀ i, a i ∈ Ideal.span (Set.range fun j ↦ x j ^ e j)) :
    Module.length A (A ⧸ Ideal.span (Set.range fun i ↦ x i ^ e i)) =
      ((∏ i, e i : ℕ) : ℕ∞)
```

## Tag 0EBZ, a lemma

[Tag 0EBZ](https://stacks.math.columbia.edu/tag/0EBZ) in the Stacks Project.

**`isIdealIndependent_map_of_flat`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/FrobeniusAction/IdealIndependentFlat.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/FrobeniusAction/IdealIndependentFlat.lean#L51).

> The image of an ideal-independent family under a flat ring map is ideal-independent.

```lean
lemma isIdealIndependent_map_of_flat
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    {ι : Type w} (φ : A →+* B) (hφ : RingHom.Flat φ)
    {f : ι → A} (hf : IsIdealIndependent f) :
    IsIdealIndependent (fun i ↦ φ (f i))
```

## Tag 0EC0, a lemma

[Tag 0EC0](https://stacks.math.columbia.edu/tag/0EC0) in the Stacks Project.

**`isRegularRing_iff_frobeniusOfPrime_flat`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/FrobeniusAction/Kunz.lean, line 743](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/FrobeniusAction/Kunz.lean#L743).

> **Kunz's theorem.** If a prime number vanishes in a Noetherian ring, the ring is regular if
> and only if its Frobenius endomorphism is flat.

```lean
lemma isRegularRing_iff_frobeniusOfPrime_flat {A : Type*} [CommRing A] [IsNoetherianRing A]
    (p : ℕ) (hp : p.Prime) (hchar : (p : A) = 0) :
    IsRegularRing A ↔ RingHom.Flat (frobeniusOfPrime p hp hchar)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.17, Tag 0EBU](https://stacks.math.columbia.edu/tag/0EBU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
