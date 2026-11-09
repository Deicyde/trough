---
declaration: theorem
origin: cited
lean: Erdos841.erdos_841, Erdos841.erdos_841.variants.selfridge_large_prime, Erdos841.erdos_841.variants.selfridge_sqrt, Erdos841.erdos_841.variants.many_small_values, Erdos841.erdos_841.variants.lower_bound
statement: formalized
---

# Erdős Problem 841

> *References:*
> - [erdosproblems.com/841](https://www.erdosproblems.com/841)
> - [ErSe92] Erdős, Paul and Selfridge, J. L., Problems and Solutions: Solutions: 6655. Amer. Math.
>   Monthly (1992), 791--794.
> - [BPZ24] Bui, Hung M. and Pratt, Kyle and Zaharescu, Alexandru, A problem of
>   Erdős-Graham-Granville-Selfridge on integral points on hyperelliptic curves. Math. Proc.
>   Cambridge Philos. Soc. (2024), 309--323.
> - [Gu04] Guy, Richard K., Unsolved problems in number theory. (2004), xviii+437.

*Quoted from [FormalConjectures/ErdosProblems/841.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/841.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/841](https://www.erdosproblems.com/841).

The file states 5 research or textbook statements: 5 solved.

## `Erdos841.erdos_841`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos841/Core.lean#L16920](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos841/Core.lean#L16920).

> Let $t_n$ be minimal such that $\{n+1,\ldots,n+t_n\}$ contains a subset whose product with $n$ is
> a square number (and let $t_n=0$ if $n$ is itself square). Estimate $t_n$.
>
> A problem of Erdős, Graham, and Selfridge. For example, $t_6=6$ since $6\cdot 8\cdot 12=24^2$. It
> is trivial that $t_n\geq P(n)$, where $P(n)$ is the largest prime divisor of $n$.
>
> Bui, Pratt, and Zaharescu [BPZ24] proved that the distribution of $t_n$ continues to follow
> $P(n)$, in that for any fixed $c\in (0,1]$
>
> $$\lim_{x\to \infty}\frac{\lvert \{ n\leq x : t_n\leq n^c\}\rvert}{x}
>   = \lim_{x\to \infty}\frac{\lvert \{ n\leq x : P(n)\leq n^c\}\rvert}{x}.$$
>
> The statement below is that the difference of the two counting functions is $o(x)$.
>
> This was formalized in Lean by Codex.

```lean
theorem erdos_841 (c : ℝ) (hc : c ∈ Set.Ioc 0 1) :
    Tendsto (fun x : ℕ ↦
      ((((Finset.Icc 1 x).filter fun n : ℕ ↦ (t n : ℝ) ≤ (n : ℝ) ^ c).card : ℝ) -
        ((Finset.Icc 1 x).filter fun n : ℕ ↦ (n.maxPrimeFac : ℝ) ≤ (n : ℝ) ^ c).card) / x)
      atTop (𝓝 0)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/841.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/841.lean#L62).

## `Erdos841.erdos_841.variants.selfridge_large_prime`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos841/LowerBound.lean#L3183](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos841/LowerBound.lean#L3183).

> Selfridge proved that $t_n=P(n)$ if $P(n)>\sqrt{2n}+1$.
>
> This was formalized in Lean by Codex.

```lean
theorem erdos_841.variants.selfridge_large_prime (n : ℕ) (hn : 1 < n)
    (h : √(2 * n) + 1 < (n.maxPrimeFac : ℝ)) : t n = n.maxPrimeFac
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/841.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/841.lean#L76).

## `Erdos841.erdos_841.variants.selfridge_sqrt`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos841/Core.lean#L1373](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos841/Core.lean#L1373).

> Selfridge proved that $t_n \ll n^{1/2}$ if $P(n)\leq\sqrt{2n}+1$.
>
> This was formalized in Lean by Codex.

```lean
theorem erdos_841.variants.selfridge_sqrt :
    ∃ C : ℝ, ∀ n : ℕ, (n.maxPrimeFac : ℝ) ≤ √(2 * n) + 1 → (t n : ℝ) ≤ C * √n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/841.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/841.lean#L87).

## `Erdos841.erdos_841.variants.many_small_values`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos841/Core.lean#L16105](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos841/Core.lean#L16105).

> Bui, Pratt, and Zaharescu [BPZ24] proved that for at least $x^{1-o(1)}$ many $n\leq x$ we have
>
> $$t_n \leq \exp(O(\sqrt{\log n\log\log n})).$$
>
> This was formalized in Lean by Codex.

```lean
theorem erdos_841.variants.many_small_values : ∃ K : ℝ,
    Tendsto (fun x : ℕ ↦
      log (((Finset.Icc 1 x).filter fun n ↦
        (t n : ℝ) ≤ exp (K * √(log n * log (log n)))).card : ℝ) / log x) atTop (𝓝 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/841.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/841.lean#L100).

## `Erdos841.erdos_841.variants.lower_bound`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos841/LowerBound.lean#L3166](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos841/LowerBound.lean#L3166).

> Bui, Pratt, and Zaharescu [BPZ24] proved that for all non-square $n$
>
> $$t_n \gg (\log\log n)^{6/5}(\log\log\log n)^{-1/5}.$$
>
> This was formalized in Lean by Codex.

```lean
theorem erdos_841.variants.lower_bound : ∃ C : ℝ, 0 < C ∧
    ∀ᶠ n : ℕ in atTop, ¬ IsSquare n →
      C * (log (log n) ^ ((6 : ℝ) / 5) * log (log (log n)) ^ (-(1 : ℝ) / 5)) ≤ t n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/841.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/841.lean#L114).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/841.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/841.lean)
- [erdosproblems.com/841](https://www.erdosproblems.com/841)
