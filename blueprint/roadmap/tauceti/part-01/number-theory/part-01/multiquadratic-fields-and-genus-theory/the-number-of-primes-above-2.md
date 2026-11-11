---
declaration: theorem
origin: cited
lean: TauCeti.Multiquadratic.ncard_primesOver_two_eq_two_pow_sub
statement: formalized
proof: formalized
---

# The number of primes above `2`

Let `K` be generated over `ℚ` by square roots of `n`
square-class independent integers `d i` (no nonempty subset product is a square) not divisible by
`4`. Then there are exactly `2 ^ (n - a - b)` primes of `𝓞 K` above `2`, where the ramification
index is `e = 2 ^ a` and the residue degree is `f = 2 ^ b`:

* `a = 2` when some `d i` is `3` modulo `4` and some `d j` is even, or some `d i` is `2` and some
  `d j` is `6` modulo `8`; otherwise `a = 0` when every `d i` is `1` modulo `4`, and `a = 1` when
  not;
* `b = 1` when some subset product `∏_{i ∈ T} dᵢ` lies in the rational square class of an integer
  that is `5` modulo `8`, and `b = 0` otherwise.

```lean
TauCeti.Multiquadratic.ncard_primesOver_two_eq_two_pow_sub.{u_1, u_2} {K : Type u_1} [Field K]
  [NumberField K] {ι : Type u_2} [Finite ι] {d : ι → ℤ} {r : ι → K}
  (hr : ∀ (i : ι), r i ^ 2 = (algebraMap ℤ K) (d i))
  (htop : IntermediateField.adjoin ℚ (Set.range r) = ⊤) (hd : ∀ (i : ι), ¬4 ∣ d i)
  (hindep : ∀ (S : Finset ι), S.Nonempty → ¬IsSquare (∏ i ∈ S, ↑(d i))) :
  ((Ideal.span {2}).primesOver (NumberField.RingOfIntegers K)).ncard =
    2 ^
      (Nat.card ι -
        ((if (∃ i j, d i % 4 = 3 ∧ 2 ∣ d j) ∨ ∃ i j, d i % 8 = 2 ∧ d j % 8 = 6 then 2
          else if ∀ (i : ι), d i % 4 = 1 then 0 else 1) +
          if ∃ T c q, c % 8 = 5 ∧ q ≠ 0 ∧ ∏ i ∈ T, ↑(d i) = ↑c * q ^ 2 then 1 else 0))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Degree of a multiquadratic field over a finite index](degree-of-a-multiquadratic-field-over-a-finite-i.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.ncard_primesOver_two_eq_two_pow_sub`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Dyadic/Decomposition.html#TauCeti.Multiquadratic.ncard_primesOver_two_eq_two_pow_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.ncard_primesOver_two_eq_two_pow_sub`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Dyadic/Decomposition.html#TauCeti.Multiquadratic.ncard_primesOver_two_eq_two_pow_sub)
- [Source of `TauCeti.Multiquadratic.ncard_primesOver_two_eq_two_pow_sub` in TauCeti/NumberTheory/Multiquadratic/Dyadic/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Multiquadratic/Dyadic/Decomposition.lean#L132)
- [Tau Ceti roadmap status: Multiquadratic fields and genus theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/Multiquadratic/STATUS.md)
