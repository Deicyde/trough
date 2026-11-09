---
declaration: theorem
origin: cited
lean: MonochromaticQuantumGraph.eqSystem4_no_solution_nnreal_ge4, MonochromaticQuantumGraph.eqSystem_no_solution_nnreal_even_ge6_ge3, MonochromaticQuantumGraph.eqSystem_no_solution_even_ge4_d_eq_n_explicit, MonochromaticQuantumGraph.eqSystem4_no_solution_d4, MonochromaticQuantumGraph.eqSystem4_no_solution_ge4, MonochromaticQuantumGraph.eqSystem6_no_solution_d3, MonochromaticQuantumGraph.eqSystem6_no_solution_d4, MonochromaticQuantumGraph.eqSystem6_no_solution_d5, MonochromaticQuantumGraph.eqSystem6_no_solution_d6, MonochromaticQuantumGraph.eqSystem6_no_solution_ge3, MonochromaticQuantumGraph.eqSystem8_no_solution_d3, MonochromaticQuantumGraph.eqSystem8_no_solution_d10, MonochromaticQuantumGraph.eqSystem10_no_solution_d3, MonochromaticQuantumGraph.eqSystem10_no_solution_d4, MonochromaticQuantumGraph.eqSystem10_no_solution_d5, MonochromaticQuantumGraph.eqSystem10_no_solution_d6, MonochromaticQuantumGraph.eqSystem10_no_solution_d7, MonochromaticQuantumGraph.eqSystem10_no_solution_d8, MonochromaticQuantumGraph.eqSystem10_no_solution_d9, MonochromaticQuantumGraph.eqSystem10_no_solution_d10, MonochromaticQuantumGraph.eqSystem12_no_solution_d3, MonochromaticQuantumGraph.eqSystem14_no_solution_d3, MonochromaticQuantumGraph.eqSystem16_no_solution_d3, MonochromaticQuantumGraph.eqSystem_no_solution_ge6_ge3, MonochromaticQuantumGraph.eqSystem4_no_solution_ge4_real, MonochromaticQuantumGraph.eqSystem6_no_solution_d3_real, MonochromaticQuantumGraph.eqSystem6_no_solution_d5_real, MonochromaticQuantumGraph.eqSystem6_no_solution_ge3_real, MonochromaticQuantumGraph.eqSystem8_no_solution_d3_real, MonochromaticQuantumGraph.eqSystem10_no_solution_d3_real, MonochromaticQuantumGraph.eqSystem_no_solution_ge6_ge3_real, MonochromaticQuantumGraph.eqSystem4_no_solution_ge4_int, MonochromaticQuantumGraph.eqSystem6_no_solution_d3_int, MonochromaticQuantumGraph.eqSystem6_no_solution_d5_int, MonochromaticQuantumGraph.eqSystem6_no_solution_ge3_int, MonochromaticQuantumGraph.eqSystem8_no_solution_d3_int, MonochromaticQuantumGraph.eqSystem10_no_solution_d3_int, MonochromaticQuantumGraph.eqSystem_no_solution_ge6_ge3_int, MonochromaticQuantumGraph.eqSystem4_no_solution_ge4_trinary_int, MonochromaticQuantumGraph.eqSystem6_no_solution_d3_trinary_int, MonochromaticQuantumGraph.eqSystem6_no_solution_d5_trinary_int, MonochromaticQuantumGraph.eqSystem6_no_solution_ge3_trinary_int, MonochromaticQuantumGraph.eqSystem8_no_solution_d3_trinary_int, MonochromaticQuantumGraph.eqSystem10_no_solution_d3_trinary_int, MonochromaticQuantumGraph.eqSystem_no_solution_ge6_ge3_trinary_int
statement: formalized
---

# Monochromatic quantum graphs (inherited vertex colorings)

