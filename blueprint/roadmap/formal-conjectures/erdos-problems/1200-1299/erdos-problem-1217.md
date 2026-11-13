---
declaration: theorem
origin: cited
lean: Erdos1217.erdos_1217, Erdos1217.erdos_1217.variants.without_density, Erdos1217.erdos_1217.variants.abllpstt, Erdos1217.erdos_1217.variants.davenport_erdos, Erdos1217.erdos_1217.variants.erdos_sarkozi_szemeredi
statement: formalized
---

# Erdős Problem 1217

> *References:*
> - [erdosproblems.com/1217](https://www.erdosproblems.com/1217)
> - [ABLLPSTT26] B. Alexeev, K. Barreto, Y. Li, J. D. Lichtman, L. Price, J. I. Shah, Q. Tang, and
>   T. Tao, *Primitive sets and von Mangoldt chains: Erdős Problem #1196 and beyond*.
>   arXiv:2605.00301 (2026).
> - [DaEr51] Davenport, H. and Erdős, P., *On sequences of positive integers*. J. Indian Math.
>   Soc. (N.S.) (1951), 19--24. [PDF](https://www.renyi.hu/~p_erdos/1951-07.pdf)
> - [ESS66] Erdős, P. and Sárközi, A. and Szemerédi, E., *On divisibility properties of sequences of
>   integers*. Studia Sci. Math. Hungar. (1966), 431--435.
>   [PDF](https://www.renyi.hu/~p_erdos/1966-09.pdf)

*Quoted from [FormalConjectures/ErdosProblems/1217.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1217.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1217](https://www.erdosproblems.com/1217).

The file states 5 research or textbook statements: 5 solved.

## `Erdos1217.erdos_1217`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1217.lean#L86](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1217.lean#L86).

> Let $A=\{a_1\lt a_2\lt \cdots\}$ be an infinite sequence of positive integers with positive lower
> logarithmic density.
>
> Must there exist a sequence $n_1\lt \cdots$ such that
>
> $$a_{n_i}\mid a_{n_{i+1}}$$
>
> for all $i\geq 1$ and
>
> $$\limsup_{x\to \infty}\frac{1}{\log\log x}\sum_{a_{n_i}\lt x}1 \geq
>   \limsup_{x\to \infty} \frac{1}{\log\log x}\sum_{a_n\lt x}\frac{1}{a_n\log a_n}?$$
>
> A problem of Erdős, Sárközi, and Szemerédi [ESS66, p. 432, (5)]. The answer is yes, proved by
> Alexeev, Barreto, Li, Lichtman, Price, Shah, Tang, and Tao [ABLLPSTT26, Theorem 1.6]. Sequences
> are indexed from $0$ here.

```lean
theorem erdos_1217 :
    ∀ a : ℕ → ℕ, StrictMono a → (∀ i, 0 < a i) → 0 < lowerLogDensity (Set.range a) →
      ∃ n : ℕ → ℕ, StrictMono n ∧ (∀ i, a (n i) ∣ a (n (i + 1))) ∧
        weightedRate (Set.range a) ≤ chainRate (a ∘ n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1217.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1217.lean#L97).

## `Erdos1217.erdos_1217.variants.without_density`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1217.lean#L66](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1217.lean#L66).

> The answer to `erdos_1217` is yes even without the assumption that $A$ has positive lower
> logarithmic density [ABLLPSTT26]: it suffices that the doubly harmonic rate on the right-hand
> side is positive, which holds whenever the lower logarithmic density is positive.

```lean
theorem erdos_1217.variants.without_density :
    ∀ a : ℕ → ℕ, StrictMono a → 0 < weightedRate (Set.range a) →
      ∃ n : ℕ → ℕ, StrictMono n ∧ (∀ i, a (n i) ∣ a (n (i + 1))) ∧
        weightedRate (Set.range a) ≤ chainRate (a ∘ n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1217.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1217.lean#L111).

## `Erdos1217.erdos_1217.variants.abllpstt`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1217/Resolution.lean#L451](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1217/Resolution.lean#L451).

> The set form of [ABLLPSTT26, Theorem 1.6]: if $A \subseteq \mathbb{N}$ has positive upper doubly
> logarithmic density
>
> $$\Delta=\limsup_{x\to\infty}\frac{1}{\log\log x}\sum_{n\in A,\ n\lt x}\frac{1}{n\log n},$$
>
> then $A$ contains a strictly increasing infinite divisibility chain $d_0\mid d_1\mid\cdots$ with
>
> $$\limsup_{x\to\infty}\frac{1}{\log\log x}\sum_{d_i\lt x}1\geq\Delta.$$

```lean
theorem erdos_1217.variants.abllpstt (A : Set ℕ) (hA : 0 < weightedRate A) :
    ∃ d : ℕ → ℕ, StrictMono d ∧ (∀ i, d i ∈ A) ∧ (∀ i, d i ∣ d (i + 1)) ∧
      weightedRate A ≤ chainRate d
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1217.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1217.lean#L127).

## `Erdos1217.erdos_1217.variants.davenport_erdos`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1217.lean#L86](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1217.lean#L86).

> Davenport and Erdős [DaEr51] proved that (assuming $A$ has positive lower logarithmic density)
> there exists a sequence $n_1\lt \cdots$ such that $a_{n_i}\mid a_{n_{i+1}}$ for all $i\geq 1$
> (as stated in [ESS66, p. 431]). This also follows from `erdos_1217`.

```lean
theorem erdos_1217.variants.davenport_erdos :
    ∀ a : ℕ → ℕ, StrictMono a → (∀ i, 0 < a i) → 0 < lowerLogDensity (Set.range a) →
      ∃ n : ℕ → ℕ, StrictMono n ∧ ∀ i, a (n i) ∣ a (n (i + 1))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1217.lean, line 140](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1217.lean#L140).

## `Erdos1217.erdos_1217.variants.erdos_sarkozi_szemeredi`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1217.lean#L66](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1217.lean#L66).

> Erdős, Sárközi, and Szemerédi [ESS66, Theorem 2] proved that if
>
> $$\limsup_{x\to \infty}\frac{1}{\log\log x}\sum_{a_n\lt x}\frac{1}{a_n\log a_n}=c>0,$$
>
> then there exists such a sequence with
>
> $$\limsup_{x\to \infty}\frac{1}{\log\log x}\sum_{a_{n_i}\lt x}1\gg_c 1.$$
>
> Here $\gg_c 1$ means a lower bound $\kappa>0$ depending only on $c$.

```lean
theorem erdos_1217.variants.erdos_sarkozi_szemeredi :
    ∀ c : ℝ, 0 < c → ∃ κ : ℝ, 0 < κ ∧ ∀ a : ℕ → ℕ, StrictMono a →
      weightedRate (Set.range a) = ENNReal.ofReal c →
        ∃ n : ℕ → ℕ, StrictMono n ∧ (∀ i, a (n i) ∣ a (n (i + 1))) ∧
          ENNReal.ofReal κ ≤ chainRate (a ∘ n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1217.lean, line 155](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1217.lean#L155).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1217.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1217.lean)
- [erdosproblems.com/1217](https://www.erdosproblems.com/1217)
