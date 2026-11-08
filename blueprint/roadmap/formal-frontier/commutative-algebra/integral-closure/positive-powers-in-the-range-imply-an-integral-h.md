---
declaration: theorem
origin: cited
lean: RingHom.isIntegral_of_forall_pow_mem_range
statement: formalized
proof: formalized
---

# Positive powers in the range imply an integral homomorphism

[`RingHom.isIntegral_of_forall_pow_mem_range`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/RingHom.lean)
proves `f.IsIntegral` if each `x : S` has some positive power in `Set.range f`.
Each element may have its own exponent; neither a uniform exponent nor
surjectivity is required.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/README.md#headline-results) of [FormalFrontier/integral-closure](https://github.com/FormalFrontier/integral-closure) at commit [8f0b15a5](https://github.com/FormalFrontier/integral-closure/tree/8f0b15a513bbb22d6b51988f2b424cc407694390), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `RingHom.isIntegral_of_forall_pow_mem_range` (theorem), declared in [IntegralClosure/RingHom.lean, line 92](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/RingHom.lean#L92).

Read from the source at commit [8f0b15a5](https://github.com/FormalFrontier/integral-closure/tree/8f0b15a513bbb22d6b51988f2b424cc407694390), without running Lean.

## Sources

- [integral-closure at 8f0b15a5: README, headline results](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/README.md#headline-results)
- [Source of `RingHom.isIntegral_of_forall_pow_mem_range` in IntegralClosure/RingHom.lean](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/RingHom.lean#L92)