> This file studies the existence of *monochromatic quantum graphs*: edge-coloured, edge-weighted
> complete graphs whose perfect matchings induce vertex colourings, with the property that
>
> - every **non-monochromatic** inherited vertex colouring has total weight `0`, while
> - each of the `D` **monochromatic** colourings has total weight `1`.
>
> In the quantum-optics motivation, such a construction corresponds to generating high-dimensional
> multipartite GHZ-type states using probabilistic pair sources and linear optics (without additional
> resources), where interference patterns can be expressed as weighted sums over perfect matchings.
>
> ## Main questions (informal)
>
> - For `N = 4` and `D ≥ 4`, does there exist such a graph/weighting?
> - For even `N ≥ 6` and `D ≥ 3`, does there exist such a graph/weighting?
>
> ## Formalisation sketch
>
> A quantum graph with `N` vertices and `D` colours can be encoded by a weight function
> `W : EdgeN N D α → α` (for a coefficient domain `α`).
>
> For each assignment of vertex indices `ι : V N → Fin D`, we define a perfect-matching sum
> `pmSumN N D W ι` (a sum over perfect matchings, where each matching contributes the product of the
> corresponding edge weights determined by `ι`). The equation system `EqSystemN N D W` requires
>
> `pmSumN N D W ι = 1` iff `ι` is constant (all entries equal), and `0` otherwise.
>
> The open conjectures in this file ask for non-existence/existence of such `W` over various
> coefficient domains (e.g. `ℂ`, `ℝ`, `ℤ`, and restricted integer weights).
>
> ## References
>
> * [Krenn2017] M. Krenn, X. Gu, A. Zeilinger,
>   "Quantum Experiments and Graphs: Multiparty States as Coherent Superpositions of Perfect Matchings",
>   *Physical Review Letters* 119(24), 240403 (2017).
>
> * [MO2018] [Vertex coloring inherited from perfect matchings (motivated by quantum physics)](https://mathoverflow.net/questions/311325),
>   MathOverflow question 311325.
>
> * [Gu2019] X. Gu, M. Erhard, A. Zeilinger, M. Krenn,
>   "Quantum experiments and graphs II: Quantum interference, computation, and state generation",
>   *PNAS* 116(10), 4147–4155 (2019).
>
> * [Krenn2019] [Questions on the Structure of Perfect Matchings inspired by Quantum Physics](https://arxiv.org/abs/1902.06023)
>   by *M. Krenn, X. Gu, U. Soltész*,
>   Proc. 2nd Croatian Combinatorial Days, 57–70 (2019).
>
> * [Chandran2022] [Edge-coloured graphs with only monochromatic perfect matchings and their connection to quantum physics](https://arxiv.org/abs/2202.05562)
>   by *N. Chandran, S. Gajjala* (2022).
>
> * [Chandran2024] [Krenn–Gu conjecture for sparse graphs](https://arxiv.org/abs/2407.00303)
>   by *N. Chandran, S. Gajjala, S. Illickan, M. Krenn*, MFCS 2024.
>
> * [Ki26] [A solver-free Lean 4 proof of the sharp bound $D \le N - 2$ for monochromatic quantum
>   graph equation systems over integral domains](https://github.com/KitaKen1/monochromatic-quantum-graph-sharp-bound-lean/tree/6c5340384479dbb36129b2e0084449be2458cce2),
>   commit `6c534038`.
>
> * [Ki26b] [A solver-free Lean 4 proof that the monochromatic quantum graph equation system has no
>   solution for $N = 10$ and $D = 8$ over integral domains](https://github.com/KitaKen1/monochromatic-quantum-graph-n10-d8-lean/tree/a9309005c7a27a2615f8e7eebef7a1db017809ab),
>   commit `a9309005`.

*Quoted from [FormalConjectures/Paper/MonochromaticQuantumGraph.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 45 research or textbook statements: 16 open and 29 solved. It also has 3 test statements, counted here but not shown.

## `MonochromaticQuantumGraph.eqSystem4_no_solution_nnreal_ge4`

Solved: stated here without proof.

> Bogdanov: for $N = 4$ and all $D \geq 4$, no solution exists over $\mathbb{R}_{\geq 0}$.

```lean
theorem eqSystem4_no_solution_nnreal_ge4 :
    ∀ D : Nat, D ≥ 4 →
      ¬ ∃ W : WeightsN 4 D ℝ≥0, EqSystemN 4 D W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 346](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L346).

## `MonochromaticQuantumGraph.eqSystem_no_solution_nnreal_even_ge6_ge3`

Solved: stated here without proof.

> Bogdanov: for all even $N \geq 6$ and $D \geq 3$, no solution exists over $\mathbb{R}_{\geq 0}$.

```lean
theorem eqSystem_no_solution_nnreal_even_ge6_ge3 :
    ∀ N D : Nat,
      N ≥ 6 → Even N → D ≥ 3 →
        ¬ ∃ W : WeightsN N D ℝ≥0, EqSystemN N D W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 353](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L353).

## `MonochromaticQuantumGraph.eqSystem_no_solution_even_ge4_d_eq_n_explicit`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/af88acbf9da0f26e3e934743a819e986e02f6875/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L1006](https://github.com/google-deepmind/formal-conjectures/blob/af88acbf9da0f26e3e934743a819e986e02f6875/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L1006).

> For all even $N \geq 4$ and $D = N$, does there exist no solution to the monochromatic quantum
> graph equation system over $\mathbb{C}$?
>
> The DeepMind prover agent has found a formal proof for this statement.

```lean
theorem eqSystem_no_solution_even_ge4_d_eq_n_explicit :
    ∀ N : Nat, N ≥ 4 → Even N →
      ¬ ∃ W : WeightsN N N ℂ, EqSystemN N N W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 383](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L383).

## `MonochromaticQuantumGraph.eqSystem4_no_solution_d4`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/af88acbf9da0f26e3e934743a819e986e02f6875/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L1021](https://github.com/google-deepmind/formal-conjectures/blob/af88acbf9da0f26e3e934743a819e986e02f6875/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L1021).

> For $N = 4$ and $D = 4$, does there exist no solution to the monochromatic quantum
> graph equation system over $\mathbb{C}$?
>
> This is the $D = N$ case, proved using `eqSystem_no_solution_even_ge4_d_eq_n_explicit`.

```lean
theorem eqSystem4_no_solution_d4 :
    ¬ ∃ W : WeightsN 4 4 ℂ, EqSystemN 4 4 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 395](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L395).

## `MonochromaticQuantumGraph.eqSystem4_no_solution_ge4`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/4854c7233c58a7dce45fdd58b1826abf2c9c1a0f/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L549](https://github.com/mo271/formal-conjectures/blob/4854c7233c58a7dce45fdd58b1826abf2c9c1a0f/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L549).

> For $N = 4$ and all $D \geq 4$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?
>
> The DeepMind prover agent has found a formal proof of this statement.

```lean
theorem eqSystem4_no_solution_ge4 :
    ∀ D : Nat, D ≥ 4 →
      ¬ ∃ W : WeightsN 4 D ℂ, EqSystemN 4 D W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 408](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L408).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_d3`

Solved: stated here; a Lean proof is at [https://github.com/algal/krenn-gu-6x3-certificate/blob/c04696e515e0c02be140353fb52ea60c62e827b1/KrennGuCertificate/Unrestricted.lean#L201-L222](https://github.com/algal/krenn-gu-6x3-certificate/blob/c04696e515e0c02be140353fb52ea60c62e827b1/KrennGuCertificate/Unrestricted.lean#L201-L222).

> For $N = 6$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?
>
> A complete Lean 4 proof is available in the linked external certificate repository.

```lean
theorem eqSystem6_no_solution_d3 :
    ¬ ∃ W : WeightsN 6 3 ℂ, EqSystemN 6 3 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 422](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L422).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_d4`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graph-n6-d4-lean/blob/7d30141a19714986d6f9e632314fd880c9a1e86e/lean/QuantumCR/FormalConjecturesWrapper.lean#L30-L37](https://github.com/KitaKen1/monochromatic-quantum-graph-n6-d4-lean/blob/7d30141a19714986d6f9e632314fd880c9a1e86e/lean/QuantumCR/FormalConjecturesWrapper.lean#L30-L37).

> For $N = 6$ and $D = 4$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?

```lean
theorem eqSystem6_no_solution_d4 :
    ¬ ∃ W : WeightsN 6 4 ℂ, EqSystemN 6 4 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 433](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L433).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_d5`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graph-sharp-bound-lean/blob/6c5340384479dbb36129b2e0084449be2458cce2/lean/QuantumCR/FormalConjecturesWrappers.lean#L55-L62](https://github.com/KitaKen1/monochromatic-quantum-graph-sharp-bound-lean/blob/6c5340384479dbb36129b2e0084449be2458cce2/lean/QuantumCR/FormalConjecturesWrappers.lean#L55-L62).

> For $N = 6$ and $D = 5$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?
>
> The sharp bound $D \le N - 2$ over an integral domain [Ki26] settles this: here $D = N - 1$.

```lean
theorem eqSystem6_no_solution_d5 :
    ¬ ∃ W : WeightsN 6 5 ℂ, EqSystemN 6 5 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 445](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L445).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_d6`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/af88acbf9da0f26e3e934743a819e986e02f6875/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L1074](https://github.com/google-deepmind/formal-conjectures/blob/af88acbf9da0f26e3e934743a819e986e02f6875/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L1074).

> For $N = 6$ and $D = 6$, does there exist no solution to the monochromatic quantum
> graph equation system over $\mathbb{C}$?
>
> This follows from `eqSystem_no_solution_even_ge4_d_eq_n_explicit`.

```lean
theorem eqSystem6_no_solution_d6 :
    ¬ ∃ W : WeightsN 6 6 ℂ, EqSystemN 6 6 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 457](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L457).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_ge3`

Open: stated without proof.

> For $N = 6$ and all $D \geq 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?

```lean
theorem eqSystem6_no_solution_ge3 :
    ∀ D : Nat, D ≥ 3 →
      ¬ ∃ W : WeightsN 6 D ℂ, EqSystemN 6 D W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 464](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L464).

## `MonochromaticQuantumGraph.eqSystem8_no_solution_d3`

Open: stated without proof.

> For $N = 8$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?

```lean
theorem eqSystem8_no_solution_d3 :
    ¬ ∃ W : WeightsN 8 3 ℂ, EqSystemN 8 3 W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 472](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L472).

## `MonochromaticQuantumGraph.eqSystem8_no_solution_d10`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/2cc6df2e95835d759caedb15e36b70025b2eae2c/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L853](https://github.com/mo271/formal-conjectures/blob/2cc6df2e95835d759caedb15e36b70025b2eae2c/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L853).

> For $N = 8$ and $D = 10$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?
>
> The DeepMind prover agent has found a formal proof of this statement.

```lean
theorem eqSystem8_no_solution_d10 :
    ¬ ∃ W : WeightsN 8 10 ℂ, EqSystemN 8 10 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 484](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L484).

## `MonochromaticQuantumGraph.eqSystem10_no_solution_d3`

Open: stated without proof.

> For $N = 10$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?

```lean
theorem eqSystem10_no_solution_d3 :
    ¬ ∃ W : WeightsN 10 3 ℂ, EqSystemN 10 3 W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 491](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L491).

## `MonochromaticQuantumGraph.eqSystem10_no_solution_d4`

Open: stated without proof.

> For $N = 10$ and $D = 4$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?

```lean
theorem eqSystem10_no_solution_d4 :
    ¬ ∃ W : WeightsN 10 4 ℂ, EqSystemN 10 4 W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 498](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L498).

## `MonochromaticQuantumGraph.eqSystem10_no_solution_d5`

Open: stated without proof.

> For $N = 10$ and $D = 5$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?

```lean
theorem eqSystem10_no_solution_d5 :
    ¬ ∃ W : WeightsN 10 5 ℂ, EqSystemN 10 5 W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 505](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L505).

## `MonochromaticQuantumGraph.eqSystem10_no_solution_d6`

Open: stated without proof.

> For $N = 10$ and $D = 6$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?

```lean
theorem eqSystem10_no_solution_d6 :
    ¬ ∃ W : WeightsN 10 6 ℂ, EqSystemN 10 6 W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 512](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L512).

## `MonochromaticQuantumGraph.eqSystem10_no_solution_d7`

Open: stated without proof.

> For $N = 10$ and $D = 7$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?

```lean
theorem eqSystem10_no_solution_d7 :
    ¬ ∃ W : WeightsN 10 7 ℂ, EqSystemN 10 7 W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 519](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L519).

## `MonochromaticQuantumGraph.eqSystem10_no_solution_d8`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graph-n10-d8-lean/blob/a9309005c7a27a2615f8e7eebef7a1db017809ab/lean/QuantumGraphTenEightFC.lean#L5466-L5473](https://github.com/KitaKen1/monochromatic-quantum-graph-n10-d8-lean/blob/a9309005c7a27a2615f8e7eebef7a1db017809ab/lean/QuantumGraphTenEightFC.lean#L5466-L5473).

> For $N = 10$ and $D = 8$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?
>
> The sharp bound $D \le N - 2$ of [Ki26] does not cover this equality case $D = N - 2$; it is
> settled over an integral domain in [Ki26b].

```lean
theorem eqSystem10_no_solution_d8 :
    ¬ ∃ W : WeightsN 10 8 ℂ, EqSystemN 10 8 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 532](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L532).

## `MonochromaticQuantumGraph.eqSystem10_no_solution_d9`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graph-sharp-bound-lean/blob/6c5340384479dbb36129b2e0084449be2458cce2/lean/QuantumCR/FormalConjecturesWrappers.lean#L73-L80](https://github.com/KitaKen1/monochromatic-quantum-graph-sharp-bound-lean/blob/6c5340384479dbb36129b2e0084449be2458cce2/lean/QuantumCR/FormalConjecturesWrappers.lean#L73-L80).

> For $N = 10$ and $D = 9$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?
>
> The sharp bound $D \le N - 2$ over an integral domain [Ki26] settles this: here $D = N - 1$.

```lean
theorem eqSystem10_no_solution_d9 :
    ¬ ∃ W : WeightsN 10 9 ℂ, EqSystemN 10 9 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 543](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L543).

## `MonochromaticQuantumGraph.eqSystem10_no_solution_d10`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/af88acbf9da0f26e3e934743a819e986e02f6875/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L1167](https://github.com/google-deepmind/formal-conjectures/blob/af88acbf9da0f26e3e934743a819e986e02f6875/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L1167).

> For $N = 10$ and $D = 10$, does there exist no solution to the monochromatic quantum
> graph equation system over $\mathbb{C}$?
>
> This follows from the $D = N$ case, see `eqSystem_no_solution_even_ge4_d_eq_n_explicit`.

```lean
theorem eqSystem10_no_solution_d10 :
    ¬ ∃ W : WeightsN 10 10 ℂ, EqSystemN 10 10 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 554](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L554).

## `MonochromaticQuantumGraph.eqSystem12_no_solution_d3`

Open: stated without proof.

> For $N = 12$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?

```lean
theorem eqSystem12_no_solution_d3 :
    ¬ ∃ W : WeightsN 12 3 ℂ, EqSystemN 12 3 W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 561](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L561).

