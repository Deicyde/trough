---
declaration: theorem
origin: cited
lean: Erdos1195.erdos_1195, Erdos1195.erdos_1195.variants.exists_set
statement: formalized
---

# Erdős Problem 1195

> *References:*
> - [erdosproblems.com/1195](https://www.erdosproblems.com/1195)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115. [PDF](https://www.renyi.hu/~p_erdos/1980-03.pdf)
> - [Ha70] Haight, J. A., *A linear set of infinite measure with no two points having integral
>   ratio*. Mathematika (1970), 133--138.
> - [HoGPT] Ho, Boon Suan and GPT-5.4 Pro, comments on Erdős Problem 1195. erdosproblems.com forum
>   thread. [Forum](https://www.erdosproblems.com/forum/thread/1195)
> - [Sc69] Schmidt, W. M., *Disproof of some conjectures on Diophantine approximations*. Studia Sci.
>   Math. Hungar. (1969), 137-144.
> - [Sz71] Szemerédi, E., *On a problem of W. Schmidt*. Studia Sci. Math. Hungar. (1971), 287--288.

*Quoted from [FormalConjectures/ErdosProblems/1195.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1195.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1195](https://www.erdosproblems.com/1195).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1195.erdos_1195`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1195.lean#L1933](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1195.lean#L1933).

> Let $S\subset \mathbb{R}$ be a set of infinite measure such that $x/y$ is never an integer for all
> distinct $x,y\in S$.
>
> How fast can $\lvert S\cap (0,x)\rvert$ tend to infinity?
>
> A question of Erdős [Er80, p. 101]. Ho Boon Suan and GPT-5.4 Pro [HoGPT] settled this: if
> $F:[1,\infty)\to [0,\infty)$ is a non-decreasing function tending to infinity, then there exists
> such a set $S$ with
> $\lvert S\cap (0,x)\rvert \geq F(x)$ if and only if
> $$\int_1^\infty \frac{F(x)}{x^2}\mathrm{d}x < \infty.$$
> Here $\lvert\cdot\rvert$ is Lebesgue measure, $S$ is measurable, and the inequality is required for
> all sufficiently large $x$. The statement says that the set of such $F$ is exactly the answer.

```lean
theorem erdos_1195 :
    {F : ℝ → ℝ | IsGrowthRate F ∧ HasSet F} = erdos_1195.answer
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1195.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1195.lean#L86).

## `Erdos1195.erdos_1195.variants.exists_set`

Solved: stated here without proof.

> Schmidt [Sc69] asked whether such a set exists. Haight [Ha70] constructed a measurable set
> $E\subset(0,\infty)$ of infinite Lebesgue measure such that $x_1/x_2$ is never an integer for
> distinct $x_1,x_2\in E$, and Szemerédi [Sz71] independently constructed such a set.

```lean
theorem erdos_1195.variants.exists_set :
    ∃ S : Set ℝ, MeasurableSet S ∧ S ⊆ Set.Ioi 0 ∧ volume S = ⊤ ∧ IntegerRatioFree S
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1195.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1195.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1195.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1195.lean)
- [erdosproblems.com/1195](https://www.erdosproblems.com/1195)
