---
declaration: section
origin: cited
lean: OAI.LeanBlast.GotsmanLinial.gotsmanLinialStatement
statement: formalized
proof: formalized
---

# 127. Average sensitivity of polynomial threshold functions

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that a degree-at-most-*d* polynomial threshold function on the uniform *n*-dimensional Boolean cube has average sensitivity at most $8d\sqrt n$, uniformly for $1\le d\le n$. Average sensitivity counts expected output changes under single-bit flips. This establishes the asymptotic Gotsman–Linial conjecture, allowing polynomial zeros with $\mathop{\mathrm{sign}}\nolimits (0)=1$.

## Average sensitivity of polynomial threshold functions

For every *n* ≥ 1 and $1\le d\le n$, we prove that a polynomial threshold function of degree at most *d* on the uniform Boolean cube has average sensitivity at most $8d\sqrt n$. This proves the asymptotic form of the Gotsman–Linial conjecture. The bound is uniform in both parameters and uses the convention $\mathop{\mathrm{sgn}}\nolimits (0)=1$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result proves the average-sensitivity bound $8d\sqrt n$ for every Boolean threshold function defined by a real multilinear polynomial of degree at most $d$ on the $n$-dimensional cube. The sign convention assigns value $1$ at zero. This establishes the stated asymptotic bound, rather than the separate conjecture identifying exact extremizers.

## Lean: Average sensitivity of polynomial threshold functions

Stated in [GotsmanLinial.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GotsmanLinial.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem gotsmanLinialStatement : GotsmanLinialStatement
```

Proved in [lean/OAI/Combinatorics/GotsmanLinial/Main.lean, line 123](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/GotsmanLinial/Main.lean#L123).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/127.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/127.md)
