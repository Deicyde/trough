---
declaration: theorem
origin: cited
lean: Erdos477.erdos_477, Erdos477.erdos_477.variants.S_sq, Erdos477.erdos_477.variants.degree_two_dvd_condition_b_ne_zero, Erdos477.erdos_477.variants.X_pow_three, Erdos477.erdos_477.variants.monomial
statement: formalized
---

# Erdős Problem 477

> *References:*
> - [erdosproblems.com/477](https://www.erdosproblems.com/477)
> - [Sek59](http://dml.cz/dmlcz/100376) Milan Sekanina, Замечания к фактoризации беcкoнечнoй цикличеcкoй группы, Czechoslovak Mathematical Journal, Vol. 9 (1959), No. 4, 485–495
> - The resolution is recorded at [erdosproblems.com/477](https://www.erdosproblems.com/477), with a
>   proof exposition by T. F. Bloom of a construction found independently by several provers.

*Quoted from [FormalConjectures/ErdosProblems/477.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/477.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/477](https://www.erdosproblems.com/477).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos477.erdos_477`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos477.lean#L54](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos477.lean#L54).

> Is there a polynomial $f:\mathbb{Z}\to \mathbb{Z}$ of degree at least $2$ and a set
> $A\subset \mathbb{Z}$ such that for any $n\in \mathbb{Z}$ there is exactly one $a\in A$ and
> $b\in \{ f(k) : k\in\mathbb{Z}\}$ such that $n=a+b$?
>
> The answer is yes, contrary to the expectation of Erdős and Graham: such an `A` exists whenever
> $f(n) = n^d$ for even $d \ge 6$.
>
> The linked formal proof (Codex, following Price's exposition) exhibits a complement of
> $\{k^6 : k \in \mathbb{Z}\}$; it states uniqueness as `∃! p : ℤ × ℤ, p.1 ∈ A ∧ p.2 ∈ B ∧ p.1 + p.2 = n`
> and the degree condition as `2 ≤ f.natDegree`.

```lean
theorem erdos_477 :
    ∃ f : ℤ[X], 2 ≤ f.degree ∧ ∃ A : Set ℤ,
      ∀ z, ∃! ab ∈ A ×ˢ (Set.range f.eval), z = ab.1 + ab.2
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/ErdosProblems/477.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/477.lean#L51).

## `Erdos477.erdos_477.variants.S_sq`

Solved: stated here without proof.

> There is no such $A$ for the polynomial $f(x) = X^2$.
>
> This is shown in [Sek59].

```lean
theorem erdos_477.variants.S_sq :
    letI f := X ^ 2
    ∀ A : Set ℤ, ∃ z, ¬ ∃! a ∈ A ×ˢ (Set.range f.eval), z = a.1 + a.2
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/ErdosProblems/477.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/477.lean#L62).

## `Erdos477.erdos_477.variants.degree_two_dvd_condition_b_ne_zero`

Solved: stated here without proof.

> There is no such $A$ for any polynomial $f(x) = aX^2 + bX + c$, if $a | b$
> with $a \ne 0$ and $b \ne 0$.
> This was found be AlphaProof for the specific instance $X^2 - X + 1$ and then generalised.

```lean
theorem erdos_477.variants.degree_two_dvd_condition_b_ne_zero {a b c : ℤ} (ha : a ≠ 0) (hb : b ≠ 0)
    (hab : a ∣ b) :
    let f := a • X ^ 2 + b • X + C c
    ∀ A : Set ℤ, ∃ z, ¬ ∃! a ∈ A ×ˢ (Set.range f.eval), z = a.1 + a.2
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/ErdosProblems/477.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/477.lean#L73).

## `Erdos477.erdos_477.variants.X_pow_three`

Open: stated without proof.

> Probably there is no such $A$ for the polynomial $X^3$.

```lean
theorem erdos_477.variants.X_pow_three :
    letI f := X ^ 3
    ∀ A : Set ℤ, ∃ z, ¬ ∃! a ∈ A ×ˢ (Set.range f.eval), z = a.1 + a.2
```

Category `research open`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/ErdosProblems/477.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/477.lean#L83).

## `Erdos477.erdos_477.variants.monomial`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos477.lean#L42](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos477.lean#L42).

> Sekanina [Sek59] asked whether there is no such $A$ for $X^k$, for every $k \ge 2$.
> This is false: a complement exists for every even $k \ge 6$. The linked formal proof gives the
> case $k = 6$.

```lean
theorem erdos_477.variants.monomial :
    ¬ ∀ (k : ℕ), 2 ≤ k →
      letI f := X ^ k
      ∀ A : Set ℤ, ∃ z, ¬ ∃! a ∈ A ×ˢ (Set.range f.eval), z = a.1 + a.2
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/ErdosProblems/477.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/477.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/477.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/477.lean)
- [erdosproblems.com/477](https://www.erdosproblems.com/477)
