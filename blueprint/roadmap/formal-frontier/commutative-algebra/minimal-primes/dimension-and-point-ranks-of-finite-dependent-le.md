---
declaration: theorem
origin: cited
lean: Order.krullDim_toLex_pi, Order.height_toLex_pi, Order.coheight_toLex_pi, Pi.Lex.isStrictOrderOfLT, Pi.Lex.partialOrderOfLT, Pi.Lex.partialOrderOfLT_lt, Pi.Lex.partialOrderOfLT_le_iff, Pi.Lex.partialOrderOfLT_eq
statement: formalized
---

# Dimension and point ranks of finite dependent lexicographic products

For arbitrary subsets of independently universed given preorders over a finite linearly ordered index, lexicographic dimension is the WithBot map of ENat decrement applied to the product of the shifted fibre dimensions. Product and addition are in WithBot ENat, with only the decrement in ENat. Empty index, empty fibres and infinite dimensions are included. The canonical partial order is equality or strict lexicographic comparison with equality prefixes; it needs only strict less-than relations on the fibres and agrees as a whole record with Mathlib's construction when the fibres have partial orders. For a given section of arbitrary given fibre preorders, height and coheight are sums of the original coordinate ranks weighted by the strict-chain vertex heights of whole later fibres. Both use the same original suffix priority. These ENat formulas include empty indices and unattained infinite heights, with no fibre partial-order, linearity, finiteness or extra inhabitation premise.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/formalization.yaml) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Order.krullDim_toLex_pi` (theorem), declared in [MinimalPrimes/Order/KrullDimension.lean, line 1551](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1551).
- `Order.height_toLex_pi` (theorem), declared in [MinimalPrimes/Order/KrullDimension.lean, line 1359](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1359).
- `Order.coheight_toLex_pi` (theorem), declared in [MinimalPrimes/Order/KrullDimension.lean, line 1424](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1424).
- `Pi.Lex.isStrictOrderOfLT` (instance), declared in [MinimalPrimes/Order/PiLex.lean, line 49](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/PiLex.lean#L49).
- `Pi.Lex.partialOrderOfLT` (instance), declared in [MinimalPrimes/Order/PiLex.lean, line 68](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/PiLex.lean#L68).
- `Pi.Lex.partialOrderOfLT_lt` (theorem), declared in [MinimalPrimes/Order/PiLex.lean, line 77](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/PiLex.lean#L77).
- `Pi.Lex.partialOrderOfLT_le_iff` (theorem), declared in [MinimalPrimes/Order/PiLex.lean, line 84](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/PiLex.lean#L84).
- `Pi.Lex.partialOrderOfLT_eq` (theorem), declared in [MinimalPrimes/Order/PiLex.lean, line 91](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/PiLex.lean#L91).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: formalization.yaml](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/formalization.yaml)
- [Source of `Order.krullDim_toLex_pi` in MinimalPrimes/Order/KrullDimension.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1551)
- [Source of `Order.height_toLex_pi` in MinimalPrimes/Order/KrullDimension.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1359)
- [Source of `Order.coheight_toLex_pi` in MinimalPrimes/Order/KrullDimension.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1424)
- [Source of `Pi.Lex.isStrictOrderOfLT` in MinimalPrimes/Order/PiLex.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/PiLex.lean#L49)
- [Source of `Pi.Lex.partialOrderOfLT` in MinimalPrimes/Order/PiLex.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/PiLex.lean#L68)
- [Source of `Pi.Lex.partialOrderOfLT_lt` in MinimalPrimes/Order/PiLex.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/PiLex.lean#L77)
- [Source of `Pi.Lex.partialOrderOfLT_le_iff` in MinimalPrimes/Order/PiLex.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/PiLex.lean#L84)
- [Source of `Pi.Lex.partialOrderOfLT_eq` in MinimalPrimes/Order/PiLex.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/PiLex.lean#L91)
