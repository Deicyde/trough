---
declaration: theorem
origin: cited
lean: RingHom.IsIntegralElem.pow
statement: formalized
proof: formalized
---

# Integrality is unchanged by positive powers

[`RingHom.IsIntegralElem.pow`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/RingHom.lean) shows that
every natural power of an integral element is integral, including exponent
zero. Conversely,
[`of_pow`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/RingHom.lean) and the simp lemma
[`pow_iff`](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/RingHom.lean) require `0 < n`: integrality of
`x ^ n` then implies, and is equivalent to, integrality of `x`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/README.md#headline-results) of [FormalFrontier/integral-closure](https://github.com/FormalFrontier/integral-closure) at commit [8f0b15a5](https://github.com/FormalFrontier/integral-closure/tree/8f0b15a513bbb22d6b51988f2b424cc407694390), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `RingHom.IsIntegralElem.pow` (theorem), declared in [IntegralClosure/RingHom.lean, line 112](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/RingHom.lean#L112).

Read from the source at commit [8f0b15a5](https://github.com/FormalFrontier/integral-closure/tree/8f0b15a513bbb22d6b51988f2b424cc407694390), without running Lean.

## Sources

- [integral-closure at 8f0b15a5: README, headline results](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/README.md#headline-results)
- [Source of `RingHom.IsIntegralElem.pow` in IntegralClosure/RingHom.lean](https://github.com/FormalFrontier/integral-closure/blob/8f0b15a513bbb22d6b51988f2b424cc407694390/IntegralClosure/RingHom.lean#L112)
