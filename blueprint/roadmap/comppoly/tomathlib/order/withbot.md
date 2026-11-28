---
catalog: module
lean: WithBot.add_lt_add
statement: formalized
proof: formalized
---

# Strict additive monotonicity on `WithBot ℕ`

`CompPoly.ToMathlib.Order.WithBot`, in [CompPoly/ToMathlib/Order/WithBot.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Order/WithBot.lean), by Juan Conejero.

> Mathlib's `WithBot.add_lt_add_of_le_of_lt` / `WithBot.add_lt_add_of_lt_of_le` carry `≠ ⊥`
> side conditions; the fully strict version below needs none of them over `ℕ`.
> Upstreaming candidate.

`WithBot.add_lt_add` (lemma, [line 23](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Order/WithBot.lean#L23))

> Strict monotonicity of `+` on `WithBot ℕ`: `a < b → c < d → a + c < b + d`.

```lean
lemma add_lt_add {a b c d : WithBot ℕ} (h1 : a < b) (h2 : c < d) : a + c < b + d
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/ToMathlib/Order/WithBot.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Order/WithBot.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.ToMathlib.Order.WithBot.json)
