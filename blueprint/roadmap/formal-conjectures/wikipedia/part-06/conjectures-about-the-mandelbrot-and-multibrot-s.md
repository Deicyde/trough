---
declaration: theorem
origin: cited
lean: Mandelbrot.MLC, Mandelbrot.MLC_general_exponent, Mandelbrot.density_of_hyperbolicity, Mandelbrot.density_of_hyperbolicity_general_exponent, Mandelbrot.volume_frontier_mandelbrotSet_eq_zero, Mandelbrot.volume_frontier_multibrotSet_eq_zero
statement: formalized
---

# Conjectures about the Mandelbrot and Multibrot sets

> This file adds three conjectures about the Mandelbrot and Multibrot sets:
> - the *MLC conjecture*, stating that these sets are locally connected
> - the *density of hyperbolicity* conjecture, stating that parameters with attracting cycles are
>   dense in the Mandelbrot and Multibrot sets
> - the conjecture that the boundaries of these sets have zero area.
> The first two conjectures are related in that the former implies the latter.
>
> *References:*
>  - [Wikipedia](https://en.wikipedia.org/wiki/Mandelbrot_set#Local_connectivity)
>  - [arxiv/math/9902155](https://arxiv.org/abs/math/9902155)
>  - [mathoverflow/37229](https://mathoverflow.net/questions/37229/)

*Quoted from [FormalConjectures/Wikipedia/Mandelbrot.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mandelbrot.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 6 open. It also has 4 test statements and 2 API statements, counted here but not shown.

## `Mandelbrot.MLC`

Open: stated without proof.

> The MLC conjecture, stating that the mandelbrot set is locally connected.

```lean
theorem MLC : LocallyConnectedSpace mandelbrotSet
```

Category `research open`; AMS [37 Dynamical systems and ergodic theory](../../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mandelbrot.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mandelbrot.lean#L111).

## `Mandelbrot.MLC_general_exponent`

Open: stated without proof.

> A stronger version of the MLC conjecture, stating that all multibrots are locally connected.
> Note that we don't need to require `2 ≤ n` because the conjecture holds in the trivial cases `n = 0`
> and `n = 1` too.

```lean
theorem MLC_general_exponent (n : ℕ) : LocallyConnectedSpace (multibrotSet n)
```

Category `research open`; AMS [37 Dynamical systems and ergodic theory](../../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mandelbrot.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mandelbrot.lean#L118).

## `Mandelbrot.density_of_hyperbolicity`

Open: stated without proof.

> The density of hyperbolicity conjecture, stating that the set of all parameters `c` for which
> `fun z ↦ z ^ 2 + c` has an attracting cycle is dense in the Mandelbrot set.

```lean
theorem density_of_hyperbolicity :
    mandelbrotSet ⊆ closure {c | ∃ m z, IsAttractingCycle (fun z ↦ z ^ 2 + c) m z}
```

Category `research open`; AMS [37 Dynamical systems and ergodic theory](../../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mandelbrot.lean, line 147](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mandelbrot.lean#L147).

## `Mandelbrot.density_of_hyperbolicity_general_exponent`

Open: stated without proof.

> The density of hyperbolicity conjecture for Multibrot sets, stating that the set of all
> parameters `c` for which `fun z ↦ z ^ n + c` has an attracting cycle is dense in `multibrotSet n`.
> Note that we need to require `2 ≤ n` because the conjecture is trivially false for `n = 1`.

```lean
theorem density_of_hyperbolicity_general_exponent {n : ℕ} (hn : 2 ≤ n) :
    multibrotSet n ⊆ closure {c | ∃ m z, IsAttractingCycle (fun z ↦ z ^ n + c) m z}
```

Category `research open`; AMS [37 Dynamical systems and ergodic theory](../../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mandelbrot.lean, line 155](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mandelbrot.lean#L155).

## `Mandelbrot.volume_frontier_mandelbrotSet_eq_zero`

Open: stated without proof.

> The boundary of the Mandelbrot set is conjectured to have zero area.

```lean
theorem volume_frontier_mandelbrotSet_eq_zero : volume (frontier mandelbrotSet) = 0
```

Category `research open`; AMS [37 Dynamical systems and ergodic theory](../../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mandelbrot.lean, line 166](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mandelbrot.lean#L166).

## `Mandelbrot.volume_frontier_multibrotSet_eq_zero`

Open: stated without proof.

> The boundary of any Multibrot set is conjectured to have zero area.
> Note that we don't need to exclude the trivial cases `n = 0` and `n = 1` because the conjecture
> holds for them.

```lean
theorem volume_frontier_multibrotSet_eq_zero {n : ℕ} : volume (frontier (multibrotSet n)) = 0
```

Category `research open`; AMS [37 Dynamical systems and ergodic theory](../../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mandelbrot.lean, line 173](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mandelbrot.lean#L173).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Mandelbrot.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mandelbrot.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Mandelbrot_set#Local_connectivity)
