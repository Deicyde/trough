---
declaration: section
origin: cited
lean: OAI.AsymptoticallyMinimalLittlewood.main, OAI.AsymptoticallyMinimalLittlewoodFiniteFlatness.main
statement: formalized
proof: formalized
---

# 076. Real ultraflat Littlewood polynomials and unbounded binary merit factors

3 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs polynomials with *N* consecutive coefficients in $\{-1,1\}$ whose modulus is $(1+o(1))\sqrt N$ uniformly on the entire unit circle, for every sufficiently large integer length *N*. Thus real Littlewood polynomials are ultraflat, including at the real endpoints. Their binary merit factors tend to infinity, disproving Turyn's bounded-merit-factor conjecture.

## Ultraflat real Littlewood polynomials

For every $\varepsilon\in(0,1)$ and every sufficiently large integer *N*, there is a polynomial of length *N* with coefficients in $\{-1,1\}$ whose modulus lies between $(1-\varepsilon)\sqrt N$ and $(1+\varepsilon)\sqrt N$ everywhere on the unit circle. Thus real Littlewood polynomials can be ultraflat through every sufficiently large integer length. The signs may be chosen separately at each length.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/ultraflat-real-littlewood-polynomials.pdf).

## Nearly minimal maxima and positive minima of Littlewood polynomials

For every *η* > 0 and every sufficiently large integer *N*, there is a polynomial with *N* consecutive coefficients in $\{-1,1\}$ whose modulus lies between $\sqrt N/16$ and $(1+\eta)\sqrt N$ everywhere on the unit circle.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/littlewood-lower-envelope.pdf).

## Asymptotically minimal maxima of real Littlewood polynomials

We prove that the minimum possible maximum modulus on the unit circle of a polynomial with *N* consecutive real coefficients in $\{-1,1\}$ is $(1+o(1))\sqrt N$, as *N* tends to infinity through all integers. This disproves the real-sign analogue of Erdős's fixed relative-gap conjecture. As a consequence, the largest binary merit factor at length *N* tends to infinity through all integer lengths, disproving Turyn's conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization gives real Littlewood polynomials of every sufficiently large length whose maximum modulus on the unit circle is at most $(1+\eta)\sqrt N$ for any fixed $\eta>0$. Thus the smallest possible maximum is asymptotically minimal through all integer lengths.

A further statement chooses one family of real sign polynomials for all lengths such that, for every fixed finite $p>0$, the $L^p$ mean of $\bigl||P_N(z)|/\sqrt N-1\bigr|$ on the unit circle tends to zero. The results are existential and do not give an effective convergence rate or a signing algorithm.

## Lean: Asymptotically minimal Littlewood maximum

```lean
theorem main : MainStatement
```

Stated in [AsymptoticallyMinimalLittlewood.lean, line 18](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/AsymptoticallyMinimalLittlewood.lean#L18). Proved in [lean/OAI/Analysis/Littlewood/Main.lean, line 187](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Littlewood/Main.lean#L187). formalization.yaml lists it as one of the repository's main results.

## Lean: Finite-exponent flatness of one all-length Littlewood family

```lean
theorem main : MainStatement
```

Stated in [LittlewoodFiniteFlatness.lean, line 34](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LittlewoodFiniteFlatness.lean#L34). Proved in [lean/OAI/Analysis/Littlewood/FiniteFlatness.lean, line 14](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Littlewood/FiniteFlatness.lean#L14).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/076.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/076.md)
