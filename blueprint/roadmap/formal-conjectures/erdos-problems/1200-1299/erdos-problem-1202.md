---
declaration: theorem
origin: cited
lean: Erdos1202.erdos_1202
statement: formalized
---

# Erdős Problem 1202

> *References:*
> - [erdosproblems.com/1202](https://www.erdosproblems.com/1202)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.
> - [Gr24] [Ben Green's 100 Open Problems, Problem 44](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.44)

*Quoted from [FormalConjectures/ErdosProblems/1202.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1202.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1202](https://www.erdosproblems.com/1202).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1202.erdos_1202`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1202.lean](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1202.lean).

> Let $\epsilon > 0$. Does there exist $k$ such that, for every $n$, any primes
> $p_1 < \cdots < p_k < n^{1-\epsilon}$ and any sets $A_i$ of $\frac{p_i - 1}{2}$ residue classes
> modulo $p_i$, the number of $m \le n$ that avoid $A_i \pmod{p_i}$ for every $i$ is at most
> $\epsilon n$?
>
> The answer is negative: according to [erdosproblems.com/1202](https://www.erdosproblems.com/1202),
> Price (with GPT-5.4 Pro) gave a construction in which the $A_i$ are intervals of residues and at
> least $(1/2 - c) n$ integers in $[1, n]$ survive. The large sieve gives a positive answer when
> $p_k < n^{1/2}$ instead. See also `Green44` for a related special case.

```lean
theorem erdos_1202 :
    ¬ ∀ ε : ℝ, 0 < ε → ∃ k : ℕ, ∀ (n : ℕ) (p : Fin k → ℕ) (A : (i : Fin k) → Finset (ZMod (p i))),
      (∀ i, (p i).Prime) →
      StrictMono p →
      (∀ i, (p i : ℝ) < (n : ℝ) ^ (1 - ε)) →
      (∀ i, (A i).card = (p i - 1) / 2) →
      ((((Finset.Icc 1 n).filter (fun m => ∀ i, (m : ZMod (p i)) ∉ A i)).card : ℕ) : ℝ) ≤ ε * n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1202.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1202.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1202.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1202.lean)
- [erdosproblems.com/1202](https://www.erdosproblems.com/1202)
