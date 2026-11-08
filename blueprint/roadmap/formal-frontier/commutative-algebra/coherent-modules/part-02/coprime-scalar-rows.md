---
declaration: theorem
origin: cited
lean: IsCoprime.existsUnique_smul_eq_pair
statement: formalized
proof: formalized
---

# Coprime scalar rows

For a commutative semiring `S`, an additive
commutative `S`-semimodule `M`, and Bézout-coprime scalars `a`, `b`,
[`IsCoprime.existsUnique_smul_eq_pair`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/Coprime.lean)
gives a unique `k` with `a • k = x` and `b • k = y` whenever
`b • x = a • y`. The companion `smul_mem_range_smul_iff` reflects
membership in the range of multiplication by `a` after multiplying by `b`.
The two universes are independent; no subtraction, additive cancellation,
nontriviality or finiteness is assumed.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `IsCoprime.existsUnique_smul_eq_pair` (theorem), declared in [CoherentModules/Algebra/Module/Coprime.lean, line 80](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/Coprime.lean#L80).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `IsCoprime.existsUnique_smul_eq_pair` in CoherentModules/Algebra/Module/Coprime.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/Coprime.lean#L80)
