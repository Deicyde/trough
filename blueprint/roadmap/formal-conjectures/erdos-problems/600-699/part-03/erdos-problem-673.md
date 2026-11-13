---
declaration: theorem
origin: cited
lean: Erdos673.erdos_673.parts.i, Erdos673.erdos_673.parts.ii, Erdos673.erdos_673.variants.average, Erdos673.erdos_673.variants.tao
statement: formalized
---

# Erdős Problem 673

> *References:*
> - [erdosproblems.com/673](https://www.erdosproblems.com/673)
> - [Er79e] Erdős, Paul, _Some unconventional problems in number theory_. Astérisque (1979), 73-82.
> - [Er82e] Erdős, Paul, _Some of my favourite problems which recently have been solved_. (1982),
>   59--79.

*Quoted from [FormalConjectures/ErdosProblems/673.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/673.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/673](https://www.erdosproblems.com/673).

The file states 4 research or textbook statements: 3 solved and 1 textbook result.

## `Erdos673.erdos_673.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos673.lean#L914](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos673.lean#L914).

> Let $1=d_1\lt \cdots \lt d_{\tau(n)}=n$ be the divisors of $n$ and
>
> $$G(n) = \sum_{1\leq i\lt \tau(n)}\frac{d_i}{d_{i+1}}.$$
>
> Is it true that $G(n)\to \infty$ for almost all $n$?
>
> The answer is yes: Tao observed that $\tau(n/m)/m\leq G(n)\leq \tau(n)$ for any $m\mid n$ with
> $m>1$, so that $G(n)$ behaves very similarly to $\tau(n)$. In [Er82e] Erdős recalls this
> conjecture and observes that it is indeed trivial that $G(n)\to \infty$ for almost all $n$.

```lean
theorem erdos_673.parts.i : ∀ C : ℝ, {n : ℕ | C < G n}.HasDensity 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/673.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/673.lean#L54).

## `Erdos673.erdos_673.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos673.lean#L914](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos673.lean#L914).

> Can one prove an asymptotic formula for $\sum_{n\leq X}G(n)$?
>
> Indeed $\sum_{n\leq X}G(n)\sim X\log X$.

```lean
theorem erdos_673.parts.ii :
    (fun X : ℕ ↦ ∑ n ∈ Finset.Icc 1 X, G n) ~[atTop] fun X : ℕ ↦ (X : ℝ) * log X
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/673.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/673.lean#L65).

## `Erdos673.erdos_673.variants.average`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos673.lean#L914](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos673.lean#L914).

> Erdős writes it is 'easy' to prove $\frac{1}{X}\sum_{n\leq X}G(n)\to \infty$.

```lean
theorem erdos_673.variants.average :
    Tendsto (fun X : ℕ ↦ (∑ n ∈ Finset.Icc 1 X, G n) / X) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/673.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/673.lean#L73).

## `Erdos673.erdos_673.variants.tao`

Textbook result, stated without proof.

> Tao observed that, for any divisor $m\mid n$ with $m>1$,
> $\frac{\tau(n/m)}{m} \leq G(n) \leq \tau(n)$.

```lean
theorem erdos_673.variants.tao (n m : ℕ) (hn : 0 < n) (hm : 1 < m) (hmn : m ∣ n) :
    ((n / m).divisors.card : ℝ) / m ≤ G n ∧ G n ≤ n.divisors.card
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/673.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/673.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/673.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/673.lean)
- [erdosproblems.com/673](https://www.erdosproblems.com/673)