## `MonochromaticQuantumGraph.eqSystem14_no_solution_d3`

Open: stated without proof.

> For $N = 14$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?

```lean
theorem eqSystem14_no_solution_d3 :
    ¬ ∃ W : WeightsN 14 3 ℂ, EqSystemN 14 3 W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 568](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L568).

## `MonochromaticQuantumGraph.eqSystem16_no_solution_d3`

Open: stated without proof.

> For $N = 16$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{C}$?

```lean
theorem eqSystem16_no_solution_d3 :
    ¬ ∃ W : WeightsN 16 3 ℂ, EqSystemN 16 3 W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 575](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L575).

## `MonochromaticQuantumGraph.eqSystem_no_solution_ge6_ge3`

Open: stated without proof.

> For all even $N \geq 6$ and $D \geq 3$, does there exist no solution to the monochromatic
> quantum graph equation system over $\mathbb{C}$?

```lean
theorem eqSystem_no_solution_ge6_ge3 :
    ∀ N D : Nat, N ≥ 6 → Even N → D ≥ 3 →
      ¬ ∃ W : WeightsN N D ℂ, EqSystemN N D W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 584](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L584).

## `MonochromaticQuantumGraph.eqSystem4_no_solution_ge4_real`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/4854c7233c58a7dce45fdd58b1826abf2c9c1a0f/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L738](https://github.com/mo271/formal-conjectures/blob/4854c7233c58a7dce45fdd58b1826abf2c9c1a0f/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L738).

> For $N = 4$ and all $D \geq 4$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{R}$?
>
> This follows from the solution of the complex version of the problem
> (see `eqSystem4_no_solution_ge4`)

```lean
theorem eqSystem4_no_solution_ge4_real :
    ∀ D : Nat, D ≥ 4 →
      ¬ ∃ W : WeightsN 4 D ℝ, EqSystemN 4 D W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 601](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L601).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_d3_real`

Open: stated without proof.

> For $N = 6$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{R}$?

```lean
theorem eqSystem6_no_solution_d3_real :
    ¬ ∃ W : WeightsN 6 3 ℝ, EqSystemN 6 3 W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 609](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L609).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_d5_real`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graph-sharp-bound-lean/blob/6c5340384479dbb36129b2e0084449be2458cce2/lean/QuantumCR/FormalConjecturesWrappers.lean#L64-L71](https://github.com/KitaKen1/monochromatic-quantum-graph-sharp-bound-lean/blob/6c5340384479dbb36129b2e0084449be2458cce2/lean/QuantumCR/FormalConjecturesWrappers.lean#L64-L71).

> For $N = 6$ and $D = 5$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{R}$?
>
> The sharp bound $D \le N - 2$ over an integral domain [Ki26] settles this: here $D = N - 1$.

```lean
theorem eqSystem6_no_solution_d5_real :
    ¬ ∃ W : WeightsN 6 5 ℝ, EqSystemN 6 5 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 620](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L620).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_ge3_real`

Open: stated without proof.

> For $N = 6$ and all $D \geq 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{R}$?

```lean
theorem eqSystem6_no_solution_ge3_real :
    ∀ D : Nat, D ≥ 3 →
      ¬ ∃ W : WeightsN 6 D ℝ, EqSystemN 6 D W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 627](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L627).

