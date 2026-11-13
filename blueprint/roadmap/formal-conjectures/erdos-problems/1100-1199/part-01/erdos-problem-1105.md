---
declaration: theorem
origin: cited
lean: Erdos1105.erdos_1105.parts.i, Erdos1105.erdos_1105.parts.ii
statement: formalized
---

# Erdős Problem 1105

> *References:*
> - [erdosproblems.com/1105](https://www.erdosproblems.com/1105)
> - [PALOMAR-2026-10-13-000006](https://palomar-registry.org/entry.html?id=PALOMAR-2026-10-13-000006&version=1)
> - [ESS75] Erdős, P. and Simonovits, M. and Sós, V. T., Anti-{R}amsey theorems. (1975), 633--643.
> - [MoNe05] Montellano-Ballesteros, J. J. and Neumann-Lara, V., An anti-{R}amsey theorem on cycles.
>   Graphs Combin. (2005), 343--354.
> - [SiSo84] Simonovits, Miklós and Sós, Vera T., On restricted colourings of {$K_n$}. Combinatorica
>   (1984), 101--110.
> - [Yu21] L.-T. Yuan, The anti-Ramsey number for paths. arXiv:2102.00807 (2021).

*Quoted from [FormalConjectures/ErdosProblems/1105.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1105.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1105](https://www.erdosproblems.com/1105).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1105.erdos_1105.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/ba96303b34a95ac458958c1eb0bbdee54733484a/erdos-1105/Solution.lean#L72](https://github.com/linrock/math-proofs/blob/ba96303b34a95ac458958c1eb0bbdee54733484a/erdos-1105/Solution.lean#L72).

> The anti-Ramsey number $\mathrm{AR}(n,G)$ is the maximum possible number of colours in which the
> edges of $K_n$ can be coloured without creating a rainbow copy of $G$ (i.e. one in which all edges
> have different colours).
>
> Let $C_k$ be the cycle on $k$ vertices. Is it true that
> $\mathrm{AR}(n,C_k)=\left(\frac{k-2}{2}+\frac{1}{k-1}\right)n+O(1)$?
>
> Montellano-Ballesteros and Neumann-Lara [MoNe05] gave an exact formula for $\mathrm{AR}(n,C_k)$,
> which implies in particular that
> $\mathrm{AR}(n,C_k)=\left(\frac{k-2}{2}+\frac{1}{k-1}\right)n+O(1).$

```lean
theorem erdos_1105.parts.i :
    ∀ k, 3 ≤ k →
    ((fun n => (antiRamseyNum (cycleGraph k) n : ℝ) - ((k - 2 : ℝ) / 2 + 1 / (k - 1)) * n)
      =O[atTop] (fun _ => (1 : ℝ)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1105.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1105.lean#L55).

## `Erdos1105.erdos_1105.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/ba96303b34a95ac458958c1eb0bbdee54733484a/erdos-1105/Solution.lean#L79](https://github.com/linrock/math-proofs/blob/ba96303b34a95ac458958c1eb0bbdee54733484a/erdos-1105/Solution.lean#L79).

> Let $P_k$ be the path on $k$ vertices and $\ell=\lfloor\frac{k-1}{2}\rfloor$. If $n\geq k\geq 5$
> then is $\mathrm{AR}(n,P_k)$ equal to $\max\left(\binom{k-2}{2}+1,
> \binom{\ell-1}{2}+(\ell-1)(n-\ell+1)+\epsilon\right)$where $\epsilon=1$ if $k$ is odd and
> $\epsilon=2$ otherwise?
>
> A proof of the formula for $\mathrm{AR}(n,P_k)$ for all $n\geq k\geq 5$ has been announced by
> Yuan [Yu21].

```lean
theorem erdos_1105.parts.ii :
    ∀ (k n : ℕ), 5 ≤ k → k ≤ n →
    let ℓ := (k - 1) / 2
    let ε := if Odd k then 1 else 2
    antiRamseyNum (pathGraph k) n = max ((k - 2).choose 2 + 1) ((ℓ - 1).choose 2 +
      (ℓ - 1) * (n - ℓ + 1) + ε)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1105.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1105.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1105.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1105.lean)
- [erdosproblems.com/1105](https://www.erdosproblems.com/1105)
