---
declaration: theorem
origin: cited
lean: Erdos235.erdos_235, Erdos235.erdos_235.variants.hooley
statement: formalized
---

# Erdős Problem 235

> *References:*
> - [erdosproblems.com/235](https://www.erdosproblems.com/235)
> - [Ho65] Hooley, Christopher, _On the difference between consecutive numbers prime to $n$_. II.
>   Publ. Math. Debrecen (1965), 39--49.

*Quoted from [FormalConjectures/ErdosProblems/235.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/235.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/235](https://www.erdosproblems.com/235).

The file states 2 research or textbook statements: 2 solved. It also has 4 test statements, counted here but not shown.

## `Erdos235.erdos_235`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos235.lean#L4266](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos235.lean#L4266).

> Let $N_k=2\cdot 3\cdots p_k$ and $\{a_1\lt a_2\lt \cdots \lt a_{\phi(N_k)}\}$ be the integers $\lt N_k$ which
> are relatively prime to $N_k$. Then, for any $c\geq 0$, the limit
> $$\frac{\#\{ a_i-a_{i-1}\leq c \frac{N_k}{\phi(N_k)} : 2\leq i\leq \phi(N_k)\}}{\phi(N_k)}$$
> exists and is a continuous function of $c$.
>
> Solved by Hooley [Ho65], who proved that these gaps have an exponential distribution: that is, if
> $f(c)$ is the function in question, then
> $$f(c)=(1+o(1))(1-e^{-c})$$
> (where the $o(1)$ goes to $0$ uniformly as $k\to \infty$).
>
> See also [234](https://www.erdosproblems.com/234) for a more difficult version of this problem using
> actual primes.

```lean
theorem erdos_235 :
    ∃ f : ℝ → ℝ, ContinuousOn f (Set.Ici (0 : ℝ)) ∧
      ∀ c, 0 ≤ c → Tendsto (fun k ↦ proportion k c) atTop (𝓝 (f c))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/235.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/235.lean#L97).

## `Erdos235.erdos_235.variants.hooley`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos235.lean#L4266](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos235.lean#L4266).

> Hooley [Ho65] proved that the limit in `erdos_235` is $1-e^{-c}$.
> For each fixed $c\geq 0$,
> $$f(c)=(1+o(1))(1-e^{-c})$$
> as $k\to\infty$.

```lean
theorem erdos_235.variants.hooley (c : ℝ) (hc : 0 ≤ c) :
    Tendsto (fun k ↦ proportion k c) atTop (𝓝 (1 - Real.exp (-c)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/235.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/235.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/235.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/235.lean)
- [erdosproblems.com/235](https://www.erdosproblems.com/235)