## `MonochromaticQuantumGraph.eqSystem8_no_solution_d3_real`

Open: stated without proof.

> For $N = 8$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{R}$?

```lean
theorem eqSystem8_no_solution_d3_real :
    ¬ ∃ W : WeightsN 8 3 ℝ, EqSystemN 8 3 W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 635](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L635).

## `MonochromaticQuantumGraph.eqSystem10_no_solution_d3_real`

Open: stated without proof.

> For $N = 10$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{R}$?

```lean
theorem eqSystem10_no_solution_d3_real :
    ¬ ∃ W : WeightsN 10 3 ℝ, EqSystemN 10 3 W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 644](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L644).

## `MonochromaticQuantumGraph.eqSystem_no_solution_ge6_ge3_real`

Open: stated without proof.

> For all even $N \geq 6$ and $D \geq 3$, does there exist no solution to the monochromatic
> quantum graph equation system over $\mathbb{R}$?

```lean
theorem eqSystem_no_solution_ge6_ge3_real :
    ∀ N D : Nat, N ≥ 6 → Even N → D ≥ 3 →
      ¬ ∃ W : WeightsN N D ℝ, EqSystemN N D W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 651](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L651).

## `MonochromaticQuantumGraph.eqSystem4_no_solution_ge4_int`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/4854c7233c58a7dce45fdd58b1826abf2c9c1a0f/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L836](https://github.com/mo271/formal-conjectures/blob/4854c7233c58a7dce45fdd58b1826abf2c9c1a0f/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L836).

> For $N = 4$ and all $D \geq 4$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{Z}$?
>
> This follows from the solution of the complex version of the problem
> (see `eqSystem4_no_solution_ge4`).

```lean
theorem eqSystem4_no_solution_ge4_int :
    ∀ D : Nat, D ≥ 4 →
      ¬ ∃ W : WeightsN 4 D ℤ, EqSystemN 4 D W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 667](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L667).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_d3_int`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L32-L39](https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L32-L39).

> For $N = 6$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{Z}$?

```lean
theorem eqSystem6_no_solution_d3_int :
    ¬ ∃ W : WeightsN 6 3 ℤ, EqSystemN 6 3 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 678](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L678).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_d5_int`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L41-L48](https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L41-L48).

> For $N = 6$ and $D = 5$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{Z}$?

```lean
theorem eqSystem6_no_solution_d5_int :
    ¬ ∃ W : WeightsN 6 5 ℤ, EqSystemN 6 5 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 688](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L688).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_ge3_int`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L50-L58](https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L50-L58).

> For $N = 6$ and all $D \geq 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{Z}$?

```lean
theorem eqSystem6_no_solution_ge3_int :
    ∀ D : Nat, D ≥ 3 →
      ¬ ∃ W : WeightsN 6 D ℤ, EqSystemN 6 D W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 698](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L698).

