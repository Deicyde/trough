---
declaration: theorem
origin: cited
lean: ManickamMiklosSinghiConjecture.manickam_miklos_singhi_conjecture, ManickamMiklosSinghiConjecture.manickam_miklos_singhi_conjecture.variants.pokrovskiy, ManickamMiklosSinghiConjecture.manickam_miklos_singhi_conjecture.variants.quadratic
statement: formalized
---

# The Manickam–Miklós–Singhi conjecture (1988)

> *References:*
> * [MM88] Manickam, N. and Miklós, D. (1988). "On the number of nonnegative partial sums of a
>   nonnegative sum." *Colloq. Math. Soc. János Bolyai* 52, pp. 385--392.
> * [MS88] Manickam, N. and Singhi, N. M. (1988). "First distribution invariants and EKR theorems."
>   *J. Combin. Theory Ser. A* 48, pp. 91--103.
> * [CSS14] Chowdhury, A., Sarkis, G. and Shahriari, S. (2014). "The Manickam–Miklós–Singhi
>   conjectures for sets and vector spaces." *J. Combin. Theory Ser. A* 128, pp. 84--103.
>   [arXiv:1309.2212](https://arxiv.org/abs/1309.2212)
> * [Po15] Pokrovskiy, A. (2015). "A linear bound on the Manickam–Miklós–Singhi conjecture."
>   *J. Combin. Theory Ser. A* 133, pp. 280--306. [arXiv:1308.2176](https://arxiv.org/abs/1308.2176)

*Quoted from [FormalConjectures/Paper/ManickamMiklosSinghiConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ManickamMiklosSinghiConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `ManickamMiklosSinghiConjecture.manickam_miklos_singhi_conjecture`

Open: stated without proof.

> **The Manickam–Miklós–Singhi conjecture (1988).**
>
> If $n \ge 4k$ and $x_1, \dots, x_n$ are real numbers with $x_1 + \dots + x_n = 0$, then at least
> $\binom{n-1}{k-1}$ of the $k$-element subsets $S \subseteq \{1, \dots, n\}$ have
> $\sum_{i \in S} x_i \ge 0$. (The bound is attained by $x = (n-1, -1, \dots, -1)$; the
> condition $n \ge 4k$ cannot be weakened to $n \ge 3k + 1$ in general.)

```lean
theorem manickam_miklos_singhi_conjecture :
    ∀ (n k : ℕ), 1 ≤ k → 4 * k ≤ n → ∀ x : Fin n → ℝ, ∑ i, x i = 0 →
      (n - 1).choose (k - 1) ≤ nonnegSubsetCount n k x
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/ManickamMiklosSinghiConjecture.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ManickamMiklosSinghiConjecture.lean#L56).

## `ManickamMiklosSinghiConjecture.manickam_miklos_singhi_conjecture.variants.pokrovskiy`

Solved: stated here without proof.

> **Pokrovskiy (2015): the conjecture holds for $n \ge C k$ with an absolute constant $C$.**
>
> Pokrovskiy proved this with $C = 10^{46}$, the first bound linear in $k$.
>
> *Reference:* [Po15].

```lean
theorem manickam_miklos_singhi_conjecture.variants.pokrovskiy :
    ∃ C : ℕ, ∀ (n k : ℕ), 1 ≤ k → C * k ≤ n → ∀ x : Fin n → ℝ, ∑ i, x i = 0 →
      (n - 1).choose (k - 1) ≤ nonnegSubsetCount n k x
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/ManickamMiklosSinghiConjecture.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ManickamMiklosSinghiConjecture.lean#L69).

## `ManickamMiklosSinghiConjecture.manickam_miklos_singhi_conjecture.variants.quadratic`

Solved: stated here without proof.

> **Chowdhury–Sarkis–Shahriari (2014): the conjecture holds for $n \ge 8k^2$.**
>
> *Reference:* [CSS14].

```lean
theorem manickam_miklos_singhi_conjecture.variants.quadratic (n k : ℕ) (hk : 1 ≤ k)
    (hn : 8 * k ^ 2 ≤ n) (x : Fin n → ℝ) (hx : ∑ i, x i = 0) :
    (n - 1).choose (k - 1) ≤ nonnegSubsetCount n k x
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/ManickamMiklosSinghiConjecture.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ManickamMiklosSinghiConjecture.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/ManickamMiklosSinghiConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ManickamMiklosSinghiConjecture.lean)
- [arXiv:1309.2212](https://arxiv.org/abs/1309.2212)
