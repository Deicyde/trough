---
declaration: theorem
origin: cited
lean: Erdos1072.erdos_1072.parts.i, Erdos1072.erdos_1072.parts.ii, Erdos1072.erdos_1072.variants.littleo
statement: formalized
---

# Erdős Problem 1072

> *Reference:* [erdosproblems.com/1072](https://www.erdosproblems.com/1072)

*Quoted from [FormalConjectures/ErdosProblems/1072.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1072.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1072](https://www.erdosproblems.com/1072).

The file states 3 research or textbook statements: 3 open.

## `Erdos1072.erdos_1072.parts.i`

Open: stated without proof.

> Is it true that there are infinitely many $p$ for which $f(p) = p − 1$?

```lean
theorem erdos_1072.parts.i : Set.Infinite {p | p.Prime ∧ f p = p - 1}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1072.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1072.lean#L38).

## `Erdos1072.erdos_1072.parts.ii`

Open: stated without proof.

> Is it true that $f(p)/p \to 0$ for $p \to \infty$ in a density 1 subset of the primes?

```lean
theorem erdos_1072.parts.ii :
    ∃ (P : Set ℕ), P ⊆ {p | p.Prime} ∧ P.HasDensity 1 {p | p.Prime} ∧
      Tendsto (fun p => (f p / p : ℝ)) (atTop ⊓ principal P) (𝓝 0)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1072.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1072.lean#L43).

## `Erdos1072.erdos_1072.variants.littleo`

Open: stated without proof.

> Erdős, Hardy, and Subbarao [HaSu02], believed that the number of $p \le x$ for which $f(p)=p−1$
> is $o(x/\log x)$.
>
> [HaSu02] Hardy, G. E. and Subbarao, M. V., _A modified problem of Pillai and some related questions._
> Amer. Math. Monthly (2002), 554--559.

```lean
theorem erdos_1072.variants.littleo :
    (fun x ↦ (({p | p.Prime ∧ f p = p - 1} ∩ Icc 0 x).ncard : ℝ)) =o[atTop]
      (fun x ↦ x / Real.log x)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1072.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1072.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1072.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1072.lean)
- [erdosproblems.com/1072](https://www.erdosproblems.com/1072)