## `MonochromaticQuantumGraph.eqSystem8_no_solution_d3_int`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L60-L67](https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L60-L67).

> For $N = 8$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{Z}$?

```lean
theorem eqSystem8_no_solution_d3_int :
    ¬ ∃ W : WeightsN 8 3 ℤ, EqSystemN 8 3 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 709](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L709).

## `MonochromaticQuantumGraph.eqSystem10_no_solution_d3_int`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L69-L76](https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L69-L76).

> For $N = 10$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{Z}$?

```lean
theorem eqSystem10_no_solution_d3_int :
    ¬ ∃ W : WeightsN 10 3 ℤ, EqSystemN 10 3 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 720](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L720).

## `MonochromaticQuantumGraph.eqSystem_no_solution_ge6_ge3_int`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L78-L86](https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L78-L86).

> For all even $N \geq 6$ and $D \geq 3$, does there exist no solution to the monochromatic
> quantum graph equation system over $\mathbb{Z}$?

```lean
theorem eqSystem_no_solution_ge6_ge3_int :
    ∀ N D : Nat, N ≥ 6 → Even N → D ≥ 3 →
      ¬ ∃ W : WeightsN N D ℤ, EqSystemN N D W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 730](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L730).

## `MonochromaticQuantumGraph.eqSystem4_no_solution_ge4_trinary_int`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/4854c7233c58a7dce45fdd58b1826abf2c9c1a0f/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L936](https://github.com/mo271/formal-conjectures/blob/4854c7233c58a7dce45fdd58b1826abf2c9c1a0f/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L936).

> For $N = 4$ and all $D \geq 4$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{Z}$ with weights in $\{-1, 0, 1\}$?
>
> This follows from the complex version, see `eqSystem4_no_solution_ge4`.

```lean
theorem eqSystem4_no_solution_ge4_trinary_int :
    ∀ D : Nat, D ≥ 4 →
      ¬ ∃ W : WeightsN 4 D ℤ,
          (∀ e, W e = (-1 : ℤ) ∨ W e = 0 ∨ W e = 1) ∧
            EqSystemN 4 D W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 746](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L746).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_d3_trinary_int`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L88-L97](https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L88-L97).

> For $N = 6$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{Z}$ with weights in $\{-1, 0, 1\}$?

```lean
theorem eqSystem6_no_solution_d3_trinary_int :
    ¬ ∃ W : WeightsN 6 3 ℤ,
        (∀ e, W e = (-1 : ℤ) ∨ W e = 0 ∨ W e = 1) ∧
          EqSystemN 6 3 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 759](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L759).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_d5_trinary_int`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L99-L108](https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L99-L108).

> For $N = 6$ and $D = 5$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{Z}$ with weights in $\{-1, 0, 1\}$?

```lean
theorem eqSystem6_no_solution_d5_trinary_int :
    ¬ ∃ W : WeightsN 6 5 ℤ,
        (∀ e, W e = (-1 : ℤ) ∨ W e = 0 ∨ W e = 1) ∧
          EqSystemN 6 5 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 771](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L771).

