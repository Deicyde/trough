---
declaration: theorem
origin: cited
lean: Filter.Product.noZeroDivisors_iff_eventually
statement: formalized
proof: formalized
---

# No zero divisors in ultrafilter products

For an ultrafilter `U` and an independently universed dependent family `R`,
[`Filter.Product.noZeroDivisors_iff_eventually`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/NoZeroDivisors.lean)
characterizes no zero divisors in the product by eventual no zero divisors in the
fibres. It requires only `Zero` and `Mul` on each fibre and uses the existing
`Con.hasMul` and `Con.zero` operations on the existing product carrier. No
associativity, unit, absorption by zero, addition, commutativity or nontriviality
hypothesis is needed. For monoids with zero,
`Filter.Product.noZeroDivisors_iff` uses the canonical product instances; the
operation-agreement lemmas identify the same zero and multiplication.
The [varying finite client](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/Order/Filter/Product/NoZeroDivisors.lean)
has no zero divisors even though zero is not absorbing.

The [constant-family bridge](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Germ/NoZeroDivisors.lean)
compares the congruence zero and multiplication records with the existing germ
operations for every filter. At an ultrafilter, `Filter.Germ.noZeroDivisors_iff`
therefore characterizes no zero divisors in the germ by no zero divisors in the
value type, still with only `Zero` and `Mul`. The same nonabsorbing client exercises
this specialization. These generic criteria are Mathlib-upstream candidates.

Eventual fibrewise no zero divisors alone does not suffice for arbitrary filters:
at the proper top filter on a two-point index type, complementary nonzero sections
over a domain multiply to zero.

For arbitrary `F`, if each fibre has a **two-sided absorbing zero** (`MulZeroClass`),
`Filter.Product.noZeroDivisors_iff_eventually_and_trace` characterizes no zero divisors
for the same congruence operations by the conjunction of eventual fibrewise no zero
divisors and `D = ⊥ ∨ IsAtom D`, where
`D = F ⊓ principal {i | Nontrivial (R i)}`. Both absorption laws are material; no unit,
associativity, properness or all-fibre nontriviality is required. The trace, not `F`
itself, must be bottom or an atom, and even an atomic trace does not remove the
fibrewise condition. The canonical monoid-with-zero specialization is
`Filter.Product.noZeroDivisors_iff_eventually_and_trace_of_monoidWithZero`.
The [mixed-fibre client](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/Order/Filter/Product/NoZeroDivisors.lean)
uses top on Bool with a natural-number fibre and a singleton fibre: its trace is
`pure false`, so the product has no zero divisors although top is not an ultrafilter.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Filter.Product.noZeroDivisors_iff_eventually` (theorem), declared in [MinimalPrimes/Order/Filter/Product/NoZeroDivisors.lean, line 56](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/NoZeroDivisors.lean#L56).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Filter.Product.noZeroDivisors_iff_eventually` in MinimalPrimes/Order/Filter/Product/NoZeroDivisors.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/NoZeroDivisors.lean#L56)
