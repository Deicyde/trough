---
declaration: theorem
origin: cited
lean: Erdos961.erdos_961.sylvester_schur, Erdos961.erdos_961.variants.well_defined, Erdos961.erdos_961, Erdos961.erdos_961.variants.erdos_upper_bound, Erdos961.erdos_961.variants.jutila_ramachandra_shorey_upper_bound
statement: formalized
---

# Erdős Problem 961

> *References:*
> - [erdosproblems.com/961](https://www.erdosproblems.com/961)
> - [Ju74] Jutila, Matti, On numbers with a large prime factor. {II}. J. Indian Math. Soc. (N.S.) (1974), 125--130.
> - [RaSh73](https://eudml.org/doc/urn:eudml:doc:205214) Ramachandra, K. and Shorey, T. N., On gaps between numbers with a large prime factor. Acta Arith. (1973), 99--111.

*Quoted from [FormalConjectures/ErdosProblems/961.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/961.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/961](https://www.erdosproblems.com/961).

The file states 5 research or textbook statements: 1 open and 4 solved. It also has 1 test statement, counted here but not shown.

## `Erdos961.erdos_961.sylvester_schur`

Solved: stated here without proof.

> Sylvester and Schur [Er34] proved that every set of $k$ consecutive integers greater than $k$
> contains an integer divisible by a prime greater than $k$, i.e. not $(k+1)$-smooth.

```lean
theorem erdos_961.sylvester_schur (k : ℕ) (hk : 0 < k) : Erdos961Prop k k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/961.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/961.lean#L43).

## `Erdos961.erdos_961.variants.well_defined`

Proved here.

> There exists $n$ such that `Erdos961Prop k n` holds.

```lean
theorem erdos_961.variants.well_defined (k : ℕ) (hk : 0 < k): ∃ n, Erdos961Prop k n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/961.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/961.lean#L60).

## `Erdos961.erdos_961`

Open: stated without proof.

> It is conjectured that $f(k) \ll (\log k)^O(1)$.

```lean
theorem erdos_961 : ∃ C : ℕ, ∀ᶠ k : ℕ in atTop, f k < log k ^ C
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/961.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/961.lean#L76).

## `Erdos961.erdos_961.variants.erdos_upper_bound`

Solved: stated here without proof.

> Erdos [Er55d] proved $f(k) < 3 \frac{k}{\log k}$ for sufficiently large $k$.

```lean
theorem erdos_961.variants.erdos_upper_bound :
    ∀ᶠ k in atTop, f k < 3 * k / log k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/961.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/961.lean#L83).

## `Erdos961.erdos_961.variants.jutila_ramachandra_shorey_upper_bound`

Solved: stated here without proof.

> Jutila [Ju74], and Ramachandra--Shorey [RaSh73] proved a stronger upper bound
> $f(k) \ll \frac{\log \log \log k}{\log \log k} \frac{k}{\log k}$.

```lean
theorem erdos_961.variants.jutila_ramachandra_shorey_upper_bound :
    (fun k => (f k : ℝ)) =O[atTop] fun k => log (log (log k)) / log (log k) * (k / log k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/961.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/961.lean#L92).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/961.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/961.lean)
- [erdosproblems.com/961](https://www.erdosproblems.com/961)
