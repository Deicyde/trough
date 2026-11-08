---
declaration: theorem
origin: cited
lean: Filter.Germ.isReduced_iff_eventually
statement: formalized
proof: formalized
---

# Reduced filter germs

For independent index and value universes, any filter `D`, and a value type `M`
with only zero and natural-number powers,
[`Filter.Germ.isReduced_iff_eventually`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Germ/Reduced.lean)
characterizes reducedness of `Germ D M` by eventual reducedness of `M`.
Equivalently, `D = ⊥` or `M` is reduced. No power laws or properness assumption
are needed. The same module characterizes nilpotence by one exponent whose
power is zero eventually, and supplies reducedness for germs of reduced values.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Filter.Germ.isReduced_iff_eventually` (theorem), declared in [MinimalPrimes/Order/Filter/Germ/Reduced.lean, line 55](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Germ/Reduced.lean#L55).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Filter.Germ.isReduced_iff_eventually` in MinimalPrimes/Order/Filter/Germ/Reduced.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Germ/Reduced.lean#L55)
