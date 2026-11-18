---
declaration: section
origin: cited
lean: OAI.ExactDerandomization.exact_logarithmic_space_derandomization
statement: formalized
proof: formalized
---

# 103. Exact derandomization of logarithmic space: $\mathsf L=\mathsf{RL}=\mathsf{BPL}$

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves $\mathsf L=\mathsf{RL}=\mathsf{BPL}$, resolving derandomization for bounded-error logarithmic-space computation. An effective compiler converts each randomized polynomial-time logarithmic-space machine deciding a language with one-sided or two-sided error into a deterministic logarithmic-space decider with explicit polynomial running-time bounds.

## Exact derandomization of logarithmic space: L = RL = BPL

We prove $\mathsf L=\mathsf{RL}=\mathsf{BPL}$, resolving the derandomization problem for polynomial-time randomized logarithmic space.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves $\mathsf L=\mathsf{RL}=\mathsf{BPL}$ for binary languages in an explicit Turing-machine model with logarithmic workspace. The randomized classes use polynomial time: $\mathsf{RL}$ never accepts a no-instance and accepts a yes-instance with probability at least $1/2$, while $\mathsf{BPL}$ has acceptance probability at least $2/3$ on yes-instances and at most $1/3$ on no-instances. Thus bounded-error randomness does not enlarge deterministic logarithmic space in this model.

The selected theorem asserts equality of the language classes. The paper's explicit compiler and numerical running-time bounds are not separately stated in this Comparator target.

## Lean: Exact equality of deterministic and randomized logarithmic space

```lean
theorem exact_logarithmic_space_derandomization :
    L = RL ∧ RL = BPL
```

Stated in [LogspaceEquality.lean, line 136](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LogspaceEquality.lean#L136). Proved in [lean/OAI/Computability/Logspace/Equality.lean, line 104](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/Logspace/Equality.lean#L104). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/103.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/103.md)
