---
declaration: theorem
origin: cited
lean: Erdos748.erdos_748, Erdos748.erdos_748.variants.lower_bound, Erdos748.erdos_748.variants.green_sapozhenko, Erdos748.erdos_748.variants.asymptotic
statement: formalized
---

# Erdős Problem 748

> *References:*
> - [erdosproblems.com/748](https://www.erdosproblems.com/748)
> - [CaEr90] Cameron, P. J. and Erdős, P., _On the number of sets of integers with various
>   properties_. (1990), 61-79.
> - [Er94b] Erdős, Paul, _Some problems in number theory, combinatorics and combinatorial
>   geometry_. Math. Pannon. (1994), 261-269.
> - [Er98] Erdős, Paul, _Some of my new and almost new problems and results in combinatorial number
>   theory_. Number theory (Eger, 1996) (1998), 169-180.
> - [Gr04] Green, Ben, _The Cameron-Erdős conjecture_. Bull. London Math. Soc. (2004), 769-778.
> - [Sa03] Sapozhenko, A. A., _The Cameron-Erdős conjecture_. Dokl. Akad. Nauk (2003), 749-752.

*Quoted from [FormalConjectures/ErdosProblems/748.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/748.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/748](https://www.erdosproblems.com/748).

The file states 4 research or textbook statements: 3 solved and 1 textbook result.

## `Erdos748.erdos_748`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos748.lean#L1228](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos748.lean#L1228).

> Let $f(n)$ count the number of sum-free $A\subseteq \{1,\ldots,n\}$, i.e. $A$ contains no
> solutions to $a=b+c$ with $a,b,c\in A$. Is it true that
> $$f(n)=2^{(1+o(1))\frac{n}{2}}?$$
>
> The Cameron–Erdős conjecture. This is true, and in fact $f(n) \ll 2^{n/2}$, which was proved
> independently by Green [Gr04] and Sapozhenko [Sa03].
>
> The statement $f(n)=2^{(1+o(1))n/2}$ is formalised as $\log_2 f(n)/n\to 1/2$.

```lean
theorem erdos_748 :
    Tendsto (fun n : ℕ ↦ logb 2 (f n) / n) atTop (nhds (1 / 2))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/748.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/748.lean#L60).

## `Erdos748.erdos_748.variants.lower_bound`

Textbook result, stated without proof.

> It is trivial to see that $f(n) \geq 2^{\frac{n}{2}}$, considering all subsets of
> $(n/2,n]$. The source writes $[n/2,n]$, but for even $n$ that interval is not sum-free,
> since $n/2 + n/2 = n$.

```lean
theorem erdos_748.variants.lower_bound (n : ℕ) :
    (2 : ℝ) ^ ((n : ℝ) / 2) ≤ (f n : ℝ)
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/748.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/748.lean#L68).

## `Erdos748.erdos_748.variants.green_sapozhenko`

Solved: stated here without proof.

> Green [Gr04] and Sapozhenko [Sa03] proved that $f(n) \ll 2^{n/2}$.

```lean
theorem erdos_748.variants.green_sapozhenko :
    ∃ C : ℝ, ∀ n : ℕ, (f n : ℝ) ≤ C * 2 ^ ((n : ℝ) / 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/748.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/748.lean#L74).

## `Erdos748.erdos_748.variants.asymptotic`

Solved: stated here without proof.

> In fact, both Green [Gr04] and Sapozhenko [Sa03] prove the stronger asymptotic
> $f(n) \sim c_n 2^{n/2}$, where $c_n$ takes on one of two values depending on the parity of
> $n$.

```lean
theorem erdos_748.variants.asymptotic :
    ∃ c₀ c₁ : ℝ, 0 < c₀ ∧ 0 < c₁ ∧
      Tendsto (fun m : ℕ ↦ (f (2 * m) : ℝ) / 2 ^ m) atTop (nhds c₀) ∧
      Tendsto (fun m : ℕ ↦ (f (2 * m + 1) : ℝ) / 2 ^ ((2 * m + 1 : ℝ) / 2)) atTop
        (nhds c₁)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/748.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/748.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/748.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/748.lean)
- [erdosproblems.com/748](https://www.erdosproblems.com/748)