## `MonochromaticQuantumGraph.eqSystem6_no_solution_ge3_trinary_int`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L110-L120](https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L110-L120).

> For $N = 6$ and all $D \geq 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{Z}$ with weights in $\{-1, 0, 1\}$?

```lean
theorem eqSystem6_no_solution_ge3_trinary_int :
    ∀ D : Nat, D ≥ 3 →
      ¬ ∃ W : WeightsN 6 D ℤ,
          (∀ e, W e = (-1 : ℤ) ∨ W e = 0 ∨ W e = 1) ∧
            EqSystemN 6 D W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 783](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L783).

## `MonochromaticQuantumGraph.eqSystem8_no_solution_d3_trinary_int`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L122-L131](https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L122-L131).

> For $N = 8$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{Z}$ with weights in $\{-1, 0, 1\}$?

```lean
theorem eqSystem8_no_solution_d3_trinary_int :
    ¬ ∃ W : WeightsN 8 3 ℤ,
        (∀ e, W e = (-1 : ℤ) ∨ W e = 0 ∨ W e = 1) ∧
          EqSystemN 8 3 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 796](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L796).

## `MonochromaticQuantumGraph.eqSystem10_no_solution_d3_trinary_int`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L133-L142](https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L133-L142).

> For $N = 10$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
> equation system over $\mathbb{Z}$ with weights in $\{-1, 0, 1\}$?

