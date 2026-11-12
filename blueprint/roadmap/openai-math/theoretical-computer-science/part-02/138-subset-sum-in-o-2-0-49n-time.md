---
declaration: section
origin: cited
---

# 138. Subset Sum in $O(2^{0.49n})$ time

2 manuscripts, with no Lean, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Gives a uniform randomized classical algorithm for worst-case Subset Sum in ordinary $O(2^{0.49n})$ word-RAM time on polynomial-bit inputs, where *n* counts the integers. The time bound holds on every execution and success probability is at least 2/3 on every input. Inputs may repeat positive integers; words have $O(n+b)$ bits for maximum input bit length *b*.

## Subset Sum in Time $O(2^{0.49n})$

We give a uniform randomized classical algorithm for Subset Sum with bounded error and worst-case running time $O(2^{0.49n})$ on polynomial-bit inputs in a word-RAM model, where *n* is the number of input integers. The time bound holds on every random execution.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/subset-sum.pdf).

## A Low-Space Algorithm for Worst-Case Subset Sum

We give a uniform classical randomized decision algorithm for worst-case Subset Sum. Under every fixed polynomial bound on input-integer bit length, it uses $\mathop{\mathrm{poly}}\nolimits (n)2^{n/2}$ time and ordinary $O(2^{n/5})$ writable words of $O(n+b)$ bits, where *b* is the largest input bit length. Both resource bounds hold on every execution. The error is one-sided: the algorithm always rejects unsolvable instances and accepts each solvable instance with probability at least 2/3.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/paper.pdf).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
