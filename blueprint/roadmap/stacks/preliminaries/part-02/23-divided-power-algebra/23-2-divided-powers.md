---
declaration: section
origin: cited
lean: DividedPowers, DividedPowers.instSubsingletonDividedPowers, DividedPowers.exists_dividedPowers_iff_factorial_mul_eq_pow, DividedPowers.nonempty_dividedPowers_iff_exists_generators_pow_mem_factorial_mul, DividedPowers.factorial_mul_dpow_eq_pow, DividedPowers.exists_dividedPowers_span_natCast, DividedPowers.exists_dividedPowers_of_axioms_on_generators, DividedPowers.existsUnique_on_ideal_add
statement: formalized
proof: formalized
---

# 23.2 Divided powers

Section 23.2 of the Stacks Project, [Tag 07GK](https://stacks.math.columbia.edu/tag/07GK). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07GL, a definition

[Tag 07GL](https://stacks.math.columbia.edu/tag/07GL) in the Stacks Project.

Declarations registered for the tag:

- [`DividedPowers`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DividedPowers#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch23.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch23.lean#L34) (StacksFrontier).

## Tag 07GM, a lemma

[Tag 07GM](https://stacks.math.columbia.edu/tag/07GM) in the Stacks Project.

**`DividedPowers.instSubsingletonDividedPowers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Criteria.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/Criteria.lean#L75). The attribute's comment: “uniqueness”.

> A divided power structure on an ideal in a ring torsion-free as a `ℤ`-module is unique.

```lean
public instance instSubsingletonDividedPowers {A : Type*} [CommRing A]
    [Module.IsTorsionFree ℤ A] (I : Ideal A) : Subsingleton (_root_.DividedPowers I)
```

**`DividedPowers.exists_dividedPowers_iff_factorial_mul_eq_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Criteria.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/Criteria.lean#L94). The attribute's comment: “factorial\_criterion”.

> Over a torsion-free commutative ring, maps on an ideal are divided power operations if and
> only if their products with the corresponding factorials are the corresponding powers.

```lean
public theorem exists_dividedPowers_iff_factorial_mul_eq_pow
    {A : Type*} [CommRing A] [Module.IsTorsionFree ℤ A] (I : Ideal A)
    (γ : ℕ → I → I) :
    (∃ dp : _root_.DividedPowers I,
        ∀ (n : ℕ) (x : I), 0 < n → dp.dpow n (x : A) = (γ n x : A)) ↔
      ∀ (n : ℕ) (x : I), 0 < n →
        (n.factorial : A) * (γ n x : A) = (x : A) ^ n
```

**`DividedPowers.nonempty_dividedPowers_iff_exists_generators_pow_mem_factorial_mul`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Criteria.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/Criteria.lean#L194). The attribute's comment: “generator\_criterion”.

> Let `I` be an ideal in a torsion-free commutative ring. Then `I` admits a divided power
> structure if and only if it has a set of ideal generators `s` such that, for every `x ∈ s` and
> every positive `n`, the power `x ^ n` belongs to `(n!) I`.

```lean
public lemma nonempty_dividedPowers_iff_exists_generators_pow_mem_factorial_mul
    {A : Type*} [CommRing A] [HasUniqueDiv A] (I : Ideal A) :
    Nonempty (_root_.DividedPowers I) ↔
      ∃ s : Set A, (Ideal.span s = I ∧
        ∀ x ∈ s, ∀ n : ℕ, (1 ≤ n →
          x ^ n ∈ Ideal.span {(n.factorial : A)} * I))
```

Declarations registered for the tag:

- [`DividedPowers.factorial_mul_dpow_eq_pow`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DividedPowers.factorial_mul_dpow_eq_pow#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/DividedPowers/Criteria.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/Criteria.lean#L71) (StacksFrontier): “factorial\_identity”.

## Tag 07GN, an example

[Tag 07GN](https://stacks.math.columbia.edu/tag/07GN) in the Stacks Project.

**`DividedPowers.exists_dividedPowers_span_natCast`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Extend/IntegersAtPrime.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/Extend/IntegersAtPrime.lean#L169).

> If `A` is a `ℤ_(p)`-algebra, the ideal generated by `p` has the divided power structure
> given by
> `γₙ(p * a) = (p ^ n / n!) * a ^ n`.
>
> The function `q` in the conclusion consists of the coefficients `p ^ n / n!` in `ℤ_(p)`;
> the first two properties say that these quotients exist and lie in `pℤ_(p)` in positive
> degrees.

```lean
public theorem exists_dividedPowers_span_natCast
    {A : Type*} [CommRing A] (p : ℕ) [Fact p.Prime] [Algebra (IntegersAtPrime p) A] :
    ∃ (q : ℕ → IntegersAtPrime p) (γ : DividedPowers (Ideal.span {(p : A)})),
      (∀ n : ℕ, (n.factorial : IntegersAtPrime p) * q n = (p : IntegersAtPrime p) ^ n) ∧
        (∀ n : ℕ, n ≠ 0 → q n ∈ Ideal.span {(p : IntegersAtPrime p)}) ∧
          ∀ (n : ℕ) (a : A),
            γ.dpow n ((p : A) * a) = algebraMap (IntegersAtPrime p) A (q n) * a ^ n
```

## Tag 07GP, a lemma

[Tag 07GP](https://stacks.math.columbia.edu/tag/07GP) in the Stacks Project.

**`DividedPowers.exists_dividedPowers_of_axioms_on_generators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Criteria.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/Criteria.lean#L563).

> The product and iteration axioms for divided powers need only be checked on a set of
> generators of the ideal, provided the other divided power axioms hold everywhere.

```lean
public theorem exists_dividedPowers_of_axioms_on_generators
    {A : Type*} [CommRing A] (I : Ideal A) (dpow : ℕ → A → A) (S : Set A)
    (hS : I = Ideal.span S)
    (dpow_zero : ∀ {x : A}, x ∈ I → dpow 0 x = 1)
    (dpow_one : ∀ {x : A}, x ∈ I → dpow 1 x = x)
    (dpow_mem : ∀ {n : ℕ} {x : A}, n ≠ 0 → x ∈ I → dpow n x ∈ I)
    (dpow_add : ∀ {n : ℕ} {x y : A}, x ∈ I → y ∈ I →
      dpow n (x + y) = (antidiagonal n).sum fun k ↦ dpow k.1 x * dpow k.2 y)
    (dpow_mul : ∀ {n : ℕ} {a x : A}, x ∈ I →
      dpow n (a * x) = a ^ n * dpow n x)
    (mul_dpow_on_generators : ∀ {m n : ℕ} {x : A}, x ∈ S →
      dpow m x * dpow n x = (choose (m + n) m : A) * dpow (m + n) x)
    (dpow_comp_on_generators : ∀ {m n : ℕ} {x : A}, n ≠ 0 → x ∈ S →
      dpow m (dpow n x) = (uniformBell m n : A) * dpow (m * n) x) :
    ∃ hI : _root_.DividedPowers I, ∀ (n : ℕ) {x : A}, x ∈ I → hI.dpow n x = dpow n x
```

## Tag 07GQ, a lemma

[Tag 07GQ](https://stacks.math.columbia.edu/tag/07GQ) in the Stacks Project.

**`DividedPowers.existsUnique_on_ideal_add`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Criteria.lean, line 766](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/Criteria.lean#L766). The attribute's comment: “part (2)”.

> Divided power structures which agree on the intersection of their ideals extend uniquely
> to the sum of the ideals.

```lean
public lemma existsUnique_on_ideal_add {A : Type*} [CommRing A] {I J : Ideal A}
    (γ : _root_.DividedPowers I)
    (δ : _root_.DividedPowers J)
    (h : ∀ (n : ℕ) {x : A}, x ∈ I ⊓ J → γ.dpow n x = δ.dpow n x) :
    ∃! ε : _root_.DividedPowers (I + J),
      (∀ (n : ℕ) {x : A}, x ∈ I → ε.dpow n x = γ.dpow n x) ∧
        (∀ (n : ℕ) {x : A}, x ∈ J → ε.dpow n x = δ.dpow n x)
```

Declarations registered for the tag:

- [`DividedPowers.coincide_on_smul`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DividedPowers.coincide_on_smul#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/DividedPowers/Criteria.lean, line 704](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/Criteria.lean#L704) (StacksFrontier): “part (1)”.

## Tag 07GR, a lemma

[Tag 07GR](https://stacks.math.columbia.edu/tag/07GR) in the Stacks Project.

**`DividedPowers.locallyNilpotent_iff_isNilpotent_natCast`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Nilpotent.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/Nilpotent.lean#L46).

> Let `p` be a prime number, let `γ` be a divided power structure on an ideal `I` of a
> commutative ring `A`, and assume `p` is nilpotent in `A ⧸ I`. Then `I` is locally nilpotent,
> i.e. every element of `I` is nilpotent, if and only if `p` is nilpotent in `A`.

```lean
public theorem locallyNilpotent_iff_isNilpotent_natCast {A : Type*} [CommRing A] {p : ℕ}
    (hp : p.Prime) {I : Ideal A} (γ : DividedPowers I) (hpI : IsNilpotent (p : A ⧸ I)) :
    I.LocallyNilpotent ↔ IsNilpotent (p : A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 23.2, Tag 07GK](https://stacks.math.columbia.edu/tag/07GK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
