---
declaration: section
origin: cited
lean: Ideal.LocallyNilpotent, Ideal.Nilpotent, Stacks.LocallyNilpotentNotNilpotent.idealJ_le_nilradical, Stacks.LocallyNilpotentNotNilpotent.not_isNilpotent_idealJ, Ideal.IsLocallyNilpotent0544.map, Stacks.NilpotentIdeal.PowerMap.isUnit_quotient_mk_iff, Ideal.exists_pow_le_of_le_radical_of_fg, Ideal.fg_of_isNoetherianRing
statement: formalized
proof: formalized
---

# 10.32 Locally nilpotent ideals

Section 10.32 of the Stacks Project, [Tag 0AMF](https://stacks.math.columbia.edu/tag/0AMF). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00IL, a definition

[Tag 00IL](https://stacks.math.columbia.edu/tag/00IL) in the Stacks Project.

**`Ideal.LocallyNilpotent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nilpotent/Ideal.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/Ideal.lean#L91). The attribute's comment: “locally nilpotent”. References: SGA 6 VI (6.1).

> An ideal `I ⊂ R` is *locally nilpotent* if every element of `I` is nilpotent,
> i.e. for every `x ∈ I` there exists `n ∈ ℕ` with `x ^ n = 0`.

```lean
def LocallyNilpotent (I : Ideal R) : Prop
```

**`Ideal.Nilpotent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nilpotent/Ideal.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/Ideal.lean#L97). The attribute's comment: “nilpotent”.

> An ideal `I ⊂ R` is *nilpotent* if there exists `n ∈ ℕ` with `I ^ n = 0`,
> where `0 = ⊥` is the zero ideal.

```lean
def Nilpotent (I : Ideal R) : Prop
```

## Tag 0EGG, an example

[Tag 0EGG](https://stacks.math.columbia.edu/tag/0EGG) in the Stacks Project.

**`Stacks.LocallyNilpotentNotNilpotent.idealJ_le_nilradical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nilpotent/Ideal.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/Ideal.lean#L188).

> `J ≤ nilradical S`, i.e. every element of `J` is nilpotent.

```lean
theorem idealJ_le_nilradical : idealJ k ≤ nilradical (S_ring k)
```

**`Stacks.LocallyNilpotentNotNilpotent.not_isNilpotent_idealJ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nilpotent/Ideal.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/Ideal.lean#L215).

> `J` is not nilpotent: there is no `m` with `J ^ m = 0`.

```lean
theorem not_isNilpotent_idealJ : ¬ IsNilpotent (idealJ k)
```

## Tag 0544, a lemma

[Tag 0544](https://stacks.math.columbia.edu/tag/0544) in the Stacks Project.

**`Ideal.IsLocallyNilpotent0544.map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nilpotent/Ideal.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/Ideal.lean#L141). References: EGA III (5.4.6), “more general”.

> If `R → R'` is a ring map and `I ⊂ R` is a locally nilpotent ideal, then
> the extended ideal `IR' = I.map f` is locally nilpotent in `R'`.

```lean
theorem Ideal.IsLocallyNilpotent0544.map
    {R R' : Type*} [CommRing R] [CommRing R']
    (f : R →+* R') (I : Ideal R)
    (hI : Ideal.IsLocallyNilpotent0544 I) :
    Ideal.IsLocallyNilpotent0544 (I.map f)
```

## Tag 0AMG, a lemma

[Tag 0AMG](https://stacks.math.columbia.edu/tag/0AMG) in the Stacks Project.

**`Stacks.NilpotentIdeal.PowerMap.isUnit_quotient_mk_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nilpotent/Lifting.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/Lifting.lean#L145). References: EGA 0 (19.10.3), “more general”; EGA 0 (7.1.12), “special case”.

> Units are detected modulo a locally nilpotent ideal.

```lean
theorem isUnit_quotient_mk_iff (hI : ∀ x ∈ I, IsNilpotent x) {x : R} :
    IsUnit x ↔ IsUnit ((Ideal.Quotient.mk I) x)
```

## Tag 00IM, a lemma

[Tag 00IM](https://stacks.math.columbia.edu/tag/00IM) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.exists_pow_le_of_le_radical_of_fg`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.exists_pow_le_of_le_radical_of_fg#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Nilpotent/Ideal.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/Ideal.lean#L123) (StacksFrontier). References: EGA I (6.1.6), “affine case”.
- [`Ideal.fg_of_isNoetherianRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.fg_of_isNoetherianRing#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Nilpotent/Ideal.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/Ideal.lean#L125) (StacksFrontier): “every ideal of a Noetherian ring is finitely generated”.
- [`Ideal.FG.isNilpotent_iff_le_nilradical`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.FG.isNilpotent_iff_le_nilradical#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Nilpotent/Ideal.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/Ideal.lean#L127) (StacksFrontier): “locally nilpotent = nilpotent”. References: EGA I (6.1.6), “affine case”.

## Tag 05BU, a lemma

[Tag 05BU](https://stacks.math.columbia.edu/tag/05BU) in the Stacks Project.

**`exists_isIdempotentElem_add_sq_sub_mul_sum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Idempotents/IntegerPolynomial.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Idempotents/IntegerPolynomial.lean#L72).

> Let `A` be a possibly noncommutative ring and let `e ∈ A` be such that `x = e ^ 2 - e` is
> nilpotent. Then there is an idempotent of the form `e + x * (∑ a i j • (e ^ i * x ^ j))` with
> integer coefficients `a i j`.

```lean
theorem exists_isIdempotentElem_add_sq_sub_mul_sum {e : A} (he : IsNilpotent (e ^ 2 - e)) :
    ∃ (N : ℕ) (a : ℕ → ℕ → ℤ), IsIdempotentElem (e + (e ^ 2 - e) *
      ∑ i ∈ Finset.range N, ∑ j ∈ Finset.range N, a i j • (e ^ i * (e ^ 2 - e) ^ j))
```

## Tag 0CAP, a lemma

[Tag 0CAP](https://stacks.math.columbia.edu/tag/0CAP) in the Stacks Project.

**`Stacks.NilpotentIdeal.PowerMap.powMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nilpotent/Lifting.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/Lifting.lean#L229). The attribute's comment: “(1)”.

> If `I` is locally nilpotent and `n ≥ 1` is invertible in `R/I`, then the `n`th power map
> `1 + x ↦ (1 + x)^n` on `1 + I` is a bijection.

```lean
theorem powMap_bijective
    (hI : ∀ x ∈ I, IsNilpotent x) {n : ℕ} (hn : 1 ≤ n)
    (hnu : IsUnit ((n : R ⧸ I))) :
    Function.Bijective (powMap I n)
```

**`Stacks.NilpotentIdeal.PowerMap.isUnit_pow_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nilpotent/Lifting.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/Lifting.lean#L238). The attribute's comment: “(2)”.

> If `I` is locally nilpotent and `n ≥ 1` is invertible in `R/I`, then a unit `u ∈ Rˣ` is
> an `n`th power in `R` if and only if its image in `R/I` is an `n`th power (as a unit) in `R/I`.

```lean
theorem isUnit_pow_iff
    (hI : ∀ x ∈ I, IsNilpotent x) {n : ℕ} (hn : 1 ≤ n)
    (hnu : IsUnit ((n : R ⧸ I))) (u : Rˣ) :
    (∃ v : Rˣ, u = v ^ n) ↔
      (∃ w : (R ⧸ I)ˣ, (Ideal.Quotient.mk I (u : R) : R ⧸ I) = (w : R ⧸ I) ^ n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.32, Tag 0AMF](https://stacks.math.columbia.edu/tag/0AMF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
