---
declaration: theorem
origin: cited
lean: Erdos920.erdos_920, Erdos920.erdos_920.variants.upper_bound, Erdos920.erdos_920.variants.k_eq_3, Erdos920.erdos_920.variants.lower_bound_k_eq_4, Erdos920.erdos_920.variants.lower_bound_k_ge_5
statement: formalized
---

# Erdős Problem 920

> *References:*
> - [erdosproblems.com/166](https://www.erdosproblems.com/166)
> - [erdosproblems.com/920](https://www.erdosproblems.com/920)
> - [erdosproblems.com/986](https://www.erdosproblems.com/986)
> - [erdosproblems.com/1104](https://www.erdosproblems.com/1104)
> - [Br26] D. Brada\v{c}, Nearly tight exponents for off-diagonal Ramsey numbers. arXiv:2605.28793
>   (2026).
> - [Er69b] Erdős, P., Problems and results in chromatic graph theory. Proof Techniques in Graph
>   Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann Arbor, Mich., 1968) (1969), 27-35.
> - [GrYa68] Graver, Jack E. and Yackel, James, Some graph theoretic results associated with Ramsey's
>   theorem. J. Combinatorial Theory (1968), 125--175.
> - [MaVe23] Mattheus, S. and Verstraete, J., The asymptotics of $r(4,t)$. arXiv:2306.04007 (2023).

*Quoted from [FormalConjectures/ErdosProblems/920.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/920.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/920](https://www.erdosproblems.com/920).

The file states 5 research or textbook statements: 5 solved.

## `Erdos920.erdos_920`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos920.lean#L76](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos920.lean#L76).

> Is it true that, for $k\geq 4$, $f_k(n) \gg \frac{n^{1-\frac{1}{k-1}}}{(\log n)^{c_k}}$ for some
> constant $c_k>0$?
>
> This problem follows immediately from Mattheus and Verstraete's lower bound [MaVe23] for k = 4 and
> Bradač's lower bound [Br26] for k ≥ 5.

```lean
theorem erdos_920 :
    ∀ k : ℕ, k ≥ 4 → ∃ c > 0,
      (fun n ↦ f k n) ≫ (fun n ↦ (n : ℝ) ^ (1 - 1 / ((k : ℝ) - 1)) / (log n) ^ c)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/920.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/920.lean#L60).

## `Erdos920.erdos_920.variants.upper_bound`

Solved: stated here without proof.

> Graver and Yackel [GrYa68] proved that
> $f_k(n) \ll \left(n\frac{\log\log n}{\log n}\right)^{1-\frac{1}{k-1}}.$

```lean
theorem erdos_920.variants.upper_bound (k : ℕ) (hk : k ≥ 3) :
    (fun n ↦ f k n) ≪ (fun n ↦ ((n : ℝ) * log (log n) / log n) ^ (1 - 1 / ((k : ℝ) - 1)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/920.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/920.lean#L70).

## `Erdos920.erdos_920.variants.k_eq_3`

Solved: stated here without proof.

> It is known that $f_3(n)\asymp (n/\log n)^{1/2}$ (see [erdosproblems.com/1104]).

```lean
theorem erdos_920.variants.k_eq_3 :
    (fun n ↦ (f 3 n : ℝ)) =Θ[atTop] (fun n ↦ ((n : ℝ) / log n) ^ (1 / 2 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/920.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/920.lean#L78).

## `Erdos920.erdos_920.variants.lower_bound_k_eq_4`

Solved: stated here without proof.

> The lower bound $R(4,m) \gg m^3/(\log m)^4$ of Mattheus and Verstraete [MaVe23]
> (see [erdosproblems.com/166]) implies $f_4(n) \gg \frac{n^{2/3}}{(\log n)^{4/3}}$.

```lean
theorem erdos_920.variants.lower_bound_k_eq_4 :
    (fun n ↦ f 4 n) ≫ (fun n ↦ (n : ℝ) ^ (2 / 3 : ℝ) / (log n) ^ (4 / 3 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/920.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/920.lean#L87).

## `Erdos920.erdos_920.variants.lower_bound_k_ge_5`

Solved: stated here without proof.

> A positive answer to this question for all $k\geq 5$, i.e.
> $f_k(n) \gg \frac{n^{1-\frac{1}{k-1}}}{(\log n)^{c_k}}$ for some constant $c_k>0$, follows from
> the lower bound in [erdosproblems.com/986] given by Bradač [Br26].

```lean
theorem erdos_920.variants.lower_bound_k_ge_5 (k : ℕ) (hk : k ≥ 5) :
    ∃ c > 0, (fun n ↦ f k n) ≫ (fun (n : ℕ) ↦
    (n : ℝ) ^ (1 - 1 / ((k : ℝ) - 1)) / (log n) ^ c)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/920.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/920.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/920.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/920.lean)
- [erdosproblems.com/920](https://www.erdosproblems.com/920)
