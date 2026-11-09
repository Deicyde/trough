---
declaration: theorem
origin: cited
lean: OeisA340737.tendsto_exp_one
statement: formalized
---

# Convergence of fraction numerators $a(n)/b(n)$ to $e$

> a: Numerators of a sequence of fractions converging to $e$.
> $$a(1) = 3, a(2) = 5$$
> For $n > 2$:
> $$a(n) = \begin{cases} \left(\frac{n+2}{2}\right) a(n-1) - a(n-2) -
> \left(\frac{n-2}{2}\right) a(n-3)
> & \text{if } n \text{ is even} \cr 2 a(n-1) + n a(n-2) & \text{if } n \text{ is odd} \end{cases}$$
>
> *References:*
> - [A340737](https://oeis.org/A340737)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.
> - [b](https://oeis.org/b)

*Quoted from [FormalConjectures/OEIS/340737.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/340737.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA340737.tendsto_exp_one`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/340737.wip.lean#L438](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/340737.wip.lean#L438).

> Conjecture: $\lim_{n \to \infty} a(n) / b(n) = e$, where $b(n)$ is the companion denominator sequence.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem tendsto_exp_one :
    Filter.Tendsto (fun n : ℕ => (a n : ℝ) / (b n : ℝ)) Filter.atTop (nhds (Real.exp 1))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/340737.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/340737.lean#L141).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/340737.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/340737.lean)
- [A340737](https://oeis.org/A340737)
