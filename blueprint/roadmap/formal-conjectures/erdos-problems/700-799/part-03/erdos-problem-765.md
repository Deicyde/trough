---
declaration: theorem
origin: cited
lean: Erdos765.erdos_765, Erdos765.erdos_765.variants.second_term
statement: formalized
---

# Erdős Problem 765

> *References:*
> - [erdosproblems.com/765](https://www.erdosproblems.com/765)
> - [Er38] Erdős, P., *On sequences of integers no one of which divides the product of two others
>   and on related problems*. Tomsk. Gos. Univ. Ucen Zap. (1938), 74-82.
> - [Re58] Reiman, I., *Über ein Problem von K. Zarankiewicz*. Acta Math. Acad. Sci. Hungar. 9
>   (1958), 269-273.
> - [ERS66] Erdős, P. and Rényi, A. and Sós, V. T., *On a problem of graph theory*. Studia Sci. Math.
>   Hungar. (1966), 215--235.
> - [Br66] Brown, W. G., *On graphs that do not contain a Thomsen graph*. Canad. Math. Bull. (1966),
>   281-285.
> - [Er75] Erdős, P., *Some recent progress on extremal problems in graph theory*. Congr. Numer.
>   (1975), 3-14.
> - [Fu83] Füredi, Z., *Graphs without quadrilaterals*. J. Combin. Theory Ser. B 34 (1983),
>   187-190.
> - [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. (1993), 333-350.
> - [MaYa23] Ma, Jie and Yang, Tianchi, *Upper bounds on the extremal number of the 4-cycle*. Bull.
>   Lond. Math. Soc. (2023), 1655--1667.

*Quoted from [FormalConjectures/ErdosProblems/765.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/765.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/765](https://www.erdosproblems.com/765).

The file states 2 research or textbook statements: 2 solved.

## `Erdos765.erdos_765`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos765.lean#L24](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos765.lean#L24).

> Give an asymptotic formula for $\mathrm{ex}(n; C_4)$.
>
> Erdős and Klein [Er38] proved $\mathrm{ex}(n; C_4) \asymp n^{3/2}$, and Reiman [Re58] proved
> $$\frac{1}{2\sqrt 2} \le \lim \frac{\mathrm{ex}(n; C_4)}{n^{3/2}} \le \frac12.$$
> Erdős and Rényi [ERS66], and independently Brown [Br66], gave a construction showing that if
> $n = q^2 + q + 1$ with $q$ a prime power then $\mathrm{ex}(n; C_4) \ge \frac12 q (q+1)^2$; together
> with Reiman's upper bound this gives $\mathrm{ex}(n; C_4) \sim \frac12 n^{3/2}$. Füredi [Fu83] proved
> $\mathrm{ex}(n; C_4) = \frac12 q (q+1)^2$ for $q > 13$.

```lean
theorem erdos_765 :
    (fun n : ℕ ↦ (SimpleGraph.extremalNumber n (SimpleGraph.cycleGraph 4) : ℝ)) ~[atTop]
      fun n : ℕ ↦ (n : ℝ) ^ (3 / 2 : ℝ) / 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/765.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/765.lean#L63).

## `Erdos765.erdos_765.variants.second_term`

Solved: stated here without proof.

> Erdős [Er93] conjectured that $\mathrm{ex}(n; C_4) = \frac{n^{3/2}}{2} + \frac n4 + O(n^{1/2})$ for all
> $n$, having proved the upper bound $\mathrm{ex}(n; C_4) \le \frac{n^{3/2}}{2} + \frac n4 + O(n^{1/2})$
> in [Er75]. This is false: Ma and Yang [MaYa23] proved that, for some absolute constant $c > 0$ and
> a positive density set of $n$, $\mathrm{ex}(n; C_4) \le \frac{n^{3/2}}{2} + (\frac14 - c) n$.

```lean
theorem erdos_765.variants.second_term :
    ¬ (fun n : ℕ ↦ (SimpleGraph.extremalNumber n (SimpleGraph.cycleGraph 4) : ℝ) -
      (n : ℝ) ^ (3 / 2 : ℝ) / 2 - (n : ℝ) / 4) =O[atTop] fun n : ℕ ↦ (n : ℝ) ^ (1 / 2 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/765.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/765.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/765.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/765.lean)
- [erdosproblems.com/765](https://www.erdosproblems.com/765)
