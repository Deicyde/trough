---
declaration: module
origin: cited
lean: DMChannel, DMChannel.on_fin, DMChannel.on_list
statement: formalized
proof: formalized
---

# QuantumInfo.ClassicalInfo.Channel

The module `QuantumInfo.ClassicalInfo.Channel`, [QuantumInfo/ClassicalInfo/Channel.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Channel.lean): 3 declarations, 3 with a docstring.

**`DMChannel`**, a structure, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Channel.lean#L54).

> Discrete Memoryless Channel. Each input symbol `I` has a corresponding
> output distribution `Distribution O`, and this process is applied
> independently on each symbol in the list.

```lean
structure DMChannel where
  symb_dist : I → ProbDistribution O
```

**`DMChannel.on_fin`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Channel.lean#L60).

> Apply a discrete memoryless channel to an n-character string.

```lean
def on_fin (C : DMChannel I O) {n : ℕ} (is : Fin n → I) : ProbDistribution (Fin n → O)
```

**`DMChannel.on_list`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Channel.lean#L71).

> Apply a discrete memoryless channel to a list.

```lean
def on_list (C : DMChannel I O) (is : List I) : ProbDistribution (Fin (is.length) → O)
```

## Depends on

- [Distributions on finite sets](distribution.md)

## Sources

- [QuantumInfo/ClassicalInfo/Channel.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Channel.lean)
