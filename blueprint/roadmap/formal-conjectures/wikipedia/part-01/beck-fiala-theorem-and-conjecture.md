---
declaration: theorem
origin: cited
lean: BeckFiala.beck_fiala_theorem, BeckFiala.beck_fiala_conjecture
statement: formalized
---

# Beck–Fiala theorem and conjecture

> Discrepancy of bounded-degree set systems. Given sets $S_1, \dots, S_m \subseteq [n]$
> such that every element of $[n]$ belongs to at most $t$ of the sets (the system has
> *degree* at most $t$), one seeks a colouring $\chi \colon [n] \to \{-1, +1\}$ making
> every set as balanced as possible, i.e. minimizing the *discrepancy*
> $\max_i \left|\sum_{j \in S_i} \chi(j)\right|$.
>
> The Beck–Fiala theorem (1981) states that every set system of degree at most $t \ge 1$
> has discrepancy at most $2t - 1$. The Beck–Fiala conjecture asserts that the truth is
> much stronger: the discrepancy of a degree-$t$ system is $O(\sqrt{t})$, with a constant
> independent of $n$, $m$ and $t$.
>
> Despite considerable attention the bound $2t - 1$ has been improved only slightly:
> Bukh (2016) proved a bound of the form $2t - \log^* t$ (where $\log^*$ is the iterated
> logarithm), and Banaszczyk's vector balancing theorem yields $O(\sqrt{t \log n})$.
> The Komlós conjecture (see `KomlosConjecture.lean`) would imply the Beck–Fiala
> conjecture, since scaling the incidence vectors of a degree-$t$ system by $1/\sqrt{t}$
> produces vectors of Euclidean norm at most $1$.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Beck%E2%80%93Fiala_theorem)
> - [J. Beck and T. Fiala, *"Integer-making" theorems*,
>   Discrete Applied Mathematics **3** (1981), 1–8](https://doi.org/10.1016/0166-218X(81)90022-6)
> - [B. Bukh, *An improvement of the Beck–Fiala theorem*,
>   Combinatorics, Probability and Computing **25** (2016), 380–398](https://doi.org/10.1017/S0963548315000140)
> - [W. Banaszczyk, *Balancing vectors and Gaussian measures of n-dimensional convex bodies*,
>   Random Structures & Algorithms **12** (1998), 351–360](https://doi.org/10.1002/(SICI)1098-2418(199807)12:4%3C351::AID-RSA3%3E3.0.CO;2-S)

*Quoted from [FormalConjectures/Wikipedia/BeckFialaConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BeckFialaConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 test statement, counted here but not shown.

## `BeckFiala.beck_fiala_theorem`

Solved: stated here; a Lean proof is at [https://github.com/Lemmy00/beck-fiala-lean/blob/19334973121b07e428c51e15b914e9ca4921fbb9/BeckFialaProof/BeckFiala.lean#L35](https://github.com/Lemmy00/beck-fiala-lean/blob/19334973121b07e428c51e15b914e9ca4921fbb9/BeckFialaProof/BeckFiala.lean#L35).

> **The Beck–Fiala theorem**
>
> If $S_1, \dots, S_m \subseteq [n]$ is a set system of degree at most $t$, i.e. every
> $j \in [n]$ lies in at most $t$ of the sets, and $t \ge 1$, then there is a colouring
> $\chi \colon [n] \to \{-1, +1\}$ with $\left|\sum_{j \in S_i} \chi(j)\right| \le 2t - 1$
> for every $i$.
>
> The hypothesis $t \ge 1$ is necessary: a system of degree $0$ consists of empty sets
> only, whose discrepancy is $0 > 2 \cdot 0 - 1$.
>
> [J. Beck and T. Fiala, *"Integer-making" theorems*,
> Discrete Applied Mathematics **3** (1981), 1–8.]

```lean
theorem beck_fiala_theorem (n m t : ℕ) (ht : 1 ≤ t) (S : Fin m → Finset (Fin n))
    (hdeg : ∀ j, (Finset.univ.filter fun i => j ∈ S i).card ≤ t) :
    ∃ χ : Fin n → ℝ, (∀ j, χ j = 1 ∨ χ j = -1) ∧
      ∀ i, |∑ j ∈ S i, χ j| ≤ 2 * (t : ℝ) - 1
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/BeckFialaConjecture.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BeckFialaConjecture.lean#L73).

## `BeckFiala.beck_fiala_conjecture`

Open: stated without proof.

> **The Beck–Fiala conjecture**
>
> There exists a universal constant $C > 0$ such that every set system
> $S_1, \dots, S_m \subseteq [n]$ of degree at most $t$ admits a colouring
> $\chi \colon [n] \to \{-1, +1\}$ with
> $\left|\sum_{j \in S_i} \chi(j)\right| \le C \sqrt{t}$ for every $i$.

```lean
theorem beck_fiala_conjecture :
    ∃ C : ℝ, 0 < C ∧ ∀ (n m t : ℕ) (S : Fin m → Finset (Fin n)),
      (∀ j, (Finset.univ.filter fun i => j ∈ S i).card ≤ t) →
      ∃ χ : Fin n → ℝ, (∀ j, χ j = 1 ∨ χ j = -1) ∧
        ∀ i, |∑ j ∈ S i, χ j| ≤ C * Real.sqrt t
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/BeckFialaConjecture.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BeckFialaConjecture.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/BeckFialaConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BeckFialaConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Beck%E2%80%93Fiala_theorem)
