---
declaration: theorem
origin: cited
lean: Erdos393.erdos_393, Erdos393.erdos_393.variants.infinitely_often_one, Erdos393.erdos_393.variants.berend_osgood, Erdos393.erdos_393.variants.bui_pratt_zaharescu, Erdos393.erdos_393.variants.luca
statement: formalized
---

# Erdős Problem 393

> *References:*
> - [erdosproblems.com/393](https://www.erdosproblems.com/393)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [BeOs92] Berend, Daniel and Osgood, Charles F., *On the equation $P(x)=n!$ and a question of
>   Erdős*. J. Number Theory 42 (1992), 189-193.
> - [BPZ23] Bui, Hung M. and Pratt, Kyle and Zaharescu, Alexandru, *Power savings for counting
>   solutions to polynomial-factorial equations*. Adv. Math. 422 (2023), Paper No. 109021, 32 pp.
>   [arXiv:2204.08423](https://arxiv.org/abs/2204.08423)
> - [Lu02] Luca, Florian, *The Diophantine equation $P(x)=n!$ and a result of M. Overholt*.
>   Glas. Mat. Ser. III 37 (2002), 269-273.
> - [OEIS A388302](https://oeis.org/A388302): the values $f(n)$ for $n \geq 2$.

*Quoted from [FormalConjectures/ErdosProblems/393.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/393.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/393](https://www.erdosproblems.com/393).

The file states 5 research or textbook statements: 2 open and 3 solved. It also has 5 test statements, counted here but not shown.

## `Erdos393.erdos_393`

Open: stated without proof.

> Let $f(n)$ denote the minimal $m\geq 1$ such that
>
> $$n! = a_1\cdots a_t$$
>
> with $a_1\lt \cdots \lt a_t=a_1+m$. What is the behaviour of $f(n)$?
>
> We formalise the question as: does $f(n) \to \infty$? A result of Luca [Lu02] implies a positive
> answer, conditional on the $abc$ conjecture (see `Erdos393.erdos_393.variants.luca`).

```lean
theorem erdos_393 : Tendsto f atTop atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/393.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/393.lean#L117).

## `Erdos393.erdos_393.variants.infinitely_often_one`

Open: stated without proof.

> Erdős and Graham [ErGr80, p. 76] write that they do not even know whether $f(n) = 1$ for infinitely
> many $n$, that is, whether a factorial is the product of two consecutive integers infinitely
> often.

```lean
theorem erdos_393.variants.infinitely_often_one :
    {n : ℕ | f n = 1}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/393.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/393.lean#L126).

## `Erdos393.erdos_393.variants.berend_osgood`

Solved: stated here without proof.

> Let $F_m(N)$ count the number of $n \leq N$ such that $f(n) = m$. A theorem of Berend and
> Osgood [BeOs92] implies that, for each fixed $m$, $F_m(N) = o(N)$, that is,
> $\{n : f(n) = m\}$ has natural density $0$.
>
> They proved that, for every $P \in \mathbb{Z}[x]$ of degree at least $2$, the set of $n$ such
> that $P(x) = n!$ has an integer solution has density $0$. For $m \geq 1$ this applies because
> $f(n) = m$ gives $n! = P(a_1)$ for one of the finitely many polynomials
> $P(x) = \prod_{j \in S} (x + j)$ with $\{0, m\} \subseteq S \subseteq \{0, \ldots, m\}$. For
> $m = 0$ the set is $\{0, 1\}$ (the junk values), so the statement is trivial.

```lean
theorem erdos_393.variants.berend_osgood (m : ℕ) :
    {n : ℕ | f n = m}.HasDensity 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/393.lean, line 142](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/393.lean#L142).

## `Erdos393.erdos_393.variants.bui_pratt_zaharescu`

Solved: stated here without proof.

> A theorem of Bui, Pratt, and Zaharescu [BPZ23] implies that, for each fixed $m$,
>
> $$F_m(N) \ll_m N^{33/34},$$
>
> where $F_m(N)$ is the number of $n \leq N$ such that $f(n) = m$.
>
> They proved that, for every $P \in \mathbb{Z}[x]$ of degree at least $2$, the number of
> $N \leq n < 2N$ such that $P(x) = n!$ has an integer solution is $\ll_P N^{33/34}$. Summing over
> the finitely many polynomials in `Erdos393.erdos_393.variants.berend_osgood` and over the dyadic
> ranges $[2^i, 2^{i+1})$ gives the bound for $n \leq N$.

```lean
theorem erdos_393.variants.bui_pratt_zaharescu (m : ℕ) :
    (fun N : ℕ ↦ (({n : ℕ | f n = m} ∩ Set.Iic N).ncard : ℝ)) =O[atTop]
      (fun N : ℕ ↦ (N : ℝ) ^ (33 / 34 : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/393.lean, line 157](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/393.lean#L157).

## `Erdos393.erdos_393.variants.luca`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-02-000011](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-02-000011).

> Luca [Lu02] proved that the $abc$ conjecture implies that, for every $P \in \mathbb{Z}[x]$ of
> degree at least $2$, the equation $P(x) = n!$ has only finitely many solutions. As remarked on
> erdosproblems.com, this implies that $f(n) \to \infty$, conditional on the $abc$ conjecture
> (`ABC.abc`).

```lean
theorem erdos_393.variants.luca (habc : type_of% ABC.abc) : Tendsto f atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/393.lean, line 170](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/393.lean#L170).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/393.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/393.lean)
- [erdosproblems.com/393](https://www.erdosproblems.com/393)
