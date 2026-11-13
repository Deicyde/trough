---
declaration: theorem
origin: cited
lean: Erdos391.erdos_391, Erdos391.erdos_391.variants.deficit
statement: formalized
---

# Erdős Problem 391

> *References:*
> - [erdosproblems.com/391](https://www.erdosproblems.com/391)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Er96b] Erdős, Paul, *Some problems I presented or planned to present in my short talk*.
>   Analytic number theory, Vol. 1 (Allerton Park, IL, 1995) (1996), 333-335.
> - [AlGr77] Alladi, Krishnaswami and Grinstead, Charles, *On the decomposition of $n!$ into prime
>   powers*. J. Number Theory (1977), 452-458.
> - [ACRSTUV25] B. Alexeev, E. Conway, M. Rosenfeld, A. Sutherland, T. Tao, M. Uhr, and K.
>   Ventullo, *Decomposing a factorial into large factors*. arXiv:2503.20170 (2025).

*Quoted from [FormalConjectures/ErdosProblems/391.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/391.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/391](https://www.erdosproblems.com/391).

The file states 2 research or textbook statements: 2 solved.

## `Erdos391.erdos_391`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos391.lean#L4924](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos391.lean#L4924).

> Let $t(n)$ be maximal such that there is a representation
>
> $$n!=a_1\cdots a_n$$
>
> with $t(n)=a_1\leq \cdots \leq a_n$. Obtain good bounds for $t(n)/n$. In particular, is it true
> that
>
> $$\lim \frac{t(n)}{n}=\frac{1}{e}?$$
>
> It is easy to see that $\lim \frac{t(n)}{n}\leq \frac{1}{e}$. Erdős [Er96b] wrote he, Selfridge,
> and Straus had proved a corresponding lower bound, so that $\lim \frac{t(n)}{n}=\frac{1}{e}$, and
> 'believed that Straus had written up our proof. Unfortunately Straus suddenly died and no trace
> was ever found of his notes. Furthermore, we never could reconstruct our proof, so our assertion
> now can be called only a conjecture.'
>
> Alladi and Grinstead [AlGr77] have obtained similar results when the $a_i$ are restricted to
> prime powers.
>
> Both questions were answered by Alexeev, Conway, Rosenfeld, Sutherland, Tao, Uhr, and Ventullo
> [ACRSTUV25], who proved that
>
> $$\frac{t(n)}{n}= \frac{1}{e}-\frac{c_0}{\log n}+O\left(\frac{1}{(\log n)^{1+c}}\right),$$
>
> where $c_0=0.3044\cdots$ is an explicit constant, for some $c>0$.

```lean
theorem erdos_391 :
    Tendsto (fun n : ℕ => (t n : ℝ) / n) atTop (𝓝 (1 / Real.exp 1))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/391.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/391.lean#L70).

## `Erdos391.erdos_391.variants.deficit`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos391.lean#L4924](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos391.lean#L4924).

> Furthermore, does there exist some constant $c>0$ such that
>
> $$\frac{t(n)}{n} \leq \frac{1}{e}-\frac{c}{\log n}$$
>
> for infinitely many $n$?
>
> This was answered in the affirmative by Alexeev, Conway, Rosenfeld, Sutherland, Tao, Uhr, and
> Ventullo [ACRSTUV25].

```lean
theorem erdos_391.variants.deficit : ∃ c : ℝ, 0 < c ∧
    {n : ℕ | (t n : ℝ) / n ≤ 1 / Real.exp 1 - c / Real.log n}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/391.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/391.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/391.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/391.lean)
- [erdosproblems.com/391](https://www.erdosproblems.com/391)
