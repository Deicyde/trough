---
declaration: section
origin: cited
lean: OAI.SharpRamseyFive.main, OAI.SharpLogRamsey.main
statement: formalized
proof: formalized
---

# 170. Sharp logarithmic exponents for off-diagonal Ramsey numbers

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For every fixed integer *s* ≥ 5, proves $r(s,t)=t^{s-1}/(\log t)^{s-2+o(1)}$ as $t\to\infty$, determining the logarithmic exponent and matching the classical upper bound at that scale. Here $r(s,t)$ is the least number of vertices forcing an *s*-clique or a *t*-vertex independent set.

## The sharp logarithmic exponent of r(5,t)

We determine the sharp logarithmic exponent of the off-diagonal Ramsey number $r(5,t)$:

$\displaystyle r(5,t)=\frac{t^4}{(\log t)^{3+o(1)}} \qquad (t\longrightarrow\infty).$

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Sharp-Logarithmic-Exponent-of-r-5-t-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## Sharp logarithmic exponents for fixed off-diagonal Ramsey numbers

For every fixed integer *s* ≥ 6, we determine the sharp logarithmic exponent of the off-diagonal Ramsey number:

$\displaystyle r(s,t)=\frac{t^{s-1}}{(\log t)^{s-2+o(1)}} \qquad (t\longrightarrow\infty).$

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-Logarithmic-Exponents-for-Fixed-Off-Diagonal-Ramsey-Numbers-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization determines the sharp logarithmic exponent of the off-diagonal Ramsey number $r(5,t)$. It proves
$r(5,t)=t^4/(\log t)^{3+o(1)}$ as $t\to\infty$.
For every $\varepsilon>0$, the lower bound $t^4/(\log t)^{3+\varepsilon}$ holds eventually, while the upper bound is $Ct^4/(\log t)^3$ for an absolute $C>0$. The corresponding logarithmic exponent converges to three along all natural values of $t$.

The formalization determines the sharp logarithmic exponent of the off-diagonal Ramsey number for every fixed integer $s\ge6$. It proves
$r(s,t)=t^{s-1}/(\log t)^{s-2+o(1)}$ as $t\to\infty$.
More explicitly, for each $\varepsilon>0$ the lower bound $t^{s-1}/(\log t)^{s-2+\varepsilon}$ holds eventually, while the upper bound is $C_s t^{s-1}/(\log t)^{s-2}$. The logarithmic exponent limit is taken along all natural values of $t$.

## Lean: Sharp logarithmic exponent of $r(5,t)$

Stated in [RamseyFive.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/RamseyFive.lean).

```lean
theorem main : SharpBounds ∧ SharpExponent
```

Proved in [lean/OAI/Combinatorics/RamseyFive/Main.lean, line 27](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/RamseyFive/Main.lean#L27).

## Lean: Sharp logarithmic exponent for fixed off-diagonal Ramsey numbers

Stated in [SharpLogRamsey.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SharpLogRamsey.lean).

```lean
theorem main (s : ℕ) (hs : 6 ≤ s) : MainBounds s ∧ MainLimit s
```

Proved in [lean/OAI/Combinatorics/SharpRamsey/Main.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/SharpRamsey/Main.lean#L12).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/170.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/170.md)
