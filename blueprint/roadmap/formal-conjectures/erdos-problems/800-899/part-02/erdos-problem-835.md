---
declaration: theorem
origin: cited
lean: Erdos835.erdos_835, Erdos835.erdos_835.variants.johnson, Erdos835.johnsonGraph_2k_k_chromaticNumber_known_cases, Erdos835.johnsonGraph_18_9_chromaticNumber, Erdos835.indepNum_johnson_le_johnsonBound, Erdos835.div_johnsonBound_le_chromaticNum_johnson, Erdos835.chromaticNumber_johnson_2k_k_lower_bound, Erdos835.chromaticNumber_johnson_2k_k_lower_bound_odd, Erdos835.johnson_chromaticNumber_odd, Erdos835.johnson_chromaticNumber_composite, Erdos835.johnson_chromaticNumber
statement: formalized
---

# Erdős Problem 835

> *References:*
>  - [erdosproblems.com/835](https://www.erdosproblems.com/835)
>  - [MT25](https://github.com/QuanyuTang/erdos-problem-835/blob/main/On_Problem_835.pdf)

*Quoted from [FormalConjectures/ErdosProblems/835.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/835.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/835](https://www.erdosproblems.com/835).

The file states 11 research or textbook statements: 3 open and 8 solved. It also has 2 test statements, counted here but not shown.

## `Erdos835.erdos_835`

Open: stated without proof.

> Does there exist a $k>2$ such that the $k$-sized subsets of {1,...,2k} can be coloured with
> $k+1$ colours such that for every $A\subset \{1,\ldots,2k\}$ with $\lvert A\rvert=k+1$ all $k+1$
> colours appear among the $k$-sized subsets of $A$?

```lean
theorem erdos_835 : ∃ k > 2, Property k
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/835.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/835.lean#L52).

## `Erdos835.erdos_835.variants.johnson`

Open: stated without proof.

> Alternative statement of Erdős Problem 835 using the chromatic number of the Johnson graph.
> This is equivalent to asking whether there exists $k > 2$ such that the chromatic number of the
> Johnson graph $J(2k, k)$ is $k+1$.

```lean
theorem erdos_835.variants.johnson : ∃ l,
    -- making sure k > 2
    letI k := l + 3
    J(2 * k, k).chromaticNumber = k + 1
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/835.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/835.lean#L69).

## `Erdos835.johnsonGraph_2k_k_chromaticNumber_known_cases`

Solved: stated here without proof.

> It is known that for $3 \leq k \leq 8$, the chromatic number of $J(2k, k)$ is greater than $k+1$,
> see [Johnson graphs](https://aeb.win.tue.nl/graphs/Johnson.html).

```lean
theorem johnsonGraph_2k_k_chromaticNumber_known_cases (k : ℕ) (hk : 3 ≤ k) (hk' : k ≤ 8) :
    J(2 * k, k).chromaticNumber > k + 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/835.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/835.lean#L80).

## `Erdos835.johnsonGraph_18_9_chromaticNumber`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000008](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000008).

> The smallest case not on this page is $k=9$:
> But that one can be solved as well:
> The chromatic number of $J(18, 9)$ is at least $11$.

```lean
theorem johnsonGraph_18_9_chromaticNumber : J(18, 9).chromaticNumber > 9 + 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/835.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/835.lean#L92).

## `Erdos835.indepNum_johnson_le_johnsonBound`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-06-000013](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-06-000013).

> Johnson's bound for the independence number of the Johnson graph.

```lean
lemma indepNum_johnson_le_johnsonBound : α(J(n, k)) ≤ johnsonBound n 4 k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/835.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/835.lean#L107).

## `Erdos835.div_johnsonBound_le_chromaticNum_johnson`

Proved here.

> Johnson's bound for the chromatic number of the Johnson graph.

```lean
lemma div_johnsonBound_le_chromaticNum_johnson :
    ⌈(n.choose k / johnsonBound n 4 k : ℚ≥0)⌉₊ ≤ χ(J(n, k))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/835.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/835.lean#L111).

## `Erdos835.chromaticNumber_johnson_2k_k_lower_bound`

Solved: stated here without proof.

> It is known that for $3 \leq k \leq 8$, the chromatic number of $J(2k, k)$ is greater than
> $k+1$, see [Johnson graphs](https://aeb.win.tue.nl/graphs/Johnson.html).

```lean
theorem chromaticNumber_johnson_2k_k_lower_bound (hk : 3 ≤ k) (hk' : k ≤ 8) :
    k + 1 < J(2 * k, k).chromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/835.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/835.lean#L122).

## `Erdos835.chromaticNumber_johnson_2k_k_lower_bound_odd`

Proved here.

> It is also known that for $3 \leq k \leq 203$ odd, the chromatic number of $J(2k, k)$ is
> greater than $k+1$, see [Johnson graphs](https://aeb.win.tue.nl/graphs/Johnson.html).

```lean
theorem chromaticNumber_johnson_2k_k_lower_bound_odd (hk : 3 ≤ k) (hk' : k ≤ 300) (hk_odd : Odd k) :
    k + 1 < J(2 * k, k).chromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/835.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/835.lean#L129).

## `Erdos835.johnson_chromaticNumber_odd`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000008](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000008).

> It can be seen that the chromatic number of $J(2k,k)$ is $>k+1$ for all odd $k>2$.

```lean
theorem johnson_chromaticNumber_odd (k : ℕ) (hk : 2 < k) (h : Odd k) :
    k + 1 < J(2 * k, k).chromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/835.lean, line 140](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/835.lean#L140).

## `Erdos835.johnson_chromaticNumber_composite`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000008](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000008).

> Ma and Tang have proved that the chromatic number of $J(2k,k)$ is $>k+1$ for all $k>2$ not of the
> form $p-1$ for prime $p$.

```lean
theorem johnson_chromaticNumber_composite (k : ℕ) (hk : 2 < k) (h : (k + 1).Composite) :
    k + 1 < J(2 * k, k).chromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/835.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/835.lean#L151).

## `Erdos835.johnson_chromaticNumber`

Open: stated without proof.

> Is the chromatic number of `J(2 * k, k)` always at least `k + 2`?

```lean
theorem johnson_chromaticNumber :
    ∀ k ≥ 3, k + 2 ≤ J(2 * k, k).chromaticNumber
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/835.lean, line 171](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/835.lean#L171).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/835.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/835.lean)
- [erdosproblems.com/835](https://www.erdosproblems.com/835)