```lean
theorem eqSystem10_no_solution_d3_trinary_int :
    ¬ ∃ W : WeightsN 10 3 ℤ,
        (∀ e, W e = (-1 : ℤ) ∨ W e = 0 ∨ W e = 1) ∧
          EqSystemN 10 3 W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 809](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L809).

## `MonochromaticQuantumGraph.eqSystem_no_solution_ge6_ge3_trinary_int`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L144-L154](https://github.com/KitaKen1/monochromatic-quantum-graphs-lean/blob/d3ed1892ef181f5f5f5d61d9b5817f05b53a6675/lean/QuantumLean/FormalConjecturesWrappers.lean#L144-L154).

> For all even $N \geq 6$ and $D \geq 3$, does there exist no solution to the monochromatic
> quantum graph equation system over $\mathbb{Z}$ with weights in $\{-1, 0, 1\}$?

```lean
theorem eqSystem_no_solution_ge6_ge3_trinary_int :
    ∀ N D : Nat, N ≥ 6 → Even N → D ≥ 3 →
      ¬ ∃ W : WeightsN N D ℤ,
          (∀ e, W e = (-1 : ℤ) ∨ W e = 0 ∨ W e = 1) ∧
            EqSystemN N D W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [81 Quantum theory](../../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/Paper/MonochromaticQuantumGraph.lean, line 821](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean#L821).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/MonochromaticQuantumGraph.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/MonochromaticQuantumGraph.lean)
