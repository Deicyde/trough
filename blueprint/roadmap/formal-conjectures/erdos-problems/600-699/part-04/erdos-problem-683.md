---
declaration: theorem
origin: cited
lean: Erdos683.erdos_683, Erdos683.erdos_683.variant.sylvester_schur, Erdos683.erdos_683.variant.erdos_log, Erdos683.erdos_683.variant.exp_sqrt
statement: formalized
---

# Erdős Problem 683

> *References:*
> - [erdosproblems.com/683](https://www.erdosproblems.com/683)
> - [Er34] Erdős, Paul, A Theorem of Sylvester and Schur. J. London Math. Soc. (1934), 282--288.
> - [Er55d] Erdős, P., On consecutive integers. Nieuw Arch. Wisk. (3) (1955), 124--128.
> - [Er79d] Erdős, P., Some unconventional problems in number theory. Acta Math. Acad. Sci. Hungar. (1979), 71-80.

*Quoted from [FormalConjectures/ErdosProblems/683.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/683.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/683](https://www.erdosproblems.com/683).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos683.erdos_683`

Open: stated without proof.

> Let $P(n, k)$ be the largest prime factor of $\binom{n}{k}$.
> There exists $c > 0$ such that $P(n, k) \ge \min(n - k + 1, k^{1 + c})$ for all $0 < k \le n/2$.
>
> Erdős stated this for $1 \le k \le n$ with the bound $\min(n-k+1, k^{1+c})$ [Er79d]. The
> minimum is needed even for $k \le n/2$: at $n = 2k$ every prime factor of $\binom{2k}{k}$ is at
> most $2k$, so $P(n, k) \ge k^{1+c}$ fails for large $k$. The range $k \le n/2$ is natural
> (cf. [#961](https://www.erdosproblems.com/961) and the
> [discussion](https://www.erdosproblems.com/forum/discuss/683)).

```lean
theorem erdos_683 :
    ∃ c > (0 : ℝ), ∀ n k : ℕ, 0 < k ∧ k ≤ n / 2 →
      (P n k : ℝ) ≥ min (↑(n - k + 1) : ℝ) ((k : ℝ) ^ (1 + c))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/683.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/683.lean#L54).

## `Erdos683.erdos_683.variant.sylvester_schur`

Solved: stated here without proof.

> Sylvester and Schur [Er34] proved that $P(n, k) > k$ for $k \le n/2$.

```lean
theorem erdos_683.variant.sylvester_schur :
    ∀ n k : ℕ, 0 < k ∧ k ≤ n / 2 → P n k > k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/683.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/683.lean#L63).

## `Erdos683.erdos_683.variant.erdos_log`

Solved: stated here without proof.

> Erdős [Er55d] improved this to $P(n, k) \gg \min(n - k + 1, k \log k)$ for $k \le n/2$. The
> minimum cannot be dropped: at $n = 2k$ one has $P(n, k) \le 2k$.

```lean
theorem erdos_683.variant.erdos_log :
    ∃ c > 0, ∀ n k : ℕ, 0 < k ∧ k ≤ n / 2 →
      (P n k : ℝ) ≥ min (↑(n - k + 1) : ℝ) (c * k * Real.log k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/683.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/683.lean#L72).

## `Erdos683.erdos_683.variant.exp_sqrt`

Open: stated without proof.

> Standard heuristics suggest that $P(n, k) > \min(n - k + 1, e^{c\sqrt{k}})$ for some constant
> $c > 0$.

```lean
theorem erdos_683.variant.exp_sqrt :
    ∃ c > 0, ∀ n k : ℕ, 0 < k ∧ k ≤ n / 2 →
      (P n k : ℝ) > min (↑(n - k + 1) : ℝ) (Real.exp (c * Real.sqrt k))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/683.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/683.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/683.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/683.lean)
- [erdosproblems.com/683](https://www.erdosproblems.com/683)
