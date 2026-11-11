---
declaration: section
origin: cited
lean: Ideal.symbolicPower, ass_quotient_symbolicPower', symbolicPower_map_of_flat
statement: formalized
proof: formalized
---

# 10.64 Symbolic powers

Section 10.64 of the Stacks Project, [Tag 05G9](https://stacks.math.columbia.edu/tag/05G9). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0313, a definition

[Tag 0313](https://stacks.math.columbia.edu/tag/0313) in the Stacks Project.

**`Ideal.symbolicPower`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/SymbolicPower.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/SymbolicPower.lean#L49). References: EGA IV (11.4.7).

> The `n`th *symbolic power* `p ^ (n)` of a prime ideal `p` of a commutative semiring `R`: the
> kernel of `R → R_p / p ^ n R_p`, realized as the contraction to `R` of the ideal `p ^ n R_p` of the
> localization `R_p`.

```lean
public def symbolicPower {R : Type*} [CommSemiring R] (p : Ideal R) [p.IsPrime] (n : ℕ) :
    Ideal R
```

## Tag 0314, a lemma

[Tag 0314](https://stacks.math.columbia.edu/tag/0314) in the Stacks Project.

**`ass_quotient_symbolicPower'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/SymbolicPower/AssociatedPrimes.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/SymbolicPower/AssociatedPrimes.lean#L166).

> For a Noetherian ring `R`, a prime ideal `p`, and `n > 0`, the set of associated primes of
> `R / p^{(n)}` is exactly `{p}`.

```lean
theorem ass_quotient_symbolicPower' {R : Type*} [CommRing R] [IsNoetherianRing R]
    (p : Ideal R) [p.IsPrime] (n : ℕ) (hn : 0 < n) :
    Stacks.AssociatedPrimes.assPrimes R (R ⧸ symbolicPower' p n) = {p}
```

## Tag 0BC0, a lemma

[Tag 0BC0](https://stacks.math.columbia.edu/tag/0BC0) in the Stacks Project.

**`symbolicPower_map_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/SymbolicPower.lean, line 697](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/SymbolicPower.lean#L697).

> For a flat ring map `R → S` and a prime `p ⊆ R` whose extension `q = p S` is prime,
> `p^{(n)} S = q^{(n)}`.

```lean
theorem symbolicPower_map_of_flat {R S : Type*} [CommRing R] [CommRing S] (φ : R →+* S)
    (hφ : φ.Flat) (p : Ideal R) [p.IsPrime] (hq : (p.map φ).IsPrime) (n : ℕ) :
    (symbolicPower' p n).map φ = symbolicPower' (p.map φ) n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.64, Tag 05G9](https://stacks.math.columbia.edu/tag/05G9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
