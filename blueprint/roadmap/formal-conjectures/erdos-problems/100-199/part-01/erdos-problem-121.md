---
declaration: theorem
origin: cited
lean: Erdos121.erdos_121, Erdos121.erdos_121.variants.odd, Erdos121.erdos_121.variants.tao, Erdos121.erdos_121.variants.three, Erdos121.erdos_121.variants.two
statement: formalized
---

# Erdős Problem 121

> *References:*
> - [erdosproblems.com/121](https://www.erdosproblems.com/121)
> - [Er94b] Erdős, Paul, *Some problems in number theory, combinatorics and combinatorial geometry*.
>   Math. Pannon. (1994), 261-269.
> - [Er97] Erdős, Paul, *Problems in number theory*. New Zealand J. Math. (1997), 155-160.
> - [Er97e] Erdős, Paul, *Some of my favourite unsolved problems*. Math. Japon. (1997), 527-537.
> - [Er98] Erdős, Paul, *Some of my new and almost new problems and results in combinatorial number
>   theory*. Number theory (Eger, 1996) (1998), 169-180.
> - [ESS95] Erdős, P. and Sárközy, A. and Sós, V. T., *On product representations of powers. I*.
>   European J. Combin. (1995), 567-588.
> - [Er38] P. Erdős, *On sequences of integers no one of which divides the product of two others
>   and on related problems*. Tomsk. Gos. Univ. Ucen Zap. (1938), 74-82.
> - [Ta24] Tao, T., *On product representations of squares*. arXiv:2405.11610 (2024).

*Quoted from [FormalConjectures/ErdosProblems/121.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/121.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/121](https://www.erdosproblems.com/121).

The file states 5 research or textbook statements: 5 solved.

## `Erdos121.erdos_121`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos121.lean#L87](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos121.lean#L87).

> Let $F_{k}(N)$ be the size of the largest $A\subseteq \{1,\ldots,N\}$ such that the product of no
> $k$ many distinct elements of $A$ is a square. Is $F_5(N)=(1-o(1))N$?
>
> Conjectured by Erdős, Sós, and Sárközy [ESS95], who proved
> $F_2(N)=\left(\frac{6}{\pi^2}+o(1)\right)N$, $F_3(N) = (1-o(1))N$, and also established
> asymptotics for $F_k(N)$ for all even $k\geq 4$ (in particular $F_k(N)\asymp N/\log N$ for all
> even $k\geq 4$). Erdős [Er38] earlier proved that $F_4(N)=o(N)$ - indeed, if
> $\lvert A\rvert \gg N$ and $A\subseteq \{1,\ldots,N\}$ then there is a non-trivial solution to
> $ab=cd$ with $a,b,c,d\in A$.
>
> This problem was answered in the negative by Tao [Ta24], who proved that for any $k\geq 4$ there
> is some constant $c_k>0$ such that $F_k(N) \leq (1-c_k+o(1))N$.
>
> See also [888](https://www.erdosproblems.com/888).

```lean
theorem erdos_121 : ¬ (fun N : ℕ => (F 5 N : ℝ)) ~[atTop] fun N : ℕ => (N : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/121.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/121.lean#L69).

## `Erdos121.erdos_121.variants.odd`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos121.lean#L87](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos121.lean#L87).

> More generally, is $F_{2k+1}(N)=(1-o(1))N$? This is false for all $k \geq 2$ by Tao's
> theorem [Ta24].

```lean
theorem erdos_121.variants.odd : ¬ ∀ k : ℕ, 1 ≤ k →
    (fun N : ℕ => (F (2 * k + 1) N : ℝ)) ~[atTop] fun N : ℕ => (N : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/121.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/121.lean#L77).

## `Erdos121.erdos_121.variants.tao`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos121.lean#L87](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos121.lean#L87).

> Tao [Ta24] proved that for any $k\geq 4$ there is some constant $c_k>0$ such that
> $F_k(N) \leq (1-c_k+o(1))N$.

```lean
theorem erdos_121.variants.tao (k : ℕ) (hk : 4 ≤ k) :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ N : ℕ in atTop, (F k N : ℝ) ≤ (1 - c) * N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/121.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/121.lean#L86).

## `Erdos121.erdos_121.variants.three`

Solved: stated here without proof.

> Erdős, Sós, and Sárközy [ESS95] proved $F_3(N) = (1-o(1))N$.

```lean
theorem erdos_121.variants.three : (fun N : ℕ => (F 3 N : ℝ)) ~[atTop] fun N : ℕ => (N : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/121.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/121.lean#L92).

## `Erdos121.erdos_121.variants.two`

Solved: stated here without proof.

> Erdős, Sós, and Sárközy [ESS95] proved $F_2(N)=\left(\frac{6}{\pi^2}+o(1)\right)N$.

```lean
theorem erdos_121.variants.two :
    (fun N : ℕ => (F 2 N : ℝ)) ~[atTop] fun N : ℕ => 6 / Real.pi ^ 2 * N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/121.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/121.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/121.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/121.lean)
- [erdosproblems.com/121](https://www.erdosproblems.com/121)
