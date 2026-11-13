---
declaration: theorem
origin: cited
lean: Erdos556.erdos_556, Erdos556.erdos_556.variants.luczak_asymptotic, Erdos556.erdos_556.variants.luczak_asymptotic_even, Erdos556.erdos_556.variants.odd_lower_bound, Erdos556.erdos_556.variants.kss_large_odd, Erdos556.erdos_556.variants.benevides_skokan_large_even
statement: formalized
---

# Erdős Problem 556

> A problem of Bondy and Erdős: for the cycle $C_n$ with $n \ge 4$, the $3$-colour Ramsey number
> satisfies
>
> $$R(C_n; 3) \le 4n - 3.$$
>
> The triangle is excluded: $C_3 = K_3$ and $R(K_3; 3) = 17 > 9$ [Rad]. The bound is best possible for odd $n$, where equality is conjectured (and known for large odd
> $n$). Łuczak proved the asymptotic bound $R(C_n; 3) \le (4 + o(1))n$, and $(3 + o(1))n$ for even
> $n$; Kohayakawa, Simonovits and Skokan settled large odd $n$, and Benevides and Skokan large even
> $n$, but the inequality for all $n$ remains open.
>
> *References:*
> - [erdosproblems.com/556](https://www.erdosproblems.com/556)
> - [Er81] P. Erdős, *On the combinatorial problems which I would most like to see solved*,
>   Combinatorica 1 (1981), 25-42.
> - [Lu99] T. Łuczak, *$R(C_n, C_n, C_n) \le (4 + o(1))n$*, J. Combin. Theory Ser. B 75 (1999),
>   174-187.
> - [KSS05] Y. Kohayakawa, M. Simonovits, J. Skokan, *The 3-colored Ramsey number of odd cycles*,
>   Proceedings of GRACO2005 (2005), 397-402.
> - [BeSk09] F. S. Benevides, J. Skokan, *The 3-colored Ramsey number of even cycles*, J. Combin.
>   Theory Ser. B 99 (2009), 690-708.
> - [Rad] S. P. Radziszowski, *Small Ramsey Numbers*, Electron. J. Combin. Dynamic Survey DS1,
>   revision 18, [p. 61](https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS1/pdf/#page=61).

*Quoted from [FormalConjectures/ErdosProblems/556.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/556.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/556](https://www.erdosproblems.com/556).

The file states 6 research or textbook statements: 1 open and 5 solved.

## `Erdos556.erdos_556`

Open: stated without proof.

> Erdős Problem 556 (Bondy–Erdős): for all $n \ge 4$,
>
> $$R(C_n; 3) \le 4n - 3.$$
>
> The case $n = 3$ is excluded since $R(K_3; 3) = 17$.

```lean
theorem erdos_556 (n : ℕ) (hn : 4 ≤ n) :
    multicolourRamsey (cycleGraph n) 3 ≤ 4 * n - 3
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/556.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/556.lean#L60).

## `Erdos556.erdos_556.variants.luczak_asymptotic`

Solved: stated here without proof.

> Łuczak's asymptotic bound [Lu99]: for every $\varepsilon > 0$, for all sufficiently large $n$,
>
> $$R(C_n; 3) \le (4 + \varepsilon)n.$$

```lean
theorem erdos_556.variants.luczak_asymptotic :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (multicolourRamsey (cycleGraph n) 3 : ℝ) ≤ (4 + ε) * n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/556.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/556.lean#L69).

## `Erdos556.erdos_556.variants.luczak_asymptotic_even`

Solved: stated here without proof.

> Łuczak's asymptotic bound for even $n$ [Lu99]: for every $\varepsilon > 0$, for all sufficiently
> large even $n$,
>
> $$R(C_n; 3) \le (3 + \varepsilon)n.$$

```lean
theorem erdos_556.variants.luczak_asymptotic_even :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, Even n →
      (multicolourRamsey (cycleGraph n) 3 : ℝ) ≤ (3 + ε) * n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/556.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/556.lean#L80).

## `Erdos556.erdos_556.variants.odd_lower_bound`

Solved: stated here without proof.

> For odd $n$ the bound $4n - 3$ is best possible: the $3$-colour Ramsey number is at least
> $4n - 3$, so equality holds whenever the conjectured upper bound does.

```lean
theorem erdos_556.variants.odd_lower_bound (n : ℕ) (hn : 3 ≤ n) (hodd : Odd n) :
    4 * n - 3 ≤ multicolourRamsey (cycleGraph n) 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/556.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/556.lean#L90).

## `Erdos556.erdos_556.variants.kss_large_odd`

Solved: stated here without proof.

> Kohayakawa, Simonovits and Skokan [KSS05] settled the conjecture for large odd $n$: for all
> sufficiently large odd $n$,
>
> $$R(C_n; 3) = 4n - 3.$$

```lean
theorem erdos_556.variants.kss_large_odd :
    ∀ᶠ n : ℕ in atTop, Odd n → multicolourRamsey (cycleGraph n) 3 = 4 * n - 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/556.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/556.lean#L100).

## `Erdos556.erdos_556.variants.benevides_skokan_large_even`

Solved: stated here without proof.

> Benevides and Skokan [BeSk09] settled the even case for large $n$: for all sufficiently large
> even $n$,
>
> $$R(C_n; 3) = 2n.$$

```lean
theorem erdos_556.variants.benevides_skokan_large_even :
    ∀ᶠ n : ℕ in atTop, Even n → multicolourRamsey (cycleGraph n) 3 = 2 * n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/556.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/556.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/556.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/556.lean)
- [erdosproblems.com/556](https://www.erdosproblems.com/556)
