---
declaration: theorem
origin: cited
lean: Erdos976.erdos_976, Erdos976.erdos_976.parts.i, Erdos976.erdos_976.parts.ii, Erdos976.erdos_976.variants.nagell_ricci, Erdos976.erdos_976.variants.erdos, Erdos976.erdos_976.variants.tenenbaum
statement: formalized
---

# Erdős Problem 976

> *References:*
> - [erdosproblems.com/976](https://www.erdosproblems.com/976)
> - [Er52c] Erdős, P., *On the greatest prime factor of $\prod_{k=1}^x f(k)$*. J. London Math. Soc.
>   27 (1952), 379-384.
> - [Er65b] Erdős, P., *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
> - [Na22] Nagell, T., Abh. Math. Sem. Hamburg 1 (1922), 179-194.
> - [Ri34] Ricci, G., Annali di Mat. (1934), 295-303.
> - [Te90] Tenenbaum, G., *Sur une question d'Erdős et Schinzel*. A tribute to Paul Erdős (1990),
>   405-443.

*Quoted from [FormalConjectures/ErdosProblems/976.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/976.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/976](https://www.erdosproblems.com/976).

The file states 6 research or textbook statements: 3 open and 3 solved.

## `Erdos976.erdos_976`

Open: stated without proof.

> Let $f\in \mathbb{Z}[x]$ be an irreducible polynomial of degree $d\geq 2$. Let $F_f(n)$ be maximal
> such that there exists $1\leq m\leq n$ with $f(m)$ is divisible by a prime $\geq F_f(n)$.
> Equivalently, $F_f(n)$ is the greatest prime divisor of
>
> $$\prod_{1\leq m\leq n}f(m).$$
>
> Estimate $F_f(n)$.
>
> We read "estimate" as determining the order of magnitude of $F_f(n)$.

```lean
theorem erdos_976 (f : ℤ[X]) (hf : Irreducible f) (hd : 2 ≤ f.natDegree) :
    (fun n ↦ (F f n : ℝ)) =Θ[atTop] erdos_976.answer f
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/976.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/976.lean#L59).

## `Erdos976.erdos_976.parts.i`

Open: stated without proof.

> Let $f\in \mathbb{Z}[x]$ be an irreducible polynomial of degree $d\geq 2$, and let $F_f(n)$ be the
> greatest prime divisor of $\prod_{1\leq m\leq n}f(m)$. Is it true that $F_f(n)\gg n^{1+c}$ for some
> constant $c>0$?

```lean
theorem erdos_976.parts.i :
    ∀ f : ℤ[X], Irreducible f → 2 ≤ f.natDegree →
      ∃ c > (0 : ℝ), (fun n : ℕ ↦ (n : ℝ) ^ (1 + c)) =O[atTop] fun n ↦ (F f n : ℝ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/976.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/976.lean#L69).

## `Erdos976.erdos_976.parts.ii`

Open: stated without proof.

> Let $f\in \mathbb{Z}[x]$ be an irreducible polynomial of degree $d\geq 2$, and let $F_f(n)$ be the
> greatest prime divisor of $\prod_{1\leq m\leq n}f(m)$. Is it true that $F_f(n)\gg n^d$?

```lean
theorem erdos_976.parts.ii :
    ∀ f : ℤ[X], Irreducible f → 2 ≤ f.natDegree →
      (fun n : ℕ ↦ (n : ℝ) ^ f.natDegree) =O[atTop] fun n ↦ (F f n : ℝ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/976.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/976.lean#L79).

## `Erdos976.erdos_976.variants.nagell_ricci`

Solved: stated here without proof.

> Nagell [Na22] and Ricci [Ri34] proved that $F_f(n) \gg n\log n$.

```lean
theorem erdos_976.variants.nagell_ricci (f : ℤ[X]) (hf : Irreducible f)
    (hd : 2 ≤ f.natDegree) :
    (fun n : ℕ ↦ (n : ℝ) * Real.log n) =O[atTop] fun n ↦ (F f n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/976.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/976.lean#L88).

## `Erdos976.erdos_976.variants.erdos`

Solved: stated here without proof.

> Erdős [Er52c] improved the bound of Nagell and Ricci to
>
> $$F_f(n) \gg n(\log n)^{\log\log\log n}.$$
>
> More precisely, [Er52c] gives $F_f(n) > n(\log n)^{c\log\log\log n}$ for some constant
> $c = c(f) > 0$; the site omits $c$.

```lean
theorem erdos_976.variants.erdos (f : ℤ[X]) (hf : Irreducible f) (hd : 2 ≤ f.natDegree) :
    ∃ c > (0 : ℝ),
      (fun n : ℕ ↦ (n : ℝ) * Real.log n ^ (c * Real.log (Real.log (Real.log n)))) =O[atTop]
        fun n ↦ (F f n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/976.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/976.lean#L100).

## `Erdos976.erdos_976.variants.tenenbaum`

Solved: stated here without proof.

> In [Er65b] Erdős claimed a proof of $F_f(n) \gg n\exp((\log n)^c)$ for some constant $c>0$, but
> never published it. A proof was provided by Tenenbaum [Te90].

```lean
theorem erdos_976.variants.tenenbaum (f : ℤ[X]) (hf : Irreducible f) (hd : 2 ≤ f.natDegree) :
    ∃ c > (0 : ℝ), (fun n : ℕ ↦ (n : ℝ) * Real.exp (Real.log n ^ c)) =O[atTop]
      fun n ↦ (F f n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/976.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/976.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/976.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/976.lean)
- [erdosproblems.com/976](https://www.erdosproblems.com/976)
