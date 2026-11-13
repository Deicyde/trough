---
declaration: section
origin: cited
lean: OAI.ExactFourier.main_theorem, OAI.PowerSaving.transform_main, OAI.PowerSaving.convolution_main
statement: formalized
proof: formalized
---

# 130. Exact Fourier transforms below $n\log n$

2 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Gives a deterministic length-*n* discrete Fourier transform algorithm using $O(n(\log n)^{1-\delta})$ operations for every *n*, with explicit $\delta=10^{-13}$. The model uses exact complex arithmetic, unrestricted coefficients and a supplied root of unity, and counts scalar preparation and logarithmic-word indexing.

## An explicit power saving for the exact discrete Fourier transform

We give a deterministic algorithm that computes the discrete Fourier transform at every length *n* in $O(n(\log n)^{1-10^{-13}})$ operations. The model uses exact complex arithmetic, unrestricted coefficients, specified Fourier roots, and unit-cost logarithmic-size indexing; scalar preparation and array organization are included.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/main.pdf); the Lean below formalizes results from it.

## Finite tensor savings and exact Fourier circuits

We construct exact nonuniform Fourier circuits of size $o(n\log n)$ along an unbounded sequence of lengths, counting every addition, subtraction, and scalar multiplication. This refutes the $\Omega(n\log n)$ lower bound in the unrestricted complex linear-circuit model. The construction uses a finite tensor saving: a tensor power of some invertible nonmonomial complex matrix can be computed with fewer matrix calls than the standard tensor-axis algorithm on the same coordinates, when invertible monomial maps are allowed freely between calls.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result gives exact discrete Fourier transforms with arbitrarily small normalized circuit cost along an unbounded sequence of lengths. For every $c>0$ and every cutoff $N_0\ge2$, some $n\ge N_0$ has a circuit computing the unnormalized DFT with fewer than $cn\log_2 n$ gates. Addition, subtraction, and multiplication by a predetermined complex scalar each cost one gate; diagonal scalings are charged. The result is subsequential, with no all-length, bounded-coefficient, conditioning, or bit-complexity claim.

A separate uniform formalization gives fixed deterministic programs for every positive length $n$, computing the canonical discrete Fourier transform and the full convolution of two length-$n$ complex vectors exactly. Their work is $O(n(\log n)^{1-10^{-13}})=o(n\log n)$, including root-order selection and scalar preparation. The chosen root of unity is supplied; the model permits exact complex arithmetic and unrestricted coefficients, while integer values and indices remain polynomially bounded in $n$. The synthesis appendix's extraction, search, and printer uniformization is outside these selected statements.

## Lean: Subsequential savings for exact Fourier circuits

```lean
theorem main_theorem : MainStatement
```

Stated in [ExactFourier.lean, line 57](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ExactFourier.lean#L57). Proved in [lean/OAI/Computability/FourierCircuit/Main.lean, line 277](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/FourierCircuit/Main.lean#L277). formalization.yaml lists it as one of the repository's main results.

## Lean: Uniform exact DFT and convolution with a power saving

```lean
theorem transform_main : DFTGoal
```

Stated in [UniformFourier.lean, line 326](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/UniformFourier.lean#L326). Proved in [lean/OAI/Computability/FourierTransform/Main.lean, line 137](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/FourierTransform/Main.lean#L137). formalization.yaml lists it as one of the repository's main results.

```lean
theorem convolution_main : ConvGoal
```

Stated in [UniformFourier.lean, line 330](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/UniformFourier.lean#L330). Proved in [lean/OAI/Computability/FourierTransform/Main.lean, line 141](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/FourierTransform/Main.lean#L141). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/130.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/130.md)
