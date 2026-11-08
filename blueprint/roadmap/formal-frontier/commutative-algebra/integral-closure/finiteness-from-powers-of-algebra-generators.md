---
declaration: theorem
origin: cited
lean: Subalgebra.finite_of_adjoin_eq_top_of_forall_exists_pow_mem
statement: formalized
proof: formalized
---

# Finiteness from powers of algebra generators

Let `R` and `A` be
commutative semirings with the given `R`-algebra structure. If a finite set
generates `A` as an `R`-algebra and `C : Subalgebra R A` contains a positive
power of each chosen generator, then the original `A` is finite as a module
over `C` through the canonical inclusion action. Exponents may vary with the
generator; no field, Noetherianity, finite type of `C/R`, or ring structure
is assumed. The theorem
[`Subalgebra.finite_of_adjoin_eq_top_of_forall_exists_pow_mem`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/Subalgebra.lean)
bounds powers in each singleton adjoin and multiplies the resulting
`C`-submodule spans.
Its finite-type, all-elements corollary is
[`Subalgebra.finite_of_forall_exists_pow_mem`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/Subalgebra.lean).
The generator-only criterion applies to `ℕ[X²] ⊊ ℕ[X]`, with generator `X`
and exponent `2`, where `1,X` span over `ℕ[X²]`. The all-elements condition
fails in this example: the `X`-coefficient of `(1+X)^n` is `n` for every
positive `n`. In general the bounded monomials span; they need not be a basis.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/README.md#headline-results) of [FormalFrontier/integral-closure](https://github.com/FormalFrontier/integral-closure) at commit [8f0b15a5](https://github.com/FormalFrontier/integral-closure/tree/8f0b15a513bbb22d6b51988f2b424cc407694390), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Subalgebra.finite_of_adjoin_eq_top_of_forall_exists_pow_mem` (theorem), declared in [IntegralClosure/Subalgebra.lean, line 94](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/Subalgebra.lean#L94).

Read from the source at commit [8f0b15a5](https://github.com/FormalFrontier/integral-closure/tree/8f0b15a513bbb22d6b51988f2b424cc407694390), without running Lean.

## Sources

- [integral-closure at 8f0b15a5: README, headline results](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/README.md#headline-results)
- [Source of `Subalgebra.finite_of_adjoin_eq_top_of_forall_exists_pow_mem` in IntegralClosure/Subalgebra.lean](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/Subalgebra.lean#L94)
